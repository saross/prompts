# Field Documentation Unification TODO

## Goal
Make all 8 field documentation files read like chapters in the same book rather than separate publications.

## Current State
- **OLD Format** (4 docs): text-fields, select-choice-fields, datetime-fields, number-fields
- **NEW Format** (4 docs): display-field, location-fields, media-fields, relationship-field
- All follow same template structure ✅
- Technical accuracy verified ✅
- Designer limitations corrected ✅

## Priority 1: Create Navigation Infrastructure ✅ COMPLETED (2025-01-05)
- [x] Create `field-type-index.md` master index file
- [x] Add header to all 8 docs: Concatenation boundaries with metadata
- [x] Add footer to all 8 docs with links to: Field Index, Cross-field patterns, Technical references

## Priority 2: Component Name Standardization ✅ COMPLETED (2025-01-05)
- [x] Add "Component Name Mapping" table to all 8 documents
- [x] Table format: Designer UI | JSON component-name | Code File | Namespace
- [x] Use consistent terminology throughout each document
- [x] Fix namespace references to actual values (faims-custom, formik-material-ui, mapping-plugin, qrcode)

## Priority 3: JSON Example Harmonization ⏳ PARTIALLY DONE
- [x] Decision: Keep educational style but add "Production Ready Examples" section
- [ ] Add valid, copy-paste JSON examples to all OLD format docs
- [ ] Ensure NEW format docs have educational context where needed
- [x] Separate commentary from JSON blocks using "💡 **Note:**" format

## Priority 4: Cross-Reference Network ✅ COMPLETED (2025-01-05)
- [x] Add "Related Field Types" section to each document
- [x] Include "Within This Category" subsection
- [x] Include "In Other Categories" subsection
- [ ] Add migration path suggestions between old/new approaches

## Priority 5: Type System Documentation ✅ COMPLETED (2025-01-05)
- [x] Create unified type reference section (type-system-reference.md)
- [x] Add to each document or create central reference
- [x] Always show actual type (e.g., faims-core::String)
- [x] Note what it represents (e.g., "ISO 8601 datetime string")
- [x] Fix remaining invalid types if any

## Priority 6: Security & Performance Standardization ⏳ NEEDS REVIEW
- [ ] Standardize warning format: `### ⚠️ SECURITY: [Specific Risk]`
- [ ] Include: Affected Fields, Risk, Mitigation
- [ ] Apply consistent format across all 8 documents
- [x] Ensure critical warnings are prominently displayed

## Priority 7: Field Selection Guidance ✅ COMPLETED (2025-01-05)
- [x] Create quick selection matrix
- [x] Add "When to use this field" prominently in each doc
- [x] Add "When NOT to use this field" section
- [x] Include decision trees where applicable

## Quick Wins (Immediate) ✅ MOSTLY COMPLETED
- [ ] Add document type badge (OLD/NEW format) if distinction needed
- [x] Ensure all type-returned values are valid
- [x] Verify all cross-links between documents work
- [x] Add "See Also" section to link related fields

## Effort Estimate
- Navigation Infrastructure: 2 hours
- Component Name Tables: 3 hours
- JSON Harmonization: 4 hours
- Cross-References: 2 hours
- Type System: 1 hour
- Security/Performance: 2 hours
- Field Selection: 2 hours
- **Total: ~16 hours**

## Success Criteria
- Any developer can navigate between related fields easily
- JSON examples can be copied and used directly
- Component naming is clear and consistent
- Security/performance warnings are impossible to miss
- Documents feel cohesive and interconnected

## Notes
- OLD format docs are comprehensive reference (average ~564 lines/field)
- NEW format docs follow template strictly (average ~705 lines/field)
- Both serve valuable purposes - unification should preserve strengths of each
- Educational JSON examples in OLD docs are intentional and valuable

## Completed Work (Initial Phase)
- ✅ All docs reorganized to template structure
- ✅ Designer limitations reviewed and corrected
- ✅ Technical accuracy verified
- ✅ Invalid types fixed (faims-core::Email, DateTime, Date → String)
- ✅ JSON syntax errors in NEW docs corrected
- ✅ Missing type-returned properties added

## Completed Work (Phase 1-2: 2025-01-05)
- ✅ Created LLM-optimized master index (field-type-index.md)
- ✅ Added concatenation boundaries and metadata to all 8 docs
- ✅ Implemented three-tier depth tagging system
- ✅ Built concatenation script (build-reference.sh)
- ✅ Generated reference.md (27,652 lines, 1MB)
- ✅ Added component name mapping tables to all docs
- ✅ Created type-system-reference.md
- ✅ Added "When to Use These Fields" selection guidance
- ✅ Fixed field status mischaracterizations:
  - RadioGroup: Removed incorrect deprecated status
  - DateTimeNow: Changed to RECOMMENDED (not discouraged)
  - DateTimePicker: Properly marked as discouraged for timezone-sensitive use
  - AdvancedSelect: Clarified as new feature (not unstable)
  - RichText: Removed false memory leak claims
- ✅ Created 8 maintenance shell scripts
- ✅ Committed and pushed to GitHub

## Current Status
- **Phase 1**: Navigation Infrastructure ✅ COMPLETED
- **Phase 2**: Component Standardization ✅ COMPLETED
- **Phase 3**: Cross-Field Integration ⏳ NOT STARTED
- **Phase 4**: Reference Consolidation ⏳ NOT STARTED