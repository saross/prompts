# Fieldmark UI Principles - Extracted from Screenshot Analysis
**Generated**: 2025-10-04
**Source**: Quickstart screenshot integration pilot (46 screenshots analysed)
**Coverage**: Notebook Editor + Data Collection App interfaces

---

## Executive Summary

This document captures fundamental UI interaction principles extracted from systematic screenshot analysis during the quickstart guide integration project. These principles are essential for LLM-first documentation, enabling accurate guidance generation without visual inspection.

**Key Finding**: Fieldmark uses **modal dialogs**, not sidebars, for configuration tasks. This architectural choice affects every instruction we generate.

---

## 🎯 Core UI Principles

### 1. Configuration Patterns: Modal Dialogs and Inline Editing {essential}

**Applies to**: Notebook Editor (modal overlay in Dashboard)

**Principle**: The Notebook Editor uses two distinct configuration patterns:
1. **Modal dialogs** for complex selections (field types, conditionals, templated strings)
2. **Inline editing** for simple text and settings (form names, section names, field configuration, form settings)

**Modal Dialog Pattern - Used for**:
- Field type selection (tabbed categories: TEXT, CHOICE, DATE & TIME, MEDIA, LOCATION, STRUCTURED, RELATIONSHIP)
- Complex field configuration (conditionals, templated strings)
- Component selection that requires browsing options

**Inline Editing Pattern - Used for**:
- Form name editing (click "EDIT FORM NAME" → inline text field with ✓/✗ buttons)
- Section name editing (type in field → click "+" to confirm)
- Field configuration (click grey bar to expand → configure options in place)
- Form Settings (click grey bar to expand → configure dropdowns in place)

**Impact on Documentation**:
- ❌ WRONG: "In the right sidebar, select FAIMS Text Field"
- ✅ RIGHT (Modal): "In the 'Add a field' dialog, click the TEXT tab and select 'FAIMS Text Field'"
- ✅ RIGHT (Inline): "Click 'EDIT FORM NAME', type the new name, then click the checkmark (✓) to confirm"

**Screenshots**: `quickstart-009-add-field-site-name.png`, `quickstart-011-add-field-choice.png`, `quickstart-014-add-field-datetime.png`, `quickstart-018-add-field-media.png`

---

### 2. Collapse/Expand Interaction Pattern {essential}

**Applies to**: Notebook Editor (modal overlay in Dashboard)

**Principle**: Collapsible grey bars are used for Fields (Visible and Hidden), Form Settings, and when present, Hidden Fields. Users must click the grey bar to expand configuration options.

**What uses this pattern**:
- **Visible Fields**: Collapsed by default, click grey bar to expand field configuration
- **Hidden Fields** (if any are added): Same collapse/expand pattern as Visible Fields
- **Form Settings**: Collapsed grey bar below form name, expands to show settings (Finish Button Behaviour, Layout Style, Summary Fields, Human-Readable ID Field)
- **"Expand All Fields" button**: Located immediately to the right of "ADD A FIELD" button, expands all fields at once

**Evidence**:
- All fields appear as collapsed grey bars initially
- Clicking the grey bar reveals full configuration form
- Expanded view shows: Label, Field ID, Helper Text, Required checkbox, other options
- Each field can be independently expanded/collapsed
- Form Settings panel uses same grey bar interaction

**User Pattern**:

1. Add field via modal → field appears collapsed in list
2. Click grey bar → field expands to show configuration
3. Configure options → click grey bar again to collapse
4. Repeat for next field OR click "EXPAND ALL FIELDS" to expand all at once

**Impact on Documentation**:
- Every field addition requires explicit "Click on the grey bar to expand the field" instruction (unless using "EXPAND ALL FIELDS")
- Cannot skip this step - configuration is invisible when collapsed
- Same pattern applies to Form Settings, Hidden Fields

**Screenshots**: `quickstart-010-site-name-expanded.png`, `quickstart-013-site-type-expanded.png`, `quickstart-015-survey-date-expanded.png`

---

### 3. Tab-Based Navigation {essential}

**Applies to**: Notebook Editor (modal overlay in Dashboard)

**Principle**: The Notebook Editor uses tabs (DESIGN / INFO), not multiple screens or wizards.

**Evidence**:

- DESIGN tab: Form building interface (always shown first)
- INFO tab: Metadata configuration (notebook name, project lead, description, custom key-value pairs)
- Active tab shows green text AND green underline indicator
- Tab bar positioned below UNDO/REDO buttons, above form editing area

**Impact on Documentation**:

- Instructions must specify which tab to use
- "In the DESIGN tab, click ADD A FIELD"
- "Switch to INFO tab to add project metadata"

**Screenshots**: `quickstart-004-editor-interface.png`

---

### 4. Action Button Placement {essential}

**Applies to**: Notebook Editor (modal overlay in Dashboard)

**Principle**: Primary actions live in specific, consistent locations.

**Layout Hierarchy** (top to bottom):
```
┌─────────────────────────────────────────┐
│ Top Bar: CANCEL (left) | SAVE (right)   │
├─────────────────────────────────────────┤
│ Action Buttons: UNDO | REDO             │  ← BELOW top bar
├─────────────────────────────────────────┤
│ Tabs: DESIGN | INFO                     │
├─────────────────────────────────────────┤
│ Form Editing Area                       │
└─────────────────────────────────────────┘
```

**Critical Correction**:
- UNDO/REDO buttons are **below the top bar**, **above the tabs** (not in the top bar itself)
- This was a key user correction during screenshot review

**Impact on Documentation**:
- Visual hierarchy must be described accurately for non-sighted users
- "Below the top bar, above the tabs" language is precise

**Screenshots**: `quickstart-004-editor-interface.png`, `quickstart-128` (same as 004)

---

### 5. Inline Editing with Confirmation {important}

**Applies to**: Notebook Editor (modal overlay in Dashboard)

**Principle**: Simple text edits (form names, section names) use inline editors with checkmark/X confirmation buttons, not modal dialogs.

**Evidence**:
- Click "EDIT FORM NAME" → inline text field appears with ✓ and ✗ buttons
- Section Name field → type name → click "+" button to confirm
- No modal dialog for simple text edits
- Confirmation required before changes apply

**Pattern**:
```
[Edit Mode ON] → [Text Field] [✓] [✗]
                    ↓ click ✓
[Edit Mode OFF] → [Updated Text Displayed]
```

**Impact on Documentation**:
- Distinguish between inline edits (checkmark/X) and modal dialogs (SAVE/CANCEL buttons)
- "Click the checkmark to confirm" vs "Click the ADD FIELD button"

**Screenshots**: `quickstart-005-form-name-editing.png`, `quickstart-007-section-name-editing.png`

---

### 6. Field Category Organisation {essential}

**Applies to**: Notebook Editor (modal overlay in Dashboard) - specifically the "Add a field" modal dialog

**Principle**: Field types are organised in horizontal tabs with scrollable categories, NOT a dropdown or sidebar tree.

**Tab Structure**:

- First page tabs: ALL, TEXT, NUMBERS, DATE & TIME, MEDIA, LOCATION
- Additional tabs accessible via right chevron (>) button: CHOICE, STRUCTURED, RELATIONSHIP
- Each tab shows 1-6 field type cards
- Cards show icon + field type name
- Selected field has green border highlight
- Hovering over a card displays helper text

**Navigation**:

- User sees first 6 tabs initially
- Must click ">" to see CHOICE tab (for radio buttons, checkboxes)
- Cannot search - must navigate tabs

**Impact on Documentation**:

- Must specify exact tab name: "Click the CHOICE tab"
- Must indicate when chevron navigation needed: "Click the right chevron (>) to see more options"
- Cannot say "find" or "search for" - tabs must be navigated

**Screenshots**: `quickstart-009-add-field-site-name.png`, `quickstart-011-add-field-choice.png`, `quickstart-014-add-field-datetime.png`, `quickstart-018-add-field-media.png`

---

### 7. Annotation & Uncertainty UI Pattern {comprehensive}

**Applies to**: Data Collection App

**Principle**: Annotation and Uncertainty features use a "blue dog ear" icon to reveal additional input areas, NOT separate fields.

**Interaction**:

1. Field has blue dog ear icon on right side (when Annotation or Uncertainty enabled)
2. Click icon → annotation text area and/or uncertainty checkbox appear below field
3. These are supplementary inputs, not separate fields in the form structure
4. Icon only appears if Annotation or Uncertainty is toggled ON in field configuration

**Use Cases**:

- Annotation: Add contextual notes about data entry (e.g., "Site type is uncertain, may be workshop")
- Uncertainty: Flag observations that require review
- Both can be enabled together

**Impact on Documentation**:

- Annotation ≠ separate field, it's a feature of the parent field
- "Blue dog ear icon" is the consistent visual indicator
- Users must know to look for the icon

**Screenshots**: `quickstart-029-annotation-interface.png`

---

### 8. Progress Indication in Forms {important}

**Applies to**: Data Collection App

**Principle**: Data entry forms show a percentage completion bar at the top, calculated from required fields.

**Behaviour**:
- Progress bar shows "X% Completed"
- Percentage increases as required fields are filled
- Reaches 100% when all required fields have values
- Optional fields don't affect percentage
- Required fields marked with red asterisk (*)

**User Experience**:
- Provides feedback on form completion status
- Helps users know if they can save/submit
- Visible at all times during data entry

**Impact on Documentation**:
- Progress bar is visual feedback, not interactive
- Can be used as "You'll Know It Worked" indicator
- "Progress bar should show 33%" = specific milestone

**Screenshots**: `quickstart-028-form-33-percent.png`, `quickstart-030-form-100-percent.png`

---

### 9. Sync Status Visual Language {important}

**Applies to**: Data Collection App

**Principle**: Record sync status is communicated through colour-coded icons in the "Sync" column.

**Icon States**:
- **Orange three-dot icon**: Record not yet synced to server (local only)
- **Green cloud with checkmark**: Record successfully synced to server
- Icons appear in leftmost "Sync" column of record list table

**Sync Behaviour**:
- Automatic when online (no user action required)
- "REFRESH RECORDS" button refreshes view from local database (doesn't trigger sync)
- Offline-first: data saved locally even without connection

**Impact on Documentation**:
- "Orange icon" and "green cloud icon" are precise visual indicators
- Must clarify REFRESH RECORDS ≠ sync trigger
- Sync happens automatically in background

**Screenshots**: `quickstart-032-record-not-synced.png`, `quickstart-033-record-synced.png`

---

### 10. Form Settings Expandable Panel {important}

**Applies to**: Notebook Editor (modal overlay in Dashboard)

**Principle**: Form Settings is a collapsible grey panel, not a separate screen or modal.

**Location & Behaviour**:
- Located below "FORM: [NAME]" badge in Editor
- Expands/collapses by clicking anywhere on grey bar
- Contains 4 key settings:
  - Finish Button Behaviour (dropdown)
  - Layout Style (dropdown)
  - Summary Fields (multi-select dropdown)
  - Human-Readable ID Field (dropdown)

**Visual Pattern**:
- Collapsed: Grey bar with "Form Settings" text and chevron icon
- Expanded: Shows all four configuration options with labels

**Impact on Documentation**:
- Users might miss this if not told to expand
- "Click anywhere in the grey 'Form Settings' bar to expand" is necessary instruction
- Settings are critical for usability (Summary Fields, HRID) but hidden by default

**Screenshots**: `quickstart-021-form-settings-panel.png`, `quickstart-022-form-settings-configured.png`

---

### 11. Data Collection App Navigation {essential}

**Applies to**: Data Collection App

**Principle**: Data Collection App uses tab-based navigation at notebook level, with separate tabs for records, settings, and other functions.

**Tab Structure**:

- **MY RECORDS (X)** or **MY [FORMNAME] (X)**: Record list showing records created by the current user (X = count)
  - Notebooks with a single visible form type display: `My [FormLabel]s` (e.g., "My Site Details")
  - Notebooks with multiple visible forms display: `My Records`
- **OTHER RECORDS (X)** or **OTHER [FORMNAME] (X)**: Records collected by other team members that have synced with your device (X = count). Hidden unless there is at least one other record.
  - Same labelling logic as MY RECORDS tab (form-specific or generic)
- **DETAILS**: Notebook information and description
- **SETTINGS**: Sync configuration, deactivation options
- **MAP**: Geographic view of records (if location fields present)

**Above Tabs**:

- Form creation buttons (orange): Create new record for specific form types (e.g., "THING 2", "THING 1")
- **REFRESH RECORDS** button (green): Refresh list from local DB

**Impact on Documentation**:

- Must specify tab: "Click the SETTINGS tab"
- Button locations are above tabs, not within them
- OTHER RECORDS tab visibility depends on sync status with team members
- Tab labels are dynamic: single-form notebooks show form-specific labels (e.g., "My Site Details"), multi-form notebooks show generic "My Records"

**Screenshots**: `quickstart-027-empty-notebook.png`, `quickstart-034-settings-tab.png`

---

### 12. Activation Workflow Modal Pattern {comprehensive}

**Applies to**: Data Collection App

**Principle**: Notebook activation uses a confirmation modal with detailed explanation, not a simple "Are you sure?" dialog.

**Modal Contents**:
- Blue information icon
- Explanation text (offline functionality, data download)
- Warning about internet connection requirements
- Note about features (e.g., "de-activation not available yet")
- Primary action: Green "ACTIVATE" button
- Secondary action: "CANCEL" button

**Context**:
- Appears when user clicks "ACTIVATE" button next to notebook in NOT ACTIVE tab
- Modal explains what activation means (downloads notebook structure for offline use)
- After confirmation, automatically switches to ACTIVE tab

**Impact on Documentation**:
- Activation is two-step (button → modal → confirm)
- Modal provides educational content, not just confirmation
- Users need to understand offline-first implications

**Screenshots**: `quickstart-025-activating-modal.png`

---

### 13. Dashboard vs Data Collection App Distinction {essential}

**Applies to**: Both Dashboard and Data Collection App

**Principle**: Two separate applications with different URLs and purposes, NOT different views of the same app. The Notebook Editor is a modal overlay spawned from the Dashboard.

**Dashboard** (`https://dashboard.fieldmark.app`):

- Notebook design and configuration
- Template management
- User and team administration
- **Notebook Editor**: Modal overlay (not a separate page) for building notebooks
- Desktop/laptop recommended (web app accessible from any device)

**Data Collection App** (`https://app.fieldmark.app`):

- Mobile-optimised data entry
- Record creation and editing
- Offline-first operation
- Field data collection
- Works on mobile devices and web browsers

**User Workflow**:

1. Design notebook in Dashboard (desktop recommended)
2. Activate notebook in Data Collection App (mobile/desktop)
3. Collect data in Data Collection App (mobile recommended)
4. Export/analyse from Dashboard (desktop)

**Impact on Documentation**:

- Must specify which app for each task
- Notebook Editor is a modal overlay in Dashboard, not a separate application
- URLs are different (dashboard.fieldmark.app vs app.fieldmark.app)
- Cannot design forms in Data Collection App
- Cannot collect data in Dashboard

**Screenshots**: `quickstart-001-login.png` (can apply to both), `quickstart-002-dashboard-overview.png`, `quickstart-027-empty-notebook.png`

---

### 14. Save Behaviour in Notebook Editor {critical}

**Applies to**: Notebook Editor (modal overlay in Dashboard)

**Principle**: Notebook Editor does NOT auto-save. Clicking SAVE closes the Editor and returns to Dashboard.

**Behaviour**:
- Green SAVE button in top-right corner
- Clicking SAVE:
  1. Saves all changes
  2. Closes Notebook Editor
  3. Returns to Dashboard notebook list
- To continue editing: Click "Open in Editor" again from Dashboard
- CANCEL button discards changes and returns to Dashboard

**User Implications**:
- Must click SAVE periodically (every few fields added)
- Editor will close after each save
- Immediate re-entry is possible but requires navigation
- Lost work if browser closes without saving

**Impact on Documentation**:
- Must warn about non-auto-save behaviour
- Explain expected "return to Dashboard" behaviour
- Provide "resume editing" instructions
- Encourage frequent saves

**Screenshots**: `quickstart-004-editor-interface.png` (shows SAVE button placement)

---

### 15. Pagination Controls in Dashboard {important}

**Applies to**: Dashboard (Notebooks, Templates, Users, and Teams all use the same pagination controls)

**Principle**: Lists use pagination controls, NOT infinite scroll.

**Elements**:

- "Filter results..." search bar at top
- "Rows per page" dropdown (default 5)
- "Page X of Y" indicator
- Navigation buttons: ⟨⟨ ⟨ ⟩ ⟩⟩ (first, previous, next, last)
- Located at bottom-right of list table

**Behaviour**:

- New items appear at END of list (last page)
- Must navigate to last page to find recently created items
- Search bar provides faster access by name

**Impact on Documentation**:

- Must explain how to find new items (pagination or search)
- Cannot assume "scroll down" - must say "navigate to last page"
- Search is preferred method for locating items

**Screenshots**: `quickstart-003-notebooks-pagination.png`

---

## 🔄 Cross-Platform Consistency Observations

**Applies to**: Both Dashboard and Data Collection App

### Desktop vs Mobile Differences

**Consistent Elements** (same on desktop and mobile):

- Field types and configuration options
- Form structure (forms → sections → fields)
- Sync status indicators
- Data entry form layout

**Platform-Specific Features**:

**Dashboard and Notebook Editor**:
- Accessible from any device (web app)
- Desktop/laptop recommended for better screen size and mouse/keyboard input
- Can be accessed from mobile devices if needed

**Data Collection App**:
- Accessible from both mobile and web browsers
- **Barcode/QR code scanning**: Mobile-only (not yet available in web app)
- Camera integration: More convenient on mobile devices
- GPS/location capture: More convenient on mobile devices
- Relative parity attempted between mobile and web for data collection

**Impact on Documentation**:

- Specify device type for each task
- Dashboard/Notebook Editor = desktop/laptop recommended (not desktop-only)
- Data collection = mobile or desktop, with mobile recommended for camera/GPS features
- Barcode/QR scanning = mobile-only
- Some features behave differently on mobile (keyboard types, date pickers)

---

## 📐 Layout and Visual Hierarchy Principles

**Applies to**: Notebook Editor (modal overlay in Dashboard)

### Vertical Structure (Notebook Editor)

```
┌─────────────────────────────────────────┐
│ LEVEL 1: Top Bar (always visible)       │
│   Left: "Notebook Editor" title         │
│   Right: CANCEL | SAVE                  │
├─────────────────────────────────────────┤
│ LEVEL 2: Action Buttons                 │
│   UNDO | REDO (greyed when unavailable) │
├─────────────────────────────────────────┤
│ LEVEL 3: Tab Navigation                 │
│   DESIGN | INFO                         │
│   (active tab: green underline)         │
├─────────────────────────────────────────┤
│ LEVEL 4: Blue Info Box                  │
│   Instructional text for guidance       │
├─────────────────────────────────────────┤
│ LEVEL 5: Form Editing Area              │
│   Form tabs (if multiple forms)         │
│   Form name + "ADD NEW FORM" button     │
│   Form Settings panel (collapsible)     │
│   Section name + "+" button             │
│   Section editing controls              │
│   ADD A FIELD button                    │
│   Visible Fields list (expandable)      │
│   Hidden Fields list                    │
└─────────────────────────────────────────┘
```

**Critical Spatial Relationships**:
- UNDO/REDO ≠ in top bar (they're below it)
- Blue info box = guidance, not error message
- Form tabs appear if multiple forms exist (tabbed interface)

---

## 🎨 Visual Indicators and Colour Coding

**Applies to**: Dashboard, Notebook Editor, and Data Collection App (colour coding is consistent across all components)

### Button Colours

| Colour | Meaning | Examples |
|-------|---------|----------|
| **Green** | Primary action / Confirm | SAVE, ACTIVATE, ADD FIELD, ADD NEW FORM, TAKE FIRST PHOTO |
| **Orange** | Create new / Warning | ADD NEW SITE DETAILS, Sync status (not synced), FINISH AND NEW |
| **Red** | Delete / Destructive | DELETE FORM, DELETE SECTION, DEACTIVATE NOTEBOOK, Required field asterisk (*) |
| **Grey** | Secondary / Cancel | CANCEL, UNDO (when disabled), REDO (when disabled), Collapsed field bars |
| **Blue** | Information | Info box, Dog ear annotation icon |

### Status Indicators

| Indicator | Meaning |
|-----------|---------|
| Orange three-dot icon | Record not synced |
| Green cloud + checkmark | Record synced successfully |
| Red asterisk (*) | Required field |
| Green checkmark badge | Field requirement enabled (Required, Annotation, etc.) |
| Number badge (e.g., "1") | Section number in sequence |

---

## 💡 Interaction Patterns by Task Type

### Pattern 1: Adding a Field

**Applies to**: Notebook Editor (modal overlay in Dashboard)

```
1. Click "ADD A FIELD" button (green, with + icon)
2. Modal dialog opens with tabbed categories
3. Navigate to appropriate tab (TEXT, CHOICE, etc.)
4. Click desired field type card (shows green border when selected)
5. Field name auto-fills with "New Field" → change to desired name
6. Click "ADD FIELD" button at bottom of modal
7. Modal closes, field appears collapsed in "Visible Fields" list
8. Click grey bar to expand field
9. Configure field options (Label, Helper Text, Required, etc.)
10. Click grey bar to collapse field (or move to next task)
```

**Key Points**:
- 10 distinct steps for one field
- Modal → List → Expand → Configure is the flow
- Cannot skip "expand" step to access configuration

### Pattern 2: Editing Text (Form Name, Section Name)

**Applies to**: Notebook Editor (modal overlay in Dashboard)

```
1. Click "EDIT [NAME]" button OR type in name field
2. Inline text editor appears with checkmark (✓) and X buttons
3. Enter or modify text
4. Click checkmark (✓) to confirm
5. OR click X to cancel
6. Inline editor closes, updated text displays
```

**Key Points**:
- Inline editing, not modal
- Must confirm with checkmark
- X cancels changes (doesn't save)

### Pattern 3: Creating a Notebook

**Applies to**: Dashboard

```
1. Dashboard → Click "Notebooks" in left sidebar
2. Click "+ Create Notebook" button
3. Modal dialog opens
4. Enter notebook name
5. Select team from dropdown
6. Optionally fill other fields
7. Click "CREATE NOTEBOOK" button
8. Modal closes, returns to notebook list
9. Navigate to last page of pagination OR use search bar
10. Find newly created notebook
11. Click notebook name → Click Actions tab → Click "Open in Editor"
```

**Key Points**:
- New items appear at END of list
- Must navigate pagination to find
- Search is faster for location

---

## 🔍 Discovered Terminology Patterns

### Consistent Terms (Always Use These)

| Correct Term | Avoid | Context |
|--------------|-------|---------|
| **Notebook Editor** | "Form Editor", "Designer", "Builder" | The interface for building notebooks |
| **Data Collection App** | "Mobile app", "Field app", "App" | Where data entry happens |
| **Dashboard** | "Control Centre", "Admin panel" | Main navigation hub |
| **Visible Fields** | "Field list", "Fields section" | List of fields in a section |
| **Grey bar** | "Field header", "Collapsed field" | Clickable element to expand fields |
| **Modal dialog** | "Popup", "Window", "Dialog box" | Centreed overlay for actions |
| **Blue dog ear icon** | "Annotation button", "Flag" | Icon to reveal annotation/uncertainty |
| **ADD A FIELD** | "Add field", "New field", "+ Field" | Exact button text to use |
| **REFRESH RECORDS** | "Sync button", "Update" | Button to refresh view from local DB |

### Terms to Clarify in Documentation

| Term | Clarification Needed |
|------|---------------------|
| "Activate" | Downloads notebook structure for offline use (NOT the same as "enable" or "turn on") |
| "Sync" | Automatic background process (NOT manual, REFRESH RECORDS doesn't trigger it) |
| "Close" | = Archive (same operation, different terminology in UI) |
| "Form" | A data entry screen within a notebook (NOT the entire notebook) |
| "Section" | A group of fields within a form (optional organisational unit) |
| "Field" | Individual data input element (the atomic unit) |

---

## 📝 Appendix: Screenshot Evidence Index

| Principle | Evidence Screenshots |
|-----------|---------------------|
| Configuration Patterns | `quickstart-009`, `011`, `014`, `018` |
| Collapse/Expand Pattern | `quickstart-010`, `013`, `015`, `017`, `019` |
| Tab-Based Navigation | `quickstart-004` |
| Action Button Placement | `quickstart-004` |
| Inline Editing | `quickstart-005`, `007` |
| Field Category Organisation | `quickstart-009`, `011`, `014`, `018` |
| Annotation & Uncertainty | `quickstart-029` |
| Progress Indication | `quickstart-028`, `030` |
| Sync Status | `quickstart-032`, `033` |
| Form Settings Panel | `quickstart-021`, `022` |
| Data Collection Navigation | `quickstart-027`, `034` |
| Activation Workflow | `quickstart-025` |
| Dashboard vs Data Collection | `quickstart-002`, `027` |
| Save Behaviour | `quickstart-004` |
| Pagination Controls | `quickstart-003` |

---

**Generated from**: Systematic analysis of 46 screenshots captured during quickstart guide integration pilot
**Next Update**: After analysis of additional UI components (map interface, template designer advanced features, etc.)
