<!-- concat:boundary:start section="component-reference" -->
<!-- concat:metadata
document_id: component-reference
category: references
version: 1.0
last_updated: 2025-01-06
purpose: Comprehensive technical reference for component configuration, namespaces, types, and Formik integration
source_documents:
  - component-namespace-reference.md (8KB)
  - meta-properties-reference.md (9KB)
  - formik-integration-reference.md (10KB)
  - type-system-reference.md (7KB)
-->

# Component Reference

## Overview {essential}

This comprehensive reference consolidates all technical details about Fieldmark v3 component configuration, including namespaces, type systems, meta properties, and Formik integration. It serves as the authoritative source for component implementation and troubleshooting.

## Component Namespace System {essential}

### The Golden Rule

**When in doubt, use `faims-custom`**

Over 90% of Fieldmark components use the `faims-custom` namespace. Only basic text fields use `formik-material-ui`.

### Quick Reference Table

| Component Category | Namespace | Components |
|-------------------|-----------|------------|
| **Text Fields** | `formik-material-ui` | TextField, MultipleTextField |
| **Custom Text** | `faims-custom` | SingleLineTextField, TemplatedStringField, Address, QRCodeFormField |
| **Number Fields** | `faims-custom` | NumberField, BasicAutoIncrementer |
| **DateTime Fields** | `faims-custom` | DateTime, DateTimeNow |
| **Selection Fields** | `faims-custom` | Checkbox, MultiSelect, RadioGroup, Select, AdvancedSelect |
| **Media Fields** | `faims-custom` | TakePhoto, FileUploader |
| **Location Fields** | `faims-custom` / `mapping-plugin` | TakePoint (custom) / MapFormField (plugin) |
| **Relationship** | `faims-custom` | RelatedRecordSelector |

### Complete Component List by Namespace

#### faims-custom Components

**Text & String Fields:**
- `SingleLineTextField` - Basic text input
- `TemplatedStringField` - Auto-generated from template
- `Address` - Structured address with components
- `QRCodeFormField` - Barcode/QR scanner

**Number Fields:**
- `NumberField` - Numeric input with validation
- `BasicAutoIncrementer` - Auto-incrementing identifier

**Date & Time Fields:**
- `DateTime` - Date and time picker
- `DateTimeNow` - Capture current timestamp

**Selection Fields:**
- `Checkbox` - Boolean toggle
- `MultiSelect` - Multiple choice selection
- `RadioGroup` - Single choice from options (DEPRECATED)
- `Select` - Dropdown single selection
- `AdvancedSelect` - Hierarchical tree selection (BETA)

**Media Fields:**
- `TakePhoto` - Camera capture
- `FileUploader` - File upload

**Location Fields:**
- `TakePoint` - GPS coordinate capture (`faims-custom`)
- `MapFormField` - Map-based location selection (`mapping-plugin`)

**Relationship Fields:**
- `RelatedRecordSelector` - Link to other records

#### formik-material-ui Components

**Basic Text Only:**
- `TextField` - Standard Material-UI text field
- `MultipleTextField` - Multi-line text area

### Common Namespace Errors

#### Error: "Component not found: [component-name]"

**Cause 1: Wrong Namespace**
```json
// ❌ WRONG
{
  "component-namespace": "material-ui",
  "component-name": "Select"
}

// ✅ CORRECT
{
  "component-namespace": "faims-custom",
  "component-name": "Select"
}
```

**Cause 2: Missing Namespace**
```json
// ❌ WRONG - No namespace specified
{
  "component-name": "Checkbox"
}

// ✅ CORRECT - Namespace required
{
  "component-namespace": "faims-custom",
  "component-name": "Checkbox"
}
```

**Cause 3: Typo in Namespace**
```json
// ❌ WRONG - Common typos
{
  "component-namespace": "faims-custom-ui"     // Extra suffix
  "component-namespace": "faims_custom"        // Underscore
  "component-namespace": "faimsCustom"         // Camel case
  "component-namespace": "FAIMS-CUSTOM"        // Wrong case
}

// ✅ CORRECT - Exact spelling
{
  "component-namespace": "faims-custom"        // All lowercase, hyphenated
}
```

### Case Sensitivity Rules

Component names are **STRICTLY CASE-SENSITIVE**:

| ❌ Wrong | ✅ Correct | Notes |
|---------|-----------|-------|
| checkbox | Checkbox | Capital C |
| multiselect | MultiSelect | Capital M and S |
| radiogroup | RadioGroup | Capital R and G |
| select | Select | Capital S |
| advancedselect | AdvancedSelect | Capital A and S |
| datetime | DateTime | Capital D and T |
| datetimenow | DateTimeNow | Capital D, T, and N |
| numberfield | NumberField | Capital N and F |
| takepoint | TakePoint | Capital T and P |
| takephoto | TakePhoto | Capital T and P |

### Designer Name vs JSON Name

The Designer UI uses different display names than the JSON component names:

| Designer Shows | JSON Uses | Namespace |
|---------------|-----------|-----------|
| "Checkbox" | `Checkbox` | `faims-custom` |
| "Select Multiple" | `MultiSelect` | `faims-custom` |
| "Select one option" | `RadioGroup` | `faims-custom` |
| "Select Field" | `Select` | `faims-custom` |
| "Select Field (Hierarchical)" | `AdvancedSelect` | `faims-custom` |
| "Text Field" | `TextField` | `formik-material-ui` |
| "Text Area" | `MultipleTextField` | `formik-material-ui` |
| "Number Input" | `NumberField` | `faims-custom` |
| "Date and Time" | `DateTime` | `faims-custom` |
| "Current Date/Time" | `DateTimeNow` | `faims-custom` |
| "Take Photo" | `TakePhoto` | `faims-custom` |
| "Upload File" | `FileUploader` | `faims-custom` |
| "GPS Point" | `TakePoint` | `faims-custom` |
| "Map Location" | `MapFormField` | `mapping-plugin` |

## Type System {important}

### Core Type System

#### Primitive Types

| Type Identifier | JavaScript Type | JSON Format | Description |
|----------------|-----------------|-------------|-------------|
| `faims-core::String` | string | `"text"` | Text data of any length |
| `faims-core::Number` | number | `123.45` | Floating point numbers |
| `faims-core::Integer` | number | `123` | Whole numbers only |
| `faims-core::Bool` | boolean | `true/false` | Boolean values |

#### Composite Types

| Type Identifier | JavaScript Type | JSON Format | Description |
|----------------|-----------------|-------------|-------------|
| `faims-core::Array` | Array | `["a", "b"]` | Ordered collections |
| `faims-core::JSON` | Object | `{...}` | Structured JSON objects |

#### Specialized Types

| Type Identifier | JavaScript Type | JSON Format | Description |
|----------------|-----------------|-------------|-------------|
| `faims-attachment::Files` | Array<File> | `[{...}]` | File attachment metadata |
| `faims-pos::Location` | GeoJSON Feature | `{...}` | Geographic coordinates |

### Type Usage by Field Category

#### Text & Input Fields {#text-field-types}
- **FAIMSTextField**: `faims-core::String`
- **MultipleTextField**: `faims-core::String` (multiline)
- **TextField**: `faims-core::String`
- **TemplatedStringField**: `faims-core::String` (generated)
- **AddressField**: `faims-core::JSON` (structured address)
- **QRCodeFormField**: `faims-core::String` (scanned value)
- **RichText**: `faims-core::String` (empty - display only)

#### Selection & Choice Fields {#selection-field-types}
- **Checkbox**: `faims-core::Bool`
- **Select**: `faims-core::String`
- **MultiSelect**: `faims-core::Array` (of strings)
- **RadioGroup**: `faims-core::String`
- **AdvancedSelect**: `faims-core::String`

#### Date & Time Fields {#datetime-field-types}
- **DateTimeNow**: `faims-core::String` (ISO 8601)
- **DateTimePicker**: `faims-core::String` (ISO 8601)
- **DatePicker**: `faims-core::String` (ISO 8601 date)
- **MonthPicker**: `faims-core::String` (YYYY-MM)

#### Numeric Fields {#number-field-types}
- **NumberField**: `faims-core::Number`
- **ControlledNumber**: `faims-core::Number`
- **BasicAutoIncrementer**: `faims-core::String` (formatted counter)

#### Location Fields {#location-field-types}
- **TakePoint**: `faims-pos::Location` (GeoJSON Feature)
- **MapFormField**: `faims-core::JSON` (GeoJSON FeatureCollection)

#### Media Fields {#media-field-types}
- **TakePhoto**: `faims-attachment::Files`
- **FileUploader**: `faims-attachment::Files`

#### Relationship Fields {#relationship-field-types}
- **RelationshipField**: `faims-core::Array` (of record IDs)

#### Display Fields {#display-field-types}
- **RichText**: `faims-core::String` (always empty)

### Type Validation Rules

#### String Types
- No length limit by default
- Can add min/max length validation
- Pattern validation via regex
- Email validation for specific variants

#### Number Types
- JavaScript number precision limits apply
- Can specify min/max ranges
- Decimal places configurable
- NaN and Infinity not allowed

#### Array Types
- Can be empty unless required
- Element type consistency enforced
- Maximum element count configurable
- Duplicate detection available

#### JSON Types
- Must be valid JSON objects
- Schema validation available
- Nested depth limits apply
- Circular references prohibited

### Type Conversion & Coercion

#### Automatic Conversions
- **String to Number**: Attempted for numeric fields
- **Date to String**: ISO 8601 format enforced
- **Array to String**: JSON stringification for export
- **Bool to String**: "true"/"false" strings

#### Invalid Type Scenarios
```javascript
// Common type mismatches and resolutions
{
  "field": "123",          // String when Number expected - parsed
  "date": 1234567890,       // Timestamp when String expected - converted
  "array": "value",         // String when Array expected - wrapped
  "bool": "yes"            // String when Bool expected - truthy evaluation
}
```

### Export Format Specifications

#### CSV Export
- **String**: Direct value
- **Number**: Numeric format
- **Bool**: "true"/"false"
- **Array**: JSON stringified
- **JSON**: JSON stringified
- **Location**: WKT or JSON string
- **Files**: File URLs concatenated

#### JSON Export
- All types maintain native JSON representation
- Metadata preserved in structured format
- Relationships expanded with record data
- Attachments include full metadata

#### GeoJSON Export
- Location types exported as Features
- Non-geographic data in properties
- Coordinate systems preserved
- Metadata in Feature properties

### Type-Related Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| Type mismatch | Wrong type returned | Verify component configuration |
| Invalid format | Malformed data | Check validation rules |
| Null reference | Missing required value | Add required validation |
| Array overflow | Too many elements | Set array limits |
| JSON parse error | Invalid JSON structure | Validate JSON syntax |

### Invalid Types (Historical)

These types appear in legacy documentation but are **NOT VALID**:

- ❌ `faims-core::Email` → Use `faims-core::String`
- ❌ `faims-core::DateTime` → Use `faims-core::String`
- ❌ `faims-core::Date` → Use `faims-core::String`
- ❌ `faims-core::Relationship` → Use `faims-core::Array`
- ❌ `faims-core::File` → Use `faims-attachment::Files`
- ❌ `faims-core::Location` → Use `faims-pos::Location`

## Meta Properties Configuration {important}

### Overview {essential}

The `meta` property provides standardized metadata options that work identically across ALL field types. These properties control annotations, uncertainty markers, persistence, and display behaviors.

### Standard Meta Structure

```json
{
  "field-name": {
    "component-namespace": "...",
    "component-name": "...",
    "type-returned": "...",
    "component-parameters": {...},
    "validationSchema": [...],
    "initialValue": "...",
    "meta": {
      "annotation": {
        "include": true,
        "label": "Notes"
      },
      "uncertainty": {
        "include": true,
        "label": "Uncertain"
      },
      "persistent": false,
      "displayParent": false
    }
  }
}
```

### Meta Properties Explained

#### annotation
**Purpose**: Adds a free-text notes field alongside the main field

**Structure**:
```json
"annotation": {
  "include": true,    // Boolean: whether to show annotation field
  "label": "Notes"    // String: label for the annotation field
}
```

**Behavior**:
- Creates an additional text input below the main field
- Stores text in a parallel data structure
- Exports as separate column in CSV
- No validation applied to annotation text
- No character limit

**Common Labels**:
- "Notes" - General purpose
- "Comments" - General purpose
- "Annotation" - Default if label omitted
- "[Field] notes" - Context-specific (e.g., "Location notes")
- "Additional information" - Verbose option

#### uncertainty
**Purpose**: Adds a checkbox to mark data as uncertain/questionable

**Structure**:
```json
"uncertainty": {
  "include": true,        // Boolean: whether to show uncertainty checkbox
  "label": "Uncertain"    // String: label for the checkbox
}
```

**Behavior**:
- Creates a checkbox beside/below the main field
- Stores boolean value in parallel structure
- Exports as separate boolean column
- When checked, may trigger visual indicators (field-dependent)
- No validation impact (uncertain data still validates)

**Common Labels**:
- "Uncertain" - Default
- "?" - Minimal
- "Questionable" - Explicit
- "Approximate" - For measurements
- "Needs verification" - Process-oriented
- "Low confidence" - Confidence scale

#### persistent
**Purpose**: Controls whether field value persists across record creation

**Values**:
- `true` - Field retains value when creating new record
- `false` - Field clears to initialValue (default)

**Structure**:
```json
"persistent": true  // or false
```

**Use Cases for persistent: true**:
- Location fields (likely same site)
- Date fields (same day's work)
- Team member fields
- Project phase fields
- Site/area identifiers

**Use Cases for persistent: false**:
- Unique identifiers
- Measurements
- Observations
- Photos
- Specimen data

#### displayParent
**Purpose**: Shows parent record context in related record forms

**Values**:
- `true` - Display parent record information
- `false` - Hide parent context (default)

**Structure**:
```json
"displayParent": true  // or false
```

**Behavior**:
- Only relevant for fields in child records
- Shows parent record's human-readable ID
- Helps maintain context during data entry
- No impact on data storage

### Designer Integration

The Designer interface provides toggles for:
- **Annotation** - Maps to `meta.annotation.include`
- **Uncertainty** - Maps to `meta.uncertainty.include`

The Designer does NOT provide controls for:
- Custom annotation labels (uses "Annotation")
- Custom uncertainty labels (uses "?")
- `persistent` property
- `displayParent` property

These require JSON editing.

### Default Values

If `meta` property is omitted entirely:
```json
// These defaults are applied:
"meta": {
  "annotation": {"include": false},
  "uncertainty": {"include": false},
  "persistent": false,
  "displayParent": false
}
```

### Partial Specification

You can specify only needed properties:
```json
// Only annotation:
"meta": {
  "annotation": {"include": true, "label": "Field notes"}
}

// Only persistence:
"meta": {
  "persistent": true
}

// Multiple properties:
"meta": {
  "annotation": {"include": true, "label": "Comments"},
  "persistent": true
}
```

### Data Storage

#### Database Storage
Meta properties create parallel data structures:
```json
{
  "field-name": "actual value",
  "field-name_annotation": "annotation text",
  "field-name_uncertainty": true/false
}
```

#### CSV Export
Each meta property creates additional columns:
- Main field: `field-name`
- Annotation: `field-name_annotation`
- Uncertainty: `field-name_uncertainty`

#### JSON Export
Preserves full structure with meta values inline.

### Common Patterns

#### Field with Full Meta
```json
{
  "species-identification": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Species",
      "ElementProps": {"options": [...]}
    },
    "meta": {
      "annotation": {"include": true, "label": "Identification notes"},
      "uncertainty": {"include": true, "label": "Tentative ID"},
      "persistent": false
    }
  }
}
```

#### Persistent Configuration Fields
```json
{
  "team-member": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Recording Team Member",
      "ElementProps": {"options": [...]}
    },
    "meta": {
      "persistent": true  // Keeps value for next record
    }
  }
}
```

#### Measurement with Uncertainty
```json
{
  "artifact-length": {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Number",
    "component-parameters": {
      "label": "Length (mm)"
    },
    "meta": {
      "uncertainty": {"include": true, "label": "Approximate"},
      "annotation": {"include": true, "label": "Measurement notes"}
    }
  }
}
```

### Field Type Compatibility

Meta properties work with ALL field types:
- ✅ Text fields (all variants)
- ✅ Number fields (all variants)
- ✅ DateTime fields (all variants)
- ✅ Selection fields (all variants)
- ✅ Media fields (all variants)
- ✅ Location fields (all variants)
- ✅ Relationship fields

### Display Behavior

#### Annotation Field Placement
- Usually appears below main field
- Full width of container
- Multi-line text input
- No character counter
- No validation indicators

#### Uncertainty Checkbox Placement
- Typically right-aligned
- Same row as field label (desktop)
- Below field (mobile)
- May show warning icon when checked

### Performance Considerations

- Meta properties have minimal performance impact
- Annotation fields add ~2KB per field to payload
- Uncertainty adds ~10 bytes per field
- Persistent fields require state management overhead
- No impact on validation performance

### Best Practices

#### When to Use Annotations
- Fields requiring explanation
- Subjective observations
- Exceptional cases
- Quality notes
- Method descriptions

#### When to Use Uncertainty
- Estimated measurements
- Tentative identifications
- Incomplete data
- Conflicting information
- Low-confidence observations

#### When to Use Persistent
- Site/context that continues across records
- Team members recording multiple items
- Date when recording in single session
- Equipment/method that remains constant

#### When NOT to Use Persistent
- Unique identifiers
- Measurements that vary
- Observations that change
- Auto-generated values
- Photos/media

### Common Issues

#### Annotation Text Lost
- **Cause**: Field name changed
- **Fix**: Annotation stored with field name key

#### Uncertainty Not Showing
- **Cause**: Missing include property
- **Fix**: Set `"include": true`

#### Persistent Not Working
- **Cause**: Form reset between records
- **Fix**: Check form submission mode

#### Labels Not Updating
- **Cause**: Designer overwrites on save
- **Fix**: Edit JSON after Designer save

### Migration Notes

#### From Older Versions
- v1-v2: `annotation: true` → `annotation: {"include": true}`
- v2-v3: No changes to meta structure

#### Designer Round-Trip
Designer preserves JSON meta properties it doesn't understand, but:
- Resets custom labels to defaults
- Ignores persistent/displayParent
- May reorder properties

## Formik Integration {comprehensive}

### Overview {essential}

Fieldmark v3 uses Formik as its form state management library. Understanding how fields integrate with Formik is essential for troubleshooting validation issues, implementing custom fields, and optimizing form performance.

### Component Categories by Formik Integration

#### Formik-Wrapped Components (`formik-material-ui`)
These components have built-in Formik integration via the `useField` hook:
- **TextField**: Base text input (used for Email)
- **MultipleTextField**: Multi-line text area
- **Deprecated Number Field**: Uses TextField with type="number"

These components automatically:
- Connect to Formik's form state
- Handle value updates through `field.onChange`
- Manage blur events via `field.onBlur`
- Display validation errors from `meta.error`
- Track touched state via `meta.touched`

#### Custom Components (`faims-custom`)
These components implement their own Formik integration:
- All selection fields (Checkbox, RadioGroup, Select, MultiSelect, AdvancedSelect)
- All datetime fields (DateTimeNow, DateTimePicker, DatePicker, MonthPicker)
- All number fields (NumberField, ControlledNumber, BasicAutoIncrementer)
- Enhanced text fields (FAIMSTextField, TemplatedStringField, AddressField)
- Display components (RichText)

Custom components must manually:
- Call `setFieldValue` to update form state
- Call `setFieldTouched` to mark fields as interacted
- Read validation state from Formik context
- Implement error display logic

#### Special Cases
- **QRCodeFormField** (`qrcode` namespace): Implements partial Formik integration
- **RichText**: No Formik integration (display only, no data binding)

### Validation Lifecycle

#### 1. Mount Phase
When a field component mounts:
```javascript
// Formik initializes field with:
- value: initialValue from field config
- touched: false
- error: undefined (even if validation would fail)
```

**Important**: Validation runs on mount but errors are hidden until the field is touched. This prevents showing errors for empty required fields on initial form load.

#### 2. Change Event
When user modifies field value:
```javascript
// Component calls:
setFieldValue(fieldName, newValue)
// This triggers:
1. Value update in Formik state
2. Field marked as touched
3. Validation schema execution
4. Error state update if validation fails
```

**Field Type Variations**:
- **Text fields**: Validate on every keystroke
- **Selection fields**: Validate on selection change
- **Number fields**: Validate after parsing attempt
- **Date fields**: Validate after date parsing

#### 3. Blur Event
When user leaves field (focus lost):
```javascript
// Component calls:
setFieldTouched(fieldName, true)
// This triggers:
1. Touched state set to true
2. Re-validation of field
3. Error display if validation fails
```

**Critical**: Fields must be "touched" for errors to display. Common issue: users submit forms without touching required fields, causing silent validation failures.

#### 4. Submit Phase
When form is submitted:
```javascript
// Formik automatically:
1. Marks all fields as touched
2. Runs all validation schemas
3. Displays all errors
4. Prevents submission if any validation fails
```

### Formik State Structure

Each field maintains this state in Formik:

```javascript
{
  values: {
    fieldName: currentValue  // The field's current value
  },
  errors: {
    fieldName: errorMessage  // Validation error message (if any)
  },
  touched: {
    fieldName: boolean       // Whether user has interacted with field
  }
}
```

### Validation Schema Integration

Formik validates using Yup schemas defined in field configuration:

```javascript
validationSchema: [
  ["yup.string"],           // Type validation
  ["yup.required"],         // Required validation
  ["yup.min", 5],          // Minimum length
  ["yup.matches", regex]    // Pattern validation
]
```

**Execution Order**:
1. Type validation first (string, number, bool, etc.)
2. Then constraint validations in array order
3. First failure stops validation chain
4. Error message from failed validation displayed

### Common Formik Integration Issues

#### Issue: Field Not Showing Errors
**Cause**: Field not marked as touched
**Solution**: Ensure field blur event calls `setFieldTouched`
**User Workaround**: Click field then click away to trigger touched state

#### Issue: Validation Not Running
**Cause**: Component not calling Formik handlers
**Solution**: Verify `setFieldValue` called on changes
**Debug**: Check Formik state in React DevTools

#### Issue: Stale Values in Dependent Fields
**Cause**: Async validation or state updates
**Solution**: Use Formik's `validateField` after dependent updates
**Pattern**:
```javascript
await setFieldValue('field1', value)
await validateField('dependentField')
```

#### Issue: Submit Without Validation
**Cause**: Custom submit handler bypassing Formik
**Solution**: Use Formik's `handleSubmit` or `submitForm`
**Never**: Directly access values without validation

### Performance Considerations

#### Validation Debouncing
For fields with expensive validation:
```javascript
// Problem: Validation runs on every keystroke
validationSchema: [["yup.test", expensiveValidation]]

// Solution: Debounce validation
const debouncedValidation = debounce(expensiveValidation, 300)
validationSchema: [["yup.test", debouncedValidation]]
```

#### Field Arrays and Dynamic Forms
When using field arrays:
- Each array item maintains separate Formik state
- Validation runs for entire array on any change
- Consider pagination for large arrays (>50 items)

#### Conditional Fields
Hidden fields still maintain Formik state:
- Values persist when fields are hidden
- Validation still runs on hidden fields
- Use `when` conditions in Yup for conditional validation

### Field-Specific Formik Behaviors

#### Text Fields {#text-field-formik}
- **TextField/MultipleTextField**: Native Formik integration
- **FAIMSTextField**: Custom integration with enhanced features
- **TemplatedString**: Updates when dependencies change
- **Address**: Complex object value requires special handling

#### Number Fields {#number-field-formik}
- **Dual validation**: HTML5 + Yup validation
- **Parse on every keystroke**: May cause validation noise
- **Null vs empty**: Different handling between field types

#### DateTime Fields {#datetime-field-formik}
- **Format parsing**: Multiple attempts on each change
- **Picker events**: May bypass normal change flow
- **Timezone handling**: Affects value comparison

#### Selection Fields {#selection-field-formik}
- **Binary state**: No partial validation states
- **Array values**: MultiSelect requires array handling
- **Empty state**: Difficult to detect unselected state

### Custom Field Implementation

When creating custom fields that integrate with Formik:

```javascript
import { useField } from 'formik';

function CustomField({ name, ...props }) {
  // Hook into Formik
  const [field, meta, helpers] = useField(name);
  
  return (
    <div>
      <input
        {...field}
        {...props}
        onChange={(e) => {
          // Custom logic here
          helpers.setValue(e.target.value);
        }}
        onBlur={() => {
          helpers.setTouched(true);
        }}
      />
      {meta.touched && meta.error && (
        <div className="error">{meta.error}</div>
      )}
    </div>
  );
}
```

### Debugging Formik Integration

#### Check Formik State
```javascript
// In browser console with React DevTools:
$r.props.formik.values     // Current values
$r.props.formik.errors     // Current errors
$r.props.formik.touched    // Touched fields
```

#### Monitor State Changes
```javascript
// Add to form component:
useEffect(() => {
  console.log('Formik state:', formik.values);
}, [formik.values]);
```

#### Validation Debugging
```javascript
// Test validation schema:
const schema = yup.string().required();
schema.validateSync(value);  // See validation result
```

### Best Practices

1. **Always handle touched state**: Fields must be marked touched for UX
2. **Validate on blur minimum**: Provides feedback after interaction
3. **Debounce expensive validation**: Prevent performance issues
4. **Clear error display**: Ensure errors are visible and clear
5. **Test validation flow**: Verify mount → change → blur → submit cycle
6. **Handle async validation**: Use proper Promise handling
7. **Document validation rules**: Help users understand requirements

### Formik Configuration in Notebooks

Notebooks configure Formik behavior at the form level:

```json
{
  "forms": {
    "formName": {
      "views": { ... },
      "sections": { ... },
      // Formik configuration happens implicitly through field definitions
    }
  }
}
```

Field-level Formik configuration:
```json
{
  "fieldName": {
    "initialValue": "",           // Formik initial value
    "validationSchema": [...],    // Yup validation rules
    "component-parameters": {
      // Component-specific Formik integration
    }
  }
}
```

### Troubleshooting Checklist

When fields aren't behaving correctly with Formik:

- [ ] Field value updates in Formik state on change
- [ ] Field marked as touched on blur
- [ ] Validation errors appear after touch
- [ ] Submit triggers validation for all fields
- [ ] Conditional fields validate correctly
- [ ] Dependent fields update when triggers change
- [ ] Error messages display to users
- [ ] Required fields prevent submission
- [ ] Initial values set correctly
- [ ] Field resets work properly

## Error Prevention Checklist {important}

### Namespace Configuration
- [ ] Namespace is exactly `faims-custom` or `formik-material-ui`
- [ ] Component name matches reference table exactly
- [ ] Case sensitivity verified (PascalCase for components)
- [ ] No typos in namespace (hyphen not underscore)
- [ ] Namespace specified for every field
- [ ] Designer name not used in JSON

### Type System
- [ ] Type-returned specified for all fields
- [ ] Types match expected component output
- [ ] No invalid/deprecated types used
- [ ] Export format considered in type selection
- [ ] Type conversions documented

### Meta Properties
- [ ] Meta properties structure valid
- [ ] Custom labels specified where needed
- [ ] Persistent fields identified correctly
- [ ] Annotation/uncertainty used appropriately
- [ ] Data storage implications understood

### Formik Integration
- [ ] Field updates trigger Formik state changes
- [ ] Touched state managed correctly
- [ ] Validation errors display appropriately
- [ ] Submit behavior validated
- [ ] Performance optimizations applied where needed

## Performance Optimization Guidelines {comprehensive}

### Component Selection
- Prefer primitive types when possible
- Use most specific component for use case
- Consider platform-specific performance
- Test with expected data volumes

### Validation Performance
- Debounce expensive validations
- Minimize complex conditional logic
- Cache computed values
- Batch validation operations

### State Management
- Limit persistent fields to necessary cases
- Avoid deep object nesting in JSON types
- Minimize array field sizes
- Consider form splitting for large datasets

## Migration and Maintenance {comprehensive}

### Namespace Evolution
- **v1-v2**: Mixed namespaces (`material-ui`, `formik-material-ui`, custom components)
- **v3**: Standardized on `faims-custom` for most components
- **Current**: Two namespaces only (`faims-custom` and `formik-material-ui`)

### Migration from Older Notebooks
- `material-ui` → `formik-material-ui` (for TextField only)
- `faims-custom-ui` → `faims-custom`
- Custom component names → Check current list
- `annotation: true` → `annotation: {"include": true}`

### Type System Migration
When migrating between field types:
- **String → Number**: Parse errors possible
- **Single → Array**: Wrap in array
- **Array → Single**: Data loss warning
- **JSON → String**: Stringify required

### Designer Round-Trip Considerations
Designer preserves JSON properties it doesn't understand, but:
- Resets custom meta labels to defaults
- Ignores persistent/displayParent properties
- May reorder properties
- Always uses correct namespaces

## Platform-Specific Notes {comprehensive}

### Web/Desktop
- All namespaces work identically
- No platform-specific namespace requirements
- Full Formik debugging available in DevTools

### iOS/Android  
- Same namespace requirements
- Native components still use faims-custom namespace
- No special mobile namespaces
- Limited debugging capabilities

### PWA
- Identical namespace behavior
- Offline capability doesn't affect namespaces
- Formik state persists across offline/online transitions

## Best Practices Summary {comprehensive}

### DO:
✅ Always specify namespace explicitly  
✅ Use exact component names from reference  
✅ Specify type-returned for all fields  
✅ Test Formik integration thoroughly  
✅ Use meta properties for field enhancement  
✅ Document type assumptions and conversions  
✅ Validate early and often  
✅ Consider export requirements in type selection  

### DON'T:
❌ Omit namespace even if it seems to work  
❌ Type component names manually  
❌ Use deprecated or invalid types  
❌ Bypass Formik validation on submit  
❌ Overuse persistent fields  
❌ Ignore platform differences  
❌ Mix namespace formats  
❌ Forget case sensitivity  

## Common Patterns and Examples {comprehensive}

### Standard Field Definition
```json
{
  "field-name": {
    "component-namespace": "faims-custom",
    "component-name": "ComponentName",
    "type-returned": "faims-core::Type",
    "component-parameters": {
      // parameters
    },
    "validationSchema": [
      // validation rules
    ],
    "initialValue": "",
    "meta": {
      // meta properties
    }
  }
}
```

### When to Use formik-material-ui
Only for these specific cases:
- Basic single-line text input without special features
- Multi-line text area without special features
- When explicitly avoiding custom validation or behavior

### Test Configuration
```json
{
  "test-field": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "name": "test-field",
      "label": "Test"
    }
  }
}
```

## Debugging Quick Reference {important}

### Quick Diagnostic Steps

1. **Check exact spelling**: `faims-custom` (all lowercase, hyphen)
2. **Verify case**: Component names use PascalCase
3. **Confirm pairing**: Component name matches namespace
4. **Test minimal**: Try simplest possible configuration
5. **Check Formik state**: Use React DevTools
6. **Verify type match**: Component output matches type-returned
7. **Test validation**: Ensure schemas execute correctly
8. **Check meta properties**: Verify structure and values

## Related Documentation {important}

- [Field Selection Guide](../patterns/field-selection-guide.md) - Choosing appropriate components
- [Dynamic Forms Guide](../patterns/dynamic-forms-guide.md) - Validation and conditional logic
- [Form Structure Guide](../patterns/form-structure-guide.md) - Form architecture patterns
- [Implementation Patterns Guide](../patterns/implementation-patterns-guide.md) - Common patterns
- Individual field documentation for component-specific details

## Version Information {comprehensive}

- **Last Updated**: 2025-01-06
- **Applies to**: Fieldmark v3 (all versions)
- **Component Library**: @faims3/data-model
- **Formik Version**: 2.x (as bundled with Fieldmark)
- **Total Valid Components**: ~30
- **Valid Namespaces**: 3 (`faims-custom`, `formik-material-ui`, `mapping-plugin`)
- **Valid Types**: 8 core types

<!-- concat:boundary:end section="component-reference" -->