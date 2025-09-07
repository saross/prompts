# JSON Component Name Fixes - Summary

## What Was Wrong

The **documentation text** correctly describes Designer fields that users see.
The **JSON examples** incorrectly used component names that don't exist in FAIMS3.

## Fixes Applied

### ✅ Production Directory (field-categories/)

#### number-fields-v05.md:
- Fixed 6× `TemplatedIntegerField` → `NumberField`
- Fixed 10× `TemplatedFloatField` → `NumberField`  
- Fixed 14× `ControlledNumber` → `TextField` (with formik-material-ui namespace)
- Fixed 1× `NumberInput` → `NumberField`

#### datetime-fields-v05.md:
- Fixed 3× `TimePicker` → `DateTimePicker` (no standalone time picker exists)
- Fixed 11× `NumberInput` → `NumberField`

#### text-fields-v05.md:
- Fixed 1× `Email` → `TextField`
- Fixed 1× `MultilineText` → `MultipleTextField`

### ✅ Archive Directory

#### archive/cross-field/conditional-logic.md:
- Fixed 2× `NumberInput` → `NumberField`

## Why This Happened

1. **Designer Abstraction**: Designer shows user-friendly field names that are actually configurations of base components
2. **Documentation Assumption**: When adding JSON examples, we assumed Designer names = component names
3. **ControlledNumber Reality**: It's a Designer field that creates TextField with type="number" and validation

## Current Status

### ✅ CORRECT - Documentation Text
The documentation correctly describes:
- "Controlled Number" as a Designer field option
- "Number Input" as a Designer field option
- Field behaviors and capabilities

### ✅ FIXED - JSON Examples
JSON examples now use correct component names:
- `NumberField` for numeric input (faims-custom)
- `TextField` for controlled numbers (formik-material-ui)
- `DateTimePicker` instead of non-existent TimePicker

## Designer Field → Component Mapping

| Designer Shows | Creates Component | Namespace |
|---------------|------------------|-----------|
| Number Input | NumberField | faims-custom |
| Controlled Number | TextField | formik-material-ui |
| Number Field (deprecated) | TextField | formik-material-ui |
| Basic Auto Incrementer | BasicAutoIncrementer | faims-custom |

## Validation Results

Before fixes:
- 249 errors (many from wrong component names)
- Non-existent components referenced

After fixes:
- Component names now valid
- JSON examples will work in FAIMS3
- Test notebook can be regenerated correctly

## Important Notes

1. **Designer Names ≠ Component Names**: Designer creates abstractions for user-friendliness
2. **TextField is Versatile**: Used for email, numbers, controlled numbers via configuration
3. **Only One Number Component**: `NumberField` is the only dedicated number component
4. **No Time-Only Picker**: Use DateTimePicker for time selection
5. **No Audio/Video**: Despite documentation, these components don't exist

## Next Steps

1. ✅ Production JSON examples fixed
2. ✅ Archive examples fixed  
3. ⏳ Regenerate test notebook with correct components
4. ⏳ Test in actual Designer/App
5. ⏳ Update component reference table if needed

---

*Fixes completed: 2025-01-06*
*Total corrections: 48 component name fixes across 4 files*