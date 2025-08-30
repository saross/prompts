# Optional: Merge Two Consolidated Document Halves

Combine two pre-deduplicated documents:
- Part 1: [Number Fields 1-3] consolidated and clean
- Part 2: [Number Fields 4-7] consolidated and clean

## CORE DIRECTIVE
Both inputs are already deduplicated. Preserve ALL content - only identify NEW shared patterns that exist BETWEEN the two halves.

## Instructions

### 1. Merge Document Structures
**Combine sections in this order**:
- Overview → Comprehensive overview listing all [7] fields
- Field Selection Guide → Combined decision tree and matrix
- Designer Capabilities → Merged tables with all fields
- Common Characteristics → Unified section (see step 2)
- Individual Field Reference → All [7] fields in logical order
- Troubleshooting Guide → Combined tables
- JSON Examples → All patterns from both
- Migration and Best Practices → Merged content

### 2. Handle Between-Half Shared Content

**Mark shared patterns between documents**:
- First occurrence: [SHARED-START: topic name - Part1/Part2]
- Second occurrence: [SHARED-END: topic name - see above]
- Different implementations: [VARIANT-PART1] and [VARIANT-PART2]

**Common Characteristics merging**:
- Combine subsections preserving all content
- Note which fields affected: [affects: Field1, Field2, Field3...]
- Create comparison tables for variants

**Example**:
```
Part 1: "Performance degrades at 50 characters for TextField"
Part 2: "Performance degrades at 100 items for SelectField"
→ Mark as [SHARED-START: performance-degradation] at first occurrence
```

### 3. Merge Tables and Lists

**Troubleshooting tables**:
- Combine entries, expanding "Field Type" column
- Merge similar issues, list ALL affected fields
- Preserve unique solutions for each part

**Performance/Platform tables**:
- Add columns for new fields
- Preserve all thresholds and metrics
- Note part-specific behaviors

**Designer mapping**:
- Combine into single comprehensive table
- Maintain all UI name variations

### 4. Preserve Part-Specific Content

**Keep distinct**:
- Field-specific examples (even if similar structure)
- Unique validation patterns
- Part-specific workarounds
- Different error messages

## Verification Checklist

**Structure**:
- [ ] All [7] fields present in Individual Field Reference
- [ ] Overview lists all fields correctly
- [ ] Designer mapping complete for all fields

**Content Preservation**:
- [ ] All JSON examples from both parts
- [ ] All warnings and security notes
- [ ] All troubleshooting items
- [ ] All performance metrics

**Marking**:
- [ ] Between-half duplicates marked with SHARED tags
- [ ] Variants marked appropriately
- [ ] No within-part deduplication (already clean)

## Quality Metrics
- Expected length: ~95% of sum of both parts
- New SHARED markers: Only for between-half patterns
- Field count: [7] complete sections
- JSON examples: Sum of both parts

## DO NOT
- ❌ Delete content appearing in both halves
- ❌ Re-deduplicate within each part
- ❌ Summarize when combining
- ❌ Reorganize already-structured content
- ❌ Apply new structure (maintain existing)

## Success Validation
The merged document should:
1. Contain ALL content from both halves
2. Have SHARED/VARIANT tags only for between-half patterns
3. Maintain the structure from input documents
4. Be ready for final deduplication pass

Output the complete merged document with between-half patterns marked.