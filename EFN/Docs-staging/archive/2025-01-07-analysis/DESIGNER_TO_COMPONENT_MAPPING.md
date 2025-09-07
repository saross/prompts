# Designer UI Names to Component Names - Complete Mapping

## Critical Finding: Designer Names ≠ Component Names

The Designer interface uses different names than the actual component implementation. This is the source of much confusion.

## The Truth About "Controlled Number"

**ControlledNumber** in Designer is NOT a separate component. It's actually:
- Component: `TextField` (from formik-material-ui)
- With type: `number`
- With validation: min/max bounds

This explains why you correctly said "Controlled Number exists in Designer" - it does! But it's not a distinct component in the codebase.

## Complete Designer → Component Mapping

### Text Fields
| Designer Name | Component Namespace | Component Name | Type Returned |
|--------------|-------------------|----------------|---------------|
| FAIMS Text Field | faims-custom | FAIMSTextField | faims-core::String |
| Email | formik-material-ui | TextField | faims-core::Email |
| (MultilineText - if exists) | formik-material-ui | MultipleTextField | faims-core::String |

### Number Fields
| Designer Name | Component Namespace | Component Name | Type Returned | Notes |
|--------------|-------------------|----------------|---------------|--------|
| Number field | formik-material-ui | TextField | faims-core::Integer | type="number" |
| **Controlled number** | formik-material-ui | TextField | faims-core::Integer | type="number" + min/max validation |
| Basic Auto Incrementer | faims-custom | BasicAutoIncrementer | faims-core::String | Returns STRING not number! |
| Number Input | faims-custom | NumberField | faims-core::Float | The actual NumberField component |

### Date/Time Fields  
| Designer Name | Component Namespace | Component Name | Type Returned |
|--------------|-------------------|----------------|---------------|
| Date picker | faims-custom | DatePicker | faims-core::Date |
| Date time picker | faims-custom | DateTimePicker | faims-core::String |
| Month picker | faims-custom | MonthPicker | faims-core::Date |
| Date and Time with Now button | faims-custom | DateTimeNow | faims-core::String |

### Selection Fields
| Designer Name | Component Namespace | Component Name |
|--------------|-------------------|----------------|
| Select | faims-custom | Select |
| MultiSelect | faims-custom | MultiSelect |
| AdvancedSelect | faims-custom | AdvancedSelect |
| Checkbox | faims-custom | Checkbox |
| RadioGroup | faims-custom | RadioGroup |

### Media Fields
| Designer Name | Component Namespace | Component Name |
|--------------|-------------------|----------------|
| Take Photo | faims-custom | TakePhoto |
| File Upload | faims-custom | FileUploader |

### Location Fields
| Designer Name | Component Namespace | Component Name |
|--------------|-------------------|----------------|
| Take Point | faims-custom | TakePoint |
| Map Input | mapping-plugin | MapFormField |

### Special Fields
| Designer Name | Component Namespace | Component Name |
|--------------|-------------------|----------------|
| Related Record | faims-custom | RelatedRecordSelector |
| Rich Text | faims-custom | RichText |
| QR Code Scanner | qrcode | QRCodeFormField |
| Address Field | faims-custom | AddressField |
| Unique ID | faims-custom | TemplatedStringField |
| Action Button | faims-custom | ActionButton |
| Random Style | faims-custom | RandomStyle |

## Components That DON'T EXIST (Documentation Errors)

These appear in our documentation but are NOT real components:

### ❌ In number-fields-v05.md JSON examples:
- **TemplatedIntegerField** - NOT REAL (we incorrectly added in examples)
- **TemplatedFloatField** - NOT REAL (we incorrectly added in examples)
- **ControlledNumber** as a component name - It's TextField with configuration

### ❌ In datetime-fields-v05.md:
- **TimePicker** - NOT REAL (no standalone time picker exists)
- **NumberInput** - NOT REAL as component (might be TextField variant)

### ❌ Incorrect names in docs:
- **Email** as component - It's TextField with type="email"
- **MultilineText** - Should be MultipleTextField

## Why This Happened

1. **Designer Abstraction**: Designer creates user-friendly names that map to configured components
2. **Documentation Error**: When we added JSON examples, we incorrectly assumed Designer names were component names
3. **ControlledNumber Confusion**: It appears as a field type in Designer but is actually TextField with specific parameters

## Actual Component Count

### Real Components in FAIMS3:
- **core-material-ui**: 3 components (low-level)
- **faims-custom**: 21 components
- **formik-material-ui**: 4 components  
- **mapping-plugin**: 1 component
- **qrcode**: 1 component
- **TOTAL**: 30 actual components

### What Designer Shows:
Designer may show more "field types" than actual components because it creates variants through configuration (like ControlledNumber = TextField with bounds).

## Documentation Corrections Needed

### Immediate Fixes Required:

1. **number-fields-v05.md**:
   - Remove ALL TemplatedIntegerField references (6 occurrences)
   - Remove ALL TemplatedFloatField references (10 occurrences)
   - Change ControlledNumber component references to TextField with configuration
   - Clarify that "Controlled Number" in Designer creates TextField

2. **datetime-fields-v05.md**:
   - Remove TimePicker documentation (3 occurrences)
   - Remove NumberInput references (12 occurrences)

3. **text-fields-v05.md**:
   - Change Email component to TextField with type="email"
   - Change MultilineText to MultipleTextField

## The Real Number Fields Story

Based on Designer fields.tsx:

1. **"Number field"** (Designer) → TextField with type="number" (deprecated approach)
2. **"Controlled number"** (Designer) → TextField with type="number" + validation
3. **"Number Input"** (if shown) → NumberField component (the proper one)
4. **"Basic Auto Incrementer"** → BasicAutoIncrementer (returns strings!)

## Summary

- Designer shows ~35-40 "field types"
- These map to only 30 actual components
- Some Designer fields are just configurations of TextField
- We incorrectly documented these configurations as separate components
- ControlledNumber EXISTS in Designer but NOT as a component

---

*This mapping explains why the test notebook failed - we were using component names that don't exist!*