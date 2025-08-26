# Prompt 1: Initial Two-Document Merge

## Merge [Field1] and [Field2] Documentation

Load and merge the [Field1] and [Field2] complete third-draft documentation files.

### PRESERVATION DIRECTIVE
**This is a MERGING operation, not summarization. Preserve 100% of content from both documents.**

### Instructions

1. **Create merged document structure**:
   - Combined overview explaining both field types
   - Shared characteristics section (mark duplicates, don't remove)
   - Individual field sections with ALL original content
   - Include EVERY subsection from originals

2. **Preservation rules**:
   - Do NOT summarize or compress any content
   - Do NOT remove anything even if redundant
   - Mark duplicated content with [DUPLICATE] tags
   - Include ALL JSON examples
   - Preserve ALL warnings, edge cases, technical notes

3. **Section completeness** - verify each field includes (if present in original):
   - Overview / Common Use Cases / Core Configuration
   - Validation Rules / Display Behaviour / Interaction Patterns
   - Conditional Logic / Data Storage / Common Patterns
   - Troubleshooting / Implementation Notes / Best Practices
   - Known Issues / See Also references

### Quality Checks
- [ ] Word count approximately sum of both originals
- [ ] Every JSON example from both originals present
- [ ] All numbered lists complete (e.g., 6 use cases = 6 in merged)
- [ ] All warnings and security notices preserved
- [ ] [DUPLICATE] tags applied to repeated content

### DO NOT
- ❌ Combine similar sections
- ❌ Summarize verbose descriptions
- ❌ Remove "redundant" examples
- ❌ Skip comprehensive content

Output the complete merged document with ALL content preserved.