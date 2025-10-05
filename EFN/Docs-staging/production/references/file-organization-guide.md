# File Organisation Guide - Fieldmark Documentation

<!-- discovery:metadata

<!-- structured:metadata
meta:purpose: technical-reference
meta:summary: Project structure and file naming conventions for Fieldmark documentation.
meta:generates: lookup-tables
meta:requires: [fieldmark-knowledge]
meta:version: 3.0.0
meta:document: file_organization_guide
meta:depth-tags: [essential]
-->

provides: [project-structure, file-layout, documentation-organisation]
see-also: [manifest]
-->


## Date: 2025-01-07

## Production Files (Keep & Maintain)

These files are part of the official documentation and should be maintained:

### Core Documentation Structure
```
production/
├── field-categories/        # Field type documentation (8 files)
│   ├── datetime-fields-v05.md
│   ├── display-field-v05.md
│   ├── location-fields-v05.md
│   ├── media-fields-v05.md
│   ├── number-fields-v05.md
│   ├── relationship-field-v05.md
│   ├── select-choice-fields-v05.md
│   └── text-fields-v05.md
│
├── patterns/               # Cross-field pattern documentation (4 files)
│   ├── conditional-visibility-patterns.md
│   ├── field-selection-guide.md
│   ├── identifier-patterns.md
│   └── validation-patterns.md
│
├── references/             # Technical references (5 files)
│   ├── component-reference.md
│   ├── constraints-reference.md
│   ├── designer-component-mapping.md  # NEW - Critical mapping reference
│   ├── operations-reference.md
│   └── platform-reference.md
│
├── scripts/                # Build & maintenance scripts
│   ├── build-reference.sh            # Main build script
│   └── validate-notebook.py          # NEW - Notebook validation
│
├── field-type-index.md     # Navigation index
├── reference.md            # Concatenated full documentation
├── README.md              # Project overview
├── manifest.md            # File inventory
└── test-notebook-fixed.json  # Working test notebook
```

## Temporary/Analysis Files (Can Archive)

These files were created during analysis and can be moved to archive:

### validation-reports/ Directory
All files in this directory are analysis outputs and can be archived:
```
validation-reports/
├── DESIGNER_TO_COMPONENT_MAPPING.md  # Draft version (now in references/)
├── FIELD_AUDIT_REPORT.md             # Analysis report
├── fix_json_components.py            # One-time fix script
├── fix_json.py                       # One-time fix script
├── JSON_FIXES_SUMMARY.md             # Fix documentation
├── JSON_VALIDATION_SUMMARY.md        # Validation results
├── MAPPING_CONSISTENCY_REPORT.md     # Consistency check
├── TEST_NOTEBOOK_FIXES.md            # Fix documentation
├── validate_json_enhanced.py         # Analysis script
├── validate_json.py                  # Analysis script
├── validation_report_enhanced.md     # Analysis output
└── validation_report.md              # Analysis output
```

### Root Level Temporary Files
```
├── test-notebook.json         # Original broken notebook (archive)
├── fix-mapping-tables.sh      # One-time fix script (can archive)
└── PRODUCTION_UPDATE_SUMMARY.md  # Summary document (keep for reference)
```

## Recommended Actions

### 1. Archive Analysis Files
```bash
# Create archive directory
mkdir -p archive/2025-01-07-analysis

# Move validation reports
mv validation-reports/* archive/2025-01-07-analysis/

# Move original test notebook
mv test-notebook.json archive/2025-01-07-analysis/

# Remove empty validation-reports directory
rmdir validation-reports
```

### 2. Keep Production Files
All files in the main production structure should be maintained as they are the official documentation.

### 3. Update Scripts Directory
Consider organizing scripts by purpose:
```
scripts/
├── build/
│   └── build-reference.sh
├── validation/
│   └── validate-notebook.py
└── maintenance/
    └── (future maintenance scripts)
```

## File Categories Summary

### Essential Production Files (21 files)
- 8 field category documents
- 4 pattern documents
- 5 reference documents
- 1 build script
- 1 validation script
- 1 test notebook
- 1 index file

### Supporting Files (3 files)
- README.md
- manifest.md
- reference.md (generated)

### Temporary Analysis Files (12 files)
- All files in validation-reports/
- Can be archived for historical reference

## Version Control Recommendations

### Files to Track in Git
- All files in production structure
- README.md, manifest.md
- This FILE_ORGANIZATION_GUIDE.md

### Files to Exclude (.gitignore)
```
# Temporary analysis
validation-reports/
archive/2025-*/

# Generated files (if regenerated frequently)
reference.md

# Backup files
*.bak
*.tmp
```

## Next Steps

1. **Archive temporary files** - Move analysis files to archive/
2. **Update manifest.md** - Reflect new organisation
3. **Clean scripts directory** - Organize by purpose
4. **Update .gitignore** - Exclude temporary files
5. **Commit production files** - Version control essential docs

---

*Organisation Guide Created: 2025-01-07*
*Purpose: Clarify production vs temporary file structure*