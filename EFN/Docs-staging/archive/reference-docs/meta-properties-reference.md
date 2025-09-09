<!-- DEPRECATED: This document has been consolidated into references/component-reference.md -->
<!-- Archived: 2025-01-06 for disaster recovery only -->
<!-- DO NOT UPDATE: Make changes to the consolidated guide instead -->

# Meta Properties Reference
## Universal Metadata Configuration for All Fieldmark v3 Fields

### Overview

The `meta` property provides standardized metadata options that work identically across ALL field types. These properties control annotations, uncertainty markers, persistence, and display behaviors.

### Standard Meta Structure

```json
{
  "field-name": {
    "component-namespace": "...",
    "component-name": "...",
    "type-returned": "...",
    "component-parameters": {...},
    "validationSchema": [...],
    "initialValue": "...",
    "meta": {
      "annotation": {
        "include": true,
        "label": "Notes"
      },
      "uncertainty": {
        "include": true,
        "label": "Uncertain"
      },
      "persistent": false,
      "displayParent": false
    }
  }
}
```

### Meta Properties Explained

#### annotation
**Purpose**: Adds a free-text notes field alongside the main field

**Structure**:
```json
"annotation": {
  "include": true,    // Boolean: whether to show annotation field
  "label": "Notes"    // String: label for the annotation field
}
```

**Behavior**:
- Creates an additional text input below the main field
- Stores text in a parallel data structure
- Exports as separate column in CSV
- No validation applied to annotation text
- No character limit

**Common Labels**:
- "Notes" - General purpose
- "Comments" - General purpose
- "Annotation" - Default if label omitted
- "[Field] notes" - Context-specific (e.g., "Location notes")
- "Additional information" - Verbose option

#### uncertainty
**Purpose**: Adds a checkbox to mark data as uncertain/questionable

**Structure**:
```json
"uncertainty": {
  "include": true,        // Boolean: whether to show uncertainty checkbox
  "label": "Uncertain"    // String: label for the checkbox
}
```

**Behavior**:
- Creates a checkbox beside/below the main field
- Stores boolean value in parallel structure
- Exports as separate boolean column
- When checked, may trigger visual indicators (field-dependent)
- No validation impact (uncertain data still validates)

**Common Labels**:
- "Uncertain" - Default
- "?" - Minimal
- "Questionable" - Explicit
- "Approximate" - For measurements
- "Needs verification" - Process-oriented
- "Low confidence" - Confidence scale

#### persistent
**Purpose**: Controls whether field value persists across record creation

**Values**:
- `true` - Field retains value when creating new record
- `false` - Field clears to initialValue (default)

**Structure**:
```json
"persistent": true  // or false
```

**Use Cases for persistent: true**:
- Location fields (likely same site)
- Date fields (same day's work)
- Team member fields
- Project phase fields
- Site/area identifiers

**Use Cases for persistent: false**:
- Unique identifiers
- Measurements
- Observations
- Photos
- Specimen data

#### displayParent
**Purpose**: Shows parent record context in related record forms

**Values**:
- `true` - Display parent record information
- `false` - Hide parent context (default)

**Structure**:
```json
"displayParent": true  // or false
```

**Behavior**:
- Only relevant for fields in child records
- Shows parent record's human-readable ID
- Helps maintain context during data entry
- No impact on data storage

### Designer Integration

The Designer interface provides toggles for:
- **Annotation** - Maps to `meta.annotation.include`
- **Uncertainty** - Maps to `meta.uncertainty.include`

The Designer does NOT provide controls for:
- Custom annotation labels (uses "Annotation")
- Custom uncertainty labels (uses "?")
- `persistent` property
- `displayParent` property

These require JSON editing.

### Default Values

If `meta` property is omitted entirely:
```json
// These defaults are applied:
"meta": {
  "annotation": {"include": false},
  "uncertainty": {"include": false},
  "persistent": false,
  "displayParent": false
}
```

### Partial Specification

You can specify only needed properties:
```json
// Only annotation:
"meta": {
  "annotation": {"include": true, "label": "Field notes"}
}

// Only persistence:
"meta": {
  "persistent": true
}

// Multiple properties:
"meta": {
  "annotation": {"include": true, "label": "Comments"},
  "persistent": true
}
```

### Data Storage

#### Database Storage
Meta properties create parallel data structures:
```json
{
  "field-name": "actual value",
  "field-name_annotation": "annotation text",
  "field-name_uncertainty": true/false
}
```

#### CSV Export
Each meta property creates additional columns:
- Main field: `field-name`
- Annotation: `field-name_annotation`
- Uncertainty: `field-name_uncertainty`

#### JSON Export
Preserves full structure with meta values inline.

### Common Patterns

#### Field with Full Meta
```json
{
  "species-identification": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Species",
      "ElementProps": {"options": [...]}
    },
    "meta": {
      "annotation": {"include": true, "label": "Identification notes"},
      "uncertainty": {"include": true, "label": "Tentative ID"},
      "persistent": false
    }
  }
}
```

#### Persistent Configuration Fields
```json
{
  "team-member": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Recording Team Member",
      "ElementProps": {"options": [...]}
    },
    "meta": {
      "persistent": true  // Keeps value for next record
    }
  }
}
```

#### Measurement with Uncertainty
```json
{
  "artifact-length": {
    "component-namespace": "faims-custom",
    "component-name": "NumberField",
    "type-returned": "faims-core::Number",
    "component-parameters": {
      "label": "Length (mm)"
    },
    "meta": {
      "uncertainty": {"include": true, "label": "Approximate"},
      "annotation": {"include": true, "label": "Measurement notes"}
    }
  }
}
```

### Field Type Compatibility

Meta properties work with ALL field types:
- ✅ Text fields (all variants)
- ✅ Number fields (all variants)
- ✅ DateTime fields (all variants)
- ✅ Selection fields (all variants)
- ✅ Media fields (all variants)
- ✅ Location fields (all variants)
- ✅ Relationship fields

### Display Behavior

#### Annotation Field Placement
- Usually appears below main field
- Full width of container
- Multi-line text input
- No character counter
- No validation indicators

#### Uncertainty Checkbox Placement
- Typically right-aligned
- Same row as field label (desktop)
- Below field (mobile)
- May show warning icon when checked

### Performance Considerations

- Meta properties have minimal performance impact
- Annotation fields add ~2KB per field to payload
- Uncertainty adds ~10 bytes per field
- Persistent fields require state management overhead
- No impact on validation performance

### Best Practices

#### When to Use Annotations
- Fields requiring explanation
- Subjective observations
- Exceptional cases
- Quality notes
- Method descriptions

#### When to Use Uncertainty
- Estimated measurements
- Tentative identifications
- Incomplete data
- Conflicting information
- Low-confidence observations

#### When to Use Persistent
- Site/context that continues across records
- Team members recording multiple items
- Date when recording in single session
- Equipment/method that remains constant

#### When NOT to Use Persistent
- Unique identifiers
- Measurements that vary
- Observations that change
- Auto-generated values
- Photos/media

### Common Issues

#### Annotation Text Lost
- **Cause**: Field name changed
- **Fix**: Annotation stored with field name key

#### Uncertainty Not Showing
- **Cause**: Missing include property
- **Fix**: Set `"include": true`

#### Persistent Not Working
- **Cause**: Form reset between records
- **Fix**: Check form submission mode

#### Labels Not Updating
- **Cause**: Designer overwrites on save
- **Fix**: Edit JSON after Designer save

### Migration Notes

#### From Older Versions
- v1-v2: `annotation: true` → `annotation: {"include": true}`
- v2-v3: No changes to meta structure

#### Designer Round-Trip
Designer preserves JSON meta properties it doesn't understand, but:
- Resets custom labels to defaults
- Ignores persistent/displayParent
- May reorder properties

### Related Documentation
- Field-specific documentation for display variations
- Export documentation for CSV column naming
- Validation reference (meta properties don't affect validation)

### Version
Last updated: 2025-09-03
Applies to: Fieldmark v3 (all versions)
Meta structure version: 1.0 (stable since v2)