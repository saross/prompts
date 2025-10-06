# Detailed Comparison: Gold Standard vs Regenerated Quickstart

**Date**: 2025-10-06
**Analyst**: Claude Code (Sonnet 4.5)

**Files Compared**:
- **Gold Standard**: `production/human-facing/quickstart-creation-and-collection.md` (663 lines)
- **Regenerated**: `production/human-facing/quickstart-regenerated-test-2025-10-06.md` (534 lines)

**Quality Scores**:
- Gold Standard: 95% compliance (21/22 metrics)
- Regenerated: 100% compliance (22/22 metrics)

---

## Executive Summary

Both versions are **production-ready** with only minor differences. The gold standard is longer (663 vs 534 lines, +24%) due to more screenshots (33 vs 15) and accumulated manual refinements. The regenerated version has cleaner structure and slightly better clarity in a few areas.

**Key Finding**: **No critical differences** - both achieve the same educational outcomes. Differences are primarily:
- **Screenshot density**: Gold standard has 2.2x more screenshots
- **Phrasing variations**: Minor wording differences
- **Structural details**: Small organizational differences

**Recommendation**: **Keep gold standard as primary version**, but consider adopting 3-4 specific improvements from regenerated version (detailed below).

---

## Section-by-Section Comparison

### Title & Opening

**Both Identical**:
- Title: "Your First Notebook in 25-30 Minutes 🚀"
- Opening paragraph identical
- Time estimate: 25-30 minutes

**Verdict**: No difference ✓

---

### What You'll Achieve

**Gold Standard** (Lines 7-12):
```markdown
- ✅ Created a working notebook from scratch
- ✅ Added fields for data collection
- ✅ Entered and saved your first record
- ✅ Learned how to invite team members
- ✅ Gained confidence to explore further
```

**Regenerated** (Lines 7-12):
```markdown
- ✅ Created a working notebook from scratch
- ✅ Added three essential fields for data collection
- ✅ Configured critical settings to prevent common mistakes
- ✅ Activated your notebook and entered your first record
- ✅ Gained confidence to build more sophisticated data collection tools
```

**Differences**:
- Regenerated explicitly mentions "three essential fields" (more specific)
- Regenerated adds "Configured critical settings to prevent common mistakes" (emphasizes HRID)
- Regenerated says "Activated your notebook" (more explicit about activation step)
- Gold standard mentions "invite team members" (useful but not covered in tutorial until "What's Next")

**Winner**: **Regenerated** - More accurate to actual tutorial content, doesn't promise features not taught in the guide

**Recommendation**: ✅ **Adopt regenerated version** - Replace gold standard lines 9, 10, 11, 12 with regenerated phrasing

---

### Before You Start

**Gold Standard** (Lines 20-23):
```markdown
**URLs you'll use**:
- **Dashboard URL**: Usually `https://dashboard.fieldmark.app` (for designing and managing notebooks)
- **Data Collection App URL**: Usually `https://app.fieldmark.app` (for entering records)
- Note: Your organisation may have custom URLs - check with your administrator
```

**Regenerated** (Lines 20-22):
```markdown
**Two URLs you'll use**:
- **Dashboard** (`https://dashboard.fieldmark.app`) - for designing and managing notebooks
- **Data Collection App** (`https://app.fieldmark.app`) - for entering records in the field
```

**Differences**:
- Regenerated says "Two URLs" (clearer count)
- Regenerated more concise formatting
- Gold standard includes note about custom URLs (useful edge case)
- Regenerated says "in the field" (emphasizes mobile/field use)

**Winner**: **Tie** - Both good, different trade-offs
- Gold standard: More comprehensive (includes custom URL note)
- Regenerated: More concise, emphasizes field use

**Recommendation**: ⚪ **Keep gold standard** - Custom URL note is valuable for some organizations

---

### Quick Terms to Know

**Both Nearly Identical**:

**Minor Difference** - Definition of "Notebook":

**Gold Standard** (Line 32):
```markdown
- **Notebook**: A data collection form you create and customise
```

**Regenerated** (Line 27):
```markdown
- **Notebook**: A customisable data collection form (like a digital fieldwork form)
```

**Regenerated adds analogy**: "like a digital fieldwork form" - helpful mental model

**Recommendation**: ✅ **Adopt regenerated phrasing** - Analogies aid comprehension

---

### Step 1: Access Your Dashboard

**Gold Standard** (Line 45):
```markdown
1. Open your browser and go to your Fieldmark Dashboard URL (usually `https://api.fieldmark.app`)
```

**Regenerated** (Line 40):
```markdown
1. Open your browser and navigate to `https://dashboard.fieldmark.app`
```

**Difference**:
- Gold standard says "usually `https://api.fieldmark.app`" - **This appears to be an error!** Should be `dashboard.fieldmark.app` not `api.fieldmark.app`
- Regenerated has correct URL

**Winner**: **Regenerated** ✅

**Recommendation**: ✅ **Fix gold standard** - Change `api.fieldmark.app` to `dashboard.fieldmark.app` (Line 45)

---

### Dashboard Description

**Gold Standard** (Lines 53-58):
```markdown
After logging in, you'll see the Dashboard Overview. This is your command centre where you can:
- Create new notebooks (from scratch or from templates)
- Access and edit existing notebooks
- Create and edit templates
- Manage teams and users
```

**Regenerated** (Lines 47-51):
```markdown
After logging in, you'll see the Dashboard interface:
- **Left sidebar**: Navigation options (Notebooks, Templates, Users, Teams)
- **Main content area**: Where you'll see lists of notebooks and templates
- **User menu**: Your profile icon in the **bottom-left corner**
```

**Differences**:
- Gold standard: Functional description (what you CAN do)
- Regenerated: Structural description (what you SEE) with specific UI element locations

**Winner**: **Regenerated** - More actionable for navigation (tells users WHERE things are)

**Recommendation**: ✅ **Adopt regenerated structure** - Better for first-time orientation

---

### Pro Tip - Bookmarking

**Gold Standard** (Line 61):
```markdown
> ✨ **Pro Tip**: Bookmark this page! You'll be coming back here often. In most browsers, press `Ctrl+D` (Windows/Linux) or `Cmd+D` (Mac) to bookmark.
```

**Regenerated** (Line 55):
```markdown
> ✨ **Pro Tip**: Bookmark this Dashboard page - you'll return here often to manage your notebooks.
```

**Differences**:
- Gold standard includes keyboard shortcuts (Ctrl+D/Cmd+D) - more actionable
- Regenerated more concise

**Winner**: **Gold standard** - Keyboard shortcuts add value

**Recommendation**: ⚪ **Keep gold standard** - Shortcuts are helpful

---

### Step 2: Create Your First Notebook - Opening

**Gold Standard** (Line 75):
```markdown
Creating a notebook is easy. Let's do it!
```

**Regenerated** (Line 70):
```markdown
**IMPORTANT**: We're creating a notebook directly, not from a template. Templates are an advanced feature - for now, we'll start simple.
```

**Differences**:
- Gold standard: Encouraging but generic
- Regenerated: Explicitly prevents template confusion upfront

**Winner**: **Regenerated** - Proactively addresses potential confusion

**Recommendation**: ✅ **Adopt regenerated opening** - Better pedagogical framing

---

### Navigate to Notebook Creation

**Both Identical**: Steps to click Notebooks → Create Notebook ✓

---

### Name Your Notebook

**Gold Standard** (Lines 88-94):
```markdown
In the creation dialog:
1. **Template/Notebook Name**: Type "My First Survey" (or any name you like!)
2. **Select team**: Use the dropdown (required)
   - If you have only one team, it will be pre-selected
   - If you have multiple teams, choose the appropriate one for this notebook
3. Ignore the 'optional' fields
4. Click **Create Notebook**
```

**Regenerated** (Lines 81-87):
```markdown
In the creation dialogue:
1. **Notebook Name**: Enter "My First Survey" (or choose your own name)
2. **Select team**: Choose your team from the dropdown
   - If you have only one team, it may be pre-selected
   - If you have multiple teams, select the appropriate one
3. Leave optional fields empty for now
4. Click **Create Notebook**
```

**Differences**:
- Gold standard says "Template/Notebook Name" (confusing - this field label may vary)
- Regenerated says just "Notebook Name" (clearer in context)
- Gold standard says "Ignore" optional fields
- Regenerated says "Leave optional fields empty for now" (softer, implies they might be useful later)
- Both have identical team dropdown guidance

**Winner**: **Regenerated** - Clearer field label, less dismissive of optional fields

**Recommendation**: ✅ **Adopt regenerated phrasing** - "Leave optional fields empty for now" is better than "Ignore"

---

### Find Your New Notebook

**Gold Standard** (Lines 96-105):
```markdown
### Navigating to your new, blank notebook

After you click 'Create Notebook', you will return to the list of notebooks, where you should:
1. **Find your new notebook**:
   - It will appear at the end of the notebook list
   - **If you have many notebooks**: Look for pagination controls at the bottom of the list (showing "1-10 of X notebooks" with arrow buttons)
   - **Quick tip**: Use the search bar at the top of the list to search for "My First Survey"
   - Scroll down and click through pages until you see your notebook
```

**Regenerated** (Lines 89-97):
```markdown
### Find Your New Notebook

**CRITICAL**: After creation, your notebook will appear at the **END of the notebook list**, not at the beginning.

1. If you have many notebooks, use these navigation tools:
   - **Search bar**: Type "My First Survey" in the search box at the top of the list
   - **Pagination controls**: Look at the bottom for "1-10 of X notebooks" with arrow buttons to navigate pages
2. Scroll through the list to find your notebook (it will be at the end)
3. Click on your notebook name to select it
```

**Differences**:
- Both cover same content
- Regenerated uses **CRITICAL** label (more emphatic)
- Regenerated says "not at the beginning" (explicitly contradicts common assumption)
- Regenerated numbered steps clearer (1. navigation tools, 2. scroll, 3. click)
- Gold standard heading says "Navigating to your new, blank notebook" (longer)
- Regenerated heading says "Find Your New Notebook" (more concise)

**Winner**: **Regenerated** - Clearer structure, better emphasis

**Recommendation**: ✅ **Adopt regenerated structure** - The numbered steps and CRITICAL label are improvements

---

### Notebook Editor Interface Description

**Gold Standard** (Lines 117-122):
```markdown
You'll see the main interface elements:
- **Top bar**: CANCEL and SAVE buttons on the right
- **Action buttons**: UNDO and REDO buttons (below the top bar, above the tabs)
- **Tab bar**: DESIGN and INFO tabs on the left
- **"+" button**: Click to add a new form
- **Form editing area**: Shows "Form Name" field with "Form 1" pre-filled, and "ADD NEW FORM" button
```

**Regenerated** (Lines 112-115):
```markdown
The Editor has three main areas:
- **Top bar**: SAVE and CANCEL buttons (top-right), UNDO and REDO buttons (below top bar)
- **Tab bar**: DESIGN and INFO tabs
- **Form editing area**: Where you'll build your forms, sections, and fields
```

**Differences**:
- Gold standard: 5 bullet points with more detail
- Regenerated: 3 bullet points (consolidates top bar description)
- Gold standard mentions "+" button separately
- Regenerated describes areas more holistically ("three main areas")
- Gold standard says "Form 1 pre-filled" (specific default state)

**Winner**: **Gold standard** - More comprehensive detail

**Recommendation**: ⚪ **Keep gold standard** - The extra detail aids first-time orientation

---

### Step 3: Understanding the Hierarchy

**Gold Standard** (Lines 143-152):
```markdown
Before we add fields, let's understand how Fieldmark organises your data:

**Notebooks** contain **Forms** → **Forms** contain **Sections** → **Sections** contain **Form Fields** (where you enter data)

Think of it like this:
- 📓 **Notebook** = Your entire survey or data collection project ("My First Survey")
- 📋 **Form** = A specific data entry screen ("Site Details", "Environmental Observations", etc.)
- 📂 **Section** = A group of related fields within a form (optional, for organisation)
- ✏️ **Form Field** = Individual data entry points (text boxes, dropdowns, etc.)
```

**Regenerated** (Lines 137-148):
```markdown
Before we start, understand how Fieldmark organises data:

**Notebook** → **Form** → **Section** → **Fields**

You MUST create them in this order:
1. First: Create a Form
2. Then: Create a Section within that form
3. Finally: Add Fields to that section

> ⚠️ **Don't Skip Steps**: You cannot add fields without first creating a section!
```

**Differences**:
- Gold standard: Uses emoji-enhanced analogy (📓 📋 📂 ✏️) with examples
- Regenerated: Emphasizes creation sequence with numbered steps + warning
- Gold standard: More conceptual/educational
- Regenerated: More procedural/action-oriented

**Winner**: **Tie** - Different approaches, both valuable
- Gold standard: Better for conceptual understanding
- Regenerated: Better for preventing errors

**Recommendation**: ⚪ **Merge both approaches** - Combine gold standard's analogy with regenerated's procedural warning

---

### Form Creation

**Both nearly identical** - No significant differences ✓

---

### Section Creation

**Both nearly identical** - No significant differences ✓

---

### Field Configuration

**Gold Standard has 5 fields**:
1. Site Name (FAIMS Text Field)
2. Site Type (Select one option / radio buttons)
3. Survey Date (DateTime with Now button)
4. Observations (Text Field / multiline)
5. Site Photo (TakePhoto)

**Regenerated has 3 fields**:
1. Site Name (FAIMS Text Field)
2. Site Type (Select one option / radio buttons)
3. Site Photo (TakePhoto)

**Differences**:
- Gold standard: 5 fields (more comprehensive)
- Regenerated: 3 fields (follows updated prompt requirement for cognitive load reduction)

**Field 2 Options**:

**Gold Standard** (Lines 245-256):
6 options: Habitation, Mortuary, Ceremonial, Workshop/Industrial, Defensive, Agricultural, Other (7 total)

**Regenerated** (Lines 215-223):
6 options: Habitation, Mortuary, Ceremonial, Agricultural, Industrial, Other (6 total)

**Minor difference**:
- Gold standard: "Workshop/Industrial" and "Defensive" (7 options)
- Regenerated: "Industrial" (simpler, 6 options)

**Winner**: **Regenerated** - 3 fields follows updated best practice (covers same field categories with less cognitive load)

**Recommendation**: ⚪ **Keep regenerated approach** - This was the Session 2 improvement (5→3 fields)

---

### HRID Warning

**Gold Standard** (Lines 338-352):
```markdown
> ⚠️ **CRITICAL: Human-Readable ID Field**
>
> **DO NOT skip this setting!** This is a very common mistake new users make.
>
> Without setting the Human-Readable ID Field, your records will display as:
> - ❌ `rec_a7f3b2c1` (meaningless code)
> - ❌ `rec_9d2e4b8f` (impossible to identify)
> - ❌ `rec_f1c5a39e` (which record is this??)
>
> With Human-Readable ID Field set to "Site Name", your records display as:
> - ✅ `Ancient Temple Site` (instantly recognisable!)
> - ✅ `Northern Settlement` (clear and meaningful)
> - ✅ `Burial Ground Alpha` (easy to find and manage!)
>
> **Set it now before saving!** Changing it later won't fix existing records.
```

**Regenerated** (Lines 286-300):
```markdown
> ⚠️ **CRITICAL: Human-Readable ID Field**
>
> **DO NOT skip this setting!** This is a very common and serious mistake new users make.
>
> Without setting the Human-Readable ID Field, your records will display as:
> - ❌ `rec_a7f3b2c1` (meaningless code - which site is this??)
> - ❌ `rec_9d2e4b8f` (impossible to identify!)
> - ❌ `rec_f1c5a39e` (you'll never find what you're looking for)
>
> With Human-Readable ID Field set to "Site Name", your records display as:
> - ✅ `Ancient Temple Site` (instantly recognisable!)
> - ✅ `Northern Settlement` (clear and meaningful!)
> - ✅ `Burial Ground Alpha` (easy to find and manage!)
>
> **Set it now before saving!** Changing it later won't fix existing records.
```

**Differences**:
- Regenerated adds "and serious" to "very common mistake"
- Regenerated adds inline commentary to the rec_xxxxx examples:
  - "which site is this??"
  - "you'll never find what you're looking for"
- Gold standard says "(which record is this??)" only on line 3

**Winner**: **Regenerated** - More emphatic inline commentary reinforces the pain point

**Recommendation**: ✅ **Adopt regenerated inline commentary** - Makes consequences more visceral

---

### Save Behaviour Warning

**Both nearly identical** - Both warn about no auto-save and Dashboard return ✓

---

### Step 4: Activation

**Both nearly identical** - Both use correct mobile app activation architecture ✓

**Minor wording difference**:

**Gold Standard** (Lines 441-463): More detailed activation explanation
**Regenerated** (Lines 322-354): Slightly more concise

**Verdict**: Both correct and complete ✓

---

### Success Checklist

**Gold Standard** (Lines 571-585):
10 items including:
- "Configured the Human-Readable ID Field (critical step!)"

**Regenerated** (Lines 441-456):
10 items including:
- "Configured the Human-Readable ID Field (critical step!)"
- "Saved your notebook (and understood that SAVE returns you to Dashboard)"

**Difference**: Regenerated explicitly mentions understanding save behaviour in checklist

**Winner**: **Regenerated** - Including save behaviour understanding is good reinforcement

**Recommendation**: ✅ **Adopt regenerated checklist item** - Add save behaviour understanding to gold standard checklist

---

### Troubleshooting Section

**Both have 7 common issues** ✓

**Minor difference in "Editor Closed After Clicking Save"**:

**Gold Standard** (Lines 623-627):
```markdown
**This is expected behaviour**: The Notebook Editor does NOT auto-save. Clicking SAVE closes the Editor
and returns you to the Dashboard. Your work is saved. To resume editing: find your notebook
in the list → Actions → Open in Editor.
```

**Regenerated** (Lines 481-483):
```markdown
**This is expected behaviour**: The Notebook Editor does NOT auto-save. Clicking SAVE closes the Editor and returns you to the Dashboard. Your work is saved! To resume editing, select your notebook → Actions → Open in Editor.
```

**Both essentially identical** - regenerated slightly more concise ✓

---

### What's Next Section

**Gold Standard** (Lines 588-600): More detailed with 6 bullet points

**Regenerated** (Lines 499-510): Similar content, includes pedagogical note about templates at end

**Pedagogical Note in Regenerated** (Line 510):
```markdown
> 💡 **Templates Are Advanced**: We started with direct notebook creation because it's best to
> field-test your design before creating reusable templates. Once you're comfortable with notebooks,
> explore template creation for projects that need repeatable patterns.
```

**Winner**: **Regenerated** - Excellent pedagogical framing about why we used notebook-first approach

**Recommendation**: ✅ **Adopt regenerated pedagogical note** - This reinforces the notebook-first principle

---

### Closing

**Both have similar closing messages** ✓

**Gold standard** (Line 662): "Remember: Every expert was once a beginner..."

**Regenerated** (Line 533): "Remember: Every expert was once a beginner. You've taken your first steps, and that's the hardest part. Keep experimenting, keep learning, and most importantly - keep collecting great data!"

**Winner**: **Regenerated** - More complete and encouraging

**Recommendation**: ✅ **Adopt regenerated closing** - Better encouragement and call to action

---

## Key Improvements to Adopt from Regenerated

### High Priority (Significant Impact)

1. ✅ **Fix URL Error** (Gold Standard Line 45)
   - Change `https://api.fieldmark.app` → `https://dashboard.fieldmark.app`
   - **Impact**: Critical - prevents user confusion

2. ✅ **"What You'll Achieve" Section** (Gold Standard Lines 7-12)
   - Replace with regenerated version (more accurate to tutorial content)
   - **Impact**: Sets better expectations

3. ✅ **Dashboard Interface Description** (Gold Standard Lines 53-58)
   - Replace functional description with regenerated's structural description
   - **Impact**: Better first-time orientation

4. ✅ **"Find Your New Notebook" Structure** (Gold Standard Lines 96-105)
   - Adopt regenerated's numbered steps and CRITICAL label
   - **Impact**: Clearer navigation guidance

5. ✅ **Pedagogical Note about Templates** (Add to Gold Standard "What's Next")
   - Add regenerated's note explaining why notebook-first approach
   - **Impact**: Reinforces learning principle

### Medium Priority (Incremental Improvements)

6. ✅ **Notebook Definition** (Gold Standard Line 32)
   - Add analogy: "like a digital fieldwork form"
   - **Impact**: Aids comprehension

7. ✅ **"Name Your Notebook" Phrasing** (Gold Standard Lines 88-94)
   - Change "Ignore" → "Leave optional fields empty for now"
   - **Impact**: Less dismissive tone

8. ✅ **Step 2 Opening** (Gold Standard Line 75)
   - Add regenerated's IMPORTANT note about notebooks vs templates
   - **Impact**: Prevents confusion upfront

9. ✅ **HRID Warning Inline Commentary** (Gold Standard Lines 338-352)
   - Add inline commentary to rec_xxxxx examples
   - **Impact**: More visceral understanding of consequences

10. ✅ **Success Checklist Item** (Gold Standard Lines 571-585)
    - Add "Saved your notebook (and understood that SAVE returns you to Dashboard)"
    - **Impact**: Reinforces save behaviour understanding

11. ✅ **Closing Message** (Gold Standard Line 662)
    - Replace with regenerated's more complete closing
    - **Impact**: Better encouragement

---

## Summary Statistics

### Overall Metrics

| Metric | Gold Standard | Regenerated | Winner |
|--------|--------------|-------------|--------|
| **Lines** | 663 | 534 | GS (more comprehensive) |
| **Screenshots** | 33 | 15 | GS (2.2x more visual aids) |
| **Field Count** | 5 fields | 3 fields | Regenerated (cognitive load) |
| **Compliance** | 95% | 100% | Regenerated |
| **Production Ready** | ✅ Yes | ✅ Yes | Tie |

### Content Differences

| Section | Significant Difference? | Winner |
|---------|------------------------|--------|
| Title & Opening | ❌ No | Tie |
| What You'll Achieve | ✅ Yes | **Regenerated** |
| Before You Start (URLs) | Minor | Tie |
| Quick Terms | Minor | **Regenerated** (analogy) |
| Step 1: Login | ✅ Yes (URL error) | **Regenerated** |
| Dashboard Description | ✅ Yes | **Regenerated** |
| Step 2: Navigate | ❌ No | Tie |
| Step 2: Name Notebook | Minor | **Regenerated** |
| Step 2: Find Notebook | ✅ Yes | **Regenerated** |
| Editor Interface | Minor | Gold Standard |
| Step 3: Hierarchy | ✅ Yes (approach) | Tie (merge both) |
| Field Configuration | ✅ Yes (3 vs 5 fields) | **Regenerated** |
| HRID Warning | Minor | **Regenerated** |
| Save Behaviour | ❌ No | Tie |
| Step 4: Activation | ❌ No | Tie |
| Success Checklist | Minor | **Regenerated** |
| Troubleshooting | ❌ No | Tie |
| What's Next | ✅ Yes | **Regenerated** (pedagogy) |
| Closing | Minor | **Regenerated** |

---

## Recommendations

### Option 1: Selective Merge (Recommended)

**Keep gold standard as base** (preserves 33 screenshots and accumulated refinements)

**Adopt 11 specific improvements from regenerated**:
1. Fix URL error (api → dashboard)
2. Replace "What You'll Achieve" section
3. Replace Dashboard description
4. Improve "Find Your New Notebook" structure
5. Add pedagogical note about templates
6. Add analogy to Notebook definition
7. Soften "Ignore" → "Leave empty for now"
8. Add IMPORTANT note at Step 2 opening
9. Enhance HRID warning inline commentary
10. Add save behaviour understanding to checklist
11. Replace closing message

**Result**: Best of both worlds - gold standard's depth + regenerated's clarity improvements

### Option 2: Keep Gold Standard As-Is

**Pros**:
- Already production-ready at 95% compliance
- Has 2.2x more screenshots
- All manual curation work preserved

**Cons**:
- Misses 11 incremental improvements
- Has URL error that needs fixing regardless

### Option 3: Switch to Regenerated

**Pros**:
- 100% compliance
- Cleaner structure
- Follows updated best practices (3 fields)

**Cons**:
- Only 15 screenshot placeholders (would need 18 more screenshots added)
- Loses some accumulated manual refinements
- Shorter overall (less comprehensive in some areas)

---

## Final Recommendation

**✅ Option 1: Selective Merge**

1. Use gold standard as base (keep all 33 screenshots)
2. Apply 11 specific improvements from regenerated (listed above)
3. **Critical**: Fix URL error immediately (Line 45)
4. Result: 98-100% compliance with best of both versions

**Time Required**: ~30 minutes to apply 11 targeted edits

**Outcome**: Production-ready guide with gold standard's comprehensive screenshots + regenerated's clarity improvements

---

**Comparison completed**: 2025-10-06
**Analysis type**: Line-by-line section comparison
**Improvements identified**: 11 (1 critical, 4 high-priority, 6 medium-priority)
**Recommendation**: Selective merge (Option 1)
