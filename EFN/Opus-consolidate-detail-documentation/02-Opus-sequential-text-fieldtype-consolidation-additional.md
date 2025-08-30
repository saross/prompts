# Prompt 2: Add Additional Field

## Add [Display] to Consolidated Document

Load and add the [Display] complete third-draft documentation to the existing [3]-field consolidated document.

### CORE DIRECTIVE
Preserve 100% of content from both the new field documentation and existing consolidated document.

### Instructions

1. **Update document structure**:
   - Add new field to overview section
   - Insert complete field section in Individual Field Reference
   - Update field counts throughout document
   - Maintain existing content unchanged

2. **Duplication Handling**
   When [Display] content overlaps with existing fields:
   - Mark in existing location: [SHARED-START: topic name]
   - Mark in Display section: [SHARED-END: topic name - see above]
   - If implementations differ: use [VARIANT-EXISTING] and [VARIANT-DISPLAY]
   - Include both versions when meaningful differences exist

3. **Integration Points**:
   - Common Characteristics: Add Display-specific items
   - Shared patterns: Mark with [SHARED: pattern name]
   - Validation rules: Note if Display uses same patterns
   - Platform behaviors: Add Display column to existing tables

4. **Critical items for [Display]**:
   - [Field-specific warnings to emphasize]
   - [Field-specific unique features]
   - [Known compatibility issues with other fields]

### Preservation Checklist
- [ ] Every section from [Display] documentation
- [ ] All JSON examples from Display
- [ ] All warnings, edge cases, technical notes
- [ ] All troubleshooting items
- [ ] All implementation details
- [ ] Existing document remains complete

### Verification Metrics
- Line count increase: +[estimated lines from Display doc]
- New JSON examples: [count from Display]
- Shared topics marked: [SHARED] tags applied
- Variants documented: [VARIANT] tags where applicable

### DO NOT
- ❌ Remove existing content
- ❌ Summarize Display content
- ❌ Merge similar sections
- ❌ Skip "redundant" information
- ❌ Reorganize existing structure

Output the expanded document with ALL content preserved and clear duplicate markers.