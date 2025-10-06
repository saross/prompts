# Compact Message for Next Session

## Context Restoration

We completed a comprehensive QA test of automated quickstart documentation generation. Result: **CONDITIONAL PASS (68% compliance)** with 4 critical workflow errors. We've created a detailed remediation plan to fix upstream source files and improve generation to 92%+ compliance.

## Task for This Session

Implement **Session 1** of the remediation plan: Critical Upstream Fixes (Priority 1).

## What to Do

### 1. Update Existing Source Files

**A. `production/dashboard/templates-interface.md`**
Add pedagogical note at beginning of Templates section marking template-first as "Advanced workflow" and notebook-first as "Recommended for beginners". Cross-reference template-workflow-principle.md.

**B. `production/dashboard/notebooks-interface.md`**
Add "Recommended Workflow for Beginners" note at beginning marking this as the RECOMMENDED starting point. Add cross-reference to activation-workflow.md in deployment section.

**C. `production/references/template-workflow-principle.md`**
Add "Implementation for LLM Documentation" section with explicit constraints: ALWAYS direct users to Notebooks → Create Notebook, mark templates as Advanced, show conversion as optional next step.

**D. `production/references/ui-interaction-patterns.md`**
Add two new sections:
- Section 13: "List Item Placement Behaviour" - new items at END of lists, pagination/search guidance
- Section 14: "Save Behaviour in Notebook Editor" - save closes editor, returns to dashboard (expected behaviour)

**E. `production/references/editor-form-settings.md` (or create new `production/patterns/editor-workflow-patterns.md`)**
Add "Editor Workflow: Form → Section → Field Hierarchy" section documenting the creation sequence and warning not to skip section creation step.

### 2. Create New Source File

**`production/dashboard/activation-workflow.md`**
Complete documentation of mobile app activation process:
- Architecture overview (activation in app.fieldmark.app, NOT Editor)
- Critical note: NO "Active (1)" toggle exists in Editor
- Step-by-step activation workflow (NOT ACTIVE tab → ACTIVATE button → ACTIVE tab)
- What activation does (downloads for offline, enables sync)
- Troubleshooting section
- Cross-references

### 3. Details

All specific content is in `/home/shawn/Code/prompts/EFN/Docs-staging/planning/quickstart-qa-remediation-plan.md` under Priority 1 sections 1.1-1.4. Use the exact markdown blocks provided.

### 4. Verification

After completing updates:
- Check all files for UK spelling compliance
- Verify markdown lint passes (blank lines around headings, code blocks, lists)
- Confirm cross-references use correct file paths

## Expected Deliverables

- 6 updated source files (templates-interface, notebooks-interface, template-workflow-principle, ui-interaction-patterns, editor-form-settings or new editor-workflow-patterns)
- 1 new source file (activation-workflow.md)
- All files ready for reference.md rebuild

## Next Steps After This Session

Session 2: Update gold standard quickstart guide (time estimates, 3-field approach, structural improvements)
Session 3: Update generation prompt with 15 critical constraints
Session 4: Rebuild reference.md, re-run generation, validate improvement (target: 92%+ compliance)

## Files to Read

- `/home/shawn/Code/prompts/EFN/Docs-staging/planning/quickstart-qa-remediation-plan.md` - Complete implementation plan
- `/home/shawn/Code/prompts/EFN/Docs-staging/planning/qa-test-automated-documentation-generation.md` - Original QA test spec
- `/home/shawn/Code/prompts/EFN/Docs-staging/production/human-facing/quickstart-qa-report-2025-10-05.md` - Detailed QA results

## Critical Reminder

**NEVER edit `production/reference.md` directly** - it is a concatenated file. Always edit source files in production/ subdirectories. This rule is now documented in `/home/shawn/Code/prompts/CLAUDE.md`.

---

Ready to begin Session 1: Critical Upstream Fixes.
