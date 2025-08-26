# Merge Two Consolidated Document Halves

Combine two pre-deduplicated documents:
- Part 1: [Fields 1-3] consolidated and clean
- Part 2: [Fields 4-7] consolidated and clean

## CRITICAL DIRECTIVE
**Both inputs are already deduplicated. Preserve ALL content - only identify NEW duplicates that exist BETWEEN the two halves.**

## Instructions

1. **Merge Structures**:
   - Combine overviews → single comprehensive overview listing all fields
   - Merge Common Characteristics sections → unified section
   - Place all Individual Field sections in order
   - Combine Troubleshooting Guides → single guide

2. **Mark Between-Half Duplicates**:
   - Add [DUPLICATE] tags where same content appears in BOTH halves
   - Don't remove anything - just mark for final cleanup
   - Example: If both halves mention "Performance degrades at X", mark it

3. **Handle Overlaps in Common Sections**:
   - If both have "Performance Boundaries", combine listings: "Fields 1-3: X limit, Fields 4-7: Y limit"
   - If both have same troubleshooting issue, merge solutions and list ALL affected fields

## Quality Checks
- [ ] All [N] fields have complete sections in order
- [ ] Both Common Characteristics sections fully merged
- [ ] Both Troubleshooting guides fully combined  
- [ ] All JSON examples present
- [ ] All warnings preserved
- [ ] [DUPLICATE] tags added for between-half patterns

## DO NOT
- ❌ Delete content that appears in both halves
- ❌ Re-deduplicate within sections (already clean)
- ❌ Summarize when merging
- ❌ Remove "redundant" examples

## Success Test
The merged document should be approximately the sum of both halves' length, with [DUPLICATE] tags marking only content that appears in BOTH documents.

Output the complete merged document.