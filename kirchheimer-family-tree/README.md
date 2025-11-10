# Kirchheimer Family Tree

The Kirchheimer Family Tree is a genealogical project to document and preserve the history of the Kirchheimer family and related families, including the Hanauer, Westheimer, and other family lines. This repository uses a structured, open-source approach to store, validate, and visualize family history data.

## Table of Contents
1. [Repository Overview](#repository-overview)
2. [Repository Structure](#repository-structure)
3. [Data Format](#data-format)
4. [Using the Repository](#using-the-repository)
5. [Visualization](#visualization)
6. [Validation](#validation)
7. [Documentation](#documentation)
8. [Contributing](#contributing)
9. [About the Kirchheimer Family](#about-the-kirchheimer-family)

## Repository Overview

The Kirchheimer Family Tree project is designed to:

1. **Preserve Family History**: Store genealogical data in a structured, standardized format
2. **Enable Collaboration**: Allow family members and researchers to contribute to and expand the family tree
3. **Ensure Data Quality**: Use validation tools to maintain data integrity
4. **Visualize Relationships**: Provide tools for creating visual representations of family relationships
5. **Document Sources**: Track all sources of information to maintain historical accuracy

## Repository Structure

```
kirchheimer-family-tree/
├── README.md                 # This file
├── CONTRIBUTING.md           # Contribution guidelines
├── family/                   # Family data directory
│   ├── individuals/         # Individual person records
│   ├── families/            # Family unit records
│   ├── events/              # Significant life events
│   ├── sources/             # Source information
│   └── images/              # Photos and documents
├── process/                  # Processing and documentation
│   ├── data_structure/      # JSON schema definitions
│   ├── documentation/       # Project documentation
│   ├── tools/               # Processing and validation tools
│   └── visualization/       # Visualization templates
```

## Data Format

The family tree data is stored in JSON format following standardized schemas:

- **Individuals**: Person records with biographical information
- **Families**: Family unit records with relationship information
- **Events**: Significant life events that involve multiple people

All data follows the Kirchheimer Family Tree JSON schemas defined in the `process/data_structure` directory. Data must be validated before contributing to the repository.

## Using the Repository

The repository is designed to be a collaborative genealogical resource. You can:

1. **Browse the Family Tree**: View individual records and family units
2. **Understand Relationships**: Use the visualization tools to see connections
3. **Contribute Data**: Add new family members, relationships, or correct information
4. **Validate Data**: Use the validation tools to ensure data quality
5. **View Sources**: Check the sources directory for reference documents

## Visualization

The repository includes visualization templates in the `process/visualization` directory:

- **Mermaid Diagrams**: Templates for creating family tree visualizations using the Mermaid library
- **Interactive Visualizations**: Tools for creating interactive family tree views

View the [Mermaid Templates](process/visualization/mermaid/kirchheimer_templates.md) for examples of how to create family tree diagrams.

## Validation

To ensure data quality, the repository includes validation tools in the `process/tools/validation` directory:

- **Schema Validation**: Ensures data follows the defined JSON schemas
- **Relationship Validation**: Checks that relationships are bidirectional and consistent
- **Data Conversion Tools**: Scripts for converting data from other formats (GEDCOM, CSV)

## Documentation

The repository includes comprehensive documentation in the `process/documentation` directory:

- **Data Entry Guide**: Guidelines for entering family tree data
- **API Documentation**: Documentation for data structures
- **Validation Tools**: Guides for using the validation tools

## Contributing

We welcome contributions to the Kirchheimer Family Tree project! Please see the [Contributing Guidelines](CONTRIBUTING.md) for detailed information on how to contribute.

## About the Kirchheimer Family

The Kirchheimer family traces its origins to Jewish communities in what is now Germany. The name "Kirchheimer" was adopted in 1809, when the Jewish community of Kirchheim was required to formalize their identities under Napoleonic rule.

The family includes the following branches:

1. **Main Kirchheimer Lineage**: Descended from Wolf Loew (c.1695-~1795)
2. **Hanauer Lineage**: Maternal line from the Hanauer family
3. **Westheimer Lineage**: Maternal line from the Westheimer family
4. **American Branch**: Immigration to the United States in the late 19th/early 20th century

The Kirchheimer family has contributed to various fields, including business, law, and public service. The project aims to document all these contributions and preserve them for future generations.
