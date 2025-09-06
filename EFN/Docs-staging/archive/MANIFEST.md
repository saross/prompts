# Archive Manifest - Fieldmark Documentation
**Last Updated**: 2025-01-06  
**Purpose**: Complete inventory of archived documentation with consolidation mapping

## Archive Overview

This archive contains 78 original documentation files that have been consolidated into the new documentation structure. All files retain their original content with added deprecation notices where applicable.

## Directory Structure

```
archive/
├── cross-field/              (10 files)  - Cross-field pattern documentation
├── detail-singlefield-docs/  (21 files)  - Individual field detailed documentation
├── planning/                 (4 files)   - Planning and architecture documents
├── reference/                (4 files)   - Component-level reference docs  
├── reference-docs/           (9 files)   - Platform & operational reference docs
├── reports/                  (27 files)  - Analysis and optimization reports
├── templates/                (1 file)    - Documentation templates
├── README.md                 (1 file)    - Archive overview
└── MANIFEST.md              (this file)  - Complete file inventory
```

## Complete File Inventory

### 1. Cross-Field Documentation (`/cross-field/`)
**Purpose**: Original cross-field pattern and workflow documentation  
**Status**: All consolidated into `/production/patterns/` directory

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
**Status**: Source material for field category documents in `/production/field-categories/`

#### Choice Fields (5 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| advanced-select.md | AdvancedSelect | select-choice-fields-v05.md |
| checkbox.md | Checkbox | select-choice-fields-v05.md |
| multiselect.md | MultiSelect | select-choice-fields-v05.md |
| radiogroup.md | RadioGroup | select-choice-fields-v05.md |
| select.md | Select | select-choice-fields-v05.md |

#### DateTime Fields (3 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| datetime.md | DateTimeNow | datetime-fields-v05.md |
| datetimepicker.md | DateTimePicker | datetime-fields-v05.md |
| datepicker.md | DatePicker | datetime-fields-v05.md |

#### Location Fields (2 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| mapformfield.md | MapFormField | location-fields-v05.md |
| takepoint.md | TakePoint | location-fields-v05.md |

#### Media Fields (2 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| fileuploader.md | FileUploader | media-fields-v05.md |
| takephoto.md | TakePhoto | media-fields-v05.md |

#### Number Fields (2 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| basicautoincrementer.md | BasicAutoIncrementer | number-fields-v05.md |
| numberinput.md | NumberInput | number-fields-v05.md |

#### Text Fields (5 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| address.md | Address | text-fields-v05.md |
| multilinetext.md | MultipleTextField | text-fields-v05.md |
| qrcode.md | QRCodeFormField | text-fields-v05.md |
| richtext.md | RichText | text-fields-v05.md |
| textfield.md | TextField | text-fields-v05.md |

#### Other Fields (2 files)
| File | Component | Category Doc |
|------|-----------|--------------|
| display.md | RichText (display) | display-field-v05.md |
| relatedrecordselector.md | RelatedRecordSelector | relationship-field-v05.md |

### 3. Planning Documents (`/planning/`)
**Purpose**: Architecture and planning documents for documentation improvements  
**Status**: Completed and archived

| File | Purpose | Status |
|------|---------|---------|
| field-docs-unification-todo.md | Unification checklist | ✅ Completed |
| phase-3-consolidation-checklist.md | Phase 3 tracking | ✅ Completed |
| TODO-v05-improvements.md | Version 5 improvements | ✅ Completed |
| unified-documentation-architecture-plan.md | Master architecture plan | ✅ Phases 1-4 Complete |

### 4. Reference Documentation (`/reference/`)
**Purpose**: Component-level reference documentation  
**Status**: Consolidated into `/production/references/component-reference.md`

| File | Purpose | Consolidated Into |
|------|---------|-------------------|
| component-namespace-reference.md | Component namespaces | component-reference.md |
| formik-integration-reference.md | Formik integration details | component-reference.md |
| meta-properties-reference.md | Meta property configuration | component-reference.md |
| type-system-reference.md | Type system documentation | component-reference.md |

### 5. Reference Docs (`/reference-docs/`)
**Purpose**: Platform and operational reference documentation  
**Status**: Consolidated into `/production/references/`

| File | Purpose | Consolidated Into |
|------|---------|-------------------|
| accessibility-reference.md | Accessibility guidelines | platform-reference.md |
| data-export-reference.md | Export format details | operations-reference.md |
| designer-limitations-reference.md | Designer constraints | constraints-reference.md |
| migration-strategies-reference.md | Migration guidance | operations-reference.md |
| performance-thresholds-reference.md | Performance limits | platform-reference.md |
| platform-behaviors-reference.md | Platform-specific behavior | platform-reference.md |
| security-considerations-reference.md | Security guidelines | constraints-reference.md |
| troubleshooting-framework-reference.md | Troubleshooting guide | operations-reference.md |
| validation-timing-reference.md | Validation behavior | constraints-reference.md |

### 6. Reports (`/reports/`)
**Purpose**: Analysis reports and optimization studies  
**Status**: Reference material, not consolidated

27 analysis and optimization reports including:
- alignment-plan-for-existing-docs.md
- centralization-summary-report.md
- content-analysis-report.md
- cross-references-added.md
- field-selection-optimization-guide.md
- llm-optimal-structure-v4.md
- media-reference-updates-checklist.md
- post-refactoring-qa-report.md
- prompt-gap-analysis.md
- prompt-restructuring-analysis.md
- shareable-content-candidates.md
- structure-comparison.md
- structure-verification.md
- template-application-report.md
- (and 13 more analysis files)

### 7. Templates (`/templates/`)
**Purpose**: Documentation templates  
**Status**: Reference template

| File | Purpose |
|------|---------|
| llm-optimized-field-doc-template.md | LLM-optimized documentation template |

## Consolidation Summary

### Original Structure (78 files)
- 10 cross-field pattern docs
- 21 single field detail docs
- 4 planning documents
- 4 component reference docs
- 9 platform/operational reference docs
- 27 analysis reports
- 1 template
- 2 readme/manifest files

### New Structure (17 production files)
- 8 field category docs
- 4 pattern guides
- 4 reference guides
- 1 master index

## Recovery Instructions

If production documentation is lost:
1. All source content exists in this archive
2. Consolidation mappings show which files combine
3. Deprecation notices can be removed
4. Original structure can be restored if needed

## Notes

- All archived files retain original content
- Deprecation notices added where applicable
- Reports directory contains valuable analysis for future reference
- Planning documents show complete project history