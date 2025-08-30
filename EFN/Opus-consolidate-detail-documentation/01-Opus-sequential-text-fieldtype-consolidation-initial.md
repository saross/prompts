# Prompt 1: Complete Content Preservation Merge

Review: 'Fieldmark Documentation Consolidation - Context and Goals.md' in project knowledge.

## Task: Merge [Number-Input] and [Controlled-Number] Documentation

Merge these complete third-draft documentation files with 100% content preservation:
- NumberInput Field - Complete Third-Draft Documentation.md  
- ControlledNumber Field - Complete Third-Draft Documentation.md

### CORE DIRECTIVE
This is a MERGING operation. Preserve every word, example, note, and warning from both documents.

### Merge Structure
1. **Combined Overview Section**
   - Both field descriptions
   - Combined use cases (list all from both)
   - Relationship between the two fields

2. **Shared Characteristics Section**
   - Mark duplicates with: [SHARED: topic name]
   - Include both versions if they differ
   - Preserve all technical specifications

3. **Individual Field Sections**
   - Complete NumberInput section (all original content)
   - Complete ControlledNumber section (all original content)
   - Keep sections clearly separated

### Preservation Checklist
- [ ] Every JSON example from both documents
- [ ] All validation rules and patterns
- [ ] All troubleshooting items
- [ ] All warnings (⚠️), notes, tips
- [ ] All edge cases and known issues
- [ ] All code snippets and configurations
- [ ] All cross-references and "See Also" items
- [ ] All implementation notes
- [ ] All best practices

### Duplication Handling
When content appears in both documents:
1. Include both versions
2. Mark first occurrence: [SHARED-START: topic]
3. Mark second occurrence: [SHARED-END: topic - see above]
4. If versions differ, include both with [VARIANT-A] and [VARIANT-B]

### Verification Metrics
- Combined line count: ~700-900 lines (sum of originals)
- JSON examples: [count] from NumberInput + [count] from ControlledNumber
- Sections: All original sections from both documents

### DO NOT
- Remove "redundant" content
- Combine similar sections
- Summarize or compress
- Skip any content as "obvious"
- Reorganize beyond basic grouping

Output the complete merged document with clear section separators.