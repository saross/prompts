# Human-Facing Documentation Standards

**Created**: 2025-01-08  
**Purpose**: Standards and templates for creating effective human-facing documentation  
**Based on**: Lessons learned from quickstart guide development and assessment

## Key Learnings from Quickstart Guide

### What LLMs Do Well
- Structure and logical flow
- Consistent terminology
- Encouraging tone
- Comprehensive coverage

### What LLMs Miss
- **Navigation specificity** - WHERE buttons are located
- **Visual continuity** - Assuming users remember previous screens
- **Cognitive load** - Too many concepts at once
- **Platform variations** - Mobile vs desktop differences
- **Success validation** - How users know they succeeded

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
[TIME CHECK: Verify this actually takes X minutes]
```

#### Success Indicator
```markdown
[SUCCESS INDICATOR: Describe what user sees when action succeeds]
```

---

## Improved Prompt Templates

### Master Template for Quickstart Guides

```markdown
Create a beginner-friendly quickstart guide for [TOPIC] that takes a new user from zero to first success in 15 minutes.

CRITICAL REQUIREMENTS FOR HUMAN-FACING DOCUMENTATION:

1. NAVIGATION SPECIFICITY
   - Never say just "click Save" - say WHERE it is
   - Provide multiple ways to find things (Option A, B, C)
   - Use landmarks: "top-right corner", "bottom of form", "main menu"
   - Add [LOCATION: element] placeholders where you're unsure

2. COGNITIVE LOAD MANAGEMENT
   - Maximum 2-3 new concepts per section
   - Break complex steps into Parts A, B, C
   - Add "Pause and Save" checkpoints
   - Include progress checks: "You should now see..."

3. SUCCESS VALIDATION
   - Add "✓ You'll Know It Worked When..." sections
   - List 3-4 concrete success indicators
   - Include what users SEE, not just what happens
   - Add [VISUAL CHECK] placeholders for verification

4. TECHNICAL TERMS
   - Add "📖 Quick Terms to Know" box early
   - Define on first use with simple analogies
   - Maximum 5-6 terms for beginners

5. PLATFORM AWARENESS
   - Add "📱 Mobile Users" notes where behavior differs
   - Include [PLATFORM NOTE] placeholders
   - Mention touchscreen vs mouse differences
   - Note where mobile is suboptimal (e.g., complex editing)

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
- ⚠️ Common Mistakes - with solutions
- ✓ Success Checks - validation points
- 📱 Platform Notes - mobile/desktop differences
- [PLACEHOLDERS] - for human additions

Tone:
- "You" throughout
- Celebrate milestones ("Great job!")
- Acknowledge mistakes are normal
- Build confidence through success

Length: 1500-2500 words (clarity over brevity)
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

1. **First Draft**: LLM creates with all placeholders
2. **Human Review**: Identify navigation gaps, add specifics
3. **Screenshot Planning**: Mark what needs visual documentation
4. **LLM Revision**: Incorporate human feedback
5. **Final Review**: Human validates and adds visuals

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

✓ You'll Know It Saved When...
- You see a success message
- The form clears or resets
- [SUCCESS INDICATOR: Describe visual confirmation]
```

### ❌ Old Style (Too Much at Once)
"Add five fields: TextField, Select, DateTimeNative, another TextField with multiline, and TakePhoto"

### ✅ New Style (Chunked)
```markdown
### Part A: Your First Two Fields (2 minutes)

Let's start with the basics - a text field and a dropdown.

#### Field 1: Site Name (Text Field)
[Detailed steps...]

> ✓ Check Your Progress: You should see "Site Name" in the preview

#### Field 2: Site Type (Dropdown)  
[Detailed steps...]

**Pause and Save**: Click Save [LOCATION: Save button] before continuing.

### Part B: Date and Long Text (2 minutes)
[Continue with next chunk...]
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