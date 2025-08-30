# Prompt C1: Create Quick Diagnosis Tables

You are enhancing a Fieldmark field documentation file for LLM-first consumption, particularly for Claude Code notebook generation.

TASK: Create Quick Diagnosis Tables that map symptoms to causes and solutions.

INPUT: The consolidated field documentation containing all [N] field types. Load this document from project knowledge to analyze, focusing on troubleshooting and common issues sections.

CRITICAL INSTRUCTION: Generate ONLY the new section to be appended. Do NOT reproduce the original document. Output ONLY the enhancement section with clear integration markers.

REQUIREMENTS:
1. Create a new section "Quick Diagnosis Tables (2025-08)" at document end, just before the Metadata section
2. Generate ONLY this new section, not the full document
3. Use markdown tables with appropriate columns for each scenario type
4. Organize tables by problem categories
5. Include field-specific issues and solutions
6. Make solutions actionable and specific
7. Include version marker (2025-08) in section title and table entries where relevant

OUTPUT FORMAT:

[START OF GENERATED SECTION - Add before Metadata]
---
## Quick Diagnosis Tables (2025-08) {important}

### When [Problem Category 1] Occurs

| Symptom | Field Type | Likely Cause | Quick Fix | Version |
|---------|------------|--------------|-----------|---------|
| [Specific symptom] | [Field name] | [Root cause] | [Actionable solution] | 2025-08 |
| [Another symptom] | [Field name] | [Root cause] | [Step-by-step fix] | 2025-08 |

### When [Problem Category 2] Fails

| Symptom | Field Type | Pattern | Fix | Version |
|---------|------------|---------|-----|---------|
| [Specific issue] | [Field name] | [Pattern that fails] | [Correction needed] | 2025-08 |
| [Another issue] | [Field name] | [Pattern that fails] | [How to fix] | 2025-08 |

### When [Problem Category 3] Issues Occur

| Symptom | When | Why | Try This | If That Fails | Long Term |
|---------|------|-----|----------|---------------|-----------|
| [Issue description] | [Context] | [Root cause] | [First attempt] | [Second attempt] | [Prevention] |
| [Another issue] | [Context] | [Root cause] | [Quick solution] | [Alternative] | [Best practice] |

### When [Performance/Display/Export/etc.] Issues Occur

[Continue with appropriate table structure for each category]

### Quick Reference Matrix

| If you see... | First try... | Then try... | Last resort... |
|---------------|--------------|-------------|----------------|
| [Common symptom] | [Immediate action] | [Secondary action] | [Escalation] |
| [Another symptom] | [Quick fix] | [Alternative] | [Get help] |

---
[END OF GENERATED SECTION]