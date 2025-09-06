# NumberInput Field (Floating-Point Number Entry)

## Overview

The NumberInput field represents the contemporary standard for numeric data entry within the Fieldmark ecosystem, superseding the deprecated NumberField through its resolution of critical null-handling ambiguities and provision of proper floating-point type management. A fundamental nomenclature paradox demands immediate clarification: whilst the Designer interface presents this component as "Number Input", its JSON implementation requires `"component-name": "NumberField"` – an inversion that reflects historical architectural decisions and creates substantial potential for implementation confusion. This paradox, though counterintuitive, remains immutable within the current system architecture and necessitates explicit documentation throughout any technical communication. The component leverages JavaScript's IEEE 754 double-precision floating-point representation, inheriting both its capabilities (scientific notation, decimal precision to approximately 15–17 significant digits) and its constraints (silent precision truncation, overflow to Infinity beyond ±1.8×10³⁰⁸). Unlike its deprecated predecessor, NumberInput maintains rigorous semantic distinction between null values (representing "not measured" or "not applicable") and zero values (representing a measured value of zero) – a differentiation fundamental to scientific data integrity. The implementation employs a sophisticated dual-validation architecture, combining HTML5 constraints with Yup schema validation, whilst managing touched-state to provide intuitive error feedback without disrupting active data entry.

## Common Use Cases

- **Quantitative measurements**: Temperature readings (°C), pH values, mass (kg), volume (mL), or distance measurements requiring decimal precision and null/zero distinction
- **Environmental parameters**: Rainfall (mm), wind speed (km/h), humidity percentage, barometric pressure, or light intensity where absence of measurement differs from zero reading
- **Coordinate values**: Decimal latitude/longitude, elevation in metres, grid references, or bearing measurements requiring high precision
- **Count data**: Species abundance, artefact tallies, sample quantities, or feature occurrences where zero represents meaningful absence rather than missing data
- **Percentage values**: Coverage estimates, composition ratios, confidence levels stored as 0–100 rather than 0–1 to avoid decimal conversion errors
- **Calculated indices**: Diversity metrics, condition scores, statistical values where null indicates "not calculated" versus zero indicating a calculated result
- **Continuous monitoring data**: Sensor readings, instrument measurements, time-series observations requiring consistent numeric type handling
- **Field measurements with uncertainty**: Values requiring associated metadata for precision, confidence intervals, or measurement conditions

## Core Configuration

### Required Properties

```json
{
  "component-namespace": "faims-custom",
  "component-name": "NumberField",
  "type-returned": "faims-core::Number",
  "component-parameters": {
    "name": "unique-field-identifier",
    "label": "Measurement Label (units)",
    "InputProps": {
      "type": "number"
    }
  },
  "validationSchema": [
    ["yup.number"],
    ["yup.nullable"]
  ],
  "initialValue": null
}
```

**CRITICAL WARNING**: Despite appearing as "Number Input" in the Designer interface, the component-name MUST be "NumberField". This nomenclature inversion represents a permanent architectural constraint that cannot be modified without breaking existing notebooks.

### Optional Properties

```json
{
  "component-parameters": {
    "helperText": "Expected range: 0–100. Use period (.) for decimals",
    "advancedHelperText": "Precision limited to 15–17 significant digits",
    "required": false,
    "min": 0,
    "max": 100,
    "fullWidth": true,
    "disabled": false,
    "protection": "none"
  },
  "validationSchema": [
    ["yup.number"],
    ["yup.nullable"],
    ["yup.min", 0, "Value must be non-negative"],
    ["yup.max", 100, "Maximum value is 100"],
    ["yup.lessThan", 1.8e308, "Value exceeds maximum range"]
  ],
  "persistent": true,
  "meta": {
    "annotation": {"include": true, "label": "measurement_notes"},
    "uncertainty": {"include": true, "label": "precision_confidence"}
  }
}
```

### Property Specifications

#### Core Namespace and Type Configuration
- **component-namespace** (`string`): Invariably "faims-custom" for NumberInput implementation
- **component-name** (`string`): Invariably "NumberField" despite Designer displaying "Number Input"
- **type-returned** (`string`): Invariably "faims-core::Number" for floating-point persistence
- **InputProps.type** (`string`): Must include `{"type": "number"}` within InputProps object

#### Field Identification and Display
- **name** (`string`): Unique identifier for data binding and form state management
- **label** (`string`): User-visible label; should include units in parentheses (e.g., "Temperature (°C)")
- **helperText** (`string`): Guidance text; we recommend documenting decimal separator requirements and precision limits
- **advancedHelperText** (`string`): Extended technical guidance for complex measurements

#### Behavioural Configuration
- **required** (`boolean`): Enforces non-null value for form submission (default: false)
- **min** (`number`): HTML5 minimum constraint affecting spinner controls but not keyboard input
- **max** (`number`): HTML5 maximum constraint; we strongly recommend including Yup validation to prevent Infinity overflow
- **fullWidth** (`boolean`): Spans container width for improved touch targets (default: true)
- **disabled** (`boolean`): Prevents all interaction whilst maintaining visibility (default: false)
- **persistent** (`boolean`): Enables sticky behaviour across sequential records (default: false)

#### Initial State Configuration
- **initialValue** (`null | number`): Starting value for new records
  - `null`: Semantically correct for optional measurements (strongly recommended)
  - Numeric value: Pre-populates field with specific value
  - Never use empty string (`""`) – this undermines null/zero distinction

## Validation Rules

### Dual-Layer Validation Architecture (Offline/Client-Side)

NumberInput implements a sophisticated validation strategy combining HTML5 constraints with Yup schema validation, executing entirely offline before synchronisation. This client-side validation architecture provides both immediate browser-level feedback and customisable error messaging without requiring server communication:

| Validation Layer | Timing | Error Display | Customisable | Platform Consistency |
|-----------------|---------|---------------|--------------|---------------------|
| HTML5 Attributes | During input | Browser default | No | Variable |
| Yup Schema | On change/blur | After touched | Yes | Consistent |

### Validation Execution Sequence

1. **Initial Mount**: Validation executes but errors remain hidden (untouched state)
2. **During Typing**: Validation runs on every keystroke; errors computed but not displayed
3. **On Blur Event**: Field marked as "touched" via `form.setFieldTouched(field.name, true)`
4. **Post-Touch**: Errors display and update in real-time with subsequent keystrokes
5. **Form Submission**: All fields marked touched; comprehensive error display

### Error Message Hierarchy

The system prioritises error messages in the following sequence:

1. **Invalid Number Check** (hardcoded): "Error with numeric input, please enter a valid number."
2. **Yup Validation Messages** (customisable): Display in schema definition order
3. **Helper Text** (when no errors): Shows guidance text

### Touched-State Management

The touched-state mechanism elegantly resolves the null/zero semantic distinction:

```javascript
const error = form.touched[field.name] && Boolean(form.errors[field.name]);
```

This prevents spurious "required field" errors for legitimately empty optional fields whilst ensuring clear feedback once users interact with the field. For field researchers, this behaviour proves particularly valuable when rapidly entering sequential measurements, as validation feedback doesn't disrupt ongoing data entry.

## Display Behaviour

### Platform-Specific Rendering Matrix

| Platform | Keyboard Type | Spinner Controls | Minus Key | Decimal | Voice Input |
|----------|--------------|------------------|-----------|---------|-------------|
| **Desktop Chrome/Firefox** | Standard physical | ✓ Styled arrows | ✓ Always | ✓ Period | Text-to-speech |
| **Desktop Safari** | Standard physical | ✓ Custom CSS | ✓ Always | ✓ Period | Dictation |
| **iOS Safari/Chrome** | Numeric pad | ✗ Hidden | ✗ Absent | ✓ Period | Requires numeric format |
| **Android Chrome** | Numeric pad | ✗ Hidden | ✓ Present* | ✓ Period | Requires numeric format |
| **Android Samsung Browser** | Varies by version | ✗ Hidden | ✓ Usually | ✓ Period | Device-dependent |

*Critical inconsistency: Android displays minus key despite `min="0"` constraint

### Spinner Control Styling

Desktop browsers receive custom-styled increment/decrement controls via:

```css
& input::-webkit-inner-spin-button,
& input::-webkit-outer-spin-button {
  opacity: 1;
  appearance: auto;
  width: 10px;
  height: 20px;
  backgroundColor: #9F9F9F;
  border-radius: 4px;
  cursor: pointer;
  border: 2px solid #000;
  padding: 8px;
}
```

These 10×20px controls prove challenging for gloved operation or low-visibility conditions – consider implementing custom increment/decrement buttons for field deployment.

### Numeric Display Transformation

| Input Value | Displayed Format | Storage Format | Threshold Rule |
|------------|------------------|----------------|----------------|
| 1234567 | 1234567 | 1234567 | < 1e7: standard notation |
| 12345678 | 1.2345678e+7 | 12345678 | ≥ 1e7: scientific notation |
| 0.000001 | 0.000001 | 0.000001 | > 1e-6: standard notation |
| 0.0000001 | 1e-7 | 1e-7 | ≤ 1e-6: scientific notation |
| 3.14159265358979323846 | 3.141592653589793 | 3.141592653589793 | ~15–17 digit truncation |

## Interaction Patterns

### Input Methods and Constraints

- **Direct keyboard entry**: Accepts numeric keys, period (.), minus (-), and 'e' for scientific notation
- **Copy-paste operations**: Accepts any text; validation occurs on blur
- **Voice dictation**: Must produce exact numeric format (e.g., "-15.5" not "negative fifteen point five")
- **Spinner controls**: Desktop-only; respect min/max bounds but small touch targets
- **Tab navigation**: Standard form traversal; Enter typically submits form

### Platform-Specific Limitations

**NumberInput accepts negative numbers by default**, with platform-specific variations in input methods. iOS users face particular challenges as the standard numeric keyboard lacks a minus key, requiring paste operations for negative values. Conversely, Android keyboards display the minus key even when `min="0"` is configured, creating an inconsistency where users can type values that subsequently fail validation. This HTML5 constraint enforcement varies across browsers – some prevent negative input when `min="0"` is set, whilst others permit entry but display validation errors.

**Voice input requires exact numeric format**. Natural language phrases ("one thousand") produce NaN errors. Field researchers should be trained to dictate numbers in standard format or use manual entry for complex values.

### Touch Target Considerations

Standard Material-UI touch targets (48×48dp minimum) may prove insufficient for:
- Gloved operation in archaeological contexts
- Wet conditions in marine research
- Low-visibility environments
- Users with motor impairments

Consider implementing larger custom touch targets or alternative input methods for challenging field conditions.

## Conditional Logic Support

NumberInput fully supports Fieldmark's conditional logic system through standard field value references:

```json
{
  "is-logic": {
    "type": "and",
    "conditions": [
      {
        "operator": ">",
        "field": "ph_measurement",
        "value": 7
      }
    ]
  }
}
```

Conditional visibility, requirement, and validation all function as expected. Note that null values in conditional comparisons require explicit handling – null is neither greater than nor less than any number.

## Data Storage and Export

### Storage Characteristics

| Value Type | Input | Database Storage | CSV Export | JSON Export |
|------------|-------|------------------|------------|-------------|
| Null (empty) | — | null | (empty cell) | null |
| Zero | 0 or 0.0 | 0 | 0 | 0 |
| Integer | 42.0 | 42 | 42 | 42 |
| Decimal | 3.14159 | 3.14159 | 3.14159 | 3.14159 |
| Scientific | 1.23e-7 | 1.23e-7 | 1.23e-7 | 1.23e-7 |
| Precision limit | π to 50 places | 3.141592653589793 | 3.141592653589793 | 3.141592653589793 |
| Overflow | 1e309 | null | (empty cell) | null |

### Critical Storage Considerations

**Trailing zeros are not preserved**: The value 42.0 stores as 42, potentially affecting downstream analysis expecting specific decimal places. Researchers requiring format preservation should consider string fields with pattern validation.

**Infinity and NaN become null**: Values exceeding ±1.8×10³⁰⁸ or resulting from invalid operations store as null, appearing as empty cells in CSV exports. Include reasonable max validation (e.g., `["yup.lessThan", 1e100]`) to prevent data loss.

**No locale formatting in exports**: Exports always use period for decimal separator and lack thousands separators, ensuring compatibility with scientific software but potentially requiring post-processing for regional reports.

### Round-Trip Fidelity

NumberInput maintains excellent round-trip fidelity within JavaScript's numeric limits:
- Scientific notation preserved if originally entered
- Precision maintained to ~15–17 significant digits
- Null/zero distinction preserved
- Format may change (1.23e7 ↔ 12300000) but value remains identical

## Common Patterns

### Heritage Site Environmental Monitoring

```json
{
  "component-namespace": "faims-custom",
  "component-name": "NumberField",
  "type-returned": "faims-core::Number",
  "component-parameters": {
    "name": "relative_humidity",
    "label": "Relative Humidity (%)",
    "helperText": "Percentage 0–100. Use period for decimals",
    "required": true,
    "min": 0,
    "max": 100,
    "fullWidth": true,
    "InputProps": {"type": "number"}
  },
  "validationSchema": [
    ["yup.number"],
    ["yup.required", "Humidity measurement required"],
    ["yup.min", 0, "Humidity cannot be negative"],
    ["yup.max", 100, "Humidity cannot exceed 100%"]
  ],
  "initialValue": null,
  "persistent": true,
  "meta": {
    "annotation": {"include": true, "label": "measurement_conditions"},
    "uncertainty": {"include": true, "label": "instrument_precision"}
  }
}
```

### GPS Coordinate Entry with Precision Validation

```json
{
  "component-namespace": "faims-custom",
  "component-name": "NumberField",
  "type-returned": "faims-core::Number",
  "component-parameters": {
    "name": "latitude_decimal",
    "label": "Latitude (decimal degrees)",
    "helperText": "Southern hemisphere negative. Precision: 6 decimal places",
    "required": true,
    "min": -90,
    "max": 90,
    "fullWidth": true,
    "InputProps": {"type": "number"}
  },
  "validationSchema": [
    ["yup.number"],
    ["yup.required", "Latitude required"],
    ["yup.min", -90, "Invalid latitude (< -90)"],
    ["yup.max", 90, "Invalid latitude (> 90)"],
    ["yup.test", "decimal-places", 
     "Maximum 6 decimal places",
     "value => value === null || value === undefined || (value.toString().split('.')[1] || '').length <= 6"]
  ],
  "initialValue": null
}
```

### Migration from Deprecated NumberField

```json
{
  "component-namespace": "faims-custom",
  "component-name": "NumberField",  // Was "TextField" in deprecated version
  "type-returned": "faims-core::Number",  // Was "faims-core::Integer"
  "component-parameters": {
    "name": "specimen_count",
    "label": "Specimen Count",
    "helperText": "Whole numbers only",
    "required": false,
    "min": 0,
    "fullWidth": true,
    "InputProps": {"type": "number"}  // Must be explicitly included
  },
  "validationSchema": [
    ["yup.number"],
    ["yup.nullable"],  // Critical for proper null handling
    ["yup.integer", "Whole numbers only"],
    ["yup.min", 0, "Count cannot be negative"]
  ],
  "initialValue": null  // Was "" (empty string) in deprecated version
}
```

## Troubleshooting Guide

### Component Naming Confusion

**Symptom**: "Cannot find component NumberInput" error  
**Cause**: Designer shows "Number Input" but requires "NumberField" in JSON  
**Solution**: Always use `"component-name": "NumberField"` regardless of Designer label  
**Prevention**: Document this paradox prominently in project documentation

### Silent Precision Loss

**Symptom**: Entering 3.141592653589793238462643 displays as 3.141592653589793  
**Cause**: JavaScript IEEE 754 limitation (~15–17 significant digits)  
**Solution**: Document precision limits in helperText; consider string fields for high-precision requirements  
**Verification**: Test with known high-precision values during development

### Negative Number Input Inconsistencies

**Symptom**: Platform-specific variations in entering negative values  
**Context**: NumberInput accepts negative numbers by default; restrictions via `min` parameter enforce inconsistently  
**Platform Behaviours**:
- iOS: Standard numeric keyboard lacks minus key – users must paste negative values
- Android: Minus key remains visible even with `min="0"` configuration
- Desktop: Full keyboard access regardless of constraints
**Solution**: Document platform differences in training materials; implement Yup validation for consistent error messaging  
**Critical Note**: Validation occurs offline/client-side only – invalid data that bypasses client validation will synchronise

### European Decimal Notation Fails

**Symptom**: Entering "15,5" produces "Error with numeric input"  
**Cause**: JavaScript Number() only accepts period as decimal separator  
**Solution**: Document period requirement prominently; consider pre-processing for European data  
**Workaround**: Provide clear error messages specifying period usage

### Infinity in Data Export

**Symptom**: CSV contains empty cells for very large numbers  
**Cause**: Values exceeding ±1.8×10³⁰⁸ overflow to Infinity, which exports as null  
**Solution**: Add Yup validation `["yup.lessThan", 1e100, "Value too large"]`  
**Prevention**: Document expected ranges for each measurement type

### Voice Input Not Recognised

**Symptom**: Dictating "negative fifteen point five" produces NaN  
**Cause**: Voice-to-text produces natural language, not numeric format  
**Solution**: Train users to dictate numbers as "minus one five point five" or use manual entry  
**Alternative**: Implement custom voice processing if critical for workflow

### Debug Checklist

- [ ] Using "NumberField" as component-name (not "NumberInput")
- [ ] InputProps includes `{"type": "number"}`
- [ ] InitialValue is null (not empty string)
- [ ] ValidationSchema includes `["yup.nullable"]` for optional fields
- [ ] Both HTML5 min/max and Yup validation configured
- [ ] HelperText documents period-only decimal separator
- [ ] Reasonable max value prevents Infinity overflow
- [ ] Server-side validation implemented for critical constraints

## Implementation Notes

### Architectural Rationale

The NumberInput implementation reflects deliberate architectural decisions prioritising semantic clarity over backwards compatibility. The transition from the deprecated NumberField (using `formik-material-ui:TextField`) emerged from critical null-handling deficiencies that compromised scientific data integrity. Whilst the nomenclature paradox creates initial confusion, the benefits of proper null/zero distinction and floating-point type management justify this architectural evolution.

### Validation Philosophy

The dual-validation pattern – combining HTML5 attributes with Yup schemas – represents a pragmatic compromise between browser-native functionality and customisable business logic. HTML5 constraints provide immediate client-side boundaries (particularly valuable for spinner controls), whilst Yup validation enables context-specific error messaging essential for field research scenarios.

### Platform Inconsistency Acceptance

Rather than attempting to normalise platform behaviours through complex polyfills, NumberInput accepts and documents platform variations. This philosophy acknowledges that perfect cross-platform consistency remains unattainable whilst ensuring researchers understand and can work within platform-specific constraints.

### Precision Limitations as Feature Boundaries

The component deliberately eschews arbitrary-precision arithmetic or sophisticated number formatting, maintaining alignment with JavaScript's native numeric handling. This constraint, whilst limiting for certain specialised applications, ensures predictable behaviour and straightforward integration with standard data analysis tools.

## Best Practices

- **Document precision requirements explicitly** in helperText, particularly for scientific measurements where significant figures matter
- **Include units in field labels** using consistent notation: "Temperature (°C)" rather than separate unit fields
- **Validate reasonable ranges** to prevent Infinity overflow: include `["yup.lessThan", 1e100]` for unbounded fields
- **Implement redundant validation** combining client-side (HTML5 + Yup) with server-side verification for critical constraints
- **Use null for optional measurements** to maintain semantic distinction from zero values in scientific datasets
- **Test with actual field devices** including gloved operation, wet conditions, and various Android/iOS versions
- **Document the nomenclature paradox** prominently in project onboarding materials to prevent implementation confusion
- **Consider string fields with pattern validation** for values requiring exact format preservation or >17 significant digits
- **Train users on platform quirks** particularly Android minus key persistence and voice input requirements
- **Export data regularly during collection** to verify format compatibility with analysis pipelines
- **Enable metadata fields** (annotation, uncertainty) for measurements requiring qualification or confidence intervals
- **Plan for offline scenarios** where validation might behave differently from online states

## See Also

- **Deprecated NumberField**: Legacy implementation using TextField – do not use for new notebooks
- **ControlledNumber**: Alternative for strictly bounded ranges with enforced constraints
- **BasicAutoIncrementer**: Sequential ID generation (returns strings, not numbers)
- **TextField with pattern**: For formatted numbers requiring specific patterns or >17 digit precision
- **Select/RadioGroup**: When numeric values map to categorical meanings
- **TemplatedString**: To incorporate numeric values into complex identifiers