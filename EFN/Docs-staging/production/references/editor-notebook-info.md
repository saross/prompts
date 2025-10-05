<!-- concat:boundary:start section="editor-notebook-info" -->
<!-- concat:metadata
document_id: editor-notebook-info
category: reference
type: editor-configuration
last_updated: 2025-01-09
-->

<!-- discovery:metadata
provides: [notebook-metadata, project-configuration, custom-metadata-fields, fair-data-support, metadata-standards]
requires: [editor-access, notebook-structure]
see-also: [notebook-format-guide, glossary, editor-form-settings, operations-reference]
-->

<!-- structured:metadata
meta:purpose: technical-reference
meta:audience: [notebook-designers, developers, llm-agents, data-managers]
meta:priority: essential
meta:complexity: intermediate
meta:version: 1.0.0
meta:document: editor_notebook_info
meta:depth-tags: [essential, important, comprehensive]
-->

# Editor Notebook Info Reference

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Form Settings](./editor-form-settings.md) | **Notebook Info** | [Notebook Format →](./notebook-format-guide.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Form Settings](#editor-form-settings) | [Notebook Format ↓](#notebook-format-guide) -->

## Overview {essential}

The Notebook Info page in the Editor provides notebook-level metadata configuration, forming the top tier of Fieldmark's three-tier metadata system (notebook → record → field). This metadata enables FAIR data practices and supports compliance with domain-specific standards.

**Location**: Notebook Editor (modal overlay in Dashboard) → INFO tab
**Access Pattern**: Dashboard → Notebook → Actions tab → "Open in Editor" → INFO tab
**Scope**: Notebook-level (global to all forms)
**JSON Path**: Root level `metadata` object
**Save Behaviour**: Click SAVE (top-right) to preserve changes and close Editor

**See**: [UI Interaction Patterns](./ui-interaction-patterns.md#14-save-behaviour-in-notebook-editor) for Editor workflow details.

### Metadata Hierarchy {essential}

| Level | Location | Purpose | Examples |
|-------|----------|---------|----------|
| **Notebook** | Info page | Project-wide metadata | Project name, lead, institution |
| **Record** | Form fields | Instance-specific data | Collection date, observer, notes |
| **Field** | Annotation/Uncertainty | Attribute-level metadata | Confidence, clarifications |

---

## Core Metadata Fields {essential}

### Fixed Fields

These fields have dedicated UI elements in the Info page:

| Field | JSON Property | Type | Required | Description |
|-------|--------------|------|----------|-------------|
| **Project Name** | `name` | string | ✅ Yes | 2-100 characters, notebook identifier |
| **Project Lead** | `project_lead` | string | ❌ No | Principal investigator or project manager |
| **Lead Institution** | `lead_institution` | string | ❌ No | Primary organisation responsible |
| **Description** | `pre_description` | string | ❌ No | Markdown-formatted project description |
| **Enable QR Code Search** | `showQRCodeButton` | string | ❌ No | "true"/"false" for QR scanning |
| **Notebook Version** | `notebook_version` | string | ❌ No | Semantic versioning (e.g., "1.0") |

### JSON Structure {essential}
```json
{
  "metadata": {
    "name": "{{PROJECT_NAME}}",
    "project_lead": "{{LEAD_NAME}}",
    "lead_institution": "{{INSTITUTION}}",
    "pre_description": "{{MARKDOWN_DESCRIPTION}}",
    "showQRCodeButton": "{{TRUE_FALSE}}",
    "notebook_version": "{{VERSION}}"
  }
}
```

---

## Custom Metadata Fields {essential}

### Key-Value Pair System

The Info page allows creation of arbitrary metadata fields through a key-value interface:

**UI Components**:
- Metadata Field Name (text input)
- Metadata Field Value (text input)
- Create New Field (button)

**Behaviour**:
- No predefined schema constraints
- All values stored as strings
- Field names must be unique
- Cannot override fixed fields
- Click SAVE to preserve custom field additions

### Use Cases for Custom Fields {important}

| Use Case | Example Fields | Purpose |
|----------|---------------|---------|
| **Grant Compliance** | `grant_number`, `funding_body` | Funding attribution |
| **Ethics Approval** | `ethics_number`, `approval_date` | Research compliance |
| **Data Repository** | `repository_id`, `collection_code` | Archive preparation |
| **Domain Standards** | `raid_id`, `darwin_core_type` | Standard compliance |
| **Internal Tracking** | `cost_centre`, `department_code` | Administrative needs |

### Example Custom Metadata
```json
{
  "metadata": {
    // Fixed fields
    "name": "Archaeological Survey 2025",
    "project_lead": "Dr. Smith",
    "lead_institution": "University Example",
    
    // Custom fields for RAiD compliance
    "raid_id": "https://raid.org/10.25917/{{RAID_SUFFIX}}",
    "raid_status": "active",
    
    // Domain-specific (UK ADS)
    "ads_project_id": "{{ADS_ID}}",
    "ads_collection_type": "excavation",
    
    // Grant tracking
    "grant_number": "{{GRANT_CODE}}",
    "funding_body": "{{FUNDER_NAME}}",
    
    // Ethics
    "ethics_approval": "{{ETHICS_NUMBER}}",
    "ethics_expiry": "{{YYYY-MM-DD}}"
  }
}
```

---

## Metadata Standards Integration {important}

### Research Activity Identifier (RAiD)

RAiD provides persistent identifiers for research projects:

```yaml
raid_integration:
  required_fields:
    - raid_id: "https://raid.org/10.25917/{{SUFFIX}}"
    - raid_status: "active|inactive|withdrawn"
    - raid_start_date: "{{YYYY-MM-DD}}"
    - raid_end_date: "{{YYYY-MM-DD}}"
  
  optional_fields:
    - raid_description: "{{PROJECT_DESCRIPTION}}"
    - raid_contributors: "{{ORCID_LIST}}"
    - raid_organisations: "{{ROR_LIST}}"
```

### Domain Repository Standards {important}

#### Archaeological Data Service (UK ADS)
```json
{
  "ads_project_id": "{{PROJECT_CODE}}",
  "ads_monument_id": "{{MONUMENT_NUMBER}}",
  "ads_period": "{{PERIOD_TERM}}",
  "ads_sitetype": "{{SITE_CLASSIFICATION}}"
}
```

#### tDAR (Digital Antiquity)
```json
{
  "tdar_project_id": "{{TDAR_ID}}",
  "tdar_resource_type": "{{RESOURCE_TYPE}}",
  "tdar_culture_keywords": "{{CULTURE_TERMS}}",
  "tdar_temporal_coverage": "{{TIME_PERIOD}}"
}
```

#### Darwin Core (Biodiversity)
```json
{
  "dwc_dataset_id": "{{DATASET_UUID}}",
  "dwc_institution_code": "{{INSTITUTION_CODE}}",
  "dwc_collection_code": "{{COLLECTION_CODE}}",
  "dwc_basis_of_record": "HumanObservation|PreservedSpecimen"
}
```

---

## System Metadata Fields {comprehensive}

These fields are managed by Fieldmark but visible in the metadata object:

| Field | Purpose | Format | Editable |
|-------|---------|--------|----------|
| `schema_version` | JSON schema version | "1.0" | ❌ No |
| `accesses` | Permission levels | Array | Via Dashboard |
| `ispublic` | Public visibility | boolean | Via Dashboard |
| `isrequest` | Request access enabled | boolean | Via Dashboard |
| `project_status` | Workflow state | string | Via Dashboard |
| `derived-from` | Template source | string | ❌ No (template) |

---

## LLM Quick Reference {essential}

### Metadata Configuration Decision Tree
```yaml
notebook_type:
  research_project:
    fixed_fields:
      name: "{{PROJECT_NAME}}"
      project_lead: "{{PI_NAME}}"
      lead_institution: "{{UNIVERSITY}}"
      notebook_version: "1.0"
    custom_fields:
      grant_number: "{{GRANT_ID}}"
      ethics_approval: "{{ETHICS_CODE}}"
      
  citizen_science:
    fixed_fields:
      name: "{{PROGRAM_NAME}}"
      project_lead: "{{COORDINATOR}}"
      showQRCodeButton: "true"
    custom_fields:
      program_website: "{{URL}}"
      target_participants: "{{NUMBER}}"
      
  commercial_compliance:
    fixed_fields:
      name: "{{PROJECT_CODE}}"
      lead_institution: "{{COMPANY}}"
    custom_fields:
      client_reference: "{{CLIENT_CODE}}"
      compliance_standard: "{{STANDARD_NAME}}"
      audit_frequency: "{{SCHEDULE}}"
```

### Common Metadata Patterns
| Pattern | Fixed Fields | Custom Fields | Standards |
|---------|-------------|---------------|-----------|
| Academic Research | name, lead, institution | grant, ethics, repository | RAiD, ORCID |
| Heritage Management | name, institution | site_id, monument_type | ADS, tDAR |
| Environmental Monitoring | name, lead, version | station_id, protocol | Darwin Core |
| Training/Education | name, lead, description | course_code, semester | None |

### Validation Rules
```javascript
// Essential validation for metadata
const validateMetadata = (metadata) => ({
  required: metadata.name && metadata.name.length >= 2 && metadata.name.length <= 100,
  qrCode: ['true', 'false', undefined].includes(metadata.showQRCodeButton),
  version: !metadata.notebook_version || /^\d+\.\d+(\.\d+)?$/.test(metadata.notebook_version),
  customFields: Object.keys(metadata).every(key => 
    !['name', 'project_lead', 'lead_institution', 'pre_description', 
     'showQRCodeButton', 'notebook_version'].includes(key) || 
    typeof metadata[key] === 'string'
  )
});
```

---

## Editor Interface Details {comprehensive}

### UI Layout

```
┌─────────────────────────────────────────────────┐
│ General Information                              │
├─────────────────────────────────────────────────┤
│ [Project Name*] [Project Lead] [Lead Institution]│
│                                                   │
│ ┌─────────────────────────────────────────────┐ │
│ │ Description (Markdown Editor)                │ │
│ │                                               │ │
│ └─────────────────────────────────────────────┘ │
│                                                   │
│ ☐ Enable QR Code Search of Records               │
│ [Notebook Version]                               │
│                                                   │
│ ┌─────────────────────────────────────────────┐ │
│ │ Custom Metadata Fields                       │ │
│ │ [Metadata Field Name  ]                      │ │
│ │ [Metadata Field Value ]                      │ │
│ │ [Create New Field]                           │ │
│ │                                               │ │
│ │ Existing Fields:                             │ │
│ │ [grant_number    ][value]                    │ │
│ │ [ethics_approval ][value]                    │ │
│ └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

### Description Editor Features
- Rich text formatting (bold, italic, lists)
- Markdown source mode
- Link insertion
- Code blocks
- Tables support

### QR Code Search Behavior
When enabled (`showQRCodeButton: "true"`):
- QR scanner button appears in app
- Searches records by QR field content
- Requires QRCodeFormField in notebook
- Mobile-only feature

---

## FAIR Data Implementation {important}

### Findable
```yaml
metadata_for_findability:
  - name: Clear, descriptive title
  - project_lead: Attribution for discovery
  - custom_identifiers:
    - doi: "10.xxxx/{{DOI}}"
    - raid_id: "https://raid.org/{{ID}}"
    - repository_id: "{{REPO_ID}}"
```

### Accessible
```yaml
metadata_for_accessibility:
  - lead_institution: Contact organisation
  - project_lead: Contact person
  - custom_access:
    - access_rights: "open|embargoed|restricted"
    - embargo_date: "{{YYYY-MM-DD}}"
    - license: "{{LICENSE_TYPE}}"
```

### Interoperable
```yaml
metadata_for_interoperability:
  - schema_version: Version tracking
  - custom_standards:
    - metadata_standard: "{{STANDARD_NAME}}"
    - vocabulary: "{{CONTROLLED_VOCAB}}"
    - ontology: "{{ONTOLOGY_URI}}"
```

### Reusable
```yaml
metadata_for_reusability:
  - pre_description: Detailed documentation
  - notebook_version: Version control
  - custom_reuse:
    - methodology: "{{METHOD_DOI}}"
    - protocol: "{{PROTOCOL_URL}}"
    - quality_assurance: "{{QA_STANDARD}}"
```

---

## Troubleshooting {important}

### Issue: Custom field not saving

| Cause | Solution | Validation |
|-------|----------|------------|
| Duplicate field name | Use unique name | Check existing fields list |
| Reserved field name | Avoid fixed field names | See fixed fields table |
| Empty field name | Provide valid name | Non-empty string required |
| Special characters | Use alphanumeric + underscore | `^[a-zA-Z0-9_]+$` |

### Issue: QR Code search not working

| Cause | Solution | Check |
|-------|----------|-------|
| Not enabled in metadata | Set `showQRCodeButton: "true"` | Info page checkbox |
| No QR field in notebook | Add QRCodeFormField | Check field definitions |
| Desktop platform | Mobile-only feature | Test on iOS/Android |

### Issue: Description formatting lost

| Cause | Solution | Prevention |
|-------|----------|------------|
| Missing blank lines | Add lines before/after markdown | Use visual editor |
| Invalid markdown | Check syntax | Preview before saving |
| HTML stripped | Use markdown only | Avoid HTML tags |

---

## Migration Considerations {comprehensive}

### From Version 2.x
```javascript
// Old format
{
  "metadata": {
    "name": "Project",
    "description": "Text only"  // Plain text
  }
}

// New format (3.x)
{
  "metadata": {
    "name": "Project",
    "pre_description": "**Markdown** supported",  // Rich text
    "project_lead": "New field",
    "lead_institution": "New field",
    "notebook_version": "3.0"
  }
}
```

### Template Derivation
When `derived-from` is present:
- Some fields may be read-only
- Template updates can cascade
- Custom fields always editable
- Version tracking important

---

## Complete JSON Examples {important}

### Archaeological Research Notebook
Full metadata configuration for standards compliance:

```json
{
  "metadata": {
    "name": "Excavation Season 2025",
    "description": "Systematic excavation of Bronze Age settlement",
    "lead_institution": "University Archaeological Department",
    "contributors": ["Dr. Jane Smith", "Archaeological Survey Team"],
    "raid": "https://raid.org/10.XXXXX/raid.2025.archaeology",
    "access": {
      "access_type": "open",
      "embargo_date": null,
      "license": "CC-BY-4.0"
    },
    "notebook_metadata": {
      "ADS_Section": "Excavation",
      "ADS_Period": "Bronze Age",
      "ADS_Monument_Type": "Settlement",
      "custom_project_code": "BA2025-SITE01"
    },
    "record_metadata": {
      "default_observer": "{{current_user}}",
      "default_institution": "University Archaeological Department",
      "coordinate_system": "WGS84"
    },
    "field_metadata": {
      "material_vocabulary": "Getty AAT",
      "period_thesaurus": "PeriodO",
      "custom_classification": "Internal typology v2.3"
    }
  }
}
```

### Environmental Monitoring
Metadata for repository integration:

```json
{
  "metadata": {
    "name": "Wetland Biodiversity Survey",
    "description": "Long-term monitoring of wetland ecosystem health",
    "lead_institution": "Environmental Research Institute",
    "contributors": ["Ecology Team", "Citizen Scientists"],
    "raid": null,
    "access": {
      "access_type": "embargoed",
      "embargo_date": "2026-12-31",
      "license": "CC-BY-NC"
    },
    "notebook_metadata": {
      "Darwin_Core_BasisOfRecord": "HumanObservation",
      "GBIF_Dataset_Type": "OCCURRENCE",
      "custom_permit_number": "ENV-2025-WET-001"
    },
    "record_metadata": {
      "default_location_precision": "10m",
      "coordinate_reference_system": "EPSG:4326"
    },
    "field_metadata": {
      "species_authority": "WoRMS",
      "habitat_classification": "EUNIS"
    }
  }
}
```

### Cultural Heritage Documentation
Metadata for FAIR compliance:

```json
{
  "metadata": {
    "name": "Indigenous Knowledge Documentation",
    "description": "Collaborative heritage recording project",
    "lead_institution": "Cultural Heritage Foundation",
    "contributors": ["Community Elders", "Heritage Team"],
    "raid": "https://raid.org/10.XXXXX/raid.2025.heritage",
    "access": {
      "access_type": "restricted",
      "access_details": "Community permission required",
      "license": "Traditional Knowledge License"
    },
    "notebook_metadata": {
      "tDAR_Resource_Type": "Ethnographic Field Records",
      "custom_community_protocol": "TCP-2025-v1",
      "ethical_clearance": "HEC-2025-0142"
    },
    "record_metadata": {
      "consent_obtained": true,
      "anonymization_applied": true
    },
    "field_metadata": {
      "language_codes": "ISO 639-3",
      "cultural_protocols": "Local Traditional Knowledge System"
    },
    "derived-from": {
      "notebook-id": "template-heritage-v2",
      "created": "2025-01-01T00:00:00Z"
    }
  }
}
```

---

## Cross-References {important}

### Core Documentation
→ [Notebook Format Guide](./notebook-format-guide.md) - Complete JSON structure  
→ [Editor Form Settings](./editor-form-settings.md) - Form-level configuration  
→ {{cross-ref:roles-permissions-reference}} - Required permissions for metadata editing  
→ [Glossary](./glossary.md) - Metadata terminology  
→ [Operations Reference](./operations-reference.md) - Import/export procedures that use metadata  

### Standards and Compliance
→ [Constraints Reference](./constraints-reference.md) - Metadata limitations  
→ [Platform Reference](./platform-reference.md) - Platform-specific features  
→ [File Organization Guide](./file-organization-guide.md) - Project structure  

### Implementation Guides
→ [Implementation Patterns](../patterns/implementation-patterns-guide.md) - Best practices  
→ [Notebook Templates](./notebook-templates.md) - Example configurations  
→ [Troubleshooting Index](./troubleshooting-index.md) - Common issues  

---

## Template Variable Reference {comprehensive}

Variables for parametric documentation generation:

| Variable | Description | Example |
|----------|-------------|---------|
| `{{PROJECT_NAME}}` | Notebook title | "Archaeological Survey 2025" |
| `{{LEAD_NAME}}` | Project lead name | "Dr. Jane Smith" |
| `{{INSTITUTION}}` | Lead institution | "University Example" |
| `{{MARKDOWN_DESCRIPTION}}` | Project description | "## Overview\n\nProject details..." |
| `{{TRUE_FALSE}}` | Boolean as string | "true" or "false" |
| `{{VERSION}}` | Notebook version | "1.0.0" |
| `{{RAID_SUFFIX}}` | RAiD identifier suffix | "5f8a9b3c" |
| `{{ADS_ID}}` | ADS project code | "PROJ2025" |
| `{{GRANT_CODE}}` | Funding reference | "ARC-DP250100123" |
| `{{FUNDER_NAME}}` | Funding body | "Australian Research Council" |
| `{{ETHICS_NUMBER}}` | Ethics approval | "2025/001" |
| `{{YYYY-MM-DD}}` | Date format | "2025-01-09" |
| `{{DOI}}` | Digital Object Identifier | "10.5281/zenodo.123456" |
| `{{ORCID_LIST}}` | Researcher IDs | "0000-0001-2345-6789" |
| `{{ROR_LIST}}` | Organisation IDs | "https://ror.org/01234567" |
| `{{STANDARD_NAME}}` | Metadata standard | "Darwin Core" |
| `{{LICENSE_TYPE}}` | Data license | "CC-BY-4.0" |
| `{{REPO_ID}}` | Repository identifier | "DS-2025-001" |
| `{{CUSTOM_KEY}}` | Custom field name | "program_code" |
| `{{CUSTOM_VALUE}}` | Custom field value | "BIODIV-2025" |

---

*Last updated: 2025-01-09 | Based on Fieldmark 3.x Editor implementation*

<!-- concat:boundary:end section="editor-notebook-info" -->