# ControlledNumber Field (Bounded Numeric Entry)

## Overview

The ControlledNumber field represents a pragmatic solution to a fundamental interface limitation within Fieldmark's three-component architecture, providing Designer users with accessible bounded numeric input capabilities that would otherwise require direct JSON manipulation. Whilst technically implemented as a standard FormikTextField configured with HTML5 numeric type constraints, this field's significance lies not in its technical novelty but in its democratisation of range-bounded data entry for researchers lacking programming expertise. The component emerges from the architectural necessity of supporting notebook creation through the web-based Designer interface, where configuring Yup validation schemas remains inaccessible to typical users who constitute the primary audience for heritage and archaeological fieldwork applications.

A critical type declaration error demands immediate acknowledgement: whilst the field specifies `"type-returned": "faims-core::Integer"`, it accepts and stores decimal values without restriction. This misalignment between declared and actual behaviour, though not affecting functionality, creates potential data integrity concerns when downstream analysis tools expect integer values but encounter floating-point data. The persistence of this error reflects broader challenges in maintaining type consistency across Fieldmark's distributed architecture, where the Designer, data collection app, and Control Centre operate with varying degrees of type enforcement.

The field's "controlled" nomenclature refers specifically to value bounding through minimum and maximum constraints – not to UI control mechanisms such as increment/decrement buttons. This semantic distinction proves essential, as researchers expecting spinner controls or stepped input interfaces will encounter instead a standard numeric text field with validation-based range enforcement. The implementation leverages HTML5's native number input capabilities, inheriting both their benefits (numeric keyboard activation on mobile devices) and limitations (inconsistent cross-browser behaviour, lack of locale-aware formatting).

## Common Use Cases

- **Environmental measurements with known bounds** – pH values (0–14), temperature ranges, percentage compositions (0–100)
- **Standardised assessment scales** – condition ratings (1–5), Likert scales, preservation indices
- **Depth measurements within excavation limits** – archaeological contexts with maximum depth constraints
- **Artefact dimensions** – length, width, thickness measurements with reasonable maxima
- **Temporal counts within defined periods** – pottery sherds per context, bone fragments per quadrant
- **Quality scores** – visibility ratings, confidence levels, completeness percentages
- **Elevation recordings** – height above sea level with site-specific bounds
- **Sample quantities** – soil sample weights, volume measurements with container limits

## Core Configuration

### Designer-Generated Configuration

When users add a ControlledNumber field through the Designer interface, the system automatically generates:

```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::Integer",
  "component-parameters": {
    "label": "User-specified label",
    "name": "auto-generated-field-id",
    "InputProps": {"type": "number"}
  },
  "validationSchema": [
    ["yup.number"],
    ["yup.min", 10],    // Designer requires min/max configuration
    ["yup.max", 20]     // Users must specify these bounds
  ],
  "initialValue": ""      // Always empty string by default
}
```

The Designer enforces range specification – users cannot create a ControlledNumber without defining minimum and maximum bounds, thereby ensuring the field's "controlled" nature.

### Optional Properties
```json
{
  "component-parameters": {
    "fullWidth": true,
    "variant": "outlined",
    "helperText": "Guidance text for users"
  },
  "validationSchema": [
    ["yup.required", "This field is required"],
    ["yup.nullable"],
    ["yup.integer", "Must be a whole number"]
  ],
  "persistent": true,
  "is-logic": {},
  "meta": {
    "annotation": {"include": true, "label": "Notes"},
    "uncertainty": {"include": true, "label": "±"}
  }
}
```

## Validation Rules

| Validation Type | Configuration | Behaviour | Error Timing | Platform Variance |
|----------------|---------------|-----------|--------------|-------------------|
| **Type checking** | HTML5 `type="number"` | Prevents alphabetic input | Real-time | iOS lacks minus key on keyboard |
| **Required field** | `["yup.required", "message"]` | Enforces non-empty value | On blur | Empty string vs null ambiguity |
| **Minimum bound** | `["yup.min", value, "message"]` | Validates ≥ minimum | On blur | Android shows minus despite min="0" |
| **Maximum bound** | `["yup.max", value, "message"]` | Validates ≤ maximum | On blur | Consistent across platforms |
| **Integer only** | `["yup.integer", "message"]` | Rejects decimal values | On blur | Not enforced by type declaration |
| **Nullable** | `["yup.nullable"]` | Permits empty field | On blur | Conflicts with required |
| **Custom regex** | Not supported | — | — | Use TextField for patterns |

### Critical Validation Considerations

The discrepancy between `"type-returned": "faims-core::Integer"` and actual decimal acceptance creates validation uncertainty. Projects requiring strict integer enforcement must explicitly include `["yup.integer"]` validation, as the type declaration alone provides no enforcement. This architectural inconsistency particularly affects archaeological contexts where "15.7 pottery sherds" represents a logical impossibility that the system nonetheless accepts.

## Display Behaviour

### Desktop Rendering
- **Input field**: Material-UI outlined TextField with numeric constraints
- **Spinner controls**: Browser-native increment/decrement arrows (10×20px)
- **Width behaviour**: Respects fullWidth parameter or defaults to auto-sizing
- **Error display**: Red outline with message below field after validation failure
- **Helper text**: Grey text below input, replaced by error when validation fails

### iOS Behaviour
- **Keyboard type**: Numeric pad without minus key (critical limitation)
- **Decimal input**: Period available on numeric keyboard
- **Spinner controls**: Absent (HTML5 limitation)
- **Negative entry**: Requires paste operation or switch to text keyboard
- **Voice input**: Requires exact numeric format ("twenty-three point five")

### Android Behaviour
- **Keyboard type**: Numeric pad with minus key (even when min="0")
- **Decimal input**: Period available on numeric keyboard
- **Spinner controls**: Hidden by Material-UI styling
- **Validation feedback**: Delayed until field blur
- **Browser variance**: Samsung Browser may show different keyboard layouts

## Interaction Patterns

### Data Entry Flow
1. **Field focus**: Activates numeric keyboard on mobile devices
2. **Value input**: Direct typing with real-time character filtering
3. **Range violation**: No prevention during typing, values outside bounds accepted temporarily
4. **Field blur**: Triggers validation, displays errors if bounds exceeded
5. **Error state**: Field remains in error with red outline until corrected
6. **Successful validation**: Error clears, field returns to normal state

### Semantic Confusion Resolution

The Designer's default configuration of `initialValue: ""` (empty string) creates an inherent semantic ambiguity that notebook designers must address through validation configuration and user guidance:

**For Designer Users:**
- The field always initialises as empty string – this cannot be changed through the GUI
- Empty fields represent "not measured" or "not applicable" by default
- To require explicit zero entry, add Required validation through the Designer
- Document in helper text whether users should enter 0 for "none found"

**For JSON Authors:**
- **Use `initialValue: 0`** when zero represents meaningful data (e.g., "no artefacts found")
- **Use `initialValue: ""`** when absence differs from zero (e.g., "not measured" vs "measured as zero")
- **Add `.nullable()`** validation to permit empty optional fields
- **Add `.required()`** to enforce value entry

This architectural decision – defaulting to empty string – reflects an assumption that absence of measurement differs semantically from a measurement of zero, though this distinction may not suit all research contexts.

## Conditional Logic Support

ControlledNumber fields fully participate in conditional logic evaluations:

```json
{
  "is-logic": {
    "type": "and",
    "conditions": [
      {
        "operator": "between",
        "field": "soil_ph",
        "value": [6.5, 7.5]
      }
    ]
  }
}
```

Comparison operators function as expected, though empty string initial values may produce unexpected results in numeric comparisons. Explicit null checks prove necessary when empty fields participate in conditional logic.

## Data Storage and Export

### Storage Characteristics

| Input State | Storage Value | CSV Export | JSON Export | Type Consistency |
|-------------|---------------|------------|-------------|------------------|
| Empty field | "" (empty string) | (empty cell) | "" | Invalid for Integer |
| Zero entry | 0 | 0 | 0 | Valid Integer |
| Integer value | 42 | 42 | 42 | Valid Integer |
| Decimal value | 3.14 | 3.14 | 3.14 | **Invalid for Integer** |
| Negative value | -15 | -15 | -15 | Valid Integer |
| Scientific notation | 1.23e-7 | 1.23e-7 | 1.23e-7 | **Invalid for Integer** |

### Type Declaration Mismatch

The persistence of decimal values despite `"faims-core::Integer"` declaration creates downstream analysis complications. Archaeological databases expecting integer counts receive floating-point values, potentially corrupting statistical analyses or triggering type errors in processing pipelines.

## Common Patterns

### Pattern 1: Environmental Measurement with Bounds
```json
{
  "soil_ph": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "label": "Soil pH",
      "name": "soil_ph",
      "fullWidth": true,
      "variant": "outlined",
      "InputProps": {"type": "number"},
      "helperText": "Measure using calibrated pH meter"
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", 0, "pH cannot be negative"],
      ["yup.max", 14, "pH cannot exceed 14"],
      ["yup.required", "pH measurement required"]
    ],
    "initialValue": "",
    "meta": {
      "uncertainty": {"include": true, "label": "± tolerance"}
    }
  }
}
```

### Pattern 2: Artefact Count with Zero Meaningful
```json
{
  "sherd_count": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "label": "Pottery Sherd Count",
      "name": "sherd_count",
      "fullWidth": false,
      "variant": "outlined",
      "InputProps": {"type": "number"},
      "helperText": "Total diagnostic sherds (enter 0 if none)"
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.integer", "Must be whole number"],
      ["yup.min", 0, "Cannot be negative"],
      ["yup.max", 9999, "Exceeds reasonable count"],
      ["yup.required", "Count required (enter 0 if none)"]
    ],
    "initialValue": 0,
    "persistent": true
  }
}
```

### Pattern 3: Depth Measurement with Site Limits
```json
{
  "depth_cm": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "label": "Depth Below Surface (cm)",
      "name": "depth_cm",
      "fullWidth": true,
      "variant": "outlined",
      "InputProps": {"type": "number"},
      "helperText": "Measure from datum point"
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", 0, "Depth cannot be negative"],
      ["yup.max", 500, "Exceeds site depth"],
      ["yup.nullable"]
    ],
    "initialValue": "",
    "meta": {
      "annotation": {"include": true, "label": "Measurement notes"},
      "uncertainty": {"include": true, "label": "± cm"}
    }
  }
}
```

## Troubleshooting Guide

### Common Issues and Resolutions

| Issue | Symptoms | Root Cause | Resolution |
|-------|----------|------------|------------|
| **Decimal values in integer fields** | "15.7" sherds accepted | Type declaration not enforced | Add `["yup.integer"]` validation |
| **Cannot enter negative values (iOS)** | No minus key on keyboard | iOS numeric pad limitation | Document workaround: paste or switch keyboard |
| **Empty field validation errors** | "Must be a number" on empty | Null/empty string confusion | Configure nullable() or required() explicitly |
| **Minus key visible despite min=0** | Android shows unnecessary key | HTML5 implementation variance | Document as known limitation |
| **Range validation delayed** | Out-of-range values during typing | Validation occurs on blur | Train users to expect delayed feedback |
| **Scientific notation stored** | 1e-7 in database | No format control | Add reasonable bounds to prevent |
| **Zero vs empty ambiguity** | Unclear if measured or not | No null support | Document semantic convention |

### Debug Checklist
- [ ] Verify `InputProps: {"type": "number"}` present
- [ ] Confirm min/max validation in correct order
- [ ] Check initialValue matches intended semantics (0 vs "")
- [ ] Test on iOS device for minus key accessibility
- [ ] Validate integer enforcement if whole numbers required
- [ ] Verify error messages are user-appropriate
- [ ] Test edge cases at exact min/max boundaries
- [ ] Confirm nullable() if empty acceptable
- [ ] Document units in label or helperText
- [ ] Test with decimal values if integers expected

## Implementation Notes

### Architectural Context

Within Fieldmark's three-component architecture, ControlledNumber addresses a specific interface limitation: Designer users cannot configure validation schemas directly. This necessitates a pre-configured field type that bundles numeric input with range validation, effectively democratising bounded data entry for non-technical users. The alternative – requiring JSON manipulation to add Yup validation to NumberInput fields – would exclude the primary user base of field researchers and heritage professionals.

### Type System Failures

The `"faims-core::Integer"` declaration represents a broader architectural challenge where type specifications exist across multiple system layers without enforcement mechanisms. This decorative typing creates false confidence, as downstream systems may reasonably expect integer data but receive floating-point values. Projects should implement explicit validation rather than trusting type declarations.

### Platform Limitations

HTML5 number inputs exhibit frustrating platform inconsistencies that ControlledNumber cannot resolve:
- iOS's missing minus key necessitates workflow adaptations
- Android's persistent minus key creates confusion when min=0
- Browser-specific spinner control implementations vary widely
- Voice input requires exact numeric pronunciation

These limitations reflect the tension between leveraging native platform capabilities and maintaining consistent user experiences across devices.

## Best Practices

- **Document semantic conventions explicitly** – specify whether empty means "not measured" or requires zero
- **Include integer validation for count data** – the type declaration alone provides no enforcement
- **Provide clear range guidance** – users should understand why bounds exist
- **Consider TextField for strict formats** – pattern validation offers more control than number inputs
- **Test on actual field devices** – emulators may not reveal keyboard limitations
- **Document units consistently** – "Depth (cm)" or append to helperText
- **Avoid scientific notation bounds** – use reasonable maxima to prevent exponential display
- **Plan for negative value entry on iOS** – document paste workaround in training materials
- **Validate decimal places explicitly** – no automatic precision control exists
- **Consider NumberInput for unbounded values** – ControlledNumber's value lies in its bounds

## See Also

- **NumberInput**: Unbounded numeric entry with better null handling (requires JSON configuration for validation)
- **TextField with pattern**: Alternative for strict numeric formats requiring specific decimal places
- **Select**: When numeric values map to predefined categories rather than continuous ranges
- **BasicAutoIncrementer**: For sequential identifiers rather than measurements
- **RadioGroup**: For small sets of discrete numeric options (e.g., ratings 1–5)