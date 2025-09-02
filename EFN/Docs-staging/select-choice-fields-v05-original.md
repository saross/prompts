# Selection and Choice Fields

## Overview {essential}

The Fieldmark ecosystem provides five selection/choice field types for controlled data entry through various interface patterns, each optimized for different selection scenarios and data structures:

### DESIGNER QUICK GUIDE
When using the Designer interface:
- ☑️ **Boolean toggle**: Choose **"Checkbox"**
- 📋 **Multiple selection**: Choose **"Select Multiple"** 
- 🔘 **Single choice (radio)**: Choose **"Select one option"**
- 📝 **Single choice (dropdown)**: Choose **"Select Field"**
- 🌳 **Hierarchical selection**: Choose **"Select Field (Hierarchical)"**

### CRITICAL NAMING DISAMBIGUATION
⚠️ **Designer UI names differ from component names**:
- **"Select Multiple"** in Designer = multi-select dropdown (component: MultiSelect)
- **"Select one option"** in Designer = radio buttons (component: RadioGroup)
- **"Select Field"** appears TWICE with different functionality:
  - Plain "Select Field" = standard dropdown (component: Select)
  - "Select Field (Hierarchical)" = tree selection (component: AdvancedSelect)

This naming inconsistency creates significant confusion. The RadioGroup name is particularly misleading as users see "Select one option" not "Radio" in Designer. Always verify the component-name in JSON when troubleshooting.

### Data Capture Fields (1-5)

1. **Checkbox** (appears as "Checkbox" in Designer) - Binary state capture through a Material-UI checkbox component, returning `faims-core::Boolean` values. As the **only boolean field type in Fieldmark**, serves dual purposes: simple true/false data capture and consent/acknowledgment workflows. Critical UX issue: label text is NOT clickable (must tap the small checkbox target), violating standard checkbox behaviour. Despite this, provides the most reliable error display among all choice fields.

2. **MultiSelect** (appears as "Select Multiple" in Designer) - Multiple value selection from predefined option lists, returning `faims-core::Array` values. Provides two distinct display modes—dropdown with checkboxes or expanded checklist—optimising for different option counts. Uniquely supports exclusive options (mutual exclusivity), where selecting "None" or "Unknown" automatically clears other selections. ⚠️ **Critical validation quirk**: Empty array [] passes "required" validation - must use `yup.min(1)` instead.

3. **RadioGroup** (appears as "Select one option" in Designer) - Single selection from 2–10 mutually exclusive options through radio button interface, returning `faims-core::String` values. Distinguished by problematic toggle deselection behaviour—clicking selected option clears selection but only works via mouse/touch, not keyboard. **Critical limitation**: Displays NO error messages (only color changes) and has no ARIA attributes. Performance degrades severely above 20 options. **Production deployments should use Select instead**.

4. **Select** (appears as "Select Field" in Designer) - Single-choice selection from dropdown list, offering space-efficient presentation of controlled vocabularies. Returns `faims-core::String` values and serves as standard solution for single selection from >5-7 options. Designer interface enforces sensible defaults, ensuring option values equal labels for human-readable exports. Lacks error message display and native mobile pickers but delivers reliable structured data collection.

5. **AdvancedSelect** (appears as "Select Field (Hierarchical)" in Designer) - Hierarchical tree navigation for selecting values from nested vocabularies, returning `faims-core::String` values representing either full paths or leaf nodes. **Currently in beta status** due to incomplete Designer integration, performance limitations, and multiple critical bugs including no error display, no clear/deselect capability, severe performance degradation beyond 100 nodes. **Production deployments should use Select with prefixed options until AdvancedSelect stabilises**.

### Component Status Summary

| Component | Status | Critical Issues | Mobile Support | Recommended |
|-----------|--------|-----------------|----------------|-------------|
| **Checkbox** | ✅ Production | Label not clickable | ✅ Full | ✅ Yes |
| **MultiSelect** | ✅ Production | Empty array validation quirk | ✅ Full | ✅ Yes |
| **RadioGroup** | ⚠️ Deprecated | No error messages, no keyboard deselect | ⚠️ Limited | ❌ Use Select |
| **Select** | ✅ Production | No error messages | ✅ Full | ✅ Yes |
| **AdvancedSelect** | 🔴 Beta | Can't clear selection, requires JSON editing | ❌ Broken | ❌ Avoid |

---

## Field Selection Guide {essential}

### Quick Decision Tree
What type of selection do you need?
│
├─ Boolean/binary state?
│  └─ YES → Checkbox
│     └─ Returns true/false boolean
│
├─ Multiple values from list?
│  └─ YES → MultiSelect
│     ├─ ≤15 options → Use expandedChecklist mode
│     └─ >15 options → Use dropdown mode
│
└─ Single value from list?
   ├─ Hierarchical/nested structure?
   │  └─ YES → Consider options:
   │     ├─ <100 nodes AND desktop-only → AdvancedSelect (⚠️ Beta)
   │     └─ Otherwise → Multiple cascading Selects
   │
   └─ Flat list of options?
      ├─ ≤7 options that should always be visible?
      │  └─ YES → Consider RadioGroup BUT prefer Select
      │     └─ ⚠️ RadioGroup deprecated (no error display)
      │
      └─ 8+ options OR need error messages?
         └─ YES → Select (dropdown)

### Quick Decision Matrix

| Field Type | Returns | Max Options | Error Display | Use When | Avoid When |
|------------|---------|-------------|---------------|----------|------------|
| **Checkbox** | Boolean | 1 (true/false) | ✅ Full | Binary states, consent | Multiple related options |
| **MultiSelect** | Array | ~50 practical | ❌ None | Multiple selections needed | Single choice required |
| **RadioGroup** | String | ~20 max | ❌ None | 2-7 visible options | Production forms (deprecated) |
| **Select** | String | ~100 practical | ❌ None | Single from many options | Boolean states |
| **AdvancedSelect** | String | ~100 max | ❌ None | Hierarchical taxonomies | Mobile, production (beta) |

### Selection Strategy

1. **Default to Select** for single-choice unless specific visual requirements
2. **Use Checkbox** for all boolean decisions (not RadioGroup with Yes/No)
3. **Prefer MultiSelect** over multiple individual Checkboxes for related options
4. **Avoid RadioGroup** in production due to missing error messages
5. **Test AdvancedSelect** thoroughly before production use (beta status)

### Platform Considerations

**Mobile Forms**:
- ❌ Avoid AdvancedSelect (500px fixed width breaks layout)
- ⚠️ Limit RadioGroup to 5 options (performance)
- ✅ Select and MultiSelect work well
- ⚠️ Checkbox label not tappable (small target)

**Data Export**:
- Checkbox → Boolean (true/false)
- Others → String or Array of strings
- Designer enforces value = label for readability
- Manual JSON editing can break export readability

---

## Designer Usage Guide {essential}

### What to Select in Designer

**For Boolean/Binary Choices**:
- ☑️ **Checkbox**: Use for true/false, yes/no, present/absent
  - Returns: Boolean (true/false)
  - Example: "Photos included", "Consent given"
  - ⚠️ Label not clickable - users must click checkbox directly

**For Multiple Selection**:
- 📋 **Select Multiple**: Use when users can choose several options
  - Returns: Array of strings
  - Example: "Site features present", "Materials observed"
  - Supports exclusive options like "None" that clear others
  - Choose expanded checklist mode for ≤15 options

**For Single Selection**:
- 🔘 **Select one option** (RadioGroup): Use for 2-7 visible options
  - Returns: String value
  - ⚠️ **DEPRECATED** - No error messages display
  - Consider Select instead for production

- 📝 **Select Field**: Use for 8+ options in dropdown
  - Returns: String value
  - Space-efficient for long lists
  - Designer ensures human-readable exports

- 🌳 **Select Field (Hierarchical)**: Use for taxonomies/hierarchies
  - Returns: String (full path or leaf node)
  - ⚠️ **BETA** - Requires JSON editing for hierarchy
  - Performance issues with >100 nodes

### When JSON Enhancement is Required

**All fields may need JSON editing for**:
- Complex validation rules beyond basic required
- Conditional logic based on selections
- Initial values (pre-selected options)
- Platform-specific configurations
- Performance optimizations

**Specific JSON-only features**:
- **Checkbox**: Setting `initialValue: true` for pre-checked
- **MultiSelect**: Configuring `exclusiveOptions` array
- **RadioGroup**: `fullWidth` property, complex validation
- **Select**: Different values vs labels (not recommended)
- **AdvancedSelect**: **Entire hierarchy structure** (critical limitation)

### Quick Use Case Examples

**Binary Decisions**:
- Heritage present/absent → Checkbox
- Consent forms → Checkbox with `yup.oneOf([true])`
- Yes/No/Unknown → Select (not RadioGroup)

**Multiple Characteristics**:
- Site features → MultiSelect with checklist
- Conservation treatments → MultiSelect
- Equipment used → MultiSelect with exclusive "None"

**Single Classification**:
- Material type → Select for 10+ options
- Condition rating → RadioGroup for 3-5 visible options (or Select)
- Taxonomic classification → AdvancedSelect (if <100 nodes)

**What These Fields Cannot Do**:
- Dynamic option loading (all static)
- Cross-field validation (no yup.when)
- Custom error messages (most don't display any)
- Keyboard-only deselection (RadioGroup bug)
- Search within hierarchies (AdvancedSelect)

---

## Designer Component Mapping {essential}

### Designer UI vs JSON Component Names

| Designer UI Label | JSON component-name | Component Namespace | Type Returned | Description |
|------------------|--------------------|--------------------|---------------|-------------|
| Checkbox | Checkbox | faims-custom | faims-core::Boolean | Boolean true/false field |
| Select Multiple | MultiSelect | faims-custom | faims-core::Array | Multi-selection dropdown/checklist |
| Select one option | RadioGroup | faims-custom | faims-core::String | Radio button group (deprecated) |
| Select Field | Select | faims-custom | faims-core::String | Standard dropdown list |
| Select Field (Hierarchical) | AdvancedSelect | faims-custom | faims-core::String | Tree selection (beta) |

⚠️ **Critical Naming Confusion**:
- **"Select Multiple"** in Designer creates `MultiSelect` component (not "SelectMultiple")
- **"Select one option"** creates `RadioGroup` (not "SelectOne" or "Radio")
- **"Select Field"** appears TWICE in Designer with different functionality:
  - Plain version → `Select` component
  - Hierarchical version → `AdvancedSelect` component
- There is NO Designer element called "RadioGroup" despite that being the component name

This mapping is essential for:
- Debugging validation issues (component names appear in error logs)
- Writing JSON configurations manually
- Understanding conditional logic that references field names
- Troubleshooting export data (component-name affects data structure)

### Designer Limitations Requiring JSON

**Cannot be configured in Designer**:
- AdvancedSelect hierarchy structure (must hand-edit `optiontree`)
- Exclusive options for MultiSelect (must add `exclusiveOptions` array)
- Initial values for any field (must set `initialValue`)
- Complex validation beyond basic required
- Conditional field visibility
- Performance optimizations

---

## Designer Capabilities vs JSON Enhancement {essential}

### What Designer CAN Configure

| Field Type | Designer Capabilities | Notable Limitations |
|------------|----------------------|---------------------|
| **Checkbox** | Label, helper text, required flag | Cannot set pre-checked state |
| **MultiSelect** | Options list, expanded mode toggle, per-option exclusive flag | Cannot set exclusive options array directly |
| **RadioGroup** | Options list, required flag | Cannot preview appearance |
| **Select** | Options list, required flag | Forces value = label (good for exports) |
| **AdvancedSelect** | Basic field properties only | Cannot define hierarchy at all |

### What Requires JSON Editing

**Essential JSON-only features**:
1. **Validation rules** beyond simple required (e.g., `yup.min(1)` for MultiSelect)
2. **Initial values** for pre-population
3. **Conditional logic** for field dependencies
4. **Meta properties** (persistent, annotation, uncertainty)
5. **Performance settings** (fullWidth, variant)
6. **AdvancedSelect hierarchy** (entire tree structure)

**Common JSON enhancements**:
```json
{
  "validationSchema": [
    ["yup.array"],
    ["yup.min", 1, "Select at least one"]  // Designer can't configure
  ],
  "initialValue": ["default-option"],  // Designer can't set
  "meta": {
    "persistent": true  // Designer can't configure
  }
}
```

### Designer vs JSON Workflow

**Use Designer when**:
- Creating basic selection fields
- Defining option lists for flat structures
- Setting labels and helper text
- Establishing field order and sections

**Switch to JSON when**:
- Implementing complex validation
- Setting up field dependencies
- Configuring hierarchical data (AdvancedSelect)
- Optimizing for specific platforms
- Adding initial values or defaults

---

## Component Namespace Errors {important}

### Troubleshooting "Component not found" Errors

If you see "Component not found" or rendering errors, verify the namespace matches the component:

| Component | Required Namespace | Common Mistake | Error Message |
|-----------|-------------------|----------------|---------------|
| Checkbox | faims-custom | Using formik-material-ui | "Component Checkbox not found" |
| MultiSelect | faims-custom | Using formik-material-ui | "Component MultiSelect not found" |
| RadioGroup | faims-custom | Using formik-material-ui | "Component RadioGroup not found" |
| Select | faims-custom | Using formik-material-ui | "Component Select not found" |
| AdvancedSelect | faims-custom | Using formik-material-ui | "Component AdvancedSelect not found" |

⚠️ **Critical Note**: ALL selection fields use `faims-custom` namespace. There are NO selection components in `formik-material-ui` namespace.

**Quick Fix Pattern**:
```json
// ❌ Wrong namespace (common copy-paste error)
{
  "component-namespace": "formik-material-ui",
  "component-name": "Select"  // Will fail!
}

// ✅ Correct namespace
{
  "component-namespace": "faims-custom",
  "component-name": "Select"  // Works!
}
```

### Common Namespace Confusion Points

**Why this happens**:
1. Text fields mix namespaces (some use formik-material-ui)
2. Copy-pasting from text field examples
3. Designer auto-generates correct namespace but manual JSON editing can break it
4. No runtime validation of namespace-component pairs

**Debugging steps**:
1. Check browser console for "Component not found" errors
2. Verify `component-namespace` is "faims-custom"
3. Verify `component-name` matches exactly (case-sensitive)
4. Check for typos in component name

---

## ⚠️ CRITICAL SELECTION FIELD RISKS {essential}

**Validation Display Failures**:
- **RadioGroup**: Shows NO error messages - only red color when invalid
- **Select**: No error display implementation - validation fails silently
- **MultiSelect**: Validation runs but messages never appear in UI
- **AdvancedSelect**: Validation errors never shown to users
- **Impact**: Users receive no feedback about what's wrong
- **Mitigation**: Use explicit helperText explaining all requirements

**Accessibility Violations (WCAG 2.1 Level A)**:
- **Checkbox**: No ARIA attributes, label not programmatically associated
- **RadioGroup**: No aria-required, aria-invalid, or aria-describedby
- **All fields**: Screen readers cannot announce error states
- **Impact**: Unusable for users requiring assistive technology
- **Mitigation**: Document limitations, plan for accessibility rewrite

**Data Integrity Issues**:
- **MultiSelect empty array**: `["yup.required"]` considers `[]` as valid
- **RadioGroup deselection**: Keyboard users cannot deselect once selected
- **AdvancedSelect clearing**: Cannot clear selection once made (critical UX bug)
- **Impact**: Invalid data states, user frustration, form abandonment
- **Mitigation**: Use appropriate validation (`yup.min(1)`), provide workarounds

**Performance Degradation**:
- **RadioGroup**: Severe issues >20 options due to markdown parsing
- **AdvancedSelect**: Unusable >100 nodes, no virtualization
- **MultiSelect**: Performance lag with >50 options in checklist mode
- **Impact**: Browser freezing, mobile crashes, poor user experience
- **Mitigation**: Limit option counts, use appropriate field types

**Platform-Specific Failures**:
- **AdvancedSelect mobile**: Fixed 500px width causes horizontal scrolling
- **RadioGroup keyboard**: Space key cannot deselect (mouse/touch only)
- **Checkbox label**: Not clickable on any platform
- **Impact**: Mobile users struggle, keyboard navigation broken
- **Mitigation**: Test on all target platforms, document workarounds

---

## What These Fields Cannot Do {important}

### Selection Processing Limitations {important}
- **Dynamic options** - All options must be predefined in JSON configuration. Cannot fetch options from API, database, or generate based on user input or other field values
- **Filtered options** - Cannot dynamically show/hide options based on other field selections. All options always visible regardless of context
- **Search capability** - No real-time filtering or type-ahead search. Select field has single-character jump that resets after ~1 second. AdvancedSelect has no search at all
- **Bulk operations** - MultiSelect lacks "select all" or "clear all" buttons. Users must manually check/uncheck each option individually
- **Keyboard shortcuts** - No Shift+Click for range selection in MultiSelect. No Ctrl+A for select all. RadioGroup Space key deselection broken
- **Option validation** - Fields accept ANY string value programmatically, not just defined options. No enforcement that selected value exists in options list

### Validation Limitations {important}
- **Cross-field validation** - `yup.when()` not supported for conditional requirements. Cannot make field required based on another field's value
- **Custom error display** - RadioGroup, Select, MultiSelect, and AdvancedSelect cannot display error message text - only Checkbox shows errors properly
- **Async validation** - No ability to validate against server/database during entry. All validation must be synchronous and client-side
- **Group validation** - Cannot enforce "at least one of these checkboxes" across multiple Checkbox fields. Must use MultiSelect for this pattern
- **Option membership** - Validation doesn't check if submitted value matches defined options. Can programmatically set invalid values

### Display Limitations {important}
- **Native controls** - Always uses Material-UI components, never iOS/Android native pickers. No platform-specific date wheels or selection interfaces
- **Horizontal layout** - RadioGroup only supports vertical layout. Cannot display radio buttons in a row. No grid layouts for any selection field
- **Preview in Designer** - Cannot test interaction or see actual rendering in Designer. Must deploy to development environment to verify appearance
- **Clear buttons** - No "×" clear button on any field. Select requires empty option. AdvancedSelect has no clear mechanism at all (critical bug)
- **Icons or images** - Options are text-only. Cannot add icons, colors, or images to options. No rich text or HTML in labels

### Interaction Limitations {important}
- **Deselection bugs** - RadioGroup Space key cannot deselect on keyboard (mouse only). AdvancedSelect cannot be cleared at all once selected
- **Touch targets** - Checkbox label not tappable (48×48px box only). AdvancedSelect chevrons too small (24×24px) for mobile guidelines
- **Gesture support** - No swipe to select multiple in MultiSelect. No long-press for context menu. No pinch-zoom for hierarchies
- **Multi-select keyboard** - Cannot use Shift+Click for range or Ctrl+Click for individual selection in MultiSelect. Each option requires separate interaction
- **Undo capability** - No built-in undo for selections. No revision history. Accidental changes cannot be reverted except by manual re-selection

---

## Common Use Cases {important}

### Archaeological and Heritage Recording

**Site Classification**:
- **Site types** → Select with 10-50 controlled vocabulary options (e.g., "Aboriginal scarred tree", "Shell midden", "Rock shelter"). Include empty option "-- Not classified --" for incomplete assessments
- **Feature presence** → MultiSelect with expandedChecklist for visibility (e.g., "Stone tools", "Bone fragments", "Charcoal"). Use exclusive option "No features observed" that clears all others
- **Condition assessment** → Select dropdown with 5-7 standardised states ("Excellent", "Good", "Fair", "Poor", "Destroyed", "Not assessed"). Avoid RadioGroup due to error display issues
- **Heritage compliance** → Checkbox with boolean true/false. For legal compliance use `yup.oneOf([true])` validation to enforce checking

**Material Culture**:
- **Artefact materials** → MultiSelect for composite objects that contain multiple materials ("Ceramic", "Glass", "Metal", "Organic"). Set `yup.min(1)` validation to ensure at least one material recorded
- **Preservation state** → Select dropdown with controlled terms ("Complete", "Near complete >75%", "Partial 25-75%", "Fragment <25%"). Include annotations for uncertainty
- **Manufacturing technique** → AdvancedSelect hierarchy only if <100 nodes and desktop-only access. Otherwise use cascading Selects (Period → Technique → Specific method)
- **Complete/fragmentary** → Checkbox boolean for simple binary state. Consider persistent meta to carry forward common states between records

### Scientific Data Collection

**Taxonomic Classification**:
- **Species identification** → AdvancedSelect with `valuetype: "full"` for complete taxonomic path if <100 taxa. For larger taxonomies use cascading Selects (Kingdom → Phylum → Class → Order → Family → Genus → Species)
- **Multiple species present** → MultiSelect with searchable dropdown (not expanded) for long species lists. Include "Unknown species" as exclusive option
- **Confidence level** → Select with standard scale ("Certain", "Probable", "Possible", "Unknown"). Never use RadioGroup due to inability to show validation errors
- **Specimen collected** → Checkbox with annotation capability for collection details. Set persistent meta if commonly collected

**Environmental Conditions**:
- **Visibility factors** → MultiSelect with exclusive options like "Excellent visibility" that auto-clears negative factors. Limit to <20 options for performance
- **Weather conditions** → Select single choice from meteorological standards ("Clear", "Partly cloudy", "Overcast", "Light rain", "Heavy rain"). Include timestamp in metadata
- **Seasonal indicators** → Select (not RadioGroup) with 4 seasons plus "Transitional" option. RadioGroup's lack of error messages makes it unsuitable
- **Data quality flags** → Individual Checkbox fields for critical flags that need separate validation (e.g., "GPS accuracy <5m", "Photos taken", "Measurements verified")

### Administrative Workflows

**Consent and Compliance**:
- **Terms acceptance** → Checkbox with `yup.oneOf([true], "You must accept the terms")` validation. Never use simple required validation as it allows false
- **Permit types required** → MultiSelect allowing multiple permit selection. Use dropdown mode for long permit lists. No exclusive options needed
- **Approval status** → Select with workflow states ("Draft", "Submitted", "Under review", "Approved", "Rejected"). Include empty option for new records
- **Confidential data flag** → Checkbox that triggers conditional fields for classification level and handling instructions

**Quality Assurance**:
- **Review status** → Select with linear progression ("Not reviewed", "In progress", "Review complete", "Approved", "Requires revision"). Track changes via annotations
- **Issues identified** → MultiSelect with expandedChecklist for visibility during review. Group related issues but keep under 15 total options
- **Peer reviewed** → Checkbox with annotation for reviewer name and date. Cannot enforce both reviewer fields due to validation limitations
- **Priority level** → Select (not RadioGroup) with ("Critical", "High", "Medium", "Low", "None"). RadioGroup cannot display required field errors

### Field Research Scenarios

**Geological Survey**:
- **Rock types observed** → MultiSelect with geological categories. Consider grouping by type (Igneous/Sedimentary/Metamorphic) in labels
- **Sample collected** → Checkbox linked to conditional sample ID field
- **Weathering grade** → Select with international standards (IRS 1-6 scale)
- **Structural features** → MultiSelect with exclusive "No structures" option

**Ecological Assessment**:
- **Habitat types** → MultiSelect with standardised ecosystem classifications. Limit options based on regional relevance
- **Disturbance indicators** → MultiSelect with exclusive "Pristine condition" that clears all disturbance options
- **Canopy cover** → Select with percentage ranges ("0-25%", "26-50%", "51-75%", "76-100%")
- **Invasive species present** → Checkbox triggering conditional MultiSelect for species list

### Data Entry Patterns

**Rapid Assessment Mode**:
- Use Select with common defaults pre-selected via initialValue
- Implement persistent meta on Checkboxes for frequently-used settings
- Prefer dropdown Select over RadioGroup for speed and error visibility
- Limit MultiSelect to essential multiple-choice scenarios

**Detailed Documentation Mode**:
- Use MultiSelect with expandedChecklist for comprehensive option visibility
- Include annotation meta on all critical fields
- Add uncertainty indicators where scientific accuracy matters
- Implement conditional fields for "Other" options requiring specification

**Mobile-Optimised Forms**:
- Avoid AdvancedSelect entirely (500px width breaks mobile)
- Limit RadioGroup to 5 options maximum (performance issues)
- Use Select dropdowns for space efficiency
- Keep MultiSelect under 30 options for performance

---

## Individual Field Reference

### Checkbox {essential}
<!-- keywords: boolean, consent, binary, toggle, checkbox -->

#### Purpose {essential}
Binary state capture returning `faims-core::Boolean` values. The **only boolean field type in Fieldmark**, serving dual purposes: simple true/false data capture and consent/acknowledgment workflows. Unlike RadioGroup and Select which return strings, Checkbox returns actual boolean primitives, making it ideal for programmatic logic.

#### Key Features {essential}
- **Boolean return type**: True/false primitives, not strings
- **Best error display**: Shows both red color AND error message text
- **Label positioning**: Displayed above by FieldWrapper
- **Persistent value**: Can carry forward to new records via meta
- **Visual feedback**: 300ms animation, ripple effect on click

**Critical UX Issue**: Label text is NOT clickable - users must tap the small 48×48px checkbox target, violating standard checkbox behaviour and making mobile interaction difficult.

#### Configuration Parameters {important}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "Checkbox",
  "type-returned": "faims-core::Boolean",
  "component-parameters": {
    "name": "field-name",
    "label": "Checkbox label",
    "id": "checkbox-field-1",
    "helperText": "Additional guidance",
    "advancedHelperText": "Extended help",
    "required": false  // Note: doesn't enforce "must be checked"
  },
  "validationSchema": [
    ["yup.boolean"],
    ["yup.oneOf", [true], "You must accept to continue"]  // For must-be-checked
  ],
  "initialValue": false,  // Designer enforces false
  "meta": {
    "annotation": {"include": false, "label": "notes"},
    "uncertainty": {"include": false},
    "persistent": false,
    "displayParent": false
  }
}
```

#### Validation Semantics {important}

| Validation Type | Configuration | Actual Behaviour | Platform Impact |
|-----------------|---------------|------------------|-----------------|
| Boolean type | `["yup.boolean"]` | Accepts true/false/null/undefined | Consistent |
| Required field | `["yup.required"]` | **Misleading!** Allows false | May confuse users |
| Must be checked | `["yup.oneOf", [true], "Message"]` | Only accepts true | Critical for consent |
| Must be unchecked | `["yup.oneOf", [false]]` | Only accepts false | Rare use case |

**Critical clarification**: "Required" for checkboxes does NOT mean "must be checked":
- `["yup.required"]` allows `false` (unchecked) as valid
- For consent forms use: `["yup.oneOf", [true], "You must accept"]`

#### Display and Interaction {important}

**Platform Rendering**:
- Desktop: 24×24px icon, 48×48px touch target
- iOS: Material-UI custom SVG (not native), no haptic feedback
- Android: Material-UI with ripple effect
- All platforms: Label NOT tappable (UX failure)

**State Transitions**:
- Unchecked → Checked: Click/tap checkbox, value becomes `true`
- Checked → Unchecked: Click/tap checkbox, value becomes `false`
- Initial state: Always `false` from Designer (JSON can set `true`)
- Null handling: null/undefined interpreted as `false`

**Accessibility Failures**:
- ❌ No aria-required attribute
- ❌ No aria-invalid for errors
- ❌ No aria-describedby for helper text
- ❌ Label not programmatically associated

#### Field-Specific Troubleshooting {important}

| Issue | Cause | Resolution |
|-------|-------|------------|
| Required not working | "Required" doesn't mean "must be checked" | Use `["yup.oneOf", [true]]` |
| Label not clickable | Label not properly associated | Train users to click checkbox |
| No initial checked | Designer forces false | Edit JSON for `initialValue: true` |
| Can't detect untouched | No isEmpty operator | Use different field or track separately |
| Multiple checkboxes | Can't enforce "at least one" | Use MultiSelect with checklist |

#### JSON Anti-patterns

❌ **Wrong validation for consent**:
```json
{
  "validationSchema": [
    ["yup.required"]  // This allows false!
  ]
}
```

✅ **Correct consent validation**:
```json
{
  "validationSchema": [
    ["yup.boolean"],
    ["yup.oneOf", [true], "You must accept the terms"]
  ]
}
```

❌ **Trying to make label clickable**:
```json
{
  "component-parameters": {
    "FormControlLabelProps": {"clickable": true}  // Doesn't work
  }
}
```

#### Spec Mapping

**Designer "Checkbox" configuration**:
- Label → `component-parameters.label`
- Helper text → `component-parameters.helperText`
- Required checkbox → Adds `["yup.required"]` (misleading for checkboxes)
- Field name → `component-parameters.name`

**Common patterns**:
```json
// Terms acceptance (must be checked)
{
  "component-name": "Checkbox",
  "validationSchema": [
    ["yup.boolean"],
    ["yup.oneOf", [true], "You must accept to proceed"]
  ]
}

// Optional flag (can be checked or unchecked)
{
  "component-name": "Checkbox",
  "validationSchema": [["yup.boolean"]],
  "meta": {"persistent": true}  // Carry forward
}

// Data quality indicator
{
  "component-name": "Checkbox",
  "meta": {
    "displayParent": true,
    "annotation": {"include": true}
  }
}
```

#### Implementation Examples {comprehensive}

**Terms Acceptance (Must Be Checked)**:
```json
{
  "terms-accept": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "terms-accept",
      "label": "I accept the terms and conditions",
      "helperText": "You must accept to continue",
      "required": true  // Visual indicator only
    },
    "validationSchema": [
      ["yup.boolean"],
      ["yup.oneOf", [true], "You must accept the terms to proceed"]
    ],
    "initialValue": false
  }
}
```

**Optional Enhancement Flag**:
```json
{
  "include-detailed": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "include-detailed",
      "label": "Record detailed measurements",
      "helperText": "Check to show additional measurement fields"
    },
    "validationSchema": [["yup.boolean"]],
    "initialValue": false,
    "meta": {
      "persistent": true  // Carry forward to new records
    }
  }
}
```

**Migration from RadioGroup Pattern**:
```json
{
  "heritage-present": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "heritage-present",
      "label": "Aboriginal heritage identified",
      "helperText": "Previously Yes/No radio - now checkbox for boolean logic",
      "required": true
    },
    "validationSchema": [
      ["yup.boolean"],
      ["yup.oneOf", [true, false], "Must explicitly indicate heritage status"]
    ],
    "initialValue": false,
    "meta": {
      "annotation": {"include": true, "label": "heritage notes"},
      "displayParent": true
    }
  }
}
```

---

### MultiSelect {essential}
<!-- keywords: multiple, selection, checklist, dropdown, array -->

#### Purpose {essential}
Multiple value selection from predefined option lists, returning `faims-core::Array` values. Provides two distinct display modes—dropdown with checkboxes or expanded checklist—optimising for different option counts and screen constraints. Unlike single-selection fields, MultiSelect handles group validation through a single field returning an array. Uniquely supports exclusive options (mutual exclusivity), where selecting "None" or "Unknown" automatically clears other selections.

#### Key Features {essential}
- **Array return type**: Returns array of strings, not single value
- **Two display modes**: Dropdown or expanded checklist
- **Exclusive options**: Mutual exclusivity support (e.g., "None" clears others)
- **Label clickable**: Unlike Checkbox, entire row is touch target in checklist
- **No virtualization**: Performance degrades with many options

**Critical validation quirk**: Empty array [] passes "required" validation - must use `yup.min(1)` for actual requirement.

#### Configuration Parameters {important}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "MultiSelect",
  "type-returned": "faims-core::Array",
  "component-parameters": {
    "name": "site-features",
    "id": "site-features",
    "label": "Site Features",
    "required": false,
    "helperText": "Select all that apply",
    "ElementProps": {
      "options": [
        {"value": "defensive", "label": "Defensive structures"},
        {"value": "domestic", "label": "Domestic occupation"},
        {"value": "industrial", "label": "Industrial remains"}
      ],
      "expandedChecklist": true,  // Display as checklist (default: false)
      "exclusiveOptions": ["none", "unknown"],  // Mutually exclusive values
      "fullWidth": true,
      "variant": "outlined"
    }
  },
  "validationSchema": [["yup.array"]],
  "initialValue": [],
  "meta": {
    "annotation": {"include": true, "label": "selection notes"},
    "uncertainty": {"include": false}
  }
}
```

#### Validation Rules {important}

| Validation Type | Configuration | Behaviour | Critical Note |
|-----------------|---------------|-----------|---------------|
| Required field | `["yup.required"]` | Checks not null/undefined | ⚠️ **Empty array [] PASSES** |
| Minimum selection | `["yup.min", 1, "Select at least one"]` | Enforces minimum | Use for "required" behaviour |
| Maximum selection | `["yup.max", 5, "Maximum 5"]` | Limits count | Not enforced during interaction |
| Array type | `["yup.array"]` | Ensures array | Default, always included |
| Specific values | `["yup.array"], ["yup.of", ["yup.oneOf", ["val1"]]]` | Restricts subset | Complex syntax |

**Critical behaviour**:
- NO ERROR DISPLAY: Validation runs but messages never appear
- Empty array gotcha: `["yup.required"]` considers `[]` as valid
- No proactive enforcement: Max selection not prevented during interaction

#### Display Modes {important}

**Expanded Checklist Mode** (`expandedChecklist: true`):
- Desktop: Vertical checkbox list, ~42px per row
- Mobile: Entire row clickable, meets 48px touch standard
- Performance: 20+ options cause lag, 100+ unusable
- No search/filter capability

**Dropdown Mode** (default):
- Desktop: MUI Select with checkboxes, standard click
- Mobile: Portal-based dropdown, ~48px MenuItems
- Shows comma-separated values when closed
- Performance: 30+ options sluggish, 150+ unusable

#### Exclusive Options Behaviour {important}

When exclusive option selected (e.g., "none"):
1. All other selections immediately clear
2. Non-exclusive options become disabled
3. Only exclusive option remains selected
4. User must deselect exclusive to enable others

```json
{
  "ElementProps": {
    "options": [
      {"value": "vegetation", "label": "Vegetation cover"},
      {"value": "erosion", "label": "Erosion"},
      {"value": "excellent-visibility", "label": "Excellent visibility"},
      {"value": "not-accessed", "label": "Could not access"}
    ],
    "exclusiveOptions": ["excellent-visibility", "not-accessed"]
  }
}
```

#### Field-Specific Troubleshooting {important}

| Issue | Cause | Solution |
|-------|-------|----------|
| Required field passes empty | `["yup.required"]` accepts `[]` | Use `["yup.min", 1]` instead |
| Performance lag 20+ options | All options render immediately | Use dropdown or reduce options |
| CSV export breaks | Commas in option values | Remove commas from values |
| Can't see validation errors | No error display | Check form submission prevention |
| Can't select after "None" | Exclusive option behaviour | Deselect exclusive first |

#### JSON Anti-patterns

❌ **Wrong required validation**:
```json
{
  "validationSchema": [
    ["yup.required"]  // Empty array [] will pass!
  ]
}
```

✅ **Correct required validation**:
```json
{
  "validationSchema": [
    ["yup.array"],
    ["yup.min", 1, "Select at least one option"]
  ]
}
```

❌ **Commas in option values**:
```json
{
  "ElementProps": {
    "options": [
      {"value": "Pottery, ceramics", "label": "Pottery, ceramics"}  // Breaks CSV
    ]
  }
}
```

✅ **Safe option values**:
```json
{
  "ElementProps": {
    "options": [
      {"value": "Pottery and ceramics", "label": "Pottery & ceramics"}
    ]
  }
}
```

#### Spec Mapping

**Designer "Select Multiple" configuration**:
- Label → `component-parameters.label`
- Options → `ElementProps.options` (drag-drop reorderable)
- Expanded checklist toggle → `ElementProps.expandedChecklist`
- Per-option exclusive checkbox → `ElementProps.exclusiveOptions`
- Designer enforces value = label for readability

**Common patterns**:
```json
// Basic multi-selection with validation
{
  "component-name": "MultiSelect",
  "ElementProps": {
    "expandedChecklist": true,
    "options": [...]
  },
  "validationSchema": [
    ["yup.array"],
    ["yup.min", 1, "Select at least one"]
  ]
}

// Exclusive options pattern
{
  "ElementProps": {
    "exclusiveOptions": ["none", "unknown"]
  }
}

// Migration from multiple checkboxes
{
  "component-name": "MultiSelect",
  "ElementProps": {
    "expandedChecklist": true  // Mimics checkbox appearance
  }
}
```

#### Implementation Examples {comprehensive}

**Site Features with Validation**:
```json
{
  "artefact-materials": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::Array",
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

**Visibility Conditions with Exclusive Options**:
```json
{
  "site-visibility": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::Array",
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

---

### RadioGroup {essential}
<!-- keywords: radio, single, selection, deprecated, broken -->

#### Purpose {essential}
Single selection from 2–10 mutually exclusive options through radio button interface, returning `faims-core::String` values. Distinguished by problematic toggle deselection behaviour—clicking selected option clears selection but only works via mouse/touch, not keyboard. **DEPRECATED**: Due to critical limitations (no error messages, accessibility violations, performance issues), production deployments should use Select instead.

#### Key Features {essential}
- **String return type**: Returns selected option value
- **Toggle deselection**: Click selected option to clear (mouse only)
- **Vertical layout only**: No horizontal option
- **No error messages**: Only shows red color, no text
- **Performance issues**: Severe degradation >20 options

**Critical limitations**: NO error message display, NO ARIA attributes, keyboard deselection broken, performance degrades from markdown parsing overhead.

#### Configuration Parameters {important}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "RadioGroup",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "label": "Select one option",
    "id": "radio-field-1",
    "helperText": "",
    "advancedHelperText": "",
    "required": false,
    "variant": "outlined",
    "ElementProps": {
      "options": [
        {"value": "opt1", "label": "Option 1"},
        {"value": "opt2", "label": "Option 2"}
      ]
    }
  },
  "validationSchema": [["yup.string"]],
  "initialValue": "",
  "meta": {
    "annotation": {"include": false},
    "uncertainty": {"include": false}
  }
}
```

#### Critical Validation Issues {important}

⚠️ **MAJOR BUG**: RadioGroup displays NO error messages - only shows red color when invalid.

| Validation Type | Configuration | Error Message | Actual Display |
|-----------------|---------------|---------------|----------------|
| Required field | `["yup.required", "Required"]` | "Required" | ❌ Red color only |
| String type | `["yup.string"]` | Automatic | ❌ No message |
| One of values | `["yup.oneOf", ["yes","no"]]` | "Invalid" | ❌ No message |

**Validation timing**:
- Form load: Validation runs but hidden
- First interaction: Red color if invalid (no message)
- Deselection: Sets null, shows red immediately
- Submit: All fields turn red, no messages

#### Interaction Bugs {important}

**Deselection Implementation (Broken)**:
1. **Mouse/Touch**: Click selected option → deselects ✅
2. **Keyboard**: Space on selected → NO EFFECT ❌
3. **Screen Reader**: Cannot deselect at all ❌

**Keyboard Navigation**:
| Key | Expected | Actual | Issue |
|-----|----------|--------|-------|
| Tab | Focus field | ✅ Works | - |
| Arrow | Navigate | ✅ Works | - |
| Space | Select | ✅ Works | - |
| Space (selected) | Deselect | ❌ BROKEN | WCAG violation |

**Accessibility Failures**:
- ❌ No `aria-required`
- ❌ No `aria-invalid`
- ❌ No `aria-errormessage`
- ❌ No `aria-describedby`

#### Performance Degradation {important}

| Options | Render Time | Experience | Recommendation |
|---------|-------------|------------|----------------|
| 1-5 | <100ms | Smooth | ✅ Use RadioGroup |
| 6-10 | ~200ms | Acceptable | ⚠️ Consider Select |
| 11-20 | ~500ms | Noticeable lag | ❌ Use Select |
| 21-50 | 2-3 seconds | Severe stuttering | ❌ Unusable |
| 50+ | 5+ seconds | Browser freeze | ❌ Will crash |

Every option runs through markdown parsing + HTML sanitization with no optimization.

#### Field-Specific Troubleshooting {important}

| Issue | Cause | Workaround | Fix Needed |
|-------|-------|------------|------------|
| No error messages | Not implemented | Add helper text | ✅ Add FormHelperText |
| Can't deselect keyboard | Bug | Use Select instead | ✅ Fix handler |
| Screen reader fails | No ARIA | Avoid RadioGroup | ✅ Add ARIA |
| Performance >20 | Markdown overhead | Use Select | ✅ Virtualization |
| Can't detect empty | No isEmpty | Add "None" option | ✅ Add operator |

#### JSON Anti-patterns

❌ **Using for production without warnings**:
```json
{
  "component-name": "RadioGroup",
  "component-parameters": {
    "label": "Critical selection",
    "required": true  // User won't see error!
  }
}
```

✅ **Migration to Select**:
```json
{
  "component-name": "Select",  // Better than RadioGroup
  "ElementProps": {
    "options": [
      {"value": "", "label": "-- Select --"},
      {"value": "yes", "label": "Yes"},
      {"value": "no", "label": "No"}
    ]
  }
}
```

❌ **Too many options**:
```json
{
  "component-name": "RadioGroup",
  "ElementProps": {
    "options": [
      // 20+ options - severe performance issues
    ]
  }
}
```

#### Spec Mapping

**Designer "Select one option" configuration**:
- Label → `component-parameters.label`
- Options → `ElementProps.options` (manual entry, drag-drop)
- Required checkbox → Adds `["yup.required"]` (won't display)
- NO preview capability in Designer

**Migration patterns**:
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
      ...existing options
    ]
  }
}
```

#### Implementation Examples {comprehensive}

**Heritage Condition (With Workarounds)**:
```json
{
  "fabric-condition": {
    "component-namespace": "faims-custom",
    "component-name": "RadioGroup",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "fabric-condition",
      "label": "Fabric Condition",
      "helperText": "Click selected to deselect (mouse only)",
      "required": true,
      "ElementProps": {
        "options": [
          {"value": "excellent", "label": "Excellent"},
          {"value": "good", "label": "Good"},
          {"value": "fair", "label": "Fair"},
          {"value": "poor", "label": "Poor"},
          {"value": "na", "label": "Not Applicable"}
        ]
      }
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Required (message won't show)"]
    ],
    "initialValue": "na",  // Default prevents empty
    "meta": {
      "annotation": {"include": true}
    }
  }
}
```

⚠️ **FINAL WARNING**: RadioGroup has critical unresolved bugs and accessibility violations. Production deployments should use Select instead.

---

### Select {essential}
<!-- keywords: dropdown, single, selection, standard -->

#### Purpose {essential}
Single-choice selection from dropdown list, offering space-efficient presentation of controlled vocabularies through Material-UI's consistent interface. Returns `faims-core::String` values and serves as standard solution for single selection from >5-7 options. While lacking error message display and native mobile pickers, delivers reliable structured data collection with human-readable exports when configured through Designer.

#### Key Features {essential}
- **String return type**: Single selected value
- **Space-efficient**: Dropdown for long option lists
- **Human-readable exports**: Designer enforces value = label
- **Consistent UI**: Same Material-UI dropdown all platforms
- **No deselection**: Must include empty option for null state

**Limitations**: No error message display, no native mobile pickers, no search beyond single character.

#### Configuration Parameters {important}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "Select",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "label": "Field Label",
    "helperText": "Choose one option",
    "fullWidth": true,
    "variant": "outlined",
    "required": false,
    "select": true,
    "disabled": false,
    "ElementProps": {
      "options": [
        {"value": "Option 1", "label": "Option 1"},
        {"value": "Option 2", "label": "Option 2"}
      ]
    }
  },
  "validationSchema": [["yup.string"]],
  "initialValue": "",
  "meta": {
    "annotation": {"include": true, "label": "notes"},
    "uncertainty": {"include": false}
  }
}
```

#### Validation Behaviour {important}

| Validation Type | Configuration | Behaviour | User Experience |
|-----------------|---------------|-----------|-----------------|
| Required | `["yup.required"]` | Blocks submission | Silent failure - no visual |
| String Type | `["yup.string"]` | Always passes | Automatic |
| Min Length | `["yup.minLength", 3]` | Validates length | No error display |
| Pattern | `["yup.matches", "pattern"]` | Regex validation | No error display |

**Validation notes**:
- On change: Validation runs but errors not displayed
- On submit: Final validation blocks submission silently
- UI prevents invalid selections, making most validation redundant
- Option membership validation not implemented

#### Display Characteristics {important}

**Desktop Rendering**:
- Material-UI Select dropdown
- Typically fullWidth
- Click or Space opens
- Scrollable dropdown with hover states
- Helper text above field (non-standard)
- No error indication

**Mobile Rendering**:
- Same Material-UI dropdown (not native)
- 48px height MenuItems (meets minimum)
- Standard touch scroll
- Direct tap selection
- No virtual keyboard
- Landscape adjusts to height

#### Interaction Patterns {important}

**Selection Flow**:
1. Displays current selection or placeholder
2. Click/tap on field or arrow
3. Scroll or arrow keys to find
4. Click/tap desired option
5. Dropdown closes with selection

**Keyboard Support**:
- Tab: Focus field
- Space/Enter: Open dropdown
- Arrow Up/Down: Navigate
- Enter: Select highlighted
- Escape: Close without selection
- Type-ahead: Single character (resets ~1 second)

**Deselection Behaviour**:
- No built-in clear button
- Cannot deselect without empty option
- Include `{"value": "", "label": "-- None --"}` if needed

#### Field-Specific Troubleshooting {important}

| Issue | Symptoms | Cause | Resolution |
|-------|----------|-------|------------|
| No error messages | Required fails silently | No error display | Train users on required fields |
| Slow dropdown | Lag with many options | No virtualization | Limit to <50 options |
| Can't deselect | No way to clear | No clear button | Include empty option |
| Data shows codes | CSV has "001" not label | Manual JSON editing | Use Designer (value = label) |
| Can't convert type | Must delete and recreate | No conversion | Note options, recreate |

#### JSON Anti-patterns

❌ **Different values and labels**:
```json
{
  "ElementProps": {
    "options": [
      {"value": "001", "label": "Archaeological Site"}  // Exports "001"
    ]
  }
}
```

✅ **Designer pattern (value = label)**:
```json
{
  "ElementProps": {
    "options": [
      {"value": "Archaeological Site", "label": "Archaeological Site"}
    ]
  }
}
```

❌ **No empty option when nullable**:
```json
{
  "ElementProps": {
    "options": [
      {"value": "Option1", "label": "Option1"}
      // No way to clear selection
    ]
  }
}
```

✅ **Include empty option**:
```json
{
  "ElementProps": {
    "options": [
      {"value": "", "label": "-- Not assessed --"},
      {"value": "Option1", "label": "Option1"}
    ]
  }
}
```

#### Spec Mapping

**Designer "Select Field" configuration**:
- Label → `component-parameters.label`
- Helper text → `component-parameters.helperText`
- Options → `ElementProps.options` (value = label enforced)
- Required → `component-parameters.required`
- No preview capability (must deploy)

**Common patterns**:
```json
// Site classification with null option
{
  "component-name": "Select",
  "ElementProps": {
    "options": [
      {"value": "", "label": "-- Select type --"},
      {"value": "Artefact scatter", "label": "Artefact scatter"},
      {"value": "Rock art", "label": "Rock art"}
    ]
  }
}

// Triggering conditional fields
{
  "material-type": {
    "component-name": "Select",
    "ElementProps": {
      "options": [
        {"value": "Other", "label": "Other"}
      ]
    }
  },
  "other-material": {
    "component-name": "TextField",
    "condition": {
      "field": "material-type",
      "operator": "equal",
      "value": "Other"
    }
  }
}
```

#### Implementation Examples {comprehensive}

**Site Classification (Heritage Context)**:
```json
{
  "site-type": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Site Type",
      "name": "site-type",
      "helperText": "Select the primary site classification",
      "fullWidth": true,
      "required": true,
      "ElementProps": {
        "options": [
          {"value": "Artefact scatter", "label": "Artefact scatter"},
          {"value": "Rock art", "label": "Rock art"},
          {"value": "Shell midden", "label": "Shell midden"},
          {"value": "Stone arrangement", "label": "Stone arrangement"},
          {"value": "Burial", "label": "Burial"},
          {"value": "Historic structure", "label": "Historic structure"},
          {"value": "Other", "label": "Other"}
        ]
      }
    },
    "validationSchema": [["yup.string"], ["yup.required"]],
    "initialValue": "",
    "meta": {
      "annotation": {"include": true, "label": "classification notes"},
      "uncertainty": {"include": true, "label": "confidence"}
    }
  }
}
```

---

### AdvancedSelect {essential}
<!-- keywords: hierarchical, tree, taxonomy, beta, broken -->

#### Purpose {essential}
Hierarchical tree navigation for selecting values from nested vocabularies, returning `faims-core::String` values representing either full paths or leaf nodes. **Currently in beta status** due to incomplete Designer integration, performance limitations, and multiple critical bugs. Renders entire tree structures without optimisation, making it unsuitable for large datasets or mobile deployment.

#### Key Features {essential}
- **Hierarchical selection**: Navigate tree structures
- **Two value formats**: Full path ("A > B > C") or leaf only ("C")
- **Any node selectable**: Parent and child nodes all valid
- **No search**: Must manually navigate hierarchy
- **No deselection**: Cannot clear once selected (critical bug)

**Critical limitations**: No error display, no clear capability, no search, severe performance degradation >100 nodes, requires JSON hand-editing, breaks mobile layouts.

#### Configuration Parameters {important}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "AdvancedSelect",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "label": "Field Label",
    "helperText": "Guidance text",
    "required": false,
    "valuetype": "full",  // or "child"
    "disabled": false,
    "ElementProps": {
      "optiontree": [
        {
          "name": "Parent",
          "label": "Display Name",  // Optional
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

**Node Structure**:
```typescript
interface TreeNode {
  name: string;        // Required: Used for value
  label?: string;      // Optional: Display override
  children?: TreeNode[];  // Optional: Child nodes
}
```

**Designer limitation**: Hierarchy structure (`optiontree`) must be hand-edited in JSON - primary reason for beta status.

#### Value Type Behaviour {important}

**With `valuetype: "full"` (default)**:
- Stores complete path: "Animalia > Chordata > Mammalia"
- Path uses " > " delimiter (with spaces)
- Useful when hierarchy context matters

**With `valuetype: "child"`**:
- Stores only selected node: "Mammalia"
- Loses hierarchical context
- Useful when only leaf value needed

**Important**: `valuetype` does NOT restrict which nodes can be selected - any node remains selectable.

#### Critical Issues {important}

**Cannot Clear Selection**:
- Once selected, no way to deselect
- No clear button provided
- Reloading form only workaround
- Major UX failure

**Performance Boundaries**:
- <50 nodes: Acceptable on all platforms
- 50-100 nodes: Noticeable lag on mobile
- 100-500 nodes: Significant delays
- 500-1000 nodes: Likely unusable
- >1000 nodes: Will crash browser

**Mobile Breaking Issues**:
- Fixed 500px width causes horizontal scrolling
- Touch targets (24px chevrons) too small
- No mobile optimizations
- Performance severely degraded

#### Display Problems {important}

**Desktop Rendering**:
- Fixed 500px min width, 300px max height
- Vertical scroll for tall hierarchies
- Material-UI TreeView with chevrons
- Starts fully collapsed
- Chip shows current selection
- No clear button
- Lost expansion state on navigation

**Mobile Rendering**:
- 500px width breaks all mobile layouts
- Chevron icons too small for touch
- No pinch-zoom or swipe support
- Identical issues iOS and Android
- Essentially unusable on phones

#### Field-Specific Troubleshooting {important}

| Issue | Cause | Solution | Prevention |
|-------|-------|----------|------------|
| Cannot clear | No deselect | Add TextField override | Document limitation |
| No error display | Not implemented | Check form won't submit | Use Select instead |
| Horizontal scroll | Fixed 500px width | Use Select for mobile | Tablet/desktop only |
| Performance | Renders entire tree | Limit <100 nodes | Multiple Selects |
| Tree collapsed | No default expansion | Document navigation | Consider flat Select |
| Lost state | Not preserved | Warn users | Single page forms |
| Required confusion | Silent validation | Document in helperText | Avoid required |
| No Designer support | Must edit JSON | Provide templates | Use Select until fixed |

#### JSON Anti-patterns

❌ **Too many nodes**:
```json
{
  "ElementProps": {
    "optiontree": [
      // 500+ nodes will crash
    ]
  }
}
```

❌ **Using " > " in node names**:
```json
{
  "optiontree": [{
    "name": "Level 1 > Special",  // Breaks path parsing!
    "children": []
  }]
}
```

❌ **Expecting clear capability**:
```json
{
  "required": false  // User can't clear to make un-required!
}
```

✅ **Workaround for clearing**:
```json
{
  "clear-override": {
    "component-name": "TextField",
    "label": "Clear Selection Workaround",
    "condition": {
      "field": "hierarchy-field",
      "operator": "not-equal",
      "value": ""
    }
  }
}
```

#### Spec Mapping

**Designer "Select Field (Hierarchical)" configuration**:
- Label → `component-parameters.label`
- Helper text → `component-parameters.helperText`
- Value type → `component-parameters.valuetype`
- **Hierarchy → Must hand-edit JSON** (critical limitation)

**Migration considerations**:
- No automated conversion from Select
- Manual data transformation required
- Breaking change when switching valuetype
- No backwards compatibility

#### Implementation Examples {comprehensive}

**Biological Taxonomy**:
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
      "helperText": "Navigate to most specific classification",
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
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Classification required"]
    ],
    "initialValue": ""
  }
}
```

⚠️ **Beta Warning**: Not recommended for production. Use Select with prefixed options until AdvancedSelect stabilizes.

---

## Troubleshooting Guide {important}

### Critical Issues Without Solutions {important}

| Issue | Affected Fields | Cause | Workaround | Fix Status |
|-------|----------------|-------|------------|------------|
| No error messages | RadioGroup, Select, MultiSelect, AdvancedSelect | Not implemented | Add explicit helperText | 🔧 On roadmap |
| Cannot deselect keyboard | RadioGroup | Bug in handler | Use Select instead | 🔧 Needs fix |
| Cannot clear selection | AdvancedSelect | No deselect mechanism | Add TextField override | 🔧 Beta issue |
| Label not clickable | Checkbox | Broken association | Train users | 🔧 Needs fix |
| Empty array passes required | MultiSelect | Validation logic | Use yup.min(1) | 📚 Documentation |
| Horizontal scroll mobile | AdvancedSelect | Fixed 500px width | Avoid on mobile | 🔧 Beta issue |

### Common Problems {important}

| Problem | Symptoms | Diagnosis | Solution |
|---------|----------|-----------|----------|
| Validation silent fail | Form won't submit, no feedback | Error display missing | Check console, add helperText |
| Performance lag | Slow interaction, freezing | Too many options | Reduce options or change field type |
| Can't find Designer option | Field type not visible | Naming confusion | Check component mapping table |
| Export missing labels | CSV shows codes not text | Different value/label | Use Designer (enforces same) |
| Hierarchy won't save | AdvancedSelect config lost | JSON editing required | Hand-edit optiontree in JSON |
| Multiple checkboxes | Need group validation | Wrong approach | Use MultiSelect instead |

### Quick Fixes {important}

**Required not working on Checkbox**:
```json
// Change from:
["yup.required"]
// To:
["yup.oneOf", [true], "Must be checked"]
```

**MultiSelect empty array issue**:
```json
// Change from:
["yup.required"]
// To:
["yup.array"], ["yup.min", 1, "Select at least one"]
```

**RadioGroup to Select migration**:
```json
// Change component-name and add empty option:
"component-name": "Select",
"ElementProps": {
  "options": [
    {"value": "", "label": "-- Select --"},
    // ... existing options
  ]
}
```

**AdvancedSelect clear workaround**:
```json
// Add conditional TextField:
{
  "clear-field": {
    "component-name": "TextField",
    "label": "Clear selection note",
    "condition": {
      "field": "advanced-select-field",
      "operator": "not-equal",
      "value": ""
    }
  }
}
```

### Debug Checklists {comprehensive}

**Field Not Appearing**:
- [ ] Check conditional logic (no isEmpty for choice fields)
- [ ] Verify field name unique in form
- [ ] Confirm parent section visible
- [ ] Check JSON syntax valid
- [ ] Verify field ID matches conditions
- [ ] Check console for React errors

**Validation Issues**:
- [ ] Remember most fields show NO error messages
- [ ] Check if using correct validation (yup.min for arrays)
- [ ] Verify initialValue type (array for MultiSelect, string for others)
- [ ] Test touched state behavior
- [ ] Check console for validation errors
- [ ] Confirm validation schema syntax

**Selection Problems**:
- [ ] Verify option values unique
- [ ] Check for duplicate labels
- [ ] Test exclusive options (MultiSelect)
- [ ] Verify deselection behavior documented
- [ ] Check keyboard navigation
- [ ] Test on target devices

**Performance Testing**:
- [ ] Count total options (<20 for RadioGroup, <100 for AdvancedSelect)
- [ ] Check markdown complexity in labels
- [ ] Monitor React DevTools render time
- [ ] Test on lowest-spec device
- [ ] Check memory usage
- [ ] Verify no infinite loops

---

## JSON Examples {comprehensive}

### Base Patterns

**Checkbox for Consent**:
```json
{
  "consent-field": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "consent-field",
      "label": "I consent to data collection",
      "required": true
    },
    "validationSchema": [
      ["yup.boolean"],
      ["yup.oneOf", [true], "Consent required to proceed"]
    ],
    "initialValue": false
  }
}
```

**MultiSelect with Exclusive Options**:
```json
{
  "features-observed": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "features-observed",
      "label": "Features Observed",
      "ElementProps": {
        "expandedChecklist": true,
        "options": [
          {"value": "walls", "label": "Defensive walls"},
          {"value": "houses", "label": "Domestic structures"},
          {"value": "none", "label": "None observed"}
        ],
        "exclusiveOptions": ["none"]
      }
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "Select at least one option"]
    ],
    "initialValue": []
  }
}
```

**Select with Conditional Field**:
```json
{
  "material-type": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "material-type",
      "label": "Primary Material",
      "ElementProps": {
        "options": [
          {"value": "", "label": "-- Select --"},
          {"value": "Stone", "label": "Stone"},
          {"value": "Metal", "label": "Metal"},
          {"value": "Other", "label": "Other"}
        ]
      }
    }
  },
  "other-material": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "component-parameters": {
      "name": "other-material",
      "label": "Specify Other Material"
    },
    "condition": {
      "field": "material-type",
      "operator": "equal",
      "value": "Other"
    }
  }
}
```

### Anti-Patterns

❌ **RadioGroup for Production** (Use Select):
```json
{
  "component-name": "RadioGroup",  // No error display!
  "ElementProps": {
    "options": [/* 20+ options */]  // Performance issues
  }
}
```

❌ **AdvancedSelect on Mobile**:
```json
{
  "component-name": "AdvancedSelect",  // 500px width breaks mobile
  "ElementProps": {
    "optiontree": [/* 200+ nodes */]  // Performance disaster
  }
}
```

❌ **Wrong MultiSelect Validation**:
```json
{
  "component-name": "MultiSelect",
  "validationSchema": [
    ["yup.required"]  // Empty array passes!
  ]
}
```

❌ **Checkbox Consent Wrong**:
```json
{
  "component-name": "Checkbox",
  "validationSchema": [
    ["yup.required"]  // Allows false!
  ]
}
```

### Platform-Specific Configurations

**Mobile-Optimized MultiSelect**:
```json
{
  "component-name": "MultiSelect",
  "ElementProps": {
    "expandedChecklist": false,  // Dropdown for space
    "options": [/* max 30 options */]
  }
}
```

**Desktop-Only AdvancedSelect**:
```json
{
  "component-name": "AdvancedSelect",
  "component-parameters": {
    "helperText": "Desktop/tablet only - not available on phones"
  }
}
```

### Integration Patterns

**Cascading Selects (Instead of AdvancedSelect)**:
```json
{
  "category": {
    "component-name": "Select",
    "ElementProps": {
      "options": [
        {"value": "Animal", "label": "Animal"},
        {"value": "Plant", "label": "Plant"}
      ]
    }
  },
  "animal-type": {
    "component-name": "Select",
    "condition": {
      "field": "category",
      "operator": "equal",
      "value": "Animal"
    },
    "ElementProps": {
      "options": [
        {"value": "Mammal", "label": "Mammal"},
        {"value": "Bird", "label": "Bird"}
      ]
    }
  }
}
```

**Migration from Multiple Checkboxes to MultiSelect**:
```json
// Before: Multiple checkbox fields
{
  "has-walls": {"component-name": "Checkbox"},
  "has-houses": {"component-name": "Checkbox"},
  "has-industrial": {"component-name": "Checkbox"}
}

// After: Single MultiSelect
{
  "site-features": {
    "component-name": "MultiSelect",
    "ElementProps": {
      "expandedChecklist": true,  // Looks like checkboxes
      "options": [
        {"value": "walls", "label": "Defensive walls"},
        {"value": "houses", "label": "Domestic structures"},
        {"value": "industrial", "label": "Industrial remains"}
      ]
    }
  }
}
```

---

## Migration and Best Practices {comprehensive}

### Migration Decision Tree

```
Need boolean value?
  → Use Checkbox

Need multiple selections?
  → Use MultiSelect (not multiple Checkboxes)

Need single selection?
  ├─ ≤7 options that should be visible?
  │   → Consider RadioGroup BUT prefer Select (RadioGroup deprecated)
  ├─ 8-50 options?
  │   → Use Select
  └─ Hierarchical/nested options?
      ├─ <100 nodes AND desktop only?
      │   → Consider AdvancedSelect (beta)
      └─ Otherwise?
          → Use multiple cascading Selects

Need error messages displayed?
  → Only Checkbox works properly
  → Document requirements in helperText for others
```

### Migration Warnings

**RadioGroup → Select**:
- Add empty option for null state
- Update conditional logic if checking for empty
- Test deselection behavior changes
- Document that errors now silent

**Multiple Checkboxes → MultiSelect**:
- Change data structure from multiple booleans to array
- Update conditions from `equal: true` to `contains: "value"`
- Revise validation from individual to array
- Test exclusive options behavior

**Select → AdvancedSelect**:
- Manual data transformation required
- No automated migration tools
- Must hand-code hierarchy in JSON
- Performance will degrade significantly

### Migration Script Templates

**RadioGroup to Select Conversion**:
```javascript
// Update field configuration
const migrateRadioToSelect = (field) => {
  if (field['component-name'] === 'RadioGroup') {
    field['component-name'] = 'Select';
    // Add empty option at start
    field.ElementProps.options.unshift({
      value: '',
      label: '-- Select --'
    });
  }
  return field;
};
```

**Checkboxes to MultiSelect Conversion**:
```javascript
// Combine multiple checkboxes
const combineCheckboxes = (fields, names, newName) => {
  const options = names.map(name => ({
    value: name,
    label: fields[name].label
  }));
  
  return {
    'component-name': 'MultiSelect',
    'type-returned': 'faims-core::Array',
    'component-parameters': {
      name: newName,
      label: 'Combined Selection',
      ElementProps: {
        expandedChecklist: true,
        options: options
      }
    },
    validationSchema: [['yup.array']],
    initialValue: []
  };
};
```

### Training Requirements

**For Users**:
- Checkbox labels not clickable - tap checkbox directly
- RadioGroup deselection only works with mouse
- No error messages in most fields - check helperText
- AdvancedSelect cannot be cleared once selected
- MultiSelect exclusive options clear others

**For Developers**:
- MultiSelect empty array validation quirk
- AdvancedSelect requires JSON editing
- RadioGroup deprecated - use Select
- Designer naming doesn't match components
- Platform-specific testing essential

### Alternative Approaches

**Instead of RadioGroup**:
- Use Select with empty option
- Use Checkbox for true binary
- Use segmented buttons (custom component)

**Instead of AdvancedSelect**:
- Multiple cascading Selects
- Select with prefixed options ("Category: Item")
- External taxonomy lookup (future)

**Instead of Multiple Checkboxes**:
- MultiSelect with expandedChecklist
- Single Checkbox with annotation
- Custom matrix component (future)

---

## Field Quirks Index (2025-08) {comprehensive}

### Checkbox
- `QUIRK` Label not clickable despite standard UX expectation
- `QUIRK` Required validation allows false (unchecked)
- `FIX` Use `yup.oneOf([true])` for must-be-checked
- `RULE` Always returns boolean, never null
- `VERSION` 2025-08

### MultiSelect
- `QUIRK` Empty array [] passes required validation
- `FIX` Use `yup.min(1)` instead of `yup.required`
- `QUIRK` No error messages display despite validation
- `RULE` Exclusive options automatically clear others
- `QUIRK` Performance degrades rapidly >50 options
- `VERSION` 2025-08

### RadioGroup
- `QUIRK` Space key cannot deselect (mouse only)
- `QUIRK` NO error messages, only color change
- `QUIRK` Performance disaster >20 options
- `FIX` Migrate to Select for production
- `RULE` Vertical layout only
- `VERSION` 2025-08

### Select
- `QUIRK` No error message display
- `QUIRK` Helper text appears above field
- `RULE` Designer enforces value = label
- `QUIRK` No deselection without empty option
- `RULE` No native mobile pickers
- `VERSION` 2025-08

### AdvancedSelect
- `QUIRK` Cannot clear selection once made
- `QUIRK` Requires JSON hand-editing for hierarchy
- `QUIRK` Fixed 500px width breaks mobile
- `QUIRK` Performance unusable >100 nodes
- `FIX` Use Select with prefixes until stable
- `VERSION` 2025-08 (Beta)

---

## Performance Thresholds Table (2025-08) {essential}

| Field Type | Optimal | Acceptable | Degraded | Unusable | Limiting Factor |
|------------|---------|------------|----------|----------|-----------------|
| **Checkbox** | 1-30 | 30-50 | 50-100 | >100 | Individual field overhead |
| **MultiSelect** | 1-20 | 20-50 | 50-100 | >100 | No virtualization |
| **RadioGroup** | 1-5 | 6-10 | 11-20 | >20 | Markdown parsing per option |
| **Select** | 1-30 | 30-50 | 50-100 | >100 | Dropdown rendering |
| **AdvancedSelect** | 1-50 | 50-100 | 100-500 | >500 | Full tree in DOM |

**Platform modifiers**:
- Mobile: Reduce all thresholds by 50%
- Older devices: Reduce by 75%
- Multiple fields: Consider cumulative impact

---

## Field Interaction Matrix (2025-08) {important}

| Field A | Field B | Interaction Type | Pattern | Issues |
|---------|---------|------------------|---------|--------|
| Select | TextField | Conditional reveal | "Other" option shows text | Works well |
| MultiSelect | TextField | Conditional reveal | Any selection shows text | Array operators needed |
| Checkbox | Any field | Enable/disable | Checkbox controls visibility | Boolean conditions only |
| RadioGroup | Multiple fields | Branch logic | Each option shows different fields | Can't detect empty |
| AdvancedSelect | Any field | Hierarchical conditions | Path matching required | Exact string match only |
| Multiple Checkbox | - | Group validation | - | Use MultiSelect instead |
| Select | Select | Cascading | First determines second options | Static only |

**Conditional operator support**:
- Checkbox: `equal`, `not-equal` (boolean)
- MultiSelect: `contains`, `contains-all-of`, `not-contains` (array)
- Others: `equal`, `not-equal` (string)
- None: `isEmpty` operator not available

---

## Quick Diagnosis Tables (2025-08) {important}

### Error Display Capability

| Field | Shows Error Color | Shows Error Text | ARIA Support | Verdict |
|-------|------------------|------------------|--------------|---------|
| Checkbox | ✅ Yes | ✅ Yes | ❌ No | Best option |
| MultiSelect | ❌ No | ❌ No | ❌ No | Silent failure |
| RadioGroup | ✅ Yes | ❌ No | ❌ No | Color only |
| Select | ❌ No | ❌ No | ❌ No | Silent failure |
| AdvancedSelect | ❌ No | ❌ No | ❌ No | Silent failure |

### Mobile Compatibility

| Field | Touch Target | Layout | Performance | Gestures | Verdict |
|-------|--------------|--------|-------------|----------|---------|
| Checkbox | ⚠️ 48px (small) | ✅ Responsive | ✅ Good | ❌ None | Usable |
| MultiSelect | ✅ Full row | ✅ Responsive | ⚠️ Depends | ❌ None | Good |
| RadioGroup | ✅ 42px | ✅ Responsive | ❌ Poor >10 | ❌ None | Avoid |
| Select | ✅ 48px items | ✅ Responsive | ✅ Good <50 | ❌ None | Good |
| AdvancedSelect | ❌ Too small | ❌ 500px fixed | ❌ Poor | ❌ None | Broken |

### Deselection Capability

| Field | Clear Method | Keyboard | Mouse/Touch | Workaround |
|-------|--------------|----------|-------------|------------|
| Checkbox | Toggle | ✅ Yes | ✅ Yes | None needed |
| MultiSelect | Click selected | ✅ Yes | ✅ Yes | None needed |
| RadioGroup | Click selected | ❌ No | ✅ Yes | Use Select |
| Select | Empty option | ✅ Yes | ✅ Yes | Include empty |
| AdvancedSelect | None | ❌ No | ❌ No | TextField override |

---

## Error Message Quick Reference (2025-08) {important}

### Critical Errors (Form Breaking)

| Error Message | Field Type(s) | Root Cause | Quick Fix | Prevention |
|---------------|---------------|------------|-----------|------------|
| "Component Checkbox not found" | Checkbox | Wrong namespace | Use faims-custom namespace | Always use faims-custom for selection |
| "Component MultiSelect not found" | MultiSelect | Wrong namespace | Use faims-custom namespace | Check namespace in JSON |
| "Component RadioGroup not found" | RadioGroup | Wrong namespace | Use faims-custom namespace | Designer generates correctly |
| "Cannot read property 'map' of undefined" | MultiSelect, AdvancedSelect | Options/optiontree undefined | Provide options array | Always define options |
| "Cannot read property 'value' of undefined" | All selection fields | Option missing value property | Add value to all options | Check option structure |
| "yup.array is not a function" | MultiSelect | Wrong validation order | Put ["yup.array"] first | Type must come before rules |
| "yup.oneOf expects array" | Checkbox | Wrong oneOf syntax | Use ["yup.oneOf", [true]] | Array required for values |
| "Maximum update depth exceeded" | MultiSelect | Exclusive options loop | Check exclusiveOptions config | Test exclusive option logic |

### Validation Errors (User Visible - When Supported)

| Error Message | Field Type(s) | Actually Displays? | Root Cause | Workaround |
|---------------|---------------|-------------------|------------|------------|
| "Field is required" | Checkbox | ✅ Yes | Empty required field | Works correctly |
| "You must accept" | Checkbox | ✅ Yes | oneOf validation | Works correctly |
| "Select at least one" | MultiSelect | ❌ No | yup.min validation | Document in helperText |
| "Field is required" | RadioGroup | ❌ No (red only) | No selection | Add to helperText |
| "Field is required" | Select | ❌ No | No selection | Add to helperText |
| "Invalid selection" | AdvancedSelect | ❌ No | Validation failure | Document requirements |

### Silent Failures (No User Feedback)

| Issue | Field Type(s) | Symptoms | Detection | Resolution |
|-------|---------------|----------|-----------|------------|
| Empty array passes required | MultiSelect | Form submits with [] | Check data on submit | Use yup.min(1) |
| Can't clear selection | AdvancedSelect | Stuck with value | User reports | Add workaround field |
| Keyboard deselect broken | RadioGroup | Space key doesn't work | Testing | Use Select instead |
| No error display | Select, MultiSelect, AdvancedSelect | Form won't submit, no message | Console logs | Check helperText |

---

## JSON Patterns Cookbook (2025-08) {comprehensive}

### Common Selection Patterns

**Consent Checkbox (Must Accept)**:
```json
{
  "consent-field": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "label": "I consent to data collection",
      "required": true
    },
    "validationSchema": [
      ["yup.boolean"],
      ["yup.oneOf", [true], "You must consent to proceed"]
    ]
  }
}
```

**MultiSelect with Minimum Selection**:
```json
{
  "materials": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "label": "Materials Present",
      "ElementProps": {
        "expandedChecklist": true,
        "options": [
          {"value": "ceramic", "label": "Ceramic"},
          {"value": "glass", "label": "Glass"},
          {"value": "none", "label": "None observed"}
        ],
        "exclusiveOptions": ["none"]
      }
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "Select at least one material"]
    ]
  }
}
```

**Select with Conditional Field**:
```json
{
  "category": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "component-parameters": {
      "label": "Category",
      "ElementProps": {
        "options": [
          {"value": "", "label": "-- Select --"},
          {"value": "Standard", "label": "Standard"},
          {"value": "Other", "label": "Other"}
        ]
      }
    }
  },
  "other-details": {
    "component-name": "TextField",
    "condition": {
      "field": "category",
      "operator": "equal",
      "value": "Other"
    }
  }
}
```

**Cascading Selects (Alternative to AdvancedSelect)**:
```json
{
  "level1": {
    "component-name": "Select",
    "component-parameters": {
      "label": "Kingdom",
      "ElementProps": {
        "options": [
          {"value": "Animalia", "label": "Animalia"},
          {"value": "Plantae", "label": "Plantae"}
        ]
      }
    }
  },
  "level2": {
    "component-name": "Select",
    "component-parameters": {
      "label": "Phylum"
    },
    "condition": {
      "field": "level1",
      "operator": "equal",
      "value": "Animalia"
    },
    "component-parameters": {
      "ElementProps": {
        "options": [
          {"value": "Chordata", "label": "Chordata"},
          {"value": "Arthropoda", "label": "Arthropoda"}
        ]
      }
    }
  }
}
```

---

## JSON Anti-patterns Quick Index {comprehensive}

### Selection Field Anti-patterns

❌ **Wrong validation for Checkbox consent**:
```json
{
  "validationSchema": [["yup.required"]]  // Allows false!
}
```
✅ **Correct**:
```json
{
  "validationSchema": [
    ["yup.boolean"],
    ["yup.oneOf", [true], "Must accept"]
  ]
}
```

❌ **Wrong validation for MultiSelect required**:
```json
{
  "validationSchema": [["yup.required"]]  // Empty array passes!
}
```
✅ **Correct**:
```json
{
  "validationSchema": [
    ["yup.array"],
    ["yup.min", 1, "Select at least one"]
  ]
}
```

❌ **Different values and labels in Select**:
```json
{
  "options": [
    {"value": "001", "label": "Site Type A"}  // Exports codes
  ]
}
```
✅ **Correct**:
```json
{
  "options": [
    {"value": "Site Type A", "label": "Site Type A"}  // Human-readable
  ]
}
```

❌ **Using RadioGroup for production**:
```json
{
  "component-name": "RadioGroup"  // No error display!
}
```
✅ **Correct**:
```json
{
  "component-name": "Select"  // Better compatibility
}
```

❌ **AdvancedSelect on mobile forms**:
```json
{
  "component-name": "AdvancedSelect"  // 500px breaks mobile
}
```
✅ **Correct**:
```json
{
  "component-name": "Select"  // Or cascading Selects
}
```

---

## Migration Warnings Index (2025-08) {comprehensive}

### Critical Migration Warnings

**RadioGroup → Select**:
- ⚠️ Add empty option for null state
- ⚠️ Update conditions checking for empty (was null, now "")
- ⚠️ Retrain users on deselection method
- ⚠️ Document that errors still won't display

**Multiple Checkboxes → MultiSelect**:
- ⚠️ Data structure changes from multiple booleans to single array
- ⚠️ Conditions change from `equal: true` to `contains: "value"`
- ⚠️ Export format completely different
- ⚠️ Cannot migrate existing data automatically

**Select → AdvancedSelect**:
- ⚠️ No automated migration path
- ⚠️ Must manually build hierarchy structure
- ⚠️ Performance will degrade significantly
- ⚠️ Mobile compatibility lost

**Checkbox Yes/No → Boolean Checkbox**:
- ⚠️ Changes from string "Yes"/"No" to boolean true/false
- ⚠️ Breaks existing conditional logic
- ⚠️ Export format changes
- ⚠️ May need data transformation scripts

### Migration Risk Matrix

| From | To | Risk Level | Data Loss | Reversible |
|------|----|------------|-----------|------------|
| RadioGroup | Select | Low | No | Yes |
| Multiple Checkbox | MultiSelect | High | Possible | No |
| Select | AdvancedSelect | High | No | Difficult |
| Text Yes/No | Checkbox | Medium | No | With script |
| Flat list | Hierarchical | High | No | No |

---

## Metadata

**Documentation Version**: 1.0.0
**Component Versions**: faims-custom 2025-08
**Platform**: Fieldmark 3.0
**Last Updated**: 2025-09-02
**Status**: Production (except RadioGroup deprecated, AdvancedSelect beta)

**Consolidated From**:
- checkbox.md (434 lines)
- multiselect.md (467 lines)
- radiogroup.md (604 lines)
- select.md (429 lines)
- advanced-select.md (574 lines)

**Total Source**: 2,508 lines
**Compression**: Maintained all technical content while eliminating redundancy
**Zero Content Loss**: All warnings, examples, and technical details preserved