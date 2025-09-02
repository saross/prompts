# Checkbox Field - Complete Third-Draft Documentation

## Overview

The Checkbox field (`faims-custom::Checkbox`) provides binary state capture through a Material-UI checkbox component, returning `faims-core::Boolean` values. As the **only boolean field type in Fieldmark**, Checkbox serves dual purposes: simple true/false data capture and consent/acknowledgment workflows. Unlike RadioGroup and Select which return strings, Checkbox returns actual boolean primitives, making it ideal for programmatic logic. However, critical UX and accessibility issues limit its effectiveness—the field label is not clickable (violating standard checkbox behaviour), and no ARIA attributes are implemented. Despite these limitations, Checkbox provides the most reliable error display among all choice fields, properly showing both visual indicators and error messages.

## Common Use Cases

• **Consent and agreements** - Terms acceptance, privacy policy acknowledgment, data usage consent
• **Binary archaeological indicators** - Presence/absence of features (charcoal present, bioturbation observed)
• **Procedural confirmations** - Safety checks completed, equipment calibrated, protocols followed
• **Optional enhancements** - Include photographs, request review, generate report
• **Data quality flags** - Provisional data, requires verification, peer reviewed
• **Workflow controls** - Skip section, detailed recording mode, offline mode enabled
• **Heritage compliance** - Aboriginal heritage present, environmental clearance obtained, council notified
• **Export filters** - Include in report, export to GIS, share with team

## Core Configuration

### Required Parameters

```json
{
  "component-namespace": "faims-custom",
  "component-name": "Checkbox",
  "type-returned": "faims-core::Boolean",
  "component-parameters": {
    "name": "field-name",
    "label": "Checkbox label"
  }
}
```

### Optional Parameters

```json
{
  "component-parameters": {
    "id": "checkbox-field-1",
    "helperText": "Additional guidance for users",
    "advancedHelperText": "Extended help with more detail",
    "required": false  // Note: doesn't enforce "must be checked"
  },
  "validationSchema": [
    ["yup.boolean"],
    ["yup.oneOf", [true], "You must accept to continue"]
  ],
  "initialValue": false,  // Designer enforces false
  "meta": {
    "annotation": {"include": false, "label": "notes"},
    "uncertainty": {"include": false, "label": "uncertain"}
  }
}
```

### Designer vs JSON Configuration

**Designer Exposes**:
- Label text
- Helper text and advanced helper text
- Required checkbox (misleading - see validation notes)
- Field name and ID
- Meta toggles (annotation, uncertainty)

**JSON-Only Properties**:
- `initialValue`: Can set to `true` for pre-checked (Designer forces `false`)
- Complex validation schemas beyond basic required
- Deprecated MUI props (FormControlLabelProps, FormHelperTextProps)

**Designer Limitations**:
- Cannot configure must-be-checked validation
- Cannot set initial checked state
- No custom editor (unlike Select/RadioGroup)
- No preview capability

## Validation Rules

### Validation Semantics

| Validation Type | Configuration | Actual Behaviour | Error Message | Platform Impact |
|-----------------|---------------|------------------|---------------|-----------------|
| Boolean type | `["yup.boolean"]` | Accepts true/false/null/undefined | "Must be a boolean" | Consistent across all |
| Required field | `["yup.required"]` | **Misleading!** Prevents null/undefined but allows false | "This field is required" | May confuse mobile users |
| Must be checked | `["yup.oneOf", [true], "Message"]` | Only accepts true (checkbox must be checked) | Custom message | Critical for consent forms |
| Must be unchecked | `["yup.oneOf", [false]]` | Only accepts false | "Must be unchecked" | Rare use case |
| Explicit selection | `["yup.oneOf", [true, false], "Message"]` | Requires deliberate true OR false | Custom message | For critical decisions |

### Critical Validation Clarification

**"Required" for checkboxes does NOT mean "must be checked":**
- `["yup.required"]` allows `false` (unchecked) as valid
- For consent forms use: `["yup.oneOf", [true], "You must accept"]`
- Designer's "required" checkbox creates confusion
- No cross-field validation support (no yup.when)

### Validation Timing
- **On mount**: Validation runs but errors hidden (not touched)
- **On change**: Field validates immediately, marks as touched
- **On blur**: Revalidates and displays any errors
- **On submit**: All fields validated, all errors shown

### Error Display Implementation

**Checkbox has the BEST error display among choice fields:**
- ✅ Shows error message text below field
- ✅ Red color applied to checkbox and label
- ✅ Respects touched state (errors after interaction)
- ✅ Uses FormHelperText correctly

Compare with:
- RadioGroup: ❌ Red color only, no text
- Select: ❌ No error indication at all

## Display Behaviour

### Desktop Rendering
- **Checkbox size**: 24×24px icon, 48×48px touch target
- **Label position**: Displayed above by FieldWrapper
- **Error messages**: Below checkbox via FormHelperText
- **Helper text**: Below error messages when present
- **Styling**: Material-UI custom SVG checkbox (not native)
- **Animation**: 300ms transition, ripple effect on click

### Mobile Rendering

#### iOS Behaviour
- **Touch target**: 48×48px checkbox area only
- **Label interaction**: ❌ NOT tappable (UX failure)
- **Visual style**: Material-UI (not iOS native)
- **Haptic feedback**: None
- **Keyboard**: Not applicable (touch only)

#### Android Behaviour
- **Touch target**: 48×48px checkbox area only
- **Label interaction**: ❌ NOT tappable (UX failure)
- **Visual style**: Material-UI (not Android native)
- **Ripple effect**: Standard Material Design ripple
- **Keyboard**: Not applicable (touch only)

### Critical UX Issue
**Label text is NOT clickable** - users must tap the small checkbox target, violating standard checkbox behaviour and making mobile interaction difficult.

## Interaction Patterns

### Standard Interaction Flow
1. User sees unchecked box with label above
2. Must click/tap directly on checkbox (not label)
3. Checkbox animates to checked state
4. Value immediately updates to true
5. Any dependent conditional logic triggers
6. Field marked as touched for validation

### State Transitions
- **Unchecked → Checked**: Click/tap checkbox, value becomes `true`
- **Checked → Unchecked**: Click/tap checkbox, value becomes `false`
- **Initial state**: Always `false` from Designer (JSON can set `true`)
- **Null handling**: null/undefined interpreted as `false`

### Accessibility Failures
⚠️ **Multiple WCAG 2.1 Level A violations:**
- ❌ No aria-required attribute
- ❌ No aria-invalid for errors
- ❌ No aria-describedby for helper text
- ❌ Label not programmatically associated
- ❌ Screen readers cannot announce field purpose

## Conditional Logic Support

### As Condition Source
```json
"conditions": [
  {
    "field": "include-photos",
    "operator": "equal",
    "value": true
  }
]
```

### Available Operators
- `equal`: Check if true (checked) or false (unchecked)
- `not-equal`: Inverse of equal
- ❌ No `isEmpty` operator
- ❌ Cannot detect untouched vs explicitly unchecked

### State Detection Limitations
- Cannot distinguish null/undefined from false
- Both render as unchecked
- No "never touched" detection

## Data Storage and Export

### Database Storage
- **Type**: Boolean primitive (true/false)
- **Not stored**: null/undefined converted to false
- **No audit trail**: Previous states not retained

### Export Formats

| Format | True Value | False Value | Null Handling |
|--------|-----------|-------------|---------------|
| JSON | `true` | `false` | Exported as `false` |
| CSV | "true" | "false" | Exported as "false" |

### Export Characteristics
- String representation in CSV (not 1/0)
- Boolean primitives in JSON
- Not configurable
- Consistent across all export types

## Common Patterns

### Example 1: Terms Acceptance (Must Be Checked)
```json
{
  "terms-accept": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "terms-accept",
      "label": "I accept the terms and conditions",
      "helperText": "You must accept to continue",
      "required": true  // Visual indicator only
    },
    "validationSchema": [
      ["yup.boolean"],
      ["yup.oneOf", [true], "You must accept the terms to proceed"]
    ],
    "initialValue": false
  }
}
```

### Example 2: Optional Enhancement Flag
```json
{
  "include-detailed": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "include-detailed",
      "label": "Record detailed measurements",
      "helperText": "Check to show additional measurement fields"
    },
    "validationSchema": [["yup.boolean"]],
    "initialValue": false,
    "meta": {
      "persistent": true  // Carry forward to new records
    }
  }
}
```

### Example 3: Data Quality Indicator with Persistence
```json
{
  "peer-reviewed": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "peer-reviewed",
      "label": "Data peer reviewed",
      "advancedHelperText": "Check after secondary verification completed"
    },
    "validationSchema": [["yup.boolean"]],
    "initialValue": false,
    "meta": {
      "displayParent": true,  // Show in parent record summary
      "persistent": true      // Carry value to new records
    }
  }
}
```

### Example 4: Migration from RadioGroup Pattern
```json
{
  "heritage-present": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "heritage-present",
      "label": "Aboriginal heritage identified",
      "helperText": "Previously Yes/No radio - now checkbox for boolean logic",
      "required": true
    },
    "validationSchema": [
      ["yup.boolean"],
      ["yup.oneOf", [true, false], "Must explicitly indicate heritage status"]
    ],
    "initialValue": false,
    "meta": {
      "annotation": {"include": true, "label": "heritage notes"},
      "displayParent": true
    }
  }
}
```
**Migration note**: Converted from RadioGroup with options [{value: "yes", label: "Yes"}, {value: "no", label: "No"}]. All conditional logic updated from string comparison (`equal: "yes"`) to boolean (`equal: true`). Validation ensures explicit selection despite being checkbox.

## Troubleshooting Guide

| Issue | Symptoms | Diagnosis | Resolution |
|-------|----------|-----------|------------|
| Required not working | Checkbox can be unchecked despite required | "Required" doesn't mean "must be checked" | Use `["yup.oneOf", [true]]` for must-be-checked |
| Label not clickable | Must click checkbox itself, not label text | Label not properly associated | Known issue - train users to click checkbox |
| No initial checked | Cannot set checkbox to start checked in Designer | Designer forces false | Edit JSON to set `initialValue: true` |
| Validation confusing | Error appears when unchecked but field is "required" | Misunderstanding of boolean validation | Required prevents null, not false |
| Can't detect untouched | Conditional logic treats untouched same as unchecked | No isEmpty operator | Use different field type or track interaction separately |
| Multiple checkboxes | Can't enforce "at least one checked" across checkboxes | Individual checkboxes don't cross-validate | Use MultiSelect with expandedChecklist instead |
| Export shows strings | CSV has "true"/"false" not 1/0 | Standard boolean serialization | Post-process if numeric needed |

### Debug Checklist
- [ ] Verify validation schema matches intent (required vs must-be-checked)
- [ ] Check if trying to make label clickable (won't work)
- [ ] Confirm initialValue in JSON if pre-checked needed
- [ ] Test validation with both checked and unchecked states
- [ ] Verify conditional logic uses equal/not-equal (no isEmpty)
- [ ] Check error messages display properly (they should!)
- [ ] Consider MultiSelect if multiple related checkboxes needed
- [ ] Test on mobile - small touch target may frustrate users

## Implementation Notes

### Technical Architecture
- Material-UI Checkbox wrapped in Formik Field
- FieldWrapper provides label display (not connected to checkbox)
- FormControl provides error styling
- FormHelperText displays validation messages
- No memoization or performance optimizations
- Each checkbox renders independently

### Historical Context & Migration Patterns

**Legacy RadioGroup Conversion**: Many existing notebooks use RadioGroup with Yes/No options for boolean data. When migrating to Checkbox:
1. Change `component-name` from "RadioGroup" to "Checkbox"
2. Remove `ElementProps.options` array
3. Change `type-returned` from "faims-core::String" to "faims-core::Boolean"
4. Update all conditional logic checking for string values
5. Revise validation schemas from string to boolean validators
6. Test thoroughly as export format changes from "yes"/"no" to "true"/"false"

**Heritage Sector Usage**: Archaeological and heritage projects frequently use checkboxes for:
- Presence/absence recording (charcoal, bioturbation, disturbance)
- Compliance tracking (permits obtained, stakeholders notified)
- Quality assurance (peer reviewed, photos taken, GPS recorded)
- Workflow control (detailed recording, skip section, provisional data)

### Performance Considerations
- Acceptable: Up to 20-30 checkboxes per form
- Degraded: 50+ individual checkboxes cause lag
- Unusable: 100+ checkboxes significantly impact performance
- Alternative: Use MultiSelect for many related options

### Accessibility Status
⚠️ **Not compliant with WCAG 2.1 Level A**
- Missing required ARIA attributes
- Label association broken
- Screen reader support inadequate
- Keyboard navigation works but not announced

### Known Workarounds
- **Label clicking**: Train users to click checkbox directly, not label
- **Initial state**: Edit JSON manually for pre-checked boxes
- **Group validation**: Use MultiSelect instead of multiple checkboxes
- **Accessibility**: Add explicit instructions in helperText for screen reader users

## Best Practices

### When to Use Checkbox
✅ **Good for:**
- Binary states where false is meaningful
- Consent and acknowledgments
- Optional features/filters
- Boolean flags for analysis

❌ **Avoid for:**
- When explicit "No" selection needed (use RadioGroup)
- Multiple related options (use MultiSelect)
- When null state must be distinct from false
- High-stakes data requiring clear negative confirmation

### Validation Strategy
- Use `["yup.oneOf", [true]]` for mandatory consent
- Make source data required if checkbox controls critical workflow
- Document validation clearly in helperText
- Test both checked and unchecked states

### Mobile Optimisation
- Add clear visual indicators for touch targets
- Consider larger custom styling for critical checkboxes
- Train users that label text is not clickable
- Provide clear helper text about what checking means

## Cross-References & Dependencies

### Required Companions
- **None** - Checkbox operates independently without required companion fields

### Common Pairings
- **[TextField](./TextField.md)** - Often paired for "Other (please specify)" patterns where checkbox reveals text input via conditional logic
- **[TemplatedString](./TemplatedString.md)** - Checkbox state frequently used in template conditionals to include/exclude sections
- **[Annotation/Uncertainty](./MetaFields.md)** - When `meta.annotation.include: true`, provides additional context for binary decisions

### Mutual Exclusions
- **[RadioGroup](./RadioGroup.md)** with Yes/No options - Don't use both for same data; choose based on whether you need boolean (Checkbox) or string values (RadioGroup)
- **Multiple individual Checkboxes** for related options - Use [MultiSelect](./MultiSelect.md) instead for group validation

### Validation Cascades
- **Child form validation**: Checkbox state can control whether child forms require completion
- **Section validation**: Required checkbox can block section completion until checked
- **Cross-field validation**: Limited - cannot use yup.when() for conditional requirements based on other fields

### Dependent Fields
Fields commonly dependent on Checkbox values:
- **Conditional text fields**: Shown/hidden based on checkbox true/false state
- **Photo fields**: May become required when "Photos included" checkbox is true
- **Measurement fields**: Displayed when "Detailed recording" checkbox is checked

### Migration Relationships
- **From RadioGroup**: When converting Yes/No RadioGroup to Checkbox, must update all conditional logic from string comparison (`"yes"`) to boolean (`true`)
- **To MultiSelect**: When multiple related checkboxes needed, migrate to MultiSelect with `expandedChecklist: true`

## See Also

- **[RadioGroup](./RadioGroup.md)** - For explicit Yes/No/Unknown selection with string values
- **[Select](./Select.md)** - For Yes/No with additional options like "Not Applicable"
- **[MultiSelect](./MultiSelect.md)** - For multiple checkbox-style selections with group validation
- **[Conditional Logic Guide](../guides/ConditionalLogic.md)** - Boolean conditions and field dependencies
- **[Validation Patterns](../guides/ValidationPatterns.md)** - Boolean validation examples and consent patterns
- **[Accessibility Guide](../guides/Accessibility.md)** - WCAG compliance requirements and workarounds