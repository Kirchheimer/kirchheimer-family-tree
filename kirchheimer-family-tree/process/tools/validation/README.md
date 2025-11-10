# Data Processing Scripts

This directory contains scripts and tools for processing and validating Kirchheimer Family Tree data.

## Available Scripts

- [JSON Schema Validation](#json-schema-validation)
- [Data Conversion Tools](#data-conversion-tools)
- [Relationship Validation](#relationship-validation)

## JSON Schema Validation

This script validates JSON files against the Kirchheimer Family Tree schemas.

### Requirements
- Python 3.6+
- `jsonschema` Python library

### Usage
```
validate.py <path_to_json_file>
```

### Example
```bash
# Validate a single person file
python validate.py family/individuals/person_001.json

# Validate all person files
python validate.py family/individuals/

# Validate against a specific schema
python validate.py family/individuals/person_001.json --schema person_schema.json
```

## Data Conversion Tools

These scripts help convert data from other formats to the Kirchheimer Family Tree JSON format.

### GEDCOM to JSON
Converts GEDCOM files to the Kirchheimer Family Tree JSON format.

```bash
gedcom_to_json.py <path_to_gedcom_file> <output_directory>
```

### CSV to JSON
Converts CSV files to the Kirchheimer Family Tree JSON format.

```bash
csv_to_json.py <path_to_csv_file> <output_directory>
```

## Relationship Validation

This script validates that all relationships in the data are consistent and bidirectional.

```bash
validate_relationships.py <data_directory>
```

## Processing Workflows

### Standard Data Processing Workflow

1. **Import Data**
   - Use `gedcom_to_json.py` or `csv_to_json.py` to convert existing data
   - Store converted files in the appropriate directories

2. **Validate Data**
   - Use `validate.py` to check for syntax and schema compliance
   - Use `validate_relationships.py` to check relationship consistency

3. **Clean and Normalize**
   - Standardize names and dates
   - Normalize locations
   - Ensure all required fields are present

4. **Generate Reports**
   - Run any report generation scripts to check for data issues
   - Generate data quality reports

5. **Update Visualizations**
   - Use data processing to update Mermaid diagrams
   - Ensure visualizations stay in sync with the data
