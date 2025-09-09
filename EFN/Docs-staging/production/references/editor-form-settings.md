<!-- concat:boundary:start section="editor-form-settings" -->
<!-- concat:metadata
document_id: editor-form-settings
category: reference
type: editor-configuration
last_updated: 2025-01-09
-->

<!-- discovery:metadata
provides: [form-settings-configuration, viewset-properties, finish-button-logic, summary-fields-setup, hrid-configuration]
requires: [editor-access, viewset-structure, field-definitions]
see-also: [form-structure-guide, designer-component-mapping, notebook-format-guide, glossary]
-->

<!-- structured:metadata
meta:purpose: technical-reference
meta:audience: [notebook-designers, developers, llm-agents]
meta:priority: essential
meta:complexity: intermediate
meta:version: 1.0.0
meta:document: editor_form_settings
meta:depth-tags: [essential, important, comprehensive]
-->

# Editor Form Settings Reference

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Designer Mapping](./designer-component-mapping.md) | **Form Settings** | [Notebook Format →](./notebook-format-guide.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Designer Mapping](#designer-component-mapping) | [Notebook Format ↓](#notebook-format-guide) -->

## Overview {essential}

Form Settings is a configuration panel within the Notebook Editor that controls per-viewset (form) behaviour. Each form in a notebook can have independent settings, allowing different data collection strategies within the same notebook.

**Location**: Editor → Design tab → Form Settings (expandable panel)  
**Scope**: Per-viewset configuration (not global)  
**JSON Path**: `ui-specification.viewsets.{{VIEWSET_ID}}`

### Key Concepts {essential}

| Concept | Description | Impact |
|---------|-------------|--------|
| **Viewset** | A form or data collection screen | Each has independent settings |
| **Record List Table** | Table showing all collected records | Configured via summary_fields |
| **HRID** | Human-Readable Identifier | Alternative to UUID display |
| **Finish Button** | Form completion control | Governed by publishButtonBehaviour |

---

## Configuration Properties {essential}

### publishButtonBehaviour {essential}

**Purpose**: Controls when users can save and complete forms  
**UI Label**: "Finish Button Behavior"  
**Type**: `enum`  
**Default**: `"always"`

#### Available Options

| Value | UI Display | Description | Use Case |
|-------|------------|-------------|----------|
| `"always"` | Always Show | Finish button always visible | Rapid data entry, drafts OK |
| `"visited"` | Show Once All Sections Visited | Requires visiting all tabs/sections | Training, ensure completeness |
| `"noErrors"` | Show Only When No Errors Exist | Requires valid data in all fields | Critical data, quality control |

#### JSON Structure
```json
{
  "viewsets": {
    "{{VIEWSET_ID}}": {
      "publishButtonBehaviour": "{{BEHAVIOUR_VALUE}}"
    }
  }
}
```

#### Implementation Logic {important}
```javascript
const showFinishButton = 
  publishButtonBehaviour === 'always' ||
  (publishButtonBehaviour === 'visited' && allSectionsVisited) ||
  (publishButtonBehaviour === 'noErrors' && !hasErrors);
```

#### Decision Matrix {important}

| Data Type | Recommended Setting | Rationale |
|-----------|-------------------|-----------|
| Field observations | `"always"` | Speed critical, can edit later |
| Archaeological finds | `"visited"` | Ensure all attributes recorded |
| Laboratory measurements | `"noErrors"` | Data integrity paramount |
| Training exercises | `"visited"` | Educational completeness |
| Citizen science | `"noErrors"` | Prevent invalid submissions |

### layout {important}

**Purpose**: Controls how form sections are displayed  
**UI Label**: "Layout Style"  
**Type**: `enum`  
**Default**: `"tabs"`

#### Available Options

| Value | Display Style | Description | Best For |
|-------|--------------|-------------|----------|
| `"tabs"` | Horizontal tabs | Sections as clickable tabs | Desktop, complex forms |
| `"inline"` | Vertical scroll | All sections in single page | Mobile, simple forms |

#### Platform Recommendations {important}

| Platform | {{SECTION_COUNT}} < 4 | {{SECTION_COUNT}} ≥ 4 |
|----------|----------------------|----------------------|
| Desktop | Either | `"tabs"` recommended |
| Tablet | Either | `"tabs"` recommended |
| Mobile | `"inline"` recommended | `"inline"` recommended |

#### JSON Structure
```json
{
  "viewsets": {
    "{{VIEWSET_ID}}": {
      "layout": "{{LAYOUT_VALUE}}"
    }
  }
}
```

### summary_fields {essential}

**Purpose**: Defines which fields appear as columns in the record list table  
**UI Label**: "Summary Fields"  
**Type**: `Array<string>`  
**Default**: `[]` (empty array)

#### Configuration

- **UI Control**: Multi-select dropdown showing all form fields
- **Selection**: Choose 2-4 most identifying fields
- **Display**: Selected fields become table columns
- **Order**: Matches selection order in array

#### Best Practices {important}

| Field Type | Good for Summary | Avoid | Reason |
|------------|-----------------|-------|--------|
| {{HRID_FIELD}} | ✅ Always include | ❌ Never | Primary identifier |
| Date fields | ✅ Recommended | | Temporal context |
| Location name | ✅ Recommended | | Spatial context |
| Short text | ✅ If identifying | | Quick identification |
| Long text | | ❌ Avoid | Takes too much space |
| Photos | | ❌ Avoid | Not displayable in table |

#### JSON Structure
```json
{
  "viewsets": {
    "{{VIEWSET_ID}}": {
      "summary_fields": [
        "{{FIELD_ID_1}}",
        "{{FIELD_ID_2}}",
        "{{FIELD_ID_3}}"
      ]
    }
  }
}
```

#### Record List Table Behavior {important}

1. **With summary_fields configured**:
   - Shows HRID + selected fields as columns
   - Field labels used as column headers
   - Missing data shows placeholder: "—"

2. **With empty summary_fields**:
   - Shows HRID column only
   - Simplified table view

3. **Invalid field handling**:
   - Gracefully ignores non-existent fields
   - Console warning: "Found null/undefined field"
   - Table still renders with valid fields

### hridField {essential}

**Purpose**: Specifies which field serves as the Human-Readable Identifier  
**UI Label**: "Human-Readable ID Field"  
**Type**: `string` (field ID)  
**Default**: `undefined`

#### Requirements {essential}

Field must meet ALL criteria:
1. `type-returned`: `"faims-core::String"`
2. `component-parameters.required`: `true`
3. Exists within the viewset's fields

#### Validation Logic {important}
```javascript
const isValidHridField = (field) => {
  return field['type-returned'] === 'faims-core::String' 
    && field['component-parameters'].required === true;
};
```

#### Fallback Chain {essential}

System attempts to find HRID in this order:
1. **Specified hridField**: Uses configured field if valid
2. **Auto-detect TemplatedStringField**: First valid template field found
3. **UUID fallback**: `"rec-{{UUID_FRAGMENT}}"` format

Example UUID format: `"rec-5f8a9b3c"`

#### JSON Structure
```json
{
  "viewsets": {
    "{{VIEWSET_ID}}": {
      "hridField": "{{FIELD_ID}}"
    }
  }
}
```

#### Common HRID Patterns {important}

| Pattern | Template Example | Result Example |
|---------|-----------------|----------------|
| Sequential | `{{PROJECT}}-{{_INCREMENT}}` | `PROJ-001` |
| Date-based | `{{_CREATED_DATE}}-{{_INCREMENT}}` | `2025-01-09-001` |
| Location-based | `{{SITE}}-{{TRENCH}}-{{_INCREMENT}}` | `SITE1-T5-042` |
| Type-based | `{{RECORD_TYPE}}-{{YYYY}}-{{_INCREMENT}}` | `FIND-2025-156` |

---

## Complete Configuration Example {comprehensive}

```json
{
  "ui-specification": {
    "viewsets": {
      "archaeological-find": {
        "views": ["basic-info", "context", "description"],
        "label": "Archaeological Find",
        "publishButtonBehaviour": "visited",
        "layout": "tabs",
        "summary_fields": [
          "find-id",
          "find-date", 
          "context-number",
          "material-type"
        ],
        "hridField": "find-id"
      },
      "site-survey": {
        "views": ["location", "observations"],
        "label": "Site Survey",
        "publishButtonBehaviour": "noErrors",
        "layout": "inline",
        "summary_fields": [
          "survey-id",
          "survey-date",
          "site-name"
        ],
        "hridField": "survey-id"
      }
    }
  }
}
```

---

## Editor Interface Details {comprehensive}

### Accessing Form Settings

1. Open Notebook Editor
2. Select Design tab
3. Choose a form from tabs (e.g., "{{FORM_NAME}}")
4. Click Form Settings gear icon to expand panel

### UI Components

#### Finish Button Behavior Dropdown
- **Location**: Top of Form Settings panel
- **Options**: Three radio buttons or dropdown
- **Live preview**: Changes apply immediately to form preview

#### Layout Style Selector
- **Location**: Below Finish Button Behavior
- **Options**: Tabs | Inline toggle or dropdown
- **Visual feedback**: Form preview updates on change

#### Summary Fields Multi-Select
- **Location**: Middle of panel
- **Type**: Autocomplete multi-select
- **Search**: Type to filter available fields
- **Chips**: Selected fields show as removable chips

#### HRID Field Dropdown
- **Location**: Bottom of panel
- **Filter**: Only shows required string fields
- **Warning**: Indicates if no valid fields available

---

## Common Issues and Solutions {important}

### Issue: Finish button not appearing

| Cause | Solution | Verification | Debug Command |
| `publishButtonBehaviour: "visited"` | Visit all form sections | Check visited sections indicator | `console.log(visitedSections)` |
| `publishButtonBehaviour: "noErrors"` | Fix validation errors | Review error messages | `console.log(formik.errors)` |
| Missing configuration | Set to `"always"` temporarily | Check JSON structure | `console.log(viewset.publishButtonBehaviour)` |

### Issue: HRID shows as "rec-xxxxx"

| Cause | Solution | Prevention | Validation Check |
| No hridField configured | Select valid field in Form Settings | Always configure HRID | `viewset.hridField !== undefined` |
| Selected field not required | Make field required | Use TemplatedStringField | `field['component-parameters'].required` |
| Field doesn't exist | Verify field ID matches | Use Editor dropdown | `fields[viewset.hridField] !== undefined` |

### Issue: Summary fields not showing in table

| Cause | Solution | Debugging | Console Check |
| Empty summary_fields array | Select fields in Form Settings | Check viewset JSON | `viewset.summary_fields.length` |
| Field IDs incorrect | Use Editor selection UI | Console shows warnings | `'Found null/undefined field'` |
| Fields from different viewset | Only select current form's fields | Verify field ownership | `viewset.views.flatMap(v => fviews[v].fields)` |

---

## Performance Considerations {comprehensive}

### Summary Fields Impact

| Number of Fields | Performance | Recommendation |
|-----------------|-------------|----------------|
| 0-3 | Optimal | Best for most cases |
| 4-6 | Good | Acceptable if needed |
| 7-10 | Degraded | Avoid, consider redesign |
| >10 | Poor | Table becomes unwieldy |

### Record List Table Optimisation

- **Lazy loading**: Only visible rows render
- **Virtual scrolling**: For >100 records
- **Column width**: Auto-calculated based on content
- **Caching**: Summary data cached per session

---

## Migration and Compatibility {comprehensive}

### Version Compatibility

| Fieldmark Version | Form Settings Support | Notes |
|------------------|----------------------|-------|
| < 3.0 | Partial | Only hridField supported |
| 3.0 - 3.2 | Full | All properties supported |
| > 3.2 | Enhanced | Additional validation options |

### Migration from Legacy Notebooks

```javascript
// Legacy format (pre-3.0)
"viewsets": {
  "form1": {
    "hrid": "field-id" // Old property name
  }
}

// Current format (3.0+)
"viewsets": {
  "form1": {
    "hridField": "field-id", // New property name
    "publishButtonBehaviour": "always",
    "layout": "tabs",
    "summary_fields": []
  }
}
```

---

## LLM Quick Reference {essential}

### Configuration Decision Tree
```yaml
form_type:
  rapid_data_collection:
    publishButtonBehaviour: "always"
    layout: "inline" # Mobile-first
    summary_fields: ["{{HRID}}", "{{DATE}}", "{{PRIMARY_FIELD}}"]
    
  validated_data_entry:
    publishButtonBehaviour: "noErrors"
    layout: "tabs" # Desktop-oriented
    summary_fields: ["{{HRID}}", "{{DATE}}", "{{LOCATION}}", "{{STATUS}}"]
    
  training_exercise:
    publishButtonBehaviour: "visited"
    layout: "tabs"
    summary_fields: ["{{HRID}}", "{{USER}}", "{{COMPLETION_STATUS}}"]
```

### Common Configurations
| Use Case | publishButton | layout | summary_fields Count | HRID Type |
|----------|--------------|--------|---------------------|------------|
| Field Survey | `always` | `inline` | 2-3 | Date-based |
| Lab Data | `noErrors` | `tabs` | 3-4 | Sequential |
| Archaeological | `visited` | `tabs` | 3-4 | Context-based |
| Citizen Science | `noErrors` | `inline` | 2-3 | Location-based |

### Property Validation Rules
```javascript
// Essential validation for LLM code generation
const validateFormSettings = (viewset) => ({
  publishButtonBehaviour: ['always', 'visited', 'noErrors'].includes(viewset.publishButtonBehaviour),
  layout: ['tabs', 'inline'].includes(viewset.layout),
  summary_fields: Array.isArray(viewset.summary_fields) && viewset.summary_fields.every(f => fields[f]),
  hridField: !viewset.hridField || (fields[viewset.hridField]?.['type-returned'] === 'faims-core::String')
});
```

---

## Enhanced Troubleshooting {important}

### Diagnostic Decision Trees

#### Problem: Finish Button Not Visible
```yaml
diagnosis:
  check_setting:
    - query: "viewsets.{{VIEWSET_ID}}.publishButtonBehaviour"
    - if_undefined: "Set to 'always' as default"
    - if_visited:
      check: "All sections visited?"
      solution: "Visit remaining sections or change to 'always'"
    - if_noErrors:
      check: "Form validation status"
      solution: "Fix validation errors or temporarily set to 'always'"
```

#### Problem: HRID Shows UUID (rec-xxxxx)
```yaml
diagnosis:
  check_hrid_field:
    - query: "viewsets.{{VIEWSET_ID}}.hridField"
    - if_undefined:
      action: "Select valid field in Form Settings"
      requirement: "Field must be required string"
    - if_defined:
      validate:
        - "fields[hridField]['type-returned'] === 'faims-core::String'"
        - "fields[hridField]['component-parameters'].required === true"
      fallback: "Create TemplatedStringField for HRID"
```

#### Problem: Summary Fields Not Displaying
```yaml
diagnosis:
  check_configuration:
    - query: "viewsets.{{VIEWSET_ID}}.summary_fields"
    - if_empty: "Select 2-4 fields in Form Settings"
    - if_populated:
      validate_each:
        - "Field exists in viewset.views[*].fields"
        - "Field ID matches exactly (case-sensitive)"
      console_check: "Look for 'null/undefined field' warnings"
```

### Validation Checklist for LLMs
```javascript
// Use this for automated validation
const formSettingsChecklist = {
  required: [
    'viewsets.{{VIEWSET_ID}}.views',
    'viewsets.{{VIEWSET_ID}}.label'
  ],
  recommended: [
    'viewsets.{{VIEWSET_ID}}.publishButtonBehaviour',
    'viewsets.{{VIEWSET_ID}}.hridField',
    'viewsets.{{VIEWSET_ID}}.summary_fields'
  ],
  optional: [
    'viewsets.{{VIEWSET_ID}}.layout'
  ]
};
```

---

## Cross-References {important}

### Core Documentation
→ [Form Structure Guide](../patterns/form-structure-guide.md) - Viewset architecture and hierarchy  
→ [Designer Component Mapping](./designer-component-mapping.md) - UI to JSON property mappings  
→ [Notebook Format Guide](./notebook-format-guide.md) - Complete JSON structure reference  
→ [Glossary](./glossary.md) - Term definitions and concepts  
→ [Troubleshooting Index](./troubleshooting-index.md) - General error solutions  

### Field Configuration
→ [Field Type Index](./field-type-index.md) - All available field types  
→ [Text Fields](../field-categories/text-fields-v05.md) - TemplatedStringField for HRIDs  
→ [Field Selection Guide](../patterns/field-selection-guide.md) - Choosing appropriate fields  

### Related Patterns
→ [Dynamic Forms Guide](../patterns/dynamic-forms-guide.md) - Conditional logic with form settings  
→ [Implementation Patterns](../patterns/implementation-patterns-guide.md) - Common notebook patterns  
→ [Notebook Templates](./notebook-templates.md) - Complete working examples  

### Validation and Testing
→ [Constraints Reference](./constraints-reference.md) - System limitations  
→ [Operations Reference](./operations-reference.md) - Testing and deployment  

---

## Template Variable Reference {comprehensive}

Variables used throughout this document for parametric generation:

| Variable | Description | Example Value |
|----------|-------------|---------------|
| `{{VIEWSET_ID}}` | Unique viewset identifier | `"archaeological-find"` |
| `{{FIELD_ID}}` | Field identifier | `"site-name"` |
| `{{FIELD_ID_1}}` | First summary field | `"record-id"` |
| `{{FIELD_ID_2}}` | Second summary field | `"date-collected"` |
| `{{FIELD_ID_3}}` | Third summary field | `"location"` |
| `{{FORM_NAME}}` | Display name of form | `"Site Survey"` |
| `{{BEHAVIOUR_VALUE}}` | publishButtonBehaviour value | `"noErrors"` |
| `{{LAYOUT_VALUE}}` | Layout style value | `"tabs"` |
| `{{SECTION_COUNT}}` | Number of sections in form | `3` |
| `{{UUID_FRAGMENT}}` | First 8 chars of UUID | `"5f8a9b3c"` |
| `{{HRID_FIELD}}` | HRID field identifier | `"survey-id"` |
| `{{PROJECT}}` | Project identifier for HRID | `"PROJ2025"` |
| `{{SITE}}` | Site code for HRID | `"SITE1"` |
| `{{TRENCH}}` | Trench identifier | `"T5"` |
| `{{_INCREMENT}}` | Auto-incrementing number | `"001"` |
| `{{_CREATED_DATE}}` | Record creation date | `"2025-01-09"` |
| `{{YYYY}}` | Current year | `"2025"` |
| `{{RECORD_TYPE}}` | Type of record | `"FIND"` |
| `{{RESEARCHER_NAME}}` | Researcher identifier | `"JSmith"` |
| `{{MAX_SUMMARY_FIELDS}}` | Recommended maximum | `4` |
| `{{PLACEHOLDER_TEXT}}` | Missing data indicator | `"—"` |

---

*Last updated: 2025-01-09 | Based on Fieldmark 3.x Editor implementation*

<!-- concat:boundary:end section="editor-form-settings" -->