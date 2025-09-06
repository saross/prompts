# TODO: V05 Documentation Improvements

## Phase 3 Trial Update (2025-01-06)
- ✅ Successfully completed trial consolidation of field-selection-guide.md
- ✅ Consolidated 3 documents into 1 comprehensive guide (408 lines)
- ✅ All 8 field documents updated with cross-references to new guide
- ✅ Field-specific anchors working (#text-fields, #number-fields, etc.)
- Next: Apply same pattern to remaining cross-field and reference docs

## Early Docs Improvements (text/number/datetime/select)
*Located in: `/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/`*

### Structural Changes
- [x] ✅ Move Field Selection Guide to position #3 in text-fields-v05.md (Added as "When to Use These Fields")
- [x] ✅ Move Field Selection Guide to position #3 in number-fields-v05.md (Added as "When to Use These Fields")
- [x] ✅ Move Field Selection Guide to position #3 in datetime-fields-v05.md (Added as "When to Use These Fields")
- [x] ✅ Move Field Selection Guide to position #3 in select-choice-fields-v05.md (Added as "When to Use These Fields")
- [ ] Add Critical Security Risks section to text-fields-v05.md
- [ ] Add Critical Security Risks section to number-fields-v05.md
- [ ] Add Critical Security Risks section to datetime-fields-v05.md
- [ ] Add Critical Security Risks section to select-choice-fields-v05.md

### Content Updates
- [ ] Standardize date suffixes from (2025-08) to (2025-01) in all early docs
- [ ] Consolidate repetitive examples in early docs
- [ ] Extract more universal patterns to reference docs from early docs
- [ ] Improve cross-referencing between related fields

## Recent Docs Improvements (media/location/relationship/display)
*Located in: `/home/shawn/Code/prompts/EFN/Docs-staging/`*

### media-fields-v05.md (789 lines)
- [x] ✅ Add Designer Component Mapping section (COMPLETED 2025-01-05)
- [ ] Add 15-20 JSON examples:
  - [ ] FileUploader with size validation patterns
  - [ ] TakePhoto with conditional capture
  - [ ] Complex media workflow examples
  - [ ] Error recovery patterns
- [ ] Expand platform behaviors:
  - [ ] iOS HEIC conversion details
  - [ ] Android storage permission scenarios
  - [ ] Web browser file size limits
  - [ ] PWA offline capabilities
- [ ] Enhance troubleshooting:
  - [ ] Memory exhaustion scenarios
  - [ ] Permission recovery workflows
  - [ ] Sync failure patterns

### location-fields-v05.md (825 lines)
- [x] ✅ Add Designer Component Mapping section (COMPLETED 2025-01-05)
- [ ] Add 15-20 JSON examples:
  - [ ] Complex MapFormField configurations
  - [ ] TakePoint accuracy validation attempts
  - [ ] Conditional location capture
  - [ ] Multi-location workflows
- [ ] Expand performance metrics:
  - [ ] GPS acquisition times by platform
  - [ ] Map tile cache sizes
  - [ ] Vertex count impact measurements
  - [ ] Battery drain quantification
- [ ] Add migration scenarios:
  - [ ] Converting between TakePoint/MapFormField
  - [ ] Handling legacy coordinate formats
  - [ ] Offline map migration

### relationship-field-v05.md (584 lines)
- [x] ✅ Add Designer Component Mapping section (COMPLETED 2025-01-05)
- [ ] Add 20-25 JSON examples:
  - [ ] Complex vocabulary pair configurations
  - [ ] Nested relationship structures
  - [ ] Conditional relationship displays
  - [ ] Performance optimization patterns
- [ ] Expand platform behaviors:
  - [ ] Mobile selection interface details
  - [ ] Offline sync timing scenarios
  - [ ] Touch target measurements
- [ ] Enhance error messages section:
  - [ ] Reciprocal update failures
  - [ ] Orphan detection messages
  - [ ] Performance threshold warnings

### display-field-v05.md (571 lines)
- [x] ✅ Add Designer Component Mapping section (COMPLETED 2025-01-05)
- [ ] Add 15-20 JSON examples:
  - [ ] Complex markdown structures
  - [ ] Conditional display patterns
  - [ ] Multi-section instructions
  - [ ] Performance-optimized content
- [ ] Expand memory leak details:
  - [ ] Quantify accumulation rates
  - [ ] Platform-specific impacts
  - [ ] Mitigation strategies
- [ ] Add accessibility workarounds:
  - [ ] Screen reader alternatives
  - [ ] ARIA attribute injection attempts
  - [ ] RTL text handling

### All Recent Docs
- [ ] Standardize date suffixes to (2025-01) consistently
- [x] ✅ Ensure all have Designer Component Mapping sections (COMPLETED 2025-01-05)
- [ ] Add 5-10 migration warning scenarios each
- [ ] Expand Quick Diagnosis Tables with 5-10 more rows
- [x] ✅ Add cross-references to field-selection-guide.md in all field docs (COMPLETED 2025-01-06)

## Priority Order
1. **Quick Fixes** (1-2 hours)
   - Add missing Designer Component Mapping sections
   - Standardize date suffixes
   - Fix section ordering in early docs

2. **Content Enhancement** (3-4 hours)
   - Add JSON examples to recent docs
   - Expand platform behaviors
   - Enhance troubleshooting sections

3. **Full Alignment** (5-6 hours)
   - Complete all structural fixes
   - Match content depth across docs
   - Optimize cross-references

## Notes
- Context running low (12% remaining)
- Focus on recent docs first as they need more work
- Early docs improvements can wait for new session
- Consider compacting conversation after recent docs improvements