# AdvancedSelect Field - Third Draft Documentation

## Overview

The AdvancedSelect field (`faims-custom::AdvancedSelect`) provides hierarchical tree navigation for selecting values from nested vocabularies, returning `faims-core::String` values representing either full paths or leaf nodes. **Currently in beta status** due to incomplete Designer integration, performance limitations, and multiple critical bugs. This field renders entire tree structures without optimisation, making it unsuitable for large datasets or mobile deployment. The component requires manual JSON editing for hierarchy configuration and suffers from the same validation display failures as other choice fields. **Production deployments should use Select or multiple Select fields with prefixed options until AdvancedSelect stabilises.**

**Critical limitations**: No error display, no clear/deselect capability, no search functionality, severe performance degradation beyond 100 nodes, requires JSON hand-editing, breaks mobile layouts.

## Common Use Cases

- Biological taxonomic classification (kingdom → phylum → class → order)
- Archaeological typologies (material → technique → form → decoration)
- Geographic hierarchies (continent → country → region → site)
- Organizational structures (department → division → team → role)
- Stratigraphic sequences (period → phase → context → feature)
- Artifact categorisation (category → type → subtype → variant)
- Controlled vocabularies requiring semantic hierarchy
- Classification systems where path context matters

## Core Configuration

### Required Parameters
```json
{
  "component-namespace": "faims-custom",
  "component-name": "AdvancedSelect",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "label": "Field Label",
    "ElementProps": {
      "optiontree": [
        {
          "name": "Parent",
          "children": [
            {
              "name": "Child",
              "children": []
            }
          ]
        }
      ]
    }
  },
  "validationSchema": [["yup.string"]],
  "initialValue": ""
}
```

### Optional Parameters
- **helperText** (`string`): Guidance text below field
- **required** (`boolean`): Makes field mandatory (but error won't display)
- **valuetype** (`"full" | "child"`): Controls stored value format
  - `"full"` (default): Stores complete path with " > " delimiters
  - `"child"`: Stores only selected node name
- **disabled** (`boolean`): Disables entire tree (no node-level control)
- **meta.annotation**: Enable annotation field
- **meta.uncertainty**: Enable uncertainty field

### Node Structure
```typescript
interface TreeNode {
  name: string;        // Required: Used for path construction
  label?: string;      // Optional: Display override
  children?: TreeNode[]; // Optional: Child nodes
}
```

**Designer limitations**: Basic parameters configurable via GUI (label, helperText, valuetype) but **optiontree structure must be hand-edited in JSON** - primary reason for beta status.

## Validation Rules

### Built-in Validation
- **Type validation**: Validates as string
- **No hierarchical validation**: Cannot validate depth, branch selection, or tree structure
- **No clearing validation**: Once selected, cannot return to empty (UX bug)

### Configurable Validation

| Rule | Configuration | Effect | Error Message | Display |
|------|---------------|--------|---------------|---------|
| required | `["yup.required"]` | Blocks submission if empty | "This field is required" | **NEVER SHOWN** |
| oneOf | `["yup.oneOf", ["val1", "val2"]]` | Restricts to specific values | "Must be one of the following values" | **NEVER SHOWN** |
| matches | `["yup.matches", "pattern"]` | Pattern matching on stored value | "Must match pattern" | **NEVER SHOWN** |

### Validation Behaviour
- **Timing**: Validates immediately on every node selection
- **Error display**: **CRITICAL BUG** - Validation errors never shown to users
- **Form blocking**: Invalid fields prevent submission but give no feedback
- **Required paradox**: Required validation fails silently, confusing users
- **Clear issue**: Cannot clear selection to fix validation errors

### Validation Examples
```json
// Required selection (blocks silently)
"validationSchema": [
  ["yup.string"],
  ["yup.required", "Classification required"]
]

// Restrict to leaf nodes only (with valuetype: "child")
"validationSchema": [
  ["yup.string"],
  ["yup.oneOf", ["Species A", "Species B", "Species C"]]
]
```

## Display Behaviour

### Desktop Rendering
- **Container**: Fixed 500px minimum width, 300px maximum height
- **Scroll behaviour**: Vertical scroll for tall hierarchies, horizontal for wide labels
- **Tree display**: Material-UI TreeView with expand/collapse chevrons
- **Initial state**: Starts fully collapsed, requires manual expansion
- **Selection indicator**: Chip display showing current selection
- **No clear button**: Selected value cannot be cleared through UI
- **Expansion state**: Lost when navigating away and returning

### Mobile Rendering

#### iOS Behaviour
- **Critical issue**: 500px fixed width causes horizontal scrolling
- **Touch targets**: Chevron icons too small for reliable interaction
- **No optimisation**: Standard TreeView without mobile adaptations
- **Performance**: Degrades significantly with 100+ nodes
- **Gestures**: No pinch-zoom or swipe support

#### Android Behaviour
- **Same width issue**: Horizontal scrolling required on most devices
- **Touch accuracy**: Difficult to hit specific nodes accurately
- **No improvements**: Identical to iOS behaviour
- **Performance**: Similar degradation with large trees

### Visual Hierarchy
- **Node display**: Shows `name` property by default
- **Label override**: If `label` present, displays as "label (name)"
- **Path separator**: Uses " > " in stored values
- **No depth indicators**: All levels styled identically
- **No icons**: Text-only display

## Interaction Patterns

### Selection Mechanics
- **Single selection only**: Each click replaces previous selection
- **Any node selectable**: Parent and child nodes all selectable
- **No deselection**: Cannot clear selection once made (critical UX issue)
- **Immediate replacement**: No confirmation for selection changes
- **valuetype misconception**: Does NOT restrict which nodes can be selected

### Navigation Patterns
- **Manual expansion**: Must click each chevron to expand branches
- **No shortcuts**: No expand all/collapse all functionality
- **No search**: Must visually scan entire hierarchy
- **No keyboard jump**: Cannot type to jump to nodes
- **Lost state**: Expansion state resets on form navigation

### Keyboard Support
- **Basic only**: Limited MUI TreeView defaults
- **Tab navigation**: Can tab to tree container
- **Arrow keys**: May work for tree navigation (unreliable)
- **No search**: No type-ahead or quick navigation
- **No shortcuts**: No keyboard commands for expansion

### Touch Interaction
- **Small targets**: 24px chevrons difficult to tap
- **No gestures**: No swipe, pinch, or long-press
- **Precision required**: Easy to select wrong node
- **No optimisation**: Desktop interactions on mobile

## Conditional Logic Support

### Field as Condition Source
AdvancedSelect values can trigger conditional logic with behaviour dependent on `valuetype`:

```json
// With valuetype: "full" (default)
{
  "field-name": {
    "component-name": "TextField",
    "condition": {
      "field": "classification",
      "operator": "equal",
      "value": "Animalia > Chordata > Mammalia"  // Must match exact path
    }
  }
}

// With valuetype: "child"
{
  "field-name": {
    "component-name": "TextField",
    "condition": {
      "field": "classification", 
      "operator": "equal",
      "value": "Mammalia"  // Matches selected node name only
    }
  }
}
```

### Conditional Patterns
- **Exact match only**: No partial path matching or wildcards
- **String operations**: Standard string operators (equal, not-equal, contains)
- **No hierarchical operators**: Cannot check "is child of" or "is parent of"
- **Path format critical**: Must include exact " > " spacing for full paths

### Field as Condition Target
- Standard visibility and requirement conditions apply
- Can be shown/hidden based on other field values
- Can be made required conditionally

## Data Storage and Export

### Storage Format
- **Type returned**: `faims-core::String`
- **Full path format**: "Level1 > Level2 > Level3" (with spaces around >)
- **Child format**: "Level3" (node name only)
- **Empty value**: Empty string "" when unselected
- **No structure**: Hierarchical relationship lost in storage

### Export Behaviour
- **CSV export**: Single column with string value
- **JSON export**: String property, not nested object
- **No hierarchy preservation**: Flat string representation only
- **Delimiter issues**: " > " in node names would break path parsing
- **No multiple columns**: Doesn't split hierarchy across columns

### Data Migration
- **No automated tools**: Cannot convert from Select fields
- **Manual mapping required**: Must transform existing values to paths
- **Breaking change**: Switching valuetype changes all stored data
- **No backwards compatibility**: Cannot read flat vocabulary data

## Common Patterns

### Example 1: Biological Taxonomy
```json
{
  "species-classification": {
    "component-namespace": "faims-custom",
    "component-name": "AdvancedSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Species Classification",
      "name": "species-classification",
      "valuetype": "full",
      "helperText": "Navigate to the most specific classification possible",
      "ElementProps": {
        "optiontree": [
          {
            "name": "Animalia",
            "children": [
              {
                "name": "Chordata",
                "children": [
                  {
                    "name": "Mammalia",
                    "children": [
                      {
                        "name": "Primates",
                        "children": [
                          {
                            "name": "Hominidae",
                            "children": [
                              {
                                "name": "Homo",
                                "children": [
                                  {
                                    "name": "Homo sapiens",
                                    "label": "Human"
                                  }
                                ]
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "name": "Aves",
                    "label": "Birds",
                    "children": []
                  }
                ]
              }
            ]
          },
          {
            "name": "Plantae",
            "children": []
          }
        ]
      }
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Species classification required"]
    ],
    "initialValue": "",
    "meta": {
      "annotation": {"include": true, "label": "Identification notes"}
    }
  }
}
```
**Behaviour**: Stores full path like "Animalia > Chordata > Mammalia > Primates > Hominidae > Homo > Homo sapiens". Parent nodes can be selected for partial classification. No error display despite required validation.

### Example 2: Archaeological Context Hierarchy
```json
{
  "context-hierarchy": {
    "component-namespace": "faims-custom",
    "component-name": "AdvancedSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Stratigraphic Context",
      "name": "context-hierarchy",
      "valuetype": "child",
      "helperText": "Select the specific context",
      "ElementProps": {
        "optiontree": [
          {
            "name": "Trench 1",
            "children": [
              {
                "name": "Layer 001",
                "label": "Topsoil",
                "children": [
                  {
                    "name": "Context 001-A",
                    "children": []
                  },
                  {
                    "name": "Context 001-B",
                    "children": []
                  }
                ]
              },
              {
                "name": "Layer 002",
                "label": "Occupation",
                "children": [
                  {
                    "name": "Context 002-A",
                    "label": "Floor surface",
                    "children": []
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
**Behaviour**: With valuetype: "child", stores only selected node like "Context 002-A" without path. Users can still select parent nodes like "Layer 001" which would store "Layer 001".

### Example 3: Geographic Location Hierarchy (Demonstrating Limitations)
```json
{
  "location-hierarchy": {
    "component-namespace": "faims-custom",
    "component-name": "AdvancedSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Site Location",
      "name": "location-hierarchy",
      "valuetype": "full",
      "ElementProps": {
        "optiontree": [
          {
            "name": "Australia",
            "children": [
              {
                "name": "New South Wales",
                "children": [
                  {
                    "name": "Sydney Region",
                    "children": [
                      {"name": "Site 001"},
                      {"name": "Site 002"}
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  },
  "clear-selection": {
    "component-name": "TextField",
    "label": "Clear Selection Workaround",
    "helperText": "Since selection cannot be cleared, provide manual override",
    "condition": {
      "field": "location-hierarchy",
      "operator": "not-equal",
      "value": ""
    }
  }
}
```
**Limitation demonstrated**: Once a location is selected, it cannot be cleared. The TextField workaround provides a manual way to note when selection should be ignored.

## Troubleshooting Guide

### Common Issues and Solutions

| Issue | Cause | Solution | Prevention |
|-------|-------|----------|------------|
| Cannot clear selection | No deselect mechanism | Add TextField for manual override or reload form | Document limitation to users |
| Validation error not showing | No error display implementation | Check form won't submit, add helperText explaining requirements | Use Select for critical fields |
| Horizontal scrolling on mobile | Fixed 500px width | Use Select field for mobile deployment | Restrict to tablet/desktop only |
| Performance degradation | Renders entire tree immediately | Limit to <100 nodes | Use multiple Select fields instead |
| Tree starts collapsed | No default expansion | Document navigation requirements | Consider flat Select if few options |
| Lost expansion state | State not preserved | Warn users about navigation | Keep forms on single page |
| Required field confusion | Silent validation failure | Explicitly document in helperText | Avoid required validation |
| Hierarchy not in Designer | Must edit JSON manually | Provide JSON templates | Use Select until Designer support |

### Debug Checklist
- [ ] Check browser console for React key warnings (duplicate names)
- [ ] Verify no circular references in optiontree structure
- [ ] Confirm all nodes have required `name` property
- [ ] Test with <100 nodes to isolate performance issues
- [ ] Check stored value format matches conditional logic expectations
- [ ] Verify JSON structure is valid (use JSON validator)
- [ ] Test on desktop first to isolate mobile-specific issues
- [ ] Check field name doesn't conflict with other fields
- [ ] Ensure valuetype setting matches downstream processing needs

### Platform-Specific Issues

**Mobile (iOS/Android)**:
- Horizontal scrolling unavoidable with current implementation
- Touch targets too small for reliable selection
- Performance severely degraded with large trees
- No mobile optimisations available

**Web Browser**:
- Works best on desktop with mouse interaction
- Keyboard navigation limited and unreliable
- No browser-specific optimisations

## Implementation Notes

### Performance Boundaries
- **<50 nodes**: Acceptable performance on all platforms
- **50-100 nodes**: Noticeable lag on mobile, acceptable on desktop
- **100-500 nodes**: Significant delays, interaction lag
- **500-1000 nodes**: Likely unusable, browser may freeze
- **>1000 nodes**: Will crash or hang browser

### Technical Limitations
- **No virtualisation**: Entire tree rendered in DOM immediately
- **No lazy loading**: All branches rendered even when collapsed
- **No memoization**: Re-renders entire tree on any change
- **No search capability**: Must manually navigate hierarchy
- **No dynamic loading**: All data must be in initial configuration
- **No error boundaries**: Malformed data crashes component

### Designer Constraints
- **JSON editing required**: Hierarchy must be hand-coded
- **No preview**: Cannot see tree structure in Designer
- **No validation**: Designer doesn't validate tree structure
- **Limited parameters**: Only basic field properties exposed
- **No migration tools**: Cannot convert from other field types

### Data Structure Requirements
- **Static only**: No external data source support
- **Complete hierarchy**: Must define entire tree upfront
- **No async loading**: Cannot load branches on demand
- **Memory impact**: Large trees consume significant memory
- **No caching**: Full tree in memory at all times

## Best Practices

### Hierarchy Design
- **Limit depth**: Maximum 3-4 levels for usability
- **Limit breadth**: <20 nodes per level for performance
- **Total nodes**: Keep under 100 for mobile compatibility
- **Clear naming**: Use descriptive, unique node names
- **Avoid delimiters**: Don't use " > " in node names

### Configuration Strategy
- **Start with JSON**: Design hierarchy in JSON editor first
- **Test small**: Verify with minimal tree before expanding
- **Document structure**: Maintain separate documentation of hierarchy
- **Version control**: Track optiontree changes carefully
- **Provide templates**: Give users JSON snippets to copy

### Deployment Decisions
- **Avoid mobile**: Use Select or MultiSelect for phone deployment
- **Tablet minimum**: Require tablet or desktop for this field
- **Warn users**: Explicitly document all limitations
- **Provide fallbacks**: Include TextField annotation for edge cases
- **Consider alternatives**: Multiple Select fields may be better

### Workarounds
- **Clear selection**: Add conditional TextField for manual override
- **Performance**: Split large hierarchies into multiple Select fields
- **Mobile**: Create separate mobile form with simplified fields
- **Search needs**: Use Select with filtered options instead
- **Validation feedback**: Add explicit helperText about requirements

### Migration Planning
- **From Select**: Manual data transformation required
- **To Select**: Export paths must be mapped to flat values
- **Data preservation**: Archive original hierarchy before changes
- **Test thoroughly**: Validate all data migrations
- **Document mappings**: Keep record of value transformations

## Cross-References & Dependencies

### Alternative Choice Fields
- **[Select](./Select.md)** - Use instead for flat vocabularies, mobile deployment, or when error display needed
  - *Trade-off*: Loses hierarchy but gains stability and mobile support
  - *Migration*: Must flatten hierarchy and map values manually
- **[MultiSelect](./MultiSelect.md)** - For multiple selections from flat vocabulary
  - *Relationship*: AdvancedSelect cannot do multiple selection (commented out in code)
  - *Alternative pattern*: Use multiple AdvancedSelect fields for multiple classifications

### Fallback Patterns
- **[TextField](./TextField.md)** - Essential pairing for annotation and manual override
  - *Usage*: Add conditional TextField to handle edge cases
  - *Workaround*: Provides way to note when selection should be cleared
- **Multiple [Select](./Select.md) fields** - Alternative for representing hierarchy
  - *Pattern*: Cascading selects where each level depends on previous
  - *Advantage*: Better mobile support and error display

### Related Components
- **[RadioGroup](./RadioGroup.md)** - For small hierarchies (2-7 options)
  - *Comparison*: Better for shallow hierarchies with few options
  - *Advantage*: All options visible, proper error display
- **[Checkbox](./Checkbox.md)** - When parent/child selection is binary
  - *Pattern*: Multiple checkboxes can represent simple hierarchies

### Conditional Logic Dependencies
- Fields commonly dependent on AdvancedSelect values:
  - Additional classification fields shown for specific branches
  - Measurement fields for certain taxonomic groups
  - Photo requirements based on classification
- Conditional matching requires exact string values

### Data Flow
- **[TemplatedStringField](./TemplatedStringField.md)** - Can reference selected values
  - *Usage*: Include classification in record IDs
  - *Format*: Must handle full path or leaf value based on valuetype
- **[RelationshipField](./RelationshipField.md)** - Same package but architecturally unrelated
  - *Note*: Both marked as complex/experimental Package F fields
  - *Difference*: RelationshipField handles record links, not hierarchies

### Export and Analysis
- **CSV Export** - Single column with delimited paths
  - *Issue*: Hierarchy structure lost in flat export
  - *Processing*: Requires post-processing to reconstruct hierarchy
- **JSON Export** - String value without structure
  - *Limitation*: Not exported as nested object

### Migration and Compatibility
- **No automated migration** from flat vocabularies
- **Breaking changes** when switching valuetype
- **Manual data transformation** required for any migration
- **Incompatible** with dynamic vocabulary systems

---

*Component Status: **Beta** - Not recommended for production use. Requires JSON hand-editing for hierarchy definition. Multiple critical bugs including inability to clear selection and missing error display. Use Select field with prefixed options for production deployments until AdvancedSelect matures.*