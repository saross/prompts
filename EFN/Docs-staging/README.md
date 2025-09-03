# Fieldmark v3 Documentation - Staging Area

## Directory Structure

### 📁 field-categories/
Main field category documentation (v05 - LLM-optimized):
- `text-fields-v05.md` - Text input fields (134KB)
- `number-fields-v05.md` - Numeric input fields (105KB)  
- `datetime-fields-v05.md` - Date and time fields (105KB)
- `select-choice-fields-v05.md` - Selection fields (135KB)

### 📁 reference-docs/
Centralized reference documentation (extracted common content):
- `accessibility-reference.md` - WCAG compliance and touch targets
- `component-namespace-reference.md` - Component naming and troubleshooting
- `data-export-reference.md` - CSV/JSON export behavior
- `designer-limitations-reference.md` - Designer UI constraints
- `formik-integration-reference.md` - Formik state management
- `meta-properties-reference.md` - Annotation and uncertainty
- `performance-thresholds-reference.md` - Performance estimates
- `security-considerations-reference.md` - XSS and security
- `validation-timing-reference.md` - Universal validation behavior

### 📁 detail-singlefield-docs/
Source documentation for individual fields:
- `choice/` - Individual choice field documentation
- `datetime/` - Individual datetime field documentation
- `location/` - MapForm, TakePoint documentation
- `media/` - FileUploader, TakePhoto documentation
- `number/` - Individual number field documentation
- `text/` - Individual text field documentation
- `other/` - Additional field types

### 📁 detail-crossfield-docs/
Cross-cutting documentation:
- `conditional-logic.md` - Field dependencies and conditions
- `field-selection-best-practices.md` - Choosing the right field
- `navigation.md` - Form navigation patterns
- `notebook-structure.md` - Notebook organization
- `patterns.md` - Common implementation patterns
- `quick-start.md` - Getting started guide
- `summary-table.md` - Field comparison matrix
- `validation.md` - Validation strategies

### 📁 prompts/
Consolidation prompts for documentation generation

### 📁 reports/
Analysis, planning, and historical documentation

## Recent Updates (2025-09-03)

### ✅ Completed - Documentation Centralization
1. Created 9 reference documents extracting ~2,000 lines of redundant content per field doc
2. Standardized decision trees across all 4 field category documents
3. Aligned all documents to LLM-optimal template structure
4. Added Error Message Quick Reference to number and datetime docs
5. Added "See Also" cross-references to all field documents
6. Reorganized folder structure for better navigation

## Previous Updates (2025-09-02)

### ✅ Completed - Morning Session
1. Generated comprehensive `select-choice-fields-v05.md` using v4 LLM-optimized prompt
2. Fixed heading hierarchy (Individual Field Reference as H2, fields as H3)
3. Organized directory with reports/ and prompts/ subdirectories
4. Created v5 lossless extraction prompt for complete content preservation
5. Developed standalone documentation strategy

### ✅ Completed - Afternoon Session
6. Added all missing content to choice fields (~240 lines total):
   - Quick Reference enhancements (touch targets, performance, storage)
   - Validation Timing Behavior subsection
   - Inline measurements and platform notes
   - 11 missing named examples with complete JSON
7. Created LLM-optimal structure specification document
8. Performed comprehensive accuracy check against codebase:
   - Fixed critical error: `faims-core::Boolean` → `faims-core::Bool`
   - Fixed validation: `yup.boolean` → `yup.bool`
   - Verified all JSON structures and technical claims
9. Achieved 85-90% content coverage from source documents

### 📋 Next Steps
1. Create priority standalone references:
   - `performance-thresholds-matrix.md`
   - `platform-specifications-reference.md`
   - `data-storage-export-reference.md`
2. Generate `media-fields-v05.md` using v5 prompt
3. Apply LLM-optimal structure to text, number, datetime fields

## Documentation Standards

### LLM-Optimal Structure
- Designer Usage Guide at position #2 (early practical context)
- Field Selection Guide at position #3 (decision support)
- Quick Reference boxes with key metrics
- Core Configuration examples immediately after Purpose
- [affects: Field] notation in Common Characteristics

### Content Guidelines
- Category docs: ~2,200-2,500 lines (lean, focused)
- Complete examples with working JSON
- Platform-specific details inline (not separate sections)
- Performance thresholds with specific numbers
- Migration procedures for deprecated components

## Master List of Planned Standalone Documents

### Priority 1 (Essential)
- [ ] `performance-thresholds-matrix.md`
- [ ] `platform-specifications-reference.md`
- [ ] `data-storage-export-reference.md`

### Priority 2 (Technical)
- [ ] `field-technical-architecture.md`
- [ ] `validation-timing-reference.md`
- [ ] `debug-procedures-guide.md`

### Priority 3 (Operational)
- [ ] `migration-procedures-handbook.md`
- [ ] `field-cross-references-matrix.md`
- [ ] `accessibility-compliance-matrix.md`

### Priority 4 (Advanced)
- [ ] `field-state-transitions.md`
- [ ] `json-patterns-cookbook.md`
- [ ] `field-quirks-reference.md`
- [ ] `error-message-reference.md`