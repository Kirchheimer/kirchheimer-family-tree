# Remote Resources Guide

This document provides information about online genealogy services and how to link to them in the Kirchheimer Family Tree repository.

## Linked Resources

The Kirchheimer Family Tree repository may contain links to external genealogy services and resources. These resources provide additional information about family members and can help verify and expand on the data in the repository.

### Online Genealogy Services

1. **FamilySearch**
   - URL: https://www.familysearch.org/
   - Description: Free genealogical records and family tree software
   - ID Format: `FS_####` (e.g., `FS_1234567`)

2. **MyHeritage**
   - URL: https://www.myheritage.com/
   - Description: Global genealogy platform with extensive records
   - ID Format: `MH_####` (e.g., `MH_1234567`)

3. **Ancestry**
   - URL: https://www.ancestry.com/
   - Description: Comprehensive genealogy platform with extensive records
   - ID Format: `AN_####` (e.g., `AN_1234567`)

4. **Geni**
   - URL: https://www.geni.com/
   - Description: Collaborative family tree platform
   - ID Format: `GN_####` (e.g., `GN_1234567`)

5. **JewishGen**
   - URL: https://www.jewishgen.org/
   - Description: Jewish genealogy database and community
   - ID Format: `JG_####` (e.g., `JG_1234567`)

### Documentation Resources

1. **US Holocaust Memorial Museum**
   - URL: https://www.ushmm.org/
   - Description: Holocaust-related records and documentation
   - ID Format: `USHMM_####` (e.g., `USHMM_1234567`)

2. **Family History Library**
   - URL: https://www.familysearch.org/en/FamilyHistoryLibrary
   - Description: Extensive collection of genealogical records
   - ID Format: `FHL_####` (e.g., `FHL_1234567`)

3. **JewishGen Family Finder**
   - URL: https://www.jewishgen.org/InfoFiles/countries.htm
   - Description: Database of Jewish genealogical research
   - ID Format: `JGF_####` (e.g., `JGF_1234567`)

### Historical Records Archives

1. **Archives Portal Europe**
   - URL: https://www.archivesportaleurope.net/
   - Description: European archival information
   - ID Format: `APE_####` (e.g., `APE_1234567`)

2. **FamilySearch Historical Records**
   - URL: https://www.familysearch.org/en/search/collection/list
   - Description: Historical records collection
   - ID Format: `FSH_####` (e.g., `FSH_1234567`)

3. **Internet Archive**
   - URL: https://archive.org/
   - Description: Digital archive of books, documents, and media
   - ID Format: `IA_####` (e.g., `IA_1234567`)

## Linking to Remote Resources

When documenting connections to remote resources in the Kirchheimer Family Tree:

1. Add a `remote_resources` field to the appropriate JSON record (individual, family, or event)
2. Include the resource type, ID, and title
3. Add a URL that points to the resource

### Example for Individual Record

```json
{
  "id": "person_001",
  "names": {
    "primary": {
      "given": "Samson",
      "surname": "Kirchheimer"
    }
  },
  "birth": {
    "date": "1872-08-10"
  },
  "remote_resources": [
    {
      "resource_type": "FamilySearch",
      "resource_id": "FS_1234567",
      "title": "Samson Kirchheimer Record",
      "url": "https://www.familysearch.org/ark:/61903/1:1:xxxx-xxxx"
    },
    {
      "resource_type": "MyHeritage",
      "resource_id": "MH_7654321",
      "title": "Samson Kirchheimer Family Tree",
      "url": "https://www.myheritage.com/person/person_7654321"
    }
  ]
}
```

### Example for Family Record

```json
{
  "id": "family_001",
  "partners": [
    "person_001",
    "person_002"
  ],
  "marriage": {
    "date": "1900-01-01"
  },
  "remote_resources": [
    {
      "resource_type": "JewishGen",
      "resource_id": "JG_1234567",
      "title": "Kirchheimer Family in Germany",
      "url": "https://www.jewishgen.org/databases/record/1234567"
    }
  ]
}
```

### Example for Event Record

```json
{
  "id": "event_001",
  "type": "immigration",
  "date": "1889-10-15",
  "participants": [
    "person_001"
  ],
  "remote_resources": [
    {
      "resource_type": "FamilySearch",
      "resource_id": "FSH_2345678",
      "title": "Passenger List: Ship to America 1889",
      "url": "https://www.familysearch.org/ark:/61903/1:1:xxxx-xxxx"
    }
  ]
}
```

## Best Practices for Remote Resources

1. **Verify Information**: Ensure the linked resource contains accurate information that matches the repository data
2. **Format Resources**: Use consistent formatting for all remote resources
3. **Include Sources**: Even when linking to remote resources, include local source documents
4. **Update Links**: Periodically check that external links are still valid
5. **Document Uncertainties**: Note any discrepancies between repository data and linked resources
