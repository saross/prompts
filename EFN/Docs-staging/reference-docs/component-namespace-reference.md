# Component Namespace Reference
## Critical Configuration for All Fieldmark v3 Components

### Quick Reference Table

| Component Category | Namespace | Components |
|-------------------|-----------|------------|
| **Text Fields** | `formik-material-ui` | TextField, MultipleTextField |
| **Custom Text** | `faims-custom` | SingleLineTextField, TemplatedStringField, Address, QRCodeFormField |
| **Number Fields** | `faims-custom` | NumberField, BasicAutoIncrementer |
| **DateTime Fields** | `faims-custom` | DateTime, DateTimeNow |
| **Selection Fields** | `faims-custom` | Checkbox, MultiSelect, RadioGroup, Select, AdvancedSelect |
| **Media Fields** | `faims-custom` | TakePhoto, FileUploader |
| **Location Fields** | `faims-custom` | MapFormField, TakePoint |
| **Relationship** | `faims-custom` | RelatedRecordSelector |

### The Golden Rule

**When in doubt, use `faims-custom`**

Over 90% of Fieldmark components use the `faims-custom` namespace. Only basic text fields use `formik-material-ui`.

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
- `MapFormField` - Map-based location selection
- `TakePoint` - GPS coordinate capture

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
| "Map Location" | `MapFormField` | `faims-custom` |

### Namespace Evolution

#### Historical Context
- **v1-v2**: Mixed namespaces (`material-ui`, `formik-material-ui`, custom components)
- **v3**: Standardized on `faims-custom` for most components
- **Current**: Two namespaces only (`faims-custom` and `formik-material-ui`)

#### Migration Notes
If migrating from older notebooks:
- `material-ui` → `formik-material-ui` (for TextField only)
- `faims-custom-ui` → `faims-custom`
- Custom component names → Check current list

### Debugging Namespace Issues

#### Quick Diagnostic Steps

1. **Check exact spelling**: `faims-custom` (all lowercase, hyphen)
2. **Verify case**: Component names use PascalCase
3. **Confirm pairing**: Component name matches namespace
4. **Test minimal**: Try simplest possible configuration

#### Test Configuration
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

### Platform-Specific Notes

#### Web/Desktop
- All namespaces work identically
- No platform-specific namespace requirements

#### iOS/Android  
- Same namespace requirements
- Native components still use faims-custom namespace
- No special mobile namespaces

#### PWA
- Identical namespace behavior
- Offline capability doesn't affect namespaces

### Best Practices

1. **Always specify namespace** - Never omit even if it seems to work
2. **Copy exact names** - Don't type manually, copy from reference
3. **Use consistent format** - All fields in a form should follow same pattern
4. **Check Designer output** - Designer always uses correct namespace
5. **Validate early** - Test one field before building entire form

### Common Patterns

#### Standard Field Definition
```json
{
  "field-name": {
    "component-namespace": "faims-custom",
    "component-name": "ComponentName",
    "type-returned": "faims-core::Type",
    "component-parameters": {
      // parameters
    }
  }
}
```

#### When to Use formik-material-ui
Only for these specific cases:
- Basic single-line text input without special features
- Multi-line text area without special features
- When explicitly avoiding custom validation or behavior

### Error Prevention Checklist

- [ ] Namespace is exactly `faims-custom` or `formik-material-ui`
- [ ] Component name matches reference table exactly
- [ ] Case sensitivity verified (PascalCase for components)
- [ ] No typos in namespace (hyphen not underscore)
- [ ] Namespace specified for every field
- [ ] Designer name not used in JSON

### Related Documentation

- Individual field references for component parameters
- Type-returned reference for data types
- Validation reference for validation schemas
- Designer documentation for UI mapping

### Version
Last updated: 2025-09-03
Applies to: Fieldmark v3 (all versions)
Component library: @faims3/data-model