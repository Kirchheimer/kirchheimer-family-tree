# Kirchheimer Family Tree Data Structures

This directory contains JSON schema definitions for the Kirchheimer Family Tree repository data structures. These schemas define the structure, format, and constraints for all genealogical data stored in the repository.

## Schema Definitions

### Person Schema (`person_schema.json`)

The Person schema defines the structure for individual person records in the family tree. It includes fields for:

- Basic identification and name information
- Vital events (birth, death, burial)
- Relationships (parents, siblings, spouses, children)
- Life events and achievements (occupations, education, military service)
- Immigration records
- Notes and sources
- **Remote resources** (links to online genealogy services)

### Family Schema (`family_schema.json`)

The Family schema defines the structure for family unit records, which capture information about:

- Partners in a family relationship
- Children within the family
- Marriage and divorce information
- Family residences
- Significant family events
- Family notes and sources
- **Remote resources** (links to online genealogy services)

### Event Schema (`event_schema.json`)

The Event schema defines the structure for significant life events, including:

- Religious ceremonies
- Legal proceedings
- Medical events
- Social gatherings
- Political events
- Natural disasters
- Other notable occurrences
- **Remote resources** (links to online genealogy services)

## Implementation Notes

All schemas follow these principles:

1. **ISO 8601 Date Format**: All dates should be in the format YYYY-MM-DD. For approximate dates, use a question mark (e.g., 1900-03-15?) or a date range.

2. **Location Standardization**: Location information follows a hierarchical structure (country > region > city > place > address) to support both broad geographical context and specific location details.

3. **Source References**: All data should include references to the source documents that support the information, using the format defined in the repository's source schema.

4. **Certainty Rating**: For uncertain or approximate information, include a certainty rating to indicate confidence level.

5. **GEDCOM Compatibility**: Fields for GEDCOM IDs are included to maintain compatibility with genealogical data exchange standards.

6. **Remote Resources**: All schemas include a `remote_resources` field to allow linking to external genealogy services and databases.

## Validation

To validate data against these schemas, you can use the validation tools provided in the `process/tools/validation` directory.

## Extending the Schemas

The schemas are designed to be extensible. Additional properties can be added to the `additionalProperties` field in any object. For new fields that will be commonly used, consider proposing a schema update to ensure consistency across records.

## Versioning

These schemas are versioned to support backward compatibility. When making changes, always:

1. Create a new version of the schema file
2. Document the changes
3. Provide migration tools for existing data
4. Maintain a changelog of schema versions

## Example Records

See the examples directory for sample person, family, and event records that conform to these schemas.
