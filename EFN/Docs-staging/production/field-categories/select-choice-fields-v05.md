<!-- concat:boundary:start section="selection-fields" -->
<!-- concat:metadata
document_id: select-choice-fields-v05
category: selection_choice
field_count: 5
designer_capable: ["Checkbox", "Select", "MultiSelect", "RadioGroup", "AdvancedSelect"]
json_only: ["dynamic_options", "dependent_selects", "option_generation"]
last_updated: 2025-01-05
-->

<!-- discovery:metadata
provides: [selection-fields, radio-groups, dropdowns, hierarchical-select, multi-select]
see-also: [field-selection-guide, dynamic-forms-guide]
-->


# Selection and Choice Fields

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Text Fields](./text-fields-v05.md) | **Selection & Choice Fields** | [Date & Time Fields →](./datetime-fields-v05.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Date & Time Fields ↓](#datetime-fields) -->

## Overview {essential}

### DESIGNER QUICK GUIDE

Selection and choice fields provide controlled vocabulary input through various interface patterns, returning structured data for standardized recording workflows. Five field types serve different selection patterns: **Checkbox** for boolean states, **Select** for single dropdown selection, **MultiSelect** for multiple choices, **RadioGroup** for visible single selection (deprecated), and **AdvancedSelect** for hierarchical vocabularies (beta).

All fields share static vocabulary requirements—options must be predefined at design time with no dynamic loading capability due to offline operation requirements. Critical limitations include no error message display (except Checkbox), limited accessibility support, and various platform-specific interaction issues.

### CRITICAL NAMING DISAMBIGUATION

**Designer Interface Labels vs JSON Component Names:**
- **"Checkbox"** in Designer → `faims-custom::Checkbox`
- **"Select Multiple"** in Designer → `faims-custom::MultiSelect`  
- **"Select one option"** in Designer → `faims-custom::RadioGroup
- **"Select Field"** in Designer → `faims-custom::Select`
- **"Select Field (Hierarchical)"** in Designer → `faims-custom::AdvancedSelect` 🔴 BETA

### Field Capabilities Summary

1. **Checkbox** ✅ PRODUCTION - Boolean states, returns `faims-core::Bool`
2. **Select** ✅ PRODUCTION - Single dropdown selection, returns `faims-core::String`  
3. **MultiSelect** ✅ PRODUCTION - Multiple selection, returns `faims-core::Array`
4. **RadioGroup - Single visible selection, returns `faims-core::String`
5. **AdvancedSelect 🔟 NEW - Hierarchical trees, returns `faims-core::String`

## Component Mapping Reference {essential}

For the complete mapping between Designer field names and JSON component implementations, see:
→ **[Designer UI to Component Mapping Reference](../references/designer-component-mapping.md)**

This central reference provides:
- Exact component names and namespaces for all fields
- Configuration requirements and examples
- Common mapping errors and solutions


## Designer Usage Guide {essential}

### What to Select in Designer

**For Binary Decisions (True/False)**:
- Use **"Checkbox"** when false state is meaningful
- Returns boolean values for programmatic logic
- Best for consent, presence/absence, feature flags

**For Single Selection from 2-7 Options**:
- Use **"Select Field"** for reliable implementation
- Avoid **"Select one option"** (RadioGroup) - deprecated due to critical bugs

**For Single Selection from 8+ Options**:
- Use **"Select Field"** - space-efficient dropdown
- Designer enforces value = label for human-readable exports

**For Multiple Selections**:
- Use **"Select Multiple"** (MultiSelect) for arrays of values
- Choose expanded checklist for ≤15 options or dropdown for more

**For Hierarchical Classifications**:
- **Avoid "Select Field (Hierarchical)"** (AdvancedSelect) - beta status
- Use cascading Select fields or Select with prefixed options instead

### When JSON Enhancement is Required

**Always Requires JSON Editing**:
- **AdvancedSelect**: Hierarchy structure (`optiontree`) not configurable in Designer
- Complex validation beyond basic `required` checkbox
- Initial values other than defaults
- Performance-critical properties (`fullWidth`, `variant`)

**Designer Sufficient For**:
- Basic Select fields with value = label
- Checkbox with standard validation
- MultiSelect with simple options
- Standard conditional logic (visibility only)

### Quick Use Case Examples

- **Site present/absent** → Checkbox (boolean output)
- **Site type from 10 options** → Select Field (dropdown)
- **Multiple damage types** → Select Multiple (array output)
- **Condition: Good/Fair/Poor** → Select Field (not RadioGroup)
- **Species taxonomy** → Multiple Select Fields (not AdvancedSelect)

## Field Selection Guide {essential}

### Decision Tree

```
What type of selection do you need?
│
├─ Boolean/binary state?
│  ├─ YES → Checkbox
│  │  ├─ Returns: faims-core::Bool  
│  │  ├─ Best for: Consent, presence/absence
│  │  └─ ⚠️ Label not clickable (bug)
│  └─ NO → Continue
│
├─ Single selection needed?
│  ├─ YES → How many options?
│  │  ├─ 2-7 options → Select Field
│  │  │  ├─ Returns: faims-core::String
│  │  │  ├─ Space efficient, reliable
│  │  │  └─ ❌ No error display
│  │  ├─ 8+ options → Select Field  
│  │  │  ├─ Dropdown handles many options
│  │  │  ├─ Performance acceptable to ~50 options
│  │  │  └─ Designer enforces readable exports
│  │  └─ Hierarchical? → Multiple Select Fields
│  │     ├─ NOT AdvancedSelect (beta/broken)
│  │     └─ Use cascading or prefixed options
│  └─ NO → Multiple selection needed
│
└─ Multiple selections → MultiSelect
   ├─ Returns: faims-core::Array
   ├─ ≤15 options: Expanded checklist mode
   ├─ >15 options: Dropdown mode  
   └─ ⚠️ No error display, CSV comma issues
```

### Decision Matrix

| Need | Field Type | Returns | Pros | Critical Issues |
|------|------------|---------|------|----------------|
| True/False | Checkbox | Boolean | Only boolean type, error display | Label not clickable |
| 1 from few | Select | String | Reliable, space efficient | No error display |
| 1 from many | Select | String | Handles 50+ options well | No error display |
| Many from list | MultiSelect | Array | Group validation, exclusive options | CSV export issues |
| Hierarchy | Multiple Selects | String each | Mobile compatible, reliable | More complex setup |

### Selection Strategy

1. **Default to Select** for single selection (most reliable)
2. **Use Checkbox** only for true boolean states  
3. **Deploy MultiSelect** for multiple selection from same vocabulary
4. **Avoid RadioGroup** (deprecated) and AdvancedSelect (beta)
5. **Prioritize Checkbox** for critical workflows needing error display

**Platform Considerations**:
- Mobile: Train users to tap checkbox icon (not label)
- Select: Excellent mobile dropdown experience
- MultiSelect: Limit to ≤20 options for performance
- RadioGroup: Accessibility violations, avoid entirely
- AdvancedSelect: Mobile broken, desktop only

**Accessibility Requirements**:
- Checkbox: Only field with error display, but label not clickable
- Select/MultiSelect: No error display, use clear helper text
- RadioGroup: Multiple WCAG violations, use Select instead
- AdvancedSelect: Not accessible, use cascading Selects instead

## ⚠️ Critical Security Risks {essential}

### Input Sanitization Issues

**HTML Content in Labels** [affects: All fields]:
- All field labels process HTML through DOMPurify sanitization
- **Risk**: Malformed HTML in option labels can break form rendering
- **Mitigation**: Validate all option text during configuration
- **Markdown parsing** in RadioGroup creates additional XSS vectors through markdown-it processing

**Option Value Injection** [affects: All fields]:
- No validation that selected values match defined options
- **Risk**: Malicious clients can submit arbitrary values
- **Impact**: Database pollution, conditional logic bypass
- **Mitigation**: Server-side validation required for all choice field data

### Data Integrity Vulnerabilities

**Conditional Logic Bypass** [affects: All fields]:
- Client can disable conditional field logic and submit hidden data  
- **Risk**: Required dependent fields bypassed
- **Example**: "Other" text field required when "Other" selected, but submission possible without text
- **Mitigation**: Server must validate all conditional requirements

**Validation Schema Bypass** [affects: All fields except Checkbox]:
- Error messages never displayed to users in Select, MultiSelect, RadioGroup, AdvancedSelect
- **Risk**: Users unaware of validation failures, submit invalid data
- **Impact**: Silent data corruption, workflow failures
- **Mitigation**: Implement server-side validation, add explicit instructions in helper text

### Export Data Tampering

**CSV Injection via Option Values** [affects: MultiSelect primarily]:
- Option values containing commas, quotes, or formulas can break CSV parsing
- **Risk**: Excel formula injection, data corruption during export
- **Example**: Option value `=SUM(1+1)` could execute in spreadsheets
- **Mitigation**: Sanitize all option values, avoid special characters

**Path Traversal in AdvancedSelect** [affects: AdvancedSelect]:
- Node names with " > " delimiters can break path parsing
- **Risk**: Hierarchy corruption, data integrity loss
- **Mitigation**: Validate node names exclude path delimiters

### Authentication and Session Issues

**State Persistence Vulnerabilities** [affects: All fields with meta.persistent]:
- Persistent field values carry across records without user awareness
- **Risk**: Sensitive selections propagated inappropriately  
- **Example**: "Contains human remains" checkbox persisting to non-burial contexts
- **Mitigation**: Audit persistent field configurations, clear documentation

**Cross-Form Data Leakage** [affects: All fields]:
- Form navigation can preserve field values between different record types
- **Risk**: Confidential classifications appearing in wrong contexts
- **Mitigation**: Implement proper form state cleanup

## What This Field Cannot Do {important}

### Selection Processing Limitations {important}

**Dynamic Vocabularies** [affects: All fields]:
- **Cannot load options from APIs** - All options must be predefined in JSON configuration. This limitation exists because fields are statically defined at form load time and must function offline. No integration with external taxonomies, databases, or web services is possible.

**Real-time Option Filtering** [affects: All fields]:  
- **Cannot modify option lists based on other fields** - Option sets are static. Cannot implement cascading dropdowns where second field options depend on first field selection. Workaround requires separate forms or conditional field display.

**Computed or Generated Options** [affects: All fields]:
- **Cannot create options from user input** - Options cannot be generated from calculations, string manipulation, or other field values. All possibilities must be enumerated at design time.

**Cross-Field Option Validation** [affects: All fields]:
- **Cannot validate option combinations across fields** - No support for rules like "If Material=Metal, then Technique cannot be Fired". Each field validates independently without awareness of other selections.

### Validation Limitations {important}

**User Feedback Display** [affects: Select, MultiSelect, RadioGroup, AdvancedSelect]:
- **No error message display** - Validation runs but error text never appears in UI. Users receive no feedback about what's wrong or how to fix validation failures. Form submission simply fails silently.

**Complex Validation Logic** [affects: All fields]:
- **No conditional validation** - Cannot make fields conditionally required based on other selections. Cannot implement logic like "Material field required only if Type=Artifact". Limited to static required/optional states.

**Empty State Detection** [affects: RadioGroup, AdvancedSelect]:
- **Cannot check if field is unselected** - No `isEmpty` operator for conditional logic. Cannot distinguish between "never touched" and "explicitly deselected" states. Must check for specific values only.

**Cross-Field Dependencies** [affects: All fields]:
- **No relational validation** - Cannot enforce relationships between field values. Cannot validate that selected combinations make logical sense or meet domain-specific rules.

### Display Limitations {important}

**Search and Filtering** [affects: All fields]:
- **No search within options** - Users must scroll through entire option lists. No type-ahead, filtering, or search capability even for vocabularies with hundreds of terms.

**Dynamic Presentation** [affects: All fields]:
- **No conditional option display** - Cannot show/hide specific options based on other field values. All defined options always appear regardless of context appropriateness.

**Responsive Layout Control** [affects: RadioGroup, AdvancedSelect]:
- **Fixed layout patterns** - RadioGroup only vertical, AdvancedSelect fixed width causes mobile horizontal scrolling. Cannot adapt presentation to screen size or content needs.

**Progressive Disclosure** [affects: AdvancedSelect]:
- **No lazy loading of hierarchies** - Entire tree structure rendered immediately. Cannot load branches on demand, causing performance issues with large taxonomies.

### Interaction Limitations {important}

**Multi-Selection Patterns** [affects: RadioGroup, Select, Checkbox, AdvancedSelect]:
- **Single selection fields cannot become multi-select** - No way to allow multiple selections from RadioGroup or Select options. Must use separate MultiSelect field with data structure changes.

**Deselection Control** [affects: Select, AdvancedSelect]:
- **Cannot clear selections** - Select has no clear button, AdvancedSelect cannot deselect once chosen. Must include empty options or reload forms to reset. RadioGroup deselection only works via mouse, not keyboard.

**Keyboard Navigation** [affects: RadioGroup, AdvancedSelect]:
- **Limited keyboard support** - RadioGroup cannot deselect via keyboard after selection. AdvancedSelect has poor keyboard navigation through hierarchies. Accessibility barriers for non-mouse users.

**Gesture Support** [affects: All fields]:
- **No touch gestures** - No swipe, pinch, long-press, or other mobile-specific interactions. All fields rely on basic tap/click patterns only.

## Common Use Cases {important}

### Archaeological and Heritage Recording

**Site Classification and Typology**:
- **Site types** → Select with 10-50 controlled vocabulary options (e.g., "Aboriginal scarred tree"). Include empty option "-- Not classified --". Set required validation only if mandatory classification workflow exists.
- **Artifact materials** → MultiSelect with expanded checklist for composite objects (ceramic with metal inlay, bone with shell decoration). Use exclusive options for "Unknown" or "Not applicable" states.
- **Condition assessment** → Select with 4-6 standardized levels (Excellent/Good/Fair/Poor/Destroyed). Always include "Not assessed" option for incomplete records.
- **Feature presence/absence** → Checkbox for binary archaeological indicators (charcoal present, bioturbation observed). Boolean return type enables programmatic logic for analysis and reporting.

**Heritage Compliance Workflows**:
- **Permit requirements** → MultiSelect for multiple concurrent permits (heritage/environmental/landowner). Use exclusive "None required" option that clears all other selections.
- **Stakeholder notifications** → MultiSelect for required consultations (Traditional Owners, Council, State Heritage). Include annotation field for contact details and dates.
- **Assessment confidence** → Select with epistemological categories (Certain/Probable/Possible/Speculative). Pair with uncertainty metadata for qualification.

### Scientific Data Collection

**Taxonomic and Species Recording**:
- **Species identification** → Select for single species per observation record. Use standardized taxonomic names as both value and label for immediate data interpretability. Include "Unknown" and "Multiple species" options.
- **Multiple species present** → MultiSelect for ecological transects or mixed assemblages. Limit to ≤20 most common species for performance, use "Other" with conditional TextField for rare species.
- **Taxonomic hierarchy** → Multiple cascading Select fields rather than AdvancedSelect (Kingdom → Phylum → Class → Order). Better mobile support and error handling than hierarchical field.

**Environmental Monitoring**:
- **Sampling methods used** → MultiSelect with exclusive options for quality control. "GPS coordinates taken", "Photographs captured", "Specimens collected" as discrete trackable actions.
- **Weather conditions** → MultiSelect for multiple concurrent conditions (rain/wind/cloud cover). Include "Excellent visibility" as exclusive option when conditions are optimal.
- **Equipment validation** → Checkbox series for procedural confirmation (instruments calibrated, GPS accuracy verified, protocols followed). Boolean logic supports quality assurance reporting.

### Administrative Workflows

**Project and Team Management**:
- **Project phases** → Select with controlled workflow states (Planning/Fieldwork/Analysis/Reporting/Complete). Include "On hold" and "Cancelled" for project lifecycle management.
- **Team member assignments** → MultiSelect for multiple specialists involved. Use "Team leader" option as exclusive when single responsibility model applies.
- **Institutional affiliations** → Select with organization codes. Use Designer value=label pattern to maintain human-readable exports without lookup tables.

**Quality Assurance and Review**:
- **Data quality flags** → Checkbox series for quality indicators (peer reviewed, supervisor approved, external validation completed). Boolean states enable automated workflow triggers.
- **Review status** → Select with review workflow states (Draft/Under review/Approved/Rejected/Requires revision). Include reviewer assignment through conditional TextField.

### Field Research Scenarios

**Site Access and Safety**:
- **Access permissions obtained** → MultiSelect for multiple permit types with exclusive "Access denied" option. Include conditional TextField for denial reasons and alternative approaches.
- **Safety protocols followed** → Checkbox series for procedural compliance (risk assessment completed, emergency contacts notified, first aid available). Boolean logic supports safety audit trails.
- **Site accessibility** → Select with accessibility categories for planning return visits. Include "Requires special equipment" or "Seasonal access only" options.

**Recording Methodology Documentation**:
- **Recording methods employed** → MultiSelect for multiple concurrent techniques (photography/drawing/GPS/photogrammetry/total station). Enable comprehensive methodology documentation.
- **Data collection completeness** → Select with completion levels (Complete/Partial/Preliminary/Incomplete). Include conditional annotation for explaining partial records.

### Data Entry Patterns

**Conditional Field Triggers**:
- **Recording detail level** → Select with workflow options (Rapid assessment/Standard recording/Detailed analysis). Each option triggers different conditional field groups through operators.
- **"Other" specification patterns** → Select with "Other" option triggering conditional TextField. Standard pattern for extending controlled vocabularies without losing structure.
- **Workflow branching** → Select for process decisions (Continue recording/Skip section/Mark for later/Complete record). Each selection changes available fields and required validations.

**Data Export and Integration**:
- **Export filtering** → Checkbox series for data subset selection (Include photographs/Export GPS coordinates/Generate report/Share with team). Boolean states enable flexible export configuration.
- **Data sharing permissions** → Select with privacy levels (Public/Restricted/Confidential/No sharing). Include conditional text for access restriction details.

## Designer Component Mapping {essential}

### Designer UI vs JSON Component Names

The Designer interface uses human-readable labels that don't match the technical JSON component names, creating confusion during configuration and troubleshooting. This mapping is critical for JSON editing and error diagnosis:

| Designer Display | JSON Component | Namespace | Notes |
|------------------|----------------|-----------|-------|
| "Checkbox" | `Checkbox` | `faims-custom` | Matches exactly |
| "Select Multiple" | `MultiSelect` | `faims-custom` | Different names |
| "Select one option" | `RadioGroup |
| "Select Field" | `Select` | `faims-custom` | Different names |
| "Select Field (Hierarchical)" | `AdvancedSelect` | `faims-custom` | 🔴 BETA status |

### Designer Limitations Requiring JSON

**Complete JSON Requirement** [affects: AdvancedSelect]:
- **Hierarchy definition**: While Designer provides a JSON template builder for `optiontree` structure, complex hierarchies may require manual JSON editing for complete tree structure including all nodes and relationships.

**Advanced Properties** [affects: All fields]:
- **Validation schemas**: Beyond basic `required` checkbox, all validation rules require JSON editing (`yup.oneOf`, `yup.min`, custom messages)
- **Initial values**: Designer enforces defaults (Checkbox: false, others: empty), though "copy value to new records" provides persistence after first entry
- **Performance properties**: `fullWidth`, `variant`, `disabled` states not exposed in Designer
- **MUI component props**: `FormControlLabelProps`, `SelectProps`, etc. only accessible via JSON

**Complex Option Configuration** [affects: RadioGroup, Select]:
- **Value vs Label separation**: Designer enforces value=label. JSON editing required if you need different internal values from display labels (e.g., store "arch_site" while displaying "Archaeological Site")
- **Option validation**: `yup.oneOf` validation against defined options requires JSON configuration

### Technical Implementation Note

**Designer-JSON Interaction Warning**:
When switching between Designer and JSON editing, **Designer changes can overwrite manual JSON configurations**. This affects:
- Custom validation schemas beyond required checkbox
- Modified initial values 
- Advanced component properties
- Complex option configurations

**Recommended Workflow**:
1. Configure basic properties in Designer first
2. Export to JSON for advanced configuration  
3. Make all further changes in JSON only
4. Do not return to Designer after JSON customization

## Designer Capabilities vs JSON Enhancement {comprehensive}

### What Designer CAN Configure

For complete meta properties documentation, see [Meta Properties Reference](meta-properties-reference.md).

**Checkbox**:
- ✅ Label, helper text, and advanced helper text
- ✅ Required validation (checkbox adds `yup.required`)
- ✅ Field name and ID assignment
- ✅ Annotation and uncertainty toggles (see Meta Properties Reference)
- ✅ Basic conditional logic for field visibility

**Select**:
- ✅ Option list management (add, remove, reorder options)
- ✅ Label, helper text configuration
- ✅ Required field checkbox
- ✅ Enforces value = label for human-readable exports
- ✅ Basic conditional logic setup

**MultiSelect**:
- ✅ Option list with drag-drop reordering
- ✅ Expanded checklist mode toggle
- ✅ Per-option exclusive configuration via checkbox (exclusive options CAN be set in Designer)
- ✅ Label and helper text
- ✅ Markdown syntax support in option labels

**RadioGroup (Deprecated)**:
- ✅ Manual option entry with drag-drop
- ✅ Basic field properties
- ✅ Required validation checkbox
- ❌ NO preview capability (must deploy to test)

**AdvancedSelect (Beta)**:
- ✅ Basic field properties (label, helperText, valuetype)
- ❌ **Hierarchy structure NOT configurable** - major limitation

### What Requires JSON Editing

**Advanced Validation** [affects: All fields]:
- Complex validation chains beyond basic required
- Custom error messages (though they won't display)
- `yup.oneOf` validation against specific values
- Array validation for MultiSelect (`yup.min`, `yup.max`)
- Boolean validation for Checkbox (`yup.oneOf([true])` for must-be-checked)

**Initial Value Control** [affects: All fields]:
- **Checkbox**: Designer forces `initialValue: false`, JSON can set `true` for pre-checked
- **Select/RadioGroup**: Designer sets empty string, JSON can set specific option
- **MultiSelect**: Designer sets empty array, JSON can pre-populate selections
- **AdvancedSelect**: JSON required for any non-empty initial state

**Performance and Display Properties** [affects: All fields]:
- `fullWidth` control for field width behavior
- `variant` styling (outlined, filled, standard)
- `disabled` state for entire field
- Component-specific props (`FormControlLabelProps`, `SelectProps`)

**Advanced Option Configuration**:
- **Different values vs labels**: Designer enforces identical strings, JSON allows separation
- **MultiSelect exclusive options**: Array of mutually exclusive values
- **Complex hierarchies**: AdvancedSelect `optiontree` structure completely JSON-only

### Designer vs JSON Workflow

**Designer-First Approach** (Recommended):
1. Configure all basic properties in Designer interface
2. Set up option lists and basic conditional logic
3. Test functionality with Designer defaults
4. Export to JSON for advanced configuration
5. **Never return to Designer** after JSON customization

**JSON-Only Approach** (Advanced):
1. Create field structure completely in JSON
2. Define complex validation schemas
3. Configure advanced component properties
4. Test thoroughly as no Designer preview available

**Hybrid Approach Risks**:
- Designer changes overwrite JSON customizations
- Validation schemas reset to basic `required` only  
- Advanced properties lost when switching to Designer
- Complex option configurations simplified

### Designer Limitations {important}

See [Designer Limitations Reference](designer-limitations-reference.md) for testing, validation, and configuration constraints that apply to all fields.

**Selection Field-Specific Limitations**:
- **Markdown processing performance**: All option labels processed through markdown parser at design-time, potentially causing lag with >20 options (hypothetical limit)
- **No option validation**: Designer doesn't validate that option values are unique or contain valid characters
- **No bulk option management**: Cannot import/export option lists or edit multiple options at once
- **Option value/label coupling**: Designer enforces option display text = stored value (cannot have "Archaeological Site" display with "arch_site" stored)

## Component Namespace Errors {important}

See [Component Namespace Reference](component-namespace-reference.md) for complete namespace documentation, error troubleshooting, and Designer name mapping.

### Selection Field-Specific Notes

**All selection fields use the same namespace**:
- Namespace: `faims-custom` for ALL selection fields (Checkbox, MultiSelect, RadioGroup, Select, AdvancedSelect)
- Never use `formik-material-ui` for selection fields

**Quick Reference for Selection Fields**:
| Component | Namespace | Case-Sensitive Name |
|-----------|-----------|-------------------|
| Checkbox | `faims-custom` | `Checkbox` (capital C) |
| MultiSelect | `faims-custom` | `MultiSelect` (capitals M, S) |
| RadioGroup | `faims-custom` | `RadioGroup` (capitals R, G) |
| Select | `faims-custom` | `Select` (capital S) |
| AdvancedSelect | `faims-custom` | `AdvancedSelect` (capitals A, S) |


## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| Yes/No questions | Checkbox | Clear boolean state |
| Single choice (<10 options) | Select | Compact dropdown |
| Single choice (>10 options) | Select | Searchable dropdown |
| Multiple choices | MultiSelect | Multi-select dropdown |
| Hierarchical categories | AdvancedSelect | Tree navigation |
| Visible options (2-5) | RadioGroup | All options visible |

### Decision Criteria
- **Number of options**: <10 → Select, >10 → Select with search, Hierarchical → AdvancedSelect
- **Selection count**: Single → Select, Multiple → MultiSelect, Boolean → Checkbox
- **Visibility**: All dropdowns hide options until opened (RadioGroup for visible options)
- **Data structure**: Flat → Select/MultiSelect, Tree → AdvancedSelect

## Common Characteristics {important}

### Shared Behaviors Across Selection Fields

**Static Vocabulary Requirement** [affects: All fields]:
All selection fields require predefined option lists configured at design time. No field can load options dynamically from APIs, databases, or user input due to offline operation requirements. This limitation is architectural - fields are statically defined at form load time and cannot modify their option sets during runtime.

**Consistent Data Flow Patterns** [affects: All fields]:
- All fields integrate with Formik for form state management
- Values immediately update on user interaction (no delayed commit)
- All fields support conditional logic as both triggers and targets
- Validation runs immediately on value change but display varies by field type

**Shared Metadata Support** [affects: All fields]:
- **Annotation fields**: All fields can include optional annotation metadata with configurable labels
- **Uncertainty indicators**: All fields support uncertainty metadata for data quality tracking
- **Persistent values**: All fields can carry values forward to new records when `meta.persistent: true`
- **Parent display**: All fields can show values in parent record summaries when `meta.displayParent: true`

### Configuration Rules {important}

#### Base Properties [affects: All fields] {important}

**Required Configuration Elements**:
```json
{
  "component-namespace": "faims-custom",
  "component-name": "Select",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "label": "Field Label"
  }
}
```

**Standard Optional Properties**:
- `helperText`: Guidance text displayed near field
- `required`: Boolean flag for validation (behavior varies by field)
- `id`: Field identifier (defaults to name if not specified)
- `disabled`: Boolean flag to disable entire field
- `meta`: Object containing annotation, uncertainty, persistence settings

**Designer vs JSON Property Exposure**:
- **Designer exposes**: Basic properties (name, label, required, helper text, meta toggles)
- **JSON only**: Advanced validation, initial values, performance properties, MUI component props
- **Hybrid risk**: Designer changes overwrite JSON customizations

#### Validation Rules [affects: All fields] {important}

**Universal Validation Schema Structure**:
```json
"validationSchema": [
  ["yup.string"],
  ["yup.required", "Error message"],

]
```

#### Standard Validation Rules [affects: All fields] {important}

**Type Validation** (Always included):
- **Checkbox**: `["yup.bool"]` - Validates true/false/null values
- **Select/RadioGroup/AdvancedSelect**: `["yup.string"]` - Validates string values
- **MultiSelect**: `["yup.array"]` - Validates array structure

**Required Validation** (Optional but common):
- **Behavior varies significantly by field type**
- **Checkbox**: `["yup.required"]` allows `false` (unchecked) as valid
- **Select/RadioGroup**: `["yup.required"]` prevents empty string submission
- **MultiSelect**: `["yup.required"]` allows empty array `[]` as valid (use `yup.min` instead)
- **AdvancedSelect**: `["yup.required"]` prevents empty selection but shows no error message

#### Validation Behavior [affects: specific fields] {important}

**Error Message Display Capability**:
- **Checkbox**: ✅ **Full error display** - Shows error text and red styling
- **Select**: ❌ **No error display** - Validation runs but messages never shown
- **MultiSelect**: ❌ **No error display** - Silent validation failures
- **RadioGroup**: ⚠️ **Color only** - Red styling but no error text
- **AdvancedSelect**: ❌ **No error display** - Silent validation failures

#### Validation Timing Behavior [affects: All fields] {important}

See [Validation Timing Reference](validation-timing-reference.md) for complete universal validation behavior.

**Selection Field-Specific Notes**:
- **Binary state changes**: Selection fields validate on discrete state changes rather than keystroke
- **No partial validation**: Selection is either valid or invalid, no intermediate states
- **Error display limitations**: Select and AdvancedSelect cannot display error messages even when validation fails

### Security Considerations {important}

See [Security Considerations Reference](../references/constraints-reference.md#field-specific-security-considerations) for comprehensive security guidelines.

**Selection Field-Specific Security Notes**:
- No server-side validation that submitted values match defined options
- CSV formula injection risk when option values contain =, +, -, @
- RadioGroup markdown processing creates XSS attack surface
- AdvancedSelect delimiter injection with " > " corrupts hierarchy
- Conditional logic easily bypassed via browser DevTools

### Performance Boundaries {important}

See [Performance Thresholds Reference](performance-thresholds-reference.md) for comprehensive performance limits, testing scenarios, and optimization triggers.

**Selection Field-Specific Performance Notes**:
- **Markdown processing**: RadioGroup/Select with >20 options causes significant lag when markdown enabled
- **DOM node multiplication**: Total nodes = fields × options × nodes-per-option (RadioGroup: ~8, Select: ~4, MultiSelect: ~6)
- **RadioGroup deprecation**: Use Select for >7 options due to severe performance issues
- **MultiSelect expanded mode**: Maximum 15 options for mobile, 25 for desktop
- **AdvancedSelect**: Beta component with poor performance above 50 nodes

**AdvancedSelect** [affects: AdvancedSelect] 🔴 BETA:
- **Total Node Limits**:
  - **Optimal**: ≤50 total nodes across entire hierarchy
  - **Acceptable**: 51-100 nodes with desktop-only deployment
  - **Degraded**: 101-500 nodes cause significant interaction lag
  - **Unusable**: >500 nodes likely to crash browsers
- **Depth Limits**:
  - **Optimal**: ≤3 hierarchy levels for usability
  - **Acceptable**: 4-5 levels with careful UX design
  - **Problematic**: >5 levels difficult to navigate on mobile
- **Breadth Limits**:
  - **Optimal**: ≤15 nodes per hierarchy level
  - **Acceptable**: 16-30 nodes per level with scroll management
  - **Unusable**: >30 nodes per level cause navigation confusion

**Performance Testing Requirements**:
- Test on lowest-specification target device
- Monitor memory usage with large option sets
- Verify touch target adequacy on mobile screens
- Check form load time with complete field configuration
- Validate CSV export performance with maximum data sets

### Platform Behaviors {important}

#### Cross-Platform Consistency {important}

**Rendering Engine Consistency** [affects: All fields]:
All choice fields use Material-UI components consistently across platforms rather than native controls. This design choice prioritizes consistent user experience over platform conventions:

- **Benefit**: Identical appearance and behavior across iOS, Android, and desktop
- **Trade-off**: Users may expect native iOS picker or Android dropdown patterns
- **Training requirement**: Users must learn Material-UI interaction patterns regardless of platform familiarity

**Touch Target Standards** [affects: All fields]:
- **Desktop**: Mouse interaction with hover states, precise clicking
- **Mobile**: Touch targets sized for finger interaction (minimum 44px iOS, 48px Android recommended)
- **Consistency**: All fields attempt to meet mobile touch standards on all platforms

#### iOS Behaviors [affects: specific fields] {comprehensive}

**Checkbox** [affects: Checkbox]:
- **Critical UX Issue**: Label text not tappable, must tap 24×24px checkbox icon directly
- **Touch target**: 48×48px checkbox area meets iOS accessibility guidelines  
- **Visual style**: Material-UI custom SVG, not iOS native toggle switch
- **No haptic feedback**: Missing tactile confirmation common in iOS apps
- **Keyboard**: Not applicable (checkbox not keyboard-accessible in mobile Safari)

**Select** [affects: Select]:
- **Dropdown behavior**: Uses Material-UI portal dropdown, not iOS native picker wheel
- **Touch interaction**: Tap to open, tap option to select, behaves like desktop
- **Scrolling**: Standard touch scroll within dropdown list
- **Selection feedback**: Immediate display of selected value
- **No gesture support**: Cannot swipe or use other iOS-standard gestures

**MultiSelect** [affects: MultiSelect]:
- **Expanded checklist**: Each row fully tappable (better than Checkbox field)
- **Dropdown mode**: Same portal-based dropdown as Select
- **Performance**: Degrades with >20 options due to DOM node count
- **Exclusive options**: Visual feedback when options become disabled

**RadioGroup:
- **Touch targets**: ~42px radio buttons (below iOS 44px recommendation)
- **Label interaction**: NOT tappable (same issue as Checkbox)
- **Deselection**: Can tap selected radio to deselect (mouse behavior on touch)
- **Accessibility**: Major VoiceOver violations, screen reader support broken

**AdvancedSelect** [affects: AdvancedSelect] 🔴 BETA:
- **Critical mobile failure**: Fixed 500px width causes horizontal scrolling on all iOS devices
- **Touch precision**: Chevron icons too small for reliable finger tapping
- **No mobile optimization**: Desktop tree navigation on mobile screen
- **Performance**: Severe degradation with >50 nodes

#### Android Behaviors [affects: specific fields] {comprehensive}

**Checkbox** [affects: Checkbox]:
- **Same label issue**: Label not tappable, must tap checkbox directly
- **Touch targets**: 48×48px meets Android accessibility guidelines
- **Material ripple**: Standard Material Design ripple effect on interaction
- **Visual consistency**: Proper Material-UI theming matches Android design language

**Select** [affects: Select]:
- **Dropdown behavior**: Material-UI dropdown with proper Material Design styling
- **Touch interaction**: Standard tap behavior with Material ripple effects
- **Back button**: Android back button closes dropdown without selection
- **Scrolling**: Smooth scroll with momentum, familiar Android behavior

**MultiSelect** [affects: MultiSelect]:
- **Material consistency**: Proper Material Design checkbox styling in both modes
- **Touch feedback**: Material ripple effects on all interactions
- **Performance**: Similar degradation patterns as iOS

**RadioGroup:
- **Material styling**: Proper Material Design radio button appearance
- **Same accessibility issues**: TalkBack violations, poor screen reader support
- **Performance**: Identical markdown processing lag as other platforms

**AdvancedSelect** [affects: AdvancedSelect] 🔴 BETA:
- **Same width issues**: Horizontal scrolling on most Android devices
- **Touch accuracy**: Difficult to select correct nodes on smaller screens
- **No Android optimizations**: No platform-specific improvements

#### Web/Desktop Behaviors [affects: All fields] {important}

**Mouse Interaction Patterns** [affects: All fields]:
- **Hover states**: All fields provide visual feedback on mouse hover
- **Precise clicking**: Exact pixel clicking allows smaller touch targets than mobile
- **Scroll behavior**: Mouse wheel scrolling in dropdown lists and hierarchies
- **Context menus**: Right-click behavior varies by field type (some suppress, others allow)

**Keyboard Navigation** [affects: All fields]:
- **Tab order**: All fields participate in logical tab sequence through form
- **Accessibility**: Better keyboard support than mobile, but still limited
- **Keyboard shortcuts**: Limited to basic Space/Enter/Arrow keys, no advanced shortcuts

**Desktop-Specific Advantages**:
- **Larger screens**: Can accommodate more options without scrolling
- **Precise interaction**: Mouse allows accurate selection of small UI elements
- **Multiple input methods**: Keyboard and mouse combination enables faster interaction
- **Performance**: Desktop browsers handle large option sets better than mobile

**Desktop Performance Characteristics**:
- **Select**: Can handle 100+ options with acceptable performance
- **MultiSelect**: Dropdown mode works well with 50+ options  
- **RadioGroup**: Still suffers from markdown processing issues
- **AdvancedSelect**: Better performance but still limited by architecture

### Shared Limitations {important}

#### Designer Interface Constraints {important}

**Configuration Limitations Across All Fields**:
- **No preview capability**: Cannot see field appearance or test interactions before deployment to actual devices
- **No field type conversion**: Cannot change RadioGroup to Select without complete field recreation and data loss
- **Limited parameter exposure**: Advanced properties require JSON editing with risk of Designer overwriting changes
- **No validation testing**: Cannot verify that validation schemas work correctly before deployment

**Option Management Constraints**:
- **Manual entry only**: No import from CSV, API, or external vocabulary sources  
- **No batch operations**: Cannot duplicate option sets across fields or projects
- **No option validation**: Designer doesn't verify option values are unique or contain safe characters
- **Performance warnings missing**: No indication when option counts will cause performance issues

#### Export Behavior {important}

See [Data Export Reference](data-export-reference.md) for comprehensive export documentation including CSV/JSON formats, special character handling, and Excel issues.

**Selection Field-Specific Export Notes**:
- **Value vs Label**: Exports values not labels (except Designer-created Select with value=label)
- **MultiSelect CSV**: Comma-joined values problematic if options contain commas
- **AdvancedSelect**: Exports path string with " > " delimiter, not hierarchical structure
- **Checkbox**: Exports as boolean true/false, not "TRUE"/"FALSE" strings
- **No option definitions**: Export doesn't include available options, only selected values

#### Component Architecture {comprehensive}

**Rendering Limitations** [affects: All fields]:
- **No virtualization**: All options render immediately in DOM, causing performance issues with large sets
- **No lazy loading**: Cannot load option subsets on demand
- **No search capability**: Users must manually scroll through all options
- **Fixed layouts**: Cannot adapt presentation to content size or device capabilities

**State Management Issues** [affects: All fields]:
- **No undo/redo**: Cannot reverse selection changes
- **State persistence problems**: Conditional navigation can lose expansion states (AdvancedSelect)
- **No draft states**: Changes apply immediately without confirmation capability

**Integration Constraints** [affects: All fields]:
- **Static vocabularies only**: No integration with external taxonomy services
- **No real-time updates**: Cannot update option lists based on other field changes
- **Limited conditional logic**: Only basic operators supported (equal, not-equal, contains)
- **No cross-field validation**: Cannot validate option combinations across multiple fields

#### Accessibility Compliance {important}

**WCAG 2.1 Level A Violations** [affects: Most fields]:

**Missing ARIA Attributes** [affects: Select, MultiSelect, RadioGroup, AdvancedSelect]:
- No `aria-required` for required fields
- No `aria-invalid` for error states  
- No `aria-describedby` for helper text association
- No `aria-errormessage` for validation feedback

**Keyboard Navigation Issues** [affects: RadioGroup, AdvancedSelect]:
- **RadioGroup**: Cannot deselect via keyboard after selection
- **AdvancedSelect**: Poor keyboard navigation through hierarchy trees
- **General**: No keyboard shortcuts for efficient navigation

**Screen Reader Support** [affects: RadioGroup, AdvancedSelect]:
- **RadioGroup**: Required state not announced, error states not communicated
- **AdvancedSelect**: Hierarchical structure not properly announced
- **All fields**: Validation error messages not announced when validation fails

**Visual Accessibility** [affects: Select, MultiSelect, RadioGroup, AdvancedSelect]:
- **Color-only error indication**: Error states shown only through color changes
- **No high contrast mode**: Limited support for high contrast themes
- **Small touch targets**: Some fields don't meet minimum 44px/48px touch target requirements

#### Testing Guidelines {comprehensive}

**Pre-Deployment Testing Checklist** [affects: All fields]:

**Functional Testing**:
- [ ] Test with minimum viable option set (2-3 options)
- [ ] Test with maximum expected option count for performance
- [ ] Verify all validation schemas work as expected
- [ ] Test conditional logic with all field states
- [ ] Verify data export format meets requirements

**Platform Testing**:
- [ ] Test on lowest-specification target mobile device
- [ ] Verify touch targets adequate on mobile screens
- [ ] Test keyboard navigation on desktop
- [ ] Check screen reader compatibility where required
- [ ] Validate consistent behavior across target browsers

**Performance Testing**:
- [ ] Monitor form load time with full field configuration
- [ ] Test interaction responsiveness with maximum option counts
- [ ] Check memory usage patterns with large datasets
- [ ] Verify export performance with realistic data volumes

**Accessibility Testing**:
- [ ] Test with screen reader (NVDA/JAWS on Windows, VoiceOver on Mac)
- [ ] Verify keyboard-only navigation works
- [ ] Check color contrast meets WCAG requirements
- [ ] Test with high contrast and zoom settings

**Data Integrity Testing**:
- [ ] Verify submitted values match expected format
- [ ] Test edge cases (empty submissions, special characters)
- [ ] Validate export/import round-trip data integrity
- [ ] Check conditional field behavior with various selections

## Field Reference {essential}

### Checkbox (Checkbox in Designer) {essential}
<!-- keywords: boolean, consent, binary, toggle, checkbox -->

**Quick Reference:**
| Property | Value |
|----------|-------|
| Designer Label | Checkbox |
| Component Name | Checkbox |
| Namespace | faims-custom |
| Type Returned | faims-core::Bool |
| Error Display | ✅ Full (only field with proper errors) |
| Mobile Support | ✅ Full (label not clickable) |
| Accessibility | ❌ Poor (no ARIA) |
| Touch Targets | 24×24px icon, 48×48px target |
| Performance | 20-30 optimal, 50+ degraded, 100+ unusable |
| Storage | Boolean (true/false, null→false) |

### Purpose {essential}

The Checkbox field provides binary state capture through a Material-UI checkbox component, returning `faims-core::Bool` values. As the **only boolean field type in Fieldmark**, Checkbox serves dual purposes: simple true/false data capture and consent/acknowledgment workflows. Unlike RadioGroup and Select which return strings, Checkbox returns actual boolean primitives, making it ideal for programmatic logic.

**When to use:**
- Binary archaeological indicators - Presence/absence of features (charcoal present, bioturbation observed)
- Consent and agreements - Terms acceptance, privacy policy acknowledgment, data usage consent
- Procedural confirmations - Safety checks completed, equipment calibrated, protocols followed
- Optional enhancements - Include photographs, request review, generate report
- Data quality flags - Provisional data, requires verification, peer reviewed

### Core Configuration {essential}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "Checkbox",
  "type-returned": "faims-core::Bool",
  "component-parameters": {
    "name": "terms-accept",
    "label": "I accept the terms and conditions",
    "helperText": "You must accept to continue",
    "required": true
  },
  "validationSchema": [
    ["yup.bool"],
    ["yup.oneOf", [true], "You must accept the terms to proceed"]
  ],
  "initialValue": false
}
```

### Key Features {essential}

- ✅ **Boolean primitive values** - Returns true/false, not strings
- ✅ **Best error display** - Only choice field showing both red color and error messages
- ✅ **Immediate validation feedback** - Errors appear on change event after interaction
- ✅ **Conditional logic support** - Works with boolean operators (equal: true/false)
- ⚠️ **Label not clickable** - Must click 24×24px checkbox icon directly, not label text (iOS requires 44×44px minimum)
- ⚠️ **Required validation misleading** - "Required" allows false but prevents null/undefined
- ⚠️ **Performance limits** - Degrades at 50+ checkboxes per form, unusable at 100+ (use MultiSelect instead)
- ❌ **No ARIA attributes** - Fails WCAG 2.1 Level A requirements
- 🐛 **Label association broken** - Screen readers cannot announce field purpose

### Configuration Parameters {important}

**Required Parameters:**
- `name` (string): Field identifier
- `label` (string): Checkbox label text

**Optional Parameters:**
- `id` (string): HTML element ID (defaults to name)
- `helperText` (string): Additional guidance text
- `advancedHelperText` (string): Extended help with more detail
- `required` (boolean): Visual indicator only - doesn't enforce "must be checked"

**JSON-Only Properties:**
- `initialValue` (boolean): Can set to `true` for pre-checked (Designer forces `false`)
- `FormControlLabelProps` (object): MUI label customization (deprecated)
- `FormHelperTextProps` (object): MUI helper text customization (deprecated)

**Meta Fields:**
- `annotation.include` (boolean): Enable annotation field
- `uncertainty.include` (boolean): Enable uncertainty field

### Checkbox-Specific Validation {important}

| Validation Type | Configuration | Actual Behaviour | Error Message | Designer Support |
|-----------------|---------------|------------------|---------------|------------------|
| Boolean type | `["yup.bool"]` | Accepts true/false/null/undefined | "Must be a boolean" | ✅ Default |
| Required field | `["yup.required"]` | **Misleading!** Prevents null/undefined but allows false | "This field is required" | ✅ Checkbox |
| Must be checked | `["yup.oneOf", [true], "Message"]` | Only accepts true (checkbox must be checked) | Custom message | ❌ JSON only |
| Must be unchecked | `["yup.oneOf", [false]]` | Only accepts false | "Must be unchecked" | ❌ JSON only |
| Explicit selection | `["yup.oneOf", [true, false], "Message"]` | Requires deliberate true OR false | Custom message | ❌ JSON only |

**Critical Validation Clarification:**
"Required" for checkboxes does NOT mean "must be checked":
- `["yup.required"]` allows `false` (unchecked) as valid
- For consent forms use: `["yup.oneOf", [true], "You must accept"]`
- Designer's "required" checkbox creates confusion

**Validation Timing:**
- Validates on change (immediate feedback after first interaction)
- Errors display on blur (user leaves field)
- All validation runs on form submit attempt

### Checkbox-Specific Issues {important}

- **Label not clickable** - Users must tap/click the small checkbox target, violating standard checkbox behavior
- **Touch target too small** - 24×24px checkbox on mobile when 44×48px recommended
- **No haptic feedback** - No tactile response on mobile interactions
- **Accessibility failures** - Missing aria-required, aria-invalid, aria-describedby attributes
- **Screen reader incompatible** - Label not programmatically associated with checkbox
- **Initial state limitation** - Designer always forces `initialValue: false`

**Platform-Specific Behaviors:**
- **iOS**: Touch target below 44×44px Apple HIG standard, no native checkbox styling
- **Android**: Material Design 48×48px touch target not met, uses Material checkbox appearance
- **Desktop**: Hover states work correctly, click target matches visual 24×24px size
- **All platforms**: Label click does not toggle checkbox (Material-UI limitation)

### Field-Specific Troubleshooting {important}

| Issue | Cause | Solution | Prevention |
|-------|-------|----------|------------|
| Required not working | Checkbox can be unchecked despite required | "Required" doesn't mean "must be checked" | Use `["yup.oneOf", [true]]` for must-be-checked |
| Label not clickable | Must click checkbox itself, not label text | Label not properly associated | Known issue - train users to click checkbox |
| No initial checked | Cannot set checkbox to start checked in Designer | Designer forces false | Edit JSON to set `initialValue: true` |
| Validation confusing | Error appears when unchecked but field is "required" | Misunderstanding of boolean validation | Required prevents null, not false |
| Can't detect untouched | Conditional logic treats untouched same as unchecked | No isEmpty operator | Use different field type or track interaction separately |
| Multiple checkboxes | Can't enforce "at least one checked" across checkboxes | Individual checkboxes don't cross-validate | Use MultiSelect with expandedChecklist instead |

### Implementation Examples {comprehensive}

#### Terms Acceptance (Must Be Checked)
```json
{
  "terms-accept": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "name": "terms-accept",
      "label": "I accept the terms and conditions",
      "helperText": "You must accept to continue",
      "required": true
    },
    "validationSchema": [
      ["yup.bool"],
      ["yup.oneOf", [true], "You must accept the terms to proceed"]
    ],
    "initialValue": false
  }
}
```

#### Optional Enhancement Flag
```json
{
  "include-detailed": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "name": "include-detailed",
      "label": "Record detailed measurements",
      "helperText": "Check to show additional measurement fields"
    },
    "validationSchema": [["yup.bool"]],
    "initialValue": false,
    "meta": {
      "persistent": true
    }
  }
}
```

#### Data Quality Indicator with Persistence
```json
{
  "peer-reviewed": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "name": "peer-reviewed",
      "label": "Data peer reviewed",
      "advancedHelperText": "Check after secondary verification completed"
    },
    "validationSchema": [["yup.bool"]],
    "initialValue": false,
    "meta": {
      "displayParent": true,
      "persistent": true
    }
  }
}
```

#### Migration from RadioGroup Pattern
```json
{
  "heritage-present": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "name": "heritage-present",
      "label": "Aboriginal heritage identified",
      "helperText": "Previously Yes/No radio - now checkbox for boolean logic",
      "required": true
    },
    "validationSchema": [
      ["yup.bool"],
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

### JSON Anti-patterns

```json

"validationSchema": [["yup.required"]]


"validationSchema": [["yup.oneOf", [true], "Must accept"]]





"helperText": "Click the label to select"


"helperText": "Click the checkbox (not the label) to select"
```

### Common Spec Mappings

**Designer → JSON mappings:**
- Designer "Required" → `required: true` + `["yup.required"]` (misleading)
- Designer Label → `label` property
- Designer Helper Text → `helperText` property
- Designer Annotation toggle → `meta.annotation.include` (see [Meta Properties Reference](meta-properties-reference.md))

**Conditional logic mappings:**
- Boolean true condition → `{"operator": "equal", "value": true}`
- Boolean false condition → `{"operator": "equal", "value": false}`
- Cannot check for empty/null state

---

### MultiSelect (Select Multiple in Designer) {essential}
<!-- keywords: multiple, selection, checklist, dropdown, array -->

**Quick Reference:**
| Property | Value |
|----------|-------|
| Designer Label | Select Multiple |
| Component Name | MultiSelect |
| Namespace | faims-custom |
| Type Returned | faims-core::Array |
| Error Display | ❌ No error messages shown |
| Mobile Support | ⚠️ Limited (performance issues >20 options) |
| Accessibility | ❌ Poor (no ARIA, on roadmap) |
| Touch Targets | Full row clickable (48px height) |
| Performance | ≤15 expanded optimal, 20+ dropdown, 50+ degraded |
| Storage | Array of strings, empty array valid |

### Purpose {essential}

The MultiSelect field enables multiple value selection from predefined option lists, returning `faims-core::Array` values. It provides two distinct display modes—dropdown with checkboxes or expanded checklist—optimizing for different option counts and screen constraints. Unlike the single-selection limitations of RadioGroup, Select, and Checkbox fields, MultiSelect handles group validation through a single field returning an array.

**When to use:**
- Archaeological site features - Multiple characteristics present (defensive walls, domestic structures, industrial remains)
- Artefact materials - Objects with composite materials (ceramic with metal inlay, bone with shell decoration)
- Site formation processes - Multiple concurrent processes (alluvial, colluvial, anthropogenic)
- Conservation treatments - Multiple interventions applied (cleaned, consolidated, reconstructed)
- Damage assessment - Multiple damage types present (weathering, vandalism, vegetation)
- Exclusive conditions - "None observed" or "Unable to assess" options that clear all others

### Core Configuration {essential}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "MultiSelect",
  "type-returned": "faims-core::Array",
  "component-parameters": {
    "name": "site-features",
    "id": "site-features",
    "label": "Site Features",
    "helperText": "Select all that apply",
    "ElementProps": {
      "options": [
        {"value": "defensive", "label": "Defensive structures"},
        {"value": "domestic", "label": "Domestic occupation"},
        {"value": "industrial", "label": "Industrial remains"}
      ],
      "expandedChecklist": true
    }
  },
  "validationSchema": [
    ["yup.array"],
    ["yup.min", 1, "Select at least one feature"]
  ],
  "initialValue": []
}
```

### Key Features {essential}

- ✅ **Multiple selection support** - Returns array of selected values
- ✅ **Two display modes** - Dropdown or expanded checklist
- ✅ **Exclusive options** - Mutual exclusivity (selecting "None" clears others)
- ✅ **Label clickable** - Unlike Checkbox field, entire row is clickable
- ✅ **Array conditional operators** - Supports contains, contains-all-of, etc.
- ⚠️ **Empty array validation gotcha** - `["yup.required"]` considers `[]` as valid
- ⚠️ **Performance degradation** - Severe lag with >20 options in checklist mode
- ❌ **No error message display** - Validation runs but messages never appear
- ❌ **No search/filter** - Must scroll through all options
- 🐛 **CSV export issue** - Comma-separated values break if options contain commas

### Configuration Parameters {important}

**Required Parameters:**
- `name` (string): Field identifier
- `label` (string): Field label
- `ElementProps.options` (array): Options array with value/label objects

**Optional Parameters:**
- `helperText` (string): Guidance text
- `required` (boolean): Validation indicator
- `ElementProps.expandedChecklist` (boolean): Display as checklist vs dropdown
- `ElementProps.exclusiveOptions` (array): Values that clear other selections
- `ElementProps.fullWidth` (boolean): Expand to container width
- `ElementProps.variant` (string): MUI variant styling

**Meta Fields:**
- `annotation.include` (boolean): Enable annotation field
- `uncertainty.include` (boolean): Enable uncertainty field

### MultiSelect-Specific Validation {important}

| Validation Type | Configuration | Behaviour | Critical Note |
|-----------------|---------------|-----------|---------------|
| Required field | `["yup.required"]` | Checks not null/undefined | ⚠️ **Empty array [] PASSES** - not what users expect |
| Minimum selection | `["yup.min", 1, "Select at least one"]` | Enforces minimum items | Use this for "required" behavior, NOT yup.required |
| Maximum selection | `["yup.max", 5, "Maximum 5 selections"]` | Limits selection count | Not enforced during interaction, only on submit |
| Array type | `["yup.array"]` | Ensures array type | Default, always included |
| Specific values | `["yup.array"], ["yup.of", ["yup.oneOf", ["val1", "val2"]]]` | Restricts to subset | Complex syntax for value validation |
| Min and max | `["yup.array"], ["yup.min", 2], ["yup.max", 5]` | Range constraint | Between 2-5 selections required |

**Critical Validation Behavior:**
- **NO ERROR DISPLAY**: Validation runs but messages never appear in UI
- **Empty array gotcha**: `["yup.required"]` considers `[]` as valid (field exists)
- **No proactive enforcement**: Max selection limit not prevented during interaction
- **Silent failures**: Users receive no feedback when validation fails

### MultiSelect-Specific Issues {important}

- **No error message display** - Validation messages configured but never shown to users
- **Performance degradation** - Severe lag with >20 options due to no virtualization
- **CSV export problems** - Options containing commas break CSV parsing
- **No search functionality** - Must manually scroll through all options
- **Touch precision required** - Small touch targets on mobile
- **No keyboard multi-select** - Cannot use Shift/Ctrl for range selection
- **Empty array validation confusion** - Required field passes with no selections

### Field-Specific Troubleshooting {important}

| Issue | Cause | Solution | Prevention |
|-------|-------|----------|------------|
| Required field passes when empty | `["yup.required"]` accepts `[]` | Use `["yup.min", 1]` instead | Always use yup.min for required multi-select |
| Performance lag with 20+ options | All options render immediately | Consider dropdown mode or reduce options | Limit options, test on mobile |
| CSV export breaks | Commas in option values | Remove commas from all option values | Use semicolons or pipes if separation needed |
| Can't see validation errors | No error display implementation | Check form submission prevention | Document validation in helperText |
| Labels not clickable | Wrong mode or version | Ensure expandedChecklist mode enabled | Test both modes |
| Can't select after choosing "None" | Exclusive option behavior | Deselect exclusive option first | Document exclusive behavior |
| No keyboard multi-select | Not implemented | Use Space/Enter on each item | Train users on individual selection |
| Options don't load dynamically | Static vocabularies only | Define all options at design time | Plan vocabulary completely upfront |

### Implementation Examples {comprehensive}

#### Basic Multi-Selection with Validation
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

#### Exclusive Options Pattern
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

#### Dropdown for Long Lists
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

#### Migration from Multiple Checkboxes
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

### JSON Anti-patterns

```json

"validationSchema": [["yup.required"]]


"validationSchema": [["yup.min", 1, "Select at least one"]]


{"value": "pottery, ceramics", "label": "Pottery, ceramics"}


{"value": "pottery and ceramics", "label": "Pottery and ceramics"}


"initialValue": ""


"initialValue": []


"options": [...100_options]


"options": [...15_options]
```

### Common Spec Mappings

**Designer → JSON mappings:**
- Designer "Required" → `required: true` (misleading - use yup.min instead)
- Designer option value/label → Enforces value = label
- Designer "Expanded Checklist" → `expandedChecklist: true`
- Designer "Exclusive" per option → `exclusiveOptions` array

**Conditional logic mappings:**
- Array contains value → `{"operator": "contains", "value": "option1"}`
- Array contains any → `{"operator": "contains-one-of", "value": ["opt1", "opt2"]}`
- Array contains all → `{"operator": "contains-all-of", "value": ["opt1", "opt2"]}`
- Empty array check → `{"operator": "equal", "value": []}`

---

### RadioGroup
<!-- keywords: radio, single, selection, deprecated, broken -->

### RadioGroup Details
**Status**: Production - Known issues with error display and accessibility are on roadmap
**Alternative**: Use Select for all new implementations
**Migration**: See Migration Procedures below

**Quick Reference:**
| Property | Value |
|----------|-------|
| Designer Label | Select one option |
| Component Name | RadioGroup |
| Namespace | faims-custom |
| Type Returned | faims-core::String |
| Error Display | ❌ Red color only, no error messages |
| Mobile Support | ⚠️ Limited (problematic deselection, performance issues) |
| Accessibility | ❌ Critical violations (no ARIA, keyboard issues) |
| Touch Targets | 42px radio buttons (below iOS 44px standard) |
| Performance | 3-7 optimal, 10+ degraded, 20+ unusable |
| Storage | String, no null state after selection |

### Purpose {essential}

The RadioGroup field provides single selection from 2–10 mutually exclusive options through radio button interface, returning `faims-core::String` values. **However, this component suffers from severe limitations that make it unsuitable for production use:** no error message display (only color changes), critical accessibility violations, problematic deselection behavior, and severe performance degradation with >10 options.

**Historical use cases (now deprecated):**
- Condition assessments - Rating heritage fabric condition (use Select instead)
- Binary archaeological decisions - Presence/absence with explicit "Unknown" option (use Checkbox or Select)
- Likert scale responses - Survey questions with 3-7 point scales (use Select instead)
- Material type classification - Quick selection from common materials (use Select)

⚠️ **WARNING**: Due to critical limitations, use Select instead for all production deployments.

### Core Configuration {essential}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "RadioGroup",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "fabric-condition",
    "label": "Fabric Condition",
    "helperText": "Click selected option to deselect (mouse only - accessibility issue)",
    "fullWidth": true,
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
    ["yup.required", "Condition required (message won't show)"],
    ["yup.oneOf", ["excellent","good","fair","poor","na"], "Invalid (won't show)"]
  ],
  "initialValue": "na"
}
```

### Key Features {essential}

- ✅ **Single selection enforcement** - Only one option can be selected
- ✅ **String values returned** - Compatible with text-based conditional logic
- ✅ **Vertical layout** - All options visible simultaneously
- ⚠️ **Toggle deselection (broken)** - Can deselect via mouse/touch but NOT keyboard
- ⚠️ **Performance issues** - Severe lag with >10 options due to markdown parsing
- ❌ **No error message display** - Critical UX failure, only red color shown
- ❌ **No ARIA attributes** - Fails WCAG 2.1 Level A requirements
- ❌ **No Designer preview** - Cannot see appearance before deployment
- 🐛 **Keyboard deselection broken** - Accessibility barrier
- 🐛 **No empty state detection** - Conditional logic cannot check for unselected

### Configuration Parameters {important}

**Required Parameters:**
- `name` (string): Field identifier
- `label` (string): Field label
- `ElementProps.options` (array): Options with value/label pairs

**Optional Parameters:**
- `helperText` (string): Guidance text
- `required` (boolean): Validation indicator (misleading due to no error display)
- `fullWidth` (boolean): Expand to container width (JSON only)
- `disabled` (boolean): Disable entire RadioGroup (JSON only)
- `FormLabelProps` (object): MUI label customization (JSON only)
- `FormHelperTextProps` (object): MUI helper customization (JSON only)

### RadioGroup-Specific Validation {important}

| Validation Type | Configuration | Error Message | Actual Display | Designer Support |
|-----------------|---------------|---------------|----------------|------------------|
| Required field | `["yup.required", "Selection required"]` | "Selection required" | ❌ Red color only | ✅ Checkbox |
| String type | `["yup.string"]` | Automatic | ❌ No message | ✅ Default |
| One of values | `["yup.oneOf", ["yes","no"], "Invalid"]` | "Invalid" | ❌ No message | ❌ JSON only |
| Not null | `["yup.notOneOf", [null], "Must select"]` | "Must select" | ❌ No message | ❌ JSON only |
| Conditional required | Not supported | - | - | ❌ Not possible |

**⚠️ MAJOR BUG**: RadioGroup displays NO error messages - only shows red color when invalid. Users receive no text feedback about validation failures.

### RadioGroup-Specific Issues {important}

- **No error message display** - Critical UX failure, users get no validation feedback
- **Keyboard deselection broken** - Can deselect with mouse/touch but NOT keyboard (accessibility barrier)
- **No ARIA attributes** - Missing aria-required, aria-invalid, aria-describedby
- **Performance degradation** - Severe lag >10 options due to markdown parsing overhead
- **No empty state detection** - Cannot use isEmpty operator in conditional logic
- **No Designer preview** - Cannot see field appearance before deployment
- **Toggle deselection confusion** - Users don't know clicking selected option clears it
- **Export shows values not labels** - CSV exports technical values requiring lookup

### Field-Specific Troubleshooting {important}

| Issue | Cause | Solution | Prevention |
|-------|-------|----------|------------|
| No error messages shown | Not implemented | Add helper text explaining requirements | Use Select instead |
| Cannot deselect via keyboard | Bug in implementation | Use Select instead | Avoid RadioGroup |
| Screen reader incompatible | No ARIA attributes | Cannot fix - use Select | Accessibility audit |
| Performance >20 options | Markdown parsing overhead | Use Select for long lists | Limit options |
| Cannot detect empty state | No isEmpty operator | Add "None" option | Design around limitation |
| Exports missing labels | By design | Post-process with config | Use Select (value=label) |
| Required field confusion | Silent validation failure | Document in helperText | Use Select with visible errors |

### Implementation Examples {comprehensive}

#### Heritage Condition Assessment (Deprecated Pattern)
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
        {"value": "na", "label": "Not Applicable"}
      ]
    }
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Condition required (message won't show)"],
    ["yup.oneOf", ["excellent","good","fair","poor","na"], "Invalid (won't show)"]
  ],
  "initialValue": "na"
}
```

#### Migration to Select (Recommended)
```json
{
  "component-namespace": "faims-custom",
  "component-name": "Select",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "fabric-condition",
    "label": "Fabric Condition",
    "helperText": "Select the current condition",
    "fullWidth": true,
    "required": true,
    "ElementProps": {
      "options": [
        {"value": "", "label": "-- Select Condition --"},
        {"value": "Excellent", "label": "Excellent"},
        {"value": "Good", "label": "Good"},
        {"value": "Fair", "label": "Fair"},
        {"value": "Poor", "label": "Poor"},
        {"value": "Not Applicable", "label": "Not Applicable"}
      ]
    }
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Condition selection required"]
  ],
  "initialValue": ""
}
```

#### Workflow Branching with Workarounds
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
    ["yup.notOneOf", [null], "Must select"]
  ],
  "initialValue": "rapid"
}
```

#### Binary Choice Alternative (Use Select Instead)
```json
{
  "component-namespace": "faims-custom",
  "component-name": "RadioGroup",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "has-features",
    "label": "Heritage Features Present",
    "helperText": "⚠️ DEPRECATED: Use Select or Checkbox instead",
    "ElementProps": {
      "options": [
        {"value": "yes", "label": "Yes"},
        {"value": "no", "label": "No"}
      ]
    }
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Required (but won't display)"]
  ],
  "initialValue": ""
}
```
**Better Alternative**: Use Checkbox for true boolean logic:
```json
{
  "component-name": "Checkbox",
  "type-returned": "faims-core::Bool",
  "component-parameters": {
    "label": "Heritage Features Present"
  }
}
```

### JSON Anti-patterns

```json

"validationSchema": [["yup.required", "This message won't show"]]


"helperText": "Click again to deselect"





"options": [...20_options]


"component-name": "Select"
"ElementProps": {
  "options": [
    {"value": "", "label": "-- Select --"},
    ...options
  ]
}
```

### Common Spec Mappings

**Designer → JSON mappings:**
- Designer "Required" → `required: true` + `["yup.required"]` (won't display error)
- Designer option values → Exported as technical values (not labels)
- Designer drag-drop → Option order in JSON array
- Designer no preview → Must deploy to test

**Migration mappings (RadioGroup → Select):**
- Add empty option: `{"value": "", "label": "-- Select --"}`
- Change validation messages (they'll actually display)
- Update conditional logic if needed
- Test error display works

---

### Select (Select Field in Designer) {essential}
<!-- keywords: dropdown, single, selection, standard -->

**Quick Reference:**
| Property | Value |
|----------|-------|
| Designer Label | Select Field |
| Component Name | Select |
| Namespace | faims-custom |
| Type Returned | faims-core::String |
| Error Display | ❌ No error messages shown |
| Mobile Support | ✅ Good (consistent Material-UI across platforms) |
| Accessibility | ⚠️ Limited (basic keyboard support, missing ARIA) |
| Touch Targets | Native picker on mobile, dropdown on desktop |
| Performance | 50 options acceptable, 100+ degraded, 200+ unusable |
| Storage | String, empty string for no selection |

### Purpose {essential}

The Select field provides single-choice selection from a dropdown list, offering space-efficient presentation of controlled vocabularies through Material-UI's consistent interface across all platforms. This field type returns `faims-core::String` values and serves as the standard solution for single selection from more than 5-7 options, where RadioGroup would consume excessive screen space. While the component lacks error message display and accessibility attributes, it delivers reliable structured data collection with human-readable exports.

**When to use:**
- Taxonomic classification - Species lists, artefact types, material categories (10-50 options)
- Site or context types - Archaeological periods, depositional environments, feature types
- Standardized descriptions - Condition states, preservation levels, completeness percentages
- Administrative categories - Project phases, team members, institutional codes
- Geographical regions - Countries, states, survey areas, management zones
- Equipment or methods - Instrument types, sampling strategies, analysis techniques

### Core Configuration {essential}

```json
{
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
        {"value": "", "label": "-- Select Site Type --"},
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
  "initialValue": ""
}
```

### Key Features {essential}

- ✅ **Space-efficient display** - Dropdown conserves screen real estate
- ✅ **Consistent cross-platform** - Same Material-UI interface on all devices
- ✅ **Human-readable exports** - Designer enforces value = label for interpretability
- ✅ **Keyboard navigation** - Arrow keys, type-ahead, Enter/Escape support
- ✅ **Standard selection flow** - Familiar dropdown interaction pattern
- ⚠️ **Limited touch targets** - 48px MenuItems meet minimum but could be larger
- ⚠️ **No search functionality** - Type-ahead limited to single character
- ❌ **No error message display** - Validation runs but errors not shown to users
- ❌ **No clear button** - Cannot deselect without choosing empty option
- ❌ **No ARIA attributes** - Missing accessibility support

### Configuration Parameters {important}

**Required Parameters:**
- `name` (string): Field identifier
- `ElementProps.options` (array): Options with value/label objects

**Optional Parameters:**
- `label` (string): Field label
- `helperText` (string): Guidance text
- `fullWidth` (boolean): Expand to container width
- `variant` (string): MUI variant ("outlined", "filled", "standard")
- `required` (boolean): Validation indicator
- `select` (boolean): Internal property (automatically true)
- `disabled` (boolean): Disable field

**JSON-Only Properties:**
- Different values vs labels (not recommended - breaks Designer advantage)
- Complex validation chains beyond basic required
- SelectProps for dropdown customization

### Select-Specific Validation {important}

| Validation Type | Configuration | Behaviour | User Experience |
|-----------------|---------------|-----------|-----------------|
| Required | `["yup.required"]` | Blocks submission if empty | Silent failure - no visual feedback |
| String Type | `["yup.string"]` | Always passes | Automatic - enforced by component |
| Min Length | `["yup.minLength", 3]` | Validates selection length | No error display |
| Pattern Match | `["yup.matches", "pattern"]` | Validates against regex | No error display |
| Custom Message | `["yup.required", "Please select"]` | Custom error text | Not displayed to user |

**Validation Behavior:**
- **On change**: Validation runs but errors not displayed
- **On blur**: No validation triggered
- **On submit**: Final validation blocks submission silently
- **In practice**: UI prevents invalid selections, making most validation redundant
- **Note**: Option membership validation not implemented (values not checked against options array)

### Select-Specific Issues {important}

- **No error message display** - Validation messages configured but never shown to users
- **No clear/deselect capability** - Must include empty option if null state needed
- **Limited search** - Type-ahead only jumps to first character, resets after ~1 second
- **No virtualization** - All options render immediately, performance degrades >50 options
- **No native mobile pickers** - Uses Material-UI dropdown instead of platform controls
- **Helper text position** - Displays above field (non-standard Material-UI position)
- **No field type conversion** - Cannot convert from RadioGroup without deletion/recreation

### Field-Specific Troubleshooting {important}

| Issue | Symptoms | Cause | Resolution |
|-------|----------|-------|------------|
| No error messages | Required field fails silently | Component lacks error display | Train users on required fields; form structure indicates requirements |
| Slow dropdown | Lag when opening with many options | No virtualization for large lists | Limit to <50 options; consider categories or different field type |
| Can't deselect | No way to clear selection | No built-in clear button | Include empty option: `{"value": "", "label": "-- None --"}` |
| Preview missing | Can't test in Designer | Feature not implemented | Save and deploy to test environment; preview on roadmap |
| Can't convert type | Must delete RadioGroup to create Select | No field type conversion | Note options, delete field, recreate as Select; conversion planned |
| Touch precision | Hard to select on mobile | Default touch targets | Ensure clean/dry hands; consider RadioGroup for frequent selections |
| Data shows codes | CSV has "001" not "Archaeological Site" | Manual JSON editing with different value/label | Use Designer; ensure value = label |

### Implementation Examples {comprehensive}

#### Site Classification (Heritage Context)
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

#### Condition Assessment with Null Option
```json
{
  "condition-state": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Condition",
      "name": "condition-state",
      "helperText": "Assess current preservation state",
      "fullWidth": true,
      "ElementProps": {
        "options": [
          {"value": "", "label": "-- Not assessed --"},
          {"value": "Excellent", "label": "Excellent"},
          {"value": "Good", "label": "Good"},
          {"value": "Fair", "label": "Fair"},
          {"value": "Poor", "label": "Poor"},
          {"value": "Destroyed", "label": "Destroyed"}
        ]
      }
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "",
    "meta": {
      "annotation": {"include": true, "label": "condition notes"}
    }
  }
}
```

#### Triggering Conditional Fields
```json
{
  "material-type": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Material Type",
      "name": "material-type",
      "fullWidth": true,
      "ElementProps": {
        "options": [
          {"value": "Ceramic", "label": "Ceramic"},
          {"value": "Glass", "label": "Glass"},
          {"value": "Metal", "label": "Metal"},
          {"value": "Other", "label": "Other"}
        ]
      }
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  },
  "other-material": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Specify Other Material",
      "name": "other-material"
    },
    "condition": {
      "field": "material-type",
      "operator": "equal",
      "value": "Other"
    }
  }
}
```

### JSON Anti-patterns

```json

{"value": "001", "label": "Archaeological Site"}


{"value": "Archaeological Site", "label": "Archaeological Site"}


"validationSchema": [["yup.required", "This message won't show"]]


"options": [
  {"value": "option1", "label": "Option 1"}

]


"options": [
  {"value": "", "label": "-- Select --"},
  {"value": "option1", "label": "Option 1"}
]
```

### Common Spec Mappings

**Designer → JSON mappings:**
- Designer options → Automatic value = label enforcement
- Designer "Required" → `required: true` (no visual validation feedback)
- Designer Label → `label` property
- Designer Helper Text → `helperText` property

**Conditional logic mappings:**
- String equality → `{"operator": "equal", "value": "exact_match"}`
- Empty check → `{"operator": "equal", "value": ""}`
- Cannot use `isEmpty`, `contains`, or `notEqual` operators

**Migration from RadioGroup:**
- Add empty option for null state capability
- Remove toggle deselection behavior
- Same string-based conditional logic works
- Better error handling (though still no display)

---

### AdvancedSelect (Select Field (Hierarchical) in Designer) {essential} 🔴 BETA
<!-- keywords: hierarchical, tree, taxonomy, beta, broken -->

⚠️ **BETA COMPONENT**
**Status**: Beta - not recommended for production use
**Issues**: Cannot clear selection, requires JSON editing for hierarchy, mobile layouts broken
**Alternative**: Use cascading Select fields or Select with prefixed options

**Quick Reference:**
| Property | Value |
|----------|-------|
| Designer Label | Select Field (Hierarchical) |
| Component Name | AdvancedSelect |
| Namespace | faims-custom |
| Type Returned | faims-core::String |
| Error Display | ❌ No error messages shown |
| Mobile Support | ❌ Broken (fixed width causes scrolling, small touch targets) |
| Accessibility | ❌ Poor (limited keyboard support, no ARIA) |
| Touch Targets | Fixed 500px width causes mobile scrolling |
| Performance | 50 nodes optimal, 100+ degraded, 500+ unusable |
| Storage | String path with " > " delimiter |

### Purpose {essential}

The AdvancedSelect field provides hierarchical tree navigation for selecting values from nested vocabularies, returning `faims-core::String` values representing either full paths or leaf nodes. **Currently in beta status** due to incomplete Designer integration, performance limitations, and multiple critical bugs. This field renders entire tree structures without optimization, making it unsuitable for large datasets or mobile deployment.

**Intended use cases (when stable):**
- Biological taxonomic classification (kingdom → phylum → class → order)
- Archaeological typologies (material → technique → form → decoration)
- Geographic hierarchies (continent → country → region → site)
- Organizational structures (department → division → team → role)
- Stratigraphic sequences (period → phase → context → feature)

**Critical limitations**: No error display, no clear/deselect capability, no search functionality, severe performance degradation beyond 100 nodes, requires JSON hand-editing, breaks mobile layouts.

### Core Configuration {essential}

```json
{
  "component-namespace": "faims-custom",
  "component-name": "AdvancedSelect",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "species-classification",
    "label": "Species Classification",
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
                }
              ]
            }
          ]
        }
      ]
    }
  },
  "validationSchema": [["yup.string"], ["yup.required", "Classification required"]],
  "initialValue": ""
}
```

### Key Features {essential}

- ✅ **Hierarchical navigation** - Tree structure with expand/collapse
- ✅ **Full path or leaf storage** - Configurable via valuetype parameter
- ✅ **Any node selectable** - Parent and child nodes can be selected
- ✅ **Conditional logic support** - Standard string operators work
- ⚠️ **Beta status** - Incomplete implementation, multiple critical bugs
- ⚠️ **JSON editing required** - Hierarchy structure must be hand-coded
- ⚠️ **Performance issues** - Severe degradation >100 nodes
- ❌ **No clear/deselect** - Cannot remove selection once made
- ❌ **No error display** - Validation messages never shown
- ❌ **Mobile broken** - Fixed width causes horizontal scrolling
- 🐛 **No search capability** - Must manually navigate entire hierarchy
- 🐛 **Lost expansion state** - Tree collapses when navigating away

### Configuration Parameters {important}

**Required Parameters:**
- `name` (string): Field identifier
- `label` (string): Field label
- `ElementProps.optiontree` (array): Hierarchical tree structure

**Optional Parameters:**
- `helperText` (string): Guidance text
- `required` (boolean): Validation indicator (error won't display)
- `valuetype` (string): "full" (default) stores complete path, "child" stores node name only
- `disabled` (boolean): Disable entire tree (no node-level control)

**Node Structure:**
```typescript
interface TreeNode {
  name: string;        // Required: Used for path construction
  label?: string;      // Optional: Display override
  children?: TreeNode[]; // Optional: Child nodes
}
```

### AdvancedSelect-Specific Validation {important}

| Rule | Configuration | Effect | Error Message | Display |
|------|---------------|--------|---------------|---------|
| required | `["yup.required"]` | Blocks submission if empty | "This field is required" | **NEVER SHOWN** |
| oneOf | `["yup.oneOf", ["val1", "val2"]]` | Restricts to specific values | "Must be one of the following values" | **NEVER SHOWN** |
| matches | `["yup.matches", "pattern"]` | Pattern matching on stored value | "Must match pattern" | **NEVER SHOWN** |

**Critical Validation Issues:**
- **No error display**: Validation errors never shown to users (same as other choice fields)
- **Form blocking**: Invalid fields prevent submission but give no feedback
- **Required paradox**: Required validation fails silently, confusing users
- **Clear issue**: Cannot clear selection to fix validation errors

### AdvancedSelect-Specific Issues {important}

- **Cannot clear selection** - No UI mechanism to deselect once a value is chosen
- **JSON editing required** - Hierarchy structure must be manually coded (Designer limitation)
- **Mobile layouts broken** - Fixed 500px width causes horizontal scrolling on phones
- **Performance degradation** - Severe lag >100 nodes, no virtualization
- **No search functionality** - Must manually expand and navigate entire tree
- **Touch targets too small** - 24px chevron icons difficult to tap accurately
- **Lost expansion state** - Tree collapses when navigating away from field
- **No Designer preview** - Cannot see tree structure before deployment
- **No validation against tree** - Can store values not in defined hierarchy

### Field-Specific Troubleshooting {important}

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

### Implementation Examples {comprehensive}

#### Biological Taxonomy (Full Path Storage)
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
      ["yup.required", "Species classification required"]
    ],
    "initialValue": "",
    "meta": {
      "annotation": {"include": true, "label": "Identification notes"}
    }
  }
}
```
**Behavior**: Stores full path like "Animalia > Chordata > Mammalia > Primates > Hominidae > Homo > Homo sapiens". No error display despite required validation.

#### Archaeological Context Hierarchy (Child Storage)
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
**Behavior**: With valuetype: "child", stores only selected node like "Context 002-A" without path.

#### Geographic Hierarchy with Clear Workaround
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

### JSON Anti-patterns

```json

"helperText": "Click to deselect"





"optiontree": [...500_nodes]


"validationSchema": [["yup.required", "Won't display"]]


"name": "Level > Sublevel"


"component-name": "Select",
"ElementProps": {
  "options": [
    {"value": "Kingdom: Animalia", "label": "Kingdom: Animalia"},
    {"value": "Phylum: Chordata", "label": "Phylum: Chordata"}
  ]
}
```

### Common Spec Mappings

**Designer → JSON mappings:**
- Designer basic properties → Limited subset (label, helperText, valuetype)
- Designer hierarchy editing → **NOT AVAILABLE** (must edit JSON)
- Designer preview → **NOT AVAILABLE** (must deploy to test)

**Conditional logic mappings:**
- Full path matching → `{"operator": "equal", "value": "Level1 > Level2 > Level3"}`
- Child name matching → `{"operator": "equal", "value": "Level3"}` (with valuetype: "child")
- Exact string match required → No partial path or wildcard support

**Migration alternatives:**
- **To cascading Select fields** → Split hierarchy levels into separate Select fields
- **To prefixed Select options** → Flatten hierarchy with "Kingdom: Animalia", "Phylum: Chordata" format
- **To multiple fields** → Use separate fields for each classification level

---

## Troubleshooting Guide {important}

### Error Message Reference {important}

| Error Message | Field(s) Affected | Cause | Quick Fix |
|---------------|-------------------|-------|-----------|
| "Component Checkbox not found" | Checkbox | Wrong namespace | Use `faims-custom` not `formik-material-ui` |
| "Component RadioGroup not found" | RadioGroup | Wrong namespace | Use `faims-custom` not `formik-material-ui` |
| "Cannot read property 'map' of undefined" | MultiSelect, Select | Missing options array | Ensure `ElementProps.options` is defined |
| "Invalid prop 'value' of type 'string'" | MultiSelect | Wrong data type | MultiSelect expects array, not string |
| "Required field" (not showing) | RadioGroup | Component limitation | RadioGroup cannot display errors - use Select |
| "options.map is not a function" | All selection fields | Options not an array | Ensure options is array of objects |

### Quick Reference Matrix {important}

| Feature | Checkbox | MultiSelect | RadioGroup | Select | AdvancedSelect |
|---------|----------|-------------|------------|--------|----------------|
| Error Display | ✅ Full | ❌ None | ❌ None | ✅ Full | ⚠️ Partial |
| Mobile Support | ✅ Good | ✅ Good | ✅ Good | ✅ Good | ❌ Poor |
| Can Deselect | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes | ❌ No |
| Accessibility | ❌ Poor | ⚠️ Basic | ⚠️ Basic | ✅ Good | ❌ Poor |
| Designer Config | ✅ Full | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial | ❌ None |

### Critical Issues Table {important}

| Issue | Field(s) | Severity | Impact | Workaround |
|-------|----------|----------|--------|------------|
| No error display | RadioGroup, MultiSelect | 🔴 High | Users don't see validation | Use Select or add helperText |
| Cannot clear selection | RadioGroup, AdvancedSelect | 🔴 High | Data correction impossible | Use Select with empty option |
| Label not clickable | Checkbox | 🟡 Medium | Poor UX on mobile | Train users to click checkbox |
| Options require JSON | All except Checkbox | 🟡 Medium | Designer limitation | Edit JSON directly |
| Empty array passes required | MultiSelect | 🟡 Medium | Invalid data saved | Use yup.min(1) validation |

### Common Problems Table {important}

| Problem | Symptoms | Fields Affected | Solution |
|---------|----------|-----------------|----------|
| Validation not showing | Form submits with invalid data | RadioGroup, MultiSelect | Switch to Select or Checkbox |
| Cannot remove selection | Once selected, stuck | RadioGroup, AdvancedSelect | Add empty option or use Select |
| Options not appearing | Dropdown empty | All selection fields | Check options array format |
| Wrong component error | Component not found | All | Check namespace is faims-custom |
| Data type mismatch | Values not saving | MultiSelect | Ensure array type for MultiSelect |

### Detailed Issue Matrix {important}

| Component | Issue Type | Platform | Frequency | User Impact | Dev Impact |
|-----------|------------|----------|-----------|-------------|------------|
| Checkbox | Label click | All | Always | Confusion | Training needed |
| MultiSelect | No errors | All | Always | Silent failure | Data validation issues |
| RadioGroup | No errors | All | Always | Silent failure | Should migrate to Select |
| RadioGroup | Can't deselect | All | Always | Data stuck | Add empty option |
| AdvancedSelect | Can't clear | All | Always | Data stuck | Use alternative |
| AdvancedSelect | No Designer | All | Always | JSON only | Manual config |

### Quick Fixes Table {important}

| Issue | Quick Fix | Permanent Solution |
|-------|-----------|-------------------|
| Component not found | Change namespace to `faims-custom` | Update all components |
| No error display | Add custom helperText | Migrate to Select |
| Cannot deselect | Add empty option `{"label": "None", "value": ""}` | Use Select component |
| Validation not working | Add yup validation schema | Test validation chain |
| Options not showing | Check options array format | Validate JSON structure |

### Complete Error Reference {comprehensive}

#### Component Loading Errors
- **"Component [name] not found"**: Wrong namespace, should be `faims-custom`
- **"Cannot read property 'component-name'"**: Missing component-name in JSON
- **"Invalid component configuration"**: Malformed JSON structure

#### Validation Errors (When Supported)
- **"Required field"**: Only shows in Checkbox and Select
- **Silent validation failure**: RadioGroup and MultiSelect don't display errors
- **"Must accept terms"**: Checkbox with yup.oneOf([true]) validation

#### Data Type Errors
- **"Expected array, got string"**: MultiSelect value must be array
- **"Expected string, got object"**: Select value must be string
- **"Expected boolean"**: Checkbox value must be true/false

### Debug Checklists {comprehensive}

#### General Field Checklist {comprehensive}
- [ ] Component namespace is `faims-custom`
- [ ] Component name matches exactly (case-sensitive)
- [ ] Options array is properly formatted
- [ ] Type-returned matches expected data type
- [ ] Validation schema matches field type
- [ ] Initial value matches field type
- [ ] Field name is unique in form
- [ ] No circular dependencies in conditionals

#### Field-Specific Checks {comprehensive}

**Checkbox Checks:**
- [ ] Using `faims-core::Bool` type
- [ ] Initial value is boolean (not string)
- [ ] For "must accept": using yup.oneOf([true])
- [ ] Not expecting label to be clickable

**MultiSelect Checks:**
- [ ] Using `faims-core::Array` type
- [ ] Initial value is array (even if empty)
- [ ] Options array has label/value objects
- [ ] Using yup.min(1) for required validation
- [ ] Not expecting error messages to display

**RadioGroup Checks:**
- [ ] Consider migrating to Select
- [ ] Has empty option if deselection needed
- [ ] Not relying on error display
- [ ] Using helperText for validation feedback

**Select Checks:**
- [ ] Using `faims-core::String` type
- [ ] Has empty option for optional fields
- [ ] Options array properly formatted
- [ ] Label positioning correct

**AdvancedSelect Checks:**
- [ ] Consider using alternatives
- [ ] JSON configuration complete
- [ ] Not using in production
- [ ] Has fallback for mobile

### Field-Specific Issues {important}

See Individual Field Reference section for detailed field-specific issues.

### Emergency Rollback Procedures {important}

#### When RadioGroup Fails in Production
1. Export all data immediately
2. Replace RadioGroup with Select in JSON
3. Map existing values (no data loss for single selection)
4. Test validation displays correctly
5. Redeploy

#### When MultiSelect Loses Data
1. Check if empty arrays were saved
2. Export data with timestamps
3. Add yup.min(1) validation
4. Review all submissions since deployment
5. Manually correct empty submissions

#### When AdvancedSelect Breaks
1. Screenshot current selections
2. Export all hierarchical data
3. Replace with Select using prefixed labels
4. Flatten hierarchy into single level
5. Update training materials

## JSON Examples {comprehensive}

### Example 1: Basic Single Select Field
```json
{
  "site-type": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "site-type",
      "id": "site-type",
      "label": "Site Type",
      "helperText": "Select the primary site classification",
      "required": true,
      "options": [
        {"label": "Residential", "value": "residential"},
        {"label": "Industrial", "value": "industrial"},
        {"label": "Religious", "value": "religious"},
        {"label": "Agricultural", "value": "agricultural"},
        {"label": "Military", "value": "military"}
      ]
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Site type is required"]
    ],
    "initialValue": ""
  }
}
```

### Example 2: MultiSelect with Validation
```json
{
  "artifact-materials": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "artifact-materials",
      "id": "artifact-materials",
      "label": "Artifact Materials",
      "helperText": "Select all materials present",
      "required": true,
      "options": [
        {"label": "Ceramic", "value": "ceramic"},
        {"label": "Glass", "value": "glass"},
        {"label": "Metal", "value": "metal"},
        {"label": "Stone", "value": "stone"},
        {"label": "Bone", "value": "bone"},
        {"label": "Wood", "value": "wood"},
        {"label": "Textile", "value": "textile"}
      ]
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "Select at least one material"],
      ["yup.max", 3, "Maximum 3 materials"]
    ],
    "initialValue": []
  }
}
```

### Example 3: RadioGroup for Condition Assessment
```json
{
  "condition-assessment": {
    "component-namespace": "faims-custom",
    "component-name": "RadioGroup",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "condition-assessment",
      "id": "condition-assessment",
      "label": "Condition Assessment",
      "helperText": "Overall condition of the artifact",
      "required": true,
      "options": [
        {"label": "Excellent", "value": "excellent"},
        {"label": "Good", "value": "good"},
        {"label": "Fair", "value": "fair"},
        {"label": "Poor", "value": "poor"},
        {"label": "Critical", "value": "critical"}
      ]
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Condition assessment required"]
    ],
    "initialValue": ""
  }
}
```

### Example 4: Checkbox for Terms Acceptance
```json
{
  "data-consent": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "name": "data-consent",
      "id": "data-consent",
      "label": "I consent to data collection and usage",
      "required": true,
      "helperText": "Required for participation"
    },
    "validationSchema": [
      ["yup.bool"],
      ["yup.oneOf", [true], "Consent is required"]
    ],
    "initialValue": false
  }
}
```

### Example 5: Select with Conditional Options
```json
{
  "pottery-form": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "pottery-form",
      "id": "pottery-form",
      "label": "Pottery Form",
      "helperText": "Select vessel form",
      "required": false,
      "options": [
        {"label": "Bowl", "value": "bowl"},
        {"label": "Jar", "value": "jar"},
        {"label": "Plate", "value": "plate"},
        {"label": "Cup", "value": "cup"},
        {"label": "Amphora", "value": "amphora"},
        {"label": "Jug", "value": "jug"}
      ]
    },
    "validationSchema": [
      ["yup.string"]
    ],
    "initialValue": null,
    "condition": {
      "operator": "includes",
      "field": "artifact-materials",
      "value": "ceramic"
    }
  }
}
```

### Example 6: Advanced MultiSelect with Groups
```json
{
  "excavation-tools": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "excavation-tools",
      "id": "excavation-tools",
      "label": "Tools Used",
      "helperText": "Select all tools used in this excavation",
      "options": [
        {"label": "Hand Tools - Trowel", "value": "trowel"},
        {"label": "Hand Tools - Brush", "value": "brush"},
        {"label": "Hand Tools - Pick", "value": "pick"},
        {"label": "Power Tools - Drill", "value": "drill"},
        {"label": "Power Tools - Saw", "value": "saw"},
        {"label": "Measurement - Tape", "value": "tape"},
        {"label": "Measurement - Level", "value": "level"}
      ]
    },
    "validationSchema": [
      ["yup.array"]
    ],
    "initialValue": []
  }
}
```

### Example 7: Select with External Vocabulary
```json
{
  "period-chronology": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "period-chronology",
      "id": "period-chronology",
      "label": "Chronological Period",
      "helperText": "Select from Getty AAT periods",
      "required": true,
      "vocabularyName": "getty-aat-periods",
      "options": []
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Period selection required"]
    ],
    "initialValue": ""
  }
}
```

### Example 8: Boolean Checkbox Array
```json
{
  "field-conditions": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "name": "field-conditions",
      "id": "field-conditions",
      "label": "Hazardous Conditions Present",
      "helperText": "Check if any hazards exist",
      "required": false
    },
    "validationSchema": [
      ["yup.bool"]
    ],
    "initialValue": false,
    "meta": {
      "annotation": {
        "include": true,
        "label": "Describe hazards if present"
      }
    }
  }
}
```

### Example 9: RadioGroup with "Other" Option
```json
{
  "soil-type": {
    "component-namespace": "faims-custom",
    "component-name": "RadioGroup",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "soil-type",
      "id": "soil-type",
      "label": "Soil Type",
      "required": true,
      "options": [
        {"label": "Clay", "value": "clay"},
        {"label": "Sandy", "value": "sandy"},
        {"label": "Loam", "value": "loam"},
        {"label": "Silt", "value": "silt"},
        {"label": "Peat", "value": "peat"},
        {"label": "Other", "value": "other"}
      ]
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Soil type required"]
    ],
    "initialValue": ""
  }
}
```

### Example 10: MultiSelect with Metadata
```json
{
  "conservation-treatments": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "conservation-treatments",
      "id": "conservation-treatments",
      "label": "Conservation Treatments Applied",
      "helperText": "Select all treatments performed",
      "options": [
        {"label": "Cleaning", "value": "cleaning"},
        {"label": "Consolidation", "value": "consolidation"},
        {"label": "Desalination", "value": "desalination"},
        {"label": "Reconstruction", "value": "reconstruction"},
        {"label": "Protective coating", "value": "coating"}
      ]
    },
    "validationSchema": [
      ["yup.array"]
    ],
    "initialValue": [],
    "meta": {
      "uncertainty": {
        "include": true,
        "label": "Treatment effectiveness"
      }
    }
  }
}
```

### Example 11: Select with Default Value
```json
{
  "recording-method": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "recording-method",
      "id": "recording-method",
      "label": "Recording Method",
      "helperText": "How was this feature recorded?",
      "options": [
        {"label": "Photography", "value": "photo"},
        {"label": "Drawing", "value": "drawing"},
        {"label": "3D Scan", "value": "scan3d"},
        {"label": "Video", "value": "video"}
      ]
    },
    "validationSchema": [
      ["yup.string"]
    ],
    "initialValue": "photo"
  }
}
```

### Example 12: Complex Conditional MultiSelect
```json
{
  "metal-types": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "metal-types",
      "id": "metal-types",
      "label": "Metal Types",
      "helperText": "Specify metal composition",
      "required": true,
      "options": [
        {"label": "Iron", "value": "iron"},
        {"label": "Bronze", "value": "bronze"},
        {"label": "Copper", "value": "copper"},
        {"label": "Silver", "value": "silver"},
        {"label": "Gold", "value": "gold"},
        {"label": "Lead", "value": "lead"},
        {"label": "Tin", "value": "tin"}
      ]
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "Select at least one metal type"]
    ],
    "initialValue": [],
    "condition": {
      "operator": "includes",
      "field": "artifact-materials",
      "value": "metal"
    }
  }
}
```

### Example 13: RadioGroup for Priority Level
```json
{
  "conservation-priority": {
    "component-namespace": "faims-custom",
    "component-name": "RadioGroup",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "conservation-priority",
      "id": "conservation-priority",
      "label": "Conservation Priority",
      "helperText": "Urgency of conservation needed",
      "required": true,
      "options": [
        {"label": "Immediate (24 hours)", "value": "immediate"},
        {"label": "High (1 week)", "value": "high"},
        {"label": "Medium (1 month)", "value": "medium"},
        {"label": "Low (6 months)", "value": "low"},
        {"label": "None required", "value": "none"}
      ]
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Priority assessment required"]
    ],
    "initialValue": "medium"
  }
}
```

### Example 14: Select with Numeric Values
```json
{
  "stratigraphic-phase": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::Integer",
    "component-parameters": {
      "name": "stratigraphic-phase",
      "id": "stratigraphic-phase",
      "label": "Stratigraphic Phase",
      "helperText": "Select phase number",
      "required": true,
      "options": [
        {"label": "Phase 1 (Earliest)", "value": 1},
        {"label": "Phase 2", "value": 2},
        {"label": "Phase 3", "value": 3},
        {"label": "Phase 4", "value": 4},
        {"label": "Phase 5 (Latest)", "value": 5}
      ]
    },
    "validationSchema": [
      ["yup.number"],
      ["yup.required", "Phase required"]
    ],
    "initialValue": null
  }
}
```

### Example 15: Checkbox with Advanced Helper
```json
{
  "photography-consent": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "name": "photography-consent",
      "id": "photography-consent",
      "label": "Photography consent obtained",
      "helperText": "Required for sensitive sites",
      "advancedHelperText": "## Photography Consent\n\nConsent must be obtained for:\n- Sacred sites\n- Private property\n- Human remains\n- Restricted areas",
      "required": false
    },
    "validationSchema": [
      ["yup.bool"]
    ],
    "initialValue": false
  }
}
```

### Example 16: MultiSelect with Extended Options
```json
{
  "dating-methods": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "dating-methods",
      "id": "dating-methods",
      "label": "Dating Methods Applied",
      "helperText": "All methods used for this context",
      "options": [
        {"label": "C14 Radiocarbon", "value": "c14"},
        {"label": "Dendrochronology", "value": "dendro"},
        {"label": "Thermoluminescence", "value": "tl"},
        {"label": "Optically Stimulated Luminescence", "value": "osl"},
        {"label": "Archaeomagnetic", "value": "archaeomag"},
        {"label": "Typological", "value": "typological"},
        {"label": "Stratigraphic", "value": "stratigraphic"}
      ]
    },
    "validationSchema": [
      ["yup.array"]
    ],
    "initialValue": ["stratigraphic"]
  }
}
```

### Example 17: RadioGroup with Disabled Option
```json
{
  "access-level": {
    "component-namespace": "faims-custom",
    "component-name": "RadioGroup",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "access-level",
      "id": "access-level",
      "label": "Data Access Level",
      "required": true,
      "options": [
        {"label": "Public", "value": "public"},
        {"label": "Restricted", "value": "restricted"},
        {"label": "Confidential", "value": "confidential"},
        {"label": "Classified", "value": "classified", "disabled": true}
      ]
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Access level required"]
    ],
    "initialValue": "public"
  }
}
```

### Example 18: Select with Dynamic Loading
```json
{
  "related-records": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "related-records",
      "id": "related-records",
      "label": "Related Records",
      "helperText": "Link to existing records",
      "multiple": false,
      "loadOptions": "dynamic",
      "optionsEndpoint": "/api/records/list"
    },
    "validationSchema": [
      ["yup.string"]
    ],
    "initialValue": null
  }
}
```

### Example 19: MultiSelect with Hierarchical Labels
```json
{
  "finds-categories": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "finds-categories",
      "id": "finds-categories",
      "label": "Finds Categories",
      "helperText": "Classify all finds",
      "options": [
        {"label": "Pottery - Prehistoric", "value": "pottery-prehistoric"},
        {"label": "Pottery - Roman", "value": "pottery-roman"},
        {"label": "Pottery - Medieval", "value": "pottery-medieval"},
        {"label": "Metal - Tools", "value": "metal-tools"},
        {"label": "Metal - Weapons", "value": "metal-weapons"},
        {"label": "Metal - Jewelry", "value": "metal-jewelry"},
        {"label": "Organic - Bone", "value": "organic-bone"},
        {"label": "Organic - Wood", "value": "organic-wood"}
      ]
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "Select at least one category"]
    ],
    "initialValue": []
  }
}
```

### Example 20: Complex Nested Conditional Select
```json
{
  "sub-context-type": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "sub-context-type",
      "id": "sub-context-type",
      "label": "Sub-context Type",
      "helperText": "Specific context classification",
      "required": true,
      "options": [
        {"label": "Fill - Occupation", "value": "fill-occupation"},
        {"label": "Fill - Destruction", "value": "fill-destruction"},
        {"label": "Fill - Construction", "value": "fill-construction"},
        {"label": "Cut - Pit", "value": "cut-pit"},
        {"label": "Cut - Posthole", "value": "cut-posthole"},
        {"label": "Cut - Ditch", "value": "cut-ditch"}
      ]
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Sub-context type required"]
    ],
    "initialValue": "",
    "condition": {
      "operator": "or",
      "conditions": [
        {
          "operator": "equal",
          "field": "context-type",
          "value": "fill"
        },
        {
          "operator": "equal",
          "field": "context-type",
          "value": "cut"
        }
      ]
    }
  }
}
```

#### Feature Checklist with Exclusive None
```json
{
  "observed-features": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "name": "observed-features",
      "id": "observed-features",
      "label": "Observed Features",
      "required": true,
      "ElementProps": {
        "options": [
          {"label": "Stone artifacts", "value": "stone"},
          {"label": "Ceramics", "value": "ceramics"},
          {"label": "Bone fragments", "value": "bone"},
          {"label": "Charcoal", "value": "charcoal"},
          {"label": "No features observed", "value": "none", "exclusive": true}
        ],
        "displayType": "expandedChecklist"
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

### RadioGroup Examples {important}

#### Deprecated - Condition Assessment
```json
{
  "condition": {
    "component-namespace": "faims-custom",
    "component-name": "RadioGroup",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "condition",
      "id": "condition",
      "label": "Site Condition",
      "required": true,
      "helperText": "Note: RadioGroup is deprecated - use Select",
      "ElementProps": {
        "options": [
          {"label": "Excellent", "value": "excellent"},
          {"label": "Good", "value": "good"},
          {"label": "Fair", "value": "fair"},
          {"label": "Poor", "value": "poor"},
          {"label": "Not assessed", "value": ""}
        ]
      }
    },
    "initialValue": ""
  }
}
```

### Select Examples {important}

#### Site Type with Empty Option
```json
{
  "site-type": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "site-type",
      "id": "site-type",
      "label": "Site Type",
      "required": false,
      "ElementProps": {
        "options": [
          {"label": "-- Select type --", "value": ""},
          {"label": "Rockshelter", "value": "rockshelter"},
          {"label": "Open camp", "value": "open_camp"},
          {"label": "Quarry", "value": "quarry"},
          {"label": "Rock art", "value": "rock_art"}
        ]
      }
    },
    "initialValue": ""
  }
}
```

### AdvancedSelect Examples {important}

#### Beta - Taxonomic Classification
```json
{
  "taxonomy": {
    "component-namespace": "faims-custom",
    "component-name": "AdvancedSelect",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "taxonomy",
      "id": "taxonomy",
      "label": "Taxonomic Classification (BETA)",
      "helperText": "Warning: Cannot clear once selected",
      "ElementProps": {
        "options": [
          {
            "label": "Animalia",
            "value": "animalia",
            "children": [
              {
                "label": "Chordata",
                "value": "chordata",
                "children": [
                  {"label": "Mammalia", "value": "mammalia"},
                  {"label": "Aves", "value": "aves"}
                ]
              }
            ]
          },
          {
            "label": "Plantae",
            "value": "plantae",
            "children": [
              {"label": "Angiosperms", "value": "angiosperms"},
              {"label": "Gymnosperms", "value": "gymnosperms"}
            ]
          }
        ]
      }
    }
  }
}
```

## Migration Scenarios {comprehensive}

### Migration Decision Tree {comprehensive}

```
Current Field Type?
│
├─ RadioGroup (DEPRECATED)
│  ├─ Single selection needed?
│  │  ├─ YES → Migrate to Select
│  │  │  ├─ Add empty option for deselection
│  │  │  └─ Update validation schemas
│  │  └─ NO → Multiple selection?
│  │     └─ YES → Migrate to MultiSelect
│  │
├─ Multiple Checkboxes
│  ├─ Logically grouped?
│  │  ├─ YES → Migrate to MultiSelect
│  │  │  └─ Use expandedChecklist display
│  │  └─ NO → Keep as separate Checkboxes
│  │
├─ AdvancedSelect (BETA)
│  ├─ Hierarchy essential?
│  │  ├─ YES → Keep but warn users
│  │  └─ NO → Migrate to Select with prefixes
│  │
└─ Text/Number for selection
   └─ Fixed options? → Migrate to Select
```

### Migration Warnings Index

#### Safe Migrations (No Data Loss)
- RadioGroup → Select (single string value preserved)
- Multiple Checkboxes → MultiSelect (combine into array)
- Text field → Select (if values match options)

#### Breaking Changes (Data Loss Risk)
- MultiSelect → Select (array to string - loses multiple selections)
- AdvancedSelect → Select (may lose hierarchical context)
- Select → Checkbox (only if binary true/false mapping possible)

#### Conditional Migrations
- RadioGroup with no empty option → Select with empty option (changes data model)
- Checkbox group → MultiSelect with exclusive options (logic change)

### Critical Implementation Procedures {comprehensive}

#### Procedure A: RadioGroup to Select Migration

1. **Export existing data**
   ```bash
   # Document all current RadioGroup selections
   ```

2. **Update JSON configuration**
   ```json

   "component-name": "RadioGroup"

   "component-name": "Select"
   ```

3. **Add empty option if needed**
   ```json
   {"label": "-- None selected --", "value": ""}
   ```

4. **Test validation display**
   - Verify error messages now appear
   - Check required field behavior

5. **Update user documentation**

#### Procedure B: Multiple Checkboxes to MultiSelect

1. **Map checkbox fields to options**
   ```json

   {"label": "Option 1", "value": "opt1"}
   ```

2. **Configure display type**
   ```json
   "ElementProps": {
     "displayType": "expandedChecklist"
   }
   ```

3. **Migrate data**
   - Combine boolean values into array
   - Map true values to option values

4. **Add validation**
   ```json
   ["yup.min", 1, "Select at least one"]
   ```

### Migration Script Templates {comprehensive}

```javascript
// RadioGroup to Select Migration
function migrateRadioGroupToSelect(fieldConfig) {
  return {
    ...fieldConfig,
    "component-name": "Select",
    "component-parameters": {
      ...fieldConfig["component-parameters"],
      "ElementProps": {
        ...fieldConfig["component-parameters"]["ElementProps"],
        "options": [
          {"label": "-- Select --", "value": ""},
          ...fieldConfig["component-parameters"]["ElementProps"]["options"]
        ]
      }
    }
  };
}

// Multiple Checkboxes to MultiSelect
function migrateCheckboxesToMultiSelect(checkboxFields) {
  const options = checkboxFields.map(field => ({
    label: field["component-parameters"]["label"],
    value: field.name
  }));
  
  return {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "ElementProps": { options }
    }
  };
}
```

### Training Requirements {important}

#### Basic Training (All Users)
- Difference between Select and MultiSelect
- How to deselect in Select (use empty option)
- Why RadioGroup shows no errors
- Checkbox label click limitation

#### Advanced Training (Data Managers)
- JSON configuration for options
- Validation schema setup
- Migration procedures
- Troubleshooting validation issues

### Alternative Approaches {comprehensive}

**Instead of RadioGroup:**
- Use Select with empty option
- Use button group (custom component)
- Use segmented control (custom)

**Instead of AdvancedSelect:**
- Cascading Selects
- Select with prefixed labels ("Parent > Child")
- Search field with filtered Select

**Instead of validation-less MultiSelect:**
- Multiple Checkboxes with validation
- Select with multiple conditional fields
- Custom component with error display

## Best Practices {comprehensive}

### Field-Specific Best Practices

**Checkbox:**
- Always use yup.oneOf([true]) for "must accept"
- Provide clear helperText for requirements
- Don't rely on label being clickable

**MultiSelect:**
- Always use yup.min(1) for required
- Consider expandedChecklist for <15 options
- Document that errors won't display
- Use exclusive options for "None" type selections

**RadioGroup (Deprecated):**
- Don't use in new forms
- Always provide migration path
- Include empty option for deselection

**Select:**
- Always include empty option for optional fields
- Use clear, descriptive labels
- Keep options under 50 for performance

**AdvancedSelect (Beta):**
- Avoid in production
- Document inability to clear
- Provide Select alternative
- Test thoroughly on all platforms

### Implementation Notes {comprehensive}

- Options arrays must be defined in JSON, not fetched dynamically
- All selection fields use the same option format: `{label, value}`
- Validation runs onChange but errors only display in some components
- Mobile platforms may have different selection UIs
- Export always uses the value, not the label

### Cross-References Between Fields {comprehensive}

- **Checkbox vs RadioGroup**: Use Checkbox for true/false, RadioGroup only for legacy
- **Select vs MultiSelect**: Data type is key difference (string vs array)
- **Select vs AdvancedSelect**: Use Select unless hierarchy is essential
- **MultiSelect vs Checkboxes**: Use MultiSelect for grouped options

## Field Quirks Index (2025-08) {comprehensive}

### Common Selection Field Quirks

**QUIRK**: All selection components require faims-custom namespace
**FIX**: Always use `"component-namespace": "faims-custom"`
**VERSION**: Since v3.0

**QUIRK**: Options cannot be dynamically loaded
**FIX**: Predefine all options in JSON
**WORKAROUND**: Use conditional logic to show/hide fields
**VERSION**: Current limitation

### Checkbox
- **QUIRK**: Label text not clickable (only checkbox itself)
- **FIX**: None - browser limitation
- **IMPACT**: Mobile usability issue
- **VERSION**: All versions

### MultiSelect
- **QUIRK**: Empty array passes required validation
- **FIX**: Use yup.min(1) validation
- **VERSION**: Since introduction

- **QUIRK**: No error message display
- **FIX**: None - component limitation
- **WORKAROUND**: Use helperText
- **VERSION**: Current

### RadioGroup
- **QUIRK**: Cannot deselect once selected
- **FIX**: Add empty option
- **VERSION**: All versions

- **QUIRK**: No error display capability
- **FIX**: Migrate to Select
- **VERSION**: Deprecated

### Select
- **QUIRK**: Label can overlap with selection
- **FIX**: Use proper label positioning
- **VERSION**: Material-UI related

### AdvancedSelect
- **QUIRK**: Cannot clear selection
- **FIX**: None - component bug
- **VERSION**: Beta

- **QUIRK**: Not configurable in Designer
- **FIX**: Manual JSON only
- **VERSION**: Current

### Performance Quirks
- **QUIRK**: >100 options slows form
- **FIX**: Limit to 50 options
- **APPLIES**: All selection fields

### Browser-Specific Quirks
- **iOS**: Select may show native picker
- **Android**: MultiSelect may show modal
- **Desktop**: Dropdown behavior varies

## Performance Thresholds Summary {important}

See [Performance Thresholds Reference](performance-thresholds-reference.md) for detailed metrics.

**Quick Reference - Selection Field Limits**:
- Options with markdown: <20 (optimal), >50 (unusable)
- Options without markdown: <50 (optimal), >100 (unusable)  
- RadioGroup: Max 20 options (deprecated for larger lists)
- MultiSelect expanded: Max 15 options (mobile), 25 (desktop)
- AdvancedSelect: Max 50 nodes (beta, poor performance)

## JSON Patterns Cookbook (2025-08) {comprehensive}

### Common Selection Patterns

#### Binary Choice Pattern
```json
{
  "field-name": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "label": "Yes/No Question?"
    },
    "initialValue": false
  }
}
```

#### Single Selection with None Pattern
```json
{
  "field-name": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "ElementProps": {
        "options": [
          {"label": "-- None --", "value": ""},
          {"label": "Option 1", "value": "opt1"}
        ]
      }
    }
  }
}
```

#### Multiple Selection with Exclusive Pattern
```json
{
  "field-name": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "type-returned": "faims-core::Array",
    "component-parameters": {
      "ElementProps": {
        "options": [
          {"label": "Option 1", "value": "opt1"},
          {"label": "None of the above", "value": "none", "exclusive": true}
        ]
      }
    }
  }
}
```

### Checkbox Patterns

#### Must Accept Pattern
```json
{
  "must-accept": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "validationSchema": [
      ["yup.bool"],
      ["yup.oneOf", [true], "Must be checked"]
    ]
  }
}
```

#### Optional Flag Pattern
```json
{
  "optional-flag": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Bool",
    "component-parameters": {
      "required": false
    }
  }
}
```

### MultiSelect Patterns

#### Expanded Checklist Pattern
```json
{
  "checklist": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "component-parameters": {
      "ElementProps": {
        "displayType": "expandedChecklist",
        "options": [...]
      }
    }
  }
}
```

#### Required Multiple Pattern
```json
{
  "required-multi": {
    "component-namespace": "faims-custom",
    "component-name": "MultiSelect",
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "Select at least one"],
      ["yup.max", 5, "Select at most 5"]
    ]
  }
}
```

## JSON Anti-patterns Quick Index {comprehensive}

### Selection Field Anti-patterns

#### ❌ Wrong Namespace
```json

"component-namespace": "formik-material-ui"

"component-namespace": "faims-custom"
```

#### ❌ Dynamic Options
```json

"ElementProps": {
  "optionsUrl": "/api/options"
}

"ElementProps": {
  "options": [...]
}
```

#### ❌ Missing Empty Option
```json

"options": [
  {"label": "Yes", "value": "yes"},
  {"label": "No", "value": "no"}
]

"options": [
  {"label": "-- Select --", "value": ""},
  {"label": "Yes", "value": "yes"},
  {"label": "No", "value": "no"}
]
```

#### ❌ Wrong Data Types
```json

"component-name": "MultiSelect",
"initialValue": ""

"component-name": "MultiSelect",
"initialValue": []
```

## Quick Diagnosis Tables (2025-08) {important}

### Error Display Capability
| Component | Shows Errors | Workaround |
|-----------|--------------|------------|
| Checkbox | ✅ Yes | None needed |
| MultiSelect | ❌ No | Use helperText |
| RadioGroup | ❌ No | Migrate to Select |
| Select | ✅ Yes | None needed |
| AdvancedSelect | ⚠️ Partial | Check console |

### Mobile Compatibility
| Component | iOS | Android | Mobile Web |
|-----------|-----|---------|------------|
| Checkbox | ✅ Good | ✅ Good | ⚠️ Label issue |
| MultiSelect | ✅ Good | ✅ Good | ✅ Good |
| RadioGroup | ✅ Good | ✅ Good | ✅ Good |
| Select | ✅ Native | ✅ Native | ✅ Good |
| AdvancedSelect | ❌ Poor | ❌ Poor | ❌ Poor |

### Deselection Capability
| Component | Can Clear | Method |
|-----------|-----------|--------|
| Checkbox | ✅ Yes | Uncheck |
| MultiSelect | ✅ Yes | Deselect all |
| RadioGroup | ❌ No | Add empty option |
| Select | ✅ Yes | Select empty option |
| AdvancedSelect | ❌ No | Bug - cannot clear |

### Platform Support Matrix
| Platform | Best Choice | Avoid |
|----------|------------|-------|
| iOS | Select, Checkbox | AdvancedSelect |
| Android | Select, MultiSelect | AdvancedSelect |
| Desktop | All except deprecated | RadioGroup, AdvancedSelect |
| Mobile Web | Select, Checkbox | AdvancedSelect |

## Field Interaction Matrix (2025-08) {important}

| Field A | Field B | Interaction Type | Notes |
|---------|---------|------------------|-------|
| Checkbox | Select | Conditional display | Checkbox can show/hide Select |
| MultiSelect | MultiSelect | Exclusive options | One excludes others |
| Select | Select | Cascading | First determines second's options |
| RadioGroup | Any | Deprecated | Should not use |
| AdvancedSelect | Any | Isolation | Too complex for interactions |

### Conditional Patterns
- Checkbox controlling field visibility
- Select determining next Select options (static)
- MultiSelect exclusive options clearing others
- Required based on other field values

## Migration Warnings Index (2025-08) {comprehensive}

### Critical Migration Warnings

⚠️ **RadioGroup Deprecation**
- Timeline: Immediate migration recommended
- Risk: No error display, cannot deselect
- Action: Migrate to Select with empty option

⚠️ **AdvancedSelect Beta Status**
- Timeline: Not production ready
- Risk: Cannot clear, poor mobile support
- Action: Use Select with prefixes

⚠️ **MultiSelect Validation**
- Timeline: Check all existing forms
- Risk: Empty arrays passing required
- Action: Add yup.min(1) validation

### Migration Risk Matrix

| From | To | Risk Level | Data Loss | Complexity |
|------|----|------------|-----------|------------|
| RadioGroup | Select | 🟢 Low | None | Simple |
| Checkboxes | MultiSelect | 🟡 Medium | None | Moderate |
| AdvancedSelect | Select | 🔴 High | Hierarchy | Complex |
| MultiSelect | Select | 🔴 High | Multiple values | Complex |
| Text | Select | 🟢 Low | None | Simple |

## See Also {comprehensive}

- **Text Fields**: For open-ended responses or pattern-validated input
- **Number Fields**: For numeric ranges (use instead of Select with numbers)
- **DateTime Fields**: For temporal selections (not period taxonomies)
- **External Vocabularies**:
  - Getty AAT for controlled terminology
  - Periodo for archaeological/historical periods
  - Heritage Data for regional vocabularies
- **Reference Documents**:
  - [Component Namespace Reference](component-namespace-reference.md) - Namespace troubleshooting
  - [Meta Properties Reference](meta-properties-reference.md) - Annotation/uncertainty setup
  - [Data Export Reference](data-export-reference.md) - CSV array handling issues
  - [Accessibility Reference](accessibility-reference.md) - Touch target problems

---

## Error Message Quick Reference (2025-08) {important}

### Critical Errors (Form Breaking)
| Error | Component | Cause | Fix |
|-------|-----------|-------|-----|
| "Component not found" | All | Wrong namespace | Use faims-custom |
| "Cannot read property" | All | Malformed JSON | Validate JSON |
| "Invalid configuration" | All | Missing required | Check parameters |

### Validation Errors (User Visible - When Supported)
| Message | Component | Trigger | Resolution |
|---------|-----------|---------|------------|
| "Required field" | Checkbox, Select | Empty submission | Make selection |
| "Must accept terms" | Checkbox | false when required | Check the box |
| "Invalid selection" | Select | Value not in options | Select valid option |

### Silent Failures (No User Feedback)
| Issue | Component | Detection | Prevention |
|-------|-----------|-----------|------------|
| Empty array saved | MultiSelect | Check data | Add yup.min(1) |
| No validation shown | RadioGroup | Test submit | Use Select |
| Cannot clear | AdvancedSelect | User reports | Use Select |
| Label not clickable | Checkbox | User confusion | Training |

## Metadata {comprehensive}

### Component Status Summary
| Component | Status | Production Ready | Recommendation |
|-----------|--------|------------------|----------------|
| Checkbox | ✅ Stable | Yes | Use for binary |
| MultiSelect | ⚠️ Limited | Yes with caveats | Add validation |
| RadioGroup | ✅ Production | No | Migrate to Select |
| Select | ✅ Stable | Yes | Preferred choice |
| AdvancedSelect | 🔴 Beta | No | Avoid |

### Documentation Coverage
- Designer usage: 80% (limited by Designer constraints)
- JSON configuration: 100%
- Troubleshooting: 100%
- Migration paths: 100%
- Platform specifics: 90%

### Quality Verification
- [ ] All examples tested
- [ ] Migration procedures verified
- [ ] Error messages documented
- [ ] Platform differences noted
- [ ] Performance thresholds validated

### Platform Versions
- FAIMS3: v3.0+
- Designer: Latest
- Mobile: iOS 14+, Android 10+
- Browsers: Chrome 90+, Safari 14+, Firefox 88+

### Known Limitations Documented
- ✅ RadioGroup no error display
- ✅ AdvancedSelect cannot clear
- ✅ Checkbox label not clickable
- ✅ MultiSelect validation issues
- ✅ Dynamic options not supported

### Critical Warnings Highlighted
- ✅ RadioGroup deprecated
- ✅ AdvancedSelect beta
- ✅ MultiSelect empty array validation
- ✅ Component namespace requirements
- ✅ Platform-specific behaviors

### Revision History
- 2025-08: Complete rewrite with v05 pattern
- 2025-08: Added LLM optimizations
- 2025-08: Enhanced troubleshooting
- 2025-08: Added migration procedures
- 2025-08: Platform-specific documentation- 2025-01: Added concatenation boundaries and navigation

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
- **Previous**: [Text Fields](./text-fields-v05.md) | [#text-input-fields](#text-input-fields)
- **Next**: [Date & Time Fields](./datetime-fields-v05.md) | [#datetime-fields](#datetime-fields)

### Cross-Field Patterns
- **Field Selection**: [Selection Field Guidance](../patterns/field-selection-guide.md#select-fields) | [#field-selection](#field-selection)
- **Validation**: [Selection Validation](../detail-crossfield-docs/validation.md#selection-fields) | [#validation-patterns](#validation-patterns)
- **Conditional Logic**: [Dependent Selects](../detail-crossfield-docs/conditional-logic.md#selection-fields) | [#conditional-logic](#conditional-logic)

### Technical References
- **Designer Limitations**: [Selection Constraints](../reference-docs/designer-limitations-reference.md#selection-fields) | [#designer-limitations](#designer-limitations)
- **Performance**: [Option List Limits](../reference-docs/performance-thresholds-reference.md#selection-fields) | [#performance-thresholds](#performance-thresholds)
- **Accessibility**: [Keyboard Navigation](../reference-docs/accessibility-reference.md#selection-fields) | [#accessibility](#accessibility)

<!-- /concat:references -->
<!-- concat:boundary:end section="selection-fields" -->
