# LLM-First Consolidation Prompt: Choice/Selection Fields (v2)

## Context
You are consolidating detailed field documentation into LLM-optimized documentation following the successful v05 pattern established for text, datetime, and number fields.

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
[or CRITICAL SELECTION FIELD RISKS for selection-specific]

## What These Fields Cannot Do {important}
### Selection Processing Limitations {important}
### Validation Limitations {important}
### Display Limitations {important}
### Interaction Limitations {important}

## Common Use Cases {important}
### [Organize by use case categories, not by field type]

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

## Designer Component Mapping {essential}
### Designer UI vs JSON Component Names
### Designer Limitations Requiring JSON

## Component Selection Decision Tree {important}
### Which Component Should You Use?

## Component Namespace Errors {important}
### Troubleshooting "Component not found" Errors
### Common Namespace Confusion Points

## Common Characteristics {important}
### [Shared behaviors across all selection fields]
### Security Considerations {important}
### Performance Boundaries {important}
### Common Validation Patterns {important}
### Platform Behaviors {important}
### Shared Limitations {important}

## Individual Field Reference {essential}

### Checkbox {essential}
#### Purpose {essential}
#### Key Features {essential}
#### Configuration Parameters {important}
#### Validation Semantics/Rules {important}
#### Display and Interaction {important}
#### Field-Specific Troubleshooting {important}
#### JSON Anti-patterns
#### Spec Mapping
#### Implementation Examples {comprehensive}

### MultiSelect {essential}
[Same subsection structure as Checkbox]

### RadioGroup {essential}
[Same subsection structure as Checkbox]

### Select {essential}
[Same subsection structure as Checkbox]

### AdvancedSelect {essential}
[Same subsection structure as Checkbox]

## Troubleshooting Guide {important}
### Critical Issues Without Solutions {important}
### Common Problems {important}
### Quick Fixes {important}
### Debug Checklists {comprehensive}

## JSON Examples {comprehensive}
### Base Patterns
### Anti-Patterns
### Platform-Specific Configurations
### Integration Patterns

## Migration and Best Practices {comprehensive}
### Migration Decision Tree
### Migration Warnings
### Migration Script Templates
### Training Requirements
### Alternative Approaches

## Field Quirks Index (2025-08) {comprehensive}
### [One section per field type with quirks]

## Performance Thresholds Table (2025-08) {essential}
[Table with optimal/acceptable/degraded/unusable thresholds]

## JSON Patterns Cookbook (2025-08) {comprehensive}
### Common Selection Patterns
[Multiple subsections with patterns]

## JSON Anti-patterns Quick Index {comprehensive}
### Selection Field Anti-patterns

## Quick Diagnosis Tables (2025-08) {important}
### Error Display Capability
### Mobile Compatibility  
### Deselection Capability

## Field Interaction Matrix (2025-08) {important}
[Table showing field-to-field interactions]

## Migration Warnings Index (2025-08) {comprehensive}
### Critical Migration Warnings
### Migration Risk Matrix

## Error Message Quick Reference (2025-08) {important}
### Critical Errors (Form Breaking)
### Validation Errors (User Visible - When Supported)
### Silent Failures (No User Feedback)

## Metadata {comprehensive}
```

## Critical Processing Rules

### 1. SECTION ORDER IS MANDATORY
- Follow the exact section order above
- All H2 sections must have tags {essential}, {important}, or {comprehensive}
- H3 sections under Individual Field Reference do not need tags
- Maintain exact heading levels (H1, H2, H3, H4)

### 2. ZERO CONTENT LOSS - CRITICAL REQUIREMENT
- Preserve EVERY technical detail from source documents
- Include ALL warnings, notes, tips
- Keep ALL JSON examples (every single one from source files)
- Include ALL implementation examples by name
- Maintain ALL troubleshooting items
- Include ALL tables from source documents
- DO NOT compress or combine examples

### 3. Component Documentation Requirements
All five components must be fully documented:
- Checkbox (boolean toggle)
- MultiSelect (multiple selection with array return)
- RadioGroup (single selection with radio buttons - DEPRECATED)
- Select (single selection dropdown)
- AdvancedSelect (hierarchical selection - BETA)

### 4. Namespace Corrections
- ALL five components use `faims-custom` namespace
- No `formik-material-ui` variants for these
- Include namespace errors as common mistakes

### 5. Anti-Pattern Organization
- Each field gets its own "JSON Anti-patterns" subsection in Individual Field Reference
- Also include consolidated "JSON Anti-patterns Quick Index" section
- Include namespace errors as anti-patterns

### 6. Designer Disambiguation
- Clearly explain the TWO "Select Field" options
- Note RadioGroup is "Select one option" not "Radio"
- Document Designer limitations requiring JSON

### 7. Platform-Specific Issues
- Mobile layout breaking (AdvancedSelect 500px width)
- Keyboard deselection bugs (RadioGroup)
- Touch target issues (Checkbox label)
- Performance degradation thresholds

### 8. Tagging Requirements
- {essential} - Core functionality, Designer mapping, critical info
- {important} - Common patterns, troubleshooting, key limitations
- {comprehensive} - Edge cases, detailed examples, migration scripts

## Known Issues to Document

1. **"Select Field" Duplication** - Two different components with similar Designer names
2. **RadioGroup Deprecation** - No error display, keyboard bugs
3. **MultiSelect Validation Quirk** - Empty array [] passes "required" validation
4. **AdvancedSelect Beta Status** - Can't clear selection, requires JSON editing
5. **Checkbox Label Not Clickable** - Touch target limitation
6. **No Error Message Display** - Most fields except Checkbox don't show errors

## Content Preservation Checklist
- [ ] ALL sections in exact order from template
- [ ] ALL H2 sections have tags
- [ ] ALL 5 Designer options documented with source content
- [ ] ALL examples from source files preserved
- [ ] ALL JSON blocks from source files included
- [ ] ALL tables from source files preserved
- [ ] Anti-patterns in each field section
- [ ] Namespace corrections applied
- [ ] Designer naming confusion addressed
- [ ] Platform limitations included
- [ ] Security/risk warnings prominent
- [ ] Target 2500-3500 lines (matching other v05 docs)
- [ ] ~400-500 lines per field in Individual Field Reference

## Output Format
Single markdown file: `select-choice-fields-v05.md` following the exact structure above, with all sections in the specified order.