<\!-- DEPRECATED: This document has been consolidated into patterns/dynamic-forms-guide.md -->
<\!-- Archived: 2025-01-06 for disaster recovery only -->
<\!-- DO NOT UPDATE: Make changes to the consolidated guide instead -->


# Validation Timing Reference
## Universal Behavior for All Fieldmark v3 Fields

### Core Validation Lifecycle

All Fieldmark fields follow the same validation timing pattern, regardless of field type:

#### 1. On Mount
- **What happens**: Validation runs immediately when form loads
- **Error display**: Hidden (field remains "pristine")
- **Field state**: Untouched, even if invalid
- **Purpose**: Establishes initial validation state without alarming users

#### 2. On Change
- **What happens**: Validation runs synchronously on every value change
- **Error display**: Immediate (if component supports error display)
- **Field state**: Transitions from "pristine" to "touched"
- **Purpose**: Provides real-time feedback during data entry

#### 3. On Blur
- **What happens**: Re-validates when user leaves field
- **Error display**: Shows/updates error messages
- **Field state**: Confirms "touched" status
- **Purpose**: Final validation before moving to next field

#### 4. On Submit
- **What happens**: All fields validated regardless of touched state
- **Error display**: All errors shown, even for untouched fields
- **Field state**: All fields marked as touched
- **Purpose**: Ensures complete form validation before submission

### Platform-Specific Behaviors

#### Mobile (iOS/Android)
- **Blur delay**: May not trigger until next field receives focus
- **Virtual keyboard**: Can interfere with blur events
- **Touch vs click**: Touch events may process differently

#### Desktop (Web)
- **Standard behavior**: Blur triggers immediately on focus loss
- **Tab navigation**: Triggers blur/focus in sequence
- **Mouse clicks**: Immediate blur when clicking outside

### Field-Specific Variations

While the core timing is universal, some fields have additional considerations:

#### Text Fields
- **Keystroke validation**: Validates on every character entry
- **Performance impact**: Can cause lag with complex regex patterns
- **Debouncing**: Not implemented - every keystroke triggers validation

#### Number Fields
- **Parse on change**: Attempts to parse numeric value on each keystroke
- **Invalid character handling**: May prevent entry rather than show error
- **Format validation**: Checks decimal places, ranges continuously

#### DateTime Fields
- **Format parsing**: Complex date parsing on each change
- **Picker integration**: Native pickers may bypass change events
- **Manual entry**: Validates partial dates during typing

#### Selection Fields (Checkbox, Radio, Select, MultiSelect)
- **Immediate validation**: Selection changes trigger instant validation
- **No keystroke issues**: Binary state changes only
- **Error display limitations**: Some components cannot display errors

#### Media Fields
- **Async validation**: File uploads validate after upload completes
- **Size checks**: Pre-upload validation for file size
- **Type validation**: MIME type checked before processing

### Error Display Capabilities by Component

| Field Type | Shows Errors | When Displayed | Where Displayed |
|------------|--------------|----------------|-----------------|
| TextField | ✅ Yes | On blur | Below field |
| NumberField | ✅ Yes | On blur | Below field |
| DateTime | ✅ Yes | On blur | Below field |
| Checkbox | ✅ Yes | On blur | Below field |
| RadioGroup | ✅ Yes | On blur | Below group |
| Select | ❌ No | Never | N/A - blocks submission |
| MultiSelect | ⚠️ Partial | On blur | Below field (limited) |
| AdvancedSelect | ❌ No | Never | N/A - blocks submission |

### State Management

#### Field States
1. **Pristine**: Never touched by user
2. **Touched**: User has interacted with field
3. **Dirty**: Value differs from initial value
4. **Valid**: Passes all validation rules
5. **Invalid**: Fails one or more validation rules

#### State Transitions
```
Mount → Pristine + (Valid|Invalid hidden)
    ↓
User Interaction → Touched + (Valid|Invalid shown)
    ↓
Value Change → Dirty + Revalidation
    ↓
Blur → Error Display Update
    ↓
Submit → All Touched + All Errors Shown
```

### Common Validation Issues

#### Race Conditions
- Rapid field navigation may skip blur events
- Async validation may complete out of order
- Submit during validation may use stale state

#### Performance Problems
- Complex regex on text fields
- Large option lists in selection fields
- Multiple dependent field validations

#### Mobile-Specific Issues
- Virtual keyboard covering error messages
- Blur events not firing between fields
- Touch targets too small for error icons

### Best Practices

#### For Developers
1. Keep validation rules simple and fast
2. Avoid complex regex patterns on text fields
3. Use type-appropriate fields (email vs text)
4. Provide clear helperText to prevent errors
5. Test on mobile devices for blur behavior

#### For Users
1. Tab through fields on desktop for best experience
2. Wait for validation to complete before submitting
3. Check for hidden errors on untouched required fields
4. Use native pickers when available (dates, times)

### Integration with Formik

All validation timing is controlled by Formik's validation strategy:

```javascript
// Formik configuration (not user-configurable)
validateOnMount: true     // Runs validation on form load
validateOnChange: true    // Validates on every field change
validateOnBlur: true      // Validates when field loses focus
```

### Validation Schema Execution Order

1. **Type validation** (yup.string, yup.number, etc.)
2. **Required validation** (yup.required)
3. **Format validation** (yup.email, yup.matches)
4. **Range validation** (yup.min, yup.max)
5. **Custom validation** (yup.test)

### Related Documentation

- Field-specific validation rules: See individual field documentation
- Validation schema syntax: See JSON Patterns Cookbook
- Error message customization: Not supported (uses Yup defaults)
- Form-level validation: See notebook-structure.md

### Version
Last updated: 2025-09-03
Applies to: Fieldmark v3 (all versions)
Component library: Formik + Material-UI + Yup