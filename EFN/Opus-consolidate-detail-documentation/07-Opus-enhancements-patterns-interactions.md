## Prompt A2: Extract Patterns & Interactions (ENHANCED)

You are enhancing a Fieldmark field documentation file for LLM-first consumption, particularly for Claude Code notebook generation.

TASK: Extract and structure Field Interaction Matrix and Migration Warnings Index from the provided documentation.

INPUT: The consolidated text field documentation is available in project knowledge as "Email and Address Fields - Merged Documentation.md" - this document contains all 7 field types. Please search for and load this document to analyze.

CRITICAL INSTRUCTION: Generate ONLY the new sections to be appended. Do NOT reproduce the original document. Output ONLY the enhancement sections with clear integration markers.

REQUIREMENTS:
1. Create two new sections that will be placed at the document's end, just before the Metadata section:
   - "Field Interaction Matrix (2025-08)"
   - "Migration Warnings Index (2025-08)"
2. Generate ONLY these new sections, not the full document
3. Include version marker "2025-08" for all entries
4. Document both positive interactions and negative conflicts
5. Include all breaking changes and safe migrations
6. **NEW**: Add specific code examples for migration procedures
7. **NEW**: Include validation test patterns for conditional migrations
8. **NEW**: Add rollback procedures for breaking changes where possible

OUTPUT FORMAT:

[START OF GENERATED SECTION - Add before Metadata]
---
## Field Interaction Matrix (2025-08) {important}

### Critical Incompatibilities
- `BREAKS` QRCodeFormField + Required validation = Web forms become permanently unsubmittable
  - `TEST` Check if any QRCodeFormField has ["yup.required"] in validationSchema
  - `FIX` Remove required validation, implement paired TextField pattern
- `BREAKS` Multiple RichText (>10) + Mobile = Memory leak accumulation causes app crash
  - `TEST` Count RichText fields: should be ≤10
  - `FIX` Consolidate content, use conditional visibility sparingly
- `BREAKS` TemplatedString referencing another TemplatedString = Circular reference, stack overflow
  - `TEST` Check no template includes {{other-template-field}}
  - `ERROR` "Maximum call stack size exceeded" indicates circular reference
- `VERSION` 2025-08

### Required Pairings
- `REQUIRED` Every notebook MUST have TemplatedString as hridField
  - `VALIDATE` Check viewset includes "hrid_fields": ["your-template-field"]
  - `IMPLEMENT`:
    ```json
    "record-id": {
      "component-name": "TemplatedStringField",
      "component-parameters": {
        "template": "{{type}}-{{counter}}"
      }
    }
    ```
- `REQUIRED` QRCodeFormField MUST pair with TextField fallback
  - `PATTERN` See [JSON Patterns Cookbook > QRCodeFormField > Paired Pattern]
- `VERSION` 2025-08

### Data Type Interactions
- `FORMAT` TemplatedString + BasicAutoIncrementer = String "0001" not number 1
  - `GOTCHA` Sorting will be alphabetic: "0002" < "0010" < "0100"
  - `SOLUTION` Ensure sufficient padding: num_digits: 5 for up to 99999
- `FORMAT` TemplatedString + Select = Uses value not label
  - `EXAMPLE` Select shows "North" but template gets "N"
- `FORMAT` TemplatedString + Photo = Shows "[object Blob]"
  - `NEVER` Use directly: {{photo}} 
  - `ALWAYS` Use conditionally: {{#photo}}has-photo{{/photo}}
- `VERSION` 2025-08

[Continue with enhanced specificity...]

---
## Migration Warnings Index (2025-08) {essential}

### Safe Migrations (No Data Loss)
- `SAFE` TextField → MultilineText
  ```json
  // BEFORE
  {"component-name": "TextField"}
  
  // AFTER
  {
    "component-name": "MultipleTextField",
    "component-parameters": {
      "multiline": true,
      "InputProps": {"rows": 4}
    }
  }
  ```
  - `VALIDATE` All existing data <10,000 characters
  - `TEST` Export data first as backup
- `VERSION` 2025-08

### Breaking Changes (Data Loss or Corruption Risk)
- `BREAKS` String type → Number type
  - `IMPACT` All existing string data becomes invalid
  - `ERROR` "Expected number, got string" validation errors
  - `NO ROLLBACK` Once data is lost, cannot recover
  - `ALTERNATIVE` Create new field, migrate manually:
    ```python
    # Export old data, transform, import to new field
    df['new_number'] = pd.to_numeric(df['old_string'], errors='coerce')
    ```
- `BREAKS` Adding required to populated field
  - `IMPACT` Cannot edit any existing records
  - `TEST` `SELECT COUNT(*) WHERE field IS NULL` before adding
  - `ROLLBACK` Remove required validation immediately
- `VERSION` 2025-08

### Conditional Migrations (Context Dependent)
- `CONDITIONAL` Changing validation patterns
  - `PRECHECK` Test pattern against all existing data:
    ```python
    import re
    pattern = r'^[A-Z]{3}-\d{4}$'
    invalid = df[~df['field'].str.match(pattern)]
    print(f"Would invalidate {len(invalid)} records")
    ```
  - `SAFE IF` All existing data passes new pattern
  - `UNSAFE IF` Any records would become invalid
- `VERSION` 2025-08

[Continue with specific procedures...]

---