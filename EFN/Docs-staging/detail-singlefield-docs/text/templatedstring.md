# Templated String Field - Complete Third-Draft Documentation

## Overview

The Templated String Field represents Fieldmark's most sophisticated field automation mechanism, generating dynamic text values through Mustache.js template evaluation with real-time reactivity. This field type transcends simple concatenation, supporting conditional logic, system variable integration, and automatic re-evaluation as dependent field values change. The implementation incorporates circular reference prevention through systematic template field filtering, ensuring computational stability while maintaining instantaneous responsiveness to data modifications. Every notebook should incorporate at least one Templated String Field as the human-readable identifier (hridField), establishing meaningful record identification throughout the data lifecycle.

## Common Use Cases

• **Human-readable identifiers (HRIDs)** - Generating structured record IDs like "SITE-2024-001" from component fields
• **System metadata display** - Automatically capturing and displaying record creator and creation timestamp
• **Conditional content generation** - Including or excluding template sections based on field presence/absence
• **Standardised institutional codes** - Enforcing organisational naming conventions across datasets
• **Composite labelling systems** - Building complex specimen or artefact labels from multiple attributes
• **Dynamic status indicators** - Generating status codes that update as workflow fields change
• **Hierarchical identifiers** - Creating nested identification schemes with optional components

## Core Configuration

### Required Parameters

```json
{
  "component-namespace": "faims-custom",
  "component-name": "TemplatedStringField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "template": "{{field1}}-{{field2}}"
  }
}
```

### Optional Parameters

```json
{
  "component-parameters": {
    "label": "Record Identifier",
    "helperText": "Auto-generated from site and number",
    "fullWidth": true,
    "InputProps": {
      "type": "text",
      "readOnly": true  // Ignored - always read-only
    }
  },
  "validationSchema": [["yup.string"], ["yup.required"]],
  "initialValue": "",
  "meta": {
    "annotation": {"include": false},
    "uncertainty": {"include": false}
  }
}
```

### Template Variables

**Field Variables**:
- `{{field-name}}` - Any field within the same form/viewset
- Empty/null fields render as empty strings without breaking template
- Template fields cannot reference other template fields (filtered out)

**System Variables**:
- `{{_CREATOR_NAME}}` - User who created the record (defaults: "Unknown User")
- `{{_CREATED_TIME}}` - Creation timestamp "DD-MM-YY H:MMam/pm" (defaults: "Unknown Time")

**Mustache.js Features Supported**:
- Variables: `{{fieldName}}`
- Conditional sections: `{{#field}}content{{/field}}`
- Inverted sections: `{{^field}}shown when empty{{/field}}`
- Nested conditionals: Multiple levels of condition nesting
- Comments: `{{! This is a comment }}`

**Unsupported Features**:
- Partials: `{{> partial}}` not available
- Functions/Lambdas: No custom formatting functions
- Helpers: No custom Mustache helpers
- Loop indices: No `{{@index}}` or `{{@key}}`

## Validation Rules

| Validation Type | Implementation | Example | Behaviour |
|----------------|----------------|---------|-----------|
| Required | `["yup.required"]` | Template evaluates to "" | Fails validation, blocks submission |
| Minimum Length | `["yup.minLength", 5]` | Result: "AB" | Fails if < 5 characters |
| Maximum Length | `["yup.maxLength", 20]` | Result exceeds limit | Truncation warning, validation failure |
| Pattern Match | `["yup.matches", "^[A-Z]{3}-\\d{3}$"]` | Must match pattern | Validates evaluated result |
| String Type | `["yup.string"]` | Always passes | Base validation |

### Validation Behaviour
- Validation applies to **evaluated result**, not template definition
- Empty template evaluation fails required validation
- Read-only status does not bypass validation
- Validation occurs after each template re-evaluation
- Source field validation recommended to prevent empty results

## Display Behaviour

### Desktop Rendering
- **Element type**: Material-UI TextField permanently disabled
- **Interaction state**: Read-only with visible but non-editable content
- **Width behaviour**: Respects fullWidth parameter, typically spanning container
- **Overflow handling**: Text truncation with ellipsis for lengthy values
- **Visual indicators**: Greyed appearance indicating non-editable status
- **Copy capability**: Text selection and copying permitted

### Mobile Rendering

#### iOS Behaviour
- **Display mode**: Non-interactive text field with system font
- **Selection**: Long-press enables text selection for copying
- **Keyboard**: Never invoked (field permanently disabled)
- **Scrolling**: Horizontal scroll for overflow text within field
- **Accessibility**: VoiceOver announces as "read-only text field"

#### Android Behaviour
- **Presentation**: Disabled Material Design text field
- **Interaction**: Tap-and-hold for copy options
- **Visual feedback**: No focus ring or interaction states
- **Text overflow**: Horizontal scrolling within field boundaries
- **Screen readers**: Announces computed value and read-only status

### Responsive Considerations
- Field maintains consistent height across viewports
- Font size preserves readability (minimum 16px)
- Touch targets maintain 44×44px minimum despite non-interactive status
- Computed values update seamlessly during device rotation

## Interaction Patterns

### Automatic Evaluation
- **Initial computation**: Template evaluates on form load
- **Real-time updates**: Re-evaluates on ANY field value change
- **Dependency tracking**: All templates re-compute simultaneously
- **Performance impact**: Multiple templates may affect form responsiveness

### User Interaction Limitations
- **No direct editing**: Field permanently read-only (hardcoded)
- **Copy operations**: Select and copy computed value only
- **No paste**: Cannot paste content into template field
- **No keyboard focus**: Tab navigation skips field
- **No manual override**: Users cannot correct computed values

### State Management
- **Value persistence**: Evaluated result stored in form state
- **Update cascade**: Template change triggers downstream conditions
- **Circular prevention**: Template fields filtered from variable context
- **Error resilience**: Invalid references render as empty strings

## Conditional Logic Support

### As Condition Source
Templates can trigger other fields' visibility:
```json
"template-status": {
  "component-name": "TemplatedStringField",
  "template": "{{priority}}-{{category}}"
},
"escalation-field": {
  "component-name": "TextField",
  "condition": {
    "operator": "contains",
    "field": "template-status",
    "value": "HIGH"
  }
}
```

### As Condition Target
Templates can be conditionally displayed:
```json
"summary-id": {
  "component-name": "TemplatedStringField",
  "template": "{{site}}-{{date}}-{{number}}",
  "condition": {
    "operator": "equal",
    "field": "show-summary",
    "value": true
  }
}
```

### Supported Operators
- All standard operators work with evaluated values
- Conditions see computed result, not template definition
- Real-time condition updates as template re-evaluates
- Empty evaluations trigger appropriate conditional responses

## Data Storage and Export

### Database Storage
- **Stored value**: Evaluated string result (e.g., "SITE-001-2024")
- **Not stored**: Template definition remains in notebook configuration
- **Update behaviour**: New evaluation overwrites previous value
- **Historical values**: Previous computed values not retained

### Export Formats
```json
// JSON Export
{
  "record_id": "rec_123",
  "template_field": "ARCH-001-2024"  // Computed value
}
```

```csv
// CSV Export
record_id,site,number,template_field
rec_123,ARCH,001,"ARCH-001-2024"
```

### Data Characteristics
- Recipients cannot determine value generation method
- Exported values remain static (won't update if template changes)
- Computed values maintain string type in all export formats
- Empty evaluations export as empty strings

## Common Patterns

### Example 1: Basic Human-Readable Identifier
```json
{
  "record-hrid": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Record ID",
      "name": "record-hrid",
      "template": "{{project-code}}-{{location}}-{{incrementer}}",
      "helperText": "Auto-generated identifier",
      "fullWidth": true
    },
    "validationSchema": [["yup.string"], ["yup.required"]],
    "initialValue": ""
  }
}
```
**Expected behaviour**: Generates "PROJ2024-SITE5-00045". Updates instantly as component fields change. Empty fields result in "PROJ2024--00045" (consecutive hyphens). Required validation ensures non-empty result.

### Example 2: Conditional Section Logic
```json
{
  "specimen-label": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Specimen Label",
      "name": "specimen-label",
      "template": "{{taxa}}{{#subspecies}}/{{subspecies}}{{/subspecies}}-{{#collector}}({{collector}}){{/collector}}{{number}}",
      "fullWidth": true
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
**Expected behaviour**: With all fields: "Eucalyptus/regnans-(J.Smith)00123". Without subspecies and collector: "Eucalyptus-00123". Conditional sections include/exclude based on field presence.

### Example 3: System Metadata Integration
```json
{
  "audit-stamp": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Audit Information",
      "name": "audit-stamp",
      "template": "Created: {{_CREATED_TIME}} by {{_CREATOR_NAME}} | Type: {{record-type}}{{#reviewed}} [REVIEWED]{{/reviewed}}",
      "helperText": "Automatic audit trail",
      "fullWidth": true
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
**Expected behaviour**: Displays "Created: 24-03-24 2:30pm by j.smith | Type: ARTEFACT [REVIEWED]". System variables provide defaults if null. Updates reviewed tag based on checkbox state.

### Example 4: Complex Nested Conditionals with Inverted Sections
```json
{
  "context-description": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Context Description",
      "name": "context-description",
      "template": "{{#primary}}Primary: {{primary}}{{#secondary}} / Secondary: {{secondary}}{{/secondary}}{{/primary}}{{^primary}}No classification assigned{{/primary}}",
      "fullWidth": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.minLength", 10, "Description too brief"]
    ],
    "initialValue": ""
  }
}
```
**Expected behaviour**: With primary="Occupation" and secondary="Domestic": "Primary: Occupation / Secondary: Domestic". With only primary: "Primary: Occupation". With neither: "No classification assigned". Minimum length validation ensures meaningful content.

## Troubleshooting Guide

| Issue | Symptoms | Diagnosis | Resolution |
|-------|----------|-----------|------------|
| Template shows empty | Field displays blank despite source fields having values | Template references may be incorrect or fields may be template fields | Verify field names match exactly, check if referencing other template fields (not allowed) |
| Validation failures | Required validation fails despite visible content | Template evaluating to empty string | Add static text to template or make source fields required |
| Not updating | Changes to source fields don't update template | Possible circular reference or performance issue | Check for template-to-template references, reduce template count |
| Shows literal braces | Display shows "{{field}}" instead of value | Field name incorrect or field is template type | Verify field exists, ensure not referencing template fields |
| System variables empty | {{_CREATOR_NAME}} shows "Unknown User" | System context not available | Normal for new records, values populate after save |
| Partial evaluation | Template only partially evaluates | Some referenced fields are undefined | Check all referenced fields exist in form |
| Performance lag | Form becomes sluggish with typing | Too many templates re-evaluating | Reduce template count or simplify template logic |

### Debug Checklist
- [ ] Verify all referenced field names match exactly (case-sensitive)
- [ ] Confirm referenced fields are not TemplatedStringFields
- [ ] Check template syntax for proper Mustache.js formatting
- [ ] Test with all source fields populated
- [ ] Verify template evaluation in Designer preview
- [ ] Check browser console for computation errors
- [ ] Confirm validation rules align with expected output
- [ ] Test conditional logic with empty and populated states

## Implementation Notes

### Technical Architecture
The Templated String Field employs Mustache.js for template evaluation, executing within the client-side form engine. Templates re-evaluate synchronously on every form value change through deep equality comparison. The implementation prevents circular references by systematically filtering all TemplatedStringFields from the template variable context. HTML escaping is disabled to preserve special characters in identifiers.

### Performance Considerations
- All templates re-evaluate on any field change (not selective)
- Multiple complex templates may impact form responsiveness
- Nested conditionals increase computation overhead
- Large forms with numerous templates require optimisation
- Consider limiting templates to essential identifiers only

### Circular Reference Prevention
```javascript
// Simplified prevention mechanism
if (fieldDetails['component-name'] === 'TemplatedStringField') {
  filterFields.push(fieldName);  // Excluded from context
}
```
Self-references and template-to-template references render as empty strings without error.

### Integration Points
- Form state manager: Triggers recomputation on value changes
- Validation engine: Validates computed results, not templates
- Conditional logic system: Uses evaluated values for conditions
- Export system: Outputs computed strings to all formats
- Database layer: Stores evaluated results as standard strings

## Best Practices

### Template Design
- Include static text to prevent completely empty evaluations
- Place critical fields early in template for visibility
- Use hyphens or underscores as reliable separators
- Limit conditional sections to improve readability
- Test templates with empty, partial, and complete data

### Validation Strategy
- Make source fields required if template has required validation
- Use minLength validation cautiously with conditional sections
- Consider pattern matching for standardised formats
- Document expected format in helperText for user clarity

### Performance Optimisation
- Minimise template count per form (ideally 1-3)
- Avoid deeply nested conditional logic
- Use simple concatenation where possible
- Consider computational cost for large datasets
- Monitor form responsiveness during testing

### Data Quality
- Establish source field validation to ensure quality inputs
- Document template patterns for data managers
- Plan for empty field scenarios in template design
- Consider downstream system requirements for generated IDs
- Implement consistent naming conventions across projects

## See Also

- **[TextField](./TextField.md)** - For user-editable text input
- **[BasicAutoIncrementer](./BasicAutoIncrementer.md)** - Often used within templates for sequential numbering
- **[Select Field](./SelectField.md)** - Provides controlled vocabulary for template components
- **[DateTimeField](./DateTimeField.md)** - Date components for temporal identifiers
- **[Conditional Logic Guide](../guides/ConditionalLogic.md)** - Advanced conditional visibility patterns
- **[Validation Rules Reference](../reference/ValidationRules.md)** - Complete validation schema options
- **[Form Design Best Practices](../guides/FormDesign.md)** - Optimising form performance with templates