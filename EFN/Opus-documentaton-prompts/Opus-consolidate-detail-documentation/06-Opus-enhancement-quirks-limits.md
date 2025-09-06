# Prompt A1: Extract Quirks & Performance Limits

You are enhancing a Fieldmark field documentation file for LLM-first consumption, particularly for Claude Code notebook generation.

TASK: Extract and structure Field Quirks Index and Performance Thresholds Table from the provided documentation.

INPUT: The consolidated field documentation containing all [N] field types. Load this document from project knowledge to analyze.

CRITICAL INSTRUCTION: Generate ONLY the new sections to be appended. Do NOT reproduce the original document. Output ONLY the enhancement sections with clear integration markers.

REQUIREMENTS:
1. Create two new sections that will be placed at the document's end, just before the Metadata section:
   - "Field Quirks Index (2025-08)"
   - "Performance Thresholds Table (2025-08)"
2. Generate ONLY these new sections, not the full document
3. Include version marker "2025-08" for all entries
4. Cover all [N] field types in the document
5. Use structured list format for quirks, markdown table for thresholds
6. Distinguish between RULE (must follow), QUIRK (known issue), ERROR (error messages), and FIX (solution)
7. FIX instructions must be SPECIFIC with code examples, regex patterns, or exact steps
8. Add cross-references to other sections using [Section Name > Subsection] format
9. Include TEST entries for verification steps where applicable

OUTPUT FORMAT:

[START OF GENERATED SECTIONS - Add before Metadata]
---
## Field Quirks Index (2025-08) {comprehensive}

### [FieldName1]
- `RULE` [Mandatory behavior or requirement]
- `RULE` [Another rule if applicable]
- `ERROR` "[Error message]" = [cause/meaning]
- `QUIRK` [Unexpected or non-obvious behavior]
- `FIX` [Specific solution]:
  ```json
  // or appropriate code language
  "example": "configuration"
  ```
- `TEST` [How to verify]: [specific test steps]
- `XREF` See [Section Name > Subsection]
- `VERSION` 2025-08

[Continue for all fields]

---
## Performance Thresholds Table (2025-08) {essential}

| Field Type | Metric | Threshold | Consequence | Platform | Version |
|------------|--------|-----------|-------------|----------|---------|
| [Field1] | [measurement] | [number] | [what happens] | [All/Mobile/Web] | 2025-08 |
| [Field2] | [measurement] | [number] | [what happens] | [platform] | 2025-08 |

### Critical Performance Notes {important}
- [Field1]: [Key performance insight]
- [Field2]: [Critical threshold to remember]
- Forms with >[N] fields: [Impact and recommendation]
- Mobile devices: [Specific limitations]
- [Other critical observations]

`VERSION` 2025-08

---

[END OF GENERATED SECTIONS]