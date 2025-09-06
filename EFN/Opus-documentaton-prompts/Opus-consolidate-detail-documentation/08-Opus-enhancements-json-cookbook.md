# Prompt B1: Generate JSON Patterns Cookbook

You are enhancing a Fieldmark field documentation file for LLM-first consumption, particularly for Claude Code notebook generation.

TASK: Create a JSON Patterns Cookbook that shows all configuration variants using compact diff notation.

INPUT: The consolidated field documentation containing all [N] field types with JSON examples. Load this document from project knowledge to analyze.

CRITICAL INSTRUCTION: Generate ONLY the new section to be appended. Do NOT reproduce the original document. Output ONLY the enhancement section with clear integration markers.

REQUIREMENTS:
1. Create a new section: "JSON Patterns Cookbook (2025-08)"
2. Generate ONLY this new section, not the full document
3. Use diff notation (+/-) to show variations from base patterns
4. Group patterns by field type
5. Include inline comments for clarity (// style)
6. Include "ANTI-PATTERNS" subsection for each field showing what NOT to do
7. Include "Integration Patterns" section showing fields working together
8. Include "Platform-Specific Configurations" section
9. Add troubleshooting comments for common issues
10. Use ⚠️ warning emoji for anti-patterns and critical issues

OUTPUT FORMAT:

[START OF GENERATED SECTION - Add before Metadata]
---
## JSON Patterns Cookbook (2025-08) {comprehensive}

### [Field1] Patterns

```json
// BASE PATTERN (all [Field1] variants start here)
{
  "component-namespace": "namespace-name",
  "component-name": "ComponentName",
  "type-returned": "faims-core::Type",
  "component-parameters": {
    "name": "field-name",  // MUST match field ID
    "label": "Field Label"
  },
  "validationSchema": [["yup.type"]],
  "initialValue": ""  // Type-specific default
}

// VARIANT: Required field
+ "component-parameters": {
+   "required": true,
+   "helperText": "This field is mandatory"
+ }
+ "validationSchema": [
+   ["yup.type"],
+   ["yup.required", "Field is required"]  // Order matters!
+ ]

// VARIANT: With validation
+ "validationSchema": [
+   ["yup.type"],
+   ["yup.validation", "parameter", "Error message"]
+ ]
```

#### [Field1] ANTI-PATTERNS ⚠️
```json
// ❌ NEVER: [Description of mistake]
{
  "problematic-config": "value"  
  // ERROR: "[Error message]"
}
// ✅ ALWAYS: [Correct approach]
{
  "correct-config": "value"
}

// ❌ NEVER: [Another mistake]
// ✅ ALWAYS: [Correct alternative]
```

### [Field2] Patterns

[Continue pattern for each field type]

### Platform-Specific Configurations

```json
// iOS-Optimized Configuration
{
  "component-parameters": {
    "fullWidth": true,
    "margin": "dense",  // More space for iOS overlay
    "InputProps": {
      "style": {
        "paddingBottom": "20px"  // Extra padding for picker
      }
    }
  }
}

// Android-Optimized Configuration
{
  "component-parameters": {
    "variant": "outlined",  // Better touch target
    "InputProps": {
      "style": {
        "minHeight": "56px"  // Material Design touch target
      }
    }
  }
}

// Desktop-Optimized Configuration
{
  "component-parameters": {
    "fullWidth": false,  // Narrower for mouse precision
    "variant": "standard"
  }
}
```

### Integration Patterns (Fields Working Together)

```json
// PATTERN: [Description of integration]
{
  "field1": {
    "component-name": "Component1",
    "component-parameters": {
      // Configuration that works with field2
    }
  },
  "field2": {
    "component-name": "Component2",
    "component-parameters": {
      // Configuration that depends on field1
    },
    "condition": {
      "field": "field1",
      "operator": "equal",
      "value": "trigger-value"
    }
  }
}

// PATTERN: [Another integration pattern]
[Continue with relevant patterns]
```

### Common Anti-Patterns Across All Fields ⚠️

```json
// ❌ NEVER: Wrong initialValue type
{
  "initialValue": null  // When expecting string
  // ERROR: "Cannot read property 'length' of null"
}

// ❌ NEVER: Validation schema in wrong order
{
  "validationSchema": [
    ["yup.required"],  // ERROR: "yup.required is not a function"
    ["yup.string"]     // Type must come first!
  ]
}

// ❌ NEVER: Mismatched name and field ID
"my-field": {
  "component-parameters": {
    "name": "different-name"  // ERROR: Field won't save data
  }
}

// ❌ NEVER: Wrong component namespace
{
  "component-namespace": "wrong-namespace",
  "component-name": "ComponentName"
  // ERROR: "Component not found"
}
```

### Error Message Quick Reference

```json
// Common errors and their meanings:
{
  "[Error message 1]": "[Cause and solution]",
  "[Error message 2]": "[Cause and solution]",
  "[Error message 3]": "[Cause and solution]"
}
```

---
[END OF GENERATED SECTION]