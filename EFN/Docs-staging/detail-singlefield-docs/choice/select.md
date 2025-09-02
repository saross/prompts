# Select Field - Complete Third-Draft Documentation

## Overview

The Select field provides single-choice selection from a dropdown list, offering space-efficient presentation of controlled vocabularies through Material-UI's consistent interface across all platforms. This field type returns `faims-core::String` values and serves as the standard solution for single selection from more than 5-7 options, where RadioGroup would consume excessive screen space. While the component lacks certain technical refinements (error message display, native mobile pickers, accessibility attributes), it delivers reliable structured data collection with human-readable exports. The Designer interface enforces sensible defaults, ensuring option values equal their labels for immediate data interpretability without requiring codebooks or post-processing.

## Common Use Cases

• **Taxonomic classification** - Species lists, artefact types, material categories (10-50 options)
• **Site or context types** - Archaeological periods, depositional environments, feature types
• **Standardised descriptions** - Condition states, preservation levels, completeness percentages
• **Administrative categories** - Project phases, team members, institutional codes
• **Geographical regions** - Countries, states, survey areas, management zones
• **Equipment or methods** - Instrument types, sampling strategies, analysis techniques
• **Temporal periods** - Geological eras, historical periods, seasonal indicators

## Core Configuration

### Required Parameters

```json
{
  "component-namespace": "faims-custom",
  "component-name": "Select",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "ElementProps": {
      "options": [
        {"value": "Option 1", "label": "Option 1"},
        {"value": "Option 2", "label": "Option 2"}
      ]
    }
  }
}
```

### Optional Parameters

```json
{
  "component-parameters": {
    "label": "Field Label",
    "helperText": "Choose one option from the list",
    "fullWidth": true,
    "variant": "outlined",
    "required": false,
    "select": true,
    "disabled": false
  },
  "validationSchema": [["yup.string"]],
  "initialValue": "",
  "meta": {
    "annotation": {"include": true, "label": "notes"},
    "uncertainty": {"include": false}
  }
}
```

### Designer vs JSON Configuration

**Designer Interface** (Primary workflow):
- Creates options where value = label automatically
- Exposes: label, helperText, required, options, conditions
- Protects from invalid configurations
- No preview capability (must deploy to test)

**JSON Editing** (Advanced):
- Can specify different values and labels (not recommended)
- Access to fullWidth, variant, validation schemas
- Risk of Designer overwriting custom configurations
- Required for complex validation rules

## Validation Rules

| Validation Type | Configuration | Behaviour | User Experience |
|-----------------|---------------|-----------|-----------------|
| Required | `["yup.required"]` | Blocks submission if empty | Silent failure - no visual feedback |
| String Type | `["yup.string"]` | Always passes | Automatic - enforced by component |
| Min Length | `["yup.minLength", 3]` | Validates selection length | No error display |
| Pattern Match | `["yup.matches", "pattern"]` | Validates against regex | No error display |
| Custom Message | `["yup.required", "Please select"]` | Custom error text | Not displayed to user |

### Validation Behaviour
- **On change**: Validation runs but errors not displayed
- **On blur**: No validation triggered
- **On submit**: Final validation blocks submission silently
- **In practice**: UI prevents invalid selections, making most validation redundant
- **Note**: Option membership validation not implemented (values not checked against options array)

## Display Behaviour

### Desktop Rendering
- **Component**: Material-UI Select dropdown
- **Width**: Typically fullWidth (spans container)
- **Activation**: Click or Space key opens dropdown
- **List presentation**: Scrollable dropdown with hover states
- **Helper text**: Displays above field (non-standard position)
- **Error indication**: None (component limitation)
- **Selection feedback**: Immediate display of selected option

### Mobile Rendering

#### iOS Behaviour
- **Component**: Material-UI dropdown (not native iOS picker)
- **Touch targets**: 48px height MenuItems (meets minimum standards)
- **Scrolling**: Standard touch scroll within dropdown
- **Selection**: Direct tap on option
- **Keyboard**: Virtual keyboard not triggered
- **Landscape**: Dropdown adjusts to available height

#### Android Behaviour
- **Component**: Same Material-UI dropdown (consistent with iOS)
- **Touch feedback**: Material ripple effects on selection
- **Back button**: Closes dropdown without selection
- **Scrolling**: Smooth scroll with momentum
- **Selection persistence**: Maintains selection on rotation

### Platform Consistency
Select prioritises uniform experience over platform-native patterns, reducing training requirements but potentially surprising users expecting native controls.

## Interaction Patterns

### Selection Flow
1. **Closed state**: Displays current selection or placeholder
2. **Opening**: Click/tap on field or dropdown arrow
3. **Navigation**: Scroll or arrow keys to find option
4. **Selection**: Click/tap on desired option
5. **Confirmation**: Dropdown closes, displaying selection

### Keyboard Support (Desktop)
- **Tab**: Focus field
- **Space/Enter**: Open dropdown when focused
- **Arrow Up/Down**: Navigate options
- **Enter**: Select highlighted option
- **Escape**: Close without selection
- **Type-ahead**: Single character jump (resets after ~1 second)

### Touch Interaction (Mobile)
- **Single tap**: Opens dropdown
- **Scroll**: Standard touch scrolling through options
- **Tap option**: Makes selection and closes
- **Tap outside**: Closes without selection
- **No gesture support**: Swipe gestures not implemented

### Deselection Behaviour
- **No built-in clear**: Cannot deselect without choosing empty option
- **Workaround**: Include "None" or empty option if null state needed
- **Contrast with RadioGroup**: RadioGroup allows toggle deselection

## Conditional Logic Support

### As Trigger
```json
{
  "condition": {
    "field": "site-type",
    "operator": "equal", 
    "value": "burial"
  }
}
```

### As Target
Select fields can be conditionally shown/hidden based on other field values.

### Limitations
- **Operators**: Only `equal` supported (no `isEmpty`, `contains`, `notEqual`)
- **Empty check**: Must use `{"operator": "equal", "value": ""}` 
- **Multiple values**: No OR logic for checking multiple options
- **Complex logic**: Requires multiple condition objects

## Data Storage and Export

### Database Storage
- **Type**: String value from selected option
- **Format**: Exact option value (Designer ensures human-readable)
- **Null state**: Empty string "" when no selection

### Export Behaviour
```csv
"Field Label","Other Field"
"Archaeological Site","Value2"
"Historical Building","Value3"
```

### Designer Advantage
- **Value = Label**: Designer enforces identical strings
- **Result**: Exports are immediately interpretable
- **No codes**: Avoids "001", "002" requiring lookup tables
- **Example**: Selecting "Archaeological Site" exports as "Archaeological Site"

### JSON Configuration Warning
If manually setting different values/labels in JSON:
```json
{"value": "001", "label": "Archaeological Site"}
```
Exports only "001", losing human readability.

## Common Patterns

### Example 1: Site Classification (Heritage Context)
```json
{
  "site-type": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Site Type",
      "name": "site-type",
      "helperText": "Select the primary site classification",
      "fullWidth": true,
      "required": true,
      "ElementProps": {
        "options": [
          {"value": "Artefact scatter", "label": "Artefact scatter"},
          {"value": "Rock art", "label": "Rock art"},
          {"value": "Shell midden", "label": "Shell midden"},
          {"value": "Stone arrangement", "label": "Stone arrangement"},
          {"value": "Burial", "label": "Burial"},
          {"value": "Historic structure", "label": "Historic structure"},
          {"value": "Other", "label": "Other"}
        ]
      }
    },
    "validationSchema": [["yup.string"], ["yup.required"]],
    "initialValue": "",
    "meta": {
      "annotation": {"include": true, "label": "classification notes"},
      "uncertainty": {"include": true, "label": "confidence"}
    }
  }
}
```
**Heritage Usage**: Standard vocabulary from NSW Heritage Office site types. The "Other" option typically triggers conditional text field for detailed description.

### Example 2: Condition Assessment with Null Option
```json
{
  "condition-state": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Condition",
      "name": "condition-state",
      "helperText": "Assess current preservation state",
      "fullWidth": true,
      "ElementProps": {
        "options": [
          {"value": "", "label": "-- Not assessed --"},
          {"value": "Excellent", "label": "Excellent"},
          {"value": "Good", "label": "Good"},
          {"value": "Fair", "label": "Fair"},
          {"value": "Poor", "label": "Poor"},
          {"value": "Destroyed", "label": "Destroyed"}
        ]
      }
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "",
    "meta": {
      "annotation": {"include": true, "label": "condition notes"}
    }
  }
}
```

### Example 3: Triggering Conditional Fields
```json
{
  "material-type": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Material Type",
      "name": "material-type",
      "fullWidth": true,
      "ElementProps": {
        "options": [
          {"value": "Ceramic", "label": "Ceramic"},
          {"value": "Glass", "label": "Glass"},
          {"value": "Metal", "label": "Metal"},
          {"value": "Other", "label": "Other"}
        ]
      }
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  },
  "other-material": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Specify Other Material",
      "name": "other-material"
    },
    "condition": {
      "field": "material-type",
      "operator": "equal",
      "value": "Other"
    }
  }
}
```

## Troubleshooting Guide

| Issue | Symptoms | Cause | Resolution |
|-------|----------|-------|------------|
| No error messages | Required field fails silently | Component lacks error display | Train users on required fields; form structure indicates requirements |
| Slow dropdown | Lag when opening with many options | No virtualisation for large lists | Limit to <50 options; consider categories or different field type |
| Can't deselect | No way to clear selection | No built-in clear button | Include empty option: `{"value": "", "label": "-- None --"}` |
| Preview missing | Can't test in Designer | Feature not implemented | Save and deploy to test environment; preview on roadmap |
| Can't convert type | Must delete RadioGroup to create Select | No field type conversion | Note options, delete field, recreate as Select; conversion planned |
| Touch precision | Hard to select on mobile | Default touch targets | Ensure clean/dry hands; consider RadioGroup for frequent selections |
| Data shows codes | CSV has "001" not "Archaeological Site" | Manual JSON editing with different value/label | Use Designer; ensure value = label |

### Debug Checklist
- [ ] Verify field name matches exactly in conditions
- [ ] Check initialValue is empty string "" not null
- [ ] Confirm all options have both value and label
- [ ] Test with <20 options first for performance
- [ ] Deploy to test environment to verify behaviour
- [ ] Include empty option if null state needed
- [ ] Use Designer for option configuration
- [ ] Check field is marked required if validation expected

## Implementation Notes

### Technical Architecture
The Select component wraps Material-UI's Select with Formik integration, using FieldWrapper for label and helper text positioning. The component enforces single selection through hardcoded configuration, preventing multiple selection despite parameter suggestions. All platforms receive identical Material-UI dropdowns rather than native controls, prioritising consistency over platform conventions.

### Current Limitations
- **No error display**: FormHelperText component absent
- **No ARIA attributes**: Accessibility support missing
- **No search**: Type-ahead limited to single character
- **No virtualisation**: All options render immediately
- **Static options only**: No dynamic loading capability
- **No option validation**: Values not checked against options array

### Designer Constraints
- Enforces value = label for human readability
- No preview capability (must deploy to test)
- No field type conversion (must recreate)
- Limited parameter exposure (many require JSON editing)

### Performance Characteristics
- **<20 options**: Optimal performance
- **20-50 options**: Acceptable with minor lag
- **50-100 options**: Noticeable performance degradation
- **>100 options**: Severe issues, consider alternatives

## Best Practices

### Option Design
- Keep option text concise but clear
- Order logically (alphabetical, chronological, or by frequency)
- Include "Other" option with conditional text field for edge cases
- Add empty option if null state is valid
- Limit to 20-30 options for optimal mobile experience

### Form Design
- Use Select for 8+ options (RadioGroup for fewer)
- Position after fields that determine available options
- Group related Selects together
- Provide clear helper text for option selection criteria
- Consider breaking very long lists into cascading Selects

### Data Quality
- Establish controlled vocabularies early in project
- Use consistent option sets across related forms
- Document option meanings in project documentation
- Plan for vocabulary evolution (additions more than deletions)
- Test option lists with domain experts before deployment

### Accessibility Considerations
- Current implementation has significant gaps
- Provide clear labels and helper text as compensation
- Consider RadioGroup for critical selections (better visibility)
- Document selection requirements in form instructions
- Plan for accessibility improvements in future versions

## Cross-References & Dependencies

### Alternative Choice Fields
- **[RadioGroup](./RadioGroup.md)** - For 2-7 options where all should be visible
  - *Relationship*: Functional alternative for small option sets
  - *Trade-off*: Better visibility but more space, has similar error display issues
- **[Checkbox](./Checkbox.md)** - For simple boolean choices
  - *Relationship*: Use instead of Select with Yes/No options when boolean value needed
  - *Difference*: Returns true/false not string values

### Multi-Selection Variants
- **[MultiSelect](./MultiSelect.md)** - For multiple selection requirements
  - *Relationship*: Similar dropdown interface but allows multiple choices
  - *Migration*: Cannot convert Select to MultiSelect without data transformation
- **[AdvancedSelect](./AdvancedSelect.md)** - For hierarchical vocabularies (beta)
  - *Relationship*: Use when options have parent-child relationships
  - *Constraint*: More complex, tablet-optimised, beta status

### Common Companion Fields
- **[TextField](./TextField.md)** - Often paired for "Other" option specification
  - *Pattern*: Select triggers conditional TextField when "Other" selected
  - *Example*: See Common Pattern #3 for implementation
- **[TemplatedStringField](./TemplatedStringField.md)** - Frequently references Select values
  - *Usage*: Select provides controlled vocabulary for template components
  - *Validation*: Ensure Select options remain stable for template consistency

### Validation Dependencies
- Select validation does not cascade to dependent fields
- Conditional fields based on Select only validate when visible
- Required Select fields block form submission silently (no error display)

### Export Relationships
- CSV export shows Select values in columns with field label as header
- Related conditional fields appear as separate columns
- No automatic codebook generation for option meanings

### Related Guides
- **[Conditional Logic Guide](../guides/ConditionalLogic.md)** - Showing/hiding fields based on selection
- **[Vocabulary Design Guide](../guides/VocabularyDesign.md)** - Best practices for option lists
- **[Form Design Patterns](../guides/FormDesign.md)** - Optimal Select placement in forms

---

*Component Status: Production-ready with known limitations. Error display and accessibility improvements on roadmap. Designer workflow enhancements (preview, field conversion) planned.*