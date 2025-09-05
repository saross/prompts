# Field Documentation Unification TODO

## Goal
Make all 8 field documentation files read like chapters in the same book rather than separate publications.

## Current State
- **OLD Format** (4 docs): text-fields, select-choice-fields, datetime-fields, number-fields
- **NEW Format** (4 docs): display-field, location-fields, media-fields, relationship-field
- All follow same template structure ✅
- Technical accuracy verified ✅
- Designer limitations corrected ✅

## Priority 1: Create Navigation Infrastructure
- [ ] Create `field-type-index.md` master index file
- [ ] Add header to all 8 docs: `📚 Part of the [Fieldmark Field Type Documentation](../field-type-index.md)`
- [ ] Add footer to all 8 docs with links to: Field Index, Designer Limitations, Platform Behaviors

## Priority 2: Component Name Standardization
- [ ] Add "Component Name Mapping" table to all 8 documents
- [ ] Table format: Designer UI | JSON component-name | Code File | Namespace
- [ ] Use consistent terminology throughout each document
- [ ] Fix namespace references to actual values (faims-custom, formik-material-ui, mapping-plugin, qrcode)

## Priority 3: JSON Example Harmonization
- [ ] Decision: Keep educational style but add "Production Ready Examples" section
- [ ] Add valid, copy-paste JSON examples to all OLD format docs
- [ ] Ensure NEW format docs have educational context where needed
- [ ] Separate commentary from JSON blocks using "💡 **Note:**" format

## Priority 4: Cross-Reference Network
- [ ] Add "Related Field Types" section to each document
- [ ] Include "Within This Category" subsection
- [ ] Include "In Other Categories" subsection
- [ ] Add migration path suggestions between old/new approaches

## Priority 5: Type System Documentation
- [ ] Create unified type reference section
- [ ] Add to each document or create central reference
- [ ] Always show actual type (e.g., faims-core::String)
- [ ] Note what it represents (e.g., "ISO 8601 datetime string")
- [ ] Fix remaining invalid types if any

## Priority 6: Security & Performance Standardization
- [ ] Standardize warning format: `### ⚠️ SECURITY: [Specific Risk]`
- [ ] Include: Affected Fields, Risk, Mitigation
- [ ] Apply consistent format across all 8 documents
- [ ] Ensure critical warnings are prominently displayed

## Priority 7: Field Selection Guidance
- [ ] Create quick selection matrix
- [ ] Add "When to use this field" prominently in each doc
- [ ] Add "When NOT to use this field" section
- [ ] Include decision trees where applicable

## Quick Wins (Immediate)
- [ ] Add document type badge (OLD/NEW format) if distinction needed
- [ ] Ensure all type-returned values are valid
- [ ] Verify all cross-links between documents work
- [ ] Add "See Also" section to link related fields

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

## Completed Work
- ✅ All docs reorganized to template structure
- ✅ Designer limitations reviewed and corrected
- ✅ Technical accuracy verified
- ✅ Invalid types fixed (faims-core::Email, DateTime, Date → String)
- ✅ JSON syntax errors in NEW docs corrected
- ✅ Missing type-returned properties added