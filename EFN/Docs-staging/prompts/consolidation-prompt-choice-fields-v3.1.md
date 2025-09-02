# LLM-First Consolidation Prompt: Choice/Selection Fields (v3.1 - Comprehensive)

## Core Directive
Extract and consolidate ALL technical content from source documents into a comprehensive, enhanced reference following the v05 pattern. Focus on COMPLETE knowledge transfer - no content should be lost.

## Input Documents
1. checkbox.md - Checkbox field documentation
2. multiselect.md - MultiSelect field documentation
3. radiogroup.md - RadioGroup field documentation  
4. select.md - Select field documentation
5. advanced-select.md - AdvancedSelect field documentation

## Designer UI to Component Mapping (CRITICAL)
| Designer Label | JSON Component | Namespace | Documentation File |
|---|---|---|---|
| Checkbox | Checkbox | faims-custom | checkbox.md |
| Select Multiple | MultiSelect | faims-custom | multiselect.md |
| Select one option | RadioGroup | faims-custom | radiogroup.md |
| Select Field | Select | faims-custom | select.md |
| Select Field (Hierarchical) | AdvancedSelect | faims-custom | advanced-select.md |

## Target Document: select-choice-fields-v05.md

## REQUIRED DOCUMENT STRUCTURE (EXACT ORDER AND TAGS)

```markdown
# Selection and Choice Fields

## Overview {essential}
### DESIGNER QUICK GUIDE
### CRITICAL NAMING DISAMBIGUATION  
### Data Capture Fields (1-5)
### Component Status Summary

## ⚠️ CRITICAL SECURITY VULNERABILITIES {essential}
[Or CRITICAL SELECTION FIELD RISKS for selection-specific issues]

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

## Field Selection Guide {essential}
### Quick Decision Tree
### Quick Decision Matrix
### Selection Strategy
### Platform Considerations

## Designer Usage Guide {essential}
### What to Select in Designer
### When JSON Enhancement is Required
### Quick Use Case Examples

## Designer Capabilities vs JSON Enhancement {essential}
### What Designer CAN Configure
### What Requires JSON Editing
### Designer vs JSON Workflow
### Designer Limitations {important}

## Designer Component Mapping {essential}
### Designer UI vs JSON Component Names
### Designer Limitations Requiring JSON
### Technical Implementation Note

## Component Selection Decision Tree {important}
### Which Component Should You Use?
### Manual JSON Configuration

## Component Namespace Errors {important}
### Troubleshooting "Component not found" Errors
### Common Namespace Confusion Points

## Common Characteristics {important}
### Shared Behaviors Across Selection Fields
### Security Considerations {important}
#### Input Sanitization {important}
#### Field-Specific Security Issues {important}
#### Security Best Practices {comprehensive}
### Performance Boundaries {important}
#### Form Design Guidelines {important}
#### Content Limits by Context {comprehensive}
### Common Validation Patterns {important}
#### Standard Validation Rules {important}
#### Validation Behavior {important}
### Platform Behaviors {important}
#### Cross-Platform Consistency {important}
#### iOS Behaviors {comprehensive}
#### Android Behaviors {comprehensive}
#### Web/Desktop Behaviors {important}
### Shared Limitations {important}
#### Designer Interface Constraints {important}
#### Export Behavior {important}
#### Component Architecture {comprehensive}
#### Accessibility Compliance {important}
#### Testing Guidelines {comprehensive}

## Individual Field Reference {essential}

### Checkbox {essential}
<!-- keywords: boolean, consent, binary, toggle, checkbox -->
**Designer Label**: Checkbox
**Component Name**: Checkbox
**Namespace**: faims-custom
**Type Returned**: faims-core::Boolean

#### Purpose {essential}
[Extract from checkbox.md]

#### Key Features {essential}
[Extract from checkbox.md]

#### Core Configuration {essential}
```json
[Complete JSON example from source]
```

#### Configuration Parameters {important}
[Extract complete parameter documentation]

#### Checkbox-Specific Validation {important}
[Include validation semantics table]

#### Display and Interaction {important}
[Platform rendering, state transitions, accessibility]

#### Checkbox-Specific Issues {important}
[All known issues and limitations]

#### Field-Specific Troubleshooting {important}
[Troubleshooting table from source]

#### JSON Anti-patterns
[All anti-patterns from source]

#### Common Spec Mappings
[Designer to JSON mappings]

#### Implementation Examples {comprehensive}
[ALL examples from source - Terms Acceptance, Optional Enhancement Flag, etc.]

### MultiSelect {essential}
<!-- keywords: multiple, selection, checklist, dropdown, array -->
[Same detailed structure as Checkbox]

### RadioGroup {essential} 🟡 DEPRECATED
<!-- keywords: radio, single, selection, deprecated, broken -->
⚠️ **DEPRECATED**: Use Select instead due to critical limitations
[Same detailed structure but with deprecation warnings prominent]

### Select {essential}
<!-- keywords: dropdown, single, selection, standard -->
[Same detailed structure]

### AdvancedSelect {essential} 🔴 BETA
<!-- keywords: hierarchical, tree, taxonomy, beta, broken -->
⚠️ **BETA STATUS**: Not recommended for production
[Same detailed structure with beta warnings prominent]

## Troubleshooting Guide {important}
### Error Message Reference {important}
### Quick Reference Matrix {important}
### Validation Issues {important}
#### Validation Not Displaying {important}
#### Cannot Submit Form on Web {important}
### Critical Issues Table {important}
### Common Problems Table {important}
### Quick Fixes Table {important}
### Debug Checklists {comprehensive}
#### General Field Checklist {comprehensive}
#### Field-Specific Checks {comprehensive}
### Field-Specific Issues {important}

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
### Migration Procedures
#### Designer Version Migration {comprehensive}
#### Field Type Migrations
### Training Requirements {important}
#### Basic Training (All Users)
#### Advanced Training (Data Managers)
### Migration Script Templates {comprehensive}
[Include actual script templates]
### Field-Specific Best Practices {comprehensive}
### Implementation Notes {comprehensive}
### Cross-References Between Fields {comprehensive}
### External Documentation {comprehensive}

## Field Quirks Index (2025-08) {comprehensive}
### Checkbox
[All quirks with QUIRK, FIX, RULE, VERSION tags]
### MultiSelect
### RadioGroup
### Select
### AdvancedSelect

## Performance Thresholds Table (2025-08) {essential}
[Complete table with optimal/acceptable/degraded/unusable thresholds]

## JSON Patterns Cookbook (2025-08) {comprehensive}
### Common Selection Patterns
[Multiple complete, runnable patterns per field type]

## JSON Anti-patterns Quick Index {comprehensive}
### Selection Field Anti-patterns
[Consolidated anti-patterns organized by type]

## Quick Diagnosis Tables (2025-08) {important}
### Error Display Capability
### Mobile Compatibility
### Deselection Capability
### Platform Support Matrix

## Field Interaction Matrix (2025-08) {important}
[Field-to-field interaction patterns]

## Migration Warnings Index (2025-08) {comprehensive}
### Critical Migration Warnings
### Migration Risk Matrix

## Error Message Quick Reference (2025-08) {important}
### Critical Errors (Form Breaking)
### Validation Errors (User Visible - When Supported)
### Silent Failures (No User Feedback)
### Component Errors (Configuration)

## Metadata {comprehensive}
### Component Status Summary
### Quality Verification
### Documentation Version
### Platform Versions
### Revision History
```

## COMPREHENSIVE EXTRACTION REQUIREMENTS

### 1. ZERO CONTENT LOSS - ABSOLUTE REQUIREMENT
From each source document, extract:
- **EVERY** technical detail, no matter how minor
- **EVERY** warning, note, tip, and aside
- **EVERY** JSON example (complete and unmodified)
- **EVERY** table and structured data
- **EVERY** troubleshooting item
- **EVERY** implementation example by name
- **EVERY** quirk, bug, and limitation
- **EVERY** platform-specific behavior
- **EVERY** validation rule and pattern
- **EVERY** error message and condition

### 2. ENHANCEMENT PATTERNS

#### For "What These Fields Cannot Do"
Transform bullet points into detailed explanations:
```markdown
### Selection Processing Limitations {important}
- **Dynamic options** - All options must be predefined in JSON configuration. Cannot fetch options from API, database, or generate based on user input or other field values. This limitation exists because fields are statically defined at form load time.
- **Filtered options** - Cannot dynamically show/hide options based on other field selections. All options remain visible regardless of context. Workaround is to use conditional fields instead.
[Continue with detailed explanation for EACH limitation]
```

#### For "Common Use Cases"
Provide domain-specific configurations:
```markdown
### Archaeological and Heritage Recording

**Site Classification**:
- **Site types** → Select with 10-50 controlled vocabulary options (e.g., "Aboriginal scarred tree", "Shell midden", "Rock shelter"). Include empty option "-- Not classified --" for incomplete assessments. Set required validation only if classification is mandatory.
- **Feature presence** → MultiSelect with expandedChecklist for visibility (e.g., "Stone tools", "Bone fragments", "Charcoal"). Use exclusive option "No features observed" that clears all others. Apply yup.min(1) validation to ensure selection.
```

#### For Decision Trees
Create comprehensive ASCII trees:
```markdown
### Quick Decision Tree
What type of selection do you need?
│
├─ Boolean/binary state?
│  ├─ YES → Checkbox
│  │  ├─ Returns: faims-core::Boolean (true/false)
│  │  ├─ Best for: Consent, presence/absence, yes/no
│  │  └─ Limitation: Label not clickable (known bug)
│  └─ NO → Continue
│
├─ Multiple values from list?
│  ├─ YES → MultiSelect
│  │  ├─ Returns: faims-core::Array
│  │  ├─ Display modes:
│  │  │  ├─ ≤15 options → expandedChecklist
│  │  │  └─ >15 options → dropdown
│  │  ├─ Unique feature: Exclusive options
│  │  └─ Validation quirk: Empty array passes required
│  └─ NO → Continue
[Continue with full tree]
```

#### For Error References
Categorize comprehensively:
```markdown
### Critical Errors (Form Breaking)
| Error Message | Field Type(s) | Root Cause | Quick Fix | Prevention | First Seen |
|---------------|---------------|------------|-----------|------------|------------|
| "Component Checkbox not found" | Checkbox | Wrong namespace | Use faims-custom | Check namespace | v3.0 |
[Include EVERY error from source documents]

### Silent Failures (No User Feedback)
| Issue | Field Type(s) | Symptoms | Detection Method | Workaround | Impact |
|-------|---------------|----------|------------------|------------|--------|
| Empty array passes required | MultiSelect | Form submits with [] | Check data on submit | Use yup.min(1) | High |
[Include ALL silent failures]
```

#### For JSON Patterns
Include complete, runnable examples:
```markdown
**Consent Checkbox (Must Accept)**:
Use case: Legal compliance requiring explicit consent
```json
{
  "consent-field": {
    "component-namespace": "faims-custom",
    "component-name": "Checkbox",
    "type-returned": "faims-core::Boolean",
    "component-parameters": {
      "name": "consent-field",
      "id": "consent-field-1",
      "label": "I consent to data collection",
      "helperText": "You must accept to continue",
      "required": true
    },
    "validationSchema": [
      ["yup.boolean"],
      ["yup.oneOf", [true], "You must consent to proceed"]
    ],
    "initialValue": false,
    "meta": {
      "annotation": {"include": false},
      "persistent": false
    }
  }
}
```
Notes: 
- Required flag is visual only
- yup.oneOf enforces must-be-checked
- initialValue must be false from Designer
```

### 3. STRUCTURAL REQUIREMENTS

#### Individual Field Reference
Each field MUST include:
1. Keywords comment for searchability
2. Designer/Component/Namespace header block
3. Status badges if deprecated/beta
4. ALL subsections in order (Purpose through Implementation Examples)
5. Field-specific prefix for sections (e.g., "Checkbox-Specific Validation")
6. Complete extraction of ALL content from source document
7. Preservation of ALL examples with their original names

#### Visual Consistency
Use these indicators throughout:
- ✅ Full support/Working
- ❌ Not supported/Broken
- ⚠️ Partial/Warning
- 🔴 Critical/Beta
- 🟡 Deprecated
- 🟢 Recommended
- 📝 Note
- 💡 Tip
- 🐛 Known bug

#### Table Standards
All tables must:
- Include complete headers with pipes
- Have consistent column alignment
- Include visual indicators where appropriate
- End with verdict/recommendation column
- Preserve ALL rows from source

### 4. SPECIAL HANDLING

#### Deprecated Components (RadioGroup)
- Add 🟡 DEPRECATED badge in title
- Include deprecation box at section start
- Document all limitations that led to deprecation
- Provide clear migration path to Select
- Keep ALL original documentation for backward compatibility

#### Beta Components (AdvancedSelect)
- Add 🔴 BETA badge in title
- Include beta warning box at section start
- Document all known issues prominently
- Suggest alternatives for production
- Include timeline for stabilization if known

#### Platform-Specific Content
Create dedicated subsections for:
- iOS-specific behaviors (with version notes)
- Android-specific behaviors (with version notes)
- Web browser differences (Chrome, Safari, Firefox)
- Offline capabilities and limitations
- Performance characteristics per platform

### 5. QUALITY CHECKS

Ensure the output includes:
- [ ] ALL content from ALL source documents
- [ ] Enhanced sections with detailed explanations
- [ ] Complete decision trees with all branches
- [ ] All JSON examples runnable as-is
- [ ] Deprecation/beta warnings prominent
- [ ] Platform-specific sections complete
- [ ] Cross-references between related fields
- [ ] Implementation notes preserved
- [ ] No bullet points without explanations
- [ ] All tables properly formatted

### 6. DO NOT

- Do NOT set target line counts - focus on completeness
- Do NOT compress or combine examples
- Do NOT omit "minor" details
- Do NOT skip platform-specific notes
- Do NOT remove redundant information
- Do NOT simplify technical details

## OUTPUT

Single markdown file: `select-choice-fields-v05.md` with COMPLETE extraction of all source content plus enhancements per patterns above.