# Component Mapping Table: Designer to JSON

This table maps Designer UI component names to their JSON notebook equivalents. Critical for converting between Designer exports and manual JSON editing.

## Quick Reference Format
**Designer Name** → `namespace:component` (Notes)

## Text Fields

| Designer Name | JSON Namespace | JSON Component | Notes |
|--------------|----------------|----------------|-------|
| **FAIMS Text Field** | `faims-custom` | `FAIMSTextField` | Enhanced with expandable help, resizable UI |
| **Text Field** | `formik-material-ui` | `MultipleTextField` | Multi-line text area (despite name) |
| **Email** | `formik-material-ui` | `TextField` | Uses `type: "email"` in InputProps. **NO dedicated Email component exists** |
| **Templated String Field** | `faims-custom` | `TemplatedStringField` | Auto-generates from template, usually hidden |
| **Scan QR Code** | `qrcode` | `QRCodeFormField` | QR code scanner |
| **Address** | `faims-custom` | `AddressField` | Structured address input |

## Date/Time Fields

| Designer Name | JSON Namespace | JSON Component | Notes |
|--------------|----------------|----------------|-------|
| **Date and Time with Now button** | `faims-custom` | `DateTimeNow` | ⚠️ **NEVER** use `faims3` namespace |
| **Date time picker** | `faims-custom` | `DateTimePicker` | **DISCOURAGED** - use DateTimeNow instead |
| **Date picker** | `faims-custom` | `DatePicker` | Date only, no time |
| **Month picker** | `faims-custom` | `MonthPicker` | Month and year only |

## Number Fields

| Designer Name | JSON Namespace | JSON Component | Notes |
|--------------|----------------|----------------|-------|
| **Number Input** | `faims-custom` | `NumberField` | Floating-point numbers |
| **Number field** | `formik-material-ui` | `TextField` | Uses `type: "number"` in InputProps |
| **Controlled number** | `formik-material-ui` | `TextField` | ⚠️ **Designer abstraction only** - maps to TextField with validation |
| **Auto Incrementing Field** | `faims-custom` | `BasicAutoIncrementer` | Sequential ID generation |

## Selection/Choice Fields

| Designer Name | JSON Namespace | JSON Component | Notes |
|--------------|----------------|----------------|-------|
| **Select Field** | `faims-custom` | `Select` | Single selection dropdown |
| **Select Field (Hierarchical)** | `faims-custom` | `AdvancedSelect` | Nested/hierarchical options |
| **Select Multiple** | `faims-custom` | `MultiSelect` | Multiple selection dropdown |
| **Select one option** | `faims-custom` | `RadioGroup` | Radio button group |
| **Checkbox** | `faims-custom` | `Checkbox` | Boolean toggle |

## Media Fields

| Designer Name | JSON Namespace | JSON Component | Notes |
|--------------|----------------|----------------|-------|
| **Take Photo** | `faims-custom` | `TakePhoto` | Camera capture |
| **Upload a File** | `faims-custom` | `FileUploader` | File attachment |

## Location Fields

| Designer Name | JSON Namespace | JSON Component | Notes |
|--------------|----------------|----------------|-------|
| **Take point** | `faims-custom` | `TakePoint` | GPS coordinate capture |
| **Map Field** | `mapping-plugin` | `MapFormField` | Interactive map for points/lines/polygons |

## Display/Relationship Fields

| Designer Name | JSON Namespace | JSON Component | Notes |
|--------------|----------------|----------------|-------|
| **Title** | `faims-custom` | `RandomStyle` | Styled heading/HTML content |
| **RichText** | `faims-custom` | `RichText` | Formatted markdown text |
| **Add Related Record** | `faims-custom` | `RelatedRecordSelector` | Link child/related records |

## Critical Warnings

### ⚠️ Components That Don't Exist
1. **Email Component**: No `faims-custom:Email` or standalone Email component exists. Use `formik-material-ui:TextField` with `type: "email"`
2. **ControlledNumber**: Designer-only abstraction. Maps to `formik-material-ui:TextField` with Yup validation

### ⚠️ Namespace Confusion
1. **DateTimeNow**: Always use `faims-custom`, NEVER `faims3`
2. **TextField variants**: Different namespaces provide different TextField components:
   - `faims-custom:FAIMSTextField` - Enhanced FAIMS version
   - `formik-material-ui:TextField` - Standard Formik version (used for Email, Number field)
   - `core-material-ui:TextField` - Raw MUI component (rarely used directly)

### ⚠️ Misleading Names
1. **MultipleTextField**: Despite the name, this is for multi-line text (textarea), not multiple text fields
2. **Number field** vs **Number Input**: Different components in different namespaces
3. **Select Field** appears twice with different functionality (standard vs hierarchical)

## Component Parameters Reference

### Common Parameters (most components)
- `label`: Display label
- `helperText`: Help text below field
- `advancedHelperText`: Expandable help text
- `required`: Boolean for validation
- `fullWidth`: Boolean for width

### Special Parameters
- **Email**: Requires `InputProps: { type: "email" }`
- **Number fields**: Requires `InputProps: { type: "number" }`
- **MultipleTextField**: Requires `multiline: true` and `InputProps: { rows: 4 }`
- **DateTimeNow**: Has `is_auto_pick` parameter
- **BasicAutoIncrementer**: Requires `num_digits` and `form_id`

## Validation Schema Patterns

Most components follow these patterns:
- Text: `[["yup.string"]]`
- Numbers: `[["yup.number"]]` or `[["yup.number"], ["yup.nullable"]]`
- Boolean: `[["yup.bool"]]`
- Arrays: `[["yup.array"]]`
- Objects: `[["yup.object"], ["yup.nullable"]]`

## Initial Values by Type

- Text fields: `""` (empty string)
- Number fields: `null` or `""` 
- Boolean: `false`
- Arrays: `[]`
- Objects/Files: `null`

## Complete Component Registry

All components available in the codebase (some may not appear in Designer):

### faims-custom namespace (23 components)
FAIMSTextField, DateTimePicker, DatePicker, MonthPicker, DateTimeNow, BasicAutoIncrementer, Checkbox, FileUploader, MultiSelect, RadioGroup, RandomStyle, RichText, RelatedRecordSelector, Select, AdvancedSelect, TakePhoto, TakePoint, TemplatedStringField, AddressField, NumberField, ActionButton

### formik-material-ui namespace (4 components)
TextField, MultipleTextField, Select, RadioGroup

### core-material-ui namespace (3 components)
TextField, Checkbox, Input

### qrcode namespace (1 component)
QRCodeFormField

### mapping-plugin namespace (1 component)
MapFormField

---

**Last Updated**: 2025-09-01
**Source**: Extracted from `/home/shawn/Code/FAIMS3/web/src/designer/fields.tsx` and verified against component registry