# Plan Refinement - 2025-10-04
**Context**: Post-quickstart pilot review and strategy adjustment

---

## Key Clarification: Template Designer = Notebook Editor

### User Feedback

**Issue Identified**: Documentation plan was treating Template Designer as a separate major UI component requiring full screenshot documentation.

**Clarification**:
- Template Designer **uses the exact same interface** as Notebook Editor
- Only difference: Save target (template vs notebook)
- Template creation is an **advanced feature**, not primary workflow

### Actual Template Workflows

**Most Common (95% of users)**:
1. Create notebook directly → Use it → Convert to template later
2. Dashboard → Select notebook → Actions → "Convert to Template"

**Less Common (Advanced users)**:
1. Templates interface → Create Template → Opens Notebook Editor → Design → Save as template

**Implication**: Don't duplicate Notebook Editor UI documentation for Template Designer.

---

## Corrected Tier 1 Structure

### BEFORE (Incorrect)
1. Dashboard Overview
2. **Template Designer** ← Treated as major component
3. Notebooks Interface

### AFTER (Corrected)
1. Dashboard Overview
2. **Notebook Editor - Complete** ← One comprehensive editor documentation
3. **Data Collection App - Complete** ← "Notebooks Interface" in user terms

---

## Documentation Strategy Adjustment

### Notebook Editor Documentation {essential}

**Scope**: Complete UI documentation of the editor interface
- All field types and configuration patterns
- Advanced features (conditional logic, validation, relationships)
- Form preview and testing
- Metadata configuration (INFO tab)

**Reuse Strategy**:
- Quickstart already documented: Basic field addition, form/section creation
- Add to this: Advanced field types, complex configurations, preview features

**Template Designer Reference**:
- Screenshot: Template list and "Create Template" button
- Note: "Template Designer uses the Notebook Editor interface. See Notebook Editor documentation for UI details."
- Screenshot: Template-to-notebook creation workflow
- Estimated addition: ~2-3 pages instead of 15-20

---

## Time and Effort Recalculation

### Original Estimate (Incorrect)
- Template Designer: 12-15 hours
- Total Tier 1: ~24-30 hours

### Corrected Estimate
- Template workflow documentation: 2-3 hours
- **Time saved**: ~10-12 hours
- **Corrected Tier 1 total**: ~14-18 hours

---

## Reference Documentation

**Principle documented in**: `/production/references/template-workflow-principle.md`

**Key points**:
- Templates are advanced/optional, not primary workflow
- Template Designer = Notebook Editor (same UI)
- Don't duplicate documentation
- Reference Notebook Editor when discussing Template Designer

---

## Updated Interface Priority

### Tier 1 (Core - 2-4 weeks)
1. Dashboard Overview (navigation, home screen)
2. Notebook Editor Complete (all features, reused for Template Designer)
3. Data Collection App Complete (full data collection workflows)

### Tier 2 (Administration - 4-6 weeks)
4. Users Interface (including API tokens)
5. Teams Interface (including virtual roles)
6. Settings & Configuration

### Tier 3 (Advanced - 6-8 weeks)
7. Map Interface
8. Relationship Fields (complex field type)
9. Export & Data Management
10. Conflict Resolution & Sync

---

## Action Items

- [x] Document template workflow principle
- [x] Update master strategy Tier 1 structure
- [x] Create this refinement note
- [ ] Review with user before proceeding
- [ ] Update integration plan to reflect corrected structure
- [ ] Begin Phase 1 implementation after approval

---

## Lesson Learned

**For LLM Documentation Authors**: Don't assume "best practice" workflow equals "actual user workflow".

In Fieldmark:
- Users create notebooks first (practical, immediate need)
- Templates come later (optimization, reuse)

Not the reverse:
- ~~Templates first (theoretical best practice)~~
- ~~Notebooks second (deployment)~~

This reflects actual human behavior: solve immediate problem → optimize later.
