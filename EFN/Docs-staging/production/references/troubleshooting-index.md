# Troubleshooting Index for Fieldmark Notebooks

**Purpose**: Direct error-to-solution mapping for common Fieldmark issues  
**Created**: 2025-01-07  
**Usage**: Search by error message or symptom to find immediate solutions

<!-- discovery:metadata

<!-- structured:metadata
meta:purpose: technical-reference
meta:summary: Error-to-solution mapping with diagnostic flowcharts covering 95% of common issues.
meta:generates: lookup-tables
meta:requires: [fieldmark-knowledge]
meta:version: 3.0.0
meta:document: troubleshooting_index
meta:depth-tags: [essential]
-->

provides: [error-solutions, diagnostic-flowcharts, validation-decoder, common-problems]
see-also: [notebook-format-guide, constraints-reference, platform-reference]
-->

## Quick Error Lookup

### By Error Message

| Error Message | Likely Cause | Solution | Reference |
|--------------|--------------|----------|-----------|
| "Sorry, something went wrong" | Missing fviews layer | Add fviews between fields and viewsets | [Notebook Structure](#notebook-structure-errors) |
| "Invalid notebook format" | JSON syntax error | Validate JSON syntax | [JSON Errors](#json-syntax-errors) |
| "Field not found" | Field referenced but not defined | Check field exists in fields object | [Field Reference Errors](#field-reference-errors) |
| "Invalid component" | Wrong component name/namespace | Check designer-component-mapping | [Component Errors](#component-errors) |
| "Validation failed" | Schema syntax error | Fix validation schema | [Validation Errors](#validation-errors) |
| "Cannot read property 'name'" | Missing name parameter | Add name to component-parameters | [Missing Parameters](#missing-parameters) |
| "Maximum call stack exceeded" | Circular reference | Check relationship loops | [Circular References](#circular-references) |
| "Network error" | Offline with online-only field | Check platform requirements | [Platform Issues](#platform-issues) |
| "GPS not available" | Web browser limitation | Use mobile app for GPS | [Mobile-Only Features](#mobile-only-features) |
| "File too large" | Exceeds upload limit | Reduce file size or compress | [File Upload Issues](#file-upload-issues) |
| "Finish button not appearing" | publishButtonBehaviour config | Check Form Settings configuration | [Form Settings Issues](#form-settings-issues) |
| "HRID shows as rec-xxxxx" | No hridField configured | Configure HRID in Form Settings | [Form Settings Issues](#form-settings-issues) |
| "Summary fields not showing" | Empty summary_fields array | Select fields in Form Settings | [Form Settings Issues](#form-settings-issues) |
| "Custom field not saving" | Duplicate or reserved name | Use unique field name | [Notebook Info Issues](#notebook-info-issues) |
| "QR Code search not working" | Not enabled in metadata | Enable in Notebook Info page | [Notebook Info Issues](#notebook-info-issues) |
| "Can't create notebook" | Missing GENERAL_CREATOR role | Grant role in Users interface | [Permission Issues](#permission-issues) |
| "Can't edit notebook structure" | Missing PROJECT_MANAGER role | Add as notebook manager | [Permission Issues](#permission-issues) |
| "Can't see team notebooks" | Not team member | Add user to team | [Permission Issues](#permission-issues) |

---

## Diagnostic Flowcharts

### Notebook Won't Import Flowchart

```
Notebook won't import?
│
├─ Does the JSON parse successfully?
│  ├─ No → [Fix JSON Syntax Errors](#json-syntax-errors)
│  └─ Yes ↓
│
├─ Does it have ui-specification?
│  ├─ No → Add ui-specification wrapper
│  └─ Yes ↓
│
├─ Does it have fields, fviews, AND viewsets?
│  ├─ No → [Fix Structure Issues](#notebook-structure-errors)
│  └─ Yes ↓
│
├─ Do all fields have unique names in component-parameters?
│  ├─ No → [Add Missing Parameters](#missing-parameters)
│  └─ Yes ↓
│
├─ Are all field references in fviews valid?
│  ├─ No → [Fix Field References](#field-reference-errors)
│  └─ Yes ↓
│
├─ Are all fview references in viewsets valid?
│  ├─ No → Fix viewset references
│  └─ Yes ↓
│
├─ Are visible_types pointing to existing viewsets?
│  ├─ No → Fix visible_types array
│  └─ Yes → Check for component-specific issues
```

### Field Not Appearing Flowchart

```
Field not visible in form?
│
├─ Is field defined in ui-specification.fields?
│  ├─ No → Add field definition
│  └─ Yes ↓
│
├─ Is field referenced in any fview?
│  ├─ No → Add field to fview.fields array
│  └─ Yes ↓
│
├─ Is that fview referenced in any viewset?
│  ├─ No → Add fview to viewset.views array
│  └─ Yes ↓
│
├─ Is viewset in visible_types?
│  ├─ No → Add viewset to visible_types
│  └─ Yes ↓
│
├─ Does field have conditional logic (is-logic)?
│  ├─ Yes → Check if condition is met
│  └─ No → Check component parameters
```

---

## Common Problems and Solutions

### Notebook Structure Errors

#### Problem: Missing fviews Layer
**Symptom**: Notebook has fields and viewsets but won't import  
**Error**: "Sorry, something went wrong" or silent failure  
**Solution**:
```json
{
  "ui-specification": {
    "fields": { /* your fields */ },
    "fviews": {  // ADD THIS LAYER
      "section-name": {
        "fields": ["field1", "field2"],
        "label": "Section Label",
        "uidesign": "form"
      }
    },
    "viewsets": {
      "form-name": {
        "views": ["section-name"],  // References fview
        "label": "Form Label"
      }
    }
  }
}
```

#### Problem: Wrong Hierarchy Order
**Symptom**: Structure exists but import fails  
**Solution**: Ensure this exact order:
1. fields (define all fields)
2. fviews (group fields into sections)
3. viewsets (group sections into forms)
4. visible_types (list accessible forms)

### JSON Syntax Errors

#### Problem: Trailing Commas
**Symptom**: "Unexpected token }" 
**Example**:
```json
{
  "field1": "value",
  "field2": "value",  // ← Remove this comma
}
```

#### Problem: Missing Quotes
**Symptom**: "Unexpected token"
**Example**:
```json
{
  name: "value"  // ← Should be "name": "value"
}
```

#### Problem: Single Quotes Instead of Double
**Symptom**: "Unexpected token '"
**Solution**: Replace all ' with " in JSON

### Field Reference Errors

#### Problem: Field in fview doesn't exist
**Symptom**: Import fails or field missing
**Diagnosis**:
```python
# Check all fview field references exist
for fview in notebook['ui-specification']['fviews'].values():
    for field_ref in fview['fields']:
        if field_ref not in notebook['ui-specification']['fields']:
            print(f"Missing field: {field_ref}")
```

### Component Errors

#### Problem: Wrong Component Name
**Common Mistakes**:
- "TextField" in Designer → Actually "FAIMSTextField" or "MultipleTextField"
- "Number Field" → Should be TextField with type="number"
- "Controlled Number" → Not a component, use TextField

**Solution**: Check [designer-component-mapping.md](./designer-component-mapping.md)

#### Problem: Wrong Namespace
**Common Mistakes**:
- Select components: Use "faims-custom" not "formik-material-ui"
- TakePoint: Use "faims-custom" not "mapping-plugin"

### Missing Parameters

#### Problem: No name in component-parameters
**Symptom**: "Cannot read property 'name' of undefined"
**Solution**:
```json
{
  "field-id": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSTextField",
    "component-parameters": {
      "name": "field-id",  // ← REQUIRED
      "label": "Field Label"
    }
  }
}
```

### Validation Errors

#### Problem: Invalid Yup Schema
**Symptom**: Validation not working or form crashes
**Common Issues**:

1. **Wrong validation order**:
```json
// ❌ WRONG
"validationSchema": [
  ["yup.required", "Field required"],
  ["yup.string"]  // Type should be first
]

// ✅ CORRECT
"validationSchema": [
  ["yup.string"],  // Type first
  ["yup.required", "Field required"]
]
```

2. **Type mismatch**:
```json
// ❌ WRONG - Number field with string validation
"type-returned": "faims-core::Number",
"validationSchema": [["yup.string"]]

// ✅ CORRECT
"type-returned": "faims-core::Number",
"validationSchema": [["yup.number"]]
```

### Conditional Logic Issues

#### Problem: Field with is-logic not appearing
**Diagnosis Checklist**:
1. Is the controller field marked with `"logic_select": true`?
2. Is the condition syntax correct?
3. Does the controller field have a value?

**Example Fix**:
```json
{
  "controller": {
    "component-parameters": {
      "logic_select": true  // ← Required for controller
    }
  },
  "dependent": {
    "is-logic": {
      "if": "controller",
      "==": "trigger-value"
    }
  }
}
```

### Platform Issues

#### Problem: QR Scanner shows disabled on web
**Symptom**: Scanner field greyed out  
**Cause**: QRCodeFormField is mobile-only  
**Solution**: 
- Use mobile app for scanning
- Provide TextField fallback for manual entry

#### Problem: GPS not working on desktop
**Symptom**: TakePoint fails or inaccurate  
**Solution**: Use mobile device for GPS capture

#### Problem: Map tiles not loading
**Symptom**: Grey map area  
**Cause**: Requires internet for initial tile load  
**Solution**: Ensure internet connection on first use

### Mobile-Only Features

Features that ONLY work on mobile apps:
- QRCodeFormField (barcode scanning)
- TakePoint (GPS capture - works poorly on desktop)
- TakePhoto (camera integration - limited on desktop)

**Best Practice**: Always provide fallbacks:
```json
{
  "barcode-scan": {
    "component-name": "QRCodeFormField"
    // Mobile scanning
  },
  "barcode-manual": {
    "component-name": "TextField"
    // Desktop fallback
  }
}
```

### Performance Issues

#### Problem: Form very slow with many relationships
**Symptom**: Lag when loading or saving  
**Cause**: >50 relationships per record  
**Solutions**:
- Limit relationships to <50 per record
- Split into multiple related forms
- Use hierarchical structure

#### Problem: Large notebook file
**Symptom**: Slow import/export  
**Cause**: >100 fields or large embedded content  
**Solutions**:
- Split into multiple viewsets
- Remove embedded images from RichText
- Optimize vocabulary lists

### HRID Issues

#### Problem: Records show as UUIDs
**Symptom**: "rec-a7f3b2c1-d4e5..." instead of readable IDs  
**Cause**: Missing TemplatedStringField configured as hridField  
**Solution**:
```json
{
  "record-id": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "component-parameters": {
      "name": "record-id",
      "template": "{{PROJECT}}-{{_CREATED_DATE}}-{{_INCREMENT}}"
    }
  }
}
// Then in metadata or form config:
"hridField": "record-id"
```

### Form Settings Issues

#### Problem: Finish button not appearing
**Symptom**: Can't complete/save form despite filling all fields  
**Causes and Solutions**:

| publishButtonBehaviour Setting | Solution |
|-------------------------------|----------|
| `"visited"` | Visit all form sections/tabs |
| `"noErrors"` | Fix all validation errors (check console) |
| Missing/undefined | Set to `"always"` in Form Settings |

**Debug Commands**:
```javascript
console.log(viewset.publishButtonBehaviour);  // Check current setting
console.log(visitedSections);  // For "visited" mode
console.log(formik.errors);  // For "noErrors" mode
```

#### Problem: HRID shows as "rec-xxxxx"
**Symptom**: Records display with UUID fragments instead of human-readable IDs  
**Solutions**:

1. **Configure hridField in Form Settings**:
   - Editor → Design → Form Settings
   - Select field from "HRID Field" dropdown
   
2. **Ensure selected field is required**:
   ```json
   {
     "survey-id": {
       "component-parameters": {
         "required": true,
         "name": "survey-id"
       }
     }
   }
   ```

3. **Use TemplatedStringField for auto-generation**:
   ```json
   {
     "component-name": "TemplatedStringField",
     "component-parameters": {
       "template": "{{PROJECT}}-{{_INCREMENT}}"
     }
   }
   ```

#### Problem: Summary fields not showing in record table
**Symptom**: Record list table has no columns or wrong columns  
**Solutions**:

1. Check summary_fields configuration:
   ```javascript
   console.log(viewset.summary_fields);  // Should be array of field IDs
   ```

2. Verify field IDs are correct:
   - Must match exact field IDs from current viewset
   - Cannot reference fields from other viewsets
   
3. Use Editor UI to select fields:
   - Editor → Design → Form Settings → Summary Fields
   - Maximum 4 fields recommended for performance

### Notebook Info Issues

#### Problem: Custom metadata field not saving
**Symptom**: Added custom field disappears or shows error  
**Causes and Solutions**:

| Cause | Solution | Example |
|-------|----------|---------|
| Duplicate field name | Use unique name | `custom_project_code` not `name` |
| Reserved field name | Avoid fixed fields | Don't use `raid`, `contributors` |
| Special characters | Use alphanumeric + underscore | `project_2025` not `project-2025` |
| Empty field name | Provide valid name | Cannot be blank |

**Valid Field Name Pattern**: `^[a-zA-Z0-9_]+$`

#### Problem: QR Code search not working
**Symptom**: QR button missing or disabled  
**Solutions**:

1. **Enable in Notebook Info page**:
   ```json
   {
     "metadata": {
       "showQRCodeButton": "true"
     }
   }
   ```

2. **Add QRCodeFormField to notebook**:
   ```json
   {
     "barcode-field": {
       "component-name": "QRCodeFormField",
       "component-namespace": "faims-custom"
     }
   }
   ```

3. **Platform limitations**:
   - Mobile-only feature (iOS/Android)
   - Desktop: Provide TextField fallback

#### Problem: Description formatting lost
**Symptom**: Markdown not rendering, appears as plain text  
**Solutions**:

| Issue | Fix | Example |
|-------|-----|---------|
| Missing blank lines | Add before/after markdown blocks | `\n\n## Heading\n\n` |
| Invalid markdown | Check syntax | Use `**bold**` not `<b>bold</b>` |
| HTML stripped | Use markdown only | Convert HTML to markdown |

### Permission Issues

#### Problem: Can't create notebook
**Symptom**: No "Create Notebook" button or fails with permission error  
**Solution Path**:

1. Check global roles: Dashboard → Users → [Your User]
2. Need: `GENERAL_CREATOR` or `TEMPLATE_CREATOR`
3. Request from: System administrator

#### Problem: Can't edit notebook structure
**Symptom**: Editor tab missing or read-only  
**Solution Path**:

1. Check notebook role: Notebooks → [Notebook] → Users
2. Need: `PROJECT_MANAGER` or higher
3. Request from: Notebook admin or creator

#### Problem: Can't see team notebooks
**Symptom**: Team notebooks not appearing in list  
**Causes and Solutions**:

| Cause | Check | Solution |
|-------|-------|----------|
| Not team member | Teams → [Team] → Users | Request team membership |
| Team role too low | Check team role | Need TEAM_CONTRIBUTOR+ |
| Notebook not shared | Notebook → Users | Ask notebook owner to add team |

#### Problem: Permission debugging flowchart
```
Permission denied?
│
├─ Global role issue?
│  └─ Dashboard → Users → [User] → Roles
│
├─ Team role issue?
│  └─ Teams → [Team] → Users → Check role
│
├─ Notebook role issue?
│  └─ Notebooks → [Notebook] → Users → Check role
│
└─ Virtual role from team?
   └─ Check if team has notebook access
```

**Quick Permission Check Commands** (for developers):
```javascript
// Check current user permissions
console.log(currentUser.roles);  // Global roles
console.log(currentUser.teams);  // Team memberships
console.log(notebook.users[currentUser.id]);  // Notebook role
```

---

## Validation Error Decoder

### Yup Validation Messages

| Error Message | Meaning | Fix |
|--------------|---------|-----|
| "must be a `number` type" | Wrong type for number field | Check type-returned matches validation |
| "must be a valid email" | Email format invalid | Ensure @ and domain present |
| "is a required field" | Required field empty | Fill field or remove required |
| "must be at least X characters" | Too short | Meet minimum length |
| "must be at most X characters" | Too long | Reduce length |
| "must be less than or equal to X" | Number too large | Check max constraint |
| "must be greater than or equal to X" | Number too small | Check min constraint |
| "must match the following" | Regex pattern failed | Check pattern requirements |

---

## Quick Fixes Checklist

### Before Import Checklist
- [ ] JSON validates (use jsonlint.com)
- [ ] Has metadata section
- [ ] Has ui-specification wrapper
- [ ] Has fields object
- [ ] Has fviews object (CRITICAL!)
- [ ] Has viewsets object
- [ ] Has visible_types array
- [ ] All fields have unique names
- [ ] All fields have name in component-parameters
- [ ] At least one TemplatedStringField for HRID
- [ ] All field references in fviews exist
- [ ] All fview references in viewsets exist
- [ ] All visible_types reference existing viewsets

### Common Quick Fixes
1. **Add missing fviews layer** - Most common issue
2. **Add name parameters** - Second most common
3. **Fix component namespaces** - Check designer-component-mapping
4. **Remove trailing commas** - JSON syntax
5. **Add HRID field** - For readable identifiers

---

## Error Prevention Tips

### Design Phase
1. Start with a working template
2. Add fields incrementally
3. Test after each major change
4. Keep sections small (<10 fields)

### Development Phase
1. Validate JSON frequently
2. Test on target platform early
3. Check all conditional logic paths
4. Verify all references

### Deployment Phase
1. Test on all target devices
2. Verify offline functionality
3. Check performance with real data
4. Validate all required fields work

---

## Related Documentation

### Core References
- [Notebook Format Guide](./notebook-format-guide.md) - Complete structure requirements
- [Complete Notebook Templates](./notebook-templates.md) - Working examples
- [Designer Component Mapping](./designer-component-mapping.md) - Component reference
- [Platform Reference](./platform-reference.md) - Platform-specific issues
- [Constraints Reference](./constraints-reference.md) - System limitations

### Editor Configuration
- {{cross-ref:editor-form-settings}} - Form Settings troubleshooting source
- {{cross-ref:editor-notebook-info}} - Notebook Info troubleshooting source
- {{cross-ref:roles-permissions-reference}} - Permission issues source

### Patterns and Guides
- [Dynamic Forms Guide](../patterns/dynamic-forms-guide.md) - Validation and conditional logic
- [Form Structure Guide](../patterns/form-structure-guide.md) - Form architecture issues

---

## Getting Help

If these solutions don't resolve your issue:
1. Check the specific field documentation in field-categories/
2. Review working examples in working-notebooks/
3. Consult platform-reference for device-specific issues
4. Check constraints-reference for system limitations

Remember: Most import failures are due to:
- Missing fviews layer (50% of cases)
- Missing name parameters (30% of cases)  
- JSON syntax errors (15% of cases)
- Wrong component names (5% of cases)

---

*This troubleshooting index covers ~95% of common Fieldmark notebook issues.*