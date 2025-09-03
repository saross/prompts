# RelationshipField - Third Draft Documentation

## Overview

The RelationshipField (`faims-custom::RelatedRecordSelector`) enables bidirectional connections between records, returning `faims-core::Relationship` values that encode both hierarchical ownership (Child) and semantic peer associations (Linked). This sophisticated field maintains data coherence through automatic reciprocal updates whilst supporting multiple vocabulary pairs for qualified relationships. Critical limitations include performance degradation beyond 50 relationships (unusable at 200), JSON-only vocabulary configuration, and soft-delete orphaning behaviour requiring manual cleanup strategies. The field operates within Fieldmark's distributed architecture where offline reciprocal updates are delayed until synchronisation.

## Common Use Cases

• **Hierarchical data organisation** - Site→Trench→Context→Find structures with automatic parent-child inheritance
• **Stratigraphic relationship documentation** - Recording "cuts/is cut by", "fills/is filled by", "above/below" relationships
• **Sample-to-context associations** - Linking samples to their collection contexts with semantic qualification
• **Feature relationships** - Documenting spatial/temporal relationships between archaeological features
• **Cross-cutting associations** - Connecting entities across different hierarchical branches
• **Find assemblages** - Grouping related artefacts whilst maintaining individual records
• **Specialist analysis links** - Connecting primary records to specialist assessment records

## Core Configuration

### Required Parameters
```json
{
  "component-namespace": "faims-custom",
  "component-name": "RelatedRecordSelector", 
  "type-returned": "faims-core::Relationship",
  "component-parameters": {
    "name": "field-name",              // Required: Field identifier
    "label": "Field Label",            // Required: Display label
    "related_type": "TargetFormID",    // Required: Target viewset ID
    "relation_type": "Child"           // Required: "Child" or "is-related-to"
  }
}
```

### Optional Parameters
```json
{
  "component-parameters": {
    "multiple": true,                   // Default: true - Allow multiple relationships
    "required": false,                  // Default: false - Field requirement
    "allowLinkToExisting": true,        // Default: true - Enable linking vs only creation
    "related_type_label": "Context",    // Human-readable form name
    "helperText": "Add related items",  // Helper text
    "relation_linked_vocabPair": [      // For Linked relationships only
      ["forward_label", "reverse_label"]
    ]
  }
}
```

### Vocabulary Pair Configuration (Linked Only)
```json
"relation_linked_vocabPair": [
  ["cuts", "is cut by"],
  ["fills", "is filled by"],
  ["is above", "is below"],
  ["same as", "same as"],
  ["contemporary with", "contemporary with"]
]
```
**Critical**: Vocabulary pairs cannot be modified after relationships are created. Requires JSON editing - Designer cannot configure these.

## Validation Rules

| Rule | Configuration | Effect | Error Message |
|------|---------------|--------|---------------|
| Required (multiple) | `["yup.array"], ["yup.required"]` | At least one relationship | "this field is required" |
| Required (single) | `["yup.string"], ["yup.required"]` | Exactly one relationship | "this field is required" |
| Optional (multiple) | `["yup.array"]` | Zero or more relationships | N/A |
| Optional (single) | `["yup.string"]` | Zero or one relationship | N/A |

### Validation Limitations
- **No circular prevention**: System allows A→B→C→A cycles
- **No cross-field validation**: Cannot validate relationship counts or types
- **No custom validation**: Cannot add project-specific rules via `yup.test()`
- **No metadata validation**: Annotations and uncertainty not validated

### Single vs Multiple Behaviour
- `multiple: false` + existing relationship = UI shows "Only one related record allowed"
- Validation type changes: Multiple uses array validation, single uses string
- Configuration change warning: Multiple→Single silently loses all but first relationship

## Display Behaviour

### Desktop Rendering
- **Add New button**: Navigates to new record form (always visible if enabled)
- **Link to Existing dropdown**: MUI Autocomplete with search (if `allowLinkToExisting: true`)
- **Relationship list**: All current relationships with type labels and remove buttons
- **Vocabulary selector**: Dropdown showing forward labels only (Linked relationships)
- **Container width**: Responsive grid layout adapting to available space
- **Error display**: Below field when validation fails

### Mobile Rendering
#### iOS Behaviour
- **Constrained viewport**: Relationship lists require vertical scrolling
- **Touch targets**: ~36px height (below WCAG 44px requirement)
- **Vocabulary dropdown**: Full screen width, may obscure content
- **Search functionality**: Available but text input can be difficult

#### Android Behaviour
- **Similar to iOS**: Same touch target issues
- **Autocomplete**: Android keyboard may offer suggestions
- **Performance**: Degrades faster than iOS with 50+ relationships

### Performance Boundaries
- **<20 relationships**: Optimal across all platforms
- **20-50 relationships**: Acceptable with minor lag
- **50-200 relationships**: Noticeable delays, UI sluggish
- **200+ relationships**: Essentially unusable, especially mobile

## Interaction Patterns

### Add New Workflow
1. User clicks "Add New [Type]" button
2. Navigates to new record form with parent context preserved
3. Creates new record (automatically linked)
4. Returns to parent with "Save and Close"
5. New relationship appears in list

### Link to Existing Workflow
1. User expands "Link to Existing" section
2. Autocomplete dropdown appears with search
3. User types to filter available records (by HRID)
4. Selects record from filtered list
5. For Linked: Must select vocabulary type
6. Clicks "Link" button
7. Relationship added to list

### Relationship Removal
1. User clicks delete icon next to relationship
2. Relationship removed from current record immediately
3. **Warning**: No confirmation dialog
4. Reciprocal relationship remains until sync

### State Transitions
- **Offline creation**: Only current record updated
- **Sync**: Reciprocal relationships established
- **Deletion**: Soft-delete flag, children orphaned
- **Vocabulary selection**: Permanent once created

## Conditional Logic Support

### Supported Conditions
```json
{
  "condition": {
    "operator": "is",
    "field": "stratigraphic_relationships",
    "value": ""  // Check if empty
  }
}
```

### Limitations
- **Cannot check relationship count**: No array.length access
- **Cannot check vocabulary types**: relation_type_vocabPair not accessible
- **Cannot access nested properties**: No relationships[0].vocabulary
- **Only existence checking**: Can only verify if field has any value

## Data Storage and Export

### Database Storage
```json
// Multiple relationships (array)
{
  "field_name": [
    {
      "record_id": "ctx-043-abc",
      "relation_type_vocabPair": ["cuts", "is cut by"]
    },
    {
      "record_id": "ctx-044-def",
      "relation_type_vocabPair": ["fills", "is filled by"]
    }
  ]
}

// Single relationship (object)
{
  "field_name": {
    "record_id": "trn-001-xyz",
    "relation_type_vocabPair": ["is child of", "is parent of"]
  }
}
```

### CSV Export Format
```csv
identifier,record_id,stratigraphic_relationships,parent_trench
"CTX-042","ctx042abc","cuts/ctx043def;is above/ctx044ghi","is child of/trn003xyz"
```

### Export Characteristics
- **Format**: `{relationship_label}/{record_id}` joined by semicolons
- **Reconstruction required**: Manual parsing to rebuild relationships
- **No JSON export**: Despite internal JSON storage
- **Hierarchy flattened**: Parent-child structure not preserved
- **No re-import**: Relationships cannot be imported from CSV

## Common Patterns

### Example 1: Hierarchical Parent-Child Structure
```json
{
  "contexts": {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Relationship",
    "component-parameters": {
      "name": "contexts",
      "label": "Contexts within Trench",
      "related_type": "Context",
      "relation_type": "Child",
      "multiple": true,
      "allowLinkToExisting": false,
      "helperText": "Create new contexts within this trench"
    },
    "validationSchema": [["yup.array"]],
    "initialValue": []
  }
}
```
**Behaviour**: Creates exclusive parent-child relationships. New contexts created from trench form. No linking to existing contexts (ensures exclusive ownership).

### Example 2: Stratigraphic Relationships with Vocabulary
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
      "relation_linked_vocabPair": [
        ["cuts", "is cut by"],
        ["fills", "is filled by"],
        ["is above", "is below"],
        ["abuts", "abuts"],
        ["same as", "same as"]
      ],
      "helperText": "Define relationships with other contexts"
    },
    "validationSchema": [["yup.array"]],
    "initialValue": [],
    "meta": {
      "annotation": {"include": true, "label": "relationship notes"},
      "uncertainty": {"include": true, "label": "confidence"}
    }
  }
}
```
**Behaviour**: Multiple qualified relationships. User selects vocabulary type per relationship. Bidirectional updates on sync. Annotation captures interpretive notes.

### Example 3: Required Single Parent
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
      "allowLinkToExisting": true,
      "related_type_label": "Site Record",
      "helperText": "Select the site this feature belongs to"
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Site association required"]
    ],
    "initialValue": null
  }
}
```
**Behaviour**: Enforces single parent. Must select before saving. Can link to existing sites. String validation for single relationship.

### Example 4: Sample Relationships with Metadata
```json
{
  "related_samples": {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Relationship",
    "component-parameters": {
      "name": "related_samples",
      "label": "Associated Samples",
      "related_type": "Sample",
      "relation_type": "is-related-to",
      "multiple": true,
      "relation_linked_vocabPair": [
        ["subsample of", "has subsample"],
        ["control for", "controlled by"],
        ["compared with", "compared with"]
      ]
    },
    "validationSchema": [["yup.array"]],
    "initialValue": [],
    "meta": {
      "annotation": {"include": true, "label": "sampling notes"},
      "uncertainty": {"include": true, "label": "association confidence"}
    }
  }
}
```

## Troubleshooting Guide

### Common Issues

#### Performance degradation with many relationships
**Cause**: Sequential metadata fetching without batching
**Solution**: Limit to <50 relationships per field; consider splitting into multiple fields

#### Relationships not showing reciprocal immediately
**Cause**: Offline architecture - reciprocal updates delayed until sync
**Solution**: This is by design; reciprocals appear after synchronisation

#### Cannot modify vocabulary pairs
**Cause**: Vocabulary pairs immutable after relationships created
**Solution**: Plan vocabulary carefully; changes require data migration

#### Deleted parent leaves orphaned children
**Cause**: Soft-delete preserves children as orphans (data preservation)
**Solution**: Implement manual cleanup procedures; document in project protocols

#### Touch targets too small on mobile
**Cause**: Buttons at ~36px instead of 44px WCAG requirement
**Solution**: Exercise care when removing relationships; consider tablet for complex relationships

#### Duplicate IDs in relationships
**Cause**: Auto-increment coordination failure across devices
**Solution**: Include device ID in TemplatedString HRIDs; coordinate ranges externally

### Debug Checklist
- [ ] Target form type exists with exact viewset ID match
- [ ] TemplatedStringField configured for meaningful HRIDs
- [ ] Vocabulary pairs defined before creating relationships
- [ ] Performance acceptable with relationship count
- [ ] Offline workflow expectations documented for team
- [ ] Parent deletion consequences understood
- [ ] Touch targets tested on target devices

## Implementation Notes

### Technical Architecture
- **No conflict resolution**: Last-write-wins for concurrent edits
- **Manual conflict resolution**: Through Control Centre UI when conflicts occur
- **No locking mechanism**: Multiple users can edit simultaneously
- **Race conditions possible**: When editing reciprocal relationships offline

### Designer Limitations
- **Cannot configure vocabulary pairs**: Requires JSON editing
- **Cannot preview relationships**: No test data in Designer
- **Cannot convert relationship types**: Child↔Linked requires migration
- **Limited parameter exposure**: Many options JSON-only

### Performance Architecture
- **No virtualization**: All relationships rendered immediately
- **No pagination**: Complete list always visible
- **Sequential fetching**: Each relationship triggers metadata fetch
- **No caching**: Metadata re-fetched on component mount

### Mobile Constraints
- **Fixed elements**: Some widths break responsive layout
- **Scroll requirements**: Long lists require extensive scrolling
- **No gesture support**: No swipe-to-delete or drag-to-reorder
- **Autocomplete issues**: Search difficult with on-screen keyboard

## Best Practices

### Design Principles
- **Shallow hierarchies**: Maximum 3-4 levels for maintainability
- **Limit relationship counts**: Stay under 50 per field
- **Plan vocabulary pairs**: Cannot modify after deployment
- **Document deletion procedures**: Users must understand orphaning
- **Include HRIDs**: Always configure TemplatedStringField for display

### Offline Coordination
- **Communicate range allocation**: For auto-incrementers feeding HRIDs
- **Document sync procedures**: Team must understand reciprocal delays
- **Plan conflict resolution**: Establish protocols for merge conflicts
- **Test offline workflows**: Verify behaviour before deployment

### Performance Optimization
- **Split complex relationships**: Multiple focused fields over one comprehensive
- **Consider alternatives**: For >50 relationships, evaluate design
- **Monitor mobile performance**: Test on lowest-spec devices
- **Implement cleanup routines**: For orphaned records

### Data Management
- **Export regularly**: Relationships preserved but need reconstruction
- **Document vocabulary meanings**: For future analysts
- **Plan migrations carefully**: Type changes lose data
- **Maintain relationship documentation**: External to system

## See Also

- **[TemplatedStringField](./TemplatedStringField.md)** - CRITICAL: Configure for meaningful HRIDs in relationship displays
- **[BasicAutoIncrementer](./BasicAutoIncrementer.md)** - Often feeds HRIDs; requires range coordination
- **[Conditional Logic Guide](../guides/ConditionalLogic.md)** - Relationships as condition sources (limited support)
- **[Export Behaviour](../guides/ExportBehaviour.md)** - CSV reconstruction procedures for relationships
- **[Distributed System Guide](../guides/DistributedSystems.md)** - Understanding offline sync and conflicts
- **[Select Field](./SelectField.md)** - Alternative for controlled vocabulary without relationships
- **[Performance Guide](../guides/Performance.md)** - System-wide performance boundaries

---

*RelationshipField represents sophisticated architecture constrained by implementation realities. The bidirectional automation and semantic qualification provide powerful data modelling capabilities, whilst performance boundaries and configuration limitations require careful planning. Success depends on understanding both the architectural intent and practical constraints.*