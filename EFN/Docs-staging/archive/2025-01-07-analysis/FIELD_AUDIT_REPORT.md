# Field Documentation Audit Report

## Executive Summary
Critical discrepancies found between documented components and actual FAIMS3 implementation.

## Components That DON'T EXIST in FAIMS3 (but are documented)

### ❌ Imaginary Components (need removal from docs):
1. **TemplatedIntegerField** (6 occurrences in docs) - DOES NOT EXIST
2. **TemplatedFloatField** (10 occurrences) - DOES NOT EXIST  
3. **ControlledNumber** (14 occurrences) - DOES NOT EXIST
4. **TimePicker** (3 occurrences) - DOES NOT EXIST
5. **NumberInput** (12 occurrences) - DOES NOT EXIST
6. **Email** (1 occurrence) - DOES NOT EXIST as component
7. **MultilineText** (1 occurrence) - DOES NOT EXIST
8. **TemplatedString** (2 occurrences) - Should be `TemplatedStringField`

### ⚠️ Incorrect Component Names in Docs:
- `MultilineTextField` (2 occurrences) - Should be `MultipleTextField`
- `TemplatedString` - Should be `TemplatedStringField`

## Components That EXIST but may be misdocumented

### ✅ Valid Components by Namespace:

#### formik-material-ui (4 components):
- TextField ✅ (48 occurrences - correctly documented)
- Select ✅ (exists but mostly using faims-custom version)
- RadioGroup ✅ (exists but mostly using faims-custom version)
- MultipleTextField ✅ (9 occurrences - correct)

#### faims-custom (21 components):
- ActionButton ✅ (NOT documented - needs addition)
- AddressField ✅ (6 occurrences)
- AdvancedSelect ✅ (5 occurrences)
- BasicAutoIncrementer ✅ (19 occurrences)
- Checkbox ✅ (14 occurrences)
- DatePicker ✅ (22 occurrences)
- DateTimeNow ✅ (19 occurrences)
- DateTimePicker ✅ (12 occurrences)
- FAIMSTextField ✅ (4 occurrences)
- FileUploader ✅ (15 occurrences)
- MonthPicker ✅ (5 occurrences)
- MultiSelect ✅ (18 occurrences)
- NumberField ✅ (31 occurrences)
- RadioGroup ✅ (13 occurrences)
- RandomStyle ✅ (NOT documented - needs addition)
- RelatedRecordSelector ✅ (22 occurrences)
- RichText ✅ (25 occurrences)
- Select ✅ (32 occurrences)
- TakePhoto ✅ (14 occurrences)
- TakePoint ✅ (11 occurrences)
- TemplatedStringField ✅ (17 occurrences)

#### mapping-plugin (1 component):
- MapFormField ✅ (11 occurrences)

#### qrcode (1 component):
- QRCodeFormField ✅ (8 occurrences)

#### core-material-ui (3 components):
- Input (NOT documented - low level component)
- Checkbox (NOT documented - low level)
- TextField (NOT documented - low level)

## Number Fields Analysis

### What Actually Exists:
- **NumberField** - The ONLY number input component in FAIMS3

### What's Documented But Doesn't Exist:
- TemplatedIntegerField ❌
- TemplatedFloatField ❌
- ControlledNumber ❌
- NumberInput ❌

### Designer UI vs Component Names:
You mentioned "Controlled Number" exists in Designer. This needs investigation:
1. It might map to `NumberField` with specific parameters
2. Or it could be a Designer-only wrapper around NumberField
3. Need to check Designer UI code to confirm

## Date/Time Fields Analysis

### What Actually Exists:
- DatePicker ✅
- DateTimePicker ✅
- DateTimeNow ✅
- MonthPicker ✅

### What Doesn't Exist:
- TimePicker ❌ (no standalone time picker)

## Files Where Imaginary Components Appear

### number-fields-v05.md:
- TemplatedIntegerField (6 times)
- TemplatedFloatField (10 times)
- ControlledNumber (14 times)

### datetime-fields-v05.md:
- TimePicker (3 times)
- NumberInput (12 times) - used in workarounds

### text-fields-v05.md:
- Email (1 time) - should just be TextField with type="email"
- MultilineText (1 time) - should be MultipleTextField

## Recommendations

### Immediate Actions Required:

1. **Remove all references to non-existent components**:
   - Delete TemplatedIntegerField documentation
   - Delete TemplatedFloatField documentation
   - Delete ControlledNumber documentation
   - Delete TimePicker documentation
   - Delete NumberInput references
   - Fix Email to be TextField with type="email"
   - Fix MultilineText to MultipleTextField

2. **Update number-fields-v05.md**:
   - Document ONLY NumberField
   - Show how to achieve integer vs float via validation
   - Show how to create controlled/slider behavior via parameters

3. **Update datetime-fields-v05.md**:
   - Remove TimePicker section
   - Remove NumberInput workarounds
   - Focus on the 4 real components

4. **Add missing documentation**:
   - ActionButton component
   - RandomStyle component
   - Core UI components (if needed)

5. **Investigate Designer mappings**:
   - Check how "Controlled Number" in Designer maps to components
   - Document the Designer name → Component name mappings

## Component Count Summary

- **Total Unique Components in FAIMS3**: 30
- **Components Documented**: 32 (including non-existent ones)
- **Imaginary Components**: 8
- **Missing Documentation**: 2 (ActionButton, RandomStyle)
- **Correctly Documented**: 22

## Next Steps

1. Create a Designer UI Name → Component Name mapping table
2. Remove all imaginary component documentation
3. Update all JSON examples to use only real components
4. Test updated documentation with actual FAIMS3 system
5. Add documentation for missing components

---

*Report generated: 2025-01-06*