# LLM Navigation Manifest for Fieldmark Documentation

<!-- discovery:metadata

<!-- structured:metadata
meta:purpose: technical-reference
meta:summary: Purpose-driven document discovery tables for LLM content navigation.
meta:generates: lookup-tables
meta:requires: [fieldmark-knowledge]
meta:version: 3.0.0
meta:document: llm_navigation_manifest
meta:depth-tags: [essential]
-->

provides: [document-discovery, purpose-tables, quick-navigation, content-matrix]
see-also: [field-type-index, all-documents]
-->


**Purpose**: Enable LLMs to quickly discover and navigate all documentation content  
**Created**: 2025-01-07  
**Usage**: This document should be included early in reference.md for optimal content discovery

## Quick Navigation: "If You Need... Look Here"

### Primary Needs → Document Mapping

| If You Need... | Use This Document | Location |
|----------------|-------------------|----------|
| **Field name to component mapping** | designer-component-mapping.md | references/ |
| **Decision trees for field selection** | field-selection-guide.md | patterns/ |
| **Complete notebook structure** | notebook-format-guide.md | references/ |
| **Platform-specific limitations** | platform-reference.md | references/ |
| **Error messages and solutions** | troubleshooting-index.md | references/ (to be created) |
| **Working notebook examples** | notebook-templates.md | references/ (to be created) |
| **Security vulnerabilities** | constraints-reference.md | references/ |
| **Migration procedures** | operations-reference.md | references/ |
| **Form structure patterns** | form-structure-guide.md | patterns/ |
| **Conditional logic implementation** | dynamic-forms-guide.md | patterns/ |
| **Dashboard operations** | dashboard-overview.md | dashboard/ |
| **Template management** | templates-interface.md | dashboard/ |
| **User permissions** | users-interface.md | dashboard/ |
| **Team collaboration** | teams-interface.md | dashboard/ |
| **Common workflows** | dashboard-patterns.md | dashboard/ |
| **Dashboard troubleshooting** | dashboard-troubleshooting.md | dashboard/ |

## Document Purpose Tables

### Dashboard Documentation (`dashboard/`)

| Document | Primary Purpose | Key Content | Lines |
|----------|----------------|-------------|-------|
| **dashboard-overview.md** | System architecture | • Navigation structure<br>• Role hierarchy<br>• Permission inheritance<br>• Platform overview | 312 |
| **templates-interface.md** | Template management | • Designer usage<br>• Field configuration<br>• Version control<br>• JSON export/import | 446 |
| **notebooks-interface.md** | Data collection | • Deployment process<br>• User management<br>• Record workflow<br>• Export options | 525 |
| **users-interface.md** | User administration | • System roles<br>• Permission matrix<br>• Activity tracking<br>• Email verification | 498 |
| **teams-interface.md** | Team collaboration | • Resource ownership<br>• Member management<br>• Team roles<br>• Shared templates | 456 |
| **dashboard-patterns.md** | Workflow recipes | • 7 parametric workflows<br>• Project setup<br>• User onboarding<br>• Migration patterns | 578 |
| **dashboard-troubleshooting.md** | Problem resolution | • 45+ common issues<br>• Error decoder<br>• Diagnostic flowcharts<br>• Emergency procedures | 305 |

### Field Documentation (`field-categories/`)

| Document | Primary Purpose | Key Content | Lines |
|----------|----------------|-------------|-------|
| **text-fields-v05.md** | Text input configuration | • FAIMSTextField vs MultipleTextField<br>• XSS prevention<br>• Template syntax<br>• 7 text components | 1,693 |
| **select-choice-fields-v05.md** | Selection field setup | • RadioGroup vs Select<br>• AdvancedSelect hierarchies<br>• CSV injection prevention<br>• 5 selection components | 1,332 |
| **datetime-fields-v05.md** | Date/time handling | • Timezone issues<br>• DateTime Now vs Picker<br>• Audit trails<br>• 4 date/time components | 1,284 |
| **number-fields-v05.md** | Numeric validation | • Controlled Number config<br>• Auto-increment setup<br>• Precision limits<br>• 3 number components | 1,298 |
| **display-field-v05.md** | Display-only content | • RichText markdown<br>• Memory management<br>• 1 display component | 571 |
| **location-fields-v05.md** | GPS and mapping | • TakePoint vs MapField<br>• GPS accuracy<br>• Privacy concerns<br>• 2 location components | 825 |
| **media-fields-v05.md** | File uploads | • TakePhoto vs FileUpload<br>• EXIF stripping<br>• Size limits<br>• 2 media components | 789 |
| **relationship-field-v05.md** | Record relationships | • RelatedRecordSelector<br>• Access control<br>• Orphan handling<br>• 1 relationship component | 584 |

### Pattern Guides (`patterns/`)

| Document | Primary Purpose | Key Content | Lines |
|----------|----------------|-------------|-------|
| **field-selection-guide.md** | Choose right field type | • Decision matrices<br>• Use case mappings<br>• Platform compatibility table | 511 |
| **form-structure-guide.md** | Build multi-section forms | • Viewsets configuration<br>• Navigation patterns<br>• Parent-child forms | 401 |
| **dynamic-forms-guide.md** | Implement conditional logic | • Visibility rules<br>• Validation patterns<br>• Computed values | 462 |
| **implementation-patterns-guide.md** | Common patterns | • Error handling<br>• Performance optimisation<br>• Best practices | 419 |

### Technical References (`references/`)

| Document | Primary Purpose | Priority | Lines |
|----------|----------------|----------|-------|
| **designer-component-mapping.md** | 🔑 **PRIMARY REFERENCE**<br>All field mappings | CRITICAL | 295 |
| **component-reference.md** | Namespaces & Formik integration | HIGH | 977 |
| **constraints-reference.md** | Security & limitations | HIGH | 497 |
| **operations-reference.md** | Migration & troubleshooting | MEDIUM | 787 |
| **platform-reference.md** | Platform-specific issues | MEDIUM | 656 |
| **notebook-format-guide.md** | JSON structure requirements | HIGH | 198 |
| **file-organization-guide.md** | Project structure | LOW | 135 |
| **field-type-index.md** | Navigation only | LOW | 81 |

## Content Coverage Matrix

### By Topic

| Topic | Primary Doc | Supporting Docs |
|-------|------------|-----------------|
| **Component Names** | designer-component-mapping | All field-categories docs |
| **JSON Structure** | notebook-format-guide | test-notebook-correct.json |
| **Field Selection** | field-selection-guide | Individual field docs |
| **Validation** | dynamic-forms-guide | Field-specific sections |
| **Security** | constraints-reference | Field-specific warnings |
| **Mobile Support** | platform-reference | media-fields, location-fields |
| **Relationships** | relationship-field | form-structure-guide |
| **Templates** | text-fields (TemplatedString) | implementation-patterns |

### By Task

| Task | Required Documents |
|------|-------------------|
| **Create a basic notebook** | notebook-format-guide + designer-component-mapping |
| **Add text fields** | text-fields-v05 + designer-component-mapping |
| **Implement validation** | dynamic-forms-guide + field-specific docs |
| **Add GPS capture** | location-fields-v05 + platform-reference |
| **Set up new project** | dashboard-patterns + teams-interface + templates-interface |
| **Manage user permissions** | users-interface + notebooks-interface |
| **Deploy template** | templates-interface + notebooks-interface |
| **Troubleshoot UI issues** | dashboard-troubleshooting + troubleshooting-index |
| **Create team structure** | teams-interface + dashboard-patterns |
| **Export collected data** | notebooks-interface + dashboard-patterns |
| **Create relationships** | relationship-field + form-structure-guide |
| **Debug import errors** | notebook-format-guide + troubleshooting-index (when created) |
| **Migrate from v2** | operations-reference + component-reference |

## Document Dependencies

```
designer-component-mapping.md (PRIMARY)
    ├── All field-categories/*.md reference it
    ├── notebook-format-guide.md uses its mappings
    └── troubleshooting relies on it

notebook-format-guide.md
    ├── Required for all notebook generation
    ├── References designer-component-mapping
    └── Used by notebook-templates (when created)

field-selection-guide.md
    ├── Aggregates all field-categories
    ├── Links to platform-reference
    └── Informs implementation-patterns

platform-reference.md
    ├── Referenced by location-fields, media-fields
    └── Impacts all mobile-specific features

constraints-reference.md
    ├── Security context for all fields
    └── Designer limitations affect all components
```

## Navigation Keywords

### Component Names
- FAIMSTextField, MultipleTextField, TextField
- RadioGroup, Select, AdvancedSelect, Checkbox, MultiSelect
- DatePicker, DateTimePicker, DateTimeNow, MonthPicker
- NumberField, ControlledNumber, AutoIncrementer
- RichText, TemplatedStringField
- TakePoint, MapField
- TakePhoto, FileUpload
- RelatedRecordSelector

### Common Issues
- "notebook won't import", "missing fviews", "no name parameter"
- "validation not working", "conditional visibility"
- "GPS not available", "photo upload failed"
- "Designer vs JSON names", "component namespace"

### Key Concepts
- fviews, viewsets, ui-specification
- component-namespace, component-name, type-returned
- validationSchema, initialValue, component-parameters
- HRID, TemplatedString, Mustache syntax

## Usage in LLM Context

When processing queries:
1. Check this manifest first to identify relevant documents
2. Load specific documents based on task requirements
3. Use designer-component-mapping.md as primary reference
4. Cross-reference with platform/constraints for edge cases

---

*This manifest enables efficient navigation of ~26,000 lines of documentation*