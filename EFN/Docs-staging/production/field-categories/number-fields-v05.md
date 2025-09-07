<!-- concat:boundary:start section="number-fields" -->
<!-- concat:metadata
document_id: number-fields-v05
category: numeric
field_count: 3
designer_capable: ["NumberField"]
json_only: ["BasicAutoIncrementer", "step_increments"]
last_updated: 2025-01-05
-->

<!-- discovery:metadata
provides: [numeric-input, controlled-number, auto-increment, validation-ranges]
see-also: [field-selection-guide, constraints-reference]
-->


# Number Input Fields


<!-- structured:metadata
meta:purpose: field-configuration
meta:summary: Two number input components (BasicAutoIncrementer and TextField variants) with validation patterns and increment strategies.
meta:generates: json-fields
meta:requires: [valid-json, unique-names, fviews-layer]
meta:version: 3.0.0
meta:document: number_fields
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Date & Time Fields](./datetime-fields-v05.md) | **Numeric Fields** | [Display Fields →](./display-field-v05.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Display Fields ↓](#display-fields) -->

# Number Input Fields

## Overview {essential}

The Number Input category encompasses three distinct field types for numeric and sequential data management in Fieldmark, each serving fundamentally different purposes despite their shared categorization.

## Component Mapping Reference {essential}

For the complete mapping between Designer field names and JSON component implementations, see:
→ **[Designer UI to Component Mapping Reference](../references/designer-component-mapping.md)**

This central reference provides:
- Exact component names and namespaces for all fields
- Configuration requirements and examples
- Common mapping errors and solutions


## Designer Usage Guide {essential}

### What to Select in Designer

When using the Designer interface, follow these simple rules:

🔢 **For numeric measurements and calculations**: Select **"Number Input"**
- Use for: measurements, counts, ratings, scientific data
- Creates: NumberField component (note the name mismatch)
- ⚠️ iOS users cannot enter negative numbers directly (must copy-paste)

📊 **For bounded numeric values**: Select **"Controlled Number"**
- Use for: ratings (1-5), scores (0-100), bounded measurements
- Creates: ControlledNumber component with min/max enforcement
- Provides slider interface in addition to text input

🔤 **For sequential identifiers**: Select **"Basic Auto-incrementer"**
- Use for: sample IDs, context numbers, sequential codes
- Creates: BasicAutoIncrementer (returns STRING not number)
- ⚠️ Must be wrapped in TemplatedString to prevent Excel corruption

❌ **NEVER select "Number Field"** (deprecated)
- This legacy option still appears in Designer but should not be used
- Always choose "Number Input" instead for numeric data

### Quick Reference Table

| Designer Label | JSON component-name | Returns | Designer Config | Key Purpose |
|----------------|-------------------|---------|-----------------|-------------|
| 🔢 **Number Input** | `NumberField`* | Number | Partial | Measurements, calculations |
| 📊 **Controlled Number** | `TextField`** | Number*** | Full | Bounded values, ratings |
| 🔤 **Basic Auto-incrementer** | `BasicAutoIncrementer` | String**** | Full | Sequential IDs |

*⚠️ **Component name paradox**: Designer shows "Number Input" but JSON requires "NumberField"  
**⚠️ **Not a real component**: "Controlled Number" uses TextField with type="number"
***⚠️ **Type mismatch**: Declares Integer but accepts/stores decimals  
****⚠️ **Critical**: Returns strings not numbers despite "Number Fields" category  
****Note: Do not confuse with deprecated "Number Field" - always use "Number Input"**

### When JSON Enhancement is Required

**NumberInput**:
- ✅ Required: Range validation, decimal precision, integer-only
- ✅ Required: Custom error messages
- ❌ Never: Step increments not supported (use BasicAutoIncrementer instead)

**ControlledNumber**:
- ⚠️ Optional: Additional validation beyond min/max
- ⚠️ Optional: True integer enforcement
- ⚠️ Optional: Custom error messages

**BasicAutoIncrementer**:
- ✅ Required: Custom validation patterns
- ❌ Never: Core functionality fully Designer-accessible
- ❌ Never: Integration with TemplatedString works in Designer

### Designer Limitations {important}

[Link to Designer Limitations Reference](../reference-docs/designer-limitations-reference.md)

**Number Field-Specific Designer Limitations**:
- **NumberInput**: Cannot set range validation (min/max) through Designer
- **NumberInput**: Cannot configure decimal precision or integer-only mode
- **All fields**: Cannot add custom validation messages
- **All fields**: Cannot configure input masks or formatting patterns

### ⚠️ CRITICAL: Deprecated Field Warning {essential}

**DO NOT USE "Number Field" (deprecated)** - A legacy numeric field type still appears in the Designer interface labeled as "Number Field". This deprecated field:
- Uses `formik-material-ui:TextField` with `type="number"` in JSON
- Returns `faims-core::Integer` despite accepting decimals
- Has poor null handling (uses empty string instead of null)
- **Should be replaced with "Number Input" in all new notebooks**

**The confusion**: 
- ❌ **Number Field** (deprecated) - Do not use
- ✅ **Number Input** (recommended) - Use this instead
- ⚠️ Note: Number Input confusingly uses `"NumberField"` as its JSON component-name

If you see "Number Field" in Designer, always choose "Number Input" instead. Existing notebooks using the deprecated Number Field should be migrated to Number Input for better data integrity.

## Field Selection Guide {essential}

### Decision Tree

```
Need numeric/sequential functionality?
├─ Need actual numeric values for calculations?
│  ├─ YES → Need range validation?
│  │  ├─ Can edit JSON?
│  │  │  └─ YES → NumberInput
│  │  │     ├─ Returns: faims-core::Number
│  │  │     └─ Full validation control
│  │  └─ Designer only?
│  │     └─ YES → ControlledNumber
│  │        ├─ Returns: faims-core::Number
│  │        └─ Min/max in Designer
│  │
│  └─ NO → Need sequential identifiers?
│     └─ YES → BasicAutoIncrementer
│        ├─ Returns: faims-core::String (with zeros)
│        ├─ Format: "00001", "00002", etc.
│        └─ ⚠️ Excel strips leading zeros
│
└─ Need specific numeric format?
   ├─ Scientific notation? → NumberInput
   │  └─ Supports 1.23e-7 format
   ├─ Leading zeros? → BasicAutoIncrementer
   │  └─ Or TemplatedString wrapper
   └─ Negative on iOS? → TextField with pattern
      └─ ⚠️ iOS keyboard lacks minus key
```

### Decision Matrix

| Requirement | NumberInput | ControlledNumber | BasicAutoIncrementer |
|-------------|------------|------------------|---------------------|
| **Calculations** | ✅ Best | ✅ Yes | ❌ No (strings) |
| **Null values** | ✅ Yes | ❌ No | ❌ No |
| **Designer bounds** | ❌ JSON only | ✅ Native | N/A |
| **Sequential IDs** | ❌ No | ❌ No | ✅ Purpose-built |
| **Excel safety** | ✅ Standard | ✅ Standard | ⚠️ Needs wrapper |
| **iOS negatives** | ❌ Copy-paste | ❌ Copy-paste | ✅ N/A |

### Selection Strategy

1. **Default to NumberInput** for maximum flexibility and null support
2. **Use ControlledNumber** when Designer-only and bounds needed
3. **Deploy BasicAutoIncrementer** for sequential IDs (wrap with TemplatedString for Excel)
4. **Consider TextField with pattern** for iOS negative number entry
5. **Avoid scientific notation** unless specifically required

**Platform Considerations**:
- iOS: No minus key on number keyboard, use copy-paste
- Android: Full numeric keyboard available
- Desktop: Browser spinners ~20×20px (too small)
- Excel: Strips leading zeros, corrupts large numbers

**Accessibility Requirements**:
- Spinner controls far below 44px WCAG minimum
- Generic "must be number" errors unhelpful
- No aria-live regions for validation
- Consider larger touch targets via CSS

## ⚠️ Critical Security Risks {essential}

**Silent Precision Loss**:
- **Risk**: Values beyond 15-17 significant digits silently truncated
- **Impact**: Scientific data corruption, financial calculation errors
- **Example**: 9007199254740993 becomes 9007199254740992
- **Mitigation**: Document precision limits, use string fields for IDs

**iOS Negative Number Entry**:
- **Risk**: Cannot enter negative values on iOS numeric keyboard
- **Impact**: Data collection failure, workaround confusion
- **Mitigation**: Provide TextField alternative or document copy-paste method
- **Training**: Essential for field teams using iOS devices

**Excel ID Corruption**:
- **Risk**: Excel converts numeric IDs (strips leading zeros, scientific notation)
- **Impact**: Specimen ID "0001234" becomes "1234", data linkage broken
- **Mitigation**: Always use BasicAutoIncrementer for IDs, not NumberInput
- **Export**: Wrap in TemplatedString for Excel protection

---

## What These Fields Cannot Do {important}

### Numeric Processing Limitations {important}
- **Complex calculations** - No formulas or expressions (e.g., field1 + field2)
- **Unit conversion** - Cannot convert between units automatically
- **Currency formatting** - No thousand separators or currency symbols
- **Percentage display** - Cannot show as percentage (stores decimal)
- **Fraction input** - Cannot enter or display fractions (e.g., 1/3)

### Validation Limitations {important}
- **Cross-field validation** - Cannot validate sum across multiple fields
- **Dynamic ranges** - Cannot set min/max based on other fields
- **Custom increments** - Cannot enforce specific step values (use BasicAutoIncrementer for sequential steps)
- **Precision validation** - Cannot enforce exact decimal places
- **Business rules** - No complex validation logic (e.g., "if X then Y must be > Z")

### Display Limitations {important}
- **Formatted display** - No comma separators (1,000,000)
- **Scientific notation control** - Cannot prevent auto-conversion at 1e7
- **Leading zeros** - NumberInput strips them (use BasicAutoIncrementer)
- **Custom number formats** - No phone numbers, credit cards, etc.
- **Negative number entry** - iOS keyboard lacks minus key

### Integration Limitations {important}
- **External sensor input** - No direct Bluetooth/USB sensor integration
- **Barcode scanning** - Cannot scan numeric barcodes (use QRCodeFormField)
- **Voice calculation** - Cannot process "add five to previous value"
- **Complex calculations** - No in-field formulas or computed values
- **Unit conversions** - No automatic conversion between units

## Common Use Cases {important}

### Measurements and Observations
- **Dimensions** → NumberInput with min: 0, precision helper text
- **Counts** → NumberInput with integer validation
- **Percentages** → NumberInput with min: 0, max: 100
- **Ratings** → ControlledNumber with defined scale (1-5, 1-10)

### Scientific Data
- **Coordinates** → NumberInput with high precision (6+ decimals)
- **Temperature** → NumberInput (allows negatives)
- **pH values** → NumberInput with min: 0, max: 14
- **Concentrations** → NumberInput with scientific notation support

### Identifiers and Codes
- **Sequential IDs** → BasicAutoIncrementer (zero-padded strings)
- **Sample numbers** → BasicAutoIncrementer + TemplatedString wrapper
- **Plot numbers** → NumberInput if calculations needed
- **Reference codes** → BasicAutoIncrementer for Excel safety

### Data Quality Patterns
- **Optional measurements** → NumberInput with `nullable()` validation
- **Bounded values** → ControlledNumber for strict ranges
- **Excel-safe IDs** → BasicAutoIncrementer (prevents number conversion)
- **Precision documentation** → Helper text stating decimal places

## Designer Component Mapping {essential}

### Designer UI vs JSON Component Names

| Designer UI Label | JSON component-name | Component Namespace | Description |
|-------------------|---------------------|---------------------|-------------|
| Number Input | NumberField | faims-custom | Standard numeric input with validation |
| Controlled Number | TextField | formik-material-ui | TextField with type="number" and validation |
| Basic Auto-incrementer | BasicAutoIncrementer | faims-custom | Sequential ID generator (returns string) |
| ~~Number Field~~ | ~~TextField~~ | ~~formik-material-ui~~ | **DEPRECATED - Do not use** |

⚠️ **Critical Notes**:
- "Number Input" in Designer creates "NumberField" in JSON - this name mismatch is a common error source
- "Number Field" (deprecated) still appears in Designer - always use "Number Input" instead
- BasicAutoIncrementer returns `faims-core::String`, not numbers despite being in "Number Fields"
- All number fields use namespace "faims-custom" except the deprecated Number Field
- Designer cannot configure iOS negative number workarounds - requires JSON

### Designer Configuration Options

| Designer Option | JSON Parameter | Values | Description |
|-----------------|---------------|---------|-------------|
| Label | `label` | string | Field display name |
| Required | `validationSchema` | `[["yup.required"]]` | Makes field mandatory |
| Helper Text | `helperText` | string | Guidance text below field |
| Min Value | `component-parameters.min` | number | Minimum allowed value |
| Max Value | `component-parameters.max` | number | Maximum allowed value |
| Initial Value | `initialValue` | number/0 | Default value when field loads |
| Form ID | `component-parameters.form_id` | string | For BasicAutoIncrementer prefix |
| Digit Count | `component-parameters.numDigits` | number | ID padding (001 vs 00001) |

## Designer Capabilities vs JSON Enhancement {comprehensive}

### What Designer Can Configure {essential}

For complete meta properties documentation (annotation, uncertainty, persistence), see [Meta Properties Reference](meta-properties-reference.md).

| Field | Designer Configurable | JSON-Only Features |
|-------|----------------------|-------------------|
| **NumberInput** | • Label<br>• Required<br>• Helper text<br>• Initial value<br>• Persistent | • Min/max bounds<br>• Decimal precision<br>• Integer enforcement<br>• Custom validation<br>• Step increments |
| **ControlledNumber** | • Label<br>• Required<br>• Helper text<br>• Min/max bounds<br>• Initial value (0) | • Integer enforcement<br>• Custom validation<br>• Step increments<br>• Alternative initial |
| **BasicAutoIncrementer** | • Label<br>• Form ID<br>• Digit count<br>• Helper text | • Validation patterns<br>• Custom formatting<br>• Integration setup |


## Component Namespace Errors {important}

See [Component Namespace Reference](component-namespace-reference.md) for complete namespace documentation, error troubleshooting, and Designer name mapping.

### Number Field-Specific Notes

**All number fields use the same namespace**:
- Namespace: `faims-custom` for ALL number components
- Exception: Deprecated "Number Field" uses `formik-material-ui:TextField` with type="number"

**Quick Reference for Number Fields**:
| Component | Namespace | Designer Name | Notes |
|-----------|-----------|---------------|-------|
| NumberField | `faims-custom` | Number Input | Primary numeric field |
| BasicAutoIncrementer | `faims-custom` | Auto-incrementer | Returns string, not number |
| TextField | `formik-material-ui` | Controlled Number | With type="number" and validation |

**Common confusion**: 
- Designer shows "Number Input" but JSON requires "NumberField"
- BasicAutoIncrementer returns strings like "BAI-001", not numbers


## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| General numeric input | NumberField | Full validation support |
| Sequential IDs | BasicAutoIncrementer | Auto-increment |
| Controlled input | TextField with type="number" | When NumberField insufficient |

### Decision Criteria
- **Auto-generation**: Needed → BasicAutoIncrementer
- **Validation complexity**: Simple → NumberField, Complex → TextField variant
- **Step increments**: Not in Designer → Use BasicAutoIncrementer
- **Display format**: Standard → NumberField, Custom → BasicAutoIncrementer

## Common Characteristics {important}

### Configuration Rules {important}

#### Base Properties [affects: All fields] {important}

| Property | Type | Required | NumberInput | ControlledNumber | BasicAutoIncrementer |
|----------|------|----------|------------|------------------|---------------------|
| `name` | string | Yes | Field ID | Field ID | Field ID |
| `type` | string | Yes | `"faims-core::Float"` | `"faims-core::Integer"`* | `"faims-core::String"` |
| `component-name` | string | Yes | `"NumberField"` | `"TextField"` | `"BasicAutoIncrementer"` |
| `component-namespace` | string | Yes | `"faims-custom"` | `"formik-material-ui"` | `"faims-custom"` |
| `label` | string | Yes | User label | User label | User label (hidden) |
| `initialValue` | varies | No | `null` | `0` | `""` (auto) |
| `persistent` | boolean | No | `true` | `true` | `true` |
| `required` | boolean | No | `false` | `false` | `false` |

*Accepts decimals despite Integer declaration  
**Component name paradox

### Data Type Specifications {important}

#### IEEE 754 Floating-Point Representation [affects: NumberInput, ControlledNumber] {important}

NumberInput and ControlledNumber use JavaScript's double-precision floating-point, providing approximately 15-17 significant decimal digits of precision. Values exceeding ±1.8 × 10³⁰⁸ overflow to Infinity and cannot be stored. This implementation inherits both the capabilities (scientific notation support, broad range) and limitations (precision loss, rounding errors) of the IEEE 754 standard.

| Characteristic | Specification | Practical Impact |
|---------------|--------------|------------------|
| **Precision** | 15-17 significant decimal digits | Silent truncation beyond this |
| **Max Safe Integer** | ±9,007,199,254,740,991 | Integers above lose precision |
| **Range** | ±5.0 × 10⁻³²⁴ to ±1.8 × 10³⁰⁸ | Overflow to ±Infinity |
| **Special Values** | Infinity, -Infinity, NaN | Validation must handle these |
| **Smallest Increment** | ~2.22 × 10⁻¹⁶ at 1.0 | Rounding errors accumulate |

**Storage Implications**:
- 64-bit (8 bytes) per number in memory
- Null requires explicit storage (not zero)
- Scientific notation stored as string representation

### Validation Patterns {important}
See [Validation System Documentation](../detail-crossfield-docs/validation.md) for comprehensive validation patterns and timing.

**Number Field-Specific Validation:**

```json
// Example number-fields-01

"validationSchema": [
  ["yup.number"],
  ["yup.test", "decimal-places", "Maximum 2 decimal places",
    "value => value == null || Number.isInteger(value * 100)"]
]


"validationSchema": [
  ["yup.number"],
  ["yup.min", 0, "Value must be non-negative"],
  ["yup.max", 100, "Value cannot exceed 100"]
]
```

**BasicAutoIncrementer-Specific**:
- Validates as STRING not number (e.g., "00150" not 150)
- String comparison issues: "0150" < "0099" returns TRUE

**Dual Validation Systems**:
- **HTML5 constraints**: Check immediately on keystroke (min, max, step)
- **Yup validation**: Runs per standard timing (mount, change, blur, submit)
- **Parse attempts**: Every keystroke attempts numeric parsing

**Performance Considerations**:
- Complex test functions impact responsiveness
- >10 validation rules cause noticeable lag  
- Consider debouncing for real-time validation
- Batch validation for related fields

### Voice Input Requirements {important}

#### Voice Dictation Formats [affects: NumberInput, ControlledNumber] {important}

Voice input requires exact numeric formatting for successful recognition:

**Successful Formats**:
- ✅ "negative fifteen point five" → -15.5
- ✅ "one zero zero zero" → 1000
- ✅ "three point one four one five nine" → 3.14159

**Failed Formats**:
- ❌ "minus fifteen and a half" → NaN
- ❌ "one thousand" → NaN  
- ❌ "fifteen hundred" → NaN
- ❌ "pi" or "pie" → NaN

**Platform Variations**:
- iOS: Siri dictation may auto-format some numbers
- Android: Google voice varies by language settings
- Desktop: Browser-dependent voice APIs

**Training Requirements**: Field teams must be trained on exact numeric dictation or use manual entry for complex values.

### Security Considerations {important}

See [Security Considerations Reference](../references/constraints-reference.md#field-specific-security-considerations) for comprehensive security guidelines.

**Number Field-Specific Security Notes**:
- Scientific notation (1e308) bypasses validation causing overflow
- Precision loss beyond 15-17 digits causes silent data corruption
- BasicAutoIncrementer sequential IDs enable enumeration attacks  
- JavaScript type coercion bypasses validation
- All numbers stored as floats causing rounding errors

### Performance Boundaries {important}

See [Performance Thresholds Reference](performance-thresholds-reference.md) for comprehensive performance limits, testing scenarios, and optimization triggers.

**Number Field-Specific Performance Notes**:
- **Validation complexity**: >10 rules causes 50-200ms blur lag
- **Memory consumption**: ~8KB per field, 8 bytes per numeric value
- **Form limits**: >50 numeric fields causes 2+ second initial render
- **Precision limit**: JavaScript loses precision beyond 17 digits
- **BasicAutoIncrementer**: Degrades with >10,000 ID ranges

**Optimization for Complex Validation**:
```javascript
// Debounce validation for >10 rules
validationSchema: [
  ["yup.number"],
  ["yup.test", "debounced-check", "Value validation",
    debounce(async (value) => {
      // Complex validation logic
      return await validateComplexRules(value);
    }, 300)
  ]
]
```

### Platform Behaviors {important}

#### iOS Platform [affects: All fields] {important}

| Aspect | NumberInput | ControlledNumber | BasicAutoIncrementer |
|--------|------------|------------------|---------------------|
| **Keyboard** | Numeric pad | Numeric pad | N/A (hidden) |
| **Minus key** | ❌ Missing | ❌ Missing | ✅ N/A |
| **Workaround** | Copy-paste | Copy-paste | N/A |
| **Decimal** | ✅ Present | ✅ Present | N/A |
| **Scientific** | ❌ No 'e' | ❌ No 'e' | N/A |

#### Android Platform [affects: All fields] {important}

| Aspect | NumberInput | ControlledNumber | BasicAutoIncrementer |
|--------|------------|------------------|---------------------|
| **Keyboard** | Numeric pad | Numeric pad | N/A (hidden) |
| **Minus key** | ✅ Always shown | ✅ Always shown | ✅ N/A |
| **Confusion** | Shows when min=0 | Shows when min=0 | N/A |
| **Voice input** | ✅ Available | ✅ Available | N/A |

### Accessibility Compliance {important}

See [Accessibility Reference](accessibility-reference.md) for comprehensive WCAG compliance status, touch target requirements, and screen reader support.

**Number Field-Specific Issues**:
- Spinner controls (~20×20px) far below 44px WCAG minimum
- iOS keyboard lacks minus key for negative numbers  
- Generic "must be number" error messages not helpful
- No aria-live regions for validation state changes
- Tremors/gloves make precise spinner interaction difficult

### Export Behavior {important}

See [Data Export Reference](data-export-reference.md) for comprehensive export documentation including CSV/JSON formats, special character handling, and Excel issues.

**Number Field-Specific Export Notes**:
- **BasicAutoIncrementer**: Exports as string with leading zeros - Excel will strip these (e.g., "00042" becomes 42)
- **Scientific notation**: Numbers like 1.23e-7 preserved in CSV but may need formatting in Excel
- **Very large numbers**: Numbers >15 digits lose precision in Excel (123456789012345 becomes 1.23457E+14)
- **Infinity/NaN**: Export as empty cells in CSV, may cause #NUM! errors in Excel
- **Prevention**: Use TemplatedString wrapper with leading apostrophe for Excel-safe IDs:
  ```json
// Example number-fields-02
  {
    "component-name": "TemplatedStringField",
    "template": "'{{identifier_field}}",
    "name": "excel_safe_id"
}
```

## Individual Field Reference {essential}

### NumberInput (Number Input in Designer) {essential}
#### JSON Anti-patterns❌ **NEVER: String initialValue for number**```json{  "component-name": "NumberField",  "initialValue": "0"  // ERROR: Must be number, not string}```✅ **ALWAYS: Use numeric type**```json{  "initialValue": 0  // Correct: number type}```❌ **NEVER: Wrong validation order**```json{  "validationSchema": [    ["yup.min", 0],  // ERROR: Type not declared first    ["yup.number"]  ]}```✅ **ALWAYS: Type first, then constraints**```json{  "validationSchema": [    ["yup.number"],    ["yup.min", 0]  ]}```
#### Common Spec Mappings- "Enter quantity" → NumberField with min validation- "Record measurement" → NumberField with decimal places- "Count items" → NumberField with integer validation- "Temperature reading" → NumberField with range validation
<!-- keywords: numeric, decimal, float, measurement, calculation, validation, null -->

#### Purpose {essential}
Standard numeric data entry supporting floating-point values, null states, and comprehensive validation. Recommended for scientific measurements, calculations, and any numeric data requiring flexibility.

#### Key Features {essential}
- ✅ **Null value support** - Distinguishes "not measured" from zero
- ✅ **Scientific notation** - Full support (1.23e-7)
- ✅ **Flexible validation** - Complete control via JSON
- ✅ **Dual validation** - HTML5 + Yup schema
- ⚠️ **Component name paradox** - Designer "Number Input" → JSON "NumberField"
- ✅ **Styled spin buttons** - Custom CSS with gray background, border, pointer cursor

#### Configuration Parameters {important}

**Designer Accessible**:
```json
// Example number-fields-03
// Template markers added for parametric generation
{
  "component-name": "NumberField",
  "type": "faims-core::Number",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
  "initialValue": null,
  "required": false,
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
}
```

**JSON Enhancement**:
```json
// Example number-fields-04
{
  "validationSchema": [
    ["yup.number"],
    ["yup.required"],
    ["yup.min", 0, "Cannot be negative"],
    ["yup.max", 1000, "Exceeds maximum"],
    ["yup.test", "precision", "Max 1 decimal",
      "value => value == null || Number.isInteger(value * 10)"]
  ],
  "InputProps": {
    "type": "number",
    "inputProps": {
      "min": 0,
      "max": 1000,
      "step": 0.1
    }
  }
}
```

#### Storage Characteristics {comprehensive}

| Input | Storage Type | Database Value | Memory | Export CSV | Export JSON |
|-------|--------------|----------------|--------|------------|-------------|
| Empty field | null | null | 0 bytes | (empty) | null |
| 0 | number | 0 | 8 bytes | 0 | 0 |
| 42.0 | number | 42 | 8 bytes | 42 | 42 |
| 3.14159265358979323846 | number | 3.141592653589793 | 8 bytes | 3.141592653589793 | 3.141592653589793 |
| 1.23e-7 | number | 0.000000123 | 8 bytes | 1.23e-7 | 1.23e-7 |
| 999999999999999999999 | number | 1e21 | 8 bytes | 1e+21 | 1e21 |
| Infinity (overflow) | null | null | 0 bytes | (empty) | null |

**Critical Notes**:
- Trailing zeros never preserved (42.000 → 42)
- Precision silently truncated at ~15-17 significant digits
- Values beyond ±1.8×10³⁰⁸ overflow to Infinity, stored as null
- NaN values from invalid operations stored as null

#### Field-Specific Troubleshooting {important}

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Component name confusion** | Field not recognized | Use `"NumberField"` not `"NumberInput"` |
| **iOS minus key** | Cannot enter negatives | Copy-paste or use TextField |
| **Trailing zeros lost** | 42.0 → 42 | Use TextField if format critical |
| **Scientific notation** | User confusion | Document format in training |

#### Conditional Logic Examples {comprehensive}

**Show field when value exceeds threshold**:
```json
// Example number-fields-05
// Template markers added for parametric generation
{
  "ph_measurement": {
    "component-name": "NumberField",
    "type": "faims-core::Number",
    "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
    "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
  },
  "alkaline_warning": {
    "component-name": "RichText",
    "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
    "content": "⚠️ High pH detected - verify calibration",
    "condition": {
      "operator": ">",
      "field": "ph_measurement", 
      "value": 8.5
    }
  }
}
```

**Null value handling in conditions**:
```json
// Example number-fields-06
{
  "condition": {
    "operator": "and",
    "conditions": [
      {
        "operator": "!=",
        "field": "depth_reading",
        "value": null
      },
      {
        "operator": ">",
        "field": "depth_reading",
        "value": 0
      }
    ]
  }
}
```

#### Implementation Examples {comprehensive}

**Environmental Monitoring**:
```json
// Example number-fields-07
// Template markers added for parametric generation
{
  "component-name": "NumberField",
  "type": "faims-core::Number",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
  "validationSchema": [
    ["yup.number"],
    ["yup.required"],
    ["yup.min", -2, "Below freezing point"],
    ["yup.max", 40, "Above expected max"]
  ]
}
```

### ControlledNumber (Controlled Number in Designer) {essential}

⚠️ **CRITICAL WARNING**: ControlledNumber is a Designer-only abstraction, NOT a real component in the codebase. It maps to NumberField in JSON.

#### JSON Anti-patterns

❌ **NEVER: This component doesn't exist in codebase**
```json
// Example number-fields-08
{
  "component-name": "TextField"
}
```
✅ **ALWAYS: Use NumberField**
```json
// Example number-fields-09
{
  "component-name": "NumberField",
  "component-namespace": "faims-custom"
}
```

#### Common Spec Mappings
- Designer-only abstraction → Maps to NumberField in JSON
- Not a real component → Always use NumberField
<!-- keywords: range, bounded, min-max, constrained, rating, percentage -->

#### Purpose {essential}
Designer-accessible bounded numeric input for non-technical users needing range validation without JSON editing. Ideal for ratings, percentages, and constrained measurements.

#### Key Features {essential}
- ✅ **Designer min/max** - No JSON required for bounds
- ✅ **HTML5 enforcement** - Browser-level validation
- ⚠️ **Type mismatch** - Declares Integer, accepts floats
- ❌ **No null support** - Always has value (default 0)
- ❌ **Fixed initial value** - Always 0

#### Configuration Parameters {important}

**Designer Configuration**:
```json
// Example number-fields-10
// Template markers added for parametric generation
{
  "component-name": "TextField",
  "type": "faims-core::Integer",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
  "min": 1,
  "max": 10,
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
  "initialValue": 0
}
```

**JSON Enhancement** (optional):
```json
// Example number-fields-11
// Template markers added for parametric generation
{
  "validationSchema": [
    ["yup.number"],
    ["yup.Whole numbers only", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
    ["yup.required"]
  ]
}
```

#### Storage Characteristics {comprehensive}

| Input | Storage Type | Database Value | Memory | Export CSV | Export JSON |
|-------|--------------|----------------|--------|------------|-------------|
| Empty (not possible) | number | 0 | 8 bytes | 0 | 0 |
| 0 | number | 0 | 8 bytes | 0 | 0 |
| 5.5 | number | 5.5 | 8 bytes | 5.5 | 5.5 |
| 10 | number | 10 | 8 bytes | 10 | 10 |

**Critical Notes**:
- Cannot store null - always has numeric value
- Decimals accepted despite Integer type declaration
- Initial value always 0 (may violate min constraint)

#### Field-Specific Troubleshooting {important}

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Type mismatch** | Decimals accepted | Document or add integer validation |
| **Initial value 0** | Violates min=1 | Set appropriate minimum |
| **No null support** | Cannot skip field | Use NumberInput if optional |
| **iOS minus key** | Cannot enter negatives | Use NumberInput with JSON |

#### Conditional Logic Examples {comprehensive}

**Trigger action based on rating**:
```json
// Example number-fields-12
// Template markers added for parametric generation
{
  "quality_rating": {
    "component-name": "TextField",
    "type": "faims-core::Integer",
    "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
    "min": 1,
    "max": 5
  },
  "poor_quality_notes": {
    "component-name": "MultilineTextField",
    "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
    "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
    "condition": {
      "operator": "<=",
      "field": "quality_rating",
      "value": 2
    }
  }
}
```

#### Implementation Examples {comprehensive}

**Survey Rating**:
```json
// Example number-fields-13
// Template markers added for parametric generation
{
  "component-name": "TextField",
  "type": "faims-core::Integer",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
  "min": 1,
  "max": 5,
  "initialValue": 3,
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
}
```

### BasicAutoIncrementer (Basic Auto-incrementer in Designer) {essential}
#### JSON Anti-patterns❌ **NEVER: Expecting number type from counter**```json{  "component-name": "BasicAutoIncrementer",  // Returns "BAI-001" not 1}```✅ **UNDERSTAND: Returns formatted string**```json{  // Returns: "BAI-001", "BAI-002", etc.  // Not: 1, 2, 3}```❌ **NEVER: Using as required field**```json{  "component-name": "BasicAutoIncrementer",  "validationSchema": [["yup.string"], ["yup.required"]]  // ERROR}```✅ **ALWAYS: Auto-generated fields are never required**```json{  "component-name": "BasicAutoIncrementer"  // No validation needed - auto-populates}```
#### Common Spec Mappings- "Auto ID" → BasicAutoIncrementer (generates BAI-001, BAI-002...)- "Sequential number" → BasicAutoIncrementer with prefix- "Counter field" → BasicAutoIncrementer (string output)- Note: Returns string, not number
<!-- keywords: sequence, identifier, auto-increment, catalog, specimen, string -->

#### Purpose {essential}
Generates sequential string identifiers for distributed offline data collection. Returns zero-padded strings suitable for specimen numbers, catalog IDs, and sequential references.

#### Key Features {essential}
- ⚠️ **Returns STRING not number** - Critical for understanding
- ✅ **Offline capable** - Range-based allocation
- ✅ **Zero padding preserved** - "00042" maintained
- ❌ **No duplicate detection** - Requires manual coordination
- ⚠️ **Excel strips zeros** - Always use with TemplatedString

#### Configuration Parameters {important}

**Designer Configuration**:
```json
// Example number-fields-14
// Template markers added for parametric generation
{
  "component-name": "BasicAutoIncrementer",
  "type": "faims-core::String",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "form_id": "specimen_registration",
  "num_digits": 5,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
}
```

**Required Integration Pattern**:
```json
// Example number-fields-15
{
  "component-name": "TemplatedStringField",
  "name": "full_specimen_id",
  "template": "SPEC-{{specimen_number}}-{{_YYYY}}",
  "label": "Complete Specimen ID"
}
```

#### Storage Characteristics {comprehensive}

| State | Storage Type | Database Value | Memory | Export CSV | Export JSON |
|-------|--------------|----------------|--------|------------|-------------|
| Ungenerated | string | "" | 2 bytes | (empty) | "" |
| Generated "00001" | string | "00001" | 7 bytes | "00001" | "00001" |
| Generated "99999" | string | "99999" | 7 bytes | "99999" | "99999" |
| With template | string | As composed | varies | Quoted | String |

**Critical Notes**:
- Never null - always empty string or value
- Padding preserved exactly as generated
- No numeric operations possible
- Template composition happens at display time

#### Range Management Protocol {important}

**External Coordination Spreadsheet** (Required):

| Device ID | User | Form ID | Range Start | Range End | Status | Date |
|-----------|------|---------|-------------|-----------|--------|------|
| iPad-A001 | Smith | specimen | 1 | 999 | Active | 2024-01-15 |
| iPad-A002 | Jones | specimen | 1000 | 1999 | Reserved | 2024-01-15 |

**Requirements**:
- Cloud-accessible (e.g., Google Sheets or Office365)
- Version controlled
- Immediate updates
- Team-wide access

##### Downloadable Template

Save the following as `range_allocation_registry.csv` and maintain in your project's shared drive:

```csv
# BasicAutoIncrementer Range Allocation Registry
# CRITICAL: Maintain this spreadsheet to prevent duplicate identifiers
# Upload to shared drive and update immediately upon any allocation
# 
# Status options: Active, Reserved, Exhausted, Disabled
# Ensure ranges NEVER overlap within the same Form ID
#
Device ID,User,Form ID,Range Start,Range End,Date Allocated,Status,Notes
iPad-A001,J. Smith,specimen_registration,1,999,2024-01-15,Active,Site A deployment - Field team 1
iPad-A001,J. Smith,specimen_registration,1000,1999,2024-03-20,Reserved,Contingency for Site A
iPad-A002,M. Jones,specimen_registration,2000,2999,2024-01-15,Active,Site B deployment - Field team 2
Phone-B001,K. Wilson,feature_recording,1,500,2024-01-15,Exhausted,Completed 2024-02-10
Phone-B001,K. Wilson,feature_recording,501,1000,2024-02-10,Active,Current range
Phone-B002,L. Chen,feature_recording,1001,1500,2024-01-15,Active,Remote team
Tablet-C001,A. Brown,finds_register,1,999,2024-01-20,Active,Laboratory cataloging
Tablet-C001,A. Brown,finds_register,1000,4999,2024-01-20,Reserved,Year 2024 allocation
Desktop-LAB,Lab Team,accession_register,10000,19999,2024-01-01,Active,Central processing
Desktop-LAB,Lab Team,accession_register,20000,29999,2024-01-01,Reserved,2025 allocation
#
# ADD NEW ALLOCATIONS BELOW - NEVER DELETE EXHAUSTED RANGES (Archive only)
#
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
```

**Usage Instructions**:
1. Save as CSV file in shared cloud storage (Google Drive, Dropbox, etc.)
2. Import into Google Sheets or Excel for easier management
3. Enable sharing with all team members
4. Set up notification rules for changes (if using Google Sheets)
5. Review weekly during active fieldwork
6. Never delete rows - mark as "Exhausted" and archive annually

#### Field-Specific Troubleshooting {important}

| Issue | Symptom | Solution |
|-------|---------|----------|
| **String type confusion** | Arithmetic fails | Document string return |
| **Duplicate IDs** | Same number multiple devices | Check range overlap |
| **Excel strips zeros** | "00042" → 42 | Use TemplatedString |
| **Range exhaustion** | Generation stops | Allocate new range |

#### Conditional Logic Examples {comprehensive}

**String comparison for identifiers**:
```json
// Example number-fields-16
// Template markers added for parametric generation
{
  "specimen_id": {
    "component-name": "BasicAutoIncrementer",
    "type": "faims-core::String",
    "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
    "form_id": "specimens",
    "num_digits": 5
  },
  "first_specimen_flag": {
    "component-name": "RichText",
    "content": "📍 This is the first specimen of the day",
    "condition": {
      "operator": "is",
      "field": "specimen_id",
      "value": "00001"
    }
  }
}
```

**Cannot use numeric operators**:
```json
// Example number-fields-17

{
  "condition": {
    "operator": ">",
    "field": "specimen_id",
    "value": 100
  }
}


{
  "condition": {
    "operator": "contains",
    "field": "specimen_id",
    "value": "999"
  }
}
```

#### Implementation Examples {comprehensive}

**Museum Cataloging**:
```json
// Example number-fields-18
[
  {
    "component-name": "BasicAutoIncrementer",
    "type": "faims-core::String",
    "name": "accession_seq",
    "form_id": "accessions",
    "num_digits": 6
  },
  {
    "component-name": "TemplatedStringField",
    "name": "accession_number",
    "template": "{{museum_code}}.{{_YYYY}}.{{accession_seq}}"
  }
]
```

## Troubleshooting Guide {important}

### Critical Issues Table {important}

| 🔴 Critical Issue | Fields Affected | Impact | Immediate Action |
|-------------------|-----------------|--------|------------------|
| **iOS minus key missing** | NumberInput, ControlledNumber | Cannot enter negatives | Use TextField or copy-paste |
| **Type mismatches** | All three | Data integrity risk | Document extensively |
| **No duplicate detection** | BasicAutoIncrementer | ID collisions | Implement range protocol |
| **Excel strips zeros** | BasicAutoIncrementer | ID corruption | Always use TemplatedString |

### Common Problems Table {important}

| 🟡 Problem | Symptom | Affected Fields | Solution |
|------------|---------|-----------------|----------|
| **Component name paradox** | Field not found | NumberInput | Use "NumberField" in JSON |
| **Decimals in Integer field** | Type confusion | ControlledNumber | Add validation or document |
| **String arithmetic** | Calculations fail | BasicAutoIncrementer | Never use for math |
| **Voice input fails** | NaN errors | NumberInput, ControlledNumber | Train exact format |
| **Touch targets small** | Hard to tap | NumberInput, ControlledNumber | Custom CSS |

### Detailed Issue Matrix {important}

| Issue | Affects | Symptoms | Solution | Priority |
|-------|---------|----------|----------|----------|
| **Validation lag** | NumberInput with >10 rules | Sluggish response on blur | Debounce validation | Medium |
| **Memory accumulation** | All fields in large forms | Browser tab crash >1000 fields | Paginate forms | High |
| **Precision silently lost** | NumberInput >17 digits | 9999999999999999 → 10000000000000000 | Document limitation | High |
| **Voice input fails** | NumberInput, ControlledNumber | "one thousand" → NaN | Train exact format | Medium |
| **Spinner too small** | NumberInput, ControlledNumber | Miss-clicks on mobile | Custom CSS sizing | Low |
| **No thousands separator** | NumberInput, ControlledNumber | Hard to read 1000000 | Feature pending | Low |
| **Paste validation timing** | All fields | Error doesn't appear immediately | Known HTML5 behavior | Low |
| **Scientific notation confusion** | NumberInput | Users don't understand 1.23e5 | Training required | Medium |
| **Null vs empty string** | ControlledNumber | Cannot represent "not measured" | Use NumberInput | High |
| **Browser autofill** | NumberInput | Fills with strings | Clear and retype | Low |

### Quick Fixes Table {important}

| 🟢 Quick Fix | Issue | Fields | Action |
|--------------|-------|--------|--------|
| **Add nullable()** | Empty field errors | NumberInput | `["yup.nullable"]` |
| **Wrap in template** | Excel zero stripping | BasicAutoIncrementer | Use TemplatedString |
| **Copy negative value** | iOS minus missing | NumberInput, ControlledNumber | Paste from notes |
| **Check range overlap** | Duplicate IDs | BasicAutoIncrementer | Review allocation log |

### Complete Error Reference {comprehensive}

| Error Message | Field | Scenario | Root Cause | Solution |
|---------------|-------|----------|------------|----------|
| "Must be a number" | NumberInput | Empty required field | Yup validation without nullable() | Add .nullable() to schema |
| "Cannot read property 'NumberField' of undefined" | NumberInput | Config error | Wrong component-name | Use "NumberField" not "NumberInput" |
| "Value must be less than or equal to X" | ControlledNumber | Exceeds max | HTML5 constraint | Adjust max or use NumberInput |
| "Invalid prop 'type-returned'" | All | JSON error | Wrong type string | Check exact type format |
| "Field is required" | All | Submit without value | Required validation | Enter value or remove required |
| "No ranges available" | BasicAutoIncrementer | Range exhausted | All numbers used | Allocate new range |
| "Duplicate identifier detected" | BasicAutoIncrementer | ID collision | Range overlap | Check range allocation |
| "NaN" | NumberInput | Voice input | Natural language | Use exact numeric format |
| "Maximum update depth exceeded" | All | Infinite loop | Circular validation | Check validation dependencies |
| "Out of memory" | All | Large dataset | Too many fields | Implement pagination |

### Error Message Reference {important}

| Error Message | Field | Meaning | Solution |
|---------------|-------|---------|----------|
| "Error with numeric input, please enter a valid number." | NumberInput | Invalid input (NaN or null) | Enter valid numeric value |
| "Component 'NumberInput' not found" | NumberInput | Wrong JSON component name | Use `"NumberField"` not `"NumberInput"` |
| "Must be a number" | All numeric | Empty field or invalid input | Add `["yup.nullable"]` or enter valid number |
| "yup.required is not a function" | All | Wrong validation order | Put type first: `["yup.number"], ["yup.required"]` |
| "TypeError: Cannot perform arithmetic" | BasicAutoIncrementer | String not number | Returns string - use for IDs only |
| "Value must be at least X" | NumberInput/Controlled | Below configured minimum | Check min constraint or adjust value |
| "Value must not exceed X" | NumberInput/Controlled | Above configured maximum | Check max constraint or adjust value |
| "Field is required" | All | Missing required value | Enter value or make field optional |
| "Invalid format" | BasicAutoIncrementer | Pattern validation failed | Check regex pattern in validationSchema |
| "Precision lost" | NumberInput | >17 significant digits | JavaScript IEEE 754 limitation |
| "Cannot read property 'length' of null" | NumberInput | Wrong initialValue type | Use null for numbers, not strings |


### Quick Reference Matrix {important}

| If you see... | First try... | Then try... | Last resort... |
|---------------|--------------|-------------|----------------|
| "Component NumberInput not found" | Change to "NumberField" in JSON | Check component-namespace | Recreate field in Designer |
| Cannot enter negative on iOS | Copy from Notes app | Use TextField with pattern | Document workaround |
| Excel corrupts IDs | Use BasicAutoIncrementer | Wrap in TemplatedString | Export as JSON |
| "Must be a number" on empty | Add `nullable()` validation | Make field required | Set initialValue: 0 |
| Decimals in ControlledNumber | Add `yup.integer()` validation | Accept decimal storage | Use NumberInput |
| Scientific notation appears | Add helper text explanation | Use TextField for display | Accept notation |
| Precision lost >17 digits | Document limitation | Use string field | Reduce precision |
| Cannot skip ControlledNumber | Switch to NumberInput | Accept 0 default | Make optional |
| Touch targets too small | Custom CSS for sizing | Train users | Accept limitation |
| Voice input fails | Train "one zero zero zero" | Manual entry | Provide number pad |
### Debug Checklists {comprehensive}

**NumberInput Checklist**:
- [ ] Using "NumberField" not "NumberInput" in JSON
- [ ] Validation schema properly formatted (array of arrays)
- [ ] InitialValue is null not undefined for empty
- [ ] Min/max constraints don't conflict
- [ ] iOS negative value workaround documented

**ControlledNumber Checklist**:
- [ ] Initial value within min/max bounds
- [ ] Integer enforcement added if needed
- [ ] Type mismatch documented
- [ ] Alternative for null values considered

**BasicAutoIncrementer Checklist**:
- [ ] Range allocation documented externally
- [ ] No overlapping ranges across devices
- [ ] TemplatedString wrapper implemented
- [ ] String type understood by team
- [ ] Form ID matches exactly

### Comprehensive Testing Matrix {comprehensive}

**NumberInput Testing**:
- [ ] Empty field saves as null (not 0 or "")
- [ ] Validation message appears only after blur
- [ ] Scientific notation accepted (1.23e-7)
- [ ] Overflow values rejected (>1.8e308)
- [ ] Precision truncation documented (>17 digits)
- [ ] iOS negative entry workaround tested
- [ ] Android minus key behavior documented
- [ ] Voice input format documented
- [ ] Conditional logic with null values
- [ ] CSV export preserves scientific notation
- [ ] JSON export maintains type (number not string)

**ControlledNumber Testing**:
- [ ] Initial value within bounds
- [ ] Cannot set to null (always has value)
- [ ] Decimal values accepted despite Integer type
- [ ] Min/max bounds enforced on blur
- [ ] Spinner respects bounds (desktop)
- [ ] Helper text displays correctly
- [ ] Required validation works
- [ ] Export includes all values

**BasicAutoIncrementer Testing**:
- [ ] Range allocation documented
- [ ] No duplicate IDs across devices
- [ ] Leading zeros preserved
- [ ] TemplatedString integration works
- [ ] String type understood (no math operations)
- [ ] Form ID exact match
- [ ] CSV export quoted properly
- [ ] Excel protection implemented
- [ ] Range exhaustion handled
- [ ] Settings UI accessible

## JSON Examples {comprehensive}

### Example 1: Basic Integer Field
```json
// Example number-fields-19
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": true
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Count is required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", 0, "Count cannot be negative"],
      ["yup.Must be a whole number", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
    ],
    "initialValue": 0
  }
}
```

### Example 2: Decimal Measurement Field
```json
// Example number-fields-20
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": true,
      "precision": 2
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Depth is required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", 0, "Depth cannot be negative"],
      ["yup.max", 100, "Maximum depth 100m"]
    ],
    "initialValue": null
  }
}
```

### Example 3: Controlled Range Slider
```json
// Example number-fields-21
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "min": 1,
      "max": 10,
      "step": 1,
      "marks": true
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Rating is required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
    ],
    "initialValue": 5
  }
}
```

### Example 4: Auto-incrementing ID
```json
// Example number-fields-22
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "BasicAutoIncrementer",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "incrementer": "specimen-counter",
      "num_digits": 5,
      "form_id": "specimens"
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.Specimen number required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
    ],
    "initialValue": ""
  }
}
```

### Example 5: pH Value with Precision
```json
// Example number-fields-23
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": true,
      "precision": 2
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.pH value required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", 0, "pH cannot be less than 0"],
      ["yup.max", 14, "pH cannot exceed 14"],
      ["yup.test", "precision", "Maximum 2 decimal places",
        "value => value == null || Number.isInteger(value * 100)"]
    ],
    "initialValue": 7.0
  }
}
```

### Example 6: Percentage Field
```json
// Example number-fields-24
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "InputProps": {
        "endAdornment": "%"
      }
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", 0, "Cannot be less than 0%"],
      ["yup.max", 100, "Cannot exceed 100%"],
      ["yup.Must be whole number", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
    ],
    "initialValue": 0
  }
}
```

### Example 7: Temperature with Negative Values
```json
// Example number-fields-25
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "precision": 1
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", -50, "Minimum -50°C"],
      ["yup.max", 60, "Maximum 60°C"]
    ],
    "initialValue": null
  }
}
```

### Example 8: Conditional Number Field
```json
// Example number-fields-26
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": true,
      "precision": 1
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Thickness required for ceramics", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", 0.1, "Minimum 0.1mm"],
      ["yup.max", 100, "Maximum 100mm"]
    ],
    "initialValue": null,
    "condition": {
      "operator": "includes",
      "field": "artifact-materials",
      "value": "ceramic"
    }
  }
}
```

### Example 9: GPS Coordinates
```json
// Example number-fields-27
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": true,
      "precision": 6
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Latitude required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", -90, "Latitude must be between -90 and 90"],
      ["yup.max", 90, "Latitude must be between -90 and 90"]
    ],
    "initialValue": null
  }
}
```

### Example 10: Currency/Budget Field
```json
// Example number-fields-28
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "precision": 2,
      "InputProps": {
        "startAdornment": "$"
      }
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", 0, "Amount cannot be negative"]
    ],
    "initialValue": null
  }
}
```

### Example 11: Weight with Units
```json
// Example number-fields-29
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "precision": 3,
      "InputProps": {
        "endAdornment": "g"
      }
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", 0.001, "Minimum 0.001g"],
      ["yup.max", 10000, "Maximum 10kg"]
    ],
    "initialValue": null,
    "meta": {
      "uncertainty": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    }
  }
}
```

### Example 12: Year Field
```json
// Example number-fields-30
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": true
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Year is required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.Must be a valid year", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", 1900, "Year must be 1900 or later"],
      ["yup.max", "new Date().getFullYear()", "Cannot be future year"]
    ],
    "initialValue": 2024
  }
}
```

### Example 13: Stepped Counter
```json
// Example number-fields-31
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "min": 1,
      "max": 100,
      "step": 1,
      "showButtons": true
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Grid square required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
    ],
    "initialValue": 1
  }
}
```

### Example 14: Area Calculation
```json
// Example number-fields-32
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "precision": 2,
      "InputProps": {
        "endAdornment": "m²"
      }
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", 0.01, "Minimum 0.01 m²"],
      ["yup.max", 10000, "Maximum 10,000 m²"]
    ],
    "initialValue": null
  }
}
```

### Example 15: Sample Size with Validation
```json
// Example number-fields-33
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": true
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Sample size required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.Must be whole number", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", 1, "At least 1 sample required"],
      ["yup.max", 1000, "Maximum 1000 samples"]
    ],
    "initialValue": 1
  }
}
```

### Example 16: Elevation Field
```json
// Example number-fields-34
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "precision": 1
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", -500, "Minimum -500m (below sea level)"],
      ["yup.max", 9000, "Maximum 9000m"]
    ],
    "initialValue": null
  }
}
```

### Example 17: Bearing/Azimuth
```json
// Example number-fields-35
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "InputProps": {
        "endAdornment": "°"
      }
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Must be whole number", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", 0, "Bearing must be 0-359"],
      ["yup.max", 359, "Bearing must be 0-359"]
    ],
    "initialValue": null
  }
}
```

### Example 18: Duration in Minutes
```json
// Example number-fields-36
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "InputProps": {
        "endAdornment": "min"
      }
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.Use whole minutes", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
      ["yup.min", 1, "Minimum 1 minute"],
      ["yup.max", 480, "Maximum 8 hours (480 min)"]
    ],
    "initialValue": null
  }
}
```

### Example 19: Volume Measurement
```json
// Example number-fields-37
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Float",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "required": false,
      "precision": 2,
      "InputProps": {
        "endAdornment": "L"
      }
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.min", 0.01, "Minimum 0.01L"],
      ["yup.max", 1000, "Maximum 1000L"]
    ],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    }
  }
}
```

### Example 20: Complex Sequential ID
```json
// Example number-fields-38
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "BasicAutoIncrementer",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
      "incrementer": "context-sequence",
      "num_digits": 4,
      "form_id": "contexts",
      "prefix": "CTX-"
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.Context number required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
    ],
    "initialValue": "",
    "meta": {
      "annotation": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    }
  }
}
```
  ]
}
```

### Integration Patterns {comprehensive}

**Complete Archaeological Recording**:
```json
// Example number-fields-39
[
  {
    "component-name": "BasicAutoIncrementer",
    "type": "faims-core::String",
    "name": "find_sequence",
    "form_id": "finds",
    "num_digits": 5
  },
  {
    "component-name": "TemplatedStringField",
    "name": "find_number",
    "template": "{{site_code}}-F{{find_sequence}}"
  },
  {
    "component-name": "NumberField",
    "type": "faims-core::Number",
    "name": "depth_cm",
    "label": "Depth (cm)",
    "validationSchema": [
      ["yup.number"],
      ["yup.required"],
      ["yup.min", 0],
      ["yup.max", 500]
    ]
  },
  {
    "component-name": "TextField",
    "type": "faims-core::Integer",
    "name": "condition",
    "label": "Condition (1-5)",
    "min": 1,
    "max": 5
  }
]
```

## Migration Scenarios {comprehensive}

### Scenario 1: Deprecated NumberField to NumberInput
**Context**: Legacy forms using the deprecated NumberField component need migration to the supported NumberInput.

**Challenge**:
- Confusing naming (NumberInput uses "NumberField" as component-name)
- Null handling differences
- Validation schema requirements

**Migration Steps**:
1. Export existing data to preserve number values
2. Update component configuration (keep name as "NumberField"):
   ```json
// Example number-fields-40
   {
     "component-name": "NumberField",
     "type": "faims-core::Number",
     "validationSchema": [
       ["yup.number"],
       ["yup.nullable"]
     ]
   }
   ```
3. Test null vs zero behavior thoroughly
4. Update user documentation about the naming paradox
5. Verify calculations still work correctly

**Solution/Workaround**: Accept the naming confusion; document it prominently in project notes.

### Scenario 2: TextField with Numeric Pattern to NumberInput
**Context**: Projects using TextField for numbers to preserve formatting need proper numeric fields.

**Challenge**:
- Loss of formatting (commas, currency symbols)
- String to number type conversion
- Validation pattern differences

**Migration Steps**:
1. Identify TextFields with numeric patterns
2. Evaluate each field:
   - Need calculations? → Migrate to NumberInput
   - Need format preservation? → Keep as TextField
   - Need range validation? → NumberInput with min/max
3. For migration candidates:
   ```javascript
   // Convert string numbers to actual numbers
   const numericValue = parseFloat(textValue.replace(/[^0-9.-]/g, ''));
   ```
4. Add appropriate validation schemas
5. Test on all platforms (especially iOS for negative numbers)

**Solution/Workaround**: Keep TextField for display-only formatted numbers; use NumberInput for calculations.

### Scenario 3: Manual ID System to BasicAutoIncrementer
**Context**: Projects with manual Excel-based ID allocation moving to automated incrementing.

**Challenge**:
- BasicAutoIncrementer returns strings not numbers
- Range coordination for offline teams
- Sorting issues with string comparison

**Migration Steps**:
1. Document existing ID ranges and allocations
2. Implement range allocation protocol:
   ```json
// Example number-fields-41


   {
     "start_at": 1000,
     "stop_at": 1999
   }
   ```
3. Wrap with TemplatedString for display:
   ```json
// Example number-fields-42
   {
     "component-name": "TemplatedStringField",
     "template": "SITE-{{auto_id}}"
   }
   ```
4. Train teams on range coordination
5. Implement periodic range reconciliation

**Solution/Workaround**: Pre-allocate large ranges; use external spreadsheet for coordination.

### Scenario 4: Adding Range Validation to Existing Data
**Context**: Unvalidated numeric fields need min/max constraints without breaking existing data.

**Challenge**:
- Existing values may violate new constraints
- Null values vs required validation
- Platform-specific input differences

**Migration Steps**:
1. Audit existing data for range:
   ```sql
   SELECT MIN(field), MAX(field), COUNT(*) 
   FROM records WHERE field IS NOT NULL;
   ```
2. Set validation ranges based on actual data
3. For ControlledNumber (Designer users):
   - Set min/max through Designer UI
   - Cannot be null (always has value)
4. For NumberInput (JSON editing):
   ```json
// Example number-fields-43
   "validationSchema": [
     ["yup.number"],
     ["yup.min", 0, "Must be positive"],
     ["yup.max", 100, "Maximum 100"],
     ["yup.nullable"]
   ]
   ```
5. Implement data cleanup for out-of-range values

**Solution/Workaround**: Set permissive ranges initially; tighten gradually with user communication.

### Scenario 5: iOS Negative Number Entry
**Context**: iOS numeric keyboards lack minus key, preventing negative number entry.

**Challenge**:
- Hardware limitation (no OS fix available)
- Users cannot enter negative values
- Copy-paste workaround not intuitive

**Migration Steps**:
1. Identify fields requiring negative values
2. Choose approach based on use case:
   - Option A: Switch to TextField with pattern:
   ```json
// Example number-fields-44
   {
     "component-name": "TextField",
     "pattern": "^-?[0-9]+(\.[0-9]+)?$"
   }
   ```
   - Option B: Provide copy button with common negatives
   - Option C: Use custom component with +/- buttons
3. Add clear helper text about limitation
4. Train iOS users on workaround
5. Document in project README

**Solution/Workaround**: For critical negative values, use TextField; otherwise document copy-paste method.

### Migration Quick Reference

⚠️ **NumberField → NumberInput**:
- Component name changes to "NumberField" (paradox)
- Add explicit nullable() validation
- Test null vs zero semantics

⚠️ **Manual IDs → BasicAutoIncrementer**:
- Returns strings not numbers
- Implement range coordination
- Add TemplatedString wrapper

⚠️ **Any field → ControlledNumber**:
- No null value support
- Type declares Integer but accepts floats
- Initial value always 0

### Migration Script Templates {comprehensive}

**NumberField to NumberInput**:
```javascript
// Before
{
  "component-name": "NumberField", // Old deprecated
  "type": "faims-core::Number"
}

// After
{
  "component-name": "NumberField", // Still "NumberField"!
  "type": "faims-core::Number",
  "validationSchema": [
    ["yup.number"],
    ["yup.nullable"] // Add explicit null handling
  ]
}
```

## Best Practices {comprehensive}

### Design Principles
- **Type clarity**: Document actual vs declared types (ControlledNumber Integer accepts floats)
- **Null handling**: Explicitly handle null vs zero semantics
- **Platform testing**: Always test on iOS for negative numbers
- **Format preservation**: Use TextField when display format matters more than calculation
- **Range allocation**: Pre-allocate ID ranges for offline coordination

### Performance Optimization
- **Validation complexity**: Keep validation rules simple (complex rules cause lag)
- **Form size**: Limit to <50 number fields per form
- **Calculation fields**: Use TemplatedString for derived values, not real-time calculation
- **Touch targets**: Increase input height to 44px minimum for accessibility
- **Precision limits**: Stay within JavaScript's safe integer range (±2^53-1)

### Data Quality Strategies
- **Range validation**: Always set realistic min/max bounds
- **Decimal precision**: Validate decimal places for scientific data
- **Zero vs null**: Document whether empty means zero or no data
- **Unit documentation**: Always specify units in labels or helper text
- **Cross-field validation**: Implement server-side for complex numeric relationships

### Common Patterns
- **Measurements**: NumberInput + unit in label + range validation
- **Identifiers**: BasicAutoIncrementer + TemplatedString wrapper
- **Currency**: TextField with pattern for display, NumberInput for calculations
- **Percentages**: ControlledNumber with 0-100 range
- **Scientific notation**: TextField for display, transform for storage

### Team Coordination
- **Range allocation spreadsheet**: Maintain external coordination for ID ranges
- **Type documentation**: Document all type mismatches in README
- **Platform-specific training**: iOS users need minus key workarounds
- **Validation testing**: Test edge cases (min, max, null, zero)
- **Format conventions**: Standardize number display formats project-wide

### Known Limitations and Feature Requests

**Current Limitations (2025-08)**:

| Feature | Status | Workaround | Priority |
|---------|--------|------------|----------|
| **iOS minus key** | Won't fix (OS limitation) | Copy-paste or TextField | - |
| **Thousands separators** | Feature request pending | None | Medium |
| **Locale-aware formatting** | Not planned | Manual formatting | Low |
| **Custom increment steps** | Under consideration | Manual validation | Low |
| **Real-time calculation** | Performance concerns | Use TemplatedString | Medium |
| **Touch target size** | CSS customization needed | Custom styles | High |
| **Decimal place enforcement** | Requires Yup validation | Add validation rules | Medium |
| **Currency formatting** | Use TextField | Pattern validation | Low |
| **Unit labels inline** | Use helper text | Document pattern | Low |
| **Undo/redo support** | Not implemented | Browser default | Low |

### Recommended Workarounds

```json
// Example number-fields-45
// Template markers added for parametric generation

{
  "component-name": "TextField",
  "component-parameters": {
    "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
    "pattern": "^[0-9]{1,3}(,[0-9]{3})*$",
    "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
  }
}


{
  "component-name": "TextField",
  "component-parameters": {
    "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
    "pattern": "^\\$[0-9]+(\\.[0-9]{2})?$",
    "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
  }
}


{
  "component-name": "TextField",
  "component-parameters": {
    "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
    "min": 0,
    "max": 100,
    "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
  }
}
```

## Field Quirks Index (2025-08) {comprehensive}

### Common Number Field Quirks
- `QUIRK` iOS numeric keyboard universally lacks minus key for negative number entry
  - `ERROR` User cannot enter negative values on iOS devices
  - `FIX` Copy-paste from Notes app or implement TextField with pattern validation
  - `TEST` Open any numeric field on iOS Safari/Chrome
  - See [Platform-Specific Behaviors](../references/platform-reference.md)
- `QUIRK` Deprecated "Number Field" still visible in Designer interface
  - `ERROR` Selecting "Number Field" uses legacy TextField implementation
  - `FIX` Always select "Number Input" instead
  - `TEST` Check Designer field selector for both options
  - See [Deprecated Field Warning](#deprecated-warning)
- `QUIRK` Touch targets (36px) below WCAG minimum (44px) for all numeric inputs
  - `ERROR` Difficult selection for users with motor impairments
  - `FIX` Custom CSS to increase touch target size
  - `TEST` Measure spinner control dimensions in DevTools
  - See [Accessibility Considerations](#accessibility)
- `QUIRK` Android shows minus key even when min=0 configured
  - `ERROR` Users type negative values that fail validation
  - `FIX` Add clear helperText explaining valid range
  - `TEST` Open ControlledNumber with min=0 on Android
  - See [Platform-Specific Behaviors](../references/platform-reference.md)
- `QUIRK` Voice input requires exact numeric pronunciation
  - `ERROR` "one thousand" produces NaN, must say "one zero zero zero"
  - `FIX` Train users on exact format or provide manual entry
  - `TEST` Try voice input with natural language vs exact numbers
  - See [Platform Notes](#platform-notes)
- `QUIRK` No thousands separators in any numeric field
  - `ERROR` 1000000 displays without commas, hard to read
  - `FIX` Feature pending - use TextField for formatted display
  - `TEST` Enter large number, check display format
  - See [Known Limitations](#known-limitations)
- `VERSION` 2025-08

### NumberInput
- `RULE` Component name inverted: Designer "Number Input" → JSON "NumberField"
  - `ERROR` "Field 'NumberInput' not found in component registry"
  - `FIX` Use exact JSON: `"component-name": "NumberField"`
  - `TEST` Verify JSON: `grep '"component-name".*NumberField' notebook.json`
  - See [Designer Quick Guide](#designer-quick-guide)
- `QUIRK` Precision silently truncated beyond 15-17 significant digits
  - `ERROR` No warning when 3.14159265358979323846 → 3.141592653589793
  - `FIX` Document precision limits in helperText
  - `TEST` Enter 20-digit number, check stored value
  - See [Configuration Rules](#configuration-rules)
- `QUIRK` Empty field shows "Must be a number" despite not being required
  - `ERROR` "Must be a number" on blur of empty non-required field
  - `FIX` Add nullable validation:
    ```json
// Example number-fields-46
    "validationSchema": [
      ["yup.number"],
      ["yup.nullable"]
    ]
    ```
  - `TEST` Blur empty field without nullable()
  - See [Validation Patterns](#validation-patterns)
- `QUIRK` Scientific notation auto-converts at 10000000 (1e7)
  - `ERROR` Users confused by "1e7" display format
  - `FIX` Add helperText explaining scientific notation
  - `TEST` Enter 10000000, observe auto-conversion
  - See field details above
- `QUIRK` Trailing zeros never preserved (42.000 → 42)
  - `ERROR` Format requirements lost, precision appears reduced
- `QUIRK` Spin buttons have custom styling (gray background #9F9F9F, 2px black border)
  - `INFO` Styled for better visibility with 8px padding, border-radius 4px
  - `FIX` Override with custom CSS if different styling needed
  - `TEST` Inspect element to verify webkit-inner-spin-button styles
  - `FIX` Use TextField if trailing zeros critical
  - `TEST` Enter 3.1400, check stored value
  - See field details above
- `QUIRK` Values >1.8×10³⁰⁸ overflow to Infinity, stored as null
  - `ERROR` Extreme values silently lost
  - `FIX` Add reasonable max bounds validation
  - `TEST` Enter 1e309, check storage (becomes null)
  - See [Data Type Specifications](#data-types)
- `QUIRK` NaN results stored as null
  - `ERROR` Invalid calculations produce null not NaN
  - `FIX` Validate before calculations
  - `TEST` Force NaN condition, check database
  - See [Field Interactions](#field-interactions)
- `QUIRK` Paste non-numeric silently converts to null on blur
  - `ERROR` Paste "about 100" → null without warning
  - `FIX` Pattern validation or preprocessing
  - `TEST` Paste text into numeric field, blur
  - See [Field Interactions](#field-interactions)
- `VERSION` 2025-08

### ControlledNumber
- `RULE` Type declares Integer but accepts/stores decimals
  - `ERROR` "faims-core::Integer" type allows 3.14159
  - `FIX` Enforce integers explicitly:
    ```json
// Example number-fields-47
    "validationSchema": [
      ["yup.number"],
      ["yup.integer", "Whole numbers only"]
    ]
    ```
  - `TEST` Enter 3.14 in Integer field: `typeof value === 'number' && value === 3.14`
  - See field details above
- `QUIRK` Initial value always 0, may violate minimum constraint
  - `ERROR` "Value must be at least 1" on form load when min=1
  - `FIX` Set min=0 or accept initial validation error
  - `TEST` Configure min=1, check initial state
  - See field details above
- `QUIRK` Cannot store null - always has numeric value
  - `ERROR` Cannot distinguish "not measured" from zero
  - `FIX` Use NumberInput if null values needed
  - `TEST` Try to clear field completely
  - See field details above
- `QUIRK` Android minus key visible even with min=0
  - `ERROR` Confusing UI - key present but values rejected
  - `FIX` Clear helperText about valid range
  - `TEST` Open field with min=0 on Android device
  - See [Platform-Specific Behaviors](../references/platform-reference.md)
- `VERSION` 2025-08

### BasicAutoIncrementer
- `RULE` Returns STRING despite "Number Fields" categorization
  - `ERROR` `TypeError: Cannot perform arithmetic on string "00042"`
  - `FIX` Never use for calculations:
    ```javascript
    // WRONG
    const next = autoValue + 1; // TypeError
    
    // RIGHT
    const display = `ID-${autoValue}`; // String concatenation
    ```
  - `TEST` Check type: `typeof fieldValue === 'string'`
  - See field details above
- `QUIRK` Excel strips leading zeros without protection
  - `ERROR` CSV "00042" becomes 42 in Excel
  - `FIX` Always wrap in TemplatedString:
    ```json
// Example number-fields-48
    {
      "component-name": "TemplatedStringField",
      "template": "SPEC-{{auto_increment}}-{{_YYYY}}"
    }
    ```
  - `TEST` Export CSV, open in Excel, verify zero preservation
  - See field details above
- `QUIRK` No duplicate detection across devices
  - `ERROR` Device A and B both generate "00001" with overlapping ranges
  - `FIX` Maintain external range allocation spreadsheet per protocol
  - `TEST` Allocate same range on two devices, check for duplicates
  - See field details above
- `QUIRK` Hidden field - users confused about auto-generation
  - `ERROR` Users search for field to edit
  - `FIX` Clear labeling that ID is automatic
  - `TEST` Check field visibility in form
  - See field details above
- `QUIRK` Range exhaustion stops generation silently
  - `ERROR` No new IDs generated, no error message
  - `FIX` Monitor range usage, allocate before exhaustion
  - `TEST` Use all numbers in range, try to generate
  - See [Field Interactions](#field-interactions)
- `QUIRK` Form ID must match exactly - case sensitive
  - `ERROR` Wrong form_id resets sequence to 1
  - `FIX` Document exact form_id values
  - `TEST` Use form_id with different case
  - See field details above
- `VERSION` 2025-08

### Performance Quirks
- `QUIRK` Complex validation (>10 rules) causes noticeable blur lag
  - `ERROR` 50-200ms delay on field blur
  - `FIX` Simplify or debounce validation
  - `TEST` Add 15 validation rules, measure blur time
  - See [Performance Thresholds](#performance-thresholds)
- `QUIRK` Forms with >50 numeric fields slow initial render
  - `ERROR` 2+ second delay on form load
  - `FIX` Implement pagination or progressive disclosure
  - `TEST` Create form with 100 NumberInput fields
  - See [Performance Thresholds](#performance-thresholds)
- `QUIRK` Memory accumulates with >1000 fields
  - `ERROR` Browser tab crash at ~4GB
  - `FIX` Paginate at 500 field threshold
  - `TEST` Generate form with 2000 fields, monitor memory
  - See [Field Interactions](#field-interactions)
- `VERSION` 2025-08

### Browser-Specific Quirks
- `QUIRK` Browser autofill may insert strings into numeric fields
  - `ERROR` Validation fails on autofilled data
  - `FIX` Clear and manually re-enter
  - `TEST` Use browser password manager on numeric field
  - See [Troubleshooting](../references/troubleshooting-index.md)
- `QUIRK` Desktop spinner controls respect bounds, mobile doesn't
  - `ERROR` Inconsistent validation behavior
  - `FIX` Document platform differences
  - `TEST` Compare spinner behavior desktop vs mobile
  - See [Platform-Specific Behaviors](../references/platform-reference.md)
- `VERSION` 2025-08

---
## Performance Thresholds Summary {important}

See [Performance Thresholds Reference](performance-thresholds-reference.md) for detailed metrics and testing scenarios.

**Number Field Critical Thresholds**:
- **Validation rules**: >10 causes 50-200ms blur lag
- **Form fields**: >50 causes 2+ second render delay
- **Precision limit**: >17 digits silently truncated (IEEE 754)
- **BasicAutoIncrementer**: >100 ranges causes UI lag, >100,000 IDs causes memory pressure
- **Export**: >10,000 rows adds 5+ seconds generation time
- **Touch targets**: 36px default (below 44px WCAG minimum)

`VERSION` 2025-08

---

## Migration Warnings Index (2025-08) {comprehensive}

### Safe Migrations (No Data Loss)
- `SAFE` Deprecated Number Field → NumberInput when adding nullable validation
  ```json
// Example number-fields-49

  {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type": "number",
    "type-returned": "faims-core::Integer"
  }
  

  {
    "component-name": "NumberField",
    "type": "faims-core::Number",
    "validationSchema": [
      ["yup.number"],
      ["yup.nullable"]
    ]
  }
  ```
  - `VALIDATE` All existing numeric data remains valid
  - `TEST` Check null handling: `value === null` not `value === ""`
- `SAFE` Adding TemplatedString wrapper to existing BasicAutoIncrementer
- `SAFE` Adding validation to NumberInput (makes stricter, not looser)
- `SAFE` Increasing BasicAutoIncrementer num_digits (e.g., 5 → 6)
- `SAFE` Adding min/max constraints to NumberInput via JSON
  - `VALIDATE` Existing values fall within new constraints
  - `TEST` Query for out-of-range values before applying
- `SAFE` Adding precision validation to existing NumberInput
  - `VALIDATE` Current precision levels acceptable
  - `TEST` Check maximum decimal places in existing data
- `SAFE` Adding helperText to any field for iOS negative number workaround
- `VERSION` 2025-08

### Breaking Changes (Data Loss or Corruption Risk)
- `BREAKS` NumberInput → ControlledNumber with existing null values
  - `IMPACT` Null values become 0, losing "not measured" semantics
  - `ERROR` "Cannot convert null to number, defaulting to 0"
  - `NO ROLLBACK` Once null→0 conversion occurs, original state lost
  - `ALTERNATIVE` Keep NumberInput, add min/max via JSON:
    ```json
// Example number-fields-50
    {
      "component-name": "NumberField",
      "validationSchema": [
        ["yup.number"],
        ["yup.min", 0],
        ["yup.max", 100]
      ]
    }
    ```
- `BREAKS` BasicAutoIncrementer → Any numeric field
  - `IMPACT` String "00042" → number 42, losing padding
  - `ERROR` "Cannot parse '00042' as number"
  - `NO ROLLBACK` Leading zeros permanently lost
  - `ALTERNATIVE` Keep as string, use TextField if needed
- `BREAKS` Changing BasicAutoIncrementer form_id
  - `IMPACT` Counter resets to 1, potential duplicates
  - `ERROR` New sequence starts, old sequence orphaned
  - `ROLLBACK` Restore original form_id, but gap remains
- `BREAKS` Reducing BasicAutoIncrementer num_digits
  - `IMPACT` Existing IDs may not fit new format
  - `ERROR` "00042" cannot fit in 3-digit format
  - `NO ROLLBACK` Existing identifiers invalid
- `BREAKS` Removing TemplatedString wrapper from BasicAutoIncrementer
  - `IMPACT` Excel will corrupt all exported identifiers
  - `ERROR` "00042" becomes 42 on next export
  - `NO ROLLBACK` Historical exports already corrupted
  - `ALTERNATIVE` Keep wrapper, hide if not needed visually
- `BREAKS` NumberInput with precision >17 digits → Any migration
  - `IMPACT` Precision already lost, cannot recover
  - `ERROR` 9999999999999999999 already stored as 1e19
  - `NO ROLLBACK` Original precision unrecoverable
  - `ALTERNATIVE` Use TextField for exact numeric strings
- `BREAKS` Changing validation from nullable to required on populated dataset
  - `IMPACT` Records with null values become uneditable
  - `ERROR` "Field is required" blocks form submission
  - `ROLLBACK` Remove required validation immediately
  - `PRECHECK`:
    ```sql
    SELECT COUNT(*) FROM records WHERE field_name IS NULL;
    ```
- `VERSION` 2025-08

### Conditional Migrations (Context Dependent)
- `CONDITIONAL` ControlledNumber → NumberInput for nullable support
  - `PRECHECK` Identify records with value=0 that mean "unmeasured":
    ```python
    # Check if zeros are meaningful or just defaults
    zeros = df[df['field_name'] == 0]
    print(f"Records with 0: {len(zeros)}")
    print("Sample contexts:", zeros[['id', 'notes']].head())
    ```
  - `SAFE IF` All zero values are meaningful measurements
  - `UNSAFE IF` Zero used as placeholder for "not measured"
  - `PROCEDURE`:
    1. Export all data
    2. Convert meaningful zeros to 0, unmeasured to null
    3. Update field configuration
    4. Re-import cleaned data
- `CONDITIONAL` TextField with numeric pattern → NumberInput
  - `PRECHECK` Validate all existing values are numeric:
    ```python
    # Check for non-numeric values
    non_numeric = df[~df['field'].str.match(r'^-?\d+\.?\d*$')]
    print(f"Non-numeric values: {len(non_numeric)}")
    ```
  - `SAFE IF` All values parse as valid numbers
  - `UNSAFE IF` Special formats like "~100" or "100+" exist
  - `PROCEDURE`:
    1. Clean special notations
    2. Convert to numeric type
    3. Add appropriate validation
- `CONDITIONAL` Manual ID system → BasicAutoIncrementer
  - `PRECHECK` Analyze existing ID patterns:
    ```python
    # Check ID format consistency
    ids = df['manual_id']
    formats = ids.str.extract(r'^([A-Z]*)-?(\d+)$')
    print(f"Numeric portions: {formats[1].value_counts()}")
    ```
  - `SAFE IF` Can map existing IDs to ranges
  - `UNSAFE IF` IDs don't follow sequential pattern
  - `PROCEDURE`:
    1. Document existing ID ranges
    2. Allocate non-overlapping ranges
    3. Preserve existing IDs as separate field
    4. Generate new IDs going forward only
- `CONDITIONAL` Scientific notation fields → Standard notation
  - `PRECHECK` Check for values using e-notation:
    ```python
    # Find scientific notation usage
    sci_notation = df[df['field'].str.contains('e', case=False, na=False)]
    print(f"Scientific notation entries: {len(sci_notation)}")
    ```
  - `SAFE IF` Values within standard display range
  - `UNSAFE IF` Values require scientific notation (very large/small)
  - `PROCEDURE`:
    1. Convert notation if within range
    2. Keep scientific for extreme values
    3. Add helperText explaining format
- `CONDITIONAL` iOS deployment → Alternative negative number strategy
  - `PRECHECK` Identify fields accepting negative values:
    ```javascript
    // Find fields with negative capability
    const negativeFields = fields.filter(f => 
      !f.min || f.min < 0
    );
    console.log(`Fields accepting negatives: ${negativeFields.length}`);
    ```
  - `REQUIRED IF` Any NumberInput/ControlledNumber accepts negatives
  - `OPTIONS`:
    1. Switch to TextField with pattern
    2. Add paste instructions to helperText
    3. Provide value templates for copying
  - `PROCEDURE`:
    1. Identify all negative-capable fields
    2. Choose consistent strategy
    3. Update all affected fields
    4. Document in training materials
- `CONDITIONAL` Range exhaustion → New BasicAutoIncrementer ranges
  - `PRECHECK` Monitor range utilization:
    ```sql
    -- Check range usage
    SELECT 
      MAX(CAST(identifier AS INTEGER)) as highest_used,
      999 - MAX(CAST(identifier AS INTEGER)) as remaining
    FROM records 
    WHERE identifier REGEXP '^[0-9]+$';
    ```
  - `CRITICAL IF` <100 numbers remaining
  - `URGENT IF` <500 numbers remaining
  - `PROCEDURE`:
    1. Document current highest number
    2. Allocate next range (e.g., 1000-1999)
    3. Update range allocation spreadsheet
    4. Configure devices with new ranges
    5. Test no overlap exists
- `VERSION` 2025-08

### Emergency Rollback Procedures

#### Corrupted Precision Data
- `SYMPTOMS` Numbers showing as 1e19, loss of significant digits
- `IMMEDIATE`:
  ```sql
  -- Identify affected records
  SELECT * FROM records 
  WHERE CAST(numeric_field AS TEXT) LIKE '%e%'
  OR LENGTH(CAST(numeric_field AS TEXT)) > 15;
  ```
- `ROLLBACK`:
  1. Stop data entry immediately
  2. Export all data
  3. Switch to TextField with pattern validation
  4. Restore from backup if precision critical
- `PREVENTION` Add precision validation before migration
- `VERSION` 2025-08

#### Duplicate Identifier Crisis
- `SYMPTOMS` Same ID on multiple records, sync conflicts
- `IMMEDIATE`:
  ```sql
  -- Find duplicates
  SELECT identifier, COUNT(*) as count
  FROM records
  GROUP BY identifier
  HAVING count > 1;
  ```
- `ROLLBACK`:
  1. Stop all data collection
  2. Export duplicate records
  3. Assign temporary unique suffixes
  4. Implement proper range allocation
  5. Merge duplicate records if needed
- `PREVENTION` External range coordination mandatory
- `VERSION` 2025-08

#### Null to Zero Corruption
- `SYMPTOMS` All unmeasured values showing as 0
- `IMMEDIATE`:
  ```python
  # Identify suspicious zeros
  zeros = df[df['field'] == 0]
  # Check if notes indicate "not measured"
  suspicious = zeros[zeros['notes'].str.contains(
    'not measured|no data|missing', 
    case=False, 
    na=False
  )]
  ```
- `ROLLBACK`:
  1. Export all data immediately
  2. Switch back to NumberInput
  3. Convert suspicious zeros to null
  4. Re-import corrected data
  5. Add nullable validation
- `PREVENTION` Never use ControlledNumber for optional measurements
- `VERSION` 2025-08

### Migration Testing Checklist

#### Pre-Migration Testing
- [ ] Backup all data in multiple formats (CSV, JSON, SQL)
- [ ] Query for edge cases (null, zero, precision extremes)
- [ ] Test migration on subset (10 records)
- [ ] Verify rollback procedure works
- [ ] Document current field configurations
- [ ] Check all conditional dependencies
- [ ] Validate no breaking changes for other fields
- [ ] Confirm range allocations (BasicAutoIncrementer)

#### Post-Migration Validation  
- [ ] All numeric values preserved correctly
- [ ] Null handling maintains semantics
- [ ] Precision within acceptable bounds
- [ ] No duplicate identifiers created
- [ ] Validation rules enforce correctly
- [ ] Export formats unchanged
- [ ] iOS negative entry documented
- [ ] Performance acceptable (<50ms validation)

#### User Acceptance Testing
- [ ] Field entry works on all platforms
- [ ] Validation messages clear
- [ ] Helper text addresses limitations
- [ ] Training materials updated
- [ ] Rollback plan communicated
- [ ] Support contact available
- [ ] Known issues documented

- `VERSION` 2025-08

---

## JSON Patterns Cookbook (2025-08) {comprehensive}

### NumberInput Patterns

```json
// Example number-fields-51
// Template markers added for parametric generation

{
  "component-name": "NumberField",
  "type": "faims-core::Number",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
  "initialValue": null,
  "persistent": true,
  "required": false,
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
}


+ "required": true,
+ "validationSchema": [
+   ["yup.number"],
+   ["yup.This measurement is required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message,
+   ["yup.min", 0, "Value cannot be negative"],
+   ["yup.max", 100, "Value cannot exceed 100"]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.nullable"]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.test", "decimal-places", "Maximum 2 decimal places",
+     "value => value == null || Number.isInteger(value * 100)"]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.Whole numbers only", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.test", "step-validation", "Must be in increments of 0.25",
+     "value => value == null || (value * 4) % 1 === 0"]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.max", 1e10, "Value too large - exceeds system limits"],
+   ["yup.min", 1e-10, "Value too small - exceeds precision"]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.test", "debounced-check", "Complex validation",
+     "debounce(async (value) => { return await validateComplexRules(value); }, 300)"]
+ ]


+ "InputProps": {
+   "type": "number",
+   "inputProps": {
+     "min": 0,
+     "max": 100,
+     "step": 0.01
+   }
+ }


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.min", 0, "Must be positive"]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.test", "overflow-check", "Number too large",
+     "value => value == null || (isFinite(value) && Math.abs(value) < 1e308)"]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.test", "nan-check", "Invalid number",
+     "value => value == null || !isNaN(value)"]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.when", "$isVisible", {
+     "is": true,
+     "then": ["yup.Field is required when visible", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
+   }]
+ ]


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.when", "category", {
+     "is": "percentage",
+     "then": ["yup.min", 0].concat(["yup.max", 100]),
+     "otherwise": ["yup.min", -Infinity]
+   }]
+ ]
```

#### NumberInput ANTI-PATTERNS ⚠️
```json
// Example number-fields-52

{
  "component-name": "NumberField"

}

{
  "component-name": "NumberField"
}


{
  "initialValue": ""

}

{
  "initialValue": null
}


{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type": "number"
}

{
  "component-name": "NumberField",
  "type": "faims-core::Number"
}
```

### ControlledNumber Patterns

```json
// Example number-fields-53
// Template markers added for parametric generation

{
  "component-name": "TextField",
  "type": "faims-core::Integer",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
  "min": 1,
  "max": 10,
  "initialValue": 0,
  "persistent": true
}


+ "validationSchema": [
+   ["yup.number"],
+   ["yup.Please enter a whole number", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
+ ]


{
  "component-name": "TextField",
  "type": "faims-core::Integer",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
  "min": 0,
  "max": 100,
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance,
  "initialValue": 0
}


{
  "component-name": "TextField",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
- "min": 1,
+ "min": 0,
  "max": 5,
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
}
```

#### ControlledNumber ANTI-PATTERNS ⚠️
```json
// Example number-fields-54

{
  "component-name": "TextField",
  "required": false

}

{
  "component-name": "NumberField",
  "validationSchema": [["yup.number"], ["yup.nullable"]]
}


{
  "min": 1,
  "max": 10,
  "initialValue": 0
}

{
  "min": 0,
  "max": 10
}
```

### BasicAutoIncrementer Patterns

```json
// Example number-fields-55

{
  "component-name": "BasicAutoIncrementer",
  "type": "faims-core::String",
  "name": "specimen_seq",
  "form_id": "specimen_registration",
  "num_digits": 5,
  "label": "Specimen Number",
  "persistent": true
}


{
  "fields": [
    {
      "component-name": "BasicAutoIncrementer",
      "type": "faims-core::String",
      "name": "seq_number",
      "form_id": "records",
      "num_digits": 6
    },
    {
      "component-name": "TemplatedStringField",
      "type": "faims-core::String",
      "name": "record_id",
      "template": "REC-{{seq_number}}-{{_YYYY}}",
      "label": "Record Identifier"
    }
  ]
}


{
  "component-name": "BasicAutoIncrementer",
  "name": "accession_seq",
  "form_id": "accessions",
  "num_digits": 6,
  "label": "Accession Sequence"
}


{
  "_range_allocation": {
    "device_A": {"start": 1, "end": 999},
    "device_B": {"start": 1000, "end": 1999},
    "device_C": {"start": 2000, "end": 2999},
    "comment": "CRITICAL: Never overlap ranges",
    "tracking_sheet": "https:
  }
}
```

#### BasicAutoIncrementer ANTI-PATTERNS ⚠️
```json
// Example number-fields-56

{
  "component-name": "BasicAutoIncrementer",
  "name": "count"


}

{
  "component-name": "BasicAutoIncrementer",
  "name": "specimen_id"
}


{
  "component-name": "BasicAutoIncrementer",
  "name": "id"
}

{
  "template": "PREFIX-{{auto_increment}}-SUFFIX"
}







```

### Platform-Specific Configurations

```json
// Example number-fields-57
// Template markers added for parametric generation

{
  "component-name": "NumberField",
  "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
  "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
  "validationSchema": [
    ["yup.number"],
    ["yup.min", 0, "Distance cannot be negative"]
  ],
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
}


{
  "component-name": "TextField",
  "min": 0,
  "max": 100,
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
}


{
  "component-name": "NumberField",
  "InputProps": {
    "type": "number",
    "inputProps": {
      "step": 0.001,
      "min": -1000,
      "max": 1000
    }
  }
}


{
  "component-name": "NumberField",
  "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
}
```


### Performance Optimization Patterns

```json
// Example number-fields-58
// Template markers added for parametric generation

{
  "component-name": "NumberField",
  "validationSchema": [
    ["yup.number"],
    ["yup.value => value ? yup.number().min(0) : yup.number()", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
  ]

}


{
  "form_config": {
    "pagination_threshold": 500,
    "comment": "Forms with >1000 fields risk browser crash"
  }
}
```

### Migration Patterns

```json
// Example number-fields-59
// Template markers added for parametric generation

{

  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type": "number",
  "type-returned": "faims-core::Integer"
}

{
  "component-name": "NumberField",
  "type": "faims-core::Number",
  "validationSchema": [
    ["yup.number"],
    ["yup.nullable"]
  ]
}


{



  "component-name": "NumberField",
  "validationSchema": [
    ["yup.number"],
    ["yup.(value, originalValue) => originalValue === '' ? null : value", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
  ]
}
```

### Excel/CSV Export Safety Patterns

```json
// Example number-fields-60

{
  "export_config": {
    "number_fields": {
      "format": "text",
      "prefix": "'",
      "comment": "Prevents scientific notation conversion"
    }
  }
}


{
  "component-name": "NumberField",
  "export_formatter": "value => value?.toFixed(6)",
  "comment": "Prevents precision loss in export"
}
```

### Integration Patterns (Fields Working Together)

```json
// Example number-fields-61

{
  "specimen_number": {
    "component-name": "BasicAutoIncrementer",
    "type": "faims-core::String",
    "form_id": "specimens",
    "num_digits": 5
  },
  "specimen_id": {
    "component-name": "TemplatedStringField",
    "template": "{{site_code}}-SP{{specimen_number}}-{{_YYYY}}",
    "label": "Full Specimen ID"
  }
}


{
  "length_cm": {
    "component-name": "NumberField",
    "type": "faims-core::Number",
    "label": "Length (cm)"
  },
  "width_cm": {
    "component-name": "NumberField",
    "type": "faims-core::Number",
    "label": "Width (cm)"
  },
  "area_display": {
    "component-name": "TextField",
    "label": "Area (cm²)",
    "disabled": true,
    "helperText": "Calculated from length × width"

  }
}


{
  "has_measurement": {
    "component-name": "Checkbox",
    "label": "Measurement taken?"
  },
  "measurement_value": {
    "component-name": "NumberField",
    "label": "Measurement (mm)",
    "condition": {
      "field": "has_measurement",
      "operator": "is",
      "value": true
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.when", "has_measurement", {
        "is": true,
        "then": ["yup.required", "Enter measurement"]
      }]
    ]
  }
}


{
  "find_number": {
    "component-name": "BasicAutoIncrementer",
    "form_id": "finds",
    "num_digits": 5
  },
  "find_id": {
    "component-name": "TemplatedStringField",
    "template": "{{trench}}-F{{find_number}}"
  },
  "depth_cm": {
    "component-name": "NumberField",
    "validationSchema": [
      ["yup.number"],
      ["yup.min", 0, "Depth cannot be negative"],
      ["yup.max", 500, "Check depth - seems too deep"]
    ]
  },
  "artifact_count": {
    "component-name": "TextField",
    "min": 0,
    "max": 9999,
    "helperText": "Number of artifacts in this context"
  }
}


{
  "context_number": {
    "component-name": "BasicAutoIncrementer",
    "form_id": "contexts",
    "num_digits": 4
  },
  "context_id": {
    "component-name": "TemplatedStringField",
    "template": "{{site}}-{{trench}}-C{{context_number}}"
  },
  "opening_depth": {
    "component-name": "NumberField",
    "validationSchema": [
      ["yup.number"],
      ["yup.required"],
      ["yup.min", -10, "Check: below sea level?"],
      ["yup.max", 100, "Check: unusually deep"]
    ]
  },
  "closing_depth": {
    "component-name": "NumberField",
    "validationSchema": [
      ["yup.number"],
      ["yup.required"],
      ["yup.when", "opening_depth", 
        "(opening, schema) => schema.min(opening, 'Must be deeper than opening')"]
    ]
  }
}
```

### Common Anti-Patterns Across All Number Fields ⚠️

```json
// Example number-fields-62

{
  "validationSchema": [
    ["yup.required"],
    ["yup.number"]
  ]
}

{
  "validationSchema": [
    ["yup.number"],
    ["yup.required"]
  ]
}


{
  "component-name": "NumberField",
  "initialValue": "0"
}

{
  "initialValue": 0
}


{
  "next_value": "{{auto_increment + 1}}"

}

{
  "display_id": "NEXT-{{auto_increment}}"
}


{
  "validationSchema": [
    ["yup.number"],
    ["yup.test", "precision", "Must have 20 decimal places"]

  ]
}
```

### Error Message Quick Reference

```json
// Example number-fields-63

{
  "Component 'NumberInput' not found": "Use 'NumberField' in JSON despite Designer label",
  "Must be a number": "Empty field needs nullable() validation or has wrong type",
  "TypeError: Cannot perform arithmetic": "BasicAutoIncrementer returns string not number",
  "Value must be at least X": "Value below configured minimum",
  "Cannot read property 'length' of null": "initialValue should be empty string not null for some fields",
  "Field is required": "Add value or make field optional",
  "yup.required is not a function": "Put yup.type() before yup.required() in validation array",
  "Precision lost": "JavaScript limit ~15-17 significant digits",
  "00042 becomes 42": "Excel strips zeros - use TemplatedString wrapper"
}
```

---


## JSON Anti-patterns Quick Index {comprehensive}

Anti-patterns have been distributed to their respective field sections for better context locality. This index provides a quick reference:

### Anti-pattern Categories by Field

- **NumberField**: Type validation, initialValue format, decimal handling → [NumberField Anti-patterns](#numberinput)
- **BasicAutoIncrementer**: String vs number output, prefix patterns → [BasicAutoIncrementer Anti-patterns](#basicautoincrementer)
- **ControlledNumber**: Designer abstraction, JSON mapping → [ControlledNumber Anti-patterns](#controllednumber)

### Common Anti-pattern Themes

1. **Type Confusion**: String vs number types in validation
2. **Validation Order**: Type declaration before constraints
3. **Auto-generated Fields**: Never mark as required
4. **Designer Abstractions**: Components that only exist in UI
5. **Platform Limitations**: iOS negative number input issues

## Quick Diagnosis Tables (2025-08) {important}

### When Component Name Errors Occur

| Symptom | Field Type | Likely Cause | Quick Fix | Version |
|---------|------------|--------------|-----------|---------|
| "Component 'NumberInput' not found" | NumberInput | Using Designer label in JSON | Change to `"component-name": "NumberField"` | 2025-08 |
| "Field type not recognized" | Number Field | Using deprecated field | Select "Number Input" in Designer, not "Number Field" | 2025-08 |
| Field saves but doesn't appear | All fields | component-name mismatch | Verify JSON name matches documentation | 2025-08 |
| "Component namespace not found" | Number Field | Old deprecated syntax | Remove namespace, use just component-name | 2025-08 |

### When Type Mismatch Issues Occur

| Symptom | Field Type | Pattern | Fix | Version |
|---------|------------|---------|-----|---------|
| Arithmetic fails with TypeError | BasicAutoIncrementer | `autoValue + 1` | It's a string - use for IDs only | 2025-08 |
| Decimals accepted in Integer field | ControlledNumber | 3.14 stored despite Integer type | Add `["yup.integer"]` validation | 2025-08 |
| "Must be a number" on empty field | NumberInput | Empty non-required field | Add `["yup.nullable"]` to validation | 2025-08 |
| Excel strips leading zeros | BasicAutoIncrementer | Direct CSV export | Wrap in TemplatedString | 2025-08 |
| Scientific notation appears | NumberInput | Large numbers (>1e7) | Add helperText explaining format | 2025-08 |

### When Platform-Specific Problems Occur

| Symptom | When | Why | Try This | If That Fails | Long Term |
|---------|------|-----|----------|---------------|-----------|
| Cannot enter negative numbers | iOS + NumberInput | No minus key on keyboard | Copy from Notes app | Use TextField with pattern | Document workaround |
| Minus key visible but min=0 | Android + ControlledNumber | HTML5 inconsistency | Add helperText "0-100 only" | Ignore (cosmetic) | Train users |
| Touch targets too small | Mobile + All numeric | 36px < WCAG 44px | Custom CSS padding | Zoom interface | Platform update |
| Voice input returns NaN | Mobile + Numeric | Natural language used | Say "fifteen point five" | Manual entry | Training materials |
| Spinner controls missing | Safari + NumberInput | Browser variance | Add custom buttons | Accept limitation | Use Chrome |

### When Validation Errors Occur

| Symptom | Field Type | Root Cause | Solution | Prevention |
|---------|------------|------------|----------|------------|
| "yup.required is not a function" | All | Wrong validation order | Put type first: `["yup.number"], ["yup.required"]` | Always type → constraints |
| Initial validation error on load | ControlledNumber | initialValue 0 < min 1 | Set min=0 or accept error | Check bounds vs initial |
| Precision silently lost | NumberInput | >17 significant digits | Document limitation | Add precision warning |
| Empty field shows error | ControlledNumber | No null support | Use NumberInput instead | Choose correct field |
| Range validation ignored | NumberInput | JSON-only feature | Add validationSchema | Check Designer limits |

### When Performance Issues Occur

| Symptom | Threshold | Cause | Quick Fix | Long-term Solution |
|---------|-----------|-------|-----------|-------------------|
| Blur event lag 50-200ms | >10 validation rules | Complex validation | Simplify rules | Debounce validation |
| Form load delay >2s | >50 numeric fields | Initial render overhead | Progressive disclosure | Pagination |
| Browser tab crash | >1000 fields | Memory exhaustion (~4GB) | Paginate at 500 fields | Split into multiple forms |
| Settings UI freezes | >100 BasicAutoIncrementer ranges | Memory pressure | Archive old ranges | Database cleanup |
| Export hangs | >10,000 records | CSV generation overhead | Batch exports | Server-side generation |
| Validation freezes UI | Complex test functions | Synchronous blocking | Add debouncing (300ms) | Async validation |

### When Accessibility Issues Occur

| Symptom | WCAG Criterion | Failure | Solution | Version |
|---------|----------------|---------|----------|---------|
| Spinner controls hard to tap | 2.5.5 Target Size | 36px < 44px minimum | Custom CSS to increase | 2025-08 |
| Screen reader silent on errors | 4.1.3 Status Messages | No aria-live regions | Would require code change | 2025-08 |
| Cannot enter required negative (iOS) | 2.1.1 Keyboard | No minus key available | Complete barrier - use TextField | 2025-08 |
| Voice input always fails | Input Purpose | Exact format required | Train "one zero zero zero" not "thousand" | 2025-08 |
| No error announcements | 3.3.3 Error Suggestion | Generic messages only | Add specific helperText | 2025-08 |

### When Storage & Precision Problems Occur

| Symptom | Field | Cause | Impact | Solution |
|---------|-------|-------|--------|----------|
| 9999999999999999 → 10000000000000000 | NumberInput | >17 digits precision | Silent data corruption | Document IEEE 754 limits |
| 1e309 stores as null | NumberInput | Overflow to Infinity | Data loss | Add max bounds 1e10 |
| 42.000 → 42 | All numeric | Trailing zeros not preserved | Format lost | Use TextField if critical |
| NaN → null | NumberInput | Invalid calculation | NaN lost | Validate before calc |
| Empty string vs null confusion | ControlledNumber | Always 0, never null | Wrong semantics | Use NumberInput |
| "00042" stays string | BasicAutoIncrementer | String type | Can't calculate | Never use for math |

### When Browser Issues Occur

| Symptom | Browser | Field | Fix | Alternative |
|---------|---------|-------|-----|-------------|
| Autofill inserts text | Chrome/Firefox | NumberInput | Clear and retype | Disable autofill |
| No spinner controls | Safari | NumberInput | Browser limitation | Custom buttons |
| Different decimal separator | European locale | All numeric | Force US locale | Server-side handling |
| Copy-paste validation delay | All browsers | All fields | Expected HTML5 behavior | Wait for blur |
| Memory leak | Chrome | >1000 fields | Restart browser | Pagination |

### When Range Management Issues Occur

| Symptom | Context | Cause | Immediate Fix | Long-term Solution |
|---------|---------|-------|---------------|-------------------|
| Generation stops | BasicAutoIncrementer | Range exhausted | Allocate new range in settings | Monitor usage |
| Duplicate IDs | Multi-device | Overlapping ranges | Check allocation spreadsheet | Implement protocol |
| Settings UI sluggish | >100 ranges | Memory pressure | Archive old ranges | Split forms |
| Range lost | Device replacement | Local-only storage | Consult external log | Maintain backups |
| Cannot modify ID | After generation | One-time only | Accept or migrate data | Document limitation |

### When Export/Import Problems Occur

| Symptom | Field Type | During | Fix | Best Practice |
|---------|------------|--------|-----|---------------|
| "00042" becomes 42 | BasicAutoIncrementer | Excel open | Import as text column | Use TemplatedString |
| Null becomes 0 | ControlledNumber | Any export | Expected behavior - no null | Use NumberInput |
| Scientific notation | NumberInput | Large number export | Format column in Excel | Document threshold |
| Trailing zeros lost | All numeric | Storage/export | Expected (42.0 → 42) | Use TextField if critical |
| CSV has quotes | BasicAutoIncrementer | Export | Normal for strings | No action needed |

### When Migration Issues Occur

| From | To | Symptom | Check | Solution |
|------|-----|---------|-------|----------|
| Deprecated Number Field | NumberInput | Empty shows error | Missing nullable() | Add ["yup.nullable"] |
| TextField | NumberInput | Non-numeric data | grep '[^0-9.-]' | Clean data first |
| NumberInput | ControlledNumber | Null values lost | Check for nulls in DB | Keep NumberInput |
| Manual IDs | BasicAutoIncrementer | Pattern mismatch | Analyze existing IDs | Preserve old, generate new |
| ControlledNumber | NumberInput | Need null support | Check zero semantics | Export, transform, import |

### When Conditional Logic Fails

| Symptom | Field | Cause | Fix | Example |
|---------|-------|-------|-----|---------|
| Numeric comparison fails | BasicAutoIncrementer | String type | Use string operators | "is" not ">" |
| Null breaks condition | NumberInput | null neither > nor < | Check for null first | "!= null AND > 0" |
| Zero triggers unwanted | ControlledNumber | Can't be null | Check for 0 explicitly | "!= 0" |
| Scientific notation compare | NumberInput | String comparison | Parse to number first | Convert 1e7 |

### Quick Reference Matrix

| If you see... | First try... | Then try... | Last resort... |
|---------------|--------------|-------------|----------------|
| "Field not found" error | Check component-name spelling | Verify not using deprecated field | Rebuild field from scratch |
| Cannot enter negatives (iOS) | Copy-paste from another app | Switch to TextField | Provide external keyboard |
| Excel corrupts IDs | Re-import as text | Add TemplatedString wrapper | Use database tools |
| Validation always fails | Check validation order (type first) | Remove validation temporarily | Simplify to basic field |
| Range exhaustion | Allocate new range immediately | Check for range leaks | Split into multiple forms |
| Type mismatch errors | Verify field returns correct type | Check string vs number | Document extensively |
| Performance degradation | Reduce validation complexity | Paginate forms | Archive old data |
| Precision lost silently | Check >17 digits | Add warning to helperText | Use string field |
| Memory exhaustion | Count fields (>1000?) | Implement pagination | Split notebook |
| Debounce not working | Check validation complexity | Simplify rules | Remove validation |
| WCAG violation warnings | Increase touch targets CSS | Document limitation | Alternative interface |
| Overflow to Infinity | Add reasonable max (1e10) | Check calculations | Use TextField |

### Emergency Fixes

| Critical Issue | Immediate Action | Command/Code | Rollback |
|----------------|------------------|--------------|----------|
| All IDs corrupted in Excel | Stop using file | Re-export with TemplatedString | Restore from backup |
| Duplicate IDs in production | Document conflicts | `grep -c "ID-VALUE" *.json` | Assign device suffix |
| Validation blocking all entries | Remove validation | Delete validationSchema block | Re-add incrementally |
| Component not found | Use working example | Copy from this documentation | Previous version |
| Range overlap detected | Stop collection | Check allocation log | Reassign ranges |

### Common Misunderstandings

| What Users Think | What Actually Happens | Why | Correct Mental Model |
|------------------|----------------------|-----|---------------------|
| NumberInput = component name | "NumberField" in JSON | Designer label ≠ JSON name | Always check JSON name |
| BasicAutoIncrementer returns number | Returns string "00042" | Preserves padding | String identifier only |
| ControlledNumber enforces integers | Accepts decimals | Type declaration wrong | Add validation if needed |
| Null same as zero | Different meanings | Scientific data integrity | Null = not measured |
| Deprecated field will be removed | Still in Designer | Backward compatibility | Never use it anyway |

`VERSION` 2025-08

---

## Field Interaction Matrix (2025-08) {important}

| Primary Field | Interacts With | Interaction Type | Notes |
|---------------|----------------|------------------|-------|
| **NumberInput** | Conditional logic | Value comparison | Null requires special handling |
| **ControlledNumber** | Conditional logic | Value comparison | 0 default may trigger conditions |
| **BasicAutoIncrementer** | TemplatedString | Composition | Essential for Excel protection |
| **BasicAutoIncrementer** | Conditional logic | String comparison | Use "is"/"contains" not ">" |
| **All numeric** | Calculations | Source values | BasicAutoIncrementer excluded (string) |

| "Invalid format" | BasicAutoIncrementer | Validation pattern | Check regex in validationSchema |

## See Also {comprehensive}

- **Text Fields**: For string identifiers or formatted numbers (phone, postal codes)
- **TemplatedString**: For wrapping BasicAutoIncrementer to prevent Excel corruption
- **DateTime Fields**: For temporal data (use instead of Unix timestamps)
- **Select/Choice Fields**: For predefined numeric ranges or categories
- **Reference Documents**:
  - [Performance Thresholds Reference](performance-thresholds-reference.md) - Form size limits
  - [Data Export Reference](data-export-reference.md) - Excel number corruption issues
  - [Formik Integration Reference](formik-integration-reference.md) - Null vs empty handling
  - [Accessibility Reference](accessibility-reference.md) - Spinner target size issues

---

## Error Message Quick Reference {important}

### Common Validation Errors (User Visible)
| Message | Component | Trigger | Resolution |
|---------|-----------|---------|------------|
| "Must be a number" | NumberInput, ControlledNumber | Non-numeric input | Enter valid number |
| "Minimum is N" | ControlledNumber | Below min bound | Enter larger value |
| "Maximum is N" | ControlledNumber | Above max bound | Enter smaller value |
| "Field is required" | All number fields | Empty submission | Enter a value |

### iOS-Specific Issues (Platform Errors)
| Issue | Component | Symptom | Workaround |
|-------|-----------|---------|------------|
| Cannot enter negative | NumberInput, ControlledNumber | No minus key | Copy-paste negative |
| Scientific notation rejected | NumberInput | 1.23e-7 fails | Enter decimal form |
| Decimal point issues | All number fields | Locale conflicts | Check device settings |

### Silent Failures (No Error Shown)
| Issue | Component | Detection | Prevention |
|-------|-----------|-----------|------------|
| Precision loss >15 digits | NumberInput | Check stored value | Use string field |
| Leading zeros stripped | BasicAutoIncrementer | Excel corruption | Wrap with TemplatedString |
| NaN saved as null | NumberInput | Check database | Add validation |
| Infinity becomes null | NumberInput | Silent conversion | Add bounds check |

---

## Metadata {comprehensive}

**Document Version**: 3.0.0  
**Last Updated**: 2025-08  
**Applies to**: Fieldmark 2025-08 release  
**Total Fields Documented**: 3  
**Total Known Issues**: 28+  
**Critical Security Warnings**: 6+  

### Revision History
- 2025-08 v3.0.0: Restored complete content from original documentation
- 2025-08 v2.0.0: Complete restructure with deduplication (content loss)
- 2025-07: BasicAutoIncrementer added
- 2025-06: Initial documentation

#
## Fields in Complete Notebooks {important}

For complete working examples showing how these fields integrate into full notebook structures with fviews and viewsets, see:

→ **[Complete Notebook Templates](../references/notebook-templates.md)**

The templates include:
- Minimal survey (3 fields) 
- Basic data collection (10 fields)
- Complex form with validation (20 fields)
- Mobile-optimized with GPS/Photo
- Production archaeological recording

Each template shows the complete JSON structure required for import into Designer, including:
- Proper field → fview → viewset hierarchy
- Required `name` parameters for all fields
- Working validation schemas
- Conditional logic examples

---

## Related Documentation {important}
- TextField Documentation (alternative for iOS negatives)
- TemplatedString Documentation (required for BasicAutoIncrementer)
- Validation Schema Reference
- Platform-Specific Guidelines

---

*Enhanced documentation with 100% content restoration from original field documentation*
---


## Fields in Complete Notebooks {important}

For complete working examples showing how these fields integrate into full notebook structures with fviews and viewsets, see:

→ **[Complete Notebook Templates](../references/notebook-templates.md)**

The templates include:
- Minimal survey (3 fields) 
- Basic data collection (10 fields)
- Complex form with validation (20 fields)
- Mobile-optimized with GPS/Photo
- Production archaeological recording

Each template shows the complete JSON structure required for import into Designer, including:
- Proper field → fview → viewset hierarchy
- Required `name` parameters for all fields
- Working validation schemas
- Conditional logic examples

---

## Related Documentation {important}
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Date & Time Fields](./datetime-fields-v05.md) | [#datetime-fields](#datetime-fields)
- **Next**: [Display Fields](./display-field-v05.md) | [#display-fields](#display-fields)

### Cross-Field Patterns
- **Field Selection**: [Number Field Selection Guidance](../patterns/field-selection-guide.md#number-fields) | [#field-selection](#field-selection)
- **Validation**: [Number Validation](../detail-crossfield-docs/validation.md#number-fields) | [#validation-patterns](#validation-patterns)
- **Calculations**: [Computed Values](../detail-crossfield-docs/patterns.md#calculations) | [#common-patterns](#common-patterns)

### Technical References
- **Designer Limitations**: [Number Constraints](../reference-docs/designer-limitations-reference.md#number-fields) | [#designer-limitations](#designer-limitations)
- **Performance**: [Numeric Processing](../reference-docs/performance-thresholds-reference.md#number-fields) | [#performance-thresholds](#performance-thresholds)

<!-- /concat:references -->
<!-- concat:boundary:end section="number-fields" -->
