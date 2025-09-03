# Formik Integration Reference
## How Fieldmark v3 Fields Integrate with Formik

### Overview

Fieldmark v3 uses Formik as its form state management library. Understanding how fields integrate with Formik is essential for troubleshooting validation issues, implementing custom fields, and optimizing form performance. This document consolidates the universal Formik behaviors that apply to all field types.

### Component Namespaces and Formik

Fieldmark components fall into two main categories regarding Formik integration:

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

#### Text Fields
- **TextField/MultipleTextField**: Native Formik integration
- **FAIMSTextField**: Custom integration with enhanced features
- **TemplatedString**: Updates when dependencies change
- **Address**: Complex object value requires special handling

#### Number Fields
- **Dual validation**: HTML5 + Yup validation
- **Parse on every keystroke**: May cause validation noise
- **Null vs empty**: Different handling between field types

#### DateTime Fields
- **Format parsing**: Multiple attempts on each change
- **Picker events**: May bypass normal change flow
- **Timezone handling**: Affects value comparison

#### Selection Fields
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

### Related Documentation
- [Validation Timing Reference](validation-timing-reference.md) for detailed timing behavior
- [Component Namespace Reference](component-namespace-reference.md) for component types
- Individual field documentation for field-specific behaviors
- Designer documentation for configuration interface

### Version
Last updated: 2025-09-03
Applies to: Fieldmark v3 (all versions)
Formik version: 2.x (as bundled with Fieldmark)