# LLM-First Consolidation Prompt: Choice/Selection Fields

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

### CRITICAL: Include ALL v05 Standard Sections
The following sections MUST be present to match other v05 documents:
1. Overview {essential}
2. Designer Usage Guide {essential}  
3. ⚠️ CRITICAL RISKS {essential}
4. What These Fields Cannot Do {important}
5. Common Use Cases {important}
6. **Common Characteristics** {important} - REQUIRED SECTION
7. **Field Selection Guide** {essential} - REQUIRED SECTION
8. **Designer Capabilities vs JSON Enhancement** {essential} - REQUIRED SECTION
9. Individual Field Reference - WITH ALL SUBSECTIONS
10. Troubleshooting Guide {important}
11. **JSON Anti-patterns Quick Index** {important} - REQUIRED SECTION
12. JSON Examples {comprehensive}
13. **JSON Patterns Cookbook** {comprehensive} - REQUIRED SECTION
14. Migration and Best Practices {comprehensive}
15. **Migration Warnings Index** {comprehensive} - REQUIRED SECTION
16. Field Quirks Index {comprehensive}
17. Performance Thresholds Table {essential}
18. Field Interaction Matrix {important}
19. Quick Diagnosis Tables {important}
20. Metadata

### Required Structure (Follow v05 Pattern EXACTLY)

```markdown
# Selection and Choice Fields

## Overview {essential}

The Fieldmark ecosystem provides five selection/choice field types for controlled data entry and option selection:

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
- **"Select Field"** appears TWICE with different functionality
  - Plain "Select Field" = standard dropdown (component: Select)
  - "Select Field (Hierarchical)" = tree selection (component: AdvancedSelect)

### Data Capture Fields (1-5)

1. **Checkbox** - [extract purpose from checkbox.md]

2. **MultiSelect** - [extract from multiselect.md]

3. **RadioGroup** - [extract from radiogroup.md]

4. **Select** - [extract from select.md]

5. **AdvancedSelect** - [extract from advanced-select.md]

### Component Status Summary
[Create table showing maturity, platform support, known issues for all 5]

## Designer Usage Guide {essential}

### What to Select in Designer
[Detailed guidance for each of the 5 Designer options]

### When JSON Enhancement is Required
[List what requires JSON editing beyond Designer capabilities]

### Quick Use Case Examples
[Common scenarios for each field type]

## ⚠️ CRITICAL SELECTION FIELD RISKS {essential}
[Extract security vulnerabilities, data integrity risks, platform limitations]

## What These Fields Cannot Do {important}

### Selection Processing Limitations {important}
[Extract from all documents]

### Validation Limitations {important}
[Extract from all documents]

### Display Limitations {important}
[Extract from all documents]

## Common Use Cases {important}
[Organize by use case, not by field]

## Individual Field Reference

### Checkbox {essential}
[Full content from checkbox.md]
#### JSON Anti-patterns
[Extract and place here, not in central location]
#### Spec Mapping
[Common Designer-to-JSON patterns]

### MultiSelect {essential}
[Full content from multiselect.md]
#### JSON Anti-patterns
[Extract and place here, not in central location]
#### Spec Mapping
[Extract mappings]

### RadioGroup {essential}
[Full content from radiogroup.md]
#### JSON Anti-patterns
[Extract and place here]
#### Spec Mapping
[Extract mappings]

### Select {essential}
[Full content from select.md]
#### JSON Anti-patterns
[Extract and place here]
#### Spec Mapping
[Extract mappings]

### AdvancedSelect {essential}
[Full content from advanced-select.md]
#### JSON Anti-patterns
[Extract and place here]
#### Spec Mapping
[Extract mappings]

[Continue with remaining v05 structure sections...]
```

## Critical Processing Rules

### 1. ZERO CONTENT LOSS - CRITICAL REQUIREMENT
- Preserve EVERY technical detail from source documents
- Include ALL warnings, notes, tips
- Keep ALL JSON examples (every single one from source files)
- Include ALL implementation examples by name (e.g., permits-required, recording-type, condition-state, context-hierarchy, location-hierarchy)
- Maintain ALL troubleshooting items
- Include ALL tables from source documents
- DO NOT compress or combine examples - include each one separately

### 2. Complete Documentation Available
All five components now have complete documentation:
- Checkbox (boolean toggle)
- MultiSelect (multiple selection with array return)
- RadioGroup (single selection with radio buttons)
- Select (single selection dropdown)
- AdvancedSelect (hierarchical selection)

### 3. Namespace Corrections
- ALL five components use `faims-custom` namespace
- No `formik-material-ui` variants for these
- Warn if any examples show wrong namespace

### 4. Anti-Pattern Distribution
- Move ALL anti-patterns from central sections to individual field sections
- Each field gets its own "JSON Anti-patterns" subsection
- Include namespace errors as anti-patterns

### 5. Designer Disambiguation
- Clearly explain the TWO "Select Field" options
- Use visual markers (🔘 vs 📝) to distinguish
- Note RadioGroup is "Select one option" not "Radio"

### 6. Platform-Specific Issues
- iOS keyboard limitations
- Web vs mobile behavior differences
- Offline capability notes

### 7. Tagging Requirements
- {essential} - Core functionality, Designer mapping
- {important} - Common patterns, troubleshooting
- {comprehensive} - Edge cases, detailed examples

## Known Issues to Address

1. **"Select Field" Duplication** - Two different components with similar Designer names
2. **RadioGroup Naming** - Called "Select one option" not "Radio" in Designer
3. **Option Format Variations** - Different fields use different option structures
4. **MultiSelect Validation Quirk** - Empty array [] passes "required" validation (need yup.min(1) instead)
5. **Exclusive Options** - MultiSelect's unique mutual exclusivity feature needs clear documentation

## Content Preservation Checklist
- [ ] ALL 5 Designer options documented with complete detail docs
- [ ] ALL examples from source (permits-required, recording-type, condition-state, context-hierarchy, location-hierarchy)
- [ ] ALL JSON blocks from source files (7+ per field minimum)
- [ ] ALL tables from source files preserved
- [ ] Anti-patterns distributed to each field
- [ ] Namespace corrections applied
- [ ] Designer naming confusion addressed
- [ ] Platform limitations included
- [ ] Security warnings prominent
- [ ] Target ~3500 lines (matching other v05 docs)
- [ ] ~400-500 lines per field section
- [ ] Include Common Characteristics section
- [ ] Include Field Selection Guide
- [ ] Include Designer Capabilities table
- [ ] Include JSON Anti-patterns Index
- [ ] Include JSON Patterns Cookbook
- [ ] Include Migration Warnings Index

## Output Format
Single markdown file: `select-choice-fields-v05.md` following the exact structure and formatting of the successful v05 files, aiming for comparable length (~3500 lines) and depth.