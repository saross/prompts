## Prompt A1: Extract Quirks & Performance Limits (ENHANCED)

You are enhancing a Fieldmark field documentation file for LLM-first consumption, particularly for Claude Code notebook generation.

TASK: Extract and structure Field Quirks Index and Performance Thresholds Table from the provided documentation.

INPUT: The consolidated text field documentation is available in project knowledge as "Email and Address Fields - Merged Documentation.md" - this document contains all 7 field types. Please search for and load this document to analyze.

CRITICAL INSTRUCTION: Generate ONLY the new sections to be appended. Do NOT reproduce the original document. Output ONLY the enhancement sections with clear integration markers.

REQUIREMENTS:
1. Create two new sections that will be placed at the document's end, just before the Metadata section:
   - "Field Quirks Index (2025-08)"
   - "Performance Thresholds Table (2025-08)"
2. Generate ONLY these new sections, not the full document
3. Include version marker "2025-08" for all entries
4. Cover all 7 field types: TextField, MultilineText, TemplatedString, Email, QRCodeFormField, Address, RichText
5. Use structured list format for quirks, markdown table for thresholds
6. Distinguish between RULE (must follow), QUIRK (known issue), and FIX (solution)
7. **NEW**: FIX instructions must be SPECIFIC with code examples, regex patterns, or exact steps
8. **NEW**: Add cross-references to other sections using [Section Name > Subsection] format
9. **NEW**: Include ERROR entries for common error messages and their meanings

OUTPUT FORMAT:

[START OF GENERATED SECTION - Add before Metadata]
---
## Field Quirks Index (2025-08) {comprehensive}

### TextField
- `RULE` Maximum 50 characters recommended for optimal display
- `QUIRK` No character counter displayed to users
- `FIX` Add helperText: "Maximum 50 characters" to component-parameters
- `VERSION` 2025-08

### MultilineText
- `RULE` Component name is "MultipleTextField" not "MultilineTextField"
- `ERROR` "Unknown component MultilineTextField" means wrong component name
- `QUIRK` Fixed height - no auto-expansion beyond configured rows
- `QUIRK` Performance degrades beyond 10,000 characters
- `FIX` Set InputProps.rows to expected content size (4-8 typical)
- `FIX` For >10,000 chars, implement pagination or use attachments
- `XREF` See [Performance Thresholds Table > MultilineText]
- `VERSION` 2025-08

### TemplatedString
- `RULE` Must exist as hridField in every notebook
- `RULE` Cannot reference other TemplatedString fields (circular reference prevention)
- `ERROR` "Maximum call stack exceeded" = circular template reference
- `QUIRK` HTML escaping disabled (formUtilities.ts line 163) [Security Risk]
- `QUIRK` Shows [object Object] for complex fields (relationships, nested objects)
- `QUIRK` Shows [object Blob] for file/photo fields
- `FIX` For security, validate templates with regex: ^[A-Za-z0-9{{}\s\-_]*$
- `FIX` For user input in templates, sanitize with: .replace(/[<>'"]/g, '')
- `FIX` Complex fields: Use only for conditionals {{#field}}exists{{/field}}
- `XREF` See [JSON Patterns Cookbook > TemplatedString > Conditional Patterns]
- `XREF` See [Field Interaction Matrix > Data Type Interactions]
- `VERSION` 2025-08

### Email
- `RULE` Not a separate component - TextField with type="email"
- `ERROR` "Component EmailField not found" = use TextField instead
- `QUIRK` Mobile keyboard @ symbol sometimes hidden
- `QUIRK` Validation accepts plus-addressing (user+tag@domain.com)
- `FIX` Set InputProps: {"type": "email"} in component-parameters
- `FIX` For strict validation add: ["yup.matches", "^[^+]+@", "No plus-addressing"]
- `VERSION` 2025-08

### QRCodeFormField
- `RULE` Mobile-only functionality - no web support
- `RULE` Never mark as required (breaks web forms completely)
- `ERROR` "Form cannot be submitted" on web = QRCodeFormField marked required
- `QUIRK` 10-scan validation mechanism with no user feedback
- `QUIRK` Silent counter reset when different barcode detected
- `FIX` Always implement paired pattern:
  ```json
  "scan": {"component-name": "QRCodeFormField"},
  "manual": {"component-name": "TextField"}
  ```
- `FIX` Add conditional logic: show scanner on mobile, text on web
- `XREF` See [JSON Patterns Cookbook > QRCodeFormField > Paired Pattern]
- `XREF` See [Field Interaction Matrix > Critical Incompatibilities]
- `VERSION` 2025-08

### Address
- `RULE` Beta feature - expect breaking changes
- `RULE` initialValue must be null or valid object, never ""
- `ERROR` "Cannot read property 'address' of undefined" = wrong initialValue
- `QUIRK` Race condition when tabbing quickly between subfields
- `QUIRK` CSV export produces JSON string in single column
- `FIX` Set initialValue: null (not "" or {})
- `FIX` For CSV extraction use Python:
  ```python
  df['postcode'] = df['address'].apply(
    lambda x: json.loads(x).get('address',{}).get('postcode','')
  )
  ```
- `XREF` See [Quick Diagnosis Tables > Export Issues]
- `VERSION` 2025-08

### RichText
- `RULE` Display-only - no data capture or export
- `ERROR` "Memory quota exceeded" = too many RichText fields
- `QUIRK` Memory leak on mobile - never releases parsed HTML
- `QUIRK` Tables/blockquotes disappear at runtime (DOMPurify strips)
- `QUIRK` External images blocked (empty whitelist hardcoded)
- `FIX` Maximum 10 RichText fields per notebook
- `FIX` Keep total word count <1000 across all RichText
- `FIX` For tables, convert to Base64 image:
  ```javascript
  const tableImage = "data:image/png;base64,iVBORw0KGgoAAAA..."
  content: `![Table](${tableImage})`
  ```
- `FIX` For external images, embed as Base64 (<100KB recommended)
- `XREF` See [Performance Thresholds Table > RichText]
- `VERSION` 2025-08

[Continue with Performance Thresholds Table as before, but add XREF entries...]