# RadioGroup Field - Complete Third-Draft Documentation

## Overview

The RadioGroup field (`faims-custom::RadioGroup`) provides single selection from 2–10 mutually exclusive options through radio button interface, returning `faims-core::String` values. Distinguished by its problematic toggle deselection behaviour—clicking a selected option clears the selection but this only works via mouse/touch, not keyboard—this field type suffers from severe accessibility violations and usability issues. **Critical limitation**: The field displays NO error messages (only color changes) and has no ARIA attributes for screen readers. Options are statically defined at design time with no support for dynamic loading, vocabulary integration, or validation against defined values. Performance degrades severely above 20 options due to markdown parsing overhead. The component enforces vertical layout only and provides no Designer preview capability.

## Common Use Cases

• **Condition assessments** - Rating heritage fabric condition (Excellent/Good/Fair/Poor) with ≤5 options
• **Binary archaeological decisions** - Presence/absence with explicit "Unknown" option (consider Checkbox instead)
• **Likert scale responses** - Survey questions with 3-7 point scales (avoid >10 options due to performance)
• **Material type classification** - Quick selection from common materials (Stone/Brick/Timber/Metal/Other)
• **Temporal period selection** - Archaeological periods (limit to major periods only)
• **Data quality indicators** - Confidence levels (Certain/Probable/Possible) - keep options minimal
• **Workflow branching** - Form navigation decisions that trigger conditional field display

⚠️ **WARNING**: Due to critical limitations, consider using Select instead for production deployments.

## Core Configuration

### Required Parameters

```json
{
  "component-namespace": "faims-custom",
  "component-name": "RadioGroup",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "label": "Select one option",
    "ElementProps": {
      "options": [
        {"value": "opt1", "label": "Option 1"},
        {"value": "opt2", "label": "Option 2"}
      ]
    }
  }
}
```

### Optional Parameters with Defaults

```json
{
  "component-parameters": {
    "id": "radio-field-1",  // Default: same as name
    "helperText": "",  // Default: empty string
    "fullWidth": false,  // Default: false (JSON only, not in Designer)
    "variant": "outlined",  // Default: "outlined"
    "required": false,  // Default: false
    "disabled": false,  // Default: false (JSON only)
    "advancedHelperText": "",  // Default: empty string
    "FormLabelProps": {},  // Default: empty object (JSON only)
    "FormHelperTextProps": {}  // Default: empty object (JSON only)
  },
  "validationSchema": [["yup.string"]],  // Default: string validation only
  "initialValue": "",  // Default: empty string (ALWAYS in Designer)
  "meta": {
    "annotation": {"include": false, "label": "annotation"},  // Default: disabled
    "uncertainty": {"include": false, "label": "uncertainty"},  // Default: disabled
    "persistent": false,  // Default: false
    "displayParent": false  // Default: false
  }
}
```

### Designer vs JSON Configuration

**Designer GUI Exposes**:
- Label, Field ID, Helper Text, Advanced Helper Text
- Options list with drag-drop reordering (manual entry only)
- Required checkbox (adds `yup.required` only)
- Annotation/Uncertainty toggles
- Conditional logic builder (visibility only)
- Persistent and Display Parent checkboxes
- **NO preview capability** - configuration only

**JSON-Only Properties**:
- `fullWidth`: Control field width behaviour
- `disabled`: Disable entire RadioGroup
- `FormLabelProps`: MUI label customization
- `FormHelperTextProps`: MUI helper customization
- Complex validation beyond required (e.g., `yup.oneOf`)
- Initial value setting (always "" in Designer)

## Validation Rules

### Critical Validation Limitations

⚠️ **MAJOR BUG**: RadioGroup displays NO error messages - only shows red color when invalid. Users receive no text feedback about what's wrong.

| Validation Type | Configuration | Error Message | Actual Display | Designer Support |
|-----------------|---------------|---------------|----------------|------------------|
| Required field | `["yup.required", "Selection required"]` | "Selection required" | ❌ Red color only | ✅ Checkbox |
| String type | `["yup.string"]` | Automatic | ❌ No message | ✅ Default |
| One of values | `["yup.oneOf", ["yes","no"], "Invalid"]` | "Invalid" | ❌ No message | ❌ JSON only |
| Not null | `["yup.notOneOf", [null], "Must select"]` | "Must select" | ❌ No message | ❌ JSON only |
| Conditional required | Not supported | - | - | ❌ Not possible |

### Validation Timing Behaviour

1. **Form Load**: Validation runs but errors hidden (field not touched)
2. **First Interaction**: Field marked touched, turns red if invalid (no message)
3. **Deselection**: Clicking selected option sets null, shows red color immediately
4. **Submit Attempt**: All untouched fields marked touched, red colors appear

### Missing Validation Features

- **No option validation**: System doesn't validate values match defined options
- **No conditional validation**: Cannot make field conditionally required
- **No error text display**: Only color change, no FormHelperText implementation
- **No custom messages**: Error messages configured but never shown

## Display Behaviour

### Platform Rendering

| Platform | Radio Style | Touch Target | Accessibility | Known Issues |
|----------|-------------|--------------|---------------|--------------|
| Desktop (Web) | MUI custom SVG | ~42px default | ❌ No ARIA | Deselection via mouse only |
| iOS (Safari) | MUI custom SVG | ~42px (below 44px standard) | ❌ No VoiceOver support | No keyboard deselection |
| Android (WebView) | MUI custom SVG | ~42px default | ❌ No TalkBack support | Performance issues >20 options |

### Visual Characteristics

- **Layout**: Fixed vertical arrangement, no horizontal option
- **Spacing**: `marginBottom: 1` between options
- **Alignment**: `flex-start` for multi-line labels
- **Label formatting**: Markdown parsing causes performance issues
- **Preview**: NO Designer preview - must test on actual devices
- **Error display**: Red color only, no error messages shown

### Performance Degradation

| Options | Render Time | User Experience | Recommendation |
|---------|-------------|-----------------|----------------|
| 1-5 | <100ms | Smooth | ✅ Use RadioGroup |
| 6-10 | ~200ms | Acceptable | ⚠️ Consider Select |
| 11-20 | ~500ms | Noticeable lag | ❌ Use Select |
| 21-50 | 2-3 seconds | Severe stuttering | ❌ Unusable |
| 50+ | 5+ seconds | Browser may freeze | ❌ Will crash mobile |

Every option runs through markdown parsing + HTML sanitization with no optimization.

## Interaction Patterns

### Click/Tap Behaviour

**Standard Selection**:
1. User clicks/taps unselected option
2. Radio fills, previous selection clears
3. Field value updates immediately
4. Field marked touched, turns red if required and null

**Deselection (Broken Implementation)**:
1. **Mouse/Touch**: Click selected option → deselects to null ✅
2. **Keyboard**: Space on selected option → NO EFFECT ❌
3. **Screen Reader**: Cannot deselect at all ❌
4. No visual indication this feature exists

### Keyboard Navigation

| Key | Expected Action | Actual Behavior | Accessibility Issue |
|-----|-----------------|-----------------|---------------------|
| Tab | Focus field | ✅ Works | - |
| Arrow Up/Down | Navigate options | ✅ Works (MUI default) | - |
| Space | Select focused | ✅ Works | - |
| Space (on selected) | Deselect | ❌ DOES NOT WORK | WCAG 2.1 violation |
| Delete/Backspace | Clear selection | ❌ Not implemented | - |

**CRITICAL**: Keyboard users cannot deselect once selected - accessibility barrier.

### Accessibility Failures

**Missing ARIA Attributes**:
- ❌ No `aria-required` for required fields
- ❌ No `aria-invalid` for error states
- ❌ No `aria-errormessage` for validation
- ❌ No `aria-describedby` for helper text
- ❌ No announcement of deselection capability

**Screen Reader Issues**:
- Required state not announced (visual asterisk only)
- Error state not announced (color change only)
- Deselection feature completely hidden
- Markdown labels may read incorrectly

## Conditional Logic Support

### Critical Limitation: No Empty State Detection

Cannot check if RadioGroup is unselected/empty. Must check for specific values only.

### Working Patterns

```json
{
  "condition": {
    "operator": "equal",
    "field": "material-type",
    "value": "other"
  }
}
```

### Operators That Work

| Operator | Syntax | Example | Detects Null/Empty |
|----------|--------|---------|-------------------|
| equal | `"operator": "equal"` | value === "yes" | ❌ No |
| not-equal | `"operator": "not-equal"` | value !== "yes" | ❌ No |
| regex | `"operator": "regex"` | Pattern match | ❌ No |
| or | Multiple conditions | Any match | ❌ No |

### What DOESN'T Work

- ❌ No `isEmpty` operator
- ❌ Cannot detect deselected state
- ❌ Cannot check for "any value"
- ❌ Cannot make field conditionally required
- ❌ Cannot filter options based on other fields

### Option-Specific Triggers

Different options CAN trigger different fields:
```json
{
  "detail-field-A": {
    "condition": {"operator": "equal", "field": "choice", "value": "optionA"}
  },
  "detail-field-B": {
    "condition": {"operator": "equal", "field": "choice", "value": "optionB"}
  }
}
```

## Data Storage and Export

### Internal Storage Format

```json
{
  "field-name": "value2",  // Selected option VALUE only
  "field-name_annotation": "User note",  // If annotation enabled
  "field-name_uncertainty": false  // If uncertainty enabled
}
```

### Export Limitations

| Format | Exported Value | Label Included | Post-Processing Required |
|--------|---------------|----------------|-------------------------|
| CSV | Raw value only | ❌ No | ✅ Must map values to labels |
| JSON | `"field": "value"` | ❌ No | ✅ Need config for labels |
| GeoJSON | Properties: value | ❌ No | ✅ Manual label lookup |

**Critical Issue**: Exports contain technical values, not human-readable labels. Recipients need field configuration to decode.

### Data Integrity Problems

- **No validation against options**: Invalid values preserved silently
- **No migration support**: Changed options don't update existing data
- **No referential integrity**: Values are plain strings with no validation
- **Empty vs null distinction**: Tracked internally but not useful

## Common Patterns

### Heritage Condition Assessment (Recommended Approach)

```json
{
  "component-namespace": "faims-custom",
  "component-name": "RadioGroup",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "fabric-condition",
    "label": "Fabric Condition",
    "helperText": "Click selected option to deselect (mouse only)",
    "fullWidth": true,
    "required": true,
    "ElementProps": {
      "options": [
        {"value": "excellent", "label": "Excellent"},
        {"value": "good", "label": "Good"},
        {"value": "fair", "label": "Fair"},
        {"value": "poor", "label": "Poor"},
        {"value": "na", "label": "Not Applicable"}  // Include to avoid deselection
      ]
    }
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Condition required (message won't show)"],
    ["yup.oneOf", ["excellent","good","fair","poor","na"], "Invalid (won't show)"]
  ],
  "initialValue": "na",  // Default to prevent empty state
  "meta": {
    "annotation": {"include": true, "label": "Condition notes"}
  }
}
```

### Binary Choice - Use Select Instead

Due to RadioGroup limitations, use Select for nullable binary choices:

```json
{
  "component-namespace": "faims-custom",
  "component-name": "Select",  // Better than RadioGroup
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "has-feature",
    "label": "Feature Present?",
    "required": true,
    "ElementProps": {
      "options": [
        {"value": "", "label": "-- Select --"},
        {"value": "yes", "label": "Yes"},
        {"value": "no", "label": "No"},
        {"value": "unknown", "label": "Unknown"}
      ]
    }
  }
}
```

### Workflow Branching with Workarounds

```json
{
  "component-namespace": "faims-custom",
  "component-name": "RadioGroup",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "recording-type",
    "label": "Recording Type",
    "helperText": "Selection is permanent - cannot be cleared",
    "required": true,
    "ElementProps": {
      "options": [
        {"value": "full", "label": "Full Recording"},
        {"value": "rapid", "label": "Rapid Assessment"},
        {"value": "photo", "label": "Photo Only"}
      ]
    }
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.required"],
    ["yup.notOneOf", [null], "Must select"]  // Prevent deselection
  ],
  "initialValue": "rapid"  // Always provide default
}
```

### Migration from RadioGroup to Select

```json
{
  "component-namespace": "faims-custom",
  "component-name": "Select",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "material-type",
    "label": "Material Type",
    "helperText": "Select the primary material",
    "fullWidth": true,
    "required": true,
    "ElementProps": {
      "options": [
        {"value": "", "label": "-- Select Material --"},
        {"value": "stone", "label": "Stone"},
        {"value": "brick", "label": "Brick"},
        {"value": "timber", "label": "Timber"},
        {"value": "metal", "label": "Metal"},
        {"value": "concrete", "label": "Concrete"},
        {"value": "other", "label": "Other"}
      ]
    }
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Material selection required"],
    ["yup.oneOf", ["stone","brick","timber","metal","concrete","other"], "Invalid material"]
  ],
  "initialValue": "",  // Empty string for placeholder
  "meta": {
    "annotation": {"include": true, "label": "Material notes"},
    "persistent": false,
    "displayParent": true
  }
}
```

## Troubleshooting Guide

### Critical Issues Without Solutions

| Issue | Cause | Workaround | Permanent Fix Needed |
|-------|-------|------------|---------------------|
| No error messages shown | Not implemented | Add helper text explaining requirements | ✅ Add FormHelperText |
| Cannot deselect via keyboard | Bug in implementation | Use Select instead | ✅ Fix keyboard handler |
| Screen reader incompatible | No ARIA attributes | Cannot fix - avoid RadioGroup | ✅ Add full ARIA |
| Performance >20 options | Markdown parsing overhead | Use Select for long lists | ✅ Add virtualization |
| Cannot detect empty state | No isEmpty operator | Add "None" option | ✅ Add operator |
| Exports missing labels | By design | Post-process with config | ✅ Export enhancement |

### Debug Checklist

**Field Not Appearing**:
- [ ] Check conditional logic on field (remember: no isEmpty operator)
- [ ] Verify field name is unique in form
- [ ] Confirm parent section is visible
- [ ] Check JSON syntax - Designer doesn't validate fully
- [ ] Verify field ID matches any condition references
- [ ] Check form mounting errors in console

**Validation Issues**:
- [ ] Remember: NO error messages will display (only red color)
- [ ] Verify required flag in Designer matches JSON
- [ ] Check initialValue is valid option or empty string (not null)
- [ ] Confirm validation schema array syntax is correct
- [ ] Test touched state - errors only show after interaction
- [ ] Check if yup.required message configured (won't display anyway)

**Selection Problems**:
- [ ] Verify option values are unique strings
- [ ] Check for duplicate option labels causing confusion
- [ ] Confirm no conflicting conditional logic on options
- [ ] Test deselection behaviour understanding with users
- [ ] Verify keyboard users informed they cannot deselect
- [ ] Check console for React key warnings

**Accessibility Testing**:
- [ ] Screen readers announce no error states (known bug)
- [ ] Required state not communicated via ARIA (known bug)
- [ ] Deselection impossible via keyboard (known bug)
- [ ] Test with NVDA/JAWS on Windows, VoiceOver on Mac
- [ ] Verify focus visible when tabbing through form
- [ ] Check color contrast meets WCAG standards

**Performance Testing**:
- [ ] Count total options - should be ≤10
- [ ] Check markdown complexity in labels
- [ ] Monitor render time in React DevTools
- [ ] Test on lowest-spec target device
- [ ] Check memory usage with many RadioGroups
- [ ] Verify no infinite re-render loops

**Export Verification**:
- [ ] Confirm exports show values not labels
- [ ] Check null vs empty string handling
- [ ] Verify annotation fields included if enabled
- [ ] Test CSV column headers match field names
- [ ] Check JSON structure for nested data

## Implementation Notes

### Critical Bugs and Limitations

1. **NO ERROR MESSAGES**: Only color change, no text feedback - major UX failure
2. **ACCESSIBILITY VIOLATIONS**: Fails WCAG 2.1 Level A requirements
3. **KEYBOARD DESELECTION BROKEN**: Only works with mouse/touch
4. **NO VOCABULARY SUPPORT**: Static options only, no dynamic loading
5. **NO OPTION VALIDATION**: Accepts any value, not just defined options
6. **PERFORMANCE ISSUES**: Severe degradation >20 options from markdown parsing
7. **NO CONDITIONAL VALIDATION**: Cannot make fields conditionally required
8. **NO EMPTY STATE DETECTION**: Conditions cannot check for unselected
9. **EXPORT USABILITY**: Only values exported, labels lost
10. **NO DESIGNER PREVIEW**: Cannot see field appearance before deployment

### Designer Constraints

**Available in Designer**:
- Basic field properties (label, helper text)
- Manual option entry with drag-drop
- Simple required validation checkbox
- Visibility conditions only

**Requires JSON Editing**:
- fullWidth property
- Complex validation rules
- disabled state
- Initial value setting
- MUI component props
- yup.oneOf validation

**Not Possible At All**:
- Conditional validation
- Dynamic options
- Vocabulary integration
- Horizontal layout
- Error message display
- Keyboard deselection

### Performance Analysis

**Rendering Cost Per Option**:
- Markdown parsing via markdown-it
- HTML sanitization via DOMPurify  
- ~10 DOM nodes created
- No virtualization or optimization

**At 50 Options**:
- 50× markdown operations
- 50× sanitization calls
- 500+ DOM nodes
- 2-3 second initial render
- Mobile devices may crash

## Best Practices

### Strong Recommendations

1. **USE SELECT INSTEAD**: For production deployments, Select is more reliable
2. **LIMIT TO 5 OPTIONS**: Performance and usability degrade rapidly above this
3. **ALWAYS PROVIDE DEFAULT**: Set initialValue to prevent empty state issues
4. **INCLUDE "NONE" OPTION**: Don't rely on deselection feature
5. **ADD WARNING TEXT**: Explain limitations in helper text
6. **TEST ACCESSIBILITY**: Verify keyboard navigation before deployment
7. **VALIDATE IN JSON**: Add yup.oneOf to ensure data integrity
8. **DOCUMENT WORKAROUNDS**: Team must know about limitations

### When to Use RadioGroup

**Marginally Acceptable For**:
- 2-5 options maximum
- Non-critical fields
- Mouse/touch only users
- No accessibility requirements

**Never Use For**:
- Required fields needing validation messages
- Accessible applications
- >10 options
- Dynamic/vocabulary-based options
- Production systems requiring data integrity

### Migration Strategy

**RadioGroup → Select Migration**:
```json
// FROM RadioGroup (problematic):
{
  "component-name": "RadioGroup",
  "ElementProps": {
    "options": [...]
  }
}

// TO Select (recommended):
{
  "component-name": "Select",
  "ElementProps": {
    "options": [
      {"value": "", "label": "-- Select --"},
      ...
    ]
  }
}
```

Benefits of migration:
- Error messages display properly
- Better accessibility support
- No deselection confusion
- Better performance with many options
- Standard keyboard behavior

## See Also

### Direct Alternatives
- **Select**: RECOMMENDED REPLACEMENT - Displays error messages properly, better accessibility, handles many options efficiently
- **Checkbox**: For true binary choices returning boolean values (different data type)

### Related Choice Fields
- **MultiSelect**: Multiple selections from same option set (also static options)
- **AdvancedSelect**: Hierarchical vocabularies for taxonomies (better for large sets)
- **RelatedRecordSelector**: Dynamic options from database (true vocabulary support)

### Field Dependencies & Relationships

**Common Pairings**:
- Often paired with conditional TextField for "Other - specify" patterns
- Frequently triggers conditional field groups based on selection
- Commonly used with annotation fields for qualification

**Validation Cascades**:
- RadioGroup selection can make other fields required via conditions
- Cannot participate in conditional validation (only visibility)
- Deselection to null may break dependent field conditions

**Mutual Exclusions**:
- Should not be used alongside Select for same data (confusing UX)
- Avoid multiple RadioGroups for related choices (use MultiSelect)

**Dependent Fields**:
- Conditional fields checking RadioGroup values fail on null/empty
- Export post-processing depends on having configuration for labels
- Annotation fields depend on RadioGroup having a value

---

⚠️ **FINAL WARNING**: RadioGroup has critical unresolved bugs and accessibility violations. Production deployments should use Select instead until RadioGroup implementation is fixed. This component should be considered deprecated pending a complete rewrite.