# Screenshot Deletion Review List

**Date**: 2025-10-06
**Purpose**: Files recommended for deletion after systematic review

## ✅ Action Completed

- **46 screenshots identified and mapped**
- **15 actively-used screenshots renamed** to proper `quickstart-XXX-raw-YYYY-MM-DD.png` format
- **5 unused screenshots already moved** from final/ to raw/

## 📋 Files Recommended for Deletion

### Category 1: Superseded by 2025-10-06 Versions (9 files)

These have fresh replacements that are already in use:

```
Screenshot from 2025-10-01 21-48-43.png  ← quickstart-004 (editor interface)
Screenshot from 2025-10-02 15-38-57.png  ← quickstart-011 (add field CHOICE)
Screenshot from 2025-10-02 15-45-56.png  ← quickstart-012 (edit option)
Screenshot from 2025-10-02 17-36-14.png  ← quickstart-020 (4 fields, now 3)
Screenshot from 2025-10-02 18-17-28.png  ← quickstart-028 (33%, now 0%)
Screenshot from 2025-10-02 18-22-20.png  ← quickstart-030 (no photo, now with photo)
Screenshot from 2025-10-02 18-25-25.png  ← quickstart-031 (date picker)
Screenshot from 2025-10-02 18-29-16.png  ← quickstart-029 (annotation, old version)
Screenshot from 2025-10-04 15-20-36.png  ← quickstart-005 (form name editing)
```

**Reason**: Replaced with corrected/updated versions on 2025-10-06

### Category 2: Exact Duplicates (10 files)

Same content as other screenshots, just different timestamps:

```
Screenshot from 2025-10-01 22-38-16.png  ← Duplicate of 22:34:38
Screenshot from 2025-10-02 15-53-41.png  ← Duplicate of 15:45:56
Screenshot from 2025-10-02 18-38-31.png  ← Duplicate of 18:33:31
Screenshot from 2025-10-04 14-35-41.png  ← Duplicate of 23:16:05
Screenshot from 2025-10-04 14-36-29.png  ← Duplicate (add field modal)
Screenshot from 2025-10-04 14-36-50.png  ← Duplicate of 14:36:29
Screenshot from 2025-10-04 14-38-42.png  ← Duplicate of Oct 1 version
Screenshot from 2025-10-04 14-44-10.png  ← Duplicate of 17:22:54
Screenshot from 2025-10-04 14-51-20.png  ← Duplicate of 14:51:04
Screenshot from 2025-10-04 14-53-55.png  ← Duplicate of 18:40:51
```

**Reason**: Identical content to other screenshots

### Category 3: Special Cases (3 files)

```
Screenshot from 2025-10-01 22-44-15.png  ← Detail view only (advanced helper text)
Screenshot from 2025-10-02 18-24-54.png  ← Annotation interface empty (superseded by 18:29:16)
Screenshot from 2025-10-04 14-52-25.png  ← OLD CONTROL CENTRE (superseded by Dashboard)
```

**Reason**: Partial views, superseded UI, or intermediate states

---

## 📁 Files Already Properly Organized

### Renamed and Ready (15 files):

```
✅ quickstart-007-editor-section-created-raw-2025-10-02.png
✅ quickstart-008-section-created-raw-2025-10-01.png
✅ quickstart-009-add-field-all-tab-raw-2025-10-01.png
✅ quickstart-010-site-name-expanded-raw-2025-10-01.png
✅ quickstart-013-site-type-expanded-raw-2025-10-02.png
✅ quickstart-018-site-photo-expanded-raw-2025-10-02.png
✅ quickstart-019-form-settings-raw-2025-10-02.png
✅ quickstart-021-form-settings-summary-fields-raw-2025-10-02.png
✅ quickstart-023-my-notebooks-not-active-raw-2025-10-02.png
✅ quickstart-024-my-notebooks-scrolled-raw-2025-10-02.png
✅ quickstart-025-activating-notebooks-modal-raw-2025-10-02.png
✅ quickstart-026-my-notebooks-active-raw-2025-10-02.png
✅ quickstart-027-record-list-empty-raw-2025-10-02.png
✅ quickstart-032-record-list-with-entry-raw-2025-10-02.png
✅ quickstart-033-notebook-settings-raw-2025-10-02.png
```

### Already Moved to Raw as Unused (5 files):

```
✅ quickstart-006-form-created-raw-unused.png
✅ quickstart-014-add-field-datetime-raw-unused.png
✅ quickstart-015-survey-date-expanded-raw-unused.png
✅ quickstart-016-add-field-text-raw-unused.png
✅ quickstart-017-observations-expanded-raw-unused.png
```

### Current 2025-10-06 Versions (11 files):

```
✅ quickstart-002-dashboard-overview-raw-2025-10-06.png
✅ quickstart-003-actions-tab-raw-2025-10-06.png
✅ quickstart-005-form-name-editing-raw-2025-10-06.png
✅ quickstart-011-add-field-choice-raw-2025-10-06-v2.png
✅ quickstart-012-edit-option-habitation-raw-2025-10-06.png
✅ quickstart-020-all-fields-visible-raw-2025-10-06.png
✅ quickstart-028-form-0-percent-raw-2025-10-06.png
✅ quickstart-029-annotation-interface-raw-2025-10-06.png
✅ quickstart-030-form-100-percent-raw-2025-10-06.png
✅ quickstart-031-datetime-picker-raw-2025-10-06.png
✅ (quickstart-004 raw file missing - was replaced directly)
```

---

## 🤔 Alternative Versions to Keep (Optional)

These Oct 4 screenshots show alternative views that might be useful:

```
Screenshot from 2025-10-04 14-40-53.png  ← quickstart-015 with helper text highlighted
Screenshot from 2025-10-04 14-42-53.png  ← quickstart-018 add field MEDIA tab
Screenshot from 2025-10-04 14-50-33.png  ← My Notebooks showing 90 not active
Screenshot from 2025-10-04 14-51-04.png  ← Login page mobile app view
```

**Decision**: Your choice whether to keep these as alternatives or delete them

---

## Summary

**Total files to delete**: ~22 files
- 9 superseded by 2025-10-06 versions
- 10 exact duplicates
- 3 special cases

**Total files properly organized**: 31 files
- 15 renamed to proper format
- 5 moved to raw as unused
- 11 current 2025-10-06 versions

**Remaining generic names**: 4 alternative versions (optional to keep)

---

## Quick Delete Commands (Review First!)

If you want to delete all recommended files in one go:

```bash
cd /home/shawn/Code/prompts/EFN/Docs-staging/production/screenshots/quickstart/raw

# Delete superseded files
rm "Screenshot from 2025-10-01 21-48-43.png"
rm "Screenshot from 2025-10-02 15-38-57.png"
rm "Screenshot from 2025-10-02 15-45-56.png"
rm "Screenshot from 2025-10-02 17-36-14.png"
rm "Screenshot from 2025-10-02 18-17-28.png"
rm "Screenshot from 2025-10-02 18-22-20.png"
rm "Screenshot from 2025-10-02 18-25-25.png"
rm "Screenshot from 2025-10-02 18-29-16.png"
rm "Screenshot from 2025-10-04 15-20-36.png"

# Delete duplicates
rm "Screenshot from 2025-10-01 22-38-16.png"
rm "Screenshot from 2025-10-02 15-53-41.png"
rm "Screenshot from 2025-10-02 18-38-31.png"
rm "Screenshot from 2025-10-04 14-35-41.png"
rm "Screenshot from 2025-10-04 14-36-29.png"
rm "Screenshot from 2025-10-04 14-36-50.png"
rm "Screenshot from 2025-10-04 14-38-42.png"
rm "Screenshot from 2025-10-04 14-44-10.png"
rm "Screenshot from 2025-10-04 14-51-20.png"
rm "Screenshot from 2025-10-04 14-53-55.png"

# Delete special cases
rm "Screenshot from 2025-10-01 22-44-15.png"
rm "Screenshot from 2025-10-02 18-24-54.png"
rm "Screenshot from 2025-10-04 14-52-25.png"
```

**⚠️ IMPORTANT**: Review the COMPLETE-SCREENSHOT-MAPPING.md file first before deleting!
