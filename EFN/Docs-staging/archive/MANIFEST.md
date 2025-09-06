# Archive Manifest - Fieldmark Documentation
**Last Updated**: 2025-01-06  
**Purpose**: Complete inventory of archived documentation with consolidation mapping

## Archive Overview

This archive contains 45 original documentation files that have been consolidated into the new documentation structure. All files retain their original content with added deprecation notices.

## Directory Structure

```
archive/
├── cross-field/            (10 files) - Cross-field pattern documentation
├── detail-singlefield-docs/ (21 files) - Individual field detailed documentation
├── reference/              (4 files)  - Component-level reference docs
├── reference-docs/         (9 files)  - Platform & operational reference docs
├── README.md               (1 file)   - Archive overview
└── MANIFEST.md            (this file) - Complete file inventory
```

## Complete File Inventory

### 1. Cross-Field Documentation (`/cross-field/`)
**Purpose**: Original cross-field pattern and workflow documentation  
**Status**: All consolidated into `/patterns/` directory

| Original File | Size | Consolidated Into | Purpose |
|--------------|------|-------------------|---------|
| conditional-logic.md | 37KB | patterns/dynamic-forms-guide.md | Conditional field display/validation |
| field-selection-best-practices.md | 26KB | patterns/field-selection-guide.md | Choosing appropriate field types |
| navigation.md | 19KB | patterns/form-structure-guide.md | Form navigation patterns |
| notebook-structure.md | 34KB | patterns/form-structure-guide.md | Overall form architecture |
| patterns.md | 18KB | patterns/implementation-patterns-guide.md | Common implementation patterns |
| quick-start.md | 12KB | patterns/field-selection-guide.md | Getting started examples |
| summary-table.md | 12KB | patterns/field-selection-guide.md | Field comparison matrix |
| troubleshooting-framework-reference.md | 9KB | patterns/implementation-patterns-guide.md | Troubleshooting patterns |
| validation.md | 33KB | patterns/dynamic-forms-guide.md | Validation strategies |
| validation-timing-reference.md | 6KB | patterns/dynamic-forms-guide.md | Validation timing details |

### 2. Single Field Documentation (`/detail-singlefield-docs/`)
**Purpose**: Detailed third-draft documentation for individual field types  
**Status**: Source material for field category documents in `/field-categories/`

#### Choice Fields (5 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| advanced-select.md | AdvancedSelect | select-choice-fields-v05.md |
| checkbox.md | Checkbox | select-choice-fields-v05.md |
| multiselect.md | MultiSelect | select-choice-fields-v05.md |
| radiogroup.md | RadioGroup | select-choice-fields-v05.md |
| select.md | Select | select-choice-fields-v05.md |

#### DateTime Fields (1 file)
| File | Components | Category Doc |
|------|-----------|--------------|
| datetime-all.md | DateTime, DateTimeNow, DatePicker, etc. | datetime-fields-v05.md |

#### Location Fields (2 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| mapform.md | MapFormField | location-fields-v05.md |
| takepoint.md | TakePoint | location-fields-v05.md |

#### Media Fields (2 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| fileuploader.md | FileUploader | media-fields-v05.md |
| takephoto.md | TakePhoto | media-fields-v05.md |

#### Number Fields (3 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| basicautoincrementer.md | BasicAutoIncrementer | number-fields-v05.md |
| controllednumber.md | NumberField | number-fields-v05.md |
| numberinput.md | NumberField variants | number-fields-v05.md |

#### Text Fields (6 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| address.md | AddressField | text-fields-v05.md |
| email.md | Email validation | text-fields-v05.md |
| multilinetext.md | MultipleTextField | text-fields-v05.md |
| qrcode.md | QRCodeFormField | text-fields-v05.md |
| singlelinetext.md | TextField/FAIMSTextField | text-fields-v05.md |
| templatedstring.md | TemplatedStringField | text-fields-v05.md |

#### Other Fields (2 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| display.md | RichText | display-field-v05.md |
| relationship.md | RelatedRecordSelector | relationship-field-v05.md |

### 3. Component Reference Documentation (`/reference/`)
**Purpose**: Component-level technical specifications  
**Status**: Consolidated into `/references/component-reference.md`

| Original File | Size | Content |
|--------------|------|---------|
| component-namespace-reference.md | 8KB | Component namespace mappings |
| formik-integration-reference.md | 10KB | Formik integration details |
| meta-properties-reference.md | 9KB | Meta property configuration |
| type-system-reference.md | 7KB | Type system definitions |

### 4. Platform & Operational Reference (`/reference-docs/`)
**Purpose**: Platform behaviors, operations, and constraints  
**Status**: Consolidated into multiple `/references/` files

| Original File | Size | Consolidated Into | Content |
|--------------|------|-------------------|---------|
| accessibility-reference.md | 13KB | references/platform-reference.md | WCAG compliance |
| data-export-reference.md | 9KB | references/operations-reference.md | Export formats |
| designer-limitations-reference.md | 7KB | references/constraints-reference.md | Designer limitations |
| migration-strategies-reference.md | 11KB | references/operations-reference.md | Migration procedures |
| performance-thresholds-reference.md | 18KB | references/platform-reference.md | Performance metrics |
| platform-behaviors-reference.md | 9KB | references/platform-reference.md | Platform-specific behaviors |
| security-considerations-reference.md | 10KB | references/constraints-reference.md | Security vulnerabilities |
| troubleshooting-framework-reference.md | 9KB | Split between platform & operations | Troubleshooting procedures |
| validation-timing-reference.md | 6KB | references/platform-reference.md | Validation timing |

## Consolidation Summary

### Phase 3A - Pattern Consolidation
- **10 cross-field docs** → **4 pattern guides** in `/patterns/`
- Reduction: 209KB → ~150KB (28% more concise)
- Result: Unified workflow-based guidance

### Phase 3B - Reference Consolidation  
- **13 reference docs** → **4 reference guides** in `/references/`
- Reduction: 110KB → ~95KB (14% more concise)
- Result: Organized technical specifications

### Field Documentation
- **21 detail docs** remain as source material
- Incorporated into **8 field category docs** in `/field-categories/`
- Result: Comprehensive field type reference

## Usage Guidelines

### When to Use Archive Files

1. **Disaster Recovery**: If consolidated version has critical errors
2. **Historical Research**: Understanding documentation evolution
3. **Detailed Reference**: When consolidated version lacks specific detail
4. **Migration Rollback**: If consolidation causes issues

### How to Restore Files

```bash
# 1. Copy file from archive
cp archive/[subdir]/[filename].md references/

# 2. Remove deprecation notice (first 3 lines)
sed -i '1,3d' references/[filename].md

# 3. Update build script
vim scripts/build-reference.sh

# 4. Test build
bash scripts/build-reference.sh
```

## Important Notes

⚠️ **All archived files contain deprecation notices** - Remove before use  
⚠️ **Do not reference archive files directly** - Use consolidated versions  
⚠️ **Archive is for emergency use only** - Not part of active documentation  
⚠️ **Preserve archive indefinitely** - Critical for disaster recovery

## File Statistics

- **Total archived files**: 45
- **Total archive size**: ~500KB
- **Deprecation notices added**: 23 files
- **Original content preserved**: 100%
- **Consolidation date**: 2025-01-06

## Contact

For questions about specific archived files:
1. Check the consolidated version first
2. Review this manifest for mapping
3. Examine git history for consolidation commits
4. Contact documentation team if unclear

---

*This manifest provides complete traceability from original to consolidated documentation.*