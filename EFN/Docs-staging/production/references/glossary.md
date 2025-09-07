# Fieldmark Glossary: Key Terms and Concepts

**Purpose**: Define critical terminology for consistent understanding  
**Created**: 2025-01-07  
**Usage**: Reference for all Fieldmark-specific terms and concepts

<!-- structured:metadata
meta:purpose: technical-reference
meta:summary: Comprehensive glossary defining all Fieldmark-specific terminology and concepts.
meta:generates: term-definitions
meta:requires: [fieldmark-knowledge]
meta:version: 3.0.0
meta:document: glossary
meta:depth-tags: [essential]
-->

<!-- discovery:metadata
provides: [term-definitions, concept-clarification, ontology]
see-also: [notebook-format-guide, component-reference, field-type-index]
-->

## Core Architecture Terms

### fields
**Definition**: The lowest level of the three-tier hierarchy containing individual field definitions.  
**Context**: Each field has a unique identifier and contains component configuration.  
**Example**: `"site-name": { "component-name": "TextField", ... }`  
**See**: [Form Structure Guide](#form-structure-guide)

### fviews
**Definition**: Form views - the middle tier that groups fields into logical sections.  
**Critical**: REQUIRED layer between fields and viewsets. 50% of import failures are due to missing fviews.  
**Example**: `"basic-info": { "fields": ["field1", "field2"], "label": "Basic Information" }`  
**See**: [Notebook Structure](#notebook-structure-errors)

### viewsets
**Definition**: The top tier that groups fviews into complete forms or pages.  
**Context**: What users see as distinct screens or tabs in the application.  
**Example**: `"main-form": { "views": ["section1", "section2"], "label": "Survey Form" }`  
**See**: [Form Structure Guide](#form-structure-guide)

### visible_types
**Definition**: Array listing which viewsets are accessible to users.  
**Critical**: Must reference existing viewsets or forms won't appear.  
**Example**: `"visible_types": ["main-form", "review-form"]`  
**See**: [Notebook Format Guide](#notebook-format-guide)

### ui-specification
**Definition**: The container object holding all form structure (fields, fviews, viewsets).  
**Context**: Required wrapper for all notebook configuration.  
**Example**: `"ui-specification": { "fields": {...}, "fviews": {...}, "viewsets": {...} }`

## Field Configuration Terms

### component-namespace
**Definition**: Package/library providing the component implementation.  
**Values**: `faims-custom`, `formik-material-ui`, `mapping-plugin`, `qrcode`  
**Example**: `"component-namespace": "faims-custom"`  
**See**: [Component Reference](#component-reference)

### component-name
**Definition**: The specific component class within the namespace.  
**Example**: `"component-name": "FAIMSTextField"`  
**Note**: Designer UI names often differ from actual component names.  
**See**: [Designer Component Mapping](#designer-component-mapping)

### component-parameters
**Definition**: Configuration object containing all field-specific settings.  
**Critical**: Must include `"name"` parameter matching the field identifier.  
**Example**: `"component-parameters": { "name": "field-id", "label": "Field Label" }`

### type-returned
**Definition**: Data type the field returns when saved.  
**Values**: `faims-core::String`, `faims-core::Number`, `faims-core::Array`, `faims-attachment::Files`  
**Example**: `"type-returned": "faims-core::String"`

### validationSchema
**Definition**: Yup-based validation rules array.  
**Format**: Array of arrays, type validation must come first.  
**Example**: `[["yup.string"], ["yup.required", "This field is required"]]`  
**See**: [Validation Errors](#validation-errors)

## Special Field Types

### HRID
**Definition**: Human-Readable Identifier - user-friendly record IDs instead of UUIDs.  
**Implementation**: Uses TemplatedStringField with template patterns.  
**Example**: `"PROJECT-2024-001"` instead of `"rec-a7f3b2c1-d4e5..."`  
**Critical**: Should be included in every notebook for usability.  
**See**: [TemplatedStringField](#templatedstringfield)

### TemplatedStringField
**Definition**: Auto-generates strings from templates with variables.  
**Variables**: `{{PROJECT}}`, `{{_CREATED_DATE}}`, `{{_INCREMENT}}`  
**Security**: ⚠️ XSS vulnerability if used with user input - use only for system-generated values.  
**See**: [Text Fields](#text-input-fields)

### RelationshipField
**Definition**: Links records within or between notebooks.  
**Limits**: Performance degrades beyond 50 relationships per record.  
**Example**: Links artifact to context, sample to site.  
**See**: [Relationship Field](#relationship-fields)

## Conditional Logic Terms

### is-logic
**Definition**: Object defining conditional visibility rules for fields.  
**Format**: `{ "if": "controller-field", "==": "trigger-value" }`  
**Complex**: Supports `and`, `or`, `in`, `!=`, `>`, `<` operators.  
**See**: [Dynamic Forms Guide](#dynamic-forms-guide)

### logic_select
**Definition**: Boolean flag marking a field as a conditional logic controller.  
**Critical**: Must be `true` on controller field for is-logic to work.  
**Example**: `"logic_select": true` on RadioGroup controlling dependent fields.

## Platform-Specific Terms

### Mobile-only Components
**Definition**: Components that only function on iOS/Android apps.  
**List**: `QRCodeFormField` (scanning), `TakePoint` (GPS), `TakePhoto` (camera)  
**Best Practice**: Always provide web fallbacks.  
**See**: [Platform Reference](#platform-reference)

### Offline Mode
**Definition**: Ability to work without internet connection.  
**Context**: Mobile apps cache data; web requires initial connection.  
**Limitation**: MapFormField needs internet for first tile load.

## Data Types

### faims-core::String
**Definition**: Basic text data type.  
**Used by**: TextField, Select, DateTimeNow, most fields.

### faims-core::Number
**Definition**: Numeric data type.  
**Used by**: TextField with type="number", BasicAutoIncrementer.

### faims-core::Array
**Definition**: Multiple value data type.  
**Used by**: MultiSelect, Checkbox groups.

### faims-attachment::Files
**Definition**: File attachment data type.  
**Used by**: TakePhoto, AudioFormField.

### faims-core::JSON
**Definition**: Complex object data type.  
**Used by**: TakePoint (GPS coordinates), MapFormField.

## Validation Terms

### yup
**Definition**: JavaScript schema validation library used by Fieldmark.  
**Usage**: All validation rules start with `yup.` prefix.  
**Order**: Type validation (yup.string) must come before constraints (yup.required).  
**See**: [Validation Error Decoder](#validation-error-decoder)

### Cross-field Validation
**Definition**: Validation rules referencing other fields.  
**Example**: `["yup.min", ["yup.ref", "start-date"], "Must be after start date"]`  
**See**: [Cookbook Recipe #1](#recipe-1-date-range-picker)

## Template System Terms

### Template Markers
**Definition**: Placeholder variables in parametric templates.  
**Format**: `{{VARIABLE_NAME}}`  
**Example**: `{{FIELD_ID}}`, `{{FIELD_LABEL}}`, `{{VALIDATION_MESSAGE}}`  
**Count**: 1,290 markers added to documentation.  
**See**: [Cookbook](#fieldmark-cookbook)

### Parametric Generation
**Definition**: Creating notebooks by replacing template variables rather than editing JSON.  
**Benefit**: Ensures all references update consistently.  
**See**: [Generation-Ready Patterns](#generation-ready-patterns)

## Common Issues Terms

### Missing fviews
**Definition**: Most common import failure - missing middle tier.  
**Impact**: 50% of notebook import failures.  
**Fix**: Add fviews layer between fields and viewsets.  
**See**: [Troubleshooting Index](#notebook-structure-errors)

### Circular Reference
**Definition**: Field relationships creating infinite loops.  
**Symptom**: "Maximum call stack exceeded" error.  
**Fix**: Check relationship field configurations.

### Race Condition
**Definition**: Timing issue where operations complete out of order.  
**Example**: Address field geocoding vs user typing.  
**Fix**: Implement debounce configuration.

## Designer vs JSON Terms

### Designer UI Name
**Definition**: Field name shown in Fieldmark Designer interface.  
**Issue**: Often differs from actual JSON component name.  
**Example**: "Text Field" in Designer = "FAIMSTextField" in JSON.  
**See**: [Designer Component Mapping](#designer-component-mapping)

### Component Mapping
**Definition**: Translation table between Designer names and JSON components.  
**Critical**: Required for converting Designer notebooks to JSON.  
**Location**: designer-component-mapping.md

## Metadata Terms

### metadata
**Definition**: Notebook-level configuration section.  
**Contains**: Project name, version, hridField designation.  
**Example**: `"metadata": { "name": "Project 2024", "hridField": "record-id" }`

### discovery:metadata
**Definition**: Documentation metadata for content discovery.  
**Format**: HTML comments with provides/see-also tags.  
**Purpose**: Helps LLMs understand document relationships.

### structured:metadata
**Definition**: Enhanced metadata with purpose, summary, requirements.  
**Format**: HTML comments with meta: prefixed tags.  
**Purpose**: Semantic understanding of document content.

## Security Terms

### XSS (Cross-Site Scripting)
**Definition**: Security vulnerability allowing malicious script injection.  
**Risk**: TemplatedStringField with user input.  
**Mitigation**: Never use user input in templates.  
**See**: [Security Considerations](#security-considerations)

## Performance Terms

### Relationship Limit
**Definition**: ~50 relationships per record before performance degrades.  
**Impact**: Slow form loading and saving.  
**Solution**: Split into multiple related forms.

### Notebook Size Limit
**Definition**: Practical limit of ~100 fields per notebook.  
**Impact**: Slow import/export, UI lag.  
**Solution**: Split into multiple viewsets.

## Acronyms

| Acronym | Full Term | Context |
|---------|-----------|---------|
| HRID | Human-Readable Identifier | User-friendly record IDs |
| XSS | Cross-Site Scripting | Security vulnerability |
| GPS | Global Positioning System | Location capture |
| JSON | JavaScript Object Notation | Data format |
| UI | User Interface | Designer or app interface |
| UUID | Universally Unique Identifier | System-generated IDs |
| CRUD | Create, Read, Update, Delete | Database operations |

---

## Usage Notes

This glossary provides:
1. **Consistent terminology** across all documentation
2. **Clear definitions** for Fieldmark-specific concepts
3. **Cross-references** to detailed documentation
4. **Context** for when and how terms are used

For implementation details, see the referenced documentation sections.

---

*This glossary defines ~60 critical terms for Fieldmark notebook development.*