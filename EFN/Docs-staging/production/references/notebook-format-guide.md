# Fieldmark Notebook Format Guide

<!-- discovery:metadata
provides: [json-structure, notebook-requirements, fviews-structure, validation]
see-also: [form-structure-guide, designer-component-mapping]
-->


## Critical Structure Differences Found

### ❌ INCORRECT Structure (What we had)
```json
{
  "ui-specification": {
    "viewsets": {
      "main": {
        "views": {
          "view1": {
            "label": "Test View",
            "fields": ["field1", "field2"]
          }
        }
      }
    }
  }
}
```

### ✅ CORRECT Structure (What Designer expects)
```json
{
  "ui-specification": {
    "fviews": {
      "view1": {
        "fields": ["field1", "field2"],
        "label": "Test View",
        "uidesign": "form"
      }
    },
    "viewsets": {
      "main": {
        "views": ["view1"],  // Array of view names, not objects
        "label": "Main Form",
        "publishButtonBehaviour": "always"
      }
    }
  }
}
```

## Key Requirements for Working Notebooks

### 1. Metadata Section
Must include these fields:
```json
"metadata": {
  "notebook_version": "1.0",
  "schema_version": "1.0",
  "name": "Notebook Name",
  "accesses": ["admin", "moderator", "team"],
  "ispublic": false,
  "isrequest": false,
  "lead_institution": "Institution Name",
  "project_lead": "Lead Name",
  "project_status": "New",
  "pre_description": "Description",
  "showQRCodeButton": false
}
```

### 2. Field Structure
Each field MUST have:
- `component-namespace`: Correct namespace for component
- `component-name`: Valid component name
- `type-returned`: Return type (e.g., "faims-core::String")
- `component-parameters`: Must include `name` field matching field ID
- `validationSchema`: Array format like `[["yup.string"]]`
- `initialValue`: Default value (empty string, array, or false)
- `meta`: Annotation and uncertainty settings

### 3. Three-Level View Hierarchy
1. **Fields** → Individual field definitions
2. **fviews** → Form views that group fields
3. **viewsets** → Collections of views

The viewsets reference fviews by name (string array), NOT as nested objects.

### 4. Component-Specific Parameters

#### TextField (formik-material-ui)
```json
"component-parameters": {
  "label": "Field Label",
  "fullWidth": true,
  "helperText": "Help text",
  "variant": "outlined",
  "required": false,
  "name": "field-name"
}
```

#### NumberField (faims-custom)
```json
"component-parameters": {
  "label": "Number Field",
  "fullWidth": true,
  "helperText": "Enter number",
  "variant": "outlined",
  "name": "field-name"
}
```

#### Controlled Number (TextField with type="number")
```json
"component-namespace": "formik-material-ui",
"component-name": "TextField",
"component-parameters": {
  "label": "Controlled Number",
  "name": "field-name",
  "InputProps": {
    "type": "number"
  }
},
"validationSchema": [
  ["yup.number"],
  ["yup.min", 0, "Must be at least 0"],
  ["yup.max", 100, "Must be at most 100"]
]
```

#### Select (faims-custom)
```json
"component-parameters": {
  "label": "Select Field",
  "name": "field-name",
  "ElementProps": {
    "options": [
      {"value": "val1", "label": "Label 1"},
      {"value": "val2", "label": "Label 2"}
    ]
  }
}
```

## Common Errors and Solutions

### Error: "Sorry, something went wrong"
**Causes:**
1. Missing `fviews` section
2. Viewsets referencing views as objects instead of string array
3. Missing required metadata fields
4. Missing `name` parameter in component-parameters

### Error: Component not found
**Causes:**
1. Using non-existent components (e.g., ControlledNumber, TimePicker)
2. Wrong namespace for component
3. Incorrect component name capitalization

## Testing Files Created

1. **test-notebook-correct.json** - Minimal working notebook with correct structure
2. **test-notebook-comprehensive.json** - All basic field types with correct format

## Validation Checklist

- [ ] All fields have `name` in component-parameters
- [ ] Uses `fviews` not just viewsets
- [ ] Viewsets reference views as string array
- [ ] All components exist in actual registry
- [ ] Correct namespaces for each component
- [ ] Meta section included for all fields
- [ ] InitialValue set for all fields
- [ ] ValidationSchema in correct array format

## Component Registry Reference

See: [Designer UI to Component Mapping Reference](./references/designer-component-mapping.md)

---

*Guide Created: 2025-01-07*
*Based on analysis of working FAIMS3 notebooks*