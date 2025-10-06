# Human-Facing Documentation Standards

**Created**: 2025-01-08
**Last Updated**: 2025-10-06
**Purpose**: Standards and templates for creating effective human-facing documentation
**Based on**: Lessons learned from quickstart guide development, screenshot verification pilot, effectiveness assessment, and October 2025 remediation cycle

## Key Learnings from Quickstart Guide

### What LLMs Do Well
- Structure and logical flow
- Consistent terminology
- Encouraging tone
- Comprehensive coverage
- Progressive disclosure of concepts
- Confidence building through celebration

### What LLMs Miss (Without Screenshot Verification & Architecture Documentation)
- **Navigation specificity** - WHERE buttons are located
- **Visual continuity** - Assuming users remember previous screens
- **Cognitive load** - Too many concepts at once (field count, step complexity)
- **Platform variations** - Mobile vs desktop differences
- **Success validation** - How users know they succeeded (checkbox format more interactive)
- **Actual UI workflows** - Assumptions about drag-and-drop, auto-save, panel locations
- **Modal dialogues vs panels** - Interface interaction patterns
- **Realistic time estimates** - Optimistic assumptions about completion time (15min vs 25-30min reality)
- **Critical workflow constraints** - Architectural truths about where actions occur (e.g., activation in mobile app, NOT Editor)
- **List placement behaviour** - Assuming new items appear at top when they appear at END
- **Save behaviour** - Assuming auto-save when manual save returns to Dashboard

### Critical Discovery: Screenshot Verification is Essential

**2025-10-02 Pilot Findings**:
- Initial quickstart had systemic errors about UI workflows (assumed drag-and-drop when actual UI uses modal dialogues)
- LLM made incorrect assumptions about auto-save, panel locations, and navigation patterns
- **Solution**: Screenshot-driven iterative development where each workflow step is verified against actual UI
- **Outcome**: 8.5/10 effectiveness score after screenshot verification vs. likely 5/10 with assumptions

### Lessons from October 2025 Quickstart Remediation

**Context**: QA testing revealed 4 critical workflow errors in regenerated quickstart guide (68% baseline compliance). Three-session remediation cycle achieved 95% compliance with all critical errors resolved.

**Key Discoveries**:

1. **Critical Workflow Constraints Must Be Explicit**
   - LLMs will assume common patterns even when actual system differs
   - Example: Assumed template-first workflow when system requires notebook-first for beginners
   - Example: Assumed activation in Editor when it actually occurs in mobile app
   - **Solution**: Document architectural truths as explicit constraints in prompt (see `quickstart-generation-prompt.md` lines 94-135)

2. **Realistic Time Estimates Essential for Trust**
   - Initial estimate: 15 minutes (optimistic)
   - QA-tested reality: 25-30 minutes for first-time users
   - **Impact**: Unrealistic estimates damage user confidence and trust
   - **Solution**: Test with actual users or account for: orientation time, screenshot reference, pagination navigation, reading comprehension, trial and error

3. **Dramatic Visual Warnings for Critical Mistakes**
   - Standard warnings insufficient for "#1 user mistakes" (e.g., HRID configuration)
   - **Solution**: Before/after visual comparisons in blockquotes
   - Example: Show "❌ rec_a7f3b2c1" vs "✅ Ancient Temple Site" side-by-side
   - **Impact**: Prevents most common configuration error

4. **Checkbox Validation Format More Effective**
   - Changed from bullet points to `- [ ]` checkbox format for validation blocks
   - **Benefits**: Interactive progress tracking, self-paced learning, clearer completion markers
   - Users can physically check off accomplishments

5. **Dedicated Troubleshooting Sections**
   - Inline troubleshooting clutters tutorial flow
   - **Solution**: Dedicated section at end marked `{optional-reference}`
   - Cover 7 most common issues with problem statement + solution format
   - More discoverable than scattered inline tips

6. **Field Count Optimisation for Cognitive Load**
   - Reduced from 5 fields to 3 fields while maintaining pedagogical coverage
   - **Criteria**: Cover major field categories (text, choice, media) with minimum examples
   - **Impact**: 40% reduction in tutorial complexity, faster completion, maintained learning outcomes

7. **Multi-Layered Error Prevention Strategy**
   - **Preventative**: Warnings before common mistakes
   - **Detective**: Validation blocks for immediate feedback ("You'll Know It Worked When...")
   - **Corrective**: Troubleshooting section for recovery
   - All three layers required for robust error handling

8. **Progress Check Callouts Mid-Step**
   - Not just end-of-step validation
   - Add "> ✓ **Progress check**: You should now see..." during long procedures
   - Catches errors early before users invest more time

9. **Upstream Documentation Dependency Critical**
   - Cannot fix documentation errors in quickstart guide alone
   - Must fix source documentation first (e.g., `activation-workflow.md`, `ui-interaction-patterns.md`)
   - Regeneration will repeat errors if source documentation incomplete
   - **Process**: Fix upstream docs → Update prompt constraints → Regenerate → Validate

10. **Workflow Architecture Must Be Documented Separately**
    - Create dedicated workflow documentation (e.g., `activation-workflow.md`, `template-workflow-principle.md`)
    - Reference these in prompts as explicit constraints
    - Prevents LLM hallucination of non-existent workflows

**Compliance Improvement**: 68% baseline → 95% after remediation (+27 percentage points)

**All 4 Critical Errors Resolved**:
- ✅ Template-first workflow → Notebook-first workflow
- ✅ Non-existent activation toggle → Mobile app activation
- ✅ Missing pagination guidance → Comprehensive navigation
- ✅ Missing save behaviour → Clear expected behaviour

---

## Standardized Placeholder System

### Screenshot Placeholders

Use these formats consistently for human review and screenshot addition:

#### Basic Screenshot
```markdown
[SCREENSHOT: Description of what should be shown]
```

#### Screenshot with Annotations
```markdown
[SCREENSHOT: Login page
 HIGHLIGHT: Email field (red box)
 HIGHLIGHT: Password field (red box)  
 CIRCLE: Sign In button (green circle)
 ARROW: Points to "Forgot Password" link]
```

#### Platform-Specific Screenshots
```markdown
[SCREENSHOT-DESKTOP: Dashboard main view]
[SCREENSHOT-MOBILE: Dashboard main view with menu collapsed]
```

#### Visual Validation Placeholders
```markdown
[VISUAL CHECK: Instructor/colleague should verify the form shows 5 fields]
```

#### Navigation Placeholders
```markdown
[NAVIGATE: Specific instruction needed - e.g., "top-right corner" or "main menu"]
```

### Content Placeholders for Human Review

#### Specific Location Needed
```markdown
[LOCATION: Save button - specify exact position]
```

#### Platform Variation
```markdown
[PLATFORM NOTE: Describe mobile vs desktop difference]
```

#### Time Estimate
```markdown
[TIME CHECK: Verify this actually takes X minutes - account for first-time user orientation, reading, navigation, trial and error]
```

#### Success Indicator
```markdown
[SUCCESS INDICATOR: Describe what user sees when action succeeds]
```

---

## Improved Prompt Templates

### Master Template for Quickstart Guides

```markdown
Create a beginner-friendly quickstart guide for [TOPIC] that takes a new user from zero to first success in 25-30 minutes.

CRITICAL REQUIREMENTS FOR HUMAN-FACING DOCUMENTATION:

0. WORKFLOW ARCHITECTURE CONSTRAINTS
   - Review all architecture documentation first ([list relevant docs])
   - Document critical workflow constraints explicitly:
     * Where actions occur (Editor vs Dashboard vs Mobile App)
     * Workflow sequences (notebook-first vs template-first)
     * List behaviour (new items at END vs beginning)
     * Save behaviour (manual vs auto-save, navigation after save)
     * Activation architecture (where and how)
   - Never assume common patterns - verify against actual system
   - Add explicit constraints section to prompt referencing architecture docs

1. NAVIGATION SPECIFICITY
   - Never say just "click Save" - say WHERE it is
   - Provide multiple ways to find things (Option A, B, C)
   - Use landmarks: "top-right corner", "bottom of form", "main menu"
   - Add [LOCATION: element] placeholders where you're unsure

2. COGNITIVE LOAD MANAGEMENT
   - Maximum 2-3 new concepts per section
   - Optimise example count (e.g., 3 fields vs 5 - cover categories with minimum examples)
   - Break complex steps into Parts A, B, C
   - Add "Pause and Save" checkpoints
   - Include progress checks: "You should now see..."
   - Add mid-step progress checks: "> ✓ **Progress check**: You should now see..."

3. SUCCESS VALIDATION
   - Add "✓ You'll Know It Worked When..." sections
   - Use checkbox format `- [ ]` for interactive progress tracking
   - List 3-4 concrete success indicators
   - Include what users SEE, not just what happens
   - Add [VISUAL CHECK] placeholders for verification
   - Example: "- [ ] You see your name in the bottom-left user menu"

4. TECHNICAL TERMS
   - Add "📖 Quick Terms to Know" box early
   - Define on first use with simple analogies
   - Maximum 5-6 terms for beginners

5. PLATFORM AWARENESS
   - Add "📱 Mobile Users" notes where behavior differs
   - Include [PLATFORM NOTE] placeholders
   - Mention touchscreen vs mouse differences
   - Note where mobile is suboptimal (e.g., complex editing)

6. CRITICAL MISTAKES AND DRAMATIC WARNINGS
   - Identify the top 1-3 most common/serious user mistakes
   - Create dramatic warning boxes with visual before/after examples
   - Example: Show "❌ rec_a7f3b2c1" vs "✅ Ancient Temple Site" for HRID
   - Use blockquotes with ⚠️ emoji for visibility
   - Explain consequences: "This is a very common mistake new users make"
   - Place warnings BEFORE the step, not after users make the mistake

7. TROUBLESHOOTING STRATEGY
   - Create dedicated troubleshooting section at end
   - Mark as `{optional-reference}` to avoid cluttering main flow
   - Cover 7 most common issues with problem statement + solution format
   - Use multi-layered error prevention:
     * Preventative warnings before mistakes
     * Detective validation blocks for immediate feedback
     * Corrective troubleshooting section for recovery

STRUCTURE REQUIREMENTS:

Opening:
- Welcome with promise of success
- "What You'll Achieve" checklist
- Prerequisites (2 sentences max)
- Terms to Know box

Each Major Step:
- Time estimate in heading
- Lead with the goal
- Break into digestible parts if >3 actions
- Navigation options (A, B, C) where applicable
- Success validation checkpoint
- Platform notes if relevant

Within Steps:
- Number each action
- Bold the action verb
- Specify locations explicitly
- Add screenshot placeholders with annotations
- Include progress checks

Standard Elements:
- ✨ Pro Tips - encouraging hints
- ⚠️ Common Mistakes - with solutions (use dramatic warnings for critical mistakes)
- ✓ Success Checks - validation points (use checkbox format `- [ ]`)
- ✓ Progress Checks - mid-step validation ("> ✓ **Progress check**: You should now see...")
- 📱 Platform Notes - mobile/desktop differences
- [PLACEHOLDERS] - for human additions
- Success Checklist - end-of-guide accomplishment summary with checkboxes
- Troubleshooting Section - dedicated section marked `{optional-reference}`

Tone:
- "You" throughout
- Celebrate milestones ("Great job!")
- Acknowledge mistakes are normal
- Build confidence through success

Length: 1500-2500 words (clarity over brevity)
Time Estimate: 25-30 minutes for first-time users (account for orientation, reading, navigation, trial and error)
```

### Template for Field User Guides

```markdown
Create a field user guide for [MOBILE APP] that helps non-technical users collect data confidently.

SPECIAL REQUIREMENTS FOR FIELD USERS:

1. MINIMAL TECHNICAL LANGUAGE
   - 8th-grade reading level
   - No jargon without explanation
   - Use everyday analogies

2. MOBILE-FIRST APPROACH
   - Assume small screen
   - Assume poor connectivity
   - Assume outdoor conditions
   - Touch-specific instructions

3. VISUAL-HEAVY DESIGN
   - [SCREENSHOT] every 2-3 paragraphs
   - Annotated screenshots for complex tasks
   - Before/after comparisons
   - Icon references 📱 ⚠️ ✓

4. ERROR RECOVERY FOCUS
   - What to do when things go wrong
   - Offline scenarios
   - Sync failures
   - Permission issues

5. TASK-BASED SECTIONS
   - "How to..." headings
   - Real-world scenarios
   - Step-by-step with validation
   - Quick reference cards

Include placeholder types:
[SCREENSHOT-MOBILE: description]
[ICON: specific icon needed]
[GESTURE: swipe/tap/hold description]
[ERROR STATE: what error looks like]
[SUCCESS STATE: successful completion]
```

### Template for Troubleshooting Guides

```markdown
Create a troubleshooting guide for [SYSTEM] that helps users solve problems independently.

TROUBLESHOOTING-SPECIFIC REQUIREMENTS:

1. PROBLEM-FIRST STRUCTURE
   # "I can't..." or "The system won't..."
   ## What You're Seeing
   ## Most Likely Cause  
   ## Step-by-Step Solution
   ## Still Not Working?

2. VISUAL PROBLEM IDENTIFICATION
   [SCREENSHOT-ERROR: Error state appearance]
   [SCREENSHOT-SUCCESS: Fixed state appearance]
   [COMPARISON: Before/after side-by-side]

3. MULTIPLE SOLUTION PATHS
   - Quick Fix (30 seconds)
   - Standard Fix (2 minutes)
   - Advanced Fix (5 minutes)
   - When to Get Help

4. PLATFORM-SPECIFIC SECTIONS
   - Separate mobile/desktop solutions
   - Browser-specific issues
   - OS-specific problems

5. VALIDATION AFTER EACH FIX
   "✓ Check: You should now see..."
   "✓ Test: Try doing X to verify"
```

---

## Collaboration Workflow

### For LLM Generation

**Prerequisites**:
0. **Review Upstream Documentation**: Ensure source documentation exists and is accurate
   - Architecture documentation (workflows, UI patterns, system behaviour)
   - Reference documentation (field types, permissions, configuration)
   - Cannot fix documentation errors in quickstart alone - must fix source first

**Generation Process**:
1. **First Draft**: LLM creates with all placeholders and explicit workflow constraints
2. **Human Review**: Identify navigation gaps, add specifics, validate against actual UI
3. **Screenshot Planning**: Mark what needs visual documentation
4. **LLM Revision**: Incorporate human feedback
5. **QA Testing**: Validate against actual system with test users
6. **Final Review**: Human validates and adds visuals

### Placeholder Resolution Process

When you see a placeholder, provide:

| Placeholder Type | Human Provides | Example |
|-----------------|----------------|---------|
| [LOCATION] | Exact position | "top-right corner, next to user name" |
| [SCREENSHOT] | Image + annotations | Screenshot with red box around button |
| [NAVIGATE] | Specific path | "Settings > Notebooks > Create" |
| [VISUAL CHECK] | What to verify | "5 fields visible in order shown" |
| [PLATFORM NOTE] | Behavioral difference | "On mobile, tap ≡ to see menu" |
| [TIME CHECK] | Actual duration | "Tested: takes 3-4 minutes" |

---

## Quality Checklist for Human-Facing Docs

Before publishing, verify:

### Navigation Clarity
- [ ] All buttons/links have location specified
- [ ] Multiple paths provided where applicable  
- [ ] Mobile/desktop differences noted
- [ ] No ambiguous directions

### Cognitive Load
- [ ] Steps broken into manageable chunks
- [ ] Maximum 3 new concepts per section
- [ ] Progress checkpoints included
- [ ] Pause points for complex procedures

### Success Validation  
- [ ] "You'll know it worked when..." sections
- [ ] Visual success indicators described
- [ ] Error states explained
- [ ] Clear next steps after success

### Visual Documentation
- [ ] Screenshot placeholders every 3-5 steps
- [ ] Annotations specified for complex screens
- [ ] Before/after comparisons where helpful
- [ ] Mobile and desktop versions where different

### User Confidence
- [ ] Encouraging tone throughout
- [ ] Mistakes normalized
- [ ] Success celebrated
- [ ] Help paths clear

---

## Examples of Improved Prompting

### ❌ Old Style (Too Vague)
"Click Save to save your work"

### ✅ New Style (Specific)
```markdown
Look for the **Save** button - it's typically:
- At the bottom of the form
- Or in the top-right corner
- Might say "Save", "Submit", or show a save icon (💾)
[LOCATION: Save button - specify exact position]

Click it to save your work.

### ✓ You'll Know It Saved When...
- [ ] You see a success message
- [ ] The form clears or resets
- [ ] [SUCCESS INDICATOR: Describe visual confirmation]
```

### ❌ Old Style (Too Much at Once)
"Add five fields: TextField, Select, DateTimeNative, another TextField with multiline, and TakePhoto"

### ✅ New Style (Optimised & Chunked)
```markdown
Now let's add three essential fields that demonstrate major field categories: text input, selection options, and media capture.

#### Field 1: Site Name (Text Field)
[Detailed steps...]

### ✓ You'll Know It Worked When...
- [ ] The "Site Name" field appears in the "Visible Fields" area
- [ ] Helper text displays correctly
- [ ] Required checkbox is checked

> ✓ **Progress check**: You should now see one field in your Visible Fields list. You're doing great!

#### Field 2: Site Type (Radio Buttons)
[Detailed steps...]

**Quick Save**: Click the **SAVE** button in the top-right to save your progress.

#### Field 3: Site Photo (Camera)
[Detailed steps...]

> ✓ **Progress check**: You should now see three fields in your Visible Fields list:
> Site Name, Site Type, and Site Photo. Each shows its field type badge.
```

---

## Notes for Future Improvements

1. **Consider User Testing Feedback Loops**
   - Mark sections that need testing: [USER TEST: Expected confusion point]
   - Note where users historically struggle
   - Update based on actual confusion points

2. **Accessibility Considerations**
   - Alt text for all images
   - Keyboard navigation notes
   - Screen reader compatibility notes

3. **Localization Readiness**
   - Simple sentence structures
   - Avoid idioms
   - Cultural neutrality

4. **Maintenance Markers**
   - [VERSION NOTE: UI might change]
   - [UPDATE CHECK: Verify still accurate]
   - Date stamps for time-sensitive content

---

*This document should be updated as we learn more about effective human-facing documentation patterns.*
