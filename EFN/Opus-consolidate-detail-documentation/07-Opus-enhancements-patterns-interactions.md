# Prompt A2: Extract Patterns & Interactions

You are enhancing a Fieldmark field documentation file for LLM-first consumption, particularly for Claude Code notebook generation.

TASK: Extract and structure Field Interaction Matrix and Migration Warnings Index from the provided documentation.

INPUT: The consolidated field documentation containing all [N] field types. Load this document from project knowledge to analyze.

CRITICAL INSTRUCTION: Generate ONLY the new sections to be appended. Do NOT reproduce the original document. Output ONLY the enhancement sections with clear integration markers.

REQUIREMENTS:
1. Create two new sections that will be placed at the document's end, just before the Metadata section:
   - "Field Interaction Matrix (2025-08)"
   - "Migration Warnings Index (2025-08)"
2. Generate ONLY these new sections, not the full document
3. Include version marker "2025-08" for all entries
4. Document both positive interactions and negative conflicts
5. Include all breaking changes and safe migrations
6. Add specific code examples for migration procedures
7. Include validation test patterns for conditional migrations
8. Add rollback procedures for breaking changes where possible

OUTPUT FORMAT:

[START OF GENERATED SECTIONS - Add before Metadata]
---
## Field Interaction Matrix (2025-08) {important}

### Critical Incompatibilities
- `BREAKS` [Field1] + [Condition] = [Failure mode]
  - `TEST` [How to detect]: [specific check]
  - `ERROR` "[Error message if any]"
  - `FIX` [Required solution]
- `BREAKS` [Field2] + [Condition] = [Failure mode]
  - `TEST` Check [specific validation]
  - `FIX` [Solution with code if applicable]
- `VERSION` 2025-08

### Required Pairings
- `REQUIRED` [Field1] MUST [requirement]
  - `VALIDATE` Check [specific validation]
  - `IMPLEMENT`:
    ```json
    "example": {
      "component-name": "ComponentName",
      "component-parameters": {}
    }
    ```
- `REQUIRED` [Field2] MUST [requirement]
  - `PATTERN` See [JSON Patterns Cookbook > Pattern Name]
- `VERSION` 2025-08

### Data Type Interactions
- `FORMAT` [Field1] + [Field2] = [Result format]
  - `EXAMPLE` [Specific example]
  - `GOTCHA` [Common mistake]
  - `SOLUTION` [How to handle]
- `VERSION` 2025-08

### Platform-Specific Combinations
- `MOBILE-ONLY` [Field] functional only on iOS/Android
- `WEB-ISSUE` [Field] + [Condition] = [Problem on web]
- `PERFORMANCE` [Field combination] = [Impact]
- `VERSION` 2025-08

### Validation Cascades
- `CASCADE` [Field1 validation] + [Field2 state] = [Result]
  - `EXAMPLE` [Specific scenario]
  - `PREVENT` [How to avoid]
- `VERSION` 2025-08

---
## Migration Warnings Index (2025-08) {essential}

### Safe Migrations (No Data Loss)
- `SAFE` [Field1] → [Field2] when [condition]
  ```json
  // BEFORE
  {"component-name": "OldComponent"}
  
  // AFTER
  {"component-name": "NewComponent"}
  ```
  - `VALIDATE` [What to check before migration]
  - `TEST` [How to verify success]
- `SAFE` [Another safe migration]
- `VERSION` 2025-08

### Breaking Changes (Data Loss or Corruption Risk)
- `BREAKS` [Change description]
  - `IMPACT` [What gets broken]
  - `ERROR` "[Error message users will see]"
  - `NO ROLLBACK` [If irreversible] OR
  - `ROLLBACK` [Recovery procedure if possible]
  - `ALTERNATIVE` [Better approach]:
    ```python
    # Example migration script
    df['new_field'] = transform(df['old_field'])
    ```
- `BREAKS` [Another breaking change]
- `VERSION` 2025-08

### Conditional Migrations (Context Dependent)
- `CONDITIONAL` [Migration type]
  - `PRECHECK` [Test to run first]:
    ```python
    # Validation script
    invalid = df[condition]
    print(f"Would affect {len(invalid)} records")
    ```
  - `SAFE IF` [Conditions for safety]
  - `UNSAFE IF` [Conditions that cause problems]
  - `PROCEDURE` [Step-by-step if safe]
- `CONDITIONAL` [Another conditional migration]
- `VERSION` 2025-08

---
[END OF GENERATED SECTIONS]