# Contribution Guidelines for Kirchheimer Family Tree

Thank you for your interest in contributing to the Kirchheimer Family Tree project! These guidelines will help you get started and ensure that your contributions are effective and consistent with the project standards.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Types of Contributions](#types-of-contributions)
3. [How to Contribute](#how-to-contribute)
4. [Data Standards](#data-standards)
5. [Code of Conduct](#code-of-conduct)
6. [Repository Structure](#repository-structure)
7. [Testing and Validation](#testing-and-validation)
8. [Questions and Support](#questions-and-support)

## Getting Started

1. **Fork the Repository**
   - Create a fork of the main repository to your GitHub account
   - Clone your fork to your local machine

2. **Set Up Your Development Environment**
   - Install Python 3.6 or higher
   - Install the required Python packages with `pip install jsonschema`
   - Make sure you have Git installed and configured

3. **Create a Branch**
   - Create a new branch for your contribution
   - Use a descriptive name (e.g., `add-maria-kirchheimer`, `fix-german-locations`)

## Types of Contributions

We welcome various types of contributions to the Kirchheimer Family Tree:

1. **Data Contributions**
   - Adding new family members
   - Correcting existing information
   - Adding sources and documentation
   - Filling in missing information

2. **Documentation Contributions**
   - Improving existing documentation
   - Creating new guides or resources
   - Adding examples or templates

3. **Code Contributions**
   - Improving data processing scripts
   - Creating new validation tools
   - Improving visualizations

4. **Bug Reports**
   - Identifying data errors
   - Reporting issues with documentation or scripts
   - Suggesting improvements

## How to Contribute

1. **For Data Contributions**
   - Follow the [Data Entry Guide](process/documentation/data_entry_guide.md)
   - Add your data in JSON format following the established schemas
   - Include sources for all information
   - Validate your data using the validation tools
   - Create a pull request with your changes

2. **For Documentation Contributions**
   - Follow the existing documentation style and format
   - Keep your changes clear and concise
   - Include examples where appropriate
   - Test any code examples or scripts you include
   - Create a pull request with your changes

3. **For Code Contributions**
   - Follow PEP 8 style guidelines for Python code
   - Include comments in your code
   - Add docstrings to functions and classes
   - Test your code with the validation tools
   - Create a pull request with your changes

## Data Standards

All data contributions must follow these standards:

1. **Schema Compliance**
   - All data must conform to the appropriate JSON schema
   - Use the validation tools to check your data

2. **Source Requirements**
   - Every piece of information must have a source
   - Use the standardized source format

3. **Date Standards**
   - All dates must follow ISO 8601 format (YYYY-MM-DD)
   - Use appropriate markers for approximate dates

4. **Location Hierarchy**
   - Use the standardized location hierarchy
   - Follow the naming conventions for locations

5. **Certainty Ratings**
   - Include certainty ratings for uncertain information
   - Use the standardized values (certain, very_likely, likely, uncertain)

## Code of Conduct

We are committed to maintaining a welcoming and inclusive environment for all contributors. Please follow these guidelines:

1. **Respectful Communication**
   - Be respectful in all interactions
   - Offer constructive feedback
   - Be patient with new contributors

2. **Inclusive Language**
   - Use inclusive language in all documentation
   - Respect cultural and religious diversity

3. **Copyright and Legal Considerations**
   - Ensure you have the right to share any information
   - Respect privacy for living individuals
   - Follow copyright laws for images and documents

4. **Disagreements**
   - Resolve disagreements professionally
   - Focus on facts and data
   - Seek mediation if needed

## Repository Structure

Please familiarize yourself with the repository structure before contributing:

- `family/individuals/` - JSON files for individual person records
- `family/families/` - JSON files for family unit records
- `family/events/` - JSON files for significant events
- `family/sources/` - JSON files for source information
- `family/images/` - Family photos and documents
- `process/data_structure/` - JSON schema definitions
- `process/documentation/` - Documentation for the project
- `process/tools/validation/` - Validation and processing scripts
- `process/visualization/mermaid/` - Mermaid diagram templates

## Testing and Validation

Before submitting any changes, please validate your data:

1. **Schema Validation**
   - Use the `validate.py` script to check your JSON files
   - Fix any errors before submitting

2. **Relationship Validation**
   - Use the `validate_relationships.py` script to check relationships
   - Ensure all relationships are bidirectional and consistent

3. **Code Testing**
   - Test any new scripts or tools you create
   - Ensure they work with the existing codebase

## Questions and Support

If you have questions or need support, please:

1. Check the existing documentation
2. Search the issues to see if your question has been addressed
3. Create a new issue with the "question" label
4. Contact the project maintainers for sensitive matters

## Thank You!

We appreciate your contribution to the Kirchheimer Family Tree project. Your help in preserving and sharing this family history is invaluable. Thank you for taking the time to contribute!
