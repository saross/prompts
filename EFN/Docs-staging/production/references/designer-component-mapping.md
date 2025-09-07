<!-- concat:boundary:start section="designer-mapping" -->
<!-- concat:metadata
document_id: designer-component-mapping
category: reference
last_updated: 2025-01-06
-->

# Designer UI to Component Mapping Reference

## Document Navigation {essential}
[← Operations Reference](./operations-reference.md) | **Designer Mapping** | [Constraints Reference →](./constraints-reference.md)

## Overview {essential}

This reference provides the critical translation between what users see in the Fieldmark Designer interface and the actual component implementations in JSON. Understanding this mapping is essential for:
- Converting Designer notebooks to JSON
- Debugging field behavior differences
- Understanding why certain Designer options create specific components
- Recognizing that Designer field names ≠ component names

### Key Insight {essential}
The Designer interface presents user-friendly "field types" that are often configurations of base components, not distinct components themselves. For example, "Controlled Number" in Designer is actually a TextField component with numeric configuration.

---

## Complete Designer to Component Mapping {essential}

### Text Input Fields {important}

| Designer Field Name | Component Namespace | Component Name | Type Returned | Configuration Notes |
|-------------------|-------------------|----------------|---------------|-------------------|
| FAIMS Text Field | faims-custom | FAIMSTextField | faims-core::String | Custom FAIMS implementation |
| Text Field | formik-material-ui | TextField | faims-core::String | Basic text input |
| Multiline Text | formik-material-ui | MultipleTextField | faims-core::String | multiline: true |
| Email | formik-material-ui | TextField | faims-core::Email | type: "email" |
| Unique ID | faims-custom | TemplatedStringField | faims-core::String | Template-based generation |
| Address Field | faims-custom | AddressField | faims-core::String | Complex JSON structure |

### Number Fields {important}

| Designer Field Name | Component Namespace | Component Name | Type Returned | Configuration Notes |
|-------------------|-------------------|----------------|---------------|-------------------|
| **Number Input** | faims-custom | **NumberField** | faims-core::Float | Recommended for numerics |
| **Controlled Number** | formik-material-ui | **TextField** | faims-core::Integer | type: "number" + validation |
| Number Field (deprecated) | formik-material-ui | TextField | faims-core::Integer | Legacy, avoid |
| Basic Auto Incrementer | faims-custom | BasicAutoIncrementer | faims-core::String | Returns STRING not number |

**Critical Note**: "Controlled Number" appears as a distinct field in Designer but is actually TextField with InputProps.type="number" and min/max validation.

### Date & Time Fields {important}

| Designer Field Name | Component Namespace | Component Name | Type Returned | Notes |
|-------------------|-------------------|----------------|---------------|--------|
| Date Picker | faims-custom | DatePicker | faims-core::Date | Date only |
| Date Time Picker | faims-custom | DateTimePicker | faims-core::String | Date + time |
| Month Picker | faims-custom | MonthPicker | faims-core::Date | Month/year only |
| Date/Time with Now | faims-custom | DateTimeNow | faims-core::String | Includes "Now" button |

**Note**: No standalone TimePicker component exists despite some documentation references.

### Selection Fields {important}

| Designer Field Name | Component Namespace | Component Name | Type Returned |
|-------------------|-------------------|----------------|---------------|
| Select | faims-custom | Select | faims-core::String |
| Multi-Select | faims-custom | MultiSelect | faims-core::String |
| Hierarchical Select | faims-custom | AdvancedSelect | faims-core::String |
| Checkbox | faims-custom | Checkbox | faims-core::Bool |
| Radio Group | faims-custom | RadioGroup | faims-core::String |

### Location Fields {important}

| Designer Field Name | Component Namespace | Component Name | Type Returned |
|-------------------|-------------------|----------------|---------------|
| Take Point | faims-custom | TakePoint | faims-pos::Location |
| Map Input | mapping-plugin | MapFormField | faims-pos::Location |

### Media Fields {important}

| Designer Field Name | Component Namespace | Component Name | Type Returned |
|-------------------|-------------------|----------------|---------------|
| Take Photo | faims-custom | TakePhoto | faims-attachment::Files |
| File Upload | faims-custom | FileUploader | faims-attachment::Files |

**Note**: AudioRecorder and VideoRecorder do not exist despite documentation references.

### Special Fields {important}

| Designer Field Name | Component Namespace | Component Name | Type Returned |
|-------------------|-------------------|----------------|---------------|
| Related Record | faims-custom | RelatedRecordSelector | faims-core::String |
| Rich Text | faims-custom | RichText | faims-core::String |
| QR Code Scanner | qrcode | QRCodeFormField | faims-core::String |
| Action Button | faims-custom | ActionButton | faims-core::String |
| Random Style | faims-custom | RandomStyle | faims-core::String |

---

## Components That Don't Exist {essential}

These components appear in documentation but are NOT real:

### Incorrectly Documented Components
- **TemplatedIntegerField** - Use NumberField instead
- **TemplatedFloatField** - Use NumberField instead  
- **ControlledNumber** (as component) - Use TextField with type="number"
- **TimePicker** - Use DateTimePicker instead
- **NumberInput** (as component) - Use NumberField
- **AudioRecorder** - Not implemented
- **VideoRecorder** - Not implemented

---

## JSON Configuration Examples {comprehensive}

### Controlled Number (Designer) → TextField Configuration

Designer shows "Controlled Number" but creates:
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::Integer",
  "component-parameters": {
    "label": "Bounded Number",
    "InputProps": {
      "type": "number"
    }
  },
  "validationSchema": [
    ["yup", "number"],
    ["yup", "min", 0, "Must be at least 0"],
    ["yup", "max", 100, "Must be at most 100"]
  ]
}
```

### Email (Designer) → TextField Configuration

Designer shows "Email" but creates:
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::Email",
  "component-parameters": {
    "label": "Email Address",
    "InputProps": {
      "type": "email"
    }
  },
  "validationSchema": [
    ["yup", "string"],
    ["yup", "email", "Enter a valid email"]
  ]
}
```

---

## Component Count Summary {important}

### What Designer Shows
- Approximately 35-40 "field types" in the interface
- User-friendly names and categories
- Configuration variants presented as distinct fields

### What Actually Exists
- **30 actual components** in the codebase
- **5 namespaces**: faims-custom (21), formik-material-ui (4), mapping-plugin (1), qrcode (1), core-material-ui (3)
- Many Designer "fields" are TextField with different configurations

### Why the Discrepancy
1. **User Experience**: Designer abstracts technical details for non-developers
2. **Configuration Variants**: Same component with different settings appears as different fields
3. **Legacy Support**: Some deprecated approaches still visible in Designer
4. **Marketing Names**: User-friendly names don't match technical implementations

---

## Common Mapping Errors {important}

### Incorrect Assumptions
| Wrong Assumption | Reality |
|-----------------|---------|
| Each Designer field = unique component | Many fields use TextField with configuration |
| "Controlled Number" is a component | It's TextField with type="number" |
| Component name matches Designer label | Names often completely different |
| All documented components exist | Some are planned but not implemented |

### Debugging Tips
1. Check actual component namespace - Designer may show wrong namespace
2. Look for InputProps configuration - Often determines field behavior
3. Verify type-returned matches expectations - May affect data storage
4. Test validation schemas separately - Designer may not show all validation

---

## Migration Guide {comprehensive}

### From Designer Export to Manual JSON

When Designer exports JSON, you may need to:

1. **Fix component names**: Designer sometimes exports internal names
2. **Add missing namespaces**: Some exports lack namespace
3. **Correct type-returned**: Designer may use wrong type strings
4. **Add InputProps**: For TextField variants (number, email, etc.)

### Example Migration

Designer might export:
```json
{
  "component-name": "ControlledNumber",
  "type-returned": "Number"
}
```

Correct to:
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::Integer",
  "component-parameters": {
    "InputProps": {
      "type": "number"
    }
  }
}
```

---

## Testing Component Validity {comprehensive}

### Quick Validation Script

```python
# Valid components by namespace
VALID_COMPONENTS = {
    'faims-custom': [
        'FAIMSTextField', 'Select', 'MultiSelect', 'AdvancedSelect',
        'Checkbox', 'RadioGroup', 'RichText', 'TakePhoto', 
        'FileUploader', 'TakePoint', 'MapFormField', 'DatePicker',
        'DateTimePicker', 'MonthPicker', 'DateTimeNow',
        'RelatedRecordSelector', 'BasicAutoIncrementer',
        'TemplatedStringField', 'AddressField', 'ActionButton',
        'RandomStyle', 'NumberField'
    ],
    'formik-material-ui': [
        'TextField', 'Select', 'RadioGroup', 'MultipleTextField'
    ],
    'mapping-plugin': ['MapFormField'],
    'qrcode': ['QRCodeFormField'],
    'core-material-ui': ['Input', 'Checkbox', 'TextField']
}

def validate_component(namespace, component_name):
    """Check if a component actually exists"""
    return component_name in VALID_COMPONENTS.get(namespace, [])
```

---

## Related Documentation {important}

- [Component Reference](./component-reference.md) - Technical component details
- [Constraints Reference](./constraints-reference.md) - Designer limitations
- [Field Selection Guide](../patterns/field-selection-guide.md) - Choosing the right field
- [Number Fields Documentation](../field-categories/number-fields-v05.md) - Number field specifics

---

## Summary {essential}

This mapping reference is critical for understanding the relationship between:
- What users see in Designer (user-friendly field names)
- What gets created in JSON (actual component implementations)
- Why some "fields" are really just configurations of TextField
- Which components actually exist vs. documentation artifacts

Remember: **Designer field names ≠ Component names**. Always verify the actual component and namespace when working with JSON configurations.

---

## Metadata {comprehensive}
- **Document Version**: 1.0
- **Last Updated**: 2025-01-06
- **Applies to**: Fieldmark v3, Designer (current web interface)
- **Component Count**: 30 actual components across 5 namespaces
- **Designer Fields**: ~35-40 user-facing options

<!-- concat:boundary:end -->