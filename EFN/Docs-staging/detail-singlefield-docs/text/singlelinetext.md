# TextField (Single-line Text)

## Overview

The TextField component provides single-line text input functionality within the Fieldmark ecosystem, serving as the fundamental mechanism for capturing brief, unconstrained textual data. Two implementations exist within the current architecture: the established `formik-material-ui/TextField`, which constitutes the production standard across existing notebooks, and the enhanced `faims-custom/FAIMSTextField`, which incorporates additional user experience refinements whilst maintaining compatibility with core functionality. Both variants restrict content to a single line, making them optimal for identifiers, labels, and brief descriptive content typically not exceeding 50 characters in field conditions.

## Common Use Cases

- **Site identifiers and codes**: Recording alphanumeric designations such as "SITE-2025-001" or heritage register numbers
- **Personnel names and roles**: Capturing recorder names, principal investigators, or institutional contacts
- **Brief descriptive labels**: Specimen identifiers, artefact codes, or sample designations requiring concise notation
- **Contextual annotations**: Short observational notes or qualifying statements accompanying primary data
- **Reference numbers**: External database identifiers, catalogue numbers, or cross-referencing codes
- **Administrative metadata**: Project codes, permit numbers, or institutional reference identifiers

## Core Configuration

### Required Properties
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-identifier",
    "label": "Field Label"
  }
}
```

### Optional Properties
```json
{
  "component-parameters": {
    "helperText": "Guidance text displayed below field",
    "placeholder": "Ghosted text within empty field",
    "required": false,
    "fullWidth": true,
    "variant": "outlined",
    "disabled": false,
    "InputProps": {
      "type": "text"
    }
  },
  "validationSchema": [["yup.string"]],
  "initialValue": "",
  "meta": {
    "annotation": {"include": true, "label": "annotation"},
    "uncertainty": {"include": false, "label": "uncertainty"}
  }
}
```

### Property Specifications

#### Required Properties
- **component-namespace** (`string`): Either "formik-material-ui" (standard) or "faims-custom" (enhanced)
- **component-name** (`string`): "TextField" for standard, "FAIMSTextField" for enhanced variant
- **type-returned** (`string`): Always "faims-core::String" for text data persistence
- **name** (`string`): Unique field identifier matching field-id
- **label** (`string`): Human-readable label displayed above input

#### Optional Properties
- **helperText** (`string`): Persistent instructional text beneath field
- **placeholder** (`string`): Ghosted prompt text in empty fields
- **required** (`boolean`): Enforces completion before form submission
- **fullWidth** (`boolean`): Expands field to container width (defaults true for FAIMSTextField)
- **variant** (`string`): Visual style – "outlined", "filled", or "standard"
- **disabled** (`boolean`): Prevents user interaction when true
- **InputProps** (`object`): Configures input behaviour, particularly type attribute for mobile keyboards

### Enhanced Variant Configuration (FAIMSTextField)
```json
{
  "component-namespace": "faims-custom",
  "component-name": "FAIMSTextField",
  "component-parameters": {
    "advancedHelperText": "## Extended Help\n\nMarkdown-formatted detailed guidance"
  }
}
```

The FAIMSTextField variant provides additional parameters:
- **advancedHelperText**: Rich text help accessible via info icon, supporting Markdown formatting
- Automatic whitespace trimming on input
- Enhanced visual presentation with bold labels and structured layout

## Validation Rules

### Built-in Validation
- **Type validation**: Enforces string data type through Yup schema
- **HTML5 validation**: Browser-native text input constraints
- **Required field validation**: When `required: true`, prevents empty submission
- **Touched-first validation**: Errors display only after field focus and blur, preventing premature error display

### Configurable Validation
| Rule | Schema | Purpose | Error Message |
|------|--------|---------|---------------|
| required | `["yup.required", "Field is required"]` | Mandatory field enforcement | "Field is required" |
| min length | `["yup.min", 3, "Minimum 3 characters"]` | Enforces minimum content | "Minimum 3 characters" |
| max length | `["yup.max", 50, "Maximum 50 characters"]` | Prevents excessive length | "Maximum 50 characters" |
| matches | `["yup.matches", /^[A-Z]/, "Must start with capital"]` | Pattern enforcement | Custom message |
| email format | `["yup.email", "Invalid email"]` | Email validation | "Invalid email" |

### Validation Examples
```json
{
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Site code is mandatory"],
    ["yup.matches", "^[A-Z]{2}[0-9]{4}$", "Format: XX9999"]
  ]
}
```

### Error Messages
| Validation State | Visual Presentation | Message Location | User Action |
|-----------------|---------------------|------------------|-------------|
| Required empty | Red border + red text | Below field | Enter any value |
| Pattern mismatch | Red border + red text | Below field | Match specified format |
| Length violation | Red border + red text | Below field | Adjust content length |
| Valid after error | Border returns to normal | Error text removed | Continue to next field |

## Display Behaviour

### Desktop Rendering
- **Input element**: Standard HTML text input with Material-UI styling
- **Width behaviour**: Respects `fullWidth` parameter, defaulting to container constraints
- **Label positioning**: Above field, left-aligned, bold for FAIMSTextField variant
- **Helper text**: Small grey text beneath input, replaced by red error text when invalid
- **Visual hierarchy**: FAIMSTextField provides enhanced spacing and typography (h5 labels)

### Mobile Rendering
#### iOS Behaviour
- **Keyboard type**: Standard text keyboard unless configured via InputProps
- **Auto-capitalisation**: Sentences by default (OS-controlled)
- **Auto-correction**: Enabled by default (OS-controlled)
- **Predictive text**: Active unless explicitly disabled
- **Font sizing**: Minimum 16px prevents zoom on focus

#### Android Behaviour
- **Keyboard type**: Standard text input with OS-specific layout
- **Auto-capitalisation**: Sentences by default (varies by keyboard app)
- **Voice input**: Available through keyboard interface
- **Gesture typing**: Supported where keyboard provides
- **Suggestion bar**: Displayed based on keyboard settings

### Responsive Considerations
- Touch targets maintain 44×44px minimum for accessibility
- Field width adjusts to container breakpoints
- Label remains above field at all viewport widths
- Virtual keyboard does not obscure field on focus

## Interaction Patterns

### User Input Methods
- **Keyboard entry**: Primary input mechanism across platforms
- **Voice dictation**: Platform-dependent availability
- **Paste operations**: Full support for clipboard content
- **Auto-fill**: Browser and password manager integration
- **Barcode scanner input**: When configured with external hardware

### Focus Behaviour
- Tab navigation follows DOM order
- Focus ring indicates active field
- Blur triggers validation check if field touched
- FAIMSTextField shows blue info icon for advanced help

### State Transitions
- **Pristine**: Initial state, no interaction
- **Focused**: Active input state
- **Touched**: Post-blur state enabling error display
- **Valid**: Green check (optional) on successful validation
- **Invalid**: Red border and error message when touched and invalid

## Conditional Logic Support

Fields support conditional display through controller field mechanisms:

```json
{
  "condition": {
    "operator": "is",
    "field": "recording-type",
    "value": "detailed"
  }
}
```

The TextField can serve as both controller and controlled field, enabling dynamic form branching based on text input values.

## Data Storage and Export

### Internal Storage
- Stores as UTF-8 encoded strings
- Preserves leading/trailing spaces (standard TextField)
- Trims whitespace (FAIMSTextField variant)
- Null values stored as empty strings

### Export Formats
- **CSV**: Text escaped with quotes when containing delimiters
- **JSON**: String values in UTF-8
- **Shapefile**: DBF limitation of 254 characters
- **GeoPackage**: Full text preservation

## Common Patterns

### Pattern: Identifier with Validation
```json
{
  "site-code": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Site Code",
      "name": "site-code",
      "helperText": "Format: ABC-9999",
      "required": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Site code required"],
      ["yup.matches", "^[A-Z]{3}-[0-9]{4}$", "Invalid format"]
    ]
  }
}
```

### Pattern: Optional Annotation Field
```json
{
  "brief-notes": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "label": "Brief Notes",
      "name": "brief-notes",
      "placeholder": "Optional contextual notes",
      "required": false,
      "advancedHelperText": "Record any brief observations"
    }
  }
}
```

## Troubleshooting Guide

### Common Issues

#### Field not appearing
**Cause**: Field omitted from section configuration or ID mismatch  
**Solution**: Verify field ID appears in appropriate view's field array

#### Cannot type in field
**Cause**: Field configured as disabled or readOnly  
**Solution**: Check `disabled: false` and absence of readOnly parameter

#### Wrong keyboard on mobile
**Cause**: Missing or incorrect InputProps configuration  
**Solution**: Set appropriate type: `"InputProps": {"type": "email"}` for email keyboard

#### Validation not triggering
**Cause**: Malformed validationSchema array structure  
**Solution**: Ensure proper nesting: `[["yup.string"], ["yup.required"]]`

#### Premature error display
**Cause**: Field touched state persisting from previous interaction  
**Solution**: This is expected behaviour; errors show after first blur

### Platform-Specific Issues

#### iOS: Unwanted auto-capitalisation
Configure explicitly: `"InputProps": {"autoCapitalize": "none"}`

#### Android: Keyboard covering field
Ensure viewport configuration includes appropriate scroll behaviour

#### Desktop: Paste not working
Verify field not disabled; check browser clipboard permissions

### Debug Checklist
- [ ] Field ID unique across entire notebook
- [ ] Component namespace and name correctly paired
- [ ] Label and name parameters present
- [ ] ValidatonSchema uses correct Yup syntax
- [ ] InitialValue is empty string, not null
- [ ] No conflicting conditional logic hiding field

## Implementation Notes

### Performance Considerations
- Standard TextField exhibits lower memory footprint
- FAIMSTextField provides enhanced UX at slight performance cost
- Validation runs on every keystroke after touched state
- Long text in single-line fields may impact render performance

### Migration Path
Existing notebooks using FAIMSTextField can migrate to standard TextField by:
1. Changing component-namespace to "formik-material-ui"
2. Changing component-name to "TextField"
3. Moving advancedHelperText content to helperText (losing formatting)
4. Testing validation behaviour remains consistent

### Selection Criteria
We recommend the standard TextField for most applications, reserving FAIMSTextField for contexts requiring rich help text or enhanced visual presentation. The production stability of formik-material-ui/TextField makes it the preferred choice for critical data collection workflows.

## Best Practices

- Limit expected input to 50 characters for optimal mobile display
- Provide clear helper text for expected formats
- Use placeholder text sparingly to avoid confusion
- Configure appropriate mobile keyboards via InputProps
- Consider MultilineTextField for content exceeding single-line constraints
- Validate format requirements at point of entry rather than submission
- Employ consistent naming conventions across related fields

## See Also

- **MultilineTextField**: For paragraph-length text entry
- **Email Field**: For validated email addresses
- **TemplatedStringField**: For auto-generated identifiers
- **Select**: When input should be constrained to predefined options
- **QRCodeFormField**: For barcode/QR code capture on mobile devices

---

*TextField represents the foundational text input mechanism within Fieldmark, with the formik-material-ui implementation serving as the production standard whilst faims-custom/FAIMSTextField offers enhanced functionality for specialised requirements.*