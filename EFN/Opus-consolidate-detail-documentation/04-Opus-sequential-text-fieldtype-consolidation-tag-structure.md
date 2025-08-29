# Add Structure and Tags to Deduplicated Document

Take the deduplicated document and add final organization and tagging.

## Instructions

### 1. Apply This Structure

```
# [Text] Input Fields

## Overview {essential}
## Field Selection Guide {essential}
## Common Characteristics
### Shared Limitations {important}
### Common Validation Patterns {important}
### Platform Behaviors {important}
### Performance Boundaries {important}
## Individual Field Reference
### [Field1 Name] {essential}
### [Field2 Name] {essential}
### [etc...]
## Troubleshooting Guide {important}
## JSON Examples {important}
## Migration and Best Practices {comprehensive}
```

### 2. Add Depth Tags

Apply to ALL sections and major subsections:
- `{essential}` - Must know to use the field
- `{important}` - Should know for effective use
- `{comprehensive}` - Complete reference details

**Tagging Guidelines**:
- Field names and overview: {essential}
- Common issues and troubleshooting: {important}
- Advanced configurations and edge cases: {comprehensive}

### 3. Add Field Metadata

For each field in Individual Field Reference:
```
### FieldName {essential}
<!-- keywords: [relevant, search, terms, 3-5 words] -->
```

Examples:
- TextField: `<!-- keywords: single-line, text, input, brief -->`
- NumberField: `<!-- keywords: numeric, decimal, validation, range -->`

### 4. Verify Critical Information Prominence

Ensure these are highly visible:
- Security vulnerabilities (near top with ⚠️ warning)
- Platform limitations (e.g., mobile-only features)
- Beta/experimental status
- Performance thresholds with specific numbers

## Quality Checks
- [ ] Every section has at least one depth tag
- [ ] All field names tagged {essential}
- [ ] Keywords added for each field
- [ ] Security warnings prominent
- [ ] Structure matches template exactly
- [ ] No content lost during restructuring

## DO NOT
- ❌ Change content (only add tags and structure)
- ❌ Skip sections when applying tags
- ❌ Move content between sections
- ❌ Remove anything that seems redundant

Output the structured and tagged document.