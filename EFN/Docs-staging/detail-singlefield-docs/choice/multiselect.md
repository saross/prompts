# MultiSelect Field - Third Draft Documentation

## Overview

The MultiSelect field (`faims-custom::MultiSelect`) enables multiple value selection from predefined option lists, returning `faims-core::Array` values. It provides two distinct display modes—dropdown with checkboxes or expanded checklist—optimising for different option counts and screen constraints. Unlike the single-selection limitations of RadioGroup, Select, and Checkbox fields, MultiSelect handles group validation through a single field returning an array. The component uniquely supports exclusive options (mutual exclusivity), where selecting "None" or "Unknown" automatically clears other selections. While solving the multiple selection gap in Package D fields, MultiSelect inherits their critical limitations: no error message display, no accessibility support, and static-only vocabularies.

## Common Use Cases

- **Archaeological site features** - Multiple characteristics present (defensive walls, domestic structures, industrial remains)
- **Artefact materials** - Objects with composite materials (ceramic with metal inlay, bone with shell decoration)
- **Site formation processes** - Multiple concurrent processes (alluvial, colluvial, anthropogenic)
- **Conservation treatments** - Multiple interventions applied (cleaned, consolidated, reconstructed)
- **Damage assessment** - Multiple damage types present (weathering, vandalism, vegetation)
- **Survey visibility conditions** - Multiple factors affecting visibility (vegetation, erosion, modern disturbance)
- **Exclusive conditions** - "None observed" or "Unable to assess" options that clear all others
- **Taxonomic identifications** - Multiple species present in ecological transect
- **Permit requirements** - Multiple permits needed (heritage, environmental, landowner)
- **Equipment used** - Multiple tools/methods employed in recording

## Core Configuration

### Required Properties
```json
{
  "component-namespace": "faims-custom",
  "component-name": "MultiSelect",
  "type-returned": "faims-core::Array",
  "component-parameters": {
    "name": "site-features",
    "id": "site-features",
    "label": "Site Features",
    "ElementProps": {
      "options": [
        {"value": "defensive", "label": "Defensive structures"},
        {"value": "domestic", "label": "Domestic occupation"},
        {"value": "industrial", "label": "Industrial remains"}
      ]
    }
  },
  "validationSchema": [["yup.array"]],
  "initialValue": []
}
```

### Optional Properties
```json
{
  "component-parameters": {
    "required": false,
    "helperText": "Select all that apply",
    "ElementProps": {
      "expandedChecklist": true,          // Display as checklist (default: false)
      "exclusiveOptions": ["none", "unknown"], // Mutually exclusive values
      "fullWidth": true,                   // Expand to container width
      "variant": "outlined"                // MUI variant styling
    }
  },
  "meta": {
    "annotation": {
      "include": true,
      "label": "selection notes"
    },
    "uncertainty": {
      "include": false
    }
  }
}
```

### Designer vs JSON Configuration

**Designer Interface Exposes**:
- Label and helper text
- Options management (add/remove/reorder with drag handles)
- Expanded checklist mode toggle
- Per-option exclusive configuration checkbox
- Markdown syntax support in options
- Advanced helper text toggle
- Enforces value = label (human-readable exports)

**JSON-Only Properties**:
- `fullWidth` control
- `variant` styling
- Complex validation chains beyond basic required
- Different values vs labels (not recommended)
- SelectProps for dropdown customisation

## Validation Rules

| Validation Type | Configuration | Behaviour | Critical Note |
|-----------------|---------------|-----------|---------------|
| Required field | `["yup.required"]` | Checks not null/undefined | ⚠️ **Empty array [] PASSES** - not what users expect |
| Minimum selection | `["yup.min", 1, "Select at least one"]` | Enforces minimum items | Use this for "required" behaviour, NOT yup.required |
| Maximum selection | `["yup.max", 5, "Maximum 5 selections"]` | Limits selection count | Not enforced during interaction, only on submit |
| Array type | `["yup.array"]` | Ensures array type | Default, always included |
| Specific values | `["yup.array"], ["yup.of", ["yup.oneOf", ["val1", "val2"]]]` | Restricts to subset | Complex syntax for value validation |
| Min and max | `["yup.array"], ["yup.min", 2], ["yup.max", 5]` | Range constraint | Between 2-5 selections required |

### Critical Validation Behaviour
- **NO ERROR DISPLAY**: Validation runs but messages never appear in UI
- **Empty array gotcha**: `["yup.required"]` considers `[]` as valid (field exists)
- **No proactive enforcement**: Max selection limit not prevented during interaction
- **No touched state management**: Field may not properly track interaction
- **Silent failures**: Users receive no feedback when validation fails

## Display Behaviour

### Expanded Checklist Mode (`expandedChecklist: true`)

| Platform | Rendering | Touch Target | Performance | Issues |
|----------|-----------|--------------|-------------|---------|
| Desktop | Vertical checkbox list | ~42px per row | 20+ options: lag | No search/filter |
| iOS | MUI checkboxes | Entire row clickable | 50+ options: slow | No haptic feedback |
| Android | MUI checkboxes | Meets 48px standard | 100+ options: unusable | No native feel |

### Dropdown Mode (default)

| Platform | Rendering | Touch Target | Performance | Issues |
|----------|-----------|--------------|-------------|---------|
| Desktop | MUI Select with checkboxes | Standard click | 30+ options: sluggish | No search function |
| iOS | Portal-based dropdown | ~48px MenuItems | 75+ options: very slow | Not native picker |
| Android | Portal-based dropdown | Material ripple effect | 150+ options: unusable | Requires precise tap |

### Visual Characteristics
- **Checklist**: Each option as FormControlLabel with checkbox
- **Dropdown**: Shows comma-separated selected values when closed
- **Exclusive options**: Automatically disable other options when selected
- **Label HTML**: Supports sanitised HTML via DOMPurify
- **No virtualisation**: All options render immediately

## Interaction Patterns

### Standard Multi-Selection Flow
1. **Checklist mode**: Click anywhere on option row to toggle
2. **Dropdown mode**: Click field to open, then click checkboxes
3. **Selection updates**: Immediate array update on each change
4. **Visual feedback**: Checkbox fills/clears, dropdown updates display

### Exclusive Options Behaviour
When exclusive option selected (e.g., "none"):
1. All other selections immediately clear
2. Non-exclusive options become disabled
3. Only exclusive option remains selected
4. User must deselect exclusive to enable others

When regular option selected while exclusive active:
- **Checklist**: Selection blocked, no change occurs
- **Dropdown**: Options disabled, cannot select

### Keyboard Navigation
- **Tab**: Move between checkboxes (checklist) or to dropdown
- **Space**: Toggle individual checkbox
- **Enter**: Open dropdown / toggle checkbox
- **Arrow keys**: Navigate between options
- **No Shift/Ctrl selection**: Each item requires individual interaction

### Touch Interaction
- Label text IS clickable (unlike Checkbox field)
- Entire row acts as touch target in checklist mode
- Dropdown requires tap to open, then tap each option
- No swipe gestures supported

## Conditional Logic Support

### As Trigger (Array Operations)
```json
{
  "condition": {
    "field": "site-features",
    "operator": "contains",
    "value": "defensive"
  }
}
```

### Supported Array Operators
| Operator | Example | Description |
|----------|---------|-------------|
| `contains` | `{"operator": "contains", "value": "option1"}` | Array includes specific value |
| `contains-one-of` | `{"operator": "contains-one-of", "value": ["opt1", "opt2"]}` | Array includes ANY of values |
| `contains-all-of` | `{"operator": "contains-all-of", "value": ["opt1", "opt2"]}` | Array includes ALL values |
| `not-contains` | `{"operator": "not-contains", "value": "option1"}` | Array doesn't include value |
| `not-contains-one-of` | `{"operator": "not-contains-one-of", "value": ["opt1", "opt2"]}` | Array includes NONE of values |
| `equal` | `{"operator": "equal", "value": []}` | Check for empty array |

### As Target
MultiSelect can be conditionally shown/hidden based on other field values.

## Data Storage and Export

### Database Storage
- **Type**: Array of strings
- **Format**: `["option1", "option3", "option5"]`
- **Empty state**: `[]` (empty array, not null)
- **Order**: Maintains selection order

### CSV Export Behaviour
```csv
"Site Features","Other Field"
"defensive,domestic,industrial","Value2"
"defensive","Value3"
```

### Critical CSV Warning
- Arrays export as **comma-separated strings in single column**
- ⚠️ **Options containing commas break parsing**
- Example problem: "Pottery, ceramics" becomes indistinguishable from two selections
- **Best practice**: Never use commas in option values
- Alternative: Use semicolons or pipes in option text if separation needed

### JSON Export
```json
{
  "site-features": ["defensive", "domestic", "industrial"]
}
```

## Common Patterns

### Basic Multi-Selection with Validation
```json
{
  "artefact-materials": {
    "component-name": "MultiSelect",
    "component-parameters": {
      "label": "Artefact Materials",
      "required": true,
      "helperText": "Select all materials present",
      "ElementProps": {
        "expandedChecklist": true,
        "options": [
          {"value": "ceramic", "label": "Ceramic"},
          {"value": "glass", "label": "Glass"},
          {"value": "metal", "label": "Metal"},
          {"value": "bone", "label": "Bone"},
          {"value": "shell", "label": "Shell"},
          {"value": "stone", "label": "Stone"}
        ]
      }
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "Select at least one material"]
    ],
    "initialValue": []
  }
}
```

### Exclusive Options Pattern
```json
{
  "site-visibility": {
    "component-name": "MultiSelect",
    "component-parameters": {
      "label": "Visibility Conditions",
      "helperText": "Factors affecting site visibility",
      "ElementProps": {
        "expandedChecklist": true,
        "options": [
          {"value": "vegetation", "label": "Vegetation cover"},
          {"value": "erosion", "label": "Erosion"},
          {"value": "modern-development", "label": "Modern development"},
          {"value": "flooding", "label": "Seasonal flooding"},
          {"value": "excellent-visibility", "label": "Excellent visibility"},
          {"value": "not-accessed", "label": "Could not access"}
        ],
        "exclusiveOptions": ["excellent-visibility", "not-accessed"]
      }
    },
    "initialValue": []
  }
}
```

### Dropdown for Long Lists
```json
{
  "permits-required": {
    "component-name": "MultiSelect",
    "component-parameters": {
      "label": "Permits Required",
      "helperText": "Select all applicable permit types",
      "ElementProps": {
        "expandedChecklist": false,
        "options": [
          {"value": "aboriginal-heritage", "label": "Aboriginal Heritage"},
          {"value": "environmental", "label": "Environmental Protection"},
          {"value": "local-council", "label": "Local Council"},
          {"value": "state-heritage", "label": "State Heritage"},
          {"value": "commonwealth", "label": "Commonwealth Heritage"},
          {"value": "landowner", "label": "Landowner Permission"},
          {"value": "mining-lease", "label": "Mining Lease Access"},
          {"value": "national-parks", "label": "National Parks"},
          {"value": "crown-lands", "label": "Crown Lands"},
          {"value": "none-required", "label": "No permits required"}
        ],
        "exclusiveOptions": ["none-required"]
      }
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "Specify permit requirements"]
    ]
  }
}
```

### Migration from Multiple Checkboxes
```json
{
  "recording-methods": {
    "component-name": "MultiSelect",
    "component-parameters": {
      "label": "Recording Methods Used",
      "ElementProps": {
        "expandedChecklist": true,
        "options": [
          {"value": "photography", "label": "Photography"},
          {"value": "drawing", "label": "Scale drawing"},
          {"value": "gps", "label": "GPS coordinates"},
          {"value": "total-station", "label": "Total station"},
          {"value": "photogrammetry", "label": "Photogrammetry"}
        ]
      }
    },
    "initialValue": [],
    "meta": {
      "annotation": {
        "include": true,
        "label": "recording notes"
      }
    }
  }
}
```

## Troubleshooting Guide

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Required field passes when empty | `["yup.required"]` accepts `[]` | Use `["yup.min", 1]` instead |
| Performance lag with 20+ options | All options render immediately | Consider dropdown mode or reduce options |
| CSV export breaks | Commas in option values | Remove commas from all option values |
| Can't see validation errors | No error display implementation | Check form submission prevention for validation |
| Labels not clickable | Wrong mode or version | Ensure expandedChecklist mode is enabled |
| Can't select after choosing "None" | Exclusive option behaviour | Deselect exclusive option first |
| No keyboard multi-select | Not implemented | Use Space/Enter on each item individually |
| Options don't load dynamically | Static vocabularies only | Define all options at design time |

### Debug Checklist
- [ ] Verify `initialValue: []` not `initialValue: ""`
- [ ] Check validation uses `yup.min` not just `yup.required`
- [ ] Confirm no commas in option values
- [ ] Count options - consider mode change if >20 (checklist) or >30 (dropdown)
- [ ] Test exclusive options work bidirectionally
- [ ] Verify array operators in conditional logic (not string operators)
- [ ] Check Designer value=label for human-readable exports
- [ ] Test on mobile devices for touch target adequacy

### Migration from Multiple Checkboxes
When converting from individual Checkbox fields:
1. Change data structure from multiple booleans to single array
2. Update conditional logic from `equal: true` to `contains: "value"`
3. Revise validation from individual `yup.bool` to `yup.array` with `min`
4. Update export processing to handle comma-separated values
5. Test exclusive options if replacing radio+checkbox combination

## Implementation Notes

### Technical Characteristics
- **Two-component implementation**: ExpandedChecklist and MuiMultiSelect classes
- **Real checkbox elements**: Uses MUI Checkbox in both modes (not custom)
- **Label association**: FormControlLabel properly links labels to checkboxes
- **HTML sanitisation**: All labels processed through DOMPurify
- **Validation timing**: Runs on change but doesn't display errors
- **Touch state**: Not properly managed, may not mark as touched

### Current Limitations
- **No error display**: Validation messages never shown to users
- **No accessibility**: Missing ARIA attributes (on roadmap)
- **No search/filter**: Type-ahead limited to first character
- **No virtualisation**: Performance degrades rapidly with options
- **Static only**: No dynamic vocabulary loading (offline requirement)
- **No keyboard shortcuts**: Shift/Ctrl selection not supported

### Improvements Over Related Fields
- **Labels clickable**: Unlike Checkbox field's broken label association
- **Multiple selection**: Solves RadioGroup/Select single-selection limit
- **Group validation**: Single field instead of multiple checkboxes
- **Exclusive options**: Sophisticated mutual exclusivity handling
- **Array operators**: Comprehensive conditional logic support

## Best Practices

### Mode Selection Guidelines
**Use Expanded Checklist when**:
- ≤15 options for optimal performance
- Users need to see all options simultaneously
- Screen space permits vertical layout
- Exclusive options require clear visibility
- Recording multiple common selections

**Use Dropdown Mode when**:
- \>15 options or space constrained
- Options are mutually familiar to users
- Mobile screen space is limited
- Selections are typically few from many

### Option Design
- Keep option count under 20 for checklist, 30 for dropdown
- Never include commas in option values
- Order options logically (alphabetical, frequency, or categorical)
- Include exclusive options at list end
- Use clear, concise labels

### Validation Strategy
- Always use `["yup.min", 1]` for required multi-selects
- Document validation rules in helperText
- Consider maximum selections for data quality
- Test empty array behaviour thoroughly

### Data Quality
- Establish controlled vocabularies early
- Plan for offline operation (static options)
- Consider future vocabulary import capabilities
- Document exclusive option semantics
- Train users on checklist vs dropdown modes

### Performance Optimisation
- Monitor option count thresholds
- Switch modes based on performance testing
- Consider breaking very long lists into categories
- Test on target devices, especially older mobile
- Plan for vocabulary refinement based on usage

## Cross-References & Dependencies

### Migration Sources
- **[Checkbox](./Checkbox.md)** - When multiple related checkboxes need group validation, migrate to MultiSelect with expandedChecklist
- **[RadioGroup](./RadioGroup.md) + [Checkbox](./Checkbox.md)** - Common pattern of "Select one" + "None of the above" better handled by MultiSelect with exclusive options

### Alternative Approaches
- **Multiple [Checkbox](./Checkbox.md) fields** - Use when each option needs individual validation or metadata
- **[Select](./Select.md)** - Use for single selection from same option list
- **[AdvancedSelect](./AdvancedSelect.md)** - For hierarchical vocabularies (when available)

### Common Companions
- **[TextField](./TextField.md)** - "Other (specify)" pattern with conditional display
- **[Annotation](./MetaFields.md)** - Additional context for complex selections

### Data Flow Relationships
- **[Conditional Logic](../guides/ConditionalLogic.md)** - Array operators for complex conditions
- **[CSV Export](../guides/DataExport.md)** - Comma-separation issues and processing requirements
- **[Validation Patterns](../guides/ValidationPatterns.md)** - Array validation examples

### See Also
- **[Choice Field Comparison](../guides/ChoiceFields.md)** - Decision matrix for field selection
- **[Performance Guide](../guides/Performance.md)** - Option count thresholds
- **[Accessibility Roadmap](../guides/Accessibility.md)** - Future ARIA implementation
- **[Vocabulary Management](../guides/Vocabularies.md)** - Upcoming import capabilities

---

*Component Status: Production-ready with documented limitations. Accessibility improvements planned. Static vocabularies required for offline operation.*