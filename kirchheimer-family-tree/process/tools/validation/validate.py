#!/usr/bin/env python3
"""
JSON Schema Validation Script

This script validates JSON files against the Kirchheimer Family Tree schemas.
"""

import os
import sys
import argparse
import json
from jsonschema import validate, ValidationError
import glob
import importlib.util

def load_schema(schema_path):
    """Load a JSON schema from a file."""
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading schema {schema_path}: {e}")
        return None

def validate_file(json_file, schema_path):
    """Validate a single JSON file against a schema."""
    # Load the schema
    schema = load_schema(schema_path)
    if not schema:
        return False, f"Could not load schema: {schema_path}"
    
    # Load the JSON file
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return False, f"Error loading JSON file {json_file}: {e}"
    
    # Validate the data
    try:
        validate(instance=data, schema=schema)
        return True, "Validation successful"
    except ValidationError as e:
        return False, f"Validation error: {e.message} at path {e.absolute_path}"

def validate_all_in_directory(directory, schema_path):
    """Validate all JSON files in a directory."""
    results = []
    json_files = glob.glob(os.path.join(directory, "*.json"))
    
    for json_file in json_files:
        is_valid, message = validate_file(json_file, schema_path)
        results.append({
            "file": json_file,
            "is_valid": is_valid,
            "message": message
        })
    
    return results

def determine_schema_type(file_path):
    """Determine the schema type based on the file path."""
    if "individuals" in file_path or "person" in file_path:
        return "person_schema.json"
    elif "families" in file_path or "family" in file_path:
        return "family_schema.json"
    elif "events" in file_path or "event" in file_path:
        return "event_schema.json"
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description="Validate Kirchheimer Family Tree JSON files against schemas.")
    parser.add_argument("path", help="Path to JSON file or directory containing JSON files")
    parser.add_argument("--schema", help="Path to specific schema file to use (optional)")
    args = parser.parse_args()
    
    if os.path.isfile(args.path):
        # Validate a single file
        if args.schema:
            is_valid, message = validate_file(args.path, args.schema)
            print(f"File: {args.path}")
            print(f"Schema: {args.schema}")
            print(f"Result: {'VALID' if is_valid else 'INVALID'}")
            print(f"Message: {message}")
        else:
            # Try to determine the schema type
            schema_type = determine_schema_type(args.path)
            if schema_type:
                schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                          "..", "..", "data_structure", schema_type)
                is_valid, message = validate_file(args.path, schema_path)
                print(f"File: {args.path}")
                print(f"Schema: {schema_type}")
                print(f"Result: {'VALID' if is_valid else 'INVALID'}")
                print(f"Message: {message}")
            else:
                print(f"Error: Could not determine schema type for {args.path}")
                sys.exit(1)
    elif os.path.isdir(args.path):
        # Validate all files in a directory
        results = []
        
        # Process person files
        individuals_dir = os.path.join(args.path, "individuals")
        if os.path.isdir(individuals_dir):
            schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                     "..", "..", "data_structure", "person_schema.json")
            if os.path.isfile(schema_path):
                for result in validate_all_in_directory(individuals_dir, schema_path):
                    result["schema"] = "person_schema.json"
                results.extend(validate_all_in_directory(individuals_dir, schema_path))
        
        # Process family files
        families_dir = os.path.join(args.path, "families")
        if os.path.isdir(families_dir):
            schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                     "..", "..", "data_structure", "family_schema.json")
            if os.path.isfile(schema_path):
                for result in validate_all_in_directory(families_dir, schema_path):
                    result["schema"] = "family_schema.json"
                results.extend(validate_all_in_directory(families_dir, schema_path))
        
        # Process event files
        events_dir = os.path.join(args.path, "events")
        if os.path.isdir(events_dir):
            schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                     "..", "..", "data_structure", "event_schema.json")
            if os.path.isfile(schema_path):
                for result in validate_all_in_directory(events_dir, schema_path):
                    result["schema"] = "event_schema.json"
                results.extend(validate_all_in_directory(events_dir, schema_path))
        
        # Print results
        valid_count = 0
        invalid_count = 0
        
        for result in results:
            if result["is_valid"]:
                valid_count += 1
                print(f"✓ VALID: {os.path.basename(result['file'])}")
            else:
                invalid_count += 1
                print(f"✗ INVALID: {os.path.basename(result['file'])}")
                print(f"  Schema: {result['schema']}")
                print(f"  Message: {result['message']}")
        
        print(f"\nSummary: {valid_count} valid, {invalid_count} invalid files")
        
        if invalid_count > 0:
            sys.exit(1)
    else:
        print(f"Error: {args.path} is not a valid file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
