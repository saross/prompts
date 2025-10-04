# Next Session Implementation Plan
## Quickstart Guide v1 Refinements

**Created**: 2025-10-02
**Context Remaining**: ~10%
**Estimated Work**: 45 minutes
**File to Edit**: `production/human-facing/quickstart-creation-and-collection.md`

---

## Session Context

We completed the screenshot verification pilot and effectiveness assessment (8.5/10). Now implementing "low-hanging fruit" improvements before v1 release.

**Assessment Document**: `production/human-facing/quickstart-effectiveness-assessment-2025-10-02.md`

---

## Implementation Tasks

### 1. Terminology & Clarity Fixes (~10 min)

#### URL Clarification
**Location**: Line ~38 (Prerequisites), Line ~418 (Step 4)

**Current**:
- "usually something like `https://api.fieldmark.app`"
- Later mentions `https://app.fieldmark.app`

**Change To**:
```markdown
**Location**: Line ~38 (after "You'll need")
Add after browser requirement:
- **Control Centre URL**: Usually `https://api.fieldmark.app` (for designing notebooks)
- **Data Collection App URL**: Usually `https://app.fieldmark.app` (for entering records)
- Note: Your organization may have custom URLs - check with your administrator

**Location**: Line ~418
Clarify: "navigate to your Fieldmark data collection app URL (usually `https://app.fieldmark.app`)"
```

#### Dashboard → Control Centre
**Action**: Global find/replace throughout document
- "Dashboard" → "Control Centre" (except where it refers to the actual UI element name)
- Verify: The UI itself may still say "Dashboard" - keep those references accurate

#### UUID Definition
**Location**: Line ~383 (HRID explanation)

**Current**: "provides meaningful record labels instead of UUID"

**Change To**: "provides meaningful record labels instead of opaque, computer-generated identifiers (UUIDs)"

#### Collapsed Fields
**Locations**: Multiple (Field 1, Field 2, etc. in Step 3)

**Current**: "If the field appears collapsed..."

**Change To**: "Click on the grey bar to expand the field" (remove conditional)

**Note**: User confirmed fields appear collapsed by default, so "if" is unnecessary

#### Team Selection
**Location**: Line ~77 (Create Notebook section)

**Current**: "(usually there will only be one option)"

**Change To**:
```markdown
2. **Select team**: Use the dropdown (required)
   - If you have only one team, it will be pre-selected
   - If you have multiple teams, choose the appropriate one for this notebook
```

---

### 2. Add Tips & Missing Context (~15 min)

#### UNDO/REDO Buttons Tip
**Location**: After line ~110 (Hello, Notebook Editor section, after interface description)

**Add**:
```markdown
> 💡 **Tip**: Notice the UNDO and REDO buttons in the top-right corner of the Editor. Use these to recover from accidental deletions or changes. They're your safety net while building forms!
```

#### Resume Editing Anytime
**Location**: Line ~402 (in "Save Your Work" section, after explaining save returns to Dashboard)

**Current**: Already mentions clicking "Open in Editor" to resume

**Enhance With**:
```markdown
> 💡 **Tip**: You can always resume editing your notebook at any time by returning to the Control Centre, selecting your notebook from the list, clicking the **Actions** tab, and choosing **Open in Editor**. Your work is saved and ready to continue.
```

#### Offline-First Reassurance
**Location**: After line ~450 (after activation completes, before "Open Your Notebook" section)

**Add**:
```markdown
### Understanding Offline-First Design

Before we continue, here's an important feature: Fieldmark is designed to work offline.

> 💡 **Offline-First**: No network connection is needed for data collection in the field. Your data is saved locally to your device, and it automatically syncs to the server when you have connectivity (unless you've disabled sync in Settings). This means you can collect data anywhere, anytime.

This is why we "activate" notebooks - the activation process downloads the notebook structure to your device so you can work without internet.
```

#### Conflict Resolution Mention
**Location**: Line ~550 (in Notebook Settings section, after sync explanation)

**Add to sync callout**:
```markdown
> 💡 **About Sync**: Fieldmark automatically syncs records when you're online. The orange icon with three dots means the record hasn't synced to the server yet. Once synced, it will turn into a green cloud icon with a checkmark. To manually refresh and see the latest records from the server, click the **REFRESH RECORDS** button.
>
> If multiple team members edit the same record, Fieldmark has a conflict resolution workflow to help you merge changes. (See the Collaboration Guide for details.)
```

---

### 3. Improve Wayfinding (~5 min)

#### Finding Newly Created Notebook
**Location**: Lines 87-94 (Step 2, after clicking Create Notebook)

**Current**:
```markdown
5. **Find your new notebook**:
   - It will appear at the end of the notebook list
   - You may need to navigate to later pages (look for pagination controls at bottom)
   - Or use the search bar if available to find "My First Survey"
```

**Enhance With**:
```markdown
5. **Find your new notebook**:
   - It will appear at the end of the notebook list
   - **If you have many notebooks**: Look for pagination controls at the bottom of the list (showing "1-10 of X notebooks" with arrow buttons)
   - **Quick tip**: Use the search bar at the top of the list to search for "My First Survey"
   - Scroll down and click through pages until you see your notebook

[SCREENSHOT: Notebook list showing pagination controls at bottom and search bar at top, with arrow pointing to newly created "My First Survey" notebook]
```

---

### 4. Reduce Verbosity (~10 min)

#### Editor Interface Description
**Location**: Lines 101-109 (Hello, Notebook Editor section)

**Current**: 7 bullet points describing interface elements

**Reduce To** (4 bullets):
```markdown
You'll see the main interface elements:
- **Top bar**: CANCEL and SAVE buttons on the right; UNDO and REDO buttons
- **Tab bar**: DESIGN and INFO tabs on the left
- **"+" button**: Click to add a new form
- **Form editing area**: Shows "Form Name" field with "Form 1" pre-filled, and "ADD NEW FORM" button

[SCREENSHOT: Notebook Editor interface showing the form builder layout]

> ⚠️ **Common Mistake**: Don't worry if it looks empty - that's normal! We're about to fill it with useful fields. Remember to click the green SAVE button in the top-right when you want to save your work.
```

#### Empty Table Description
**Location**: Lines 462-470 (Open Your Notebook section)

**Current**: Exhaustive list of all table columns

**Reduce To**:
```markdown
You'll see the record list interface:
- **ADD NEW SITE DETAILS** button (orange) - for creating new records
- **REFRESH RECORDS** button (green) - to sync with server
- **MY SITE DETAILSS (0)** tab - shows your record list (currently empty)
- Additional tabs: DETAILS, SETTINGS, MAP
- **Empty table** showing column headers for your data (Site Name, Site Type, Created, Last Updated, etc.)
- "No rows" message - because this is a brand new notebook

[SCREENSHOT: Empty notebook view showing interface elements and empty table with column headers]
```

**Note**: The screenshot will show the columns, no need to list them all

---

### 5. Screenshot Placeholders to Add (~5 min)

Add these new placeholders:

1. **Line ~40** (Prerequisites section):
```markdown
[SCREENSHOT: Two browser windows side by side showing Control Centre (api.fieldmark.app) and Data Collection App (app.fieldmark.app) URLs with labels]
```

2. **Line ~92** (Finding notebook):
```markdown
[SCREENSHOT: Notebook list showing pagination controls at bottom ("< 1 2 3 >") and search bar at top, with arrow pointing to "My First Survey" at end of list]
```

3. **Line ~110** (UNDO/REDO tip):
```markdown
[SCREENSHOT: Close-up of Editor top-right corner showing UNDO and REDO buttons with cursor hovering]
```

4. **Line ~553** (Conflict resolution mention):
```markdown
[NOTE: Conflict resolution screenshot/workflow will be covered in Collaboration Guide - just mention here]
```

---

## Out of Scope (Note for Future)

These items from the assessment are explicitly **NOT** in scope for v1 quickstart:

- Comprehensive error handling (network failures, permission errors, validation)
- Detailed browser specifications ("modern" is sufficient)
- Storage space calculations
- Internet speed requirements
- Detailed conflict resolution workflow (just mention it exists)
- How to edit existing records (view-only workflow)
- Camera/photo troubleshooting details

---

## Testing Before Commit

After implementing changes:
1. ✅ Read through entire document for flow
2. ✅ Verify all "Dashboard" → "Control Centre" changes are contextually correct
3. ✅ Check that all new tips have appropriate placement
4. ✅ Confirm screenshot placeholders are adequately described
5. ✅ Run word count (should stay ~5,000 words despite adding tips)

---

## Git Commit Message Template

```
Implement v1 refinements from effectiveness assessment

Applied low-hanging fruit improvements identified in assessment:
- Clarified URL usage (Control Centre vs Data Collection App)
- Standardized terminology (Dashboard → Control Centre)
- Removed conditional field collapse language
- Added UNDO/REDO, offline-first, and resume editing tips
- Improved wayfinding for new notebook navigation
- Reduced verbosity in interface descriptions
- Added strategic screenshot placeholders

Based on quickstart-effectiveness-assessment-2025-10-02.md
recommendations. Focus on clarity and user confidence without
scope creep.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Files to Update in Session

1. **Primary**: `production/human-facing/quickstart-creation-and-collection.md`
2. **Session log**: `to-do-next.md` (add 2025-10-02 afternoon session notes)
3. **Commit and push**: Both files

---

## Reference Materials for Next Session

- **Assessment**: `production/human-facing/quickstart-effectiveness-assessment-2025-10-02.md`
- **Current quickstart**: `production/human-facing/quickstart-creation-and-collection.md` (5,019 words)
- **Standards**: `production/human-facing/documentation-standards.md`
- **Screenshots location**: `/home/shawn/Pictures/Screenshots/` (for reference during edits)

---

## Success Criteria

Next session is successful when:
1. ✅ All 5 task categories completed
2. ✅ Document flows naturally with new additions
3. ✅ No scope creep (stayed focused on listed items)
4. ✅ Word count remains ~5,000 words (±200)
5. ✅ Git commit with clear message
6. ✅ Pushed to GitHub
7. ✅ Session notes updated in to-do-next.md

---

**End of handover document. Begin next session by reading this file first.**
