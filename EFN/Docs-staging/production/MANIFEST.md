# Production Manifest - Fieldmark Documentation
**Last Updated**: 2025-01-07 (Final Cleanup)  
**Purpose**: Complete inventory of production documentation

## Production Overview

This production folder contains the authoritative Fieldmark v3 field documentation, consolidated from 78 source files into comprehensive documents optimized for LLM consumption.

## Directory Structure

```
production/
├── field-categories/       (8 files)   - Field type documentation by category
├── patterns/              (4 files)   - Cross-field patterns and workflows
├── references/            (9 files)   - Technical references, guides, mappings, and index
├── scripts/               (2 files)   - Build and validation scripts
├── reference.md           (1 file)   - LLM-optimized concatenated reference
├── test-notebook-correct.json (1 file) - Minimal working test notebook
├── test-notebook-comprehensive.json (1 file) - Comprehensive component test
├── PRODUCTION_UPDATE_SUMMARY.md (1 file) - Summary of recent updates
├── MANIFEST.md            (this file) - Production inventory
└── README.md              (1 file)   - Production overview
```

**Archives Created**:
- `archive/2025-01-07-analysis/` - Validation reports and analysis files
- `archive/2025-01-07-notebooks/` - Old test notebooks with incorrect structure
- `archive/2025-01-07-scripts/` - One-time fix scripts

## Complete File Inventory

### 1. Field Category Documentation (`/field-categories/`)
**Purpose**: Comprehensive documentation for each field type category  
**Format**: LLM-optimized with depth tags {essential}, {important}, {comprehensive}

#### Field Documentation Purpose Table

| File | LLM Purpose | Fields Covered | Lines |
|------|------------|----------------|-------|
| **text-fields-v05.md** | Text input validation, XSS prevention, template syntax | 7 text components | 1,693 |
| **select-choice-fields-v05.md** | Option configuration, CSV injection prevention | 5 selection components | 1,332 |
| **datetime-fields-v05.md** | Date handling, timezone issues, audit trails | 4 date/time components | 1,284 |
| **number-fields-v05.md** | Numeric validation, precision limits, auto-increment | 3 number components | 1,298 |
| **display-field-v05.md** | Markdown rendering, memory management | 1 display component | 571 |
| **location-fields-v05.md** | GPS accuracy, privacy concerns, map configuration | 2 location components | 825 |
| **media-fields-v05.md** | File validation, EXIF stripping, size limits | 2 media components | 789 |
| **relationship-field-v05.md** | Record linking, access control, orphan handling | 1 relationship component | 584 |

### 2. Pattern Guides (`/patterns/`)
**Purpose**: Cross-field patterns showing how fields work together  
**Status**: Consolidated from 10 source documents

#### Pattern Guide Purpose Table

| File | LLM Purpose | Lines |
|------|------------|-------|
| **field-selection-guide.md** | Decision trees for choosing appropriate field types | 511 |
| **form-structure-guide.md** | Multi-section forms, navigation patterns, viewsets | 401 |
| **dynamic-forms-guide.md** | Conditional visibility, validation rules, computed values | 462 |
| **implementation-patterns-guide.md** | Common implementation patterns, error handling | 419 |

### 3. Technical References (`/references/`)
**Purpose**: Consolidated technical documentation  
**Status**: 8 reference documents serving distinct LLM purposes

#### LLM Purpose Reference Table

| Reference File | LLM Purpose | Lines |
|---------------|-------------|-------|
| **designer-component-mapping.md** | 🔑 PRIMARY REFERENCE - All field mappings, components, configurations | 295 |
| **component-reference.md** | Deep technical dive into namespaces, types, Formik integration | 977 |
| **constraints-reference.md** | Security vulnerabilities, Designer limitations | 497 |
| **operations-reference.md** | Migration procedures, troubleshooting workflows | 787 |
| **platform-reference.md** | Platform-specific behaviors and workarounds | 656 |
| **notebook-format-guide.md** | JSON structure for notebook creation/debugging | 198 |
| **file-organization-guide.md** | Project structure (meta-documentation) | 135 |
| **field-type-index.md** | Navigation and documentation structure only | 81 |

### 4. Scripts (`/scripts/`)

| File | Purpose | Type |
|------|---------|------|
| build-reference.sh | Build concatenated reference.md | Build |
| validate-notebook.py | Validate notebook JSON structure | Validation |
| fix-mapping-tables.sh | Fix component mapping tables (archived) | One-time |

### 5. Navigation & Test Files (`/`)

| File | Purpose | Lines |
|------|---------|-------|
| field-type-index.md | Master navigation with depth tags | 299 |
| reference.md | Concatenated LLM reference | ~26,000 |
| test-notebook-fixed.json | Working test notebook | 875 |
| FILE_ORGANIZATION_GUIDE.md | Organization documentation | 135 |
| PRODUCTION_UPDATE_SUMMARY.md | Update history | 112 |

## Key Features

### LLM Optimization
- Three-tier depth tagging system
- Concatenated reference for single-context loading
- Consistent structure across all documents
- Clean, executable JSON examples

### Navigation
- Master index with categorized links
- Cross-references between related topics
- Breadcrumb headers and footers
- Component name mapping tables

### Security & Constraints
- Standardized security sections
- Contextualized risk assessments
- Designer limitations documented
- Platform-specific behaviors

## Statistics

### Document Metrics
- **Total Files**: 21 (including scripts and meta files)
- **Documentation Files**: 18
- **Total Lines**: ~33,000 (including reference.md)
- **Compressed from**: 78 original files
- **Reduction**: 78% fewer files

### Content Coverage
- **Field Types**: 23 components documented
- **Patterns**: 10 cross-field workflows
- **Security Issues**: 30+ risks documented
- **Platform Behaviors**: 4 platforms covered
- **JSON Examples**: 100+ (currently minimal, expansion planned)

## Maintenance

### Regular Updates Needed
- Monthly review of Designer limitations
- Quarterly migration strategy updates
- Security advisories as discovered
- Performance threshold adjustments

### Remaining Enhancements
- ~~Add 60-80 production JSON examples~~ ✅ Added 20 per file
- Expand platform-specific behaviors
- Enhanced troubleshooting sections
- Additional migration scenarios

### Recent Fixes (2025-01-06)
- Fixed all incorrect component names in JSON examples
- Corrected TemplatedIntegerField/FloatField → NumberField
- Fixed ControlledNumber → TextField with type="number"
- Added Designer UI to Component mapping reference

## Build Process

To regenerate reference.md:
```bash
cd /production
./scripts/build-reference.sh
```

Output:
- File: reference.md
- Size: ~868KB
- Lines: ~24,400

## Quality Standards

All production documentation follows:
- LLM-optimized template structure
- Consistent security note format
- Standardized component naming
- Validated technical accuracy
- Clean executable JSON

## Version History

- **v05**: Current production version
- **Phase 1-2**: Navigation and standardization (completed)
- **Phase 3-4**: Consolidation (completed)
- **2025-01-06**: Security sections standardized
- **2025-01-06**: JSON cleaned for LLM consumption
- **2025-01-06**: Fixed component names in JSON examples
- **2025-01-06**: Added Designer → Component mapping reference
- **2025-01-07 Morning**: Fixed mapping table contradictions in field docs
- **2025-01-07 Morning**: Corrected namespaces (select/location fields)
- **2025-01-07 Morning**: Resolved RelatedRecordSelector naming confusion
- **2025-01-07 Morning**: Archived analysis files to archive/2025-01-07-analysis/
- **2025-01-07 Afternoon**: Fixed notebook structure issues (added fviews)
- **2025-01-07 Afternoon**: Created working test notebooks
- **2025-01-07 Afternoon**: Added notebook-format-guide.md
- **2025-01-07 Final**: Moved field-type-summary-table.md from FAIMS3
- **2025-01-07 Final**: Archived old notebooks and scripts
- **2025-01-07 Final**: Updated build script with all new documentation
- **2025-01-07 Final**: Final cleanup and organization