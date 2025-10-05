<!-- concat:boundary:start section="relationship-fields" -->
<!-- concat:metadata
document_id: relationship-field-v05
category: relationship
field_count: 1
designer_capable: ["RelationshipField"]
json_only: ["complex_rules", "cascading_relationships"]
last_updated: 2025-01-05
-->

<!-- discovery:metadata
provides: [record-relationships, parent-child, peer-links, access-control]
see-also: [form-structure-guide, dynamic-forms-guide]
-->


# Relationship Field - Fieldmark v3 Documentation


<!-- structured:metadata
meta:purpose: field-configuration
meta:summary: RelationshipField for complex record linking with performance limits and hierarchical structure support.
meta:generates: json-fields
meta:requires: [valid-json, unique-names, fviews-layer]
meta:version: 3.0.0
meta:document: relationship_field
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Media Fields](./media-fields-v05.md) | **Relationship Fields** | [Field Index →](../field-type-index.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) -->


## Overview {essential}

### DESIGNER QUICK GUIDE
**Relationship Field Available:**
- **RelatedRecordSelector** → Connect records with bidirectional relationships
## Component Mapping Reference {essential}

For the complete mapping between Designer field names and JSON component implementations, see:
→ **[Designer UI to Component Mapping Reference](../references/designer-component-mapping.md)**

This central reference provides:
- Exact component names and namespaces for all fields
- Configuration requirements and examples
- Common mapping errors and solutions


## Designer Usage Guide {essential}

### What to Select in Designer
1. Navigate to Field Type selection
2. Choose "Custom Field" category
3. Select "RelatedRecordSelector"
4. Configure available properties:
   - Label and name
   - Related form type
   - Relationship type (Child/Linked)
   - Multiple selection toggle

### When JSON Enhancement is Required
**JSON-only parameters:**
- `relation_linked_vocabPair` - Vocabulary pairs for qualified relationships
- `allowLinkToExisting` - Enable/disable linking to existing records
- `related_type_label` - Human-readable form name
- Complex validation schemas
- Performance optimizations

### Designer Limitations {important}
See [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) for universal constraints.

**Relationship-Specific Designer Limitations:**
- Cannot configure vocabulary pairs for custom relationship labels (JSON only)
- Cannot preview relationships in Designer (must test in web app)
- No test data available (must create real records to test)
- Cannot configure branding or some advanced parameters

## Field Selection Guide {essential}

### When to Use RelatedRecordSelector
RelatedRecordSelector is the **only** relationship field option in Fieldmark. Use it when you need to:
- **Connect two forms/entities** - Link records that reference each other
- **Create hierarchical structures** - Build parent-child relationships (e.g., Site→Trench→Context)
- **Establish associations** - Connect peer records with qualified relationships
- **Track provenance** - Link samples to their sources
- **Document relationships** - Record how entities relate to each other

**Not suitable for:**
- Simple categorization (use Select fields instead)
- Temporal sequences (use DateTime fields with proper ordering)
- Spatial relationships only (use Location fields with coordinates)
- File attachments (use Media fields)

### Choosing Your Relationship Type
```
Need to connect records?
├─ Parent owns children?
│  └─ YES → Child relationship
│     ├─ Cascade: Orphans on delete
│     ├─ Exclusive: One parent only
│     └─ Best for: Site→Trench→Context
│
└─ Equal partnership?
   └─ YES → Linked relationship (is-related-to)
      ├─ Cascade: No deletion impact
      ├─ Vocabulary: Qualified labels
      └─ Best for: Stratigraphic relations
```

### Relationship Type Matrix
| Aspect | Child | Linked (is-related-to) |
|--------|-------|-------------------------|
| Hierarchy | Parent→Child | Peer↔Peer |
| Deletion | Creates orphans | No impact |
| Vocabulary | Fixed labels | Custom pairs |
| Cardinality | 1:N typical | N:N typical |
| Use Case | Site structure | Stratigraphic |

### Vocabulary Pairs for Linked Relationships
**Bidirectional labeling (JSON-only configuration):**
```json
// Example relationship-field-01
{
  "relation_linked_vocabPair": [
    ["cuts", "is cut by"],
    ["fills", "is filled by"],
    ["is above", "is below"],
    ["same as", "same as"]
  ]
}
```
- First element: Forward label (shown in current record)
- Second element: Reverse label (shown in related record)
- Immutable after relationship creation
- Must be configured before first use

## ⚠️ Critical Security Risks {essential}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for general security patterns.

**Relationship-Specific Security Concerns:**
- **No access control** - Any user can modify any relationship
- **Orphan creation** - Deleting parents leaves orphaned children
- **No cascade delete** - Manual cleanup required
- **Sync conflicts** - Simultaneous edits can corrupt relationships
- **Data exposure** - All relationships visible to all users

**Critical Performance Risks:**
- **<20 relationships**: Optimal performance
- **20-50 relationships**: Acceptable with minor lag
- **50-100 relationships**: Noticeable delays, UI sluggish
- **100-200 relationships**: Severe degradation
- **200+ relationships**: Essentially unusable

**Mitigation Requirements:**
- Split into multiple focused fields for performance
- Document deletion procedures to prevent orphans
- Implement access policies through training
- Archive historical relationships regularly
- Consider alternative designs for large datasets

## What This Field Cannot Do {important}
- **Prevent circular relationships** - A→B→C→A allowed
- **Modify vocabulary after creation** - Immutable once used
- **Validate relationship counts** - No array.length access
- **Show reciprocals immediately offline** - Sync required
- **Handle 200+ relationships** - Performance collapse
- **Auto-cleanup orphans** - Manual intervention needed
- **Provide conflict resolution** - Last-write-wins only
- **Support gesture controls** - No swipe/drag actions in UI

## Common Use Cases {important}
- **Site hierarchies** - Site→Trench→Context→Find structures
- **Stratigraphic documentation** - Cuts/filled by relationships
- **Sample associations** - Linking samples to contexts
- **Feature relationships** - Spatial/temporal connections
- **Cross-cutting associations** - Across hierarchical branches
- **Find assemblages** - Grouping related artifacts
- **Specialist analysis** - Primary→specialist records

## Designer Component Mapping {essential}

### Designer UI vs JSON Component Names

| Designer UI Label | JSON component-name | Component Namespace | Description |
|------------------|--------------------|--------------------|-------------|
| RelatedRecordSelector | RelatedRecordSelector | faims-custom | Bidirectional record relationships |

### Designer Configuration Options

| Designer Option | JSON Parameter | Values | Description |
|----------------|----------------|---------|-------------|
| Related Form | `related_type` | Form viewset ID | Target form for relationships |
| Relationship Type | `relation_type` | "Child" or "is-related-to" | Hierarchical vs peer relationships |
| Allow Multiple | `multiple` | true/false | Single or multiple relationships |
| Allow Link to Existing | `allowLinkToExisting` | true/false | Enable linking vs only creation |
| Required | Via validation schema | yup.required | Must be set with validation |

⚠️ **Critical Notes**:
- Only one relationship field type exists (RelatedRecordSelector)
- Vocabulary pairs for "is-related-to" require JSON editing
- Performance degrades severely beyond 50 relationships
- Reciprocal updates only occur after synchronization

## Designer Capabilities vs JSON Enhancement {comprehensive}

### Designer Configuration
- ✅ Field label and name
- ✅ Related form selection
- ✅ Relationship type (Child/Linked dropdown)
- ✅ Multiple selection toggle
- ✅ Allow linking to existing records toggle
- ✅ Related Type Label field
- ✅ Helper text (basic and advanced)
- ✅ Required flag
- ✅ Display in child records option

### JSON-Only Configuration
```json
// Example relationship-field-02
{
  "relation_linked_vocabPair": [
    ["forward", "reverse"]  // Custom relationship labels
  ],
  "branding": {},          // Advanced branding options
  "initialValue": []       // Pre-selected relationships
}
```

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

**Common Relationship Errors:**
- Using incorrect component names (e.g., "RelationshipField")
- Wrong case in component name (must be exact: "RelatedRecordSelector")
- Missing related_type parameter


## When to Use This Field {essential}

### Use RelatedRecordSelector When
- Linking parent records to child records (hierarchical data)
- Creating associations between peer records (many-to-many)
- Building specimen/sample hierarchies
- Connecting related observations

### Do NOT Use RelatedRecordSelector When
- You have >50 relationships per record (performance degrades)
- Relationships might exceed 200 (becomes unusable)
- You need one-way relationships (always bidirectional)
- Simple foreign key reference sufficient (use Select instead)

### Relationship Type Selection
- **Child**: Hierarchical parent-child with cascade operations
- **is-related-to**: Peer relationships with semantic vocabulary

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Relationship-Specific Security Notes:**
- Access control at notebook level (not field-specific)
- Users with edit permissions can modify all relationships
- Read-only users cannot modify any relationships
- Soft-delete preserves data trail
- Changes tracked via PouchDB revision history

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for general limits.

**Relationship-Specific Performance:**
- **Query time**: Linear with relationship count
- **Render time**: 100ms per 10 relationships
- **Memory usage**: ~10KB per relationship
- **Sync payload**: Grows exponentially
- **Mobile impact**: 2x slower than desktop

### Validation Patterns {important}
See [Validation System Documentation](../detail-crossfield-docs/validation.md) for comprehensive validation patterns and timing.

**Relationship Field-Specific Validation:**
- **Type depends on `multiple`**: Array validation when `multiple=true`, String when `false`
- **Reciprocal validation**: Only occurs after sync (delayed)
- **Performance limits**: Use `yup.max` to enforce <50 relationships
- **No error display**: RelatedRecordSelector doesn't show validation messages (known bug)

### Platform Behaviors {important}
See [Platform Behaviors Reference](../reference-docs/platform-behaviors-reference.md) for general platform characteristics.

**Relationship Field-Specific Behaviors:**
- **iOS**: Touch targets 36px (below WCAG); scroll momentum issues; modal height limited to 70%
- **Android**: 20% worse performance than iOS; 200ms autocomplete lag; back button closes modal
- **Web**: Best performance for large sets; partial keyboard navigation; hover shows full HRID
- **Mobile**: Viewport constraints; keyboard obscures content; faster performance degradation

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.

Relationships support annotations and uncertainty:
- Annotation: Document relationship rationale
- Uncertainty: Flag tentative associations

### Export Behaviour {important}
See [Data Export Reference](../reference-docs/data-export-reference.md) for universal patterns.

**Relationship-Specific Export:**
- **CSV Format**: `{label}/{record_id}` semicolon-separated
- **Example**: `"cuts/ctx043;fills/ctx044"`
- **No hierarchy preservation**: Flattened structure
- **No re-import capability**: Manual reconstruction
- **JSON not available**: Despite internal storage

## Field Reference {essential}

### RelatedRecordSelector {essential}

#### Purpose {essential}
Enables bidirectional connections between records, supporting both hierarchical parent-child relationships and semantic peer associations with qualified vocabulary pairs. Maintains data coherence through automatic reciprocal updates within distributed architecture.

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | `faims-custom::RelatedRecordSelector` |
| Returns | `faims-core::Array` |
| Designer | ⚠️ Limited support |
| JSON Required | Vocabulary pairs |
| Performance Limit | 50 relationships |
| Offline Behaviour | Delayed reciprocals |
| Touch Target | 36px (suboptimal) |
| Cascade Delete | Orphans (Child only) |

#### Core Configuration
```json
// Example relationship-field-03
// Template markers added for parametric generation
{
  "component-namespace": "faims-custom",
  "component-name": "RelatedRecordSelector",
  "type-returned": "faims-core::Array",
  "component-parameters": {
    "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
    "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
    "related_type": "TargetFormID",
    "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
    "multiple": true,
    "required": false,
    "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
  },
  "validationSchema": [["yup.array"]],
  "initialValue": []
}
```

#### Advanced Configuration
```json
// Example relationship-field-04
// Template markers added for parametric generation
{
  "stratigraphic_relationships": {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Context",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": true,
      "related_type_label": "Context Record",
      "relation_linked_vocabPair": [
        ["cuts", "is cut by"],
        ["fills", "is filled by"],
        ["is above", "is below"],
        ["abuts", "abuts"],
        ["same as", "same as"],
        ["contemporary with", "contemporary with"]
      ],
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "At least one relationship required"]
    ],
    "initialValue": [],
    "meta": {
      "annotation": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      },
      "uncertainty": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    }
  }
}
```

#### Platform-Specific Behaviors
- **Desktop**: Full autocomplete, easier selection
- **Mobile**: Constrained viewport, difficult search
- **Offline**: No reciprocal updates until sync
- **All**: Sequential metadata fetching causes lag

#### Common Issues & Solutions
| Issue | Cause | Solution |
|-------|-------|----------|
| Performance lag | >50 relationships | Split into multiple fields |
| No reciprocals | Offline operation | Wait for sync |
| Cannot change vocabulary | Immutable design | Plan carefully |
| Orphaned records | Parent deletion | Manual cleanup |
| Touch targets small | 36px height | Use desktop for complex work |

## Troubleshooting Guide {important}

### Issue 1: Severe Performance Degradation
**Symptoms**: UI becomes sluggish, selection modal slow to open, app may freeze

**Diagnosis Steps**:
1. Count total relationships in the field
2. Check if approaching 50 relationship threshold
3. Monitor browser/app memory usage
4. Test on different device to isolate issue

**Performance Thresholds**:
- **<20 relationships**: Optimal performance
- **20-50 relationships**: Noticeable slowdown
- **50-100 relationships**: Severe degradation
- **100-200 relationships**: Nearly unusable
- **>200 relationships**: App crashes likely

**Solutions**:
1. Split into multiple relationship fields by category
2. Archive completed relationships regularly
3. Use hierarchical Child relationships instead of flat lists
4. Consider external reference system for large networks

### Issue 2: Reciprocal Updates Not Appearing
**Symptoms**: Related record doesn't show reverse relationship

**Root Cause**: Offline mode delays reciprocal updates until sync

**Diagnosis**:
- Check sync status indicator
- Verify both records have been synced
- Confirm vocabulary pair configuration
- Test with forced sync

**Solutions**:
1. **Immediate**: Force sync and refresh both records
2. **Workaround**: Document relationships externally while offline
3. **Prevention**: Sync before major relationship changes
4. **Training**: Explain delayed reciprocals to users

### Issue 3: Orphaned Records After Deletion
**Symptoms**: Child records exist without parent, shown as "orphaned"

**Understanding the Behaviour**:
- Deleting parent with Child relationships creates orphans
- Orphaned records remain in database
- No automatic cascade delete
- Orphans marked but not removed

**Solutions**:
1. **Manual cleanup**: Delete orphans individually
2. **Reassignment**: Link orphans to new parent
3. **Prevention**: Delete children before parent
4. **Policy**: Document deletion procedures

### Issue 4: Cannot Find Records to Link
**Symptoms**: Known records don't appear in selection modal

**Common Causes**:
1. **No HRID**: Records without TemplatedString field won't display properly
2. **Wrong form type**: Checking incorrect related_type
3. **Not synced**: New records not yet synchronized
4. **Search syntax**: Autocomplete requires exact HRID prefix

**Solutions by Cause**:
- **Missing HRID**: Add TemplatedString field to related form
- **Wrong type**: Verify related_type matches target form
- **Sync issue**: Force sync and retry
- **Search issue**: Use exact HRID format (case-sensitive)

### Issue 5: Validation Errors Not Clear
**Symptoms**: Form won't submit but no clear error on relationship field

**Diagnosis Checklist**:
- [ ] Check if field marked as required
- [ ] Verify multiple setting matches validation schema
- [ ] Count relationships against any max validation
- [ ] Test with single vs array validation

**Common Validation Issues**:
```json
// Example relationship-field-05
{
  "WRONG_example": {
    "comment": "Single relationship with array validation - MISMATCH",
    "multiple": false,
    "validationSchema": [["yup.array"]]
  },
  "CORRECT_single": {
    "comment": "Single relationship - correct validation",
    "multiple": false,
    "validationSchema": [["yup.string"]]
  },
  "CORRECT_multiple": {
    "comment": "Multiple relationships - correct validation",
    "multiple": true,
    "validationSchema": [["yup.array"]]
  }
}
```
4. Review sync payload size
5. Consider field splitting

### Data Integrity
- Document deletion procedures
- Plan orphan cleanup
- Coordinate auto-incrementer ranges
- Test offline workflows
- Establish conflict protocols

### Configuration Problems
- Verify exact viewset IDs
- Check TemplatedString HRIDs
- Confirm vocabulary pairs before use
- Test on all platforms
- Document team procedures

## JSON Examples {comprehensive}

### Example 1: Basic Parent-Child Hierarchy
```json
// Example relationship-field-06
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Context",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": false
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

### Example 2: Required Single Parent
```json
// Example relationship-field-07
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Trench",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": false,
      "required": true,
      "allowLinkToExisting": true,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.Parent trench required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
    ],
    "initialValue": null
  }
}
```

### Example 3: Stratigraphic Relationships with Vocabulary
```json
// Example relationship-field-08
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Context",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": true,
      "relation_linked_vocabPair": [
        ["cuts", "is cut by"],
        ["fills", "is filled by"],
        ["is above", "is below"],
        ["abuts", "abuts"],
        ["same as", "same as"]
      ],
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

### Example 4: Find Assemblage Grouping
```json
// Example relationship-field-09
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Find",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": true,
      "relation_linked_vocabPair": [
        ["part of set", "includes"],
        ["matches", "matches"],
        ["associated with", "associated with"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": [],
    "meta": {
      "annotation": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    }
  }
}
```

### Example 5: Sample Chain of Custody
```json
// Example relationship-field-10
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Sample",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "relation_linked_vocabPair": [
        ["subsample of", "has subsample"],
        ["split from", "split into"],
        ["control for", "controlled by"],
        ["duplicate of", "duplicate of"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

### Example 6: Site-Trench-Context Hierarchy
```json
// Example relationship-field-11
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Trench",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": false,
      "related_type_label": "Trench Record",
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

### Example 7: Feature Cross-References
```json
// Example relationship-field-12
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Feature",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": true,
      "relation_linked_vocabPair": [
        ["built on", "supports"],
        ["replaces", "replaced by"],
        ["contemporary with", "contemporary with"],
        ["connected to", "connected to"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

### Example 8: Specialist Analysis Links
```json
// Example relationship-field-13
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Analysis",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": false,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [["yup.array"]],
    "initialValue": [],
    "meta": {
      "annotation": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    }
  }
}
```

### Example 9: Conditional Parent Requirement
```json
// Example relationship-field-14
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Structure",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": false,
      "allowLinkToExisting": true,
      "required": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.Parent structure required", "{VALIDATION_MESSAGE}"]  // CUSTOMIZE: error message
    ],
    "initialValue": null,
    "condition": {
      "operator": "equal",
      "field": "element-type",
      "value": "structural-element"
    }
  }
}
```

### Example 10: Documentation Attachments
```json
// Example relationship-field-15
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Document",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "relation_linked_vocabPair": [
        ["documented in", "documents"],
        ["referenced in", "references"],
        ["illustrated in", "illustrates"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

### Example 11: Survey Unit Hierarchy
```json
// Example relationship-field-16
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "SurveyUnit",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": false,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "At least one survey unit required"]
    ],
    "initialValue": []
  }
}
```

### Example 12: Temporal Relationships
```json
// Example relationship-field-17
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Phase",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "relation_linked_vocabPair": [
        ["earlier than", "later than"],
        ["contemporary with", "contemporary with"],
        ["transitions to", "transitions from"],
        ["overlaps with", "overlaps with"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

### Example 13: Performance-Limited Configuration
```json
// Example relationship-field-18
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Record",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.max", 30, "Maximum 30 relationships allowed"]
    ],
    "initialValue": []
  }
}
```

### Example 14: Excavation Team Assignment
```json
// Example relationship-field-19
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Person",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "allowLinkToExisting": true,
      "relation_linked_vocabPair": [
        ["excavated by", "excavated"],
        ["recorded by", "recorded"],
        ["supervised by", "supervised"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

### Example 15: Conservation Treatment Chain
```json
// Example relationship-field-20
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Treatment",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "relation_linked_vocabPair": [
        ["treated with", "applied to"],
        ["follows", "precedes"],
        ["reverses", "reversed by"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": [],
    "meta": {
      "annotation": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    }
  }
}
```

### Example 16: Interpretive Associations
```json
// Example relationship-field-21
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Interpretation",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "relation_linked_vocabPair": [
        ["interpreted as", "interpretation of"],
        ["supports interpretation", "supported by"],
        ["contradicts", "contradicted by"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": [],
    "meta": {
      "uncertainty": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    }
  }
}
```

### Example 17: Conditional Relationship Field
```json
// Example relationship-field-22
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Sample",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "related_type_label": "Analysis Sample",
      "allowLinkToExisting": false
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "At least one sample required"]
    ],
    "condition": {
      "operator": "equal",
      "field": "requires-analysis",
      "value": "yes"
    },
    "initialValue": []
  }
}
```

### Example 18: Cross-Referenced Features
```json
// Example relationship-field-23
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Feature",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "relation_linked_vocabPair": [
        ["references", "referenced by"],
        ["supersedes", "superseded by"],
        ["duplicates", "duplicates"],
        ["contradicts", "contradicted by"],
        ["supports", "supported by"]
      ],
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.max", 50, "Maximum 50 relationships for performance"]
    ],
    "initialValue": []
  }
}
```

### Example 19: Equipment Assignment Tracking
```json
// Example relationship-field-24
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Equipment",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "relation_linked_vocabPair": [
        ["used equipment", "used in operation"],
        ["borrowed", "loaned to"],
        ["damaged", "damaged during"]
      ],
      "allowLinkToExisting": true,
      "advancedHelperText": "## Equipment Protocol\n\n- Log all equipment at start of day\n- Note any damage immediately\n- Update if equipment changed"
    },
    "validationSchema": [["yup.array"]],
    "meta": {
      "annotation": {
        "include": true,
        "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label
      }
    },
    "initialValue": []
  }
}
```

### Example 20: Publication Citations Network
```json
// Example relationship-field-25
// Template markers added for parametric generation
{
  "{{FIELD_ID}}"  // REPLACE: unique field identifier: {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier,
      "label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label,
      "related_type": "Publication",
      "relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type,
      "multiple": true,
      "relation_linked_vocabPair": [
        ["cites", "cited by"],
        ["responds to", "response from"],
        ["builds upon", "foundation for"],
        ["critiques", "critiqued by"],
        ["corroborates", "corroborated by"]
      ],
      "helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```

## Migration Scenarios {comprehensive}

### Scenario 1: Performance Scaling - Splitting Large Relationship Sets
**Context**: A project's relationship field has grown beyond the 50-relationship performance threshold, causing severe UI lag on mobile devices.

**Challenge**: 
- Single field with 100+ relationships causes 2-3 second delays
- Mobile devices experiencing crashes
- Sync operations timing out

**Migration Steps**:
1. Export existing relationships to CSV for backup
2. Create multiple relationship fields with semantic groupings:
   ```json
// Example relationship-field-26
   {
     "primary-relationships": { 
       "multiple": true, 
       "relation_linked_vocabPair": [["primary", "primary of"]] 
     },
     "secondary-relationships": { 
       "multiple": true, 
       "relation_linked_vocabPair": [["secondary", "secondary of"]] 
     }
   }
   ```
3. Manually redistribute relationships across new fields
4. Add validation to enforce maximum of 50 per field
5. Update form documentation with new field organisation

**Solution/Workaround**: Split relationships into semantically meaningful groups (e.g., "direct-relationships", "indirect-relationships") with clear documentation of the separation criteria.

### Scenario 2: Vocabulary Restructuring
**Context**: Project needs to change relationship vocabulary pairs after deployment, but vocabulary is immutable once relationships exist.

**Challenge**:
- Vocabulary pairs cannot be modified after first use
- Existing relationships would be lost if field deleted
- No built-in migration tool for vocabulary changes

**Migration Steps**:
1. Create new relationship field with corrected vocabulary
2. Document mapping between old and new vocabulary terms
3. Export all existing relationships
4. Manually recreate relationships with new field
5. Hide (but don't delete) old field to preserve history

**Solution/Workaround**: Run parallel fields during transition period, then hide old field via conditions once migration complete.

### Scenario 3: Hierarchy Flattening
**Context**: Deep hierarchical relationships (5+ levels) are causing performance issues and user confusion.

**Challenge**:
- Deep hierarchies exponentially increase query complexity
- Mobile devices struggle with nested displays
- Users lose context in deep trees

**Migration Steps**:
1. Map existing hierarchy to flattened structure
2. Replace Child relationships with is-related-to
3. Use vocabulary pairs to maintain semantic relationships:
   ```json
// Example relationship-field-27
   "relation_linked_vocabPair": [
     ["contains", "contained by"],
     ["parent of", "child of"]
   ]
   ```
4. Update queries and reports for flattened structure
5. Retrain users on new relationship model

**Solution/Workaround**: Maintain hierarchy semantically through vocabulary while using flat is-related-to structure.

### Scenario 4: Orphan Cleanup After Mass Deletions
**Context**: Bulk deletion of parent records has left numerous orphaned child records in the database.

**Challenge**:
- No automatic cascade delete
- Orphaned records clutter search results
- Performance degradation from unused records
- No built-in orphan detection

**Migration Steps**:
1. Export all records to identify orphans
2. Create cleanup script to identify records with null parents
3. Document orphan handling policy
4. Implement regular cleanup routine
5. Add pre-deletion checklist to prevent future orphans

**Solution/Workaround**: Implement monthly orphan cleanup routine with documentation of deletion criteria.

### Scenario 5: Converting Between Child and Linked Relationships
**Context**: Project needs to convert Child relationships to is-related-to for flexibility.

**Challenge**:
- Child relationships have different data structure
- Reciprocal relationships need manual recreation
- Loss of hierarchical context

**Migration Steps**:
1. Export all Child relationships
2. Create new is-related-to field with appropriate vocabulary
3. Import relationships with new structure
4. Update all queries expecting Child type
5. Test bidirectional relationship integrity

**Solution/Workaround**: Maintain hierarchical semantics through careful vocabulary design while using flexible is-related-to structure.

## Best Practices {comprehensive}

### Design Principles
- **Shallow hierarchies**: Maximum 3-4 levels
- **Relationship limits**: Stay under 50
- **Vocabulary planning**: Cannot modify later
- **HRID configuration**: Always include TemplatedString
- **Deletion procedures**: Document orphan handling

### Offline Coordination
- Allocate auto-incrementer ranges
- Document sync procedures
- Plan conflict resolution
- Test offline workflows
- Understand reciprocal delays

### Performance Optimization
- Split complex relationships
- Monitor mobile performance
- Implement cleanup routines
- Consider alternatives for large datasets
- Test on lowest-spec devices

### Relationship Management
- Regular orphan cleanup schedules
- Performance monitoring dashboards
- Vocabulary documentation standards
- Relationship limit enforcement
- User training on best practices

## Field Quirks Index (2025-01-03) {comprehensive}
- Vocabulary pairs immutable after use
- Reciprocals delayed until sync
- Performance cliff at 50 relationships
- Touch targets below WCAG standards
- No circular relationship prevention
- Orphans on parent deletion
- No gesture controls
- Autocomplete by HRID only

## Performance Thresholds Summary {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for detailed metrics.

**Relationship-Specific Thresholds:**
| Metric | Value | Impact |
|--------|-------|---------|
| Optimal | <20 | Smooth operation |
| Acceptable | 20-50 | Minor lag |
| Degraded | 50-100 | Noticeable delays |
| Severe | 100-200 | Very slow |
| Unusable | >200 | System failure |

## JSON Patterns Cookbook (2025-01-03) {comprehensive}

### Pattern: Conditional Relationships
```json
// Example relationship-field-28
{
  "condition": {
    "operator": "is",
    "field": "needs_relationships",
    "value": "yes"
  }
}
```

### Pattern: Validation Enforcement
```json
// Example relationship-field-29
{
  "validationSchema": [
    ["yup.array"],
    ["yup.min", 1, "Required"],
    ["yup.max", 50, "Performance limit"]
  ]
}
```

## JSON Anti-patterns Quick Index {comprehensive}

### ❌ Don't: Exceed Performance Limits
```json
// Example relationship-field-30
{
  "comment": "WRONG - Will cause severe degradation, no maximum validation",
  "multiple": true
}
```

### ❌ Don't: Change Vocabulary After Creation
Note: Vocabulary is immutable - must plan before deployment

### ❌ Don't: Mix Validation Types
```json
// Example relationship-field-31
{
  "comment": "WRONG - Multiple requires array validation",
  "multiple": true,
  "validationSchema": [["yup.string"]]
}
```

## Quick Diagnosis Tables (2025-01-03) {important}

### Relationship Issues Diagnosis
| Symptom | Likely Cause | Quick Fix | Platform | Prevention |
|---------|--------------|-----------|----------|------------|
| Slow UI | >50 relationships | Split field | All | Design limits |
| No reciprocals | Offline mode | Wait for sync | All | Sync first |
| Validation fails | Wrong schema type | Check multiple setting | All | Test config |
| Orphaned records | Parent deleted | Manual cleanup | All | Delete order |
| Can't find record | HRID not configured | Add TemplatedString | All | Form design |
| Modal won't open | Too many records | Reduce relationships | Mobile | Limit to 50 |
| Autocomplete broken | Case mismatch | Use exact case | All | Document format |
| Wrong vocabulary | Config locked | Cannot change | All | Plan carefully |
| Duplicate relationships | No validation | Manual check | All | User training |
| Crash on selection | Memory exhaustion | Restart app | Mobile | Regular cleanup |
| Lost relationships | Sync conflict | Check server | All | Avoid simultaneous |
| Can't delete relationship | UI limitation | Edit JSON | All | Known issue |
| Performance lag | Network latency | Work offline | All | Local-first |
| Touch targets small | 36px height | Use desktop | Mobile | WCAG issue |
| Back button closes | Android behaviour | Save first | Android | Platform quirk |

## Field Interaction Matrix (2025-01-03) {important}

### Relationships with Other Fields
| Field Combination | Interaction | Pattern |
|------------------|-------------|---------|
| RelatedRecordSelector + TemplatedString | Essential | HRIDs for display |
| RelatedRecordSelector + AutoIncrementer | Common | Feeds HRIDs |
| RelatedRecordSelector + Conditions | Limited | Existence only |
| Multiple RelatedRecordSelectors | Caution | Performance impact |

## Migration Warnings Index (2025-01-03) {comprehensive}

### Critical Migration Issues
1. **Vocabulary pairs immutable** - Cannot change after creation
2. **Type conversion loses data** - Child↔Linked migration
3. **Performance degradation** - Plan for <50 relationships
4. **No conflict resolution** - Last-write-wins only
5. **Orphan accumulation** - Soft-delete behaviour
6. **No re-import** - CSV export one-way
7. **Touch target issues** - Mobile accessibility

## See Also {comprehensive}

### Other Field Categories
- **[Text Fields](./text-fields-v05.md)**: TemplatedString for meaningful HRIDs
- **[Number Fields](./number-fields-v05.md)**: AutoIncrementer feeding HRIDs
- **[DateTime Fields](./datetime-fields-v05.md)**: Temporal relationship tracking
- **[Select/Choice Fields](./select-choice-fields-v05.md)**: Alternative for simple vocabularies
- **[Media Fields](./media-fields-v05.md)**: Attaching files to relationships
- **[Location Fields](./location-fields-v05.md)**: Spatial relationships
- **[Display Field](./display-field-v05.md)**: Relationship instructions

### Reference Documents
  - [Validation Timing Reference](../reference-docs/validation-timing-reference.md)
  - [Component Namespace Reference](../reference-docs/component-namespace-reference.md)
  - [Data Export Reference](../reference-docs/data-export-reference.md)
  - [Security Considerations Reference](../reference-docs/security-considerations-reference.md)
  - [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md)
  - [Meta Properties Reference](../reference-docs/meta-properties-reference.md)
  - [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md)
  - [Formik Integration Reference](../reference-docs/formik-integration-reference.md)
  - [Accessibility Reference](../reference-docs/accessibility-reference.md)

## Error Message Quick Reference {important}

### Relationship-Specific Errors
| Error | Cause | Solution |
|-------|-------|----------|
| "Only one related record allowed" | multiple: false with existing | Remove first |
| "this field is required" | Required validation | Add relationship |
| "Target form not found" | Wrong related_type | Check viewset ID |
| Silent failure | Performance overload | Reduce count |
| No autocomplete results | HRID not configured | Add TemplatedString |

## Metadata {comprehensive}
- **Document Version**: v05 (transformed)
- **Source Document**: relationship.md (Third Draft)
- **Platform Version**: Fieldmark v3 (January 2025)
- **Field Count**: 1 (RelatedRecordSelector)
- **Key Limitations**: 50 relationship limit, immutable vocabulary, orphan behaviour
- **Performance Critical**: Yes - degrades rapidly
- **Reference Docs**: 9 linked documents
---


## Fields in Complete Notebooks {important}

For complete working examples showing how these fields integrate into full notebook structures with fviews and viewsets, see:

→ **[Complete Notebook Templates](../references/notebook-templates.md)**

The templates include:
- Minimal survey (3 fields) 
- Basic data collection (10 fields)
- Complex form with validation (20 fields)
- Mobile-optimized with GPS/Photo
- Production archaeological recording

Each template shows the complete JSON structure required for import into Designer, including:
- Proper field → fview → viewset hierarchy
- Required `name` parameters for all fields
- Working validation schemas
- Conditional logic examples

---

## Related Documentation {important}
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Media Fields](./media-fields-v05.md) | [#media-fields](#media-fields)
- **Index**: [Field Documentation Index](../field-type-index.md) | [#fieldmark-v3-field-type-documentation-index](#fieldmark-v3-field-type-documentation-index)

### Cross-Field Patterns
- **Field Selection**: [Relationship Field Selection Guidance](../patterns/field-selection-guide.md#relationship-field) | [#field-selection](#field-selection)
- **Hierarchical Data**: [Parent-Child Records](../detail-crossfield-docs/patterns.md#hierarchical) | [#common-patterns](#common-patterns)
- **Conditional Logic**: [Dependent Records](../detail-crossfield-docs/conditional-logic.md#relationship-fields) | [#conditional-logic](#conditional-logic)

### Technical References
- **Designer Limitations**: [Relationship Constraints](../reference-docs/designer-limitations-reference.md#relationship-fields) | [#designer-limitations](#designer-limitations)
- **Data Export**: [Relationship Handling](../reference-docs/data-export-reference.md#relationships) | [#data-export](#data-export)

<!-- /concat:references -->
<!-- concat:boundary:end section="relationship-fields" -->
