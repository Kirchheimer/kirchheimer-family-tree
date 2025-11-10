# Data Entry Guide for Kirchheimer Family Tree

This guide outlines the standards and best practices for entering genealogical data into the Kirchheimer Family Tree repository.

## Table of Contents
1. [General Principles](#general-principles)
2. [Name Conventions](#name-conventions)
3. [Date Standards](#date-standards)
4. [Location Hierarchy](#location-hierarchy)
5. [Relationship Documentation](#relationship-documentation)
6. [Source Citation Format](#source-citation-format)
7. [Certainty Ratings](#certainty-ratings)
8. [Required Fields](#required-fields)
9. [Common Data Entry Tasks](#common-data-entry-tasks)
10. [Data Validation](#data-validation)

## General Principles

1. **Accuracy First**: Ensure all data is accurate and properly cited to reliable sources.

2. **Completeness**: Fill in all relevant fields, but don't make assumptions. Mark uncertain information with appropriate confidence levels.

3. **Consistency**: Use the same format and standards throughout the repository.

4. **Source Everything**: Every piece of information should be traceable to a source.

5. **Clarity**: Use clear, concise language. Avoid jargon when possible.

6. **Standardization**: Follow the established schemas and conventions in this guide.

## Name Conventions

### Primary Names
- Use the complete name as officially recorded
- Separate given names and surnames
- Use proper capitalization (not ALL CAPS)
- Include middle names or initials if recorded

### Example
```json
{
  "names": {
    "primary": {
      "given": "Samson Nathan",
      "surname": "Kirchheimer",
      "maiden": "",
      "nickname": "Sam"
    }
  }
}
```

### Alternative Names
- Include maiden names, Hebrew names, German names, and anglicized versions
- Mark the period during which each name was used (if known)
- Use the `alternative` array to list other names

### Example
```json
{
  "names": {
    "primary": {
      "given": "Hanna",
      "surname": "Rosenfeld",
      "maiden": "",
      "nickname": ""
    },
    "alternative": [
      {
        "given": "Hilde",
        "surname": "Neumann",
        "type": "maiden",
        "period": {
          "start": "1941-01-01",
          "end": ""
        }
      },
      {
        "given": "Hanna",
        "surname": "Kirchheimer",
        "type": "other",
        "period": {
          "start": "1928-01-01",
          "end": "1941-01-01"
        }
      }
    ]
  }
}
```

## Date Standards

### ISO 8601 Format
All dates should follow the ISO 8601 standard: YYYY-MM-DD

### Approximate Dates
- Use a question mark after the date for approximate dates (e.g., 1900-03-15?)
- For uncertain years only, use YYYY? (e.g., 1900?)

### Date Ranges
For uncertain dates or events spanning multiple dates, use a range:

```json
{
  "date_range": {
    "start": "1900-03-01",
    "end": "1900-03-31"
  }
}
```

### Example
```json
{
  "birth": {
    "date": "1872-08-10",
    "location": {
      "city": "Houston",
      "region": "Texas",
      "country": "USA"
    },
    "sources": ["family_record_001"]
  }
}
```

## Location Hierarchy

Record locations in a hierarchical structure from most specific to most general:

1. Address (if known)
2. Place (specific location name)
3. City/Town
4. Region (state, province, county)
5. Country

### Example
```json
{
  "location": {
    "address": "1817 Chestnut Street",
    "place": "Home of Samson Kirchheimer",
    "city": "Houston",
    "region": "Texas",
    "country": "USA"
  }
}
```

## Relationship Documentation

When documenting relationships:

1. Use the appropriate relationship type from the schema
2. Include certainty ratings for uncertain relationships
3. Always provide sources for relationships
4. For parent-child relationships, include the child in both parents' records

### Example
```json
{
  "parents": [
    {
      "relationship": "biological_father",
      "person_id": "person_001",
      "certainty": "certain",
      "sources": ["family_record_001"]
    }
  ],
  "spouses": [
    {
      "person_id": "person_002",
      "relationship_type": "spouse",
      "marriage_date": "1928-01-01",
      "certainty": "certain",
      "sources": ["family_record_002"]
    }
  ]
}
```

## Source Citation Format

Every piece of information should include a source reference. Use the following format for source IDs:

- `record_TYPE_###` (e.g., `record_birth_001`)
- Where TYPE is a shorthand for the source type (birth, death, census, etc.)
- And ### is a sequential number starting with 001

### Source Reference File
The full source information should be stored in the `family/sources` directory, with the source ID as the filename.

### Example
```json
{
  "birth": {
    "date": "1872-08-10",
    "sources": ["record_birth_001", "record_census_010"]
  }
}
```

## Certainty Ratings

Use certainty ratings to indicate your confidence level in the information:

- `certain`: There is no doubt about this information
- `very_likely`: Very high probability this is correct
- `likely`: Probable, but with some uncertainty
- `uncertain`: Significant uncertainty about this information

### Example
```json
{
  "birth": {
    "date": "1872-08-10?",
    "certainty": "likely",
    "sources": ["record_census_010"]
  }
}
```

## Required Fields

The following fields are required for all person records:
- id
- names.primary.given
- names.primary.surname

Other required fields depend on the information available:
- If birth information is known, then birth.date or birth.date_range is required
- If death information is known, then death.date or death.date_range is required
- For parents, either person_id or relationship must be provided

## Common Data Entry Tasks

### Adding a New Person
1. Create a new JSON file in the `family/individuals` directory
2. Use the person schema as a template
3. Include at least a name and an ID
4. Add any other known information
5. Make sure to include sources for all information

### Adding a Family Unit
1. Create a new JSON file in the `family/families` directory
2. Use the family schema as a template
3. Include partner references
4. Add children references
5. Include marriage information if known

### Documenting a Relationship
1. Update the person records for both individuals
2. Use the appropriate relationship type
3. Include certainty ratings
4. Add sources for the relationship

### Adding a Significant Event
1. Create a new JSON file in the `family/events` directory (if not already present)
2. Use the event schema as a template
3. Include participants
4. Add sources

## Data Validation

Before submitting any data changes:

1. Validate your JSON files against the appropriate schema
2. Check that all required fields are present
3. Verify that all referenced IDs exist
4. Ensure dates are in the correct format
5. Make sure locations follow the hierarchy

Use the validation tools in the `process/tools/validation` directory to check your data before submitting it.
