# Quickstart Guide Generation Prompt

## Purpose
This prompt template generates or updates the "Your First Notebook in 25-30 Minutes" quickstart guide for Fieldmark notebook creators.

---

## Generation Prompt

Generate a comprehensive quickstart guide for first-time Fieldmark users to create their first notebook in 25-30 minutes. Use the following specifications:

### Document Structure Requirements

1. **Title**: "Your First Notebook in 25-30 Minutes 🚀"
2. **Opening**: Welcoming paragraph emphasising no experience needed
3. **Time Limit**: Realistic 25-30 minute completion time for novices
4. **Tone**: Friendly, encouraging, non-technical
5. **Length**: ~500-600 lines (comprehensive but scannable)

### Required Sections (in order)

#### 1. What You'll Achieve
- Bulleted checklist of 5 accomplishments
- Use checkmark emoji (✅) for visual appeal
- Focus on concrete outcomes

#### 2. Before You Start
- Prerequisites (account requirements)
- Browser recommendations
- "Quick Terms to Know" subsection with 5 key terms:
  - Dashboard
  - Notebook  
  - Notebook Editor
  - Records
  - Fields

#### 3. Step 1: Access Your Dashboard (3-5 minutes)
Include:
- Login process
- Dashboard overview
- [SCREENSHOT] placeholder for login page
- [SCREENSHOT] placeholder for dashboard
- Pro tip about bookmarking
- "You'll Know It Worked When..." checklist
- Common issue: where to find user menu (bottom-left)

#### 4. Step 2: Create Your First Notebook (5-8 minutes)
Include:
- **CRITICAL**: Direct notebook creation only (NOT via Templates)
- Navigate to Notebooks → Create Notebook (never Templates → Create Template)
- Notebook Editor introduction
- [SCREENSHOT] placeholder for editor interface
- Three-panel layout explanation
- Mobile device warning
- "You'll Know It Worked When..." checklist

#### 5. Step 3: Add Your Fields (8-12 minutes)
**CRITICAL**: Use only 3 fields to demonstrate core field categories:

**Field 1: Text Field**
- Text field (use correct component name from reference.md)
- Configuration details
- Progress check

**Field 2: Choice Field**
- Dropdown/Select field (radio buttons)
- Configuration details
- Progress check

**Field 3: Photo Field**
- Photo field (TakePhoto)
- Configuration details
- [SCREENSHOT] placeholder for completed form

**CRITICAL: Form Settings Configuration**
- **MUST include dramatic HRID warning** with before/after examples
- Show records displaying as "rec_xxxxx" vs meaningful names
- This is a very common and serious mistake - emphasise heavily
- Summary Fields configuration
- Submit button setup

#### 6. Step 4: Activate and Test Your Notebook (5-8 minutes)
Include:
- **CRITICAL**: Activation in mobile/data collection app (app.fieldmark.app)
- **NOT** in Dashboard or Editor
- Navigate to separate data collection app URL
- Click NOT ACTIVE tab → find notebook → ACTIVATE button
- Entering first record
- Saving the record
- Viewing in records list
- [SCREENSHOT] placeholders for activation and records
- "You'll Know It Worked When..." checklist

### ⚠️ CRITICAL WORKFLOW CONSTRAINTS ⚠️

**These constraints are based on QA testing that revealed critical documentation gaps. Violating these will create workflow-breaking errors for users.**

#### 1. Notebook-First Workflow for Beginners (NOT Template-First)
- **For quickstart/beginner documentation**: NEVER direct users to Templates → Create Template
- **ALWAYS** use: Notebooks → Create Notebook for first-time users
- Templates are an **advanced feature** for experienced users who need reusable patterns
- **Pedagogical rationale**: Novices need to field-test notebooks before converting to templates
- **Advanced users**: May use template-first workflow when appropriate for their needs
- Document template conversion as optional "next step" after field-testing
- Cross-reference: template-workflow-principle.md

#### 2. Activation Architecture
- Activation occurs in the **mobile/data collection app** (app.fieldmark.app)
- **NOT** in the Dashboard or Editor
- **NO** "Active" toggle exists in Editor's Info tab
- Process: Navigate to app.fieldmark.app → NOT ACTIVE tab → ACTIVATE button → modal confirmation
- Cross-reference: activation-workflow.md

#### 3. List Behaviour (New Items at End)
- New notebooks appear at **END of list**, not beginning
- **MUST** document pagination controls ("1-10 of X notebooks")
- **MUST** document search bar for finding notebooks
- Users with many notebooks need explicit navigation guidance
- Cross-reference: ui-interaction-patterns.md Section 13

#### 4. Save Behaviour (No Auto-Save)
- Editor **does NOT auto-save**
- Clicking SAVE **closes Editor and returns to Dashboard**
- This is **expected behaviour**, not a bug
- Must document: "You'll be returned to the Dashboard - this is expected"
- Must explain: Click "Open in Editor" again to resume editing
- Cross-reference: ui-interaction-patterns.md Section 15

#### 5. Form → Section → Field Hierarchy
- Creation sequence: **Form FIRST, then Section, then Fields**
- **CANNOT** add fields without creating a section first
- Must explicitly show section creation step
- "Don't skip the section creation step" warning required
- Cross-reference: editor-form-settings.md

### Required Elements Throughout

#### Visual Markers
- [SCREENSHOT: description] placeholders (10-12 total)
- ✓ checkpoints after major steps
- > blockquotes for tips and warnings
- Emoji usage: sparingly, only ✅, 🚀, 🎯, 📱, ⚠️, ✨, 💡, 🎊

#### Troubleshooting Boxes
After each major step, include common issues:
- Problem statement
- **Solution**: Clear fix
- Format as heading + solution

#### Platform Notes
- Mobile vs desktop differences
- Browser-specific behaviors
- Touchscreen adaptations

### Required Subsections at End

#### Success Checklist
- 8-10 items with checkboxes ([ ] format for markdown)
- Comprehensive coverage of all steps
- Victory message when complete
- **MUST include**: "Configured the Human-Readable ID Field (critical step!)"

#### Troubleshooting {optional-reference}
**MUST be clearly marked as optional reference material**

7 most common problems with solutions:
- Can't Find the Notebook Editor
- Notebook Not in List After Creation (END of list issue)
- Fields Not Showing in the Form
- Editor Closed After Clicking Save (expected behaviour)
- Records Show "rec_xxxxx" Instead of Readable Names (HRID issue - very common!)
- Notebook Not Appearing in Mobile App
- Photos Won't Upload

#### What's Next
- Immediate next steps (5-6 items)
- Brief mention of template conversion (as advanced feature)
- Help resources

#### Closing
- Encouraging final message
- Note about Fieldmark formerly being FAIMS3

### Technical Accuracy Requirements

Pull current information from reference.md for:

1. **Field Component Names**
   - Use Notebook Editor UI names (not JSON names)
   - Example: "DateTime with Now button" not "DateTimeNow"
   - Refer to designer-component-mapping.md

2. **Navigation Paths**
   - Dashboard → Templates → Create Template
   - User menu location (bottom-left)
   - Tab structures per interface documentation

3. **Permission Model**
   - Team-based access for templates
   - Virtual roles explanation
   - No individual "template permissions"

4. **Critical Configuration**
   - HRID field setup (prevents rec_xxxxx IDs)
   - Form completion settings
   - Required field indicators

### Style Guidelines

1. **Paragraph Length**: 2-3 sentences max
2. **List Items**: Brief, action-oriented
3. **Technical Terms**: Define on first use
4. **Voice**: Second person, present tense
5. **Encouragement**: After each major milestone

### Screenshot Placeholder Format
```
[SCREENSHOT: Brief description of what should be shown]
```

### Common Mistakes to Address (with Preventative Solutions)
- **Template-first workflow** → Direct to Notebooks, mark Templates as advanced
- **HRID configuration missing** → Dramatic warning box with before/after examples
- **Activation confusion** → Explicit mobile app URL, clear NOT ACTIVE tab instructions
- **List navigation** → Document pagination and search bar upfront
- **Save behaviour** → "Expected behaviour" messaging
- **Section creation skipped** → Explicit section creation step with warning

### Version Notes
- Mention Fieldmark (not FAIMS3) throughout
- Note the name change at the very end only
- Account for team-based permissions
- Include virtual roles concept

---

## Usage Instructions

1. **To Generate New Guide**:
   - Load reference.md for current field information
   - Check dashboard documentation for current UI
   - Generate following structure above
   - Maintain encouraging, friendly tone

2. **To Update Existing Guide**:
   - Compare against this template structure
   - Update field names from reference.md
   - Refresh navigation paths
   - Maintain existing screenshot placeholders

3. **Quality Checks**:
   - Verify 25-30 minute completion realistic
   - Ensure all checkpoints included (checkbox format)
   - Confirm troubleshooting covers real issues
   - Test navigation paths against Critical Workflow Constraints
   - **Verify HRID warning is dramatic and prominent**
   - **Verify notebook-first workflow (never template-first)**

---

## Example Opening

```markdown
# Your First Notebook in 25-30 Minutes 🚀

*Welcome to Fieldmark! In the next 25-30 minutes, you'll create your first data collection notebook and enter your first record. No experience needed - just follow along!*

## What You'll Achieve

By the end of this guide, you'll have:
- ✅ Created a working notebook from scratch
- ✅ Added fields for data collection
- ✅ Entered and saved your first record
- ✅ Learned how to invite team members
- ✅ Gained confidence to explore further
```

---

*Prompt Template Version: 1.0*
*Created: 2025-01-10*
*Source: reference.md and dashboard documentation*