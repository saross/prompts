# LLM-First Consolidation Prompt: Choice/Selection Fields (v3 - Enhanced)

## Context
You are consolidating detailed field documentation into LLM-optimized documentation following the successful v05 pattern established for text, datetime, and number fields. This v3 prompt includes instructions for automatically generating enhanced sections that add significant value beyond source documentation.

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
[For selection fields, this might be "CRITICAL SELECTION FIELD RISKS" - data integrity, validation failures, etc.]

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

## Designer Component Mapping {essential}
### Designer UI vs JSON Component Names
### Designer Limitations Requiring JSON

## Component Selection Decision Tree {important}
### Which Component Should You Use?

## Component Namespace Errors {important}
### Troubleshooting "Component not found" Errors
### Common Namespace Confusion Points

## Common Characteristics {important}
### Shared Behaviors Across Selection Fields
### Security Considerations {important}
### Performance Boundaries {important}
### Common Validation Patterns {important}
### Platform Behaviors {important}
### Shared Limitations {important}

## Individual Field Reference {essential}
[One section per field with full subsections]

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

## Performance Thresholds Table (2025-08) {essential}

## JSON Patterns Cookbook (2025-08) {comprehensive}

## JSON Anti-patterns Quick Index {comprehensive}

## Quick Diagnosis Tables (2025-08) {important}

## Field Interaction Matrix (2025-08) {important}

## Migration Warnings Index (2025-08) {comprehensive}

## Error Message Quick Reference (2025-08) {important}

## Metadata {comprehensive}
```

## ENHANCED CONTENT GENERATION RULES

### 1. What These Fields Cannot Do - DETAILED EXPLANATIONS
For EACH limitation, provide:
- **Brief title** - What cannot be done
- **Detailed explanation** - Full sentence explaining the limitation, why it exists, and impact
- **Example**: "**Dynamic options** - All options must be predefined in JSON configuration. Cannot fetch options from API, database, or generate based on user input or other field values"

Minimum requirements:
- 5+ limitations per subsection
- Each with 1-2 sentence explanation
- Include specific technical reasons

### 2. Common Use Cases - DOMAIN-SPECIFIC EXAMPLES
Structure as:
```markdown
### Archaeological and Heritage Recording

**Site Classification**:
- **Site types** → Select with 10-50 controlled vocabulary options (e.g., "Aboriginal scarred tree", "Shell midden", "Rock shelter"). Include empty option "-- Not classified --" for incomplete assessments
- **Feature presence** → MultiSelect with expandedChecklist for visibility (e.g., "Stone tools", "Bone fragments", "Charcoal"). Use exclusive option "No features observed" that clears all others
[... continue with specific configurations ...]
```

Requirements:
- 3+ domain categories minimum
- 4+ specific scenarios per domain
- Include exact field type recommendations
- Add configuration details in parentheses
- Mention validation approaches

### 3. Field Selection Guide - VISUAL DECISION TREE
Create ASCII decision tree:
```markdown
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
```

Include comparison matrix with visual indicators:
| Field Type | Returns | Max Options | Error Display | Use When | Avoid When |
Use ✅❌⚠️ symbols for quick scanning

### 4. Designer Component Mapping - COMPLETE TABLES
Always include:
```markdown
| Designer UI Label | JSON component-name | Component Namespace | Type Returned | Description |
```
Add critical naming confusion warnings with specific examples

### 5. Error Message Quick Reference - THREE-TIER CATEGORIZATION
Structure as:
```markdown
### Critical Errors (Form Breaking)
| Error Message | Field Type(s) | Root Cause | Quick Fix | Prevention |

### Validation Errors (User Visible - When Supported)
| Error Message | Field Type(s) | Actually Displays? | Root Cause | Workaround |

### Silent Failures (No User Feedback)
| Issue | Field Type(s) | Symptoms | Detection | Resolution |
```

### 6. JSON Patterns Cookbook - COMPLETE EXAMPLES
For each pattern:
- **Pattern name** (e.g., "Consent Checkbox (Must Accept)")
- **Complete JSON** ready to copy-paste
- **Use case** explanation
- Minimum 5 patterns per field type

Example:
```markdown
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

### 7. Quick Diagnosis Tables - VISUAL COMPARISONS
Create comparison tables with:
- Visual indicators (✅ Yes, ❌ No, ⚠️ Partial, 🔴 Critical)
- Clear verdicts/recommendations
- Multiple comparison dimensions

Example:
```markdown
### Error Display Capability
| Field | Shows Error Color | Shows Error Text | ARIA Support | Verdict |
|-------|------------------|------------------|--------------|---------|
| Checkbox | ✅ Yes | ✅ Yes | ❌ No | Best option |
| MultiSelect | ❌ No | ❌ No | ❌ No | Silent failure |
```

### 8. Migration Warnings Index - RISK ASSESSMENT
Include risk matrix:
```markdown
### Migration Risk Matrix
| From | To | Risk Level | Data Loss | Reversible |
|------|----|------------|-----------|------------|
| RadioGroup | Select | Low | No | Yes |
| Multiple Checkbox | MultiSelect | High | Possible | No |
```

Add specific warnings for each migration path

### 9. Common Characteristics - SHARED BEHAVIORS
Document behaviors common to ALL selection fields:
- Namespace requirements (all use faims-custom)
- Validation timing
- Export formats
- Platform differences
- Performance considerations

### 10. Component Selection Decision Tree
Create a separate decision tree focused on technical requirements:
```markdown
### Which Component Should You Use?
Need error messages displayed?
├─ YES → Only Checkbox shows errors properly
└─ NO → Continue to next criterion
   │
   Need mobile support?
   ├─ NO → Can use AdvancedSelect
   └─ YES → Avoid AdvancedSelect (500px width issue)
```

## CONTENT ENHANCEMENT PATTERNS

### Visual Indicators
Use consistently:
- ✅ Full support/Yes
- ❌ No support/No  
- ⚠️ Partial/Warning
- 🔴 Critical issue/Beta
- 🟡 Deprecated
- 🟢 Recommended
- 📝 Note
- 💡 Tip

### Decision Trees
- Use ASCII art with ├─ └─ │ characters
- Include decision criteria at each branch
- End with specific recommendations

### Tables
- Always include headers
- Use pipe | separators
- Add visual indicators in cells
- Include "Verdict" or "Recommendation" columns

### JSON Examples
- Must be syntactically valid
- Include all required fields
- Add comments for clarity
- Show both correct and incorrect patterns

### Platform Notes
Always specify when something is:
- Mobile-specific
- iOS/Android differences
- Web-only
- Desktop-optimized

## CRITICAL PROCESSING RULES

### 1. ZERO CONTENT LOSS
- Include ALL content from source documents
- ADD enhanced sections per patterns above
- Never remove technical details
- Preserve all warnings and quirks

### 2. ENHANCED DEPTH
Each section should be:
- **Overview**: 100-150 lines with complete status tables
- **Individual Field Reference**: 400-500 lines per field
- **Troubleshooting**: 150+ lines with multiple tables
- **JSON Examples**: 200+ lines with 20+ examples
- **Error Reference**: 100+ lines with categorized errors

### 3. PRACTICAL FOCUS
- Every example should be runnable
- Every pattern should be copy-pasteable
- Every decision tree should lead to action
- Every table should support decisions

### 4. CONSISTENCY
- Use same visual indicators throughout
- Maintain consistent table formats
- Follow same pattern for each field type
- Use consistent terminology

## Target Metrics
- Total document: 2,500-3,500 lines
- Enhanced sections: 30-40% of content
- JSON examples: 50+ total
- Tables: 15+ total
- Decision trees: 3+ total
- Complete patterns: 25+ total

## Output Format
Single markdown file: `select-choice-fields-v05.md` following the exact structure above, with all enhanced sections automatically generated per these patterns.