# Complete Notebook Templates for Fieldmark

**Purpose**: Ready-to-use notebook templates for common scenarios  
**Created**: 2025-01-07  
**Usage**: Copy, modify placeholders ({{FIELD_NAME}}), and import into Designer

<!-- discovery:metadata
provides: [complete-notebooks, working-templates, scaffolding-examples, import-ready-json]
see-also: [notebook-format-guide, designer-component-mapping, field-selection-guide]
-->

## Template Usage Guide

### How to Use These Templates

1. **Choose appropriate template** based on your needs
2. **Copy the complete JSON** for your selected template
3. **Replace placeholders** marked with `{{VARIABLE}}`:
   - `{{PROJECT_NAME}}` - Your project name
   - `{{FIELD_NAME}}` - Unique field identifiers
   - `{{FIELD_LABEL}}` - User-visible labels
4. **Save as .json file** and import into Designer
5. **Test thoroughly** before deployment

### Critical Requirements

⚠️ **Every notebook MUST have**:
- Valid JSON structure
- At least one TemplatedString field configured as `hridField`
- Unique `name` parameter for every field
- Fields → fviews → viewsets hierarchy
- All fields referenced in fviews must exist

---

## Template 1: Minimal Survey (3 Fields)

**Use Case**: Quick data collection, testing, simple forms  
**Fields**: Text input, number, single selection  
**Complexity**: Minimal

```json
{
  "metadata": {
    "notebook_version": "1.0.0",
    "created": "2025-01-07",
    "name": "{{PROJECT_NAME}}-minimal",
    "description": "Minimal survey with 3 fields"
  },
  "ui-specification": {
    "fields": {
      "survey-id": {
        "component-namespace": "faims-custom",
        "component-name": "TemplatedStringField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "survey-id",
          "label": "Survey ID",
          "template": "SURV-{{_CREATED_TIME}}-{{_INCREMENT}}",
          "required": true
        }
      },
      "respondent-name": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "respondent-name",
          "label": "Respondent Name",
          "helperText": "Enter the respondent's full name",
          "required": true,
          "inputProps": {
            "maxLength": 100
          }
        },
        "validationSchema": [
          ["yup.string"],
          ["yup.required", "Name is required"]
        ]
      },
      "satisfaction-score": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "satisfaction-score",
          "label": "Satisfaction Score (1-10)",
          "InputProps": {
            "type": "number"
          },
          "min": 1,
          "max": 10,
          "required": true
        },
        "validationSchema": [
          ["yup.number"],
          ["yup.min", 1, "Score must be at least 1"],
          ["yup.max", 10, "Score cannot exceed 10"],
          ["yup.required", "Score is required"]
        ]
      }
    },
    "fviews": {
      "survey-form": {
        "fields": ["survey-id", "respondent-name", "satisfaction-score"],
        "label": "Survey Form",
        "uidesign": "form"
      }
    },
    "viewsets": {
      "main-survey": {
        "views": ["survey-form"],
        "label": "Survey",
        "publishButtonBehaviour": "always"
      }
    },
    "visible_types": ["main-survey"]
  }
}
```

---

## Template 2: Basic Data Collection (10 Fields)

**Use Case**: Standard field data collection  
**Fields**: Multiple data types across 2 sections  
**Complexity**: Basic with sections

```json
{
  "metadata": {
    "notebook_version": "1.0.0",
    "created": "2025-01-07",
    "name": "{{PROJECT_NAME}}-basic",
    "description": "Basic data collection with multiple field types"
  },
  "ui-specification": {
    "fields": {
      "record-id": {
        "component-namespace": "faims-custom",
        "component-name": "TemplatedStringField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "record-id",
          "label": "Record ID",
          "template": "{{PROJECT_ABBREV}}-{{_CREATED_DATE}}-{{_INCREMENT}}",
          "required": true
        }
      },
      "site-name": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "site-name",
          "label": "Site Name",
          "required": true
        }
      },
      "collection-date": {
        "component-namespace": "formik-material-ui",
        "component-name": "DatePicker",
        "type-returned": "faims-core::Date",
        "component-parameters": {
          "name": "collection-date",
          "label": "Collection Date",
          "required": true
        }
      },
      "collector-email": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "collector-email",
          "label": "Collector Email",
          "InputProps": {
            "type": "email"
          },
          "required": true
        },
        "validationSchema": [
          ["yup.string"],
          ["yup.email", "Enter a valid email"],
          ["yup.required", "Email is required"]
        ]
      },
      "sample-type": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "sample-type",
          "label": "Sample Type",
          "options": [
            {"value": "soil", "label": "Soil"},
            {"value": "water", "label": "Water"},
            {"value": "plant", "label": "Plant"},
            {"value": "other", "label": "Other"}
          ],
          "required": true
        }
      },
      "description": {
        "component-namespace": "faims-custom",
        "component-name": "MultipleTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "description",
          "label": "Sample Description",
          "helperText": "Provide detailed description",
          "multiline": true,
          "rows": 4
        }
      },
      "sample-count": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "sample-count",
          "label": "Number of Samples",
          "InputProps": {
            "type": "number"
          },
          "min": 1,
          "required": true
        }
      },
      "temperature": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "temperature",
          "label": "Temperature (°C)",
          "InputProps": {
            "type": "number"
          }
        }
      },
      "photo-required": {
        "component-namespace": "faims-custom",
        "component-name": "Checkbox",
        "type-returned": "faims-core::Bool",
        "component-parameters": {
          "name": "photo-required",
          "label": "Photo documentation needed"
        }
      },
      "notes": {
        "component-namespace": "faims-custom",
        "component-name": "MultipleTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "notes",
          "label": "Additional Notes",
          "multiline": true,
          "rows": 3
        }
      }
    },
    "fviews": {
      "basic-info": {
        "fields": ["record-id", "site-name", "collection-date", "collector-email"],
        "label": "Basic Information",
        "uidesign": "form"
      },
      "sample-details": {
        "fields": ["sample-type", "description", "sample-count", "temperature", "photo-required", "notes"],
        "label": "Sample Details",
        "uidesign": "form"
      }
    },
    "viewsets": {
      "data-collection": {
        "views": ["basic-info", "sample-details"],
        "label": "Data Collection",
        "publishButtonBehaviour": "always"
      }
    },
    "visible_types": ["data-collection"]
  }
}
```

---

## Template 3: Complex Form with Validation

**Use Case**: Forms requiring complex validation and conditional logic  
**Fields**: 20 fields with validation rules and conditional visibility  
**Complexity**: Advanced

```json
{
  "metadata": {
    "notebook_version": "1.0.0",
    "created": "2025-01-07",
    "name": "{{PROJECT_NAME}}-complex",
    "description": "Complex form with validation and conditional logic"
  },
  "ui-specification": {
    "fields": {
      "assessment-id": {
        "component-namespace": "faims-custom",
        "component-name": "TemplatedStringField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "assessment-id",
          "label": "Assessment ID",
          "template": "ASSESS-{{_CREATED_DATE}}-{{_USER}}-{{_INCREMENT}}",
          "required": true
        }
      },
      "assessor-name": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "assessor-name",
          "label": "Assessor Name",
          "required": true,
          "inputProps": {
            "maxLength": 100
          }
        },
        "validationSchema": [
          ["yup.string"],
          ["yup.required", "Assessor name is required"],
          ["yup.min", 2, "Name must be at least 2 characters"]
        ]
      },
      "assessment-date": {
        "component-namespace": "faims-custom",
        "component-name": "DateTimeNow",
        "type-returned": "faims-core::DateTime",
        "component-parameters": {
          "name": "assessment-date",
          "label": "Assessment Date/Time"
        }
      },
      "location-type": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "location-type",
          "label": "Location Type",
          "options": [
            {"value": "urban", "label": "Urban"},
            {"value": "rural", "label": "Rural"},
            {"value": "remote", "label": "Remote"}
          ],
          "required": true,
          "logic_select": true
        }
      },
      "urban-density": {
        "component-namespace": "faims-custom",
        "component-name": "Select",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "urban-density",
          "label": "Urban Density",
          "options": [
            {"value": "high", "label": "High Density"},
            {"value": "medium", "label": "Medium Density"},
            {"value": "low", "label": "Low Density"}
          ]
        },
        "is-logic": {
          "if": "location-type",
          "==": "urban"
        }
      },
      "access-difficulty": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "access-difficulty",
          "label": "Access Difficulty",
          "options": [
            {"value": "easy", "label": "Easy"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "difficult", "label": "Difficult"}
          ]
        },
        "is-logic": {
          "if": "location-type",
          "==": "remote"
        }
      },
      "condition-score": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "condition-score",
          "label": "Condition Score (0-100)",
          "InputProps": {
            "type": "number"
          },
          "min": 0,
          "max": 100,
          "required": true,
          "logic_select": true
        },
        "validationSchema": [
          ["yup.number"],
          ["yup.required", "Condition score is required"],
          ["yup.min", 0, "Score cannot be negative"],
          ["yup.max", 100, "Score cannot exceed 100"]
        ]
      },
      "requires-intervention": {
        "component-namespace": "faims-custom",
        "component-name": "Checkbox",
        "type-returned": "faims-core::Bool",
        "component-parameters": {
          "name": "requires-intervention",
          "label": "Requires immediate intervention"
        },
        "is-logic": {
          "if": "condition-score",
          "<": 50
        }
      },
      "intervention-type": {
        "component-namespace": "faims-custom",
        "component-name": "MultiSelect",
        "type-returned": "faims-core::Array",
        "component-parameters": {
          "name": "intervention-type",
          "label": "Intervention Types Required",
          "options": [
            {"value": "structural", "label": "Structural Repair"},
            {"value": "safety", "label": "Safety Measures"},
            {"value": "environmental", "label": "Environmental Protection"},
            {"value": "monitoring", "label": "Ongoing Monitoring"}
          ]
        },
        "is-logic": {
          "if": "requires-intervention",
          "==": true
        }
      },
      "priority-level": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "priority-level",
          "label": "Priority Level",
          "options": [
            {"value": "urgent", "label": "Urgent (24 hours)"},
            {"value": "high", "label": "High (1 week)"},
            {"value": "medium", "label": "Medium (1 month)"},
            {"value": "low", "label": "Low (3 months)"}
          ],
          "required": true
        },
        "is-logic": {
          "if": "requires-intervention",
          "==": true
        }
      },
      "hazards-present": {
        "component-namespace": "faims-custom",
        "component-name": "MultiSelect",
        "type-returned": "faims-core::Array",
        "component-parameters": {
          "name": "hazards-present",
          "label": "Hazards Present",
          "options": [
            {"value": "none", "label": "None Identified"},
            {"value": "structural", "label": "Structural Instability"},
            {"value": "chemical", "label": "Chemical Hazard"},
            {"value": "biological", "label": "Biological Hazard"},
            {"value": "electrical", "label": "Electrical Hazard"},
            {"value": "other", "label": "Other"}
          ],
          "expandedChecklist": true,
          "exclusiveOptions": ["none"]
        }
      },
      "hazard-details": {
        "component-namespace": "faims-custom",
        "component-name": "MultipleTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "hazard-details",
          "label": "Hazard Details",
          "helperText": "Describe the hazards in detail",
          "multiline": true,
          "rows": 4,
          "required": true
        },
        "is-logic": {
          "if": "hazards-present",
          "not-includes": "none"
        },
        "validationSchema": [
          ["yup.string"],
          ["yup.required", "Hazard details required when hazards present"],
          ["yup.min", 20, "Please provide at least 20 characters of detail"]
        ]
      },
      "measurements-taken": {
        "component-namespace": "faims-custom",
        "component-name": "Checkbox",
        "type-returned": "faims-core::Bool",
        "component-parameters": {
          "name": "measurements-taken",
          "label": "Detailed measurements recorded",
          "logic_select": true
        }
      },
      "length-m": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "length-m",
          "label": "Length (meters)",
          "InputProps": {
            "type": "number",
            "step": 0.01
          },
          "min": 0
        },
        "is-logic": {
          "if": "measurements-taken",
          "==": true
        }
      },
      "width-m": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "width-m",
          "label": "Width (meters)",
          "InputProps": {
            "type": "number",
            "step": 0.01
          },
          "min": 0
        },
        "is-logic": {
          "if": "measurements-taken",
          "==": true
        }
      },
      "height-m": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "height-m",
          "label": "Height (meters)",
          "InputProps": {
            "type": "number",
            "step": 0.01
          },
          "min": 0
        },
        "is-logic": {
          "if": "measurements-taken",
          "==": true
        }
      },
      "weather-conditions": {
        "component-namespace": "faims-custom",
        "component-name": "Select",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "weather-conditions",
          "label": "Weather During Assessment",
          "options": [
            {"value": "clear", "label": "Clear"},
            {"value": "cloudy", "label": "Cloudy"},
            {"value": "rain", "label": "Rain"},
            {"value": "storm", "label": "Storm"},
            {"value": "snow", "label": "Snow"}
          ],
          "required": true
        }
      },
      "visibility": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "visibility",
          "label": "Visibility",
          "options": [
            {"value": "excellent", "label": "Excellent (>10km)"},
            {"value": "good", "label": "Good (5-10km)"},
            {"value": "moderate", "label": "Moderate (1-5km)"},
            {"value": "poor", "label": "Poor (<1km)"}
          ],
          "required": true
        }
      },
      "follow-up-required": {
        "component-namespace": "faims-custom",
        "component-name": "Checkbox",
        "type-returned": "faims-core::Bool",
        "component-parameters": {
          "name": "follow-up-required",
          "label": "Follow-up assessment required"
        }
      },
      "assessment-notes": {
        "component-namespace": "faims-custom",
        "component-name": "MultipleTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "assessment-notes",
          "label": "Assessment Notes",
          "helperText": "Any additional observations or recommendations",
          "multiline": true,
          "rows": 5
        }
      }
    },
    "fviews": {
      "identification": {
        "fields": ["assessment-id", "assessor-name", "assessment-date"],
        "label": "Identification",
        "uidesign": "form"
      },
      "location": {
        "fields": ["location-type", "urban-density", "access-difficulty"],
        "label": "Location Details",
        "uidesign": "form"
      },
      "condition": {
        "fields": ["condition-score", "requires-intervention", "intervention-type", "priority-level"],
        "label": "Condition Assessment",
        "uidesign": "form"
      },
      "hazards": {
        "fields": ["hazards-present", "hazard-details"],
        "label": "Hazard Assessment",
        "uidesign": "form"
      },
      "measurements": {
        "fields": ["measurements-taken", "length-m", "width-m", "height-m"],
        "label": "Measurements",
        "uidesign": "form"
      },
      "environment": {
        "fields": ["weather-conditions", "visibility"],
        "label": "Environmental Conditions",
        "uidesign": "form"
      },
      "summary": {
        "fields": ["follow-up-required", "assessment-notes"],
        "label": "Summary",
        "uidesign": "form"
      }
    },
    "viewsets": {
      "complex-assessment": {
        "views": ["identification", "location", "condition", "hazards", "measurements", "environment", "summary"],
        "label": "Complex Assessment",
        "publishButtonBehaviour": "always"
      }
    },
    "visible_types": ["complex-assessment"]
  }
}
```

---

## Template 4: Mobile-Optimized (GPS/Photo)

**Use Case**: Field data collection on mobile devices  
**Fields**: GPS capture, photo documentation, mobile-friendly inputs  
**Complexity**: Mobile-specific

```json
{
  "metadata": {
    "notebook_version": "1.0.0",
    "created": "2025-01-07",
    "name": "{{PROJECT_NAME}}-mobile",
    "description": "Mobile-optimized form with GPS and photo capture"
  },
  "ui-specification": {
    "fields": {
      "observation-id": {
        "component-namespace": "faims-custom",
        "component-name": "TemplatedStringField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "observation-id",
          "label": "Observation ID",
          "template": "OBS-{{_CREATED_DATE}}-{{_INCREMENT}}",
          "required": true
        }
      },
      "observer-name": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "observer-name",
          "label": "Observer",
          "initialValue": "{{_USER}}",
          "required": true
        }
      },
      "observation-time": {
        "component-namespace": "faims-custom",
        "component-name": "DateTimeNow",
        "type-returned": "faims-core::DateTime",
        "component-parameters": {
          "name": "observation-time",
          "label": "Observation Time"
        }
      },
      "location-point": {
        "component-namespace": "faims-custom",
        "component-name": "TakePoint",
        "type-returned": "faims-core::JSON",
        "component-parameters": {
          "name": "location-point",
          "label": "GPS Location",
          "helperText": "Tap to capture current GPS position",
          "required": true
        }
      },
      "location-accuracy": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "location-accuracy",
          "label": "GPS Accuracy",
          "options": [
            {"value": "high", "label": "High (<5m)"},
            {"value": "medium", "label": "Medium (5-15m)"},
            {"value": "low", "label": "Low (>15m)"}
          ]
        }
      },
      "observation-type": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "observation-type",
          "label": "Observation Type",
          "options": [
            {"value": "flora", "label": "Flora"},
            {"value": "fauna", "label": "Fauna"},
            {"value": "geological", "label": "Geological"},
            {"value": "cultural", "label": "Cultural"},
            {"value": "other", "label": "Other"}
          ],
          "required": true
        }
      },
      "quick-description": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "quick-description",
          "label": "Quick Description",
          "helperText": "Brief description (voice input available)",
          "required": true
        }
      },
      "photo-1": {
        "component-namespace": "faims-custom",
        "component-name": "TakePhoto",
        "type-returned": "faims-core::File",
        "component-parameters": {
          "name": "photo-1",
          "label": "Primary Photo",
          "helperText": "Tap to take photo"
        }
      },
      "photo-2": {
        "component-namespace": "faims-custom",
        "component-name": "TakePhoto",
        "type-returned": "faims-core::File",
        "component-parameters": {
          "name": "photo-2",
          "label": "Context Photo",
          "helperText": "Optional wider context shot"
        }
      },
      "abundance": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "abundance",
          "label": "Abundance",
          "options": [
            {"value": "single", "label": "Single"},
            {"value": "few", "label": "Few (2-10)"},
            {"value": "many", "label": "Many (11-100)"},
            {"value": "abundant", "label": "Abundant (>100)"}
          ]
        }
      },
      "confidence": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "confidence",
          "label": "ID Confidence",
          "options": [
            {"value": "certain", "label": "Certain"},
            {"value": "probable", "label": "Probable"},
            {"value": "possible", "label": "Possible"}
          ],
          "required": true
        }
      },
      "specimen-collected": {
        "component-namespace": "faims-custom",
        "component-name": "Checkbox",
        "type-returned": "faims-core::Bool",
        "component-parameters": {
          "name": "specimen-collected",
          "label": "Specimen collected",
          "logic_select": true
        }
      },
      "specimen-id": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "specimen-id",
          "label": "Specimen ID",
          "helperText": "Enter specimen bag/container ID"
        },
        "is-logic": {
          "if": "specimen-collected",
          "==": true
        }
      },
      "weather": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "weather",
          "label": "Weather",
          "options": [
            {"value": "sunny", "label": "☀️ Sunny"},
            {"value": "cloudy", "label": "☁️ Cloudy"},
            {"value": "rain", "label": "🌧️ Rain"},
            {"value": "wind", "label": "💨 Windy"}
          ]
        }
      },
      "field-notes": {
        "component-namespace": "faims-custom",
        "component-name": "MultipleTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "field-notes",
          "label": "Field Notes",
          "helperText": "Additional observations",
          "multiline": true,
          "rows": 3
        }
      }
    },
    "fviews": {
      "quick-capture": {
        "fields": ["observation-id", "observer-name", "observation-time", "location-point", "location-accuracy"],
        "label": "Location & Time",
        "uidesign": "form"
      },
      "observation": {
        "fields": ["observation-type", "quick-description", "photo-1", "photo-2"],
        "label": "Observation",
        "uidesign": "form"
      },
      "details": {
        "fields": ["abundance", "confidence", "specimen-collected", "specimen-id"],
        "label": "Details",
        "uidesign": "form"
      },
      "conditions": {
        "fields": ["weather", "field-notes"],
        "label": "Conditions & Notes",
        "uidesign": "form"
      }
    },
    "viewsets": {
      "mobile-observation": {
        "views": ["quick-capture", "observation", "details", "conditions"],
        "label": "Field Observation",
        "publishButtonBehaviour": "always"
      }
    },
    "visible_types": ["mobile-observation"]
  }
}
```

---

## Template 5: Production Archaeological Recording

**Use Case**: Professional archaeological excavation recording  
**Fields**: Context recording, relationships, stratigraphy  
**Complexity**: Production-ready

```json
{
  "metadata": {
    "notebook_version": "1.0.0",
    "created": "2025-01-07",
    "name": "{{PROJECT_NAME}}-archaeological",
    "description": "Production archaeological context recording"
  },
  "ui-specification": {
    "fields": {
      "context-id": {
        "component-namespace": "faims-custom",
        "component-name": "TemplatedStringField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "context-id",
          "label": "Context Number",
          "template": "{{SITE_CODE}}-CTX-{{_INCREMENT}}",
          "required": true
        }
      },
      "trench": {
        "component-namespace": "faims-custom",
        "component-name": "Select",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "trench",
          "label": "Trench/Area",
          "options": [
            {"value": "T1", "label": "Trench 1"},
            {"value": "T2", "label": "Trench 2"},
            {"value": "T3", "label": "Trench 3"},
            {"value": "A1", "label": "Area 1"},
            {"value": "A2", "label": "Area 2"}
          ],
          "required": true
        }
      },
      "context-type": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "context-type",
          "label": "Context Type",
          "options": [
            {"value": "deposit", "label": "Deposit"},
            {"value": "cut", "label": "Cut"},
            {"value": "structure", "label": "Structure"},
            {"value": "fill", "label": "Fill"}
          ],
          "required": true,
          "logic_select": true
        }
      },
      "deposit-type": {
        "component-namespace": "faims-custom",
        "component-name": "Select",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "deposit-type",
          "label": "Deposit Type",
          "options": [
            {"value": "topsoil", "label": "Topsoil"},
            {"value": "subsoil", "label": "Subsoil"},
            {"value": "occupation", "label": "Occupation Layer"},
            {"value": "destruction", "label": "Destruction Layer"},
            {"value": "natural", "label": "Natural"}
          ]
        },
        "is-logic": {
          "if": "context-type",
          "==": "deposit"
        }
      },
      "cut-type": {
        "component-namespace": "faims-custom",
        "component-name": "Select",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "cut-type",
          "label": "Cut Type",
          "options": [
            {"value": "pit", "label": "Pit"},
            {"value": "posthole", "label": "Posthole"},
            {"value": "ditch", "label": "Ditch"},
            {"value": "foundation", "label": "Foundation Trench"},
            {"value": "grave", "label": "Grave"}
          ]
        },
        "is-logic": {
          "if": "context-type",
          "==": "cut"
        }
      },
      "opening-date": {
        "component-namespace": "formik-material-ui",
        "component-name": "DatePicker",
        "type-returned": "faims-core::Date",
        "component-parameters": {
          "name": "opening-date",
          "label": "Date Opened",
          "required": true
        }
      },
      "excavator": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "excavator",
          "label": "Excavator(s)",
          "required": true
        }
      },
      "soil-colour": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "soil-colour",
          "label": "Soil Colour (Munsell)",
          "helperText": "e.g., 10YR 3/2"
        }
      },
      "soil-texture": {
        "component-namespace": "faims-custom",
        "component-name": "Select",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "soil-texture",
          "label": "Soil Texture",
          "options": [
            {"value": "sand", "label": "Sand"},
            {"value": "silt", "label": "Silt"},
            {"value": "clay", "label": "Clay"},
            {"value": "sandy-silt", "label": "Sandy Silt"},
            {"value": "silty-clay", "label": "Silty Clay"},
            {"value": "sandy-clay", "label": "Sandy Clay"}
          ]
        }
      },
      "compaction": {
        "component-namespace": "faims-custom",
        "component-name": "RadioGroup",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "compaction",
          "label": "Compaction",
          "options": [
            {"value": "loose", "label": "Loose"},
            {"value": "moderate", "label": "Moderate"},
            {"value": "compact", "label": "Compact"},
            {"value": "very-compact", "label": "Very Compact"}
          ]
        }
      },
      "inclusions": {
        "component-namespace": "faims-custom",
        "component-name": "MultiSelect",
        "type-returned": "faims-core::Array",
        "component-parameters": {
          "name": "inclusions",
          "label": "Inclusions",
          "options": [
            {"value": "none", "label": "None"},
            {"value": "charcoal", "label": "Charcoal"},
            {"value": "pottery", "label": "Pottery"},
            {"value": "bone", "label": "Bone"},
            {"value": "stone", "label": "Stone"},
            {"value": "brick", "label": "Brick/Tile"},
            {"value": "metal", "label": "Metal"},
            {"value": "glass", "label": "Glass"}
          ],
          "expandedChecklist": true,
          "exclusiveOptions": ["none"]
        }
      },
      "dimensions-length": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "dimensions-length",
          "label": "Length (m)",
          "InputProps": {
            "type": "number",
            "step": 0.01
          },
          "min": 0
        }
      },
      "dimensions-width": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "dimensions-width",
          "label": "Width (m)",
          "InputProps": {
            "type": "number",
            "step": 0.01
          },
          "min": 0
        }
      },
      "dimensions-depth": {
        "component-namespace": "formik-material-ui",
        "component-name": "TextField",
        "type-returned": "faims-core::Number",
        "component-parameters": {
          "name": "dimensions-depth",
          "label": "Depth/Thickness (m)",
          "InputProps": {
            "type": "number",
            "step": 0.01
          },
          "min": 0
        }
      },
      "stratigraphic-relationships": {
        "component-namespace": "faims-custom",
        "component-name": "RelatedRecordSelector",
        "type-returned": "faims-core::Relationship",
        "component-parameters": {
          "name": "stratigraphic-relationships",
          "label": "Stratigraphic Relationships",
          "relation_type": "stratigraphic",
          "vocabulary": [
            {"label": "Above", "value": "above"},
            {"label": "Below", "value": "below"},
            {"label": "Cuts", "value": "cuts"},
            {"label": "Cut by", "value": "cut-by"},
            {"label": "Fills", "value": "fills"},
            {"label": "Filled by", "value": "filled-by"},
            {"label": "Same as", "value": "same-as"}
          ]
        }
      },
      "interpretation": {
        "component-namespace": "faims-custom",
        "component-name": "MultipleTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "interpretation",
          "label": "Interpretation",
          "helperText": "Preliminary interpretation of the context",
          "multiline": true,
          "rows": 4,
          "required": true
        }
      },
      "finds-collected": {
        "component-namespace": "faims-custom",
        "component-name": "Checkbox",
        "type-returned": "faims-core::Bool",
        "component-parameters": {
          "name": "finds-collected",
          "label": "Finds collected",
          "logic_select": true
        }
      },
      "finds-summary": {
        "component-namespace": "faims-custom",
        "component-name": "MultipleTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "finds-summary",
          "label": "Finds Summary",
          "helperText": "Brief description of finds",
          "multiline": true,
          "rows": 2
        },
        "is-logic": {
          "if": "finds-collected",
          "==": true
        }
      },
      "samples-taken": {
        "component-namespace": "faims-custom",
        "component-name": "MultiSelect",
        "type-returned": "faims-core::Array",
        "component-parameters": {
          "name": "samples-taken",
          "label": "Samples Taken",
          "options": [
            {"value": "none", "label": "None"},
            {"value": "soil", "label": "Soil Sample"},
            {"value": "flotation", "label": "Flotation"},
            {"value": "c14", "label": "C14"},
            {"value": "pollen", "label": "Pollen"},
            {"value": "phytolith", "label": "Phytolith"},
            {"value": "other", "label": "Other"}
          ],
          "expandedChecklist": true,
          "exclusiveOptions": ["none"]
        }
      },
      "photo-plan": {
        "component-namespace": "faims-custom",
        "component-name": "TakePhoto",
        "type-returned": "faims-core::File",
        "component-parameters": {
          "name": "photo-plan",
          "label": "Plan Photo",
          "helperText": "Overview from above"
        }
      },
      "photo-section": {
        "component-namespace": "faims-custom",
        "component-name": "TakePhoto",
        "type-returned": "faims-core::File",
        "component-parameters": {
          "name": "photo-section",
          "label": "Section Photo",
          "helperText": "Profile/section view"
        }
      },
      "drawing-refs": {
        "component-namespace": "faims-custom",
        "component-name": "FAIMSTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "drawing-refs",
          "label": "Drawing References",
          "helperText": "Plan/section drawing numbers"
        }
      },
      "closed-date": {
        "component-namespace": "formik-material-ui",
        "component-name": "DatePicker",
        "type-returned": "faims-core::Date",
        "component-parameters": {
          "name": "closed-date",
          "label": "Date Closed"
        }
      },
      "recorder-notes": {
        "component-namespace": "faims-custom",
        "component-name": "MultipleTextField",
        "type-returned": "faims-core::String",
        "component-parameters": {
          "name": "recorder-notes",
          "label": "Recorder Notes",
          "helperText": "Additional observations",
          "multiline": true,
          "rows": 3
        }
      }
    },
    "fviews": {
      "identification": {
        "fields": ["context-id", "trench", "context-type", "deposit-type", "cut-type", "opening-date", "excavator"],
        "label": "Identification",
        "uidesign": "form"
      },
      "description": {
        "fields": ["soil-colour", "soil-texture", "compaction", "inclusions"],
        "label": "Physical Description",
        "uidesign": "form"
      },
      "dimensions": {
        "fields": ["dimensions-length", "dimensions-width", "dimensions-depth"],
        "label": "Dimensions",
        "uidesign": "form"
      },
      "stratigraphy": {
        "fields": ["stratigraphic-relationships", "interpretation"],
        "label": "Stratigraphy & Interpretation",
        "uidesign": "form"
      },
      "finds-samples": {
        "fields": ["finds-collected", "finds-summary", "samples-taken"],
        "label": "Finds & Samples",
        "uidesign": "form"
      },
      "documentation": {
        "fields": ["photo-plan", "photo-section", "drawing-refs"],
        "label": "Documentation",
        "uidesign": "form"
      },
      "closure": {
        "fields": ["closed-date", "recorder-notes"],
        "label": "Closure",
        "uidesign": "form"
      }
    },
    "viewsets": {
      "context-record": {
        "views": ["identification", "description", "dimensions", "stratigraphy", "finds-samples", "documentation", "closure"],
        "label": "Context Record",
        "publishButtonBehaviour": "always"
      }
    },
    "visible_types": ["context-record"]
  }
}
```

---

## Common Issues and Solutions

### Issue: Notebook won't import
**Solution**: Check these common problems:
1. JSON syntax errors - validate with JSON validator
2. Missing fviews layer between fields and viewsets
3. Field referenced in fview doesn't exist
4. Missing `name` parameter in component-parameters
5. Duplicate field names

### Issue: Fields not appearing
**Solution**: Ensure:
1. Field is listed in an fview
2. Fview is listed in a viewset
3. Viewset is listed in visible_types
4. No conditional logic hiding the field

### Issue: Validation not working
**Solution**: Check:
1. Validation schema syntax is correct
2. Using correct Yup methods
3. Type-returned matches validation type
4. Required fields marked correctly

### Issue: GPS/Photo not working on web
**Solution**: These are mobile-only features:
- TakePoint requires mobile GPS
- TakePhoto requires mobile camera
- Provide alternative text fields for web users

---

## Related Documentation

- [Notebook Format Guide](./notebook-format-guide.md) - Complete structure requirements
- [Designer Component Mapping](./designer-component-mapping.md) - All component mappings
- [Field Selection Guide](../patterns/field-selection-guide.md) - Choosing appropriate fields
- [Dynamic Forms Guide](../patterns/dynamic-forms-guide.md) - Conditional logic patterns

---

*These templates provide working starting points for notebook development. Always test thoroughly before deployment.*