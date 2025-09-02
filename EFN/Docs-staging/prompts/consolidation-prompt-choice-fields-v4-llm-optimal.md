# LLM-Optimized Consolidation Prompt: Choice/Selection Fields (v4)

## Core Directive
Create comprehensive, LLM-optimized documentation that enables efficient notebook generation and field implementation. Extract ALL content from source documents while organizing for optimal machine consumption and human usability.

## Input Documents
1. checkbox.md - Checkbox field documentation
2. multiselect.md - MultiSelect field documentation
3. radiogroup.md - RadioGroup field documentation  
4. select.md - Select field documentation
5. advanced-select.md - AdvancedSelect field documentation

## Target Document: select-choice-fields-v05.md

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
### Security Considerations {important}
#### Input Sanitization {important}
#### Field-Specific Security Issues {important}
#### Security Best Practices {comprehensive}
### Performance Boundaries {important}
#### Form Design Guidelines {important}
#### Content Limits by Context {comprehensive}
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
- ✅ [Positive features from source]
- ⚠️ [Limitations]
- ❌ [Missing features]
- 🐛 [Known bugs]

#### Configuration Parameters {important}
[Complete parameter documentation from source]

#### Checkbox-Specific Validation {important}
[Include validation semantics table]
[Special note about required vs must-be-checked]

#### Checkbox-Specific Issues {important}
[All known issues, especially label click bug]

#### Field-Specific Troubleshooting {important}
| Issue | Cause | Solution | Prevention |
[Complete troubleshooting table]

#### Implementation Examples {comprehensive}
[ALL named examples from source - Terms Acceptance, etc.]

#### JSON Anti-patterns
[All anti-patterns from source]

#### Common Spec Mappings
[Designer patterns to JSON mappings]

### MultiSelect (Select Multiple in Designer) {essential}
<!-- keywords: multiple, selection, checklist, dropdown, array -->
[SAME STRUCTURE as Checkbox]

### RadioGroup (Select one option in Designer) {essential} 🟡 DEPRECATED
<!-- keywords: radio, single, selection, deprecated, broken -->

⚠️ **DEPRECATED COMPONENT**
**Status**: Deprecated due to no error message display
**Alternative**: Use Select for all new implementations
**Migration**: See [Migration Procedures > RadioGroup to Select]

[SAME STRUCTURE but with deprecation warnings prominent]

### Select (Select Field in Designer) {essential}
<!-- keywords: dropdown, single, selection, standard -->
[SAME STRUCTURE]

### AdvancedSelect (Select Field (Hierarchical) in Designer) {essential} 🔴 BETA
<!-- keywords: hierarchical, tree, taxonomy, beta, broken -->

⚠️ **BETA COMPONENT** 
**Status**: Beta - not recommended for production
**Issues**: Cannot clear selection, requires JSON editing, mobile broken
**Alternative**: Use cascading Selects or Select with prefixes

[SAME STRUCTURE with beta warnings prominent]

## Troubleshooting Guide {important}
### Error Message Reference {important}
### Quick Reference Matrix {important}
### Critical Issues Table {important}
### Common Problems Table {important}
### Detailed Issue Matrix {important}
### Quick Fixes Table {important}
### Complete Error Reference {comprehensive}
### Debug Checklists {comprehensive}
#### General Field Checklist {comprehensive}
#### Field-Specific Checks {comprehensive}
### Field-Specific Issues {important}
### Emergency Rollback Procedures {important}

## JSON Examples {comprehensive}
### Checkbox Examples {important}
#### [Named examples from source]
### MultiSelect Examples {important}
#### [Named examples from source]
### RadioGroup Examples {important}
#### [Named examples from source]
### Select Examples {important}
#### [Named examples from source]
### AdvancedSelect Examples {important}
#### [Named examples from source]

## Migration and Best Practices {comprehensive}
### Migration Decision Tree {comprehensive}
### Migration Warnings Index
#### Safe Migrations (No Data Loss)
#### Breaking Changes (Data Loss Risk)
#### Conditional Migrations
### Critical Implementation Procedures {comprehensive}
#### Procedure A: RadioGroup to Select Migration
#### Procedure B: Multiple Checkboxes to MultiSelect
### Migration Script Templates {comprehensive}
### Training Requirements {important}
#### Basic Training (All Users)
#### Advanced Training (Data Managers)
### Alternative Approaches {comprehensive}
### Field-Specific Best Practices {comprehensive}
### Implementation Notes {comprehensive}
### Cross-References Between Fields {comprehensive}

## Field Quirks Index (2025-08) {comprehensive}
### Common Selection Field Quirks
### Checkbox
### MultiSelect  
### RadioGroup
### Select
### AdvancedSelect
### Performance Quirks
### Browser-Specific Quirks

## Performance Thresholds Table (2025-08) {essential}
[Table with optimal/acceptable/degraded/unusable thresholds]

## JSON Patterns Cookbook (2025-08) {comprehensive}
### Common Selection Patterns
### Checkbox Patterns
#### [Pattern name and complete JSON]
### MultiSelect Patterns
#### [Pattern name and complete JSON]
[Continue for all field types]

## JSON Anti-patterns Quick Index {comprehensive}
### Selection Field Anti-patterns
[Consolidated anti-patterns by category]

## Quick Diagnosis Tables (2025-08) {important}
### Error Display Capability
### Mobile Compatibility
### Deselection Capability
### Platform Support Matrix

## Field Interaction Matrix (2025-08) {important}
[Field-to-field interactions and dependencies]

## Migration Warnings Index (2025-08) {comprehensive}
### Critical Migration Warnings
### Migration Risk Matrix

## Error Message Quick Reference (2025-08) {important}
### Critical Errors (Form Breaking)
### Validation Errors (User Visible - When Supported)
### Silent Failures (No User Feedback)

## Metadata {comprehensive}
### Component Status Summary
### Documentation Coverage
### Quality Verification
### Platform Versions
### Known Limitations Documented
### Critical Warnings Highlighted
### Revision History
```

## LLM-OPTIMIZATION REQUIREMENTS

### 1. Quick Reference Box for Each Field
MANDATORY: Start each field with a structured table:
```markdown
**Quick Reference:**
| Property | Value |
|----------|-------|
| Designer Label | [What users see] |
| Component Name | [JSON component] |
| Namespace | [component-namespace] |
| Type Returned | [data type] |
| Error Display | ✅/⚠️/❌ [capability] |
| Mobile Support | ✅/⚠️/❌ [level] |
| Accessibility | ✅/⚠️/❌ [compliance] |
```

### 2. Core Configuration EARLY
Place working JSON example immediately after Purpose, before detailed features. This enables quick copying and modification.

### 3. [affects: Field1, Field2] Notation
In Common Characteristics, show which fields are affected:
```markdown
#### Base Properties [affects: All fields] {important}
#### iOS Behaviors [affects: Checkbox, MultiSelect] {comprehensive}
```

### 4. Status Badges for Special Components
- 🟡 DEPRECATED - For RadioGroup
- 🔴 BETA - For AdvancedSelect
- ✅ PRODUCTION - For stable components

### 5. Example-First Approach
- Core Configuration shows immediate working example
- Implementation Examples include ALL named patterns from source
- Anti-patterns come AFTER positive examples

### 6. Progressive Disclosure Structure
1. Quick Reference - Instant identification
2. Purpose - When to use
3. Core Configuration - How to use (example)
4. Key Features - What it can do
5. Parameters - Detailed configuration
6. Issues/Troubleshooting - Problems and solutions
7. More Examples - Additional patterns
8. Anti-patterns - What to avoid

## COMPREHENSIVE EXTRACTION RULES

### Zero Content Loss
Extract from source documents:
- EVERY technical detail
- EVERY warning, note, tip
- EVERY JSON example (complete)
- EVERY table
- EVERY troubleshooting item
- EVERY implementation example BY NAME
- EVERY quirk and limitation
- EVERY platform-specific behavior
- EVERY validation rule
- EVERY error condition

### Enhancement Patterns

#### For Limitations
Transform bullets into explanations:
```markdown
- **Dynamic options** - All options must be predefined in JSON configuration. Cannot fetch from API, database, or generate based on user input. This limitation exists because fields are statically defined at form load time.
```

#### For Use Cases
Provide specific configurations:
```markdown
**Site Classification**:
- **Site types** → Select with 10-50 controlled vocabulary options (e.g., "Aboriginal scarred tree"). Include empty option "-- Not classified --". Set required validation only if mandatory.
```

#### For Decision Trees
Create comprehensive trees:
```markdown
What type of selection do you need?
│
├─ Boolean/binary state?
│  ├─ YES → Checkbox
│  │  ├─ Returns: faims-core::Boolean
│  │  ├─ Best for: Consent, presence/absence
│  │  └─ ⚠️ Label not clickable (bug)
│  └─ NO → Continue
```

### Visual Consistency
Always use:
- ✅ Full support/Working
- ❌ Not supported/Broken
- ⚠️ Partial/Warning/Limited
- 🔴 Critical/Beta
- 🟡 Deprecated
- 🟢 Recommended
- 🐛 Known bug
- 💡 Tip
- 📝 Note

### Quality Verification
Ensure output includes:
- [ ] Sections in LLM-optimal order
- [ ] Quick Reference box for each field
- [ ] Core Configuration early with working JSON
- [ ] [affects:] notation in Common Characteristics
- [ ] Status badges for deprecated/beta
- [ ] ALL content from source documents
- [ ] Enhanced explanations (not just bullets)
- [ ] Complete decision trees
- [ ] All examples runnable
- [ ] Cross-references preserved

## DO NOT
- Set target line counts
- Compress examples
- Omit minor details
- Skip platform notes
- Simplify technical content
- Combine similar patterns

## OUTPUT
Single markdown file optimized for LLM consumption and notebook generation.