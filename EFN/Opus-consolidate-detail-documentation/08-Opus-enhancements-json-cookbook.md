## Prompt B1: Generate JSON Patterns Cookbook (ENHANCED)

You are enhancing a Fieldmark field documentation file for LLM-first consumption, particularly for Claude Code notebook generation.

TASK: Create a JSON Patterns Cookbook that shows all configuration variants using compact diff notation.

INPUT: The consolidated text field documentation is available in project knowledge as "Email and Address Fields - Merged Documentation.md" - this document contains all 7 field types with JSON examples. Please search for and load this document to analyze.

CRITICAL INSTRUCTION: Generate ONLY the new section to be appended. Do NOT reproduce the original document. Output ONLY the enhancement section with clear integration markers.

REQUIREMENTS:
1. Create a new section: "JSON Patterns Cookbook (2025-08)"
2. Generate ONLY this new section, not the full document
3. Use diff notation (+/-) to show variations from base patterns
4. Group patterns by field type
5. Include inline comments for clarity (// style)
6. Add "ANTI-PATTERNS" section for each field showing what NOT to do
7. Include "ERROR PATTERNS" showing common mistakes and their error messages
8. Add "INTEGRATION PATTERNS" showing fields working together
9. Include troubleshooting comments for common issues

OUTPUT FORMAT:

[START OF GENERATED SECTION - Add before Metadata]
---
## JSON Patterns Cookbook (2025-08) {comprehensive}

### TextField Patterns

```json
// BASE PATTERN (all TextField variants start here)
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",  // MUST match field ID
    "label": "Field Label"
  },
  "validationSchema": [["yup.string"]],
  "initialValue": ""  // MUST be "" not null for strings
}

// VARIANT: Required field
+ "component-parameters": {
+   "required": true,
+   "helperText": "This field is mandatory"
+ }
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.required", "Field is required"]  // Order matters!
+ ]

// VARIANT: Pattern validation (e.g., site codes)
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.matches", "^[A-Z]{3}-\\d{3}$", "Format: ABC-123"]
+   // NOTE: Double escape in JSON: \d becomes \\d
+ ]
```

#### TextField ANTI-PATTERNS ⚠️
```json
// ❌ NEVER: Wrong initialValue type
{
  "initialValue": null  // ERROR: "Cannot read property 'length' of null"
}

// ❌ NEVER: Validation order reversed
{
  "validationSchema": [
    ["yup.required"],  // ERROR: "yup.required is not a function"
    ["yup.string"]     // Type must come first!
  ]
}

// ❌ NEVER: Missing name parameter
{
  "component-parameters": {
    "label": "Field Label"
    // ERROR: "Field name is required"
  }
}

// ❌ NEVER: Mismatched name and field ID
"my-field": {
  "component-parameters": {
    "name": "different-name"  // ERROR: Field won't save data
  }
}
```

### TemplatedString Patterns

```json
// BASE: Human-Readable Identifier (CRITICAL - every notebook needs one!)
{
  "component-namespace": "faims-custom",
  "component-name": "TemplatedStringField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "record-id",
    "template": "{{entity}}-{{counter}}"
    // All referenced fields MUST exist in same form
  }
}

// VARIANT: With system variables
  "template": "{{site}}-{{_CREATED_TIME}}-{{_CREATOR_NAME}}"
  // _CREATED_TIME format: "DD-MM-YY H:MMam/pm"
  // _CREATOR_NAME may be "Unknown User" if null

// VARIANT: Hidden boolean for conditionals (clever hack!)
+ "component-parameters": {
+   "hidden": true,
+   "name": "_has_photos",  // Prefix with _ for system fields
+   "template": "{{#photos}}true{{/photos}}{{^photos}}false{{/photos}}"
+ }
// Use in conditional logic: field="_has_photos", value="true"
```

#### TemplatedString ANTI-PATTERNS ⚠️
```json
// ❌ NEVER: Circular reference
{
  "hrid1": {"template": "{{hrid2}}-A"},
  "hrid2": {"template": "{{hrid1}}-B"}
  // ERROR: "Maximum call stack size exceeded"
}

// ❌ NEVER: Direct complex field reference
{
  "template": "Record-{{relationship}}"
  // RESULT: "Record-[object Object]" (useless!)
  // FIX: Use conditional: "{{#relationship}}linked{{/relationship}}"
}

// ❌ NEVER: User text fields without sanitization
{
  "template": "{{user-input}}"  // XSS RISK!
  // If user enters: <script>alert('XSS')</script>
  // Template renders script! HTML escaping is DISABLED
}
```

### QRCodeFormField Patterns

```json
// BASE: Scanner only (REMEMBER: mobile-only!)
{
  "component-namespace": "qrcode",
  "component-name": "QRCodeFormField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "barcode-scan",
    "label": "Scan Barcode"
  },
  "validationSchema": [["yup.string"]],  // NEVER add required!
  "initialValue": ""
}
```

#### QRCodeFormField ANTI-PATTERNS ⚠️
```json
// ❌ NEVER: Required validation
{
  "validationSchema": [
    ["yup.string"],
    ["yup.required"]  // BREAKS ALL WEB USERS!
  ]
}

// ❌ NEVER: Scanner without fallback
{
  "barcode": {
    "component-name": "QRCodeFormField"
    // Web users see disabled field, cannot proceed!
  }
}
// ✅ ALWAYS: Pair with TextField (see Integration Patterns)
```

### Integration Patterns (Fields Working Together)

```json
// PATTERN: QRCode + Manual Entry with Conditional Display
{
  "platform-check": {
    "component-name": "RadioGroup",
    "component-parameters": {
      "label": "Select your platform",
      "options": [
        {"value": "mobile", "label": "Mobile (iOS/Android)"},
        {"value": "web", "label": "Web/Desktop"}
      ]
    }
  },
  "barcode-scan": {
    "component-name": "QRCodeFormField",
    "condition": {
      "field": "platform-check",
      "operator": "equal",
      "value": "mobile"
    }
  },
  "barcode-manual": {
    "component-name": "TextField",
    "condition": {
      "field": "platform-check",
      "operator": "equal",
      "value": "web"
    }
  }
}

// PATTERN: TemplatedString + Counter + Type
{
  "record-type": {
    "component-name": "Select",
    "component-parameters": {
      "options": [
        {"value": "ART", "label": "Artefact"},
        {"value": "SAM", "label": "Sample"},
        {"value": "FEA", "label": "Feature"}
      ]
    }
  },
  "counter": {
    "component-name": "BasicAutoIncrementer",
    "component-parameters": {
      "num_digits": 5  // Pads to "00001"
    }
  },
  "record-id": {
    "component-name": "TemplatedStringField",
    "component-parameters": {
      "template": "{{record-type}}-2025-{{counter}}"
      // Result: "ART-2025-00042"
    }
  }
  // Don't forget: Set record-id as hridField in viewset!
}
```

### Error Message Reference

```json
// Common errors and their meanings:
{
  "Cannot read property 'length' of null": "String field has null initialValue",
  "Maximum call stack size exceeded": "Circular template reference",
  "[object Object]": "Complex field in template, use conditionals",
  "Unknown component": "Wrong component name or namespace",
  "Field name is required": "Missing name in component-parameters",
  "yup.required is not a function": "Validation schema order wrong",
  "Form cannot be submitted": "QRCodeFormField marked required on web"
}