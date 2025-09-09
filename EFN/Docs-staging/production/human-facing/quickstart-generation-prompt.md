# Quickstart Guide Generation Prompt

## Purpose
This prompt template generates or updates the "Your First Notebook in 15 Minutes" quickstart guide for Fieldmark notebook creators.

---

## Generation Prompt

Generate a comprehensive quickstart guide for first-time Fieldmark users to create their first notebook in 15 minutes. Use the following specifications:

### Document Structure Requirements

1. **Title**: "Your First Notebook in 15 Minutes 🚀"
2. **Opening**: Welcoming paragraph emphasizing no experience needed
3. **Time Limit**: Must be completable in 15 minutes by a novice
4. **Tone**: Friendly, encouraging, non-technical
5. **Length**: ~400-450 lines (comprehensive but scannable)

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

#### 3. Step 1: Access Your Dashboard (2 minutes)
Include:
- Login process
- Dashboard overview
- [SCREENSHOT] placeholder for login page
- [SCREENSHOT] placeholder for dashboard
- Pro tip about bookmarking
- "You'll Know It Worked When..." checklist
- Common issue: where to find user menu (bottom-left)

#### 4. Step 2: Create Your First Notebook (3 minutes)
Include:
- Two paths: via Templates or direct Notebooks
- Notebook Editor introduction
- [SCREENSHOT] placeholder for editor interface
- Three-panel layout explanation
- Mobile device warning
- "You'll Know It Worked When..." checklist

#### 5. Step 3: Add Your Fields (5-7 minutes)
Break into parts A, B, C:

**Part A: First Two Fields (2 min)**
- Text field (use correct component name from reference.md)
- Dropdown/Select field
- Configuration details for each
- Progress check

**Part B: Date and Long Text (2 min)**
- Date field (use "DateTime with Now button" → DateTimeNow)
- Multiline text field
- Configuration details
- Progress check

**Part C: Photo Capability (1 min)**
- Photo field (TakePhoto)
- Configuration details
- [SCREENSHOT] placeholder for completed form

**Critical Addition**: Form Completion Settings
- Must include HRID configuration
- Submit button setup
- This prevents the "rec_xxxxx" ID problem

#### 6. Step 4: Deploy and Test Your Notebook (3 minutes)
Include:
- Deployment from template
- Entering first record
- Saving the record
- Viewing in records list
- [SCREENSHOT] placeholders for form and records
- "You'll Know It Worked When..." checklist

#### 7. Step 5: Collaborate and Refine (2 minutes)
Include:
- Permission roles table
- Invitation process
- Making an improvement
- Virtual roles mention for teams
- [SCREENSHOT] placeholder for invite dialog

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
- 8-10 items with checkboxes
- Comprehensive coverage of all steps
- Victory message when complete

#### Quick Troubleshooting
5-6 most common problems:
- Can't find Notebook Editor
- Fields not showing
- Save button missing
- Invitation issues
- Photo problems
- HRID configuration

#### Power User Tips
Brief mentions of:
- Virtual roles through teams
- API automation possibility
- Conditional logic
- Template library concept

#### What's Next
- Immediate next steps (3 items)
- Learning path (4 items)
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

### Common Mistakes to Address
- Empty form confusion
- Template vs Notebook distinction
- HRID configuration missing
- Mobile editing attempts
- Permission confusion

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
   - Verify 15-minute completion feasible
   - Ensure all checkpoints included
   - Confirm troubleshooting covers real issues
   - Test navigation paths are current

---

## Example Opening

```markdown
# Your First Notebook in 15 Minutes 🚀

*Welcome to Fieldmark! In the next 15 minutes, you'll create your first data collection notebook and enter your first record. No experience needed - just follow along!*

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