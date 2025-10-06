# Upstream Corrections List - 2025-10-05
## Root Cause Analysis for Quickstart QA Test

**Test Result**: CONDITIONAL PASS (68% compliance)
**Critical Issues Found**: 4 workflow-breaking errors
**Root Cause Categories**: Upstream gaps, prompt deficiencies, LLM limitations

---

## Root Cause Categorisation

### Category 1: Upstream Documentation Gaps (Reference.md Issues)

These errors occurred because reference.md lacks or inadequately documents key information:

#### Critical Impact

**Issue #1: Notebook Creation Workflow Not Documented**
- **Error**: Regenerated guide uses Templates → Create Template (incorrect)
- **Correct**: Notebooks → Create Notebook → Find in list → Actions → Open in Editor
- **Root Cause**: reference.md doesn't explicitly document the complete notebook creation workflow
- **Fix Required**: Add workflow documentation to dashboard section

**Issue #2: Notebook Placement Behaviour Undocumented**
- **Error**: No mention of new notebooks appearing at END of list
- **Root Cause**: UI behaviour pattern not documented in reference.md
- **Fix Required**: Add to UI interaction patterns documentation

**Issue #3: Two-URL Architecture Not Clear**
- **Error**: Regenerated omits Dashboard vs App URL distinction
- **Root Cause**: System architecture with two separate URLs not clearly explained
- **Fix Required**: Document in system architecture section

**Issue #4: Activation Workflow Location Ambiguous**
- **Error**: Regenerated incorrectly places activation in Editor's "Info" tab
- **Correct**: Activation occurs in mobile app (app.fieldmark.app)
- **Root Cause**: Activation architecture not clearly documented
- **Fix Required**: Add explicit activation workflow documentation

#### Major Impact

**Issue #5: Field Type Naming Inconsistency**
- **Error**: "Select one option" vs "Select Field" confusion
- **Root Cause**: reference.md uses JSON component names, not Designer UI names consistently
- **Fix Required**: Ensure designer-component-mapping.md is complete and referenced

**Issue #6: Form Settings Components Underdocumented**
- **Error**: Regenerated focuses only on HRID, omits other Form Settings
- **Root Cause**: Form Settings panel documentation may be incomplete
- **Fix Required**: Add comprehensive Form Settings documentation

**Issue #7: Save Behaviour and Dashboard Return Not Explicit**
- **Error**: Regenerated doesn't warn about Dashboard return after save
- **Root Cause**: Editor save behaviour not documented as explicit UI pattern
- **Fix Required**: Add to UI interaction patterns

**Issue #8: Section Creation Workflow Missing**
- **Error**: Regenerated skips section creation step
- **Root Cause**: Form → Section → Field hierarchy not clearly documented
- **Fix Required**: Add explicit workflow documentation

#### Minor Impact

**Issue #9: Annotation/Uncertainty Features Underemphasised**
- **Error**: Regenerated omits Fieldmark's unique annotation/uncertainty features
- **Root Cause**: These features not highlighted as "signature" Fieldmark capabilities
- **Fix Required**: Add "key features" section highlighting unique capabilities

**Issue #10: Offline-First Architecture Not Prominent**
- **Error**: Regenerated gives minimal offline explanation
- **Root Cause**: Offline-first design principle not emphasised in architecture docs
- **Fix Required**: Add architectural principles documentation

---

### Category 2: Generation Prompt Deficiencies

These errors could be prevented by more explicit prompt constraints:

#### Critical Impact

**Prompt Fix #1: Notebook-First Workflow Constraint**
```markdown
Add to prompt:
"CRITICAL CONSTRAINT: Users must create Notebooks (NOT Templates) first.
Workflow: Dashboard → Notebooks → Create Notebook → Fill dialog →
Find at END of list → Click notebook → Actions tab → Open in Editor."
```

**Prompt Fix #2: Activation Location Constraint**
```markdown
Add to prompt:
"CRITICAL CONSTRAINT: Notebook activation occurs in the mobile/data collection
app (app.fieldmark.app), NOT in the Editor or Dashboard. There is NO 'Active'
toggle in the Editor's Info tab."
```

**Prompt Fix #3: New Item Placement Constraint**
```markdown
Add to prompt:
"CRITICAL CONSTRAINT: New notebooks appear at the END of the list, not the
beginning. Always include guidance on pagination controls and search functionality."
```

**Prompt Fix #4: Dashboard Return Constraint**
```markdown
Add to prompt:
"CRITICAL CONSTRAINT: Clicking SAVE in the Notebook Editor returns the user to
the Dashboard. This is expected behaviour, not an error. Explicitly warn users."
```

#### Major Impact

**Prompt Fix #5: Two-URL Architecture Requirement**
```markdown
Add to prompt:
"Include explanation of Fieldmark's two-URL architecture:
- Dashboard URL (dashboard.fieldmark.app) - for designing notebooks
- App URL (app.fieldmark.app) - for collecting data
This distinction is critical for users to understand."
```

**Prompt Fix #6: Form Settings Completeness**
```markdown
Add to prompt:
"When documenting Form Settings, include ALL four settings:
1. Finish Button Behaviour
2. Layout Style
3. Summary Fields
4. Human-Readable ID Field
Do not focus only on HRID."
```

**Prompt Fix #7: Section Creation Requirement**
```markdown
Add to prompt:
"Include explicit section creation step before adding fields:
1. Name the section
2. Click + to create
3. Confirm section appears with badge
This step is mandatory in the workflow."
```

**Prompt Fix #8: Annotation/Uncertainty Feature Requirement**
```markdown
Add to prompt:
"Highlight Fieldmark's unique annotation and uncertainty features when
configuring choice fields. Provide example of how annotations capture
data quality nuances."
```

#### Minor Impact

**Prompt Fix #9: Offline-First Architecture Requirement**
```markdown
Add to prompt:
"Explain Fieldmark's offline-first architecture in the activation section.
Cover: local storage, background sync, orange vs green sync indicators."
```

**Prompt Fix #10: Screenshot Density Requirement**
```markdown
Add to prompt:
"Target 30-35 screenshot placeholders (approximately 1 every 20 lines).
Ensure every UI interaction has visual reference."
```

---

### Category 3: LLM Limitations (Accept or Workaround)

These issues represent inherent model limitations:

#### Pattern Recognition Limitations

**Limitation #1: Workflow Inference**
- **Issue**: LLM inferred Template-first workflow (plausible but incorrect)
- **Workaround**: Provide explicit workflow constraints in prompt (see Prompt Fix #1)
- **Status**: Addressable via prompt engineering

**Limitation #2: Feature Existence Hallucination**
- **Issue**: LLM created "Active (1)" toggle that doesn't exist
- **Analysis**: Model filled gaps in knowledge with plausible-sounding features
- **Workaround**: Explicit "does NOT exist" constraints in prompt
- **Status**: Addressable via negative constraints

**Limitation #3: UI Pattern Generalisation**
- **Issue**: LLM omitted modal overlay description, treating as inline
- **Analysis**: Model generalised UI patterns without specific architectural context
- **Workaround**: Provide explicit UI architecture patterns in reference.md
- **Status**: Addressable via upstream documentation

#### Acceptable Variations

**Variation #1: Screenshot Density**
- **Issue**: 16 screenshots vs 33 in gold standard
- **Analysis**: LLM made reasonable judgment about screenshot placement density
- **Status**: Accept with guideline adjustment (see Prompt Fix #10)

**Variation #2: Structural Organisation**
- **Issue**: Different section organisation (dedicated troubleshooting vs inline)
- **Analysis**: Both approaches valid; regenerated actually superior
- **Status**: Accept as improvement

**Variation #3: Field Type Naming**
- **Issue**: "Select Field" vs "Select one option"
- **Analysis**: Both terms recognisable; ambiguity from upstream docs
- **Status**: Accept pending upstream clarification

---

## Prioritised Fix List

### Priority 1: Critical (Workflow-Breaking) - 4 Issues

| # | Issue | Type | Fix Location | Impact | Effort |
|---|-------|------|--------------|--------|--------|
| 1 | Notebook creation workflow | Upstream gap | dashboard/ + workflow docs | CRITICAL | Medium |
| 2 | Activation location/workflow | Upstream gap | activation/ + architecture | CRITICAL | Medium |
| 3 | Notebook placement behaviour | Upstream gap | ui-interaction-patterns.md | CRITICAL | Low |
| 4 | Dashboard return on save | Upstream gap | ui-interaction-patterns.md | CRITICAL | Low |

**Estimated Impact**: These fixes will prevent 100% of workflow-blocking errors

---

### Priority 2: Major (Significant Usability) - 11 Issues

| # | Issue | Type | Fix Location | Impact | Effort |
|---|-------|------|--------------|--------|--------|
| 5 | Two-URL architecture | Upstream gap | system-architecture.md | MAJOR | Low |
| 6 | Form creation workflow | Upstream gap | editor-workflow.md | MAJOR | Low |
| 7 | Section creation workflow | Upstream gap | editor-workflow.md | MAJOR | Low |
| 8 | Annotation/uncertainty features | Upstream gap | field-types/ | MAJOR | Medium |
| 9 | Form Settings completeness | Upstream gap | form-settings.md | MAJOR | Low |
| 10 | Offline-first architecture | Upstream gap | architecture.md | MAJOR | Medium |
| 11 | Settings tab sync controls | Upstream gap | mobile-app-settings.md | MAJOR | Low |
| 12 | Field type naming consistency | Upstream gap | designer-component-mapping.md | MAJOR | Medium |
| 13 | Prompt: Notebook workflow constraint | Prompt deficiency | quickstart-generation-prompt.md | MAJOR | Low |
| 14 | Prompt: Activation constraint | Prompt deficiency | quickstart-generation-prompt.md | MAJOR | Low |
| 15 | Prompt: Pagination constraint | Prompt deficiency | quickstart-generation-prompt.md | MAJOR | Low |

**Estimated Impact**: These fixes will prevent ~80% of usability confusion

---

### Priority 3: Minor (Quality/Completeness) - 12 Issues

| # | Issue | Type | Fix Location | Impact | Effort |
|---|-------|------|--------------|--------|--------|
| 16 | UK spelling consistency | Gold standard error | quickstart-creation-and-collection.md | MINOR | Trivial |
| 17 | Screenshot density guideline | Prompt deficiency | quickstart-generation-prompt.md | MINOR | Trivial |
| 18 | Dashboard return warning | Prompt deficiency | quickstart-generation-prompt.md | MINOR | Low |
| 19 | Form Settings coverage | Prompt deficiency | quickstart-generation-prompt.md | MINOR | Low |
| 20 | Annotation feature requirement | Prompt deficiency | quickstart-generation-prompt.md | MINOR | Low |
| 21 | Offline architecture requirement | Prompt deficiency | quickstart-generation-prompt.md | MINOR | Low |
| 22 | Two-URL requirement | Prompt deficiency | quickstart-generation-prompt.md | MINOR | Low |
| 23 | Section creation requirement | Prompt deficiency | quickstart-generation-prompt.md | MINOR | Low |
| 24 | Sync icon visual explanation | Upstream gap | ui-elements.md | MINOR | Low |
| 25 | Modal overlay architecture | Upstream gap | ui-interaction-patterns.md | MINOR | Low |
| 26 | Notebook vs template distinction | Upstream gap | concepts.md | MINOR | Low |
| 27 | Time estimate realism | Both documents | Requires field testing | MINOR | N/A |

**Estimated Impact**: These fixes will improve polish and reduce minor confusion

---

## Implementation Recommendations

### Phase 1: Upstream Documentation (Priority 1 + Critical Priority 2)

**Timeline**: 1-2 sessions

**Files to Create/Update**:
1. `upstream/dashboard/notebook-creation-workflow.md` - Complete creation workflow
2. `upstream/architecture/activation-workflow.md` - Mobile app activation process
3. `upstream/architecture/two-url-system.md` - Dashboard vs App architecture
4. `upstream/ui-patterns/list-behaviours.md` - Item placement, pagination, search
5. `upstream/ui-patterns/editor-save-behaviour.md` - Save → Dashboard return
6. `upstream/editor/form-section-field-hierarchy.md` - Complete editor workflow

**Validation**: Re-run quickstart generation after these fixes

---

### Phase 2: Prompt Engineering (All Prompt Fixes)

**Timeline**: 1 session

**File to Update**: `production/prompts/quickstart-generation-prompt.md`

**Additions**:
1. Explicit workflow constraints (Prompt Fixes #1-4)
2. Architecture requirements (Prompt Fixes #5, #9)
3. Completeness requirements (Prompt Fixes #6-8)
4. Quality guidelines (Prompt Fix #10)

**Validation**: Re-run quickstart generation with updated prompt

---

### Phase 3: Secondary Documentation (Priority 2 Major)

**Timeline**: 1-2 sessions

**Files to Create/Update**:
1. `upstream/field-categories/annotation-uncertainty.md` - Feature deep-dive
2. `upstream/editor/form-settings-reference.md` - Complete settings documentation
3. `upstream/mobile-app/settings-sync-controls.md` - App settings reference
4. `upstream/architecture/offline-first-design.md` - Architecture principles

---

### Phase 4: Re-Test and Validate

**Timeline**: 1 session

**Process**:
1. Rebuild reference.md with all upstream fixes
2. Execute quickstart generation with updated prompt
3. Compare against gold standard
4. Measure improvement (target: 90%+ compliance)
5. Identify remaining gaps

**Success Criteria**:
- 0 critical errors
- ≤2 major errors
- Technical accuracy ≥90%

---

## Expected Outcomes

### If All Priority 1-2 Fixes Applied

**Projected Compliance**: 90-95%
**Critical Errors**: 0
**Major Errors**: 0-2
**Minor Errors**: 8-10

**Verdict**: PASS with minor curation needed

### Validation Metrics

After implementing fixes, regenerated guide should achieve:
- Technical Accuracy: 90%+ (vs 50% current)
- Structural Completeness: 85%+ (vs 75% current)
- Quality Indicators: 85%+ (vs 83% current)
- Overall: 90%+ (vs 68% current)

---

## Critical Insights from QA Test

### What Worked Well

1. **Structural improvements in regenerated version are genuine wins**
   - Dedicated troubleshooting section
   - Success checklist
   - Power user tips
   - Collaboration coverage

2. **Reference.md provides sufficient field-level information**
   - Component names accurate
   - Field types correct
   - Configuration options documented

3. **LLM follows prompt structure faithfully**
   - All required sections included
   - Tone and style matched
   - UK spelling maintained

### What Needs Improvement

1. **Workflow documentation is insufficient**
   - Multi-step processes not captured
   - Navigation paths missing
   - UI interaction sequences incomplete

2. **System architecture not explicit enough**
   - Two-URL system unclear
   - Activation location ambiguous
   - Offline-first design underexplained

3. **Prompt lacks negative constraints**
   - Doesn't say what NOT to do
   - Doesn't prevent plausible-but-wrong inferences
   - Doesn't block hallucinated features

### Key Learning

**The LLM generates excellent structure but needs explicit workflow knowledge.** Field-level documentation (types, names, configurations) is sufficient. Process-level documentation (workflows, navigation, sequences) needs significant enhancement.

---

## Files for Next Session

### To Create
1. `upstream/dashboard/notebook-creation-workflow.md`
2. `upstream/architecture/activation-workflow.md`
3. `upstream/architecture/two-url-system.md`
4. `upstream/ui-patterns/list-behaviours.md`
5. `upstream/ui-patterns/editor-save-behaviour.md`
6. `upstream/editor/form-section-field-hierarchy.md`

### To Update
1. `production/prompts/quickstart-generation-prompt.md` - Add explicit constraints
2. `production/human-facing/quickstart-creation-and-collection.md` - Fix US spellings
3. `upstream/references/designer-component-mapping.md` - Verify Select Field naming

---

## Conclusion

The QA test revealed that:
1. **Upstream docs excel at field-level detail** but lack workflow documentation
2. **Prompt needs explicit constraints** to prevent plausible inferences
3. **LLM structural decisions are often superior** to gold standard
4. **Hybrid approach recommended**: gold standard accuracy + regenerated structure

**Next Action**: Implement Priority 1 upstream fixes (4 critical workflow documentation gaps) and re-test.

---

*Analysis completed: 2025-10-05*
*Root causes: 10 upstream gaps, 10 prompt deficiencies, 7 LLM limitations*
*Total fixes required: 27 (4 critical, 11 major, 12 minor)*
*Expected improvement: 68% → 90%+ compliance*
