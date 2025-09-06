# LLM-Optimized LOSSLESS Consolidation Prompt: Choice/Selection Fields (v5)

## Core Directive
Create comprehensive, LLM-optimized documentation with COMPLETE LOSSLESS extraction from source documents. The goal is to amalgamate, de-duplicate, and enhance WITHOUT losing ANY content from the source documents. Every technical detail, measurement, example, and note must be preserved.

## Input Documents
1. checkbox.md - Checkbox field documentation
2. multiselect.md - MultiSelect field documentation
3. radiogroup.md - RadioGroup field documentation  
4. select.md - Select field documentation
5. advanced-select.md - AdvancedSelect field documentation

## Target Document: select-choice-fields-v05.md

## CRITICAL EXTRACTION REQUIREMENTS

### LOSSLESS CONTENT PRESERVATION
You MUST extract and preserve:

1. **Every Named Example** - Extract ALL examples with their EXACT titles:
   - Checkbox: "Terms Acceptance", "Optional Enhancement Flag", "Data Quality Indicator", "Migration from RadioGroup"
   - MultiSelect: "Basic Multi-Selection", "Exclusive Options Pattern", "Dropdown for Long Lists", "Migration from Multiple Checkboxes"
   - RadioGroup: "Heritage Condition Assessment", "Binary Choice", "Workflow Branching"
   - Select: "Site Classification", "Condition Assessment with Null Option", "Triggering Conditional Fields"
   - AdvancedSelect: "Biological Taxonomy", "Archaeological Context", "Geographic Location Hierarchy"

2. **Every Technical Specification** including:
   - Exact pixel measurements (e.g., "24×24px icon, 48×48px touch target")
   - Performance thresholds with specific numbers (e.g., "20-30 acceptable, 50+ degraded")
   - Platform-specific behaviors with version numbers
   - Memory usage patterns
   - Rendering pipeline details

3. **Every Table** with ALL columns:
   - Troubleshooting tables MUST include: Issue | Symptoms | Diagnosis | Resolution | Prevention
   - Validation tables MUST include: Operator | Configuration | Behavior | Edge Cases | Notes
   - Performance tables MUST include platform-specific breakdowns

4. **Every Section** from source including:
   - Technical Architecture sections
   - Debug Checklists (complete item lists)
   - Cross-References & Dependencies
   - Migration Procedures with code
   - Data Storage & Export specifications
   - Historical Context sections

5. **Every Platform-Specific Detail**:
   - iOS behaviors with iOS version notes
   - Android behaviors with Android version notes
   - Desktop browser differences (Chrome, Safari, Firefox)
   - Touch target specifications per platform
   - Native vs web component behaviors

## REQUIRED STRUCTURE - LLM-OPTIMIZED ORDER

```markdown
# Selection and Choice Fields

## Overview {essential}
### DESIGNER QUICK GUIDE
### CRITICAL NAMING DISAMBIGUATION  
### Data Capture Fields (1-5)
### Component Status Summary

## Designer Usage Guide {essential}
[MOVED EARLY for practical context]
### What to Select in Designer
### When JSON Enhancement is Required
### Quick Use Case Examples

## Field Selection Guide {essential}
[MOVED EARLY for decision support]
### Quick Decision Tree
### Quick Decision Matrix
### Selection Strategy
### Platform Considerations

## ⚠️ CRITICAL SECURITY VULNERABILITIES {essential}
[Or CRITICAL SELECTION FIELD RISKS - AFTER users know what fields exist]

## What These Fields Cannot Do {important}
### Selection Processing Limitations {important}
### Validation Limitations {important}
### Display Limitations {important}
### Interaction Limitations {important}

## Common Use Cases {important}
### Archaeological and Heritage Recording
### Scientific Data Collection
### Administrative Workflows
### Field Research Scenarios
### Data Entry Patterns

## Designer Component Mapping {essential}
[MOVED EARLIER for reference]
### Designer UI vs JSON Component Names
### Designer Limitations Requiring JSON
### Technical Implementation Note

## Designer Capabilities vs JSON Enhancement {essential}
### What Designer CAN Configure
### What Requires JSON Editing
### Designer vs JSON Workflow
### Designer Limitations {important}

## Component Namespace Errors {important}
### Troubleshooting "Component not found" Errors
### Common Namespace Confusion Points

## Common Characteristics {important}
### Shared Behaviors Across Selection Fields
### Configuration Rules {important}
#### Base Properties [affects: All fields] {important}
### Validation Patterns {important}
#### Standard Validation Rules [affects: All fields] {important}
#### Validation Behavior [affects: specific fields] {important}
#### Validation Timing [affects: All fields] {important}
### Security Considerations {important}
#### Input Sanitization {important}
#### Field-Specific Security Issues {important}
#### Security Best Practices {comprehensive}
### Performance Boundaries {important}
#### Form Design Guidelines {important}
#### Content Limits by Context {comprehensive}
#### Performance Thresholds [affects: specific fields] {important}
### Platform Behaviors {important}
#### Cross-Platform Consistency {important}
#### iOS Behaviors [affects: specific fields] {comprehensive}
#### Android Behaviors [affects: specific fields] {comprehensive}
#### Web/Desktop Behaviors [affects: All fields] {important}
### Shared Limitations {important}
#### Designer Interface Constraints {important}
#### Export Behavior {important}
#### Component Architecture {comprehensive}
#### Accessibility Compliance {important}
#### Testing Guidelines {comprehensive}
### Data Storage and Export {important}
#### Database Storage [affects: All fields] {important}
#### Export Formats [affects: All fields] {important}
#### Null Handling [affects: All fields] {important}

## Individual Field Reference {essential}

### Checkbox (Checkbox in Designer) {essential} 
<!-- keywords: boolean, consent, binary, toggle, checkbox -->

**Quick Reference:**
| Property | Value |
|----------|-------|
| Designer Label | Checkbox |
| Component Name | Checkbox |
| Namespace | faims-custom |
| Type Returned | faims-core::Boolean |
| Error Display | ✅ Full (only field with proper errors) |
| Mobile Support | ✅ Full (label not clickable) |
| Accessibility | ❌ Poor (no ARIA) |
| Touch Targets | 24×24px icon, 48×48px target |
| Performance Limit | 20-30 optimal, 50+ degraded |

#### Purpose {essential}
[Extract from checkbox.md - WHEN and WHY to use]

#### Core Configuration {essential}
```json
{
  // WORKING EXAMPLE from source
  // that can be copied and used immediately
}
```

#### Key Features {essential}
[Extract ALL features with measurements]

#### Technical Architecture {important}
[Extract COMPLETE architecture details including:]
- Material-UI component wrapping
- Formik Field integration
- FieldWrapper label handling
- FormControl error styling
- FormHelperText message display
- Memoization status
- Rendering pipeline

#### Configuration Parameters {important}
[Complete parameter documentation]

#### Platform-Specific Rendering {important}
##### Desktop Rendering
[Include ALL specifications: sizes, positions, animations]
##### iOS Rendering  
[Include touch target sizes, gesture requirements]
##### Android Rendering
[Include Material Design compliance notes]

#### State Transitions {important}
[Complete state diagram with all 4 states]

#### Checkbox-Specific Validation {important}
[Include COMPLETE validation table with ALL columns]

#### Validation Timing Behavior {important}
[Extract timing for: mount, change, blur, submit]

#### Checkbox-Specific Issues {important}
[All known issues with pixel measurements]

#### Field-Specific Troubleshooting {important}
| Issue | Symptoms | Diagnosis | Resolution | Prevention |
[Complete table with ALL columns]

#### Performance Considerations {important}
[Specific thresholds: 20-30 acceptable, 50+ degraded, 100+ unusable]

#### Data Storage and Export {comprehensive}
[Database format, CSV format, JSON format, null handling]

#### Implementation Examples {comprehensive}
[ALL named examples from source]
##### Terms Acceptance
[Complete example with explanation]
##### Optional Enhancement Flag
[Complete example with explanation]
##### Data Quality Indicator
[Complete example with explanation]
##### Migration from RadioGroup
[Complete example with migration notes]

#### Debug Checklist {important}
[Complete checklist from source - ALL items]

#### JSON Anti-patterns
[All anti-patterns from source]

#### Common Spec Mappings
[Designer patterns to JSON mappings]

#### Cross-References and Dependencies {comprehensive}
[All related fields and migration paths]

#### Historical Context {comprehensive}
[Legacy patterns and migration guidance]

### MultiSelect (Select Multiple in Designer) {essential}
<!-- keywords: multiple, selection, checklist, dropdown, array -->
[SAME COMPREHENSIVE STRUCTURE as Checkbox]
[Must include exclusive options interaction flow]
[Must include performance tables by platform]
[Must include ALL 4 named examples]

### RadioGroup (Select one option in Designer) {essential} 🟡 DEPRECATED
<!-- keywords: radio, single, selection, deprecated, broken -->

⚠️ **DEPRECATED COMPONENT**
**Status**: Deprecated due to no error message display
**Alternative**: Use Select for all new implementations
**Migration**: See [Migration Procedures > RadioGroup to Select]
**Accessibility Violations**: [List ALL 7 WCAG violations]

[SAME COMPREHENSIVE STRUCTURE with deprecation context]

### Select (Select Field in Designer) {essential}
<!-- keywords: dropdown, single, selection, standard -->
[Must include Designer advantage documentation]
[Must include native picker behaviors]
[Must include keyboard shortcuts]

### AdvancedSelect (Select Field (Hierarchical) in Designer) {essential} 🔴 BETA
<!-- keywords: hierarchical, tree, taxonomy, beta, broken -->

⚠️ **BETA COMPONENT** 
**Status**: Beta - not recommended for production
**Issues**: Cannot clear selection, requires JSON editing, mobile broken
**Alternative**: Use cascading Selects or Select with prefixes
**Performance Boundaries**: 50 nodes optimal, 500+ unusable
**Mobile Issue**: Fixed 500px width causes horizontal scrolling

[SAME COMPREHENSIVE STRUCTURE with beta warnings]

## Troubleshooting Guide {important}
[Include ALL troubleshooting content with complete tables]

## JSON Examples {comprehensive}
[ALL named examples organized by field]

## Migration and Best Practices {comprehensive}
[Complete migration procedures with code]

## Field Quirks Index (2025-08) {comprehensive}
[ALL quirks with measurements and version notes]

## Performance Thresholds Table (2025-08) {essential}
[Platform-specific tables with exact numbers]

## JSON Patterns Cookbook (2025-08) {comprehensive}
[ALL patterns with complete JSON]

## JSON Anti-patterns Quick Index {comprehensive}
[Consolidated anti-patterns]

## Quick Diagnosis Tables (2025-08) {important}
[Complete diagnostic tables]

## Field Interaction Matrix (2025-08) {important}
[Field relationships and dependencies]

## Migration Warnings Index (2025-08) {comprehensive}
[Complete migration risks]

## Error Message Quick Reference (2025-08) {important}
[ALL error messages with contexts]

## Metadata {comprehensive}
### Component Status Summary
### Documentation Coverage
### Quality Verification
### Platform Versions
### Known Limitations Documented
### Critical Warnings Highlighted
### Revision History
```

## EXTRACTION VERIFICATION CHECKLIST

For EACH field in the source documents, verify:

- [ ] ALL named examples extracted with complete JSON
- [ ] ALL pixel measurements preserved (e.g., 24×24px, 48×48px)
- [ ] ALL performance thresholds with numbers (e.g., 20-30, 50+, 100+)
- [ ] ALL platform behaviors with version notes
- [ ] ALL tables with ALL original columns
- [ ] ALL debug checklist items
- [ ] ALL cross-references to other fields
- [ ] ALL migration procedures with code
- [ ] ALL validation operators and timing
- [ ] ALL error messages and conditions
- [ ] ALL accessibility violations specified
- [ ] ALL keyboard shortcuts documented
- [ ] ALL touch gestures described
- [ ] ALL data storage formats
- [ ] ALL export format details
- [ ] ALL historical context preserved

## ENHANCED EXTRACTION PATTERNS

### For Technical Details
Preserve exact specifications:
```markdown
**Desktop Rendering**:
- Checkbox size: 24×24px icon with 48×48px touch target
- Label position: Above checkbox via FieldWrapper (not connected)
- Error display: Below via FormHelperText (red, 12px font)
- Animation: 300ms transition with ripple effect
- Focus ring: 2px blue outline on keyboard navigation
```

### For Performance Thresholds
Include specific numbers:
```markdown
**Performance Boundaries**:
- **Optimal**: 3-20 options (instant response, <50ms render)
- **Acceptable**: 20-30 options (slight lag, 50-200ms render)  
- **Degraded**: 30-50 options (noticeable lag, 200-500ms render)
- **Unusable**: 50+ options (severe lag, >500ms render)
```

### For Platform Behaviors
Document all differences:
```markdown
**iOS Safari**:
- Gesture requirement: User tap required (not programmable)
- Touch target: 44×44px minimum (Apple HIG)
- Native picker: Uses HTML select dropdown (not custom)
- Zoom behavior: Auto-zooms if font <16px
- Version notes: iOS 14+ required for full support
```

### For Troubleshooting
Complete table structure:
```markdown
| Issue | Symptoms | Diagnosis | Resolution | Prevention |
|-------|----------|-----------|------------|------------|
| Label not clickable | Users tap label, nothing happens | Label not associated with input | Train users to tap checkbox | Cannot fix - Material-UI limitation |
```

### For Examples
Preserve complete context:
```markdown
#### Heritage Site Classification (Recommended Pattern)
**Use Case**: Categorizing archaeological sites with hierarchical taxonomy
**Why This Pattern**: Demonstrates proper null handling and label formatting
```json
{
  // Complete JSON configuration
  // With all properties
  // And explanatory comments
}
```
**Key Points**:
- Empty option for incomplete assessments
- Human-readable labels with codes as values
- Validation allows empty for draft records
```

## QUALITY VERIFICATION

The output MUST:
- [ ] Contain 100% of source content (no omissions)
- [ ] Include all exact measurements and numbers
- [ ] Preserve all technical specifications
- [ ] Include every named example with complete code
- [ ] Maintain all platform-specific details
- [ ] Include all troubleshooting guidance
- [ ] Preserve all cross-references
- [ ] Document all historical context
- [ ] Include all debug checklists
- [ ] Preserve all performance data

## DO NOT

- Summarize or condense technical details
- Omit measurements or specific numbers
- Skip "minor" platform differences
- Combine similar examples
- Simplify troubleshooting tables
- Remove historical context
- Generalize platform behaviors
- Skip debug checklist items
- Omit cross-references
- Simplify validation timing

## OUTPUT

Single markdown file with COMPLETE LOSSLESS extraction of ALL source content, enhanced with cross-references and consistent structure, optimized for LLM consumption and notebook generation.