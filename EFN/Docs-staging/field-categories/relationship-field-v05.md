# Relationship Field - Fieldmark v3 Documentation

## Overview {essential}

### DESIGNER QUICK GUIDE
**Relationship Field Available:**
- **RelatedRecordSelector** → Connect records with bidirectional relationships

**Component Namespace:** `"faims-custom"`
**Component Name:** `RelatedRecordSelector` (case-sensitive)
**Return Type:** `faims-core::Relationship`
**Designer Support:** Limited - vocabulary pairs require JSON

### CRITICAL NAMING DISAMBIGUATION
- **RelatedRecordSelector** (exact case) - NOT "RelationshipField" or "RecordSelector"
- Component uses namespace `"faims-custom"` - standard custom field
- Two relationship types: `"Child"` (hierarchical) or `"is-related-to"` (peer)
- Vocabulary pairs immutable after creation - plan carefully

### Field Capabilities Summary
Enables bidirectional connections between records with automatic reciprocal updates. Supports hierarchical parent-child relationships with cascade behavior and semantic peer associations with qualified vocabulary pairs. Critical performance degradation beyond 50 relationships (unusable at 200+). Offline reciprocal updates delayed until synchronization.

### Component Status
| Property | Status | Notes |
|----------|--------|-------|
| Designer Support | ⚠️ Limited | No vocabulary pair configuration |
| JSON Enhancement | Required | Vocabulary pairs, advanced options |
| Validation | ✅ Works | Array/string based on multiple |
| Performance | ⚠️ 50 limit | Degrades rapidly above threshold |
| Offline | ⚠️ Delayed | Reciprocals after sync only |

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
- Cannot configure vocabulary pairs (JSON only)
- Cannot preview relationships in Designer
- Cannot convert between Child/Linked types
- No test data for relationship testing
- Limited parameter exposure

## Relationship Types Guide {essential}

### Decision Tree
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

### Vocabulary Pairs
**Bidirectional labeling for Linked relationships:**
```json
"relation_linked_vocabPair": [
  ["cuts", "is cut by"],
  ["fills", "is filled by"],
  ["is above", "is below"],
  ["same as", "same as"]
]
```
- First element: Forward label (shown in current record)
- Second element: Reverse label (shown in related record)
- Immutable after relationship creation
- JSON configuration only

## ⚠️ Critical Performance Risks {essential}
**Performance Degradation Thresholds:**
- **<20 relationships**: Optimal performance
- **20-50 relationships**: Acceptable with minor lag
- **50-100 relationships**: Noticeable delays, UI sluggish
- **100-200 relationships**: Severe degradation
- **200+ relationships**: Essentially unusable

**Mitigation Strategies:**
- Split into multiple focused fields
- Implement pagination (custom development)
- Use hierarchical organization
- Archive historical relationships
- Consider alternative designs for large datasets

## What This Field Cannot Do {important}
- **Prevent circular relationships** - A→B→C→A allowed
- **Modify vocabulary after creation** - Immutable once used
- **Validate relationship counts** - No array.length access
- **Show reciprocals immediately offline** - Sync required
- **Handle 200+ relationships** - Performance collapse
- **Auto-cleanup orphans** - Manual intervention needed
- **Provide conflict resolution** - Last-write-wins only
- **Support gesture controls** - No swipe/drag actions

## Common Use Cases {important}
- **Site hierarchies** - Site→Trench→Context→Find structures
- **Stratigraphic documentation** - Cuts/filled by relationships
- **Sample associations** - Linking samples to contexts
- **Feature relationships** - Spatial/temporal connections
- **Cross-cutting associations** - Across hierarchical branches
- **Find assemblages** - Grouping related artifacts
- **Specialist analysis** - Primary→specialist records

## Designer Component Mapping {essential}
| Designer Option | JSON Configuration | Notes |
|-----------------|-------------------|-------|
| Field Type → RelatedRecordSelector | `"component-name": "RelatedRecordSelector"` | |
| Related Form | `"related_type": "FormID"` | Target viewset ID |
| Relationship Type | `"relation_type": "Child"` or `"is-related-to"` | |
| Allow Multiple | `"multiple": true` | Changes validation |
| Required | `"required": true` | With validation schema |

## Designer Capabilities vs JSON Enhancement {essential}

### Designer Configuration
- ✅ Field label and name
- ✅ Related form selection
- ✅ Relationship type (Child/Linked)
- ✅ Multiple selection toggle
- ✅ Helper text
- ⚠️ Required flag (needs validation)

### JSON-Only Configuration
```json
{
  "relation_linked_vocabPair": [
    ["forward", "reverse"]
  ],
  "allowLinkToExisting": true,
  "related_type_label": "Context Record"
}
```

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

**Common Relationship Errors:**
- Using "RelationshipField" instead of "RelatedRecordSelector"
- Wrong case in component name
- Missing related_type parameter

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Relationship-Specific Security Notes:**
- No access control on relationships
- All users can modify any relationship
- Soft-delete preserves data trail
- No audit log for relationship changes

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for general limits.

**Relationship-Specific Performance:**
- **Query time**: Linear with relationship count
- **Render time**: 100ms per 10 relationships
- **Memory usage**: ~10KB per relationship
- **Sync payload**: Grows exponentially
- **Mobile impact**: 2x slower than desktop

### Validation Patterns {important}
See [Validation Timing Reference](../reference-docs/validation-timing-reference.md) for universal behavior.

**Relationship-Specific Validation:**
```json
// Multiple relationships
"validationSchema": [
  ["yup.array"],
  ["yup.required", "At least one required"]
]

// Single relationship
"validationSchema": [
  ["yup.string"],
  ["yup.required", "Parent required"]
]
```

### Platform Behaviors {important}
**All Platforms:**
- Touch targets ~36px (below 44px WCAG)
- No gesture support
- Autocomplete search by HRID only

**Mobile Specific:**
- Constrained viewport issues
- Keyboard obscures content
- Performance degrades faster
- Scroll-heavy interface

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.

Relationships support annotations and uncertainty:
- Annotation: Document relationship rationale
- Uncertainty: Flag tentative associations

### Export Behavior {important}
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
| Returns | `faims-core::Relationship` |
| Designer | ⚠️ Limited support |
| JSON Required | Vocabulary pairs |
| Performance Limit | 50 relationships |
| Offline Behavior | Delayed reciprocals |
| Touch Target | 36px (suboptimal) |
| Cascade Delete | Orphans (Child only) |

#### Core Configuration
```json
{
  "component-namespace": "faims-custom",
  "component-name": "RelatedRecordSelector",
  "type-returned": "faims-core::Relationship",
  "component-parameters": {
    "name": "field-name",
    "label": "Relationships",
    "related_type": "TargetFormID",
    "relation_type": "Child",
    "multiple": true,
    "required": false,
    "helperText": "Add related records"
  },
  "validationSchema": [["yup.array"]],
  "initialValue": []
}
```

#### Advanced Configuration
```json
{
  "stratigraphic_relationships": {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Relationship",
    "component-parameters": {
      "name": "stratigraphic_relationships",
      "label": "Stratigraphic Relationships",
      "related_type": "Context",
      "relation_type": "is-related-to",
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
      "helperText": "Define stratigraphic relationships"
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "At least one relationship required"]
    ],
    "initialValue": [],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Relationship notes"
      },
      "uncertainty": {
        "include": true,
        "label": "Confidence level"
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

### Performance Issues
1. Count relationships in field
2. Check device specifications
3. Monitor network latency
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

### Hierarchical Parent-Child
```json
{
  "contexts": {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Relationship",
    "component-parameters": {
      "name": "contexts",
      "label": "Contexts in Trench",
      "related_type": "Context",
      "relation_type": "Child",
      "multiple": true,
      "allowLinkToExisting": false,
      "helperText": "Create contexts within this trench"
    }
  }
}
```

### Required Single Parent
```json
{
  "parent_site": {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Relationship",
    "component-parameters": {
      "name": "parent_site",
      "label": "Parent Site",
      "related_type": "Site",
      "relation_type": "Child",
      "multiple": false,
      "required": true,
      "allowLinkToExisting": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Site required"]
    ]
  }
}
```

### Sample Relationships
```json
{
  "related_samples": {
    "component-parameters": {
      "relation_type": "is-related-to",
      "relation_linked_vocabPair": [
        ["subsample of", "has subsample"],
        ["control for", "controlled by"],
        ["compared with", "compared with"]
      ]
    }
  }
}
```

## Migration and Best Practices {comprehensive}

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

## Field Quirks Index (2025-01) {comprehensive}
- Vocabulary pairs immutable after use
- Reciprocals delayed until sync
- Performance cliff at 50 relationships
- Touch targets below WCAG standards
- No circular relationship prevention
- Orphans on parent deletion
- No gesture controls
- Autocomplete by HRID only

## Performance Thresholds Summary {essential}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for detailed metrics.

**Relationship-Specific Thresholds:**
| Metric | Value | Impact |
|--------|-------|---------|
| Optimal | <20 | Smooth operation |
| Acceptable | 20-50 | Minor lag |
| Degraded | 50-100 | Noticeable delays |
| Severe | 100-200 | Very slow |
| Unusable | >200 | System failure |

## JSON Patterns Cookbook (2025-01) {comprehensive}

### Pattern: Conditional Relationships
```json
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
"validationSchema": [
  ["yup.array"],
  ["yup.min", 1, "Required"],
  ["yup.max", 50, "Performance limit"]
]
```

## JSON Anti-patterns Quick Index {comprehensive}

### ❌ Don't: Exceed Performance Limits
```json
// WRONG - Will cause severe degradation
{
  "multiple": true
  // No maximum validation
}
```

### ❌ Don't: Change Vocabulary After Creation
```json
// WRONG - Vocabulary immutable
// Must plan before deployment
```

### ❌ Don't: Mix Validation Types
```json
// WRONG - Multiple requires array validation
{
  "multiple": true,
  "validationSchema": [["yup.string"]]
}
```

## Quick Diagnosis Tables (2025-01) {important}

### Relationship Issues Diagnosis
| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| Slow UI | >50 relationships | Split field |
| No reciprocals | Offline mode | Wait for sync |
| Validation fails | Wrong schema type | Check multiple setting |
| Orphaned records | Parent deleted | Manual cleanup |
| Can't find record | HRID not configured | Add TemplatedString |

## Field Interaction Matrix (2025-01) {important}

### Relationships with Other Fields
| Field Combination | Interaction | Pattern |
|------------------|-------------|---------|
| RelatedRecordSelector + TemplatedString | Essential | HRIDs for display |
| RelatedRecordSelector + AutoIncrementer | Common | Feeds HRIDs |
| RelatedRecordSelector + Conditions | Limited | Existence only |
| Multiple RelatedRecordSelectors | Caution | Performance impact |

## Migration Warnings Index (2025-01) {comprehensive}

### Critical Migration Issues
1. **Vocabulary pairs immutable** - Cannot change after creation
2. **Type conversion loses data** - Child↔Linked migration
3. **Performance degradation** - Plan for <50 relationships
4. **No conflict resolution** - Last-write-wins only
5. **Orphan accumulation** - Soft-delete behavior
6. **No re-import** - CSV export one-way
7. **Touch target issues** - Mobile accessibility

## See Also {comprehensive}
- **Text Fields**: TemplatedString for HRIDs
- **Number Fields**: AutoIncrementer for IDs
- **Select Fields**: Alternative for simple vocabularies
- **Reference Documents:**
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
- **Key Limitations**: 50 relationship limit, immutable vocabulary, orphan behavior
- **Performance Critical**: Yes - degrades rapidly
- **Reference Docs**: 9 linked documents