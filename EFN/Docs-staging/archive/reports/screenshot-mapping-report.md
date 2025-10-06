# Screenshot Mapping Report
**Generated**: 2025-10-03
**Analysis**: Claude vision matching for Quickstart Guide

## Summary
- **Total placeholders**: 32
- **Total screenshots**: 33
- **Good matches**: 23
- **Needs retake**: 9
- **Missing completely**: 6

---

## ✅ Good Matches (23)

### Dashboard & Getting Started
| Placeholder | Line | Description | Screenshot | Status |
|------------|------|-------------|------------|--------|
| Dashboard Overview | 59 | Dashboard showing main navigation | `Screenshot from 2025-10-02 18-40-51.png` | ✅ Good |
| Notebooks interface | 84 | Notebooks with Create button | `Screenshot from 2025-10-02 18-40-51.png` | ✅ Good |

### Notebook Editor - Form Creation
| Placeholder | Line | Description | Screenshot | Status |
|------------|------|-------------|------------|--------|
| Notebook Editor interface | 115 | Main editor layout | `Screenshot from 2025-10-02 23-16-05.png` | ✅ Excellent |
| UNDO/REDO buttons | 128 | Close-up of UNDO/REDO below top bar | `Screenshot from 2025-10-02 23-16-05.png` | ✅ Good |
| Form created "Site Details" | 174 | Created form with success message | `Screenshot from 2025-10-01 22-06-00.png` | ✅ Good |
| Section created "Basic Information" | 197 | Created section with ADD A FIELD button | `Screenshot from 2025-10-01 22-14-51.png` | ✅ Excellent |

### Field Creation - Site Type (Choice)
| Placeholder | Line | Description | Screenshot | Status |
|------------|------|-------------|------------|--------|
| "Add a field" - CHOICE category | 250 | Dialog showing "Select one option" | `Screenshot from 2025-10-02 15-38-57.png` | ✅ Excellent |
| Edit Option dialog | 262 | Changing "1" to "Habitation" | `Screenshot from 2025-10-02 15-53-41.png` | ✅ Good |
| Expanded "Site Type" field | 272 | Options list with Required/Annotation/Uncertainty | `Screenshot from 2025-10-02 15-58-56.png` | ✅ Excellent |

### Field Creation - Survey Date (Date/Time)
| Placeholder | Line | Description | Screenshot | Status |
|------------|------|-------------|------------|--------|
| "Add a field" - DATE & TIME | 305 | Dialog showing "Date and Time with Now button" | `Screenshot from 2025-10-02 16-08-37.png` | ✅ Excellent |

### Field Creation - Observations (Text)
| Placeholder | Line | Description | Screenshot | Status |
|------------|------|-------------|------------|--------|
| "Add a field" - TEXT tab | 335 | Dialog showing "Text Field" with "Observations" | `Screenshot from 2025-10-02 17-15-31.png` | ✅ Good |
| Expanded "Observations" field | 344 | Configuration with rows to display | `Screenshot from 2025-10-02 17-18-22.png` | ✅ Good |

### Form Settings
| Placeholder | Line | Description | Screenshot | Status |
|------------|------|-------------|------------|--------|
| All five fields visible | 387 | Visible Fields list complete | `Screenshot from 2025-10-02 17-36-14.png` | ✅ Excellent |
| Form Settings panel | 393 | Configuration options visible | `Screenshot from 2025-10-02 17-29-25.png` | ✅ Good |
| Form Settings configured | 403 | Always Show, Tabs, selections shown | `Screenshot from 2025-10-02 17-37-35.png` | ✅ Excellent |

### Activation Workflow
| Placeholder | Line | Description | Screenshot | Status |
|------------|------|-------------|------------|--------|
| NOT ACTIVE tab | 447 | List of notebooks with ACTIVATE buttons | `Screenshot from 2025-10-02 17-53-59.png` | ✅ Good |
| "Activating Notebooks" modal | 455 | Dialog with warning and ACTIVATE/CANCEL | `Screenshot from 2025-10-02 18-01-18.png` | ✅ Excellent |
| ACTIVE (1) tab | 464 | "Quickstart-test" in active list | `Screenshot from 2025-10-02 18-02-37.png` | ✅ Good |

### Data Collection
| Placeholder | Line | Description | Screenshot | Status |
|------------|------|-------------|------------|--------|
| Empty notebook view | 497 | Interface elements and empty table | `Screenshot from 2025-10-02 18-14-40.png` | ✅ Excellent |
| Data entry form 33% | 505 | Site Name and Site Type fields, progress bar | `Screenshot from 2025-10-02 18-17-28.png` | ✅ Good |
| Annotation interface | 517 | Annotation text + uncertainty checkbox | `Screenshot from 2025-10-02 18-29-16.png` | ✅ Excellent |
| Complete form 100% | 545 | All fields filled, TAKE FIRST PHOTO button | `Screenshot from 2025-10-02 18-22-20.png` | ✅ Good |
| Date/time picker open | 557 | Calendar open, action buttons visible | `Screenshot from 2025-10-02 18-25-25.png` | ✅ Good |
| Orange sync icon | 565 | Record with three-dot icon (not synced) | `Screenshot from 2025-10-02 18-33-31.png` | ✅ Good |
| Green sync icon | 582 | Record with cloud checkmark (synced) | `Screenshot from 2025-10-02 18-38-31.png` | ✅ Good |

---

## ⚠️ Needs Retake (9)

### Critical Issues - Wrong Content
| Placeholder | Line | Description | Current Screenshot | Issue | Priority |
|------------|------|-------------|-------------------|-------|----------|
| Form Name → "Site Details" | 163 | Form Name field being edited, ADD NEW FORM highlighted | *No exact match* | Have form creation but not the specific "Form 1" → "Site Details" editing step | HIGH |
| Section Name → "Basic Information" | 186 | Section Name field being edited, "+" button highlighted | *No exact match* | Have section created but not the specific editing step | HIGH |
| "Add a field" - Site Name dialog | 219 | Dialog with "Site Name" + "FAIMS Text Field" selected | `Screenshot from 2025-10-01 22-28-06.png` (shows ALL tab, field name is "New Field") | Field name should be "Site Name", FAIMS Text Field should be highlighted | HIGH |
| Expanded "Site Name" field | 228 | Configuration with Required toggled ON | `Screenshot from 2025-10-01 22-38-16.png` (Required is OFF, not ON) | Required checkbox needs to be checked | MEDIUM |
| Expanded "Survey Date" field | 315 | Time pre-populated checked, Required enabled | `Screenshot from 2025-10-02 16-11-54.png` (Time pre-populated is unchecked) | Checkbox state incorrect | MEDIUM |
| "Add a field" - MEDIA "Take Photo" | 367 | Dialog showing MEDIA tab with "Take Photo" highlighted | *No exact match* | Need dialog open to MEDIA tab | HIGH |
| Expanded "Site Photo" field | 378 | Configuration showing Take Photo field settings | *Partial match only* | Have field visible in list but not expanded configuration | HIGH |

### Visual/Technical Issues
| Placeholder | Line | Description | Current Screenshot | Issue | Priority |
|------------|------|-------------|-------------------|-------|----------|
| URLs comparison | 25 | Two browser windows side by side (Dashboard vs Data Collection App) | *Missing* | Need two windows showing different URLs | LOW |
| "My Notebooks" ACTIVE (0) | 441 | Home screen showing 0 active notebooks | `Screenshot from 2025-10-02 17-53-59.png` (shows NOT ACTIVE tab, not ACTIVE (0)) | Wrong tab visible | MEDIUM |

---

## ❌ Missing Completely (6)

| Placeholder | Line | Description | Why Missing | Priority |
|------------|------|-------------|-------------|----------|
| Login page | 49 | Email and password fields | No login screenshot captured | LOW |
| Pagination controls | 105 | Notebook list showing pagination "< 1 2 3 >" and search bar | Dashboard screenshot doesn't show pagination | MEDIUM |
| SETTINGS tab | 590 | Sync toggle ON, Get attachments Off, Deactivate section | No Settings tab screenshot | MEDIUM |

**Additional missing:**
- **URLs comparison (Line 25)**: Two browser windows side by side showing Dashboard vs Data Collection App URLs
- **Login page (Line 49)**: Authentication screen
- **Pagination controls (Line 105)**: Need notebook list with pagination visible

---

## 📋 Retake Instructions

### For exact documentation match, please capture:

#### HIGH Priority (7 screenshots needed)

1. **Form Name editing** (Line 163)
   - Show Form Name field with "Site Details" typed in
   - ADD NEW FORM button should be highlighted/visible
   - Before: shows "Form 1", After: shows "Site Details"

2. **Section Name editing** (Line 186)
   - Show Section Name field with "Basic Information" typed in
   - "+" button should be highlighted/visible
   - Capture the editing moment

3. **"Add a field" dialog - Site Name** (Line 219)
   - Open "Add a field" dialog
   - Field name: "Site Name" (not "New Field")
   - ALL or TEXT tab active
   - "FAIMS Text Field" option should be highlighted

4. **Expanded "Site Name" field** (Line 228)
   - Site Name field expanded
   - **Required checkbox must be CHECKED** (currently unchecked in screenshot)

5. **"Add a field" dialog - MEDIA tab** (Line 367)
   - Open "Add a field" dialog
   - Click on MEDIA tab
   - "Take Photo" option should be highlighted

6. **Expanded "Site Photo" field** (Line 378)
   - Site Photo field expanded showing full configuration
   - Show all settings for Take Photo field

7. **URLs comparison** (Line 25)
   - **Two browser windows** side by side
   - Left: Dashboard at `https://dashboard.fieldmark.app`
   - Right: Data Collection App at `https://app.fieldmark.app`
   - Add labels if possible

#### MEDIUM Priority (4 screenshots needed)

8. **Expanded "Survey Date" field** (Line 315)
   - Survey Date field expanded
   - **"Time pre-populated" checkbox must be CHECKED**
   - Required should be enabled

9. **"My Notebooks" ACTIVE (0) tab** (Line 441)
   - Must show **ACTIVE (0)** tab selected (not NOT ACTIVE)
   - Empty state with 0 active notebooks
   - Text explaining activation needed

10. **Pagination controls** (Line 105)
    - Notebook list with **multiple pages**
    - Show pagination controls: "< 1 2 3 >" at bottom
    - Search bar at top
    - Point to specific notebook in list

11. **SETTINGS tab** (Line 590)
    - In Data Collection App, open SETTINGS tab
    - Show "Sync Notebook" toggle ON
    - "Get attachments from other devices" toggle OFF
    - "Deactivate Notebook" section visible

#### LOW Priority (1 screenshot needed)

12. **Login page** (Line 49)
    - Email field
    - Password field
    - Login button
    - At `https://dashboard.fieldmark.app` or `https://app.fieldmark.app`

---

## 🎯 Screenshot Naming Convention (for retakes)

Use this format: `quickstart-{number}-{descriptor}.png`

Examples:
- `quickstart-001-url-comparison.png`
- `quickstart-002-login-page.png`
- `quickstart-003-form-name-editing.png`
- `quickstart-004-site-name-dialog.png`

---

## 📊 Next Steps

1. **User reviews this report** ✓
2. **User captures 12 retake screenshots** (following instructions above)
3. **Save retakes to** `/screenshots/quickstart/raw/`
4. **Re-run Claude vision analysis** on complete set
5. **Compare with qwen2.5-vl:72b** (optional overnight test)
6. **Rename all screenshots** with final convention
7. **Update markdown placeholders** with actual screenshot references
