# Deduplicate the [7]-Field Document

Take the merged document with [DUPLICATE] tags and reorganize to remove redundancy while preserving ALL information.

## CRITICAL DIRECTIVE
**Deduplication = MOVING content to shared sections, never DELETING.** Every piece of information must remain in the document, just better organized.

## Instructions

### Step 1: Move Duplicated Content to Common Sections

Review all [DUPLICATE] tags and move shared content to:

**Common Characteristics**:
- Shared Limitations (affecting 2+ fields)
- Common Validation Patterns
- Platform Behaviors (iOS/Android/Web)
- Performance Boundaries
- Security Considerations

**Troubleshooting Guide**:
- Merge similar issues into single entries
- Note which fields are affected

### Step 2: Replace with Specific References

In individual field sections, replace moved content with clear references:
- `See [Common Characteristics > Shared Limitations > Performance]`
- `See [Troubleshooting Guide > Validation Not Displaying]`

**Keep in Individual Sections**:
- Field-specific configuration
- Unique behaviors for that field
- Field-specific examples (even if similar structure)
- Unique validation rules
- Field-specific troubleshooting

### Step 3: Handle Partial Duplicates

When content is SIMILAR but not IDENTICAL:
- **Trivial differences** → Move to common section, note variations: "TextField: 50 chars, MultilineText: 10,000 chars"
- **Significant differences** → Keep in individual sections
- **When unsure** → Keep in both with cross-reference

## Quality Checks

**Before/After Counts** (must match):
- Total warnings: ___
- Total JSON examples: ___
- Total validation rules: ___
- All [DUPLICATE] tags addressed: Yes/No

**Expected Changes**:
- Individual sections: 40-60% shorter
- Word count: 20-40% reduction overall
- Common sections: Expanded with organized subsections

## Example

**BEFORE** (in TextField):
> Performance degrades above 50 characters [DUPLICATE]

**BEFORE** (in MultilineText):
> Performance degrades above 10,000 characters [DUPLICATE]

**AFTER** (in Common Characteristics):
> **Performance Boundaries**
> - TextField: 50 characters
> - MultilineText: 10,000 characters
> - Form becomes sluggish when exceeded

**AFTER** (in individual sections):
> Performance: See [Common Characteristics > Performance Boundaries]

## DO NOT
- ❌ Delete any content
- ❌ Summarize when moving  
- ❌ Create vague references like "See above"
- ❌ Merge different issues that look similar
- ❌ Remove examples because they seem redundant

## Final Test
Can you answer YES to: "Could I recreate the original separate documents from this reorganized version?"

Output the deduplicated document with ALL information preserved in its new organization.