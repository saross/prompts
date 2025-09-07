# Enhanced JSON Validation Report

Validated 455 JSON examples

## Summary

- Total examples: 455
- Syntax valid: 362/455
- Examples with comments: 29
- Examples with ellipsis: 14
- Schema compliant: 207
- Component valid: 198
- Security warnings: 1

## Critical Issues (94)


### Syntax Errors (93)
- field-categories/datetime-fields-v05.md:435 - JSON syntax error after cleaning: Extra data
- field-categories/datetime-fields-v05.md:840 - JSON syntax error after cleaning: Extra data
- field-categories/datetime-fields-v05.md:1628 - JSON syntax error after cleaning: Extra data
- field-categories/datetime-fields-v05.md:1661 - JSON syntax error after cleaning: Extra data
- field-categories/datetime-fields-v05.md:1688 - JSON syntax error after cleaning: Extra data
  ... and 88 more


### Invalid Namespaces (1)
- field-categories/media-fields-v05.md:1355 - Invalid namespace 'core'

## Warnings (152)

- Incomplete field definitions: 109
- Type corrections needed: 38
- Other warnings: 4
- Potential XSS risks: 1

## Statistics

### Namespace Usage
- ⚠️ ANY-namespace: 1
- ⚠️ core: 1
- ✓ faims-custom: 187
- ⚠️ faims3: 1
- ✓ formik-material-ui: 21
- ✓ mapping-plugin: 12
- ✓ qrcode: 3

### Top Components
- RelatedRecordSelector: 22
- TextField: 20
- RichText: 19
- NumberField: 17
- FileUploader: 15
- Select: 15
- TakePhoto: 13
- DateTimeNow: 12
- TakePoint: 11
- MapFormField: 11
- Checkbox: 11
- MultiSelect: 11
- DatePicker: 10
- RadioGroup: 9
- DateTimePicker: 8

### Type Distribution
- ✓ faims-attachment::Files: 27
- ⚠️ (needs correction) faims-core::Array: 25
- ✓ faims-core::Bool: 12
- ✓ faims-core::Float: 10
- ✓ faims-core::Integer: 9
- ⚠️ (needs correction) faims-core::JSON: 13
- ✓ faims-core::String: 104
- ✓ faims-pos::Location: 10

## Recommendations

1. Replace all `faims-core::Array` with `faims-core::String`
2. Replace all `faims-core::JSON` with `faims-core::String`
3. 29 examples use comments - consider separate documentation
4. Review 1 potential XSS vulnerabilities in TemplatedString fields