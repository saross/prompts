<!-- DEPRECATED: This document has been consolidated into references/component-reference.md -->
<!-- Archived: 2025-01-06 for disaster recovery only -->
<!-- DO NOT UPDATE: Make changes to the consolidated guide instead -->

# Fieldmark Type System Reference

## Overview {essential}

The Fieldmark type system defines how data is stored, validated, and exported across different field types. All field components return values using standardized type identifiers that determine serialization format, validation rules, and export behavior.

## Core Type System {essential}

### Primitive Types

| Type Identifier | JavaScript Type | JSON Format | Description |
|----------------|-----------------|-------------|-------------|
| `faims-core::String` | string | `"text"` | Text data of any length |
| `faims-core::Number` | number | `123.45` | Floating point numbers |
| `faims-core::Integer` | number | `123` | Whole numbers only |
| `faims-core::Bool` | boolean | `true/false` | Boolean values |

### Composite Types

| Type Identifier | JavaScript Type | JSON Format | Description |
|----------------|-----------------|-------------|-------------|
| `faims-core::Array` | Array | `["a", "b"]` | Ordered collections |
| `faims-core::JSON` | Object | `{...}` | Structured JSON objects |

### Specialized Types

| Type Identifier | JavaScript Type | JSON Format | Description |
|----------------|-----------------|-------------|-------------|
| `faims-attachment::Files` | Array<File> | `[{...}]` | File attachment metadata |
| `faims-pos::Location` | GeoJSON Feature | `{...}` | Geographic coordinates |

## Type Usage by Field Category {important}

### Text & Input Fields
- **FAIMSTextField**: `faims-core::String`
- **MultipleTextField**: `faims-core::String` (multiline)
- **TextField**: `faims-core::String`
- **TemplatedStringField**: `faims-core::String` (generated)
- **AddressField**: `faims-core::JSON` (structured address)
- **QRCodeFormField**: `faims-core::String` (scanned value)
- **RichText**: `faims-core::String` (empty - display only)

### Selection & Choice Fields
- **Checkbox**: `faims-core::Bool`
- **Select**: `faims-core::String`
- **MultiSelect**: `faims-core::Array` (of strings)
- **RadioGroup**: `faims-core::String`
- **AdvancedSelect**: `faims-core::String`

### Date & Time Fields
- **DateTimeNow**: `faims-core::String` (ISO 8601)
- **DateTimePicker**: `faims-core::String` (ISO 8601)
- **DatePicker**: `faims-core::String` (ISO 8601 date)
- **MonthPicker**: `faims-core::String` (YYYY-MM)

### Numeric Fields
- **NumberField**: `faims-core::Number`
- **ControlledNumber**: `faims-core::Number`
- **BasicAutoIncrementer**: `faims-core::String` (formatted counter)

### Location Fields
- **TakePoint**: `faims-pos::Location` (GeoJSON Feature)
- **MapFormField**: `faims-core::JSON` (GeoJSON FeatureCollection)

### Media Fields
- **TakePhoto**: `faims-attachment::Files`
- **FileUploader**: `faims-attachment::Files`

### Relationship Fields
- **RelationshipField**: `faims-core::Array` (of record IDs)

### Display Fields
- **RichText**: `faims-core::String` (always empty)

## Type Validation Rules {important}

### String Types
- No length limit by default
- Can add min/max length validation
- Pattern validation via regex
- Email validation for specific variants

### Number Types
- JavaScript number precision limits apply
- Can specify min/max ranges
- Decimal places configurable
- NaN and Infinity not allowed

### Array Types
- Can be empty unless required
- Element type consistency enforced
- Maximum element count configurable
- Duplicate detection available

### JSON Types
- Must be valid JSON objects
- Schema validation available
- Nested depth limits apply
- Circular references prohibited

## Type Conversion & Coercion {comprehensive}

### Automatic Conversions
- **String to Number**: Attempted for numeric fields
- **Date to String**: ISO 8601 format enforced
- **Array to String**: JSON stringification for export
- **Bool to String**: "true"/"false" strings

### Invalid Type Scenarios
```javascript
// Common type mismatches and resolutions
{
  "field": "123",          // String when Number expected - parsed
  "date": 1234567890,       // Timestamp when String expected - converted
  "array": "value",         // String when Array expected - wrapped
  "bool": "yes"            // String when Bool expected - truthy evaluation
}
```

## Export Format Specifications {comprehensive}

### CSV Export
- **String**: Direct value
- **Number**: Numeric format
- **Bool**: "true"/"false"
- **Array**: JSON stringified
- **JSON**: JSON stringified
- **Location**: WKT or JSON string
- **Files**: File URLs concatenated

### JSON Export
- All types maintain native JSON representation
- Metadata preserved in structured format
- Relationships expanded with record data
- Attachments include full metadata

### GeoJSON Export
- Location types exported as Features
- Non-geographic data in properties
- Coordinate systems preserved
- Metadata in Feature properties

## Type-Related Errors {important}

### Common Type Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| Type mismatch | Wrong type returned | Verify component configuration |
| Invalid format | Malformed data | Check validation rules |
| Null reference | Missing required value | Add required validation |
| Array overflow | Too many elements | Set array limits |
| JSON parse error | Invalid JSON structure | Validate JSON syntax |

### Type Migration Issues

When migrating between field types:
- **String → Number**: Parse errors possible
- **Single → Array**: Wrap in array
- **Array → Single**: Data loss warning
- **JSON → String**: Stringify required

## Performance Considerations {comprehensive}

### Type Performance Impact

| Type | Memory Usage | Serialization Cost | Validation Cost |
|------|--------------|-------------------|-----------------|
| String | Variable | Low | Low |
| Number | 8 bytes | Low | Low |
| Bool | 1 byte | Minimal | Minimal |
| Array | N × element | Medium | Medium |
| JSON | Variable | High | High |
| Location | ~1KB | High | High |
| Files | Metadata only | High | Medium |

### Optimization Guidelines
- Prefer primitive types when possible
- Limit array sizes for performance
- Avoid deep JSON nesting
- Cache computed type conversions
- Batch type validations

## Best Practices {important}

### Type Selection
1. Use most specific type available
2. Consider export requirements
3. Plan for type migrations
4. Document type assumptions
5. Validate early and often

### Type Safety
- Always specify type-returned
- Handle null/undefined cases
- Validate before type conversion
- Test edge cases thoroughly
- Document type contracts

### Type Documentation
- Include type in field description
- Note any type conversions
- Document validation rules
- Specify export behavior
- Warn about type limitations

## Invalid Types (Historical) {comprehensive}

These types appear in legacy documentation but are **NOT VALID**:

- ❌ `faims-core::Email` → Use `faims-core::String`
- ❌ `faims-core::DateTime` → Use `faims-core::String`
- ❌ `faims-core::Date` → Use `faims-core::String`
- ❌ `faims-core::Relationship` → Use `faims-core::Array`
- ❌ `faims-core::File` → Use `faims-attachment::Files`
- ❌ `faims-core::Location` → Use `faims-pos::Location`

## Type System Metadata {comprehensive}

- **Version**: 3.0.0
- **Total Valid Types**: 8
- **Primitive Types**: 4
- **Composite Types**: 2
- **Specialized Types**: 2
- **Deprecated Types**: 6
- **Last Updated**: 2025-01-05