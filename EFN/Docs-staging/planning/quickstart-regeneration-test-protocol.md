# Quickstart Regeneration Test Protocol

**Protocol Version**: 1.0
**Created**: 2025-10-06
**Last Updated**: 2025-10-06
**Purpose**: Standardised testing procedure for automated quickstart guide generation quality assessment

---

## Purpose & Scope

### What This Protocol Tests

This protocol validates whether the LLM-first documentation system can automatically generate high-quality human-facing quickstart guides with minimal human intervention.

**Specifically tests**:
- Upstream documentation completeness (`reference.md`)
- Generation prompt effectiveness (`quickstart-generation-prompt.md`)
- Critical workflow constraint adherence
- Technical accuracy propagation
- Structural completeness
- Overall quality and usability

### When to Use This Protocol

- **After upstream documentation updates** - Validate fixes propagate to generated content
- **After prompt template revisions** - Test whether prompt improvements increase quality
- **Before major releases** - Ensure generated documentation meets production standards
- **Periodic quality checks** - Monitor system performance over time
- **Regression testing** - Verify new changes don't break existing quality

### What This Protocol Does NOT Test

- Screenshot quality or availability
- User testing or actual completion times
- Accessibility compliance
- Localisation accuracy beyond UK/Australian English spelling

---

## Prerequisites

### Required Files

Before starting the test, verify these files exist and are current:

| File | Location | Purpose |
|------|----------|---------|
| reference.md | `production/reference.md` | Source documentation for generation |
| Generation prompt | `production/prompts/quickstart-generation-prompt.md` | Instructions for LLM |
| Gold standard guide | `production/human-facing/quickstart-creation-and-collection.md` | Comparison baseline |
| Previous QA report | `production/human-facing/` or `archive/reports/` | Baseline metrics |

### Context Verification

Before beginning, document:

- **Date**: [YYYY-MM-DD]
- **reference.md build date**: Check file header or build log
- **reference.md stats**: Line count, file size, template marker count
- **Generation prompt version**: Check "Last Updated" in prompt file
- **Baseline comparison**: Which previous test/version are we comparing against?
- **Recent changes**: What upstream fixes or prompt updates were made since last test?

### Environment

- **LLM Model**: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929) or current production model
- **Context Window**: 200K tokens minimum
- **Generation Mode**: Single-pass, zero human intervention

---

## Phase 1: Generation (5-10 minutes)

### Step 1: Load Source Documentation

Read the following files into context:

1. **Primary source**: `production/reference.md`
   - This is the consolidated upstream documentation
   - Contains all field types, UI patterns, workflows, permissions

2. **Generation instructions**: `production/prompts/quickstart-generation-prompt.md`
   - Contains structure requirements
   - Critical workflow constraints
   - Style guidelines
   - Success criteria

### Step 2: Execute Generation

**CRITICAL**: Zero human intervention during generation. Do not:
- Provide mid-generation corrections
- Answer clarifying questions
- Offer additional context
- Guide structure or content choices

**Execution**:
1. Follow the generation prompt exactly as written
2. Generate complete quickstart guide in single pass
3. Include all required sections
4. Apply all critical workflow constraints

### Step 3: Save Raw Output

Save the generated content with standardised naming:

**File**: `production/human-facing/quickstart-regenerated-test-[YYYY-MM-DD].md`

**Example**: `quickstart-regenerated-test-2025-10-06.md`

**Important**:
- Save the raw, unedited output
- Do not fix typos, errors, or formatting issues
- Do not add missing sections
- The test evaluates the generation AS-IS

### Step 4: Document Generation Context

At the top of the generated file or in a separate log, record:

```markdown
<!-- Generation Context
Date: [YYYY-MM-DD]
reference.md build date: [date from file]
reference.md stats: [lines, size, markers]
Generation prompt version: [date from prompt file]
Model: [model name and version]
Context: [brief description of what changed since last test]
-->
```

---

## Phase 2: QA Assessment (30-45 minutes)

### Assessment Methodology

Compare the regenerated guide against the gold standard using a **22-metric framework** across three categories:

1. **Technical Accuracy** (8 metrics) - 36% of total score
2. **Structural Completeness** (8 metrics) - 36% of total score
3. **Quality Indicators** (6 metrics) - 27% of total score

### Scoring System

Each metric is scored as:
- **PASS** ✅ - Criterion fully met
- **PARTIAL PASS** ⚠️ - Criterion mostly met with minor issues
- **FAIL** ❌ - Criterion not met or major issues

**Overall Compliance Calculation**:
- PASS = 1.0 point
- PARTIAL PASS = 0.5 points
- FAIL = 0 points

**Total Score** = (Sum of points / 22 metrics) × 100%

---

### Category 1: Technical Accuracy Metrics (8 metrics)

#### 1.1 Field Component Names Match reference.md?

**Criteria**:
- Field types use Notebook Editor UI names (not JSON internal names)
- Examples: "FAIMS Text Field", "Select one option", "Take Photo"
- Parenthetical clarifications helpful: "Select one option (creates radio buttons)"

**Evidence to check**:
- Lines describing field addition in Step 3
- Field type selection instructions
- Field configuration sections

**Common errors**:
- Using JSON names like "TextField" instead of "FAIMS Text Field"
- Generic terms like "text box" without specific field type
- Incorrect field type for stated purpose (dropdown vs radio buttons)

---

#### 1.2 Dashboard → Editor Navigation Workflows Correct?

**Criteria**:
- Correct starting point: **Notebooks** (NOT Templates for beginners)
- Complete workflow: Notebooks → Create Notebook → Find in list → Actions → Open in Editor
- Acknowledges list placement: notebook appears at END of list
- Includes navigation aids: pagination, search bar

**Evidence to check**:
- Step 2: Create Your First Notebook
- Navigation instructions from Dashboard to Editor

**Critical errors** (automatic FAIL):
- Directs to Templates → Create Template
- Assumes Editor opens immediately after creation
- Skips notebook list navigation step
- Doesn't mention END of list placement

---

#### 1.3 UI Element Descriptions Match Screenshot Evidence?

**Criteria**:
- Specific locations: "top-right corner", "below the top bar", "bottom-left"
- Hierarchical positioning: "UNDO/REDO buttons below top bar, above tabs"
- Button/element identification: names, colors, icons described
- Screenshot placeholders positioned appropriately

**Evidence to check**:
- Step 2: Notebook Editor interface description
- Step 3: Field addition modal descriptions
- All UI element references throughout

**Partial pass indicators**:
- Generic descriptions: "click the button" without location
- Vague positioning: "on the screen" or "in the interface"
- Missing visual details: no colours, icons, or distinguishing features

---

#### 1.4 Modal Overlay Architecture (Not Separate Page Misconception)?

**Criteria**:
- Explicitly mentions "dialogue", "modal", or "dialogue that opens"
- Clarifies overlay vs separate page
- Users understand action happens in overlay context

**Evidence to check**:
- Step 3: "Add a field" dialogue description
- Any multi-step process involving overlays

**Common errors**:
- Describes modal as if it's a separate page or screen
- Uses ambiguous language: "you'll see a form" without context
- Omits any mention of dialogue/modal architecture

---

#### 1.5 Save Behaviour (Manual vs Auto-Save)?

**Criteria**:
- **Explicitly states**: "The Notebook Editor does not auto-save"
- **Warns**: Clicking SAVE returns user to Dashboard
- **Clarifies**: This is expected behaviour, not a bug
- **Explains**: How to resume editing (Open in Editor again)

**Evidence to check**:
- Save instructions in Step 2 or Step 3
- Warnings about save behaviour
- Troubleshooting section

**Critical errors** (automatic FAIL):
- Assumes auto-save without stating it
- Doesn't warn about Dashboard return
- Users would think Editor crashed when returned to Dashboard

---

#### 1.6 New Item Placement (End of List vs Beginning)?

**Criteria**:
- **Explicitly states**: "It will appear at the end of the notebook list"
- **Documents**: Pagination controls and how to use them
- **Documents**: Search bar functionality
- **Provides guidance**: How to find notebook with many existing items

**Evidence to check**:
- Step 2: Finding newly created notebook
- Navigation instructions after creation

**Critical errors** (automatic FAIL):
- No mention of list placement behaviour
- Assumes notebook appears at top/beginning
- Omits pagination or search guidance

---

#### 1.7 Field Selection Workflow (6-Tab Modal Dialogue)?

**Criteria**:
- Describes tab/category navigation in Add Field modal
- Mentions chevron controls (>) for accessing additional tabs
- Shows how to navigate to different field categories

**Evidence to check**:
- Step 3: Field addition instructions
- Navigating to CHOICE, MEDIA, or other field categories

**Partial pass indicators**:
- Describes field selection but omits tab navigation details
- Assumes all categories visible without scrolling/chevrons

---

#### 1.8 Collapsible Panel Interactions Described?

**Criteria**:
- Describes expand/collapse mechanism: "click on the grey bar"
- Consistent terminology throughout
- Users understand how to show/hide field configuration panels

**Evidence to check**:
- Step 3: Field configuration sections
- Instructions to expand/collapse fields

**Partial pass indicators**:
- Describes expansion but not collapse
- Inconsistent terminology (sometimes "click arrow", sometimes "click bar")

---

### Category 2: Structural Completeness Metrics (8 metrics)

#### 2.1 All Required Sections from Template Present?

**Required sections** (from generation prompt):
1. What You'll Achieve
2. Before You Start (with Quick Terms)
3. Step 1: Access Your Dashboard
4. Step 2: Create Your First Notebook
5. Step 3: Add Your Fields
6. Step 4: Activate and Test Your Notebook
7. Success Checklist
8. Troubleshooting {optional-reference}
9. Next Steps / What's Next
10. Get Help / Keep Learning

**Scoring**:
- PASS: All 10 sections present with appropriate content
- PARTIAL: 8-9 sections present, or sections present but under-developed
- FAIL: <8 sections, or critical sections missing (Steps 1-4)

---

#### 2.2 "✓ You'll Know It Worked When..." Validation Blocks?

**Criteria**:
- Present after each major step (minimum 4: Steps 1-4)
- Use checkbox format: `- [ ]` for interactive tracking
- List 3-5 concrete, observable success indicators
- Focus on what users SEE, not just what happens

**Evidence to check**:
- End of Step 1, 2, 3, 4
- After sub-steps within Step 3 (field additions)

**Scoring**:
- PASS: 6+ validation blocks, checkbox format, concrete criteria
- PARTIAL: 4-5 validation blocks, or present but not checkbox format
- FAIL: <4 validation blocks, or vague/unobservable criteria

---

#### 2.3 Screenshot Placeholders Properly Positioned?

**Criteria**:
- Screenshot placeholders every 3-5 steps or at each major action
- Proper markdown syntax or placeholder format
- Detailed descriptions of what should be shown
- Positioned logically (after describing the action, before validation)

**Evidence to check**:
- Count of screenshot placeholders (baseline: 33)
- Distribution throughout document
- Quality of descriptions

**Scoring**:
- PASS: 25+ placeholders, well-distributed, detailed descriptions
- PARTIAL: 15-24 placeholders, or uneven distribution
- FAIL: <15 placeholders, or generic descriptions

---

#### 2.4 Success Criteria Observable and Concrete?

**Criteria**:
- Success indicators are visual/observable
- Specific UI elements referenced: "You see your name in the bottom-left user menu"
- Avoids abstract criteria: "The system is ready" (not observable)
- Users can verify success without technical knowledge

**Evidence to check**:
- All "You'll Know It Worked When..." sections
- Validation checkpoints throughout

**Scoring**:
- PASS: All criteria concrete and observable
- PARTIAL: Most concrete, some abstract
- FAIL: Many abstract or unverifiable criteria

---

#### 2.5 Pro Tips and Warnings Included?

**Criteria**:
- Minimum 10 tips/warnings throughout guide
- Mix of encouraging tips (✨ Pro Tip) and preventative warnings (⚠️)
- Contextually relevant to the step
- Includes critical warnings (e.g., HRID configuration, save behaviour)

**Evidence to check**:
- Count of tip/warning callouts
- Critical warnings present (HRID, save behaviour, mobile vs desktop)

**Scoring**:
- PASS: 12+ tips/warnings, includes all critical warnings
- PARTIAL: 8-11 tips/warnings, or missing 1 critical warning
- FAIL: <8 tips/warnings, or missing multiple critical warnings

---

#### 2.6 Troubleshooting Sections Present?

**Criteria**:
- Dedicated troubleshooting section at end marked `{optional-reference}`
- Covers 7 most common issues (from generation prompt)
- Problem statement + solution format
- Issues include: notebook not in list, Editor closed after save, records show rec_xxxxx, etc.

**Evidence to check**:
- Troubleshooting section presence and placement
- Coverage of common issues
- Problem-solution format clarity

**Scoring**:
- PASS: Dedicated section, 7+ issues covered, clear solutions
- PARTIAL: Section present but <7 issues, or solutions unclear
- FAIL: No dedicated section, or scattered troubleshooting only

---

#### 2.7 Time Estimates Realistic (25-30 min)?

**Criteria**:
- Title states: "Your First Notebook in 25-30 Minutes"
- Step estimates sum to 21-33 minutes
- Step 1: 3-5 min, Step 2: 5-8 min, Step 3: 8-12 min, Step 4: 5-8 min
- Accounts for first-time user orientation, reading, trial and error

**Evidence to check**:
- Title
- Individual step time estimates
- Overall completion time claim

**Scoring**:
- PASS: Title says 25-30 min, step totals align
- PARTIAL: Title says 25-30 min but step totals misaligned (e.g., sum to 15-20 or 35-40)
- FAIL: Title says 15 min or other unrealistic estimate

---

#### 2.8 Error Handling and Troubleshooting Included?

**Criteria**:
- Multi-layered approach:
  - **Preventative**: Warnings before common mistakes
  - **Detective**: Validation blocks for immediate feedback
  - **Corrective**: Troubleshooting section for recovery
- Covers workflow-breaking errors: HRID, activation, pagination
- Solutions are actionable and specific

**Evidence to check**:
- Presence of all three error-handling layers
- Coverage of critical failure points
- Quality of solutions

**Scoring**:
- PASS: All three layers present, covers critical errors
- PARTIAL: Two layers present, or incomplete coverage
- FAIL: One or no layers, or critical errors not addressed

---

### Category 3: Quality Indicators (6 metrics)

#### 3.1 Confidence-Building Language Present?

**Criteria**:
- Encouraging tone throughout
- Celebration at milestones: "Great!", "Fantastic!", "Congratulations!"
- Acknowledges achievements: "You've just...", "This is a major milestone!"
- Minimum 8 instances of celebratory language

**Evidence to check**:
- Opening welcome
- After each major step completion
- Final success message

**Scoring**:
- PASS: Enthusiastic, supportive language at all milestones (8+ instances)
- PARTIAL: Some celebration but inconsistent (4-7 instances)
- FAIL: Dry, technical tone throughout (<4 instances)

---

#### 3.2 Grade 8-9 Readability Maintained?

**Criteria**:
- Short sentences (average <20 words)
- Active voice predominates
- Common vocabulary, technical terms defined on first use
- Analogies for complex concepts
- Progressive disclosure (simple → complex)

**Evidence to check**:
- Sample paragraphs from each major section
- Technical term definitions
- Use of analogies (e.g., notebook/form/section/field hierarchy)

**Scoring**:
- PASS: Consistently accessible language, all terms defined
- PARTIAL: Mostly accessible, some jargon or undefined terms
- FAIL: Complex language, assumes technical knowledge

---

#### 3.3 Encouragement and Celebration at Milestones?

**Criteria**:
- Every major step ends with celebration
- Progress checks include encouragement: "You're doing great!"
- Final completion message celebrates achievement
- Emoji usage appropriate (sparingly): 🎉, 🎯, ✨

**Evidence to check**:
- End of Steps 1, 2, 3, 4
- Progress check callouts
- Final success section

**Scoring**:
- PASS: Celebration at all 4 major milestones + final
- PARTIAL: Celebration at 2-3 milestones
- FAIL: Minimal or no celebration language

---

#### 3.4 UK/Australian English Spelling?

**Criteria**:
- Consistent UK/Australian spelling throughout
- Common terms: behaviour, colour, organisation, customise, centre, analyse
- No US spellings: behavior, color, organization, customize, center, analyze

**Evidence to check**:
- Scan for common variant words
- Check field configuration sections (behaviour, customise)
- Check "Before You Start" and "Next Steps" sections

**Scoring**:
- PASS: 100% UK/Australian spelling, zero US spellings
- PARTIAL: 1-3 instances of US spelling
- FAIL: 4+ instances of US spelling, or inconsistent

---

#### 3.5 Overall Polish and Professionalism?

**Criteria**:
- Consistent formatting (headings, lists, code blocks)
- Proper markdown syntax throughout
- Logical flow and progressive disclosure
- Visual hierarchy clear (headings, blockquotes, lists)
- No typos or grammatical errors
- Screenshot integration smooth

**Evidence to check**:
- Overall document structure
- Markdown compliance
- Logical section flow
- Attention to detail

**Scoring**:
- PASS: Professional-grade, production-ready
- PARTIAL: Minor formatting issues or inconsistencies
- FAIL: Multiple formatting errors, poor structure, or many typos

---

#### 3.6 Time Estimates (Shared with 2.7)

This metric is scored in Structural Completeness 2.7. Count it once to avoid double-counting.

---

## Phase 3: Reporting (15-20 minutes)

### Generate QA Report

Create: `production/human-facing/quickstart-qa-regeneration-test-[YYYY-MM-DD].md`

### Report Structure

```markdown
# QA Regeneration Test: Quickstart Guide

## Test Metadata
- **Date**: [YYYY-MM-DD]
- **Analyst**: [Your name or "Claude Code"]
- **Document Tested**: quickstart-regenerated-test-[YYYY-MM-DD].md
- **Baseline Comparison**: [Which previous test/version]
- **Context**: [What changed since last test]

## Executive Summary

**VERDICT**: [PASS / CONDITIONAL PASS / FAIL] ([XX]% Compliance)

[2-3 paragraph summary of findings]

**Key Metrics**:
- Technical Accuracy: [XX]% ([X]/8 metrics passed)
- Structural Completeness: [XX]% ([X]/8 metrics passed)
- Quality Indicators: [XX]% ([X]/6 metrics passed)
- Overall Compliance: [XX]%

**Critical Finding**: [Most important discovery - errors resolved or still present]

---

## Metric-by-Metric Analysis

### Technical Accuracy Metrics

#### ✅/⚠️/❌ 1. Field Component Names Match reference.md?

**Evidence**: [Quote lines from regenerated guide]

**Analysis**: [Detailed assessment against criteria]

**Verdict**: [PASS / PARTIAL PASS / FAIL]

[Repeat for all 8 technical metrics...]

### Structural Completeness Metrics

[Repeat for all 8 structural metrics...]

### Quality Indicator Metrics

[Repeat for all 6 quality metrics...]

---

## Critical Issues

### [Issue Title]

**Location**: Lines [X-Y] in regenerated guide

**Error**: [Description of what's wrong]

**Impact**: [Workflow-breaking / Major accuracy issue / Minor cosmetic]

**Recommendation**: [How to fix - upstream doc change or prompt refinement]

[Repeat for each critical issue...]

---

## Comparison to Baseline

| Metric Category | Baseline | Current | Change |
|-----------------|----------|---------|--------|
| Technical Accuracy | [XX]% | [XX]% | [+/-X]% |
| Structural Completeness | [XX]% | [XX]% | [+/-X]% |
| Quality Indicators | [XX]% | [XX]% | [+/-X]% |
| Overall Compliance | [XX]% | [XX]% | [+/-X]% |

**Improvements**:
- [List specific improvements from baseline]

**Regressions**:
- [List any new issues not in baseline]

---

## Recommendations

### Priority 1: Critical (Blocks Production)
1. [Specific fix needed]
2. [Specific fix needed]

### Priority 2: Major (Significant Impact)
1. [Specific fix needed]
2. [Specific fix needed]

### Priority 3: Minor (Polish)
1. [Specific fix needed]
2. [Specific fix needed]

---

## Verdict Details

**PASS Criteria**: ≥90% compliance, all critical errors resolved
**CONDITIONAL PASS Criteria**: 70-89% compliance, critical errors resolved, minor issues remain
**FAIL Criteria**: <70% compliance, or critical errors present

**This Test**: [XX]% compliance → [VERDICT]

**Ready for Production?**: [Yes / No / With minor edits]

---

**Report compiled**: [YYYY-MM-DD]
**Analysis duration**: [X minutes]
**Total deviations identified**: [X] ([Y] critical, [Z] major, [W] minor)
```

---

## Success Criteria & Verdict Thresholds

### PASS (≥90% compliance)

**Criteria**:
- Overall score: 90%+ (≥20/22 metrics pass)
- Technical Accuracy: ≥95% (≥7.5/8 metrics)
- Structural Completeness: ≥90% (≥7/8 metrics)
- Quality Indicators: ≥83% (≥5/6 metrics)
- Zero critical workflow-breaking errors

**Interpretation**:
- Guide is production-ready with minimal edits (<10% of content)
- Automated generation validated as effective
- Only minor stylistic adjustments needed
- Can proceed to screenshot integration and publication

**Next Steps**:
- Document successful generation process
- Create workflow documentation for automated generation
- Use as template for other human-facing documentation

---

### CONDITIONAL PASS (70-89% compliance)

**Criteria**:
- Overall score: 70-89% (16-19/22 metrics pass)
- All 4 critical workflow constraints met:
  - ✅ Notebook-first workflow (NOT template-first)
  - ✅ Mobile app activation (NOT Editor toggle)
  - ✅ List placement documented (END of list)
  - ✅ Save behaviour documented (returns to Dashboard)
- Minor to moderate accuracy issues present
- Structural issues addressable

**Interpretation**:
- System validated with improvements needed
- Critical errors resolved (major achievement)
- Moderate curation required (10-30% of content)
- Targeted upstream fixes or prompt refinements identified

**Next Steps**:
- Implement recommended fixes (upstream docs or prompt)
- Re-test to validate improvements
- Document lessons learned
- Iterate toward PASS threshold

---

### FAIL (<70% compliance)

**Criteria**:
- Overall score: <70% (<16/22 metrics pass)
- OR any critical workflow-breaking errors present:
  - ❌ Template-first workflow directed
  - ❌ Non-existent activation toggle referenced
  - ❌ List placement not documented
  - ❌ Save behaviour not documented
- Significant structural gaps
- Extensive rework required (>30% of content)

**Interpretation**:
- Systemic documentation issues remain
- Significant upstream documentation overhaul needed
- Generation prompt may need fundamental redesign
- Automated generation not yet viable for production

**Next Steps**:
- Comprehensive root cause analysis
- Identify critical documentation gaps
- Plan systematic documentation review
- Define improvement roadmap with milestones
- Re-test after major overhaul

---

## Deliverables Checklist

After completing all three phases, verify:

- [ ] **Regenerated guide saved**: `production/human-facing/quickstart-regenerated-test-[YYYY-MM-DD].md`
- [ ] **Generation context documented**: Model, date, reference.md version, changes
- [ ] **QA report created**: `production/human-facing/quickstart-qa-regeneration-test-[YYYY-MM-DD].md`
- [ ] **All 22 metrics assessed**: With evidence, analysis, and verdict
- [ ] **Overall compliance calculated**: Percentage and verdict
- [ ] **Comparison to baseline**: Improvements and regressions identified
- [ ] **Recommendations prioritised**: Critical, Major, Minor categories
- [ ] **Next steps documented**: Based on verdict

### File Management

**If test is PASS or shows improvement**:
- Keep newest QA report in `production/human-facing/`
- Move previous QA report to `archive/reports/`
- Keep regenerated guide in `production/human-facing/` for reference

**If test shows regression**:
- Save QA report to `archive/reports/` immediately
- Save regenerated guide to `archive/reports/` (not production)
- Document what went wrong in planning notes

---

## Version History

### Protocol Version 1.0 (2025-10-06)

**Created by**: Claude Code (Sonnet 4.5)

**Based on**:
- Baseline QA test (2025-10-05): 68% compliance, 4 critical errors
- Effectiveness assessment (2025-10-02): 8.5/10 quality score
- Remediation cycle (2025-10-05 to 2025-10-06): Sessions 1-3

**Test Results Using This Protocol**:
- [To be added as tests are performed]

**Changes in This Version**:
- Initial protocol creation
- Established 22-metric framework
- Defined PASS/CONDITIONAL/FAIL thresholds at 90%/70%
- Incorporated Critical Workflow Constraints validation
- Added detailed scoring methodology

**Known Limitations**:
- Does not test actual user completion (requires user testing)
- Screenshot quality assessment is limited
- Accessibility compliance not formally tested
- No automated metric calculation (manual assessment required)

---

## Notes for Protocol Users

### For LLM Sessions

When using this protocol in a new session:

1. **Read this protocol completely** before beginning
2. **Verify prerequisites** - all required files present and current
3. **Document context** - what changed since last test
4. **Follow phases sequentially** - do not skip steps
5. **Zero intervention in Phase 1** - critical for valid test
6. **Be thorough in Phase 2** - assess all 22 metrics with evidence
7. **Compare to baseline in Phase 3** - show improvement/regression trends

### For Human Reviewers

When manually executing this protocol:

1. **Allow sufficient time** - Plan for 60-90 minutes total
2. **Use comparison tools** - Diff tools help identify changes
3. **Reference baseline** - Keep previous QA report open
4. **Document evidence** - Quote lines, provide specific examples
5. **Be objective** - Score against criteria, not expectations
6. **Consider context** - Recent changes may explain issues

### For Continuous Improvement

This protocol should evolve:

- Update metrics based on new learnings
- Refine criteria as system matures
- Adjust thresholds based on capability improvements
- Add new test dimensions as needed
- Track trends across multiple test iterations

---

*This protocol represents best practices for automated documentation generation quality assurance as of October 2025. Update as system capabilities and requirements evolve.*
