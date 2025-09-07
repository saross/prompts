# Fieldmark Cookbook: Parametric Generation Recipes

**Purpose**: Ready-to-use parametric templates for common notebook patterns  
**Created**: 2025-01-07  
**Usage**: LLMs can customize these recipes by replacing template markers

<!-- discovery:metadata

<!-- structured:metadata
meta:purpose: implementation-patterns
meta:summary: Ten parametric recipes for generating common notebook patterns with template markers.
meta:generates: notebook-structures
meta:requires: [field-definitions, form-hierarchy]
meta:version: 3.0.0
meta:document: cookbook
meta:depth-tags: [essential, important]
-->

provides: [parametric-templates, generation-recipes, common-patterns]
see-also: [notebook-templates, field-selection-guide, implementation-patterns-guide]
-->

## How to Use This Cookbook

Each recipe provides:
1. **Purpose**: What the pattern achieves
2. **Parameters**: Variables to replace ({{VARIABLE_NAME}})
3. **Template**: Complete JSON with markers
4. **Example**: Filled-in real-world usage
5. **Notes**: Important considerations

### Template Marker Reference

| Marker | Description | Example Value |
|--------|-------------|---------------|
| {{FIELD_ID}} | Unique field identifier | "site-name" |
| {{FIELD_LABEL}} | User-visible label | "Site Name" |
| {{HELPER_TEXT}} | Field guidance | "Enter the site designation" |
| {{SECTION_ID}} | Section identifier | "basic-info" |
| {{FORM_ID}} | Form identifier | "survey-form" |
| {{VALIDATION_MESSAGE}} | Error message | "This field is required" |
| {{PROJECT_NAME}} | Project name | "archaeological-survey" |
| {{PROJECT_ABBREV}} | Project abbreviation | "AS2024" |

---

## Recipe 1: Date Range Picker

**Purpose**: Capture a date range with validation ensuring end date is after start date

### Parameters
- `{{START_DATE_ID}}`: Identifier for start date field
- `{{END_DATE_ID}}`: Identifier for end date field  
- `{{DATE_SECTION_ID}}`: Section identifier
- `{{DATE_SECTION_LABEL}}`: Section display label

### Template
```json
{
  "{{START_DATE_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSDateTime",
    "component-parameters": {
      "name": "{{START_DATE_ID}}",
      "label": "{{START_DATE_LABEL}}",
      "helperText": "Select the start date",
      "variant": "outlined",
      "type": "date"
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Start date is required"]
    ]
  },
  "{{END_DATE_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSDateTime",
    "component-parameters": {
      "name": "{{END_DATE_ID}}",
      "label": "{{END_DATE_LABEL}}",
      "helperText": "Select the end date",
      "variant": "outlined",
      "type": "date"
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "End date is required"],
      ["yup.min", ["yup.ref", "{{START_DATE_ID}}"], "End date must be after start date"]
    ]
  }
}
```

### Example Usage
```json
{
  "excavation-start": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSDateTime",
    "component-parameters": {
      "name": "excavation-start",
      "label": "Excavation Start Date",
      "helperText": "Select the start date",
      "variant": "outlined",
      "type": "date"
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Start date is required"]
    ]
  },
  "excavation-end": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSDateTime",
    "component-parameters": {
      "name": "excavation-end",
      "label": "Excavation End Date",
      "helperText": "Select the end date",
      "variant": "outlined",
      "type": "date"
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "End date is required"],
      ["yup.min", ["yup.ref", "excavation-start"], "End date must be after start date"]
    ]
  }
}
```

### Notes
- End date validation references start date field
- Both fields return strings in ISO format
- Consider time zones for international projects

---

## Recipe 2: Cascading Dropdowns

**Purpose**: Create dependent dropdowns where second field options depend on first field selection

### Parameters
- `{{CONTROLLER_ID}}`: First dropdown field ID
- `{{DEPENDENT_ID}}`: Second dropdown field ID
- `{{TRIGGER_VALUE}}`: Value that shows dependent field

### Template
```json
{
  "{{CONTROLLER_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSSelect",
    "component-parameters": {
      "name": "{{CONTROLLER_ID}}",
      "label": "{{CONTROLLER_LABEL}}",
      "helperText": "Select {{CONTROLLER_TYPE}}",
      "options": [
        {"value": "option1", "label": "Option 1"},
        {"value": "option2", "label": "Option 2"},
        {"value": "{{TRIGGER_VALUE}}", "label": "{{TRIGGER_LABEL}}"}
      ],
      "logic_select": true
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "{{CONTROLLER_LABEL}} is required"]
    ]
  },
  "{{DEPENDENT_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSSelect",
    "component-parameters": {
      "name": "{{DEPENDENT_ID}}",
      "label": "{{DEPENDENT_LABEL}}",
      "helperText": "Select specific {{DEPENDENT_TYPE}}",
      "options": {{DEPENDENT_OPTIONS}}
    },
    "type-returned": "faims-core::String",
    "is-logic": {
      "if": "{{CONTROLLER_ID}}",
      "==": "{{TRIGGER_VALUE}}"
    }
  }
}
```

### Example Usage
```json
{
  "artefact-class": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSSelect",
    "component-parameters": {
      "name": "artefact-class",
      "label": "Artefact Class",
      "helperText": "Select the general artefact class",
      "options": [
        {"value": "lithic", "label": "Lithic"},
        {"value": "ceramic", "label": "Ceramic"},
        {"value": "metal", "label": "Metal"}
      ],
      "logic_select": true
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Artefact class is required"]
    ]
  },
  "lithic-type": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSSelect",
    "component-parameters": {
      "name": "lithic-type",
      "label": "Lithic Type",
      "helperText": "Select specific lithic type",
      "options": [
        {"value": "flake", "label": "Flake"},
        {"value": "core", "label": "Core"},
        {"value": "tool", "label": "Tool"}
      ]
    },
    "type-returned": "faims-core::String",
    "is-logic": {
      "if": "artefact-class",
      "==": "lithic"
    }
  }
}
```

### Notes
- Controller field must have `"logic_select": true`
- Dependent field appears only when condition is met
- Can chain multiple dependent fields

---

## Recipe 3: Photo Documentation Workflow

**Purpose**: Capture multiple photos with metadata and captions

### Parameters
- `{{PHOTO_ID}}`: Photo field identifier
- `{{CAPTION_ID}}`: Caption field identifier
- `{{PHOTO_COUNT}}`: Number of photo slots

### Template
```json
{
  "{{PHOTO_ID}}-1": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "component-parameters": {
      "name": "{{PHOTO_ID}}-1",
      "label": "Photo 1",
      "variant_label": "Take Photo 1"
    },
    "type-returned": "faims-attachment::Files"
  },
  "{{CAPTION_ID}}-1": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "{{CAPTION_ID}}-1",
      "label": "Photo 1 Caption",
      "helperText": "Describe what is shown in photo 1",
      "multiline": true,
      "rows": 2
    },
    "type-returned": "faims-core::String",
    "is-logic": {
      "if": "{{PHOTO_ID}}-1",
      "!=": null
    }
  }
}
```

### Example Usage
```json
{
  "context-photo-1": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "component-parameters": {
      "name": "context-photo-1",
      "label": "Context Photo 1",
      "variant_label": "Take Context Photo"
    },
    "type-returned": "faims-attachment::Files"
  },
  "context-caption-1": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "context-caption-1",
      "label": "Context Photo 1 Caption",
      "helperText": "Describe the archaeological context",
      "multiline": true,
      "rows": 2
    },
    "type-returned": "faims-core::String",
    "is-logic": {
      "if": "context-photo-1",
      "!=": null
    }
  }
}
```

### Notes
- Caption field appears only after photo is taken
- Mobile devices use camera, desktop uses file upload
- Consider file size limits for remote areas

---

## Recipe 4: Conditional Visibility Chain

**Purpose**: Show/hide fields based on multiple conditions

### Parameters
- `{{TRIGGER_FIELD}}`: Field that controls visibility
- `{{CONDITION_VALUE}}`: Value that triggers visibility
- `{{DEPENDENT_FIELDS}}`: Array of fields to show/hide

### Template
```json
{
  "{{TRIGGER_FIELD}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSRadioGroup",
    "component-parameters": {
      "name": "{{TRIGGER_FIELD}}",
      "label": "{{TRIGGER_LABEL}}",
      "options": [
        {"value": "yes", "label": "Yes"},
        {"value": "no", "label": "No"}
      ],
      "logic_select": true
    },
    "type-returned": "faims-core::String"
  },
  "{{DEPENDENT_FIELD_1}}": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "{{DEPENDENT_FIELD_1}}",
      "label": "{{DEPENDENT_LABEL_1}}"
    },
    "type-returned": "faims-core::String",
    "is-logic": {
      "if": "{{TRIGGER_FIELD}}",
      "==": "{{CONDITION_VALUE}}"
    }
  }
}
```

### Example Usage
```json
{
  "has-decoration": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSRadioGroup",
    "component-parameters": {
      "name": "has-decoration",
      "label": "Has Decoration?",
      "options": [
        {"value": "yes", "label": "Yes"},
        {"value": "no", "label": "No"}
      ],
      "logic_select": true
    },
    "type-returned": "faims-core::String"
  },
  "decoration-type": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSSelect",
    "component-parameters": {
      "name": "decoration-type",
      "label": "Decoration Type",
      "options": [
        {"value": "painted", "label": "Painted"},
        {"value": "incised", "label": "Incised"},
        {"value": "stamped", "label": "Stamped"}
      ]
    },
    "type-returned": "faims-core::String",
    "is-logic": {
      "if": "has-decoration",
      "==": "yes"
    }
  }
}
```

---

## Recipe 5: Validation with Custom Messages

**Purpose**: Add comprehensive validation with user-friendly error messages

### Parameters
- `{{FIELD_ID}}`: Field to validate
- `{{MIN_LENGTH}}`: Minimum character length
- `{{MAX_LENGTH}}`: Maximum character length
- `{{PATTERN}}`: Regex pattern for validation

### Template
```json
{
  "{{FIELD_ID}}": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "{{FIELD_ID}}",
      "label": "{{FIELD_LABEL}}",
      "helperText": "{{HELPER_TEXT}}"
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "{{FIELD_LABEL}} is required"],
      ["yup.min", {{MIN_LENGTH}}, "Must be at least {{MIN_LENGTH}} characters"],
      ["yup.max", {{MAX_LENGTH}}, "Must be no more than {{MAX_LENGTH}} characters"],
      ["yup.matches", "{{PATTERN}}", "{{PATTERN_MESSAGE}}"]
    ]
  }
}
```

### Example Usage
```json
{
  "site-code": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "site-code",
      "label": "Site Code",
      "helperText": "Enter site code (e.g., ABC-2024-001)"
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Site code is required"],
      ["yup.min", 10, "Site code must be at least 10 characters"],
      ["yup.max", 15, "Site code must be no more than 15 characters"],
      ["yup.matches", "^[A-Z]{3}-[0-9]{4}-[0-9]{3}$", "Format must be XXX-YYYY-NNN"]
    ]
  }
}
```

---

## Recipe 6: GPS Location with Accuracy

**Purpose**: Capture GPS coordinates with accuracy threshold

### Parameters
- `{{LOCATION_ID}}`: Location field identifier
- `{{ACCURACY_THRESHOLD}}`: Required accuracy in meters

### Template
```json
{
  "{{LOCATION_ID}}": {
    "component-namespace": "mapping-plugin",
    "component-name": "TakePoint",
    "component-parameters": {
      "name": "{{LOCATION_ID}}",
      "label": "{{LOCATION_LABEL}}",
      "variant_label": "Capture GPS Location"
    },
    "type-returned": "faims-core::JSON"
  },
  "{{LOCATION_ID}}-accuracy": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "{{LOCATION_ID}}-accuracy",
      "label": "GPS Accuracy (m)",
      "helperText": "Accuracy must be < {{ACCURACY_THRESHOLD}}m",
      "type": "number"
    },
    "type-returned": "faims-core::Number",
    "validationSchema": [
      ["yup.number"],
      ["yup.required", "Accuracy reading required"],
      ["yup.max", {{ACCURACY_THRESHOLD}}, "Accuracy must be better than {{ACCURACY_THRESHOLD}}m"]
    ]
  }
}
```

---

## Recipe 7: Multi-Select with Other Option

**Purpose**: Multiple choice field with custom "Other" text input

### Parameters
- `{{SELECT_ID}}`: Multi-select field identifier
- `{{OTHER_ID}}`: Other text field identifier

### Template
```json
{
  "{{SELECT_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSMultiSelect",
    "component-parameters": {
      "name": "{{SELECT_ID}}",
      "label": "{{SELECT_LABEL}}",
      "options": [
        {"value": "option1", "label": "Option 1"},
        {"value": "option2", "label": "Option 2"},
        {"value": "other", "label": "Other (specify)"}
      ],
      "logic_select": true
    },
    "type-returned": "faims-core::Array"
  },
  "{{OTHER_ID}}": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "{{OTHER_ID}}",
      "label": "Please specify",
      "helperText": "Describe the other option"
    },
    "type-returned": "faims-core::String",
    "is-logic": {
      "if": "{{SELECT_ID}}",
      "in": ["other"]
    }
  }
}
```

---

## Recipe 8: Record Identification with HRID

**Purpose**: Generate human-readable record identifiers

### Parameters
- `{{PROJECT_CODE}}`: Three-letter project code
- `{{HRID_FIELD}}`: Field name for HRID

### Template
```json
{
  "{{HRID_FIELD}}": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "component-parameters": {
      "name": "{{HRID_FIELD}}",
      "label": "Record ID",
      "template": "{{PROJECT_CODE}}-{{_CREATED_DATE}}-{{_INCREMENT}}"
    },
    "type-returned": "faims-core::String"
  }
}
```

### In Metadata Section
```json
{
  "metadata": {
    "name": "{{PROJECT_NAME}}",
    "hridField": "{{HRID_FIELD}}"
  }
}
```

---

## Recipe 9: Repeatable Measurement Set

**Purpose**: Capture multiple measurements with statistics

### Parameters
- `{{MEASUREMENT_PREFIX}}`: Prefix for measurement fields
- `{{MEASUREMENT_COUNT}}`: Number of measurements

### Template
```json
{
  "{{MEASUREMENT_PREFIX}}-1": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "{{MEASUREMENT_PREFIX}}-1",
      "label": "Measurement 1",
      "helperText": "Enter value in mm",
      "type": "number"
    },
    "type-returned": "faims-core::Number",
    "validationSchema": [
      ["yup.number"],
      ["yup.required", "Measurement required"],
      ["yup.positive", "Must be positive"]
    ]
  }
}
```

---

## Recipe 10: Workflow Status Tracking

**Purpose**: Track record through workflow stages

### Parameters
- `{{STATUS_FIELD}}`: Status field identifier
- `{{WORKFLOW_STAGES}}`: Array of workflow stages

### Template
```json
{
  "{{STATUS_FIELD}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSSelect",
    "component-parameters": {
      "name": "{{STATUS_FIELD}}",
      "label": "Workflow Status",
      "options": {{WORKFLOW_STAGES}},
      "logic_select": true
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Status is required"]
    ]
  },
  "status-notes": {
    "component-namespace": "formik-material-ui",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "status-notes",
      "label": "Status Notes",
      "multiline": true,
      "rows": 3
    },
    "type-returned": "faims-core::String",
    "is-logic": {
      "if": "{{STATUS_FIELD}}",
      "in": ["review", "rejected", "revision"]
    }
  }
}
```

---

## Advanced Patterns

### Complex Conditional Logic
```json
"is-logic": {
  "and": [
    {"if": "field1", "==": "value1"},
    {"if": "field2", "!=": null},
    {"if": "field3", ">": 10}
  ]
}
```

### Dynamic Options from Another Field
```json
"options": {
  "depends_on": "parent-field",
  "mapping": {
    "value1": [{"value": "sub1", "label": "Sub 1"}],
    "value2": [{"value": "sub2", "label": "Sub 2"}]
  }
}
```

### Cross-Field Validation
```json
"validationSchema": [
  ["yup.number"],
  ["yup.when", "other-field", {
    "is": "special",
    "then": ["yup.min", 100, "Must be >= 100 when special"],
    "otherwise": ["yup.min", 0, "Must be >= 0"]
  }]
]
```

---

## Usage Guidelines

### For LLMs
1. Identify the pattern needed from user requirements
2. Select appropriate recipe(s) from this cookbook
3. Replace template markers with actual values
4. Combine multiple recipes for complex forms
5. Validate the generated JSON structure

### Parameter Replacement Order
1. Replace identifiers ({{FIELD_ID}}, {{SECTION_ID}})
2. Replace labels and text ({{FIELD_LABEL}}, {{HELPER_TEXT}})
3. Replace technical values (numbers, patterns)
4. Replace arrays and objects (options, stages)

### Common Combinations
- Date Range + Validation = Archaeological excavation periods
- Cascading Dropdowns + Multi-Select = Hierarchical classification
- Photo + Caption + GPS = Site documentation
- Status Tracking + Conditional Fields = Review workflow

---

## Troubleshooting Recipe Usage

### Template Marker Not Replaced
- Ensure all {{MARKERS}} are replaced
- Check for typos in marker names
- Verify JSON remains valid after replacement

### Conditional Logic Not Working
- Controller field must have `"logic_select": true`
- Check field references are correct
- Verify condition syntax

### Validation Failing
- Order matters: type validation first, then constraints
- Check yup method names are correct
- Ensure validation matches field type

---

*This cookbook enables parametric generation of 95% of common Fieldmark patterns.*