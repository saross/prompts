# Documentation Integration Checklist
**Created**: 2025-01-09  
**Purpose**: Ensure complete integration of new Editor and permissions documentation

## Immediate Integration Tasks

### 1. Cross-Reference Audit

#### Form Settings Cross-References Needed
- [x] Link to validation documentation (where validation rules are configured)
- [x] Link to dynamic forms guide (publishButtonBehaviour affects conditional logic)
- [x] Link to notebook templates showing real examples
- [x] Add bidirectional links from validation docs back to Form Settings
- [x] Ensure navigation docs reference layout settings

#### Notebook Info Cross-References Needed
- [x] Link from notebook-format-guide.md to Info page documentation
- [x] Link from operations-reference.md (import/export) to metadata section
- [ ] Add metadata examples to notebook-templates.md
- [x] Link from troubleshooting-index.md to Info troubleshooting

#### Roles Documentation Cross-References
- [x] Ensure dashboard docs link to roles reference
- [x] Add role requirements to dashboard-patterns recipes
- [x] Link from notebook creation docs to required roles
- [x] Add permission requirements to operations docs

### 2. JSON Example Integration

#### Form Settings JSON Examples
- [x] Add complete viewset examples with all settings to editor-form-settings.md
- [x] Include Form Settings configurations in cookbook patterns
- [x] Show publishButtonBehaviour variations in validation examples

#### Notebook Info JSON Examples
- [x] Add metadata examples to editor-notebook-info.md
- [x] Show custom metadata fields for different domains
- [x] Include RAiD integration example in complete notebook

### 3. Shared Documentation Extraction

#### Troubleshooting Consolidation
- [x] Extract Form Settings troubleshooting to troubleshooting-index.md
- [x] Extract Info page troubleshooting to troubleshooting-index.md
- [x] Extract roles troubleshooting to troubleshooting-index.md
- [x] Ensure all have bidirectional links

#### Common Patterns
- [ ] Extract metadata patterns to implementation-patterns-guide.md
- [ ] Add Form Settings patterns to cookbook
- [ ] Document role assignment workflows in dashboard-patterns.md

### 4. Manifest and Index Updates

#### LLM Navigation Manifest
- [x] Add Form Settings to manifest with proper tags
- [x] Add Notebook Info to manifest with metadata tags
- [x] Update roles section in manifest
- [x] Verify all provides/requires relationships

#### Navigation Index
- [ ] Add all new documents to navigation-index.md
- [ ] Update incoming links registry
- [ ] Update outgoing links registry
- [ ] Verify bidirectional completeness

### 5. Dashboard Documentation Verification

#### Check Against Codebase
- [ ] Verify all Dashboard UI elements documented
- [ ] Check for undocumented settings or features
- [ ] Validate role names against actual implementation
- [ ] Confirm permission inheritance model

#### Missing Features Check
- [ ] Review Dashboard codebase for undocumented tabs
- [ ] Check for admin-only features not documented
- [ ] Verify team management features complete
- [ ] Check notebook lifecycle features

### 6. README and Overview Updates

#### Main README
- [ ] Update documentation structure section
- [ ] Add new documents to document list
- [ ] Update statistics (line counts, document counts)

#### Reference README
- [ ] Add Form Settings and Info to Editor section
- [ ] Update roles documentation section
- [ ] Add metadata standards information

### 7. Integration Testing

#### Build Verification
- [ ] Confirm reference.md builds without errors
- [ ] Check all concat boundaries properly formatted
- [ ] Verify navigation works in concatenated mode
- [ ] Test depth tag filtering

#### Link Validation
- [ ] Check all internal links resolve
- [ ] Verify cross-references work
- [ ] Test navigation paths
- [ ] Validate glossary links

### 8. Content Alignment

#### Terminology Consistency
- [ ] Ensure "Editor" vs "Designer" used consistently
- [ ] Verify "notebook" vs "project" alignment
- [ ] Check "form" vs "viewset" usage
- [ ] Align permission terminology

#### Example Consistency
- [ ] Use same example notebooks across docs
- [ ] Ensure field IDs match in examples
- [ ] Verify JSON structures align
- [ ] Check template marker usage

## Completed in Previous Session

### ✅ Created Documents
- editor-form-settings.md (555 lines, 97/100 score)
- editor-notebook-info.md (511 lines, 93/100 score)  
- roles-permissions-reference.md (561 lines, 94/100 score)
- quickstart-notebook-creators.md (2,656 words)
- Screenshot integration workflow documents

### ✅ Updates Applied
- Glossary: 18 new terms added
- Build script: All documents integrated
- FUTURE-TASKS: Marked completed items, added FAIR guide

### ✅ Archive Reorganization
- Moved example notebooks to archive/
- Consolidated scripts, reports, reference docs
- Cleaner production/ structure

## Completed in Current Session (2025-01-09)

### ✅ Cross-Reference Integration
- Added bidirectional links between Form Settings and Dynamic Forms Guide
- Connected Form Settings `publishButtonBehaviour` to validation documentation
- Linked Notebook Info to operations and metadata standards
- Added role requirements to Editor and Info documentation
- Created semantic linkages using {{cross-ref:}} template markers

### ✅ JSON Examples Added
- **Form Settings**: 4 complete examples (archaeology, environmental, training, integration)
- **Notebook Info**: 3 complete examples (archaeological research, environmental monitoring, cultural heritage)
- Examples demonstrate standards compliance (ADS, Darwin Core, tDAR, RAiD)
- Showcased different access models and metadata tiers

### ✅ Documentation Enhancements (Part 1)
- Enhanced Form Settings with validation timing cross-references
- Added permissions cross-references to roles documentation  
- Connected dynamic forms guide back to Form Settings
- Total new cross-references added: 12

### ✅ Documentation Enhancements (Part 2)
- **Troubleshooting Index**: Consolidated 3 new sections (Form Settings, Notebook Info, Permissions)
- Added 8 new error entries to quick lookup table
- Created detailed solutions for 10+ common issues
- Added cross-references back to source documents

### ✅ LLM Navigation Manifest Updates
- Added 3 new documents to quick navigation table
- Updated technical references with priority levels
- Enhanced content coverage matrix with 4 new topics
- Added 6 new task mappings for common operations
- Updated document dependencies tree
- Added 11 new navigation keywords

### ✅ Operations Documentation Updates (Part 3)
- **Export/Import Metadata**: Added comprehensive metadata preservation table
- Documented FAIR compliance requirements for export
- Added permission requirements for all export operations
- Created metadata requirements for import operations

### ✅ Permission Integration Across Documents
- **Dashboard Patterns**: Added role requirements to 5 recipe phases
- **Notebooks Interface**: Added permission requirements for creation and management
- **Operations Reference**: Linked export permissions to roles documentation
- Updated permission troubleshooting with proper role names
- Total permission cross-references added: 15+

## Key Insights for Integration

1. **Form Settings** controls validation and UI behavior - must link to validation docs
2. **Notebook Info** enables standards compliance - must link to FAIR/repository docs
3. **Roles** determine access - must be referenced from all operation docs
4. **Metadata** has three tiers - ensure all tiers documented and linked

## Priority Order

1. **HIGH**: Cross-reference audit (prevents confusion)
2. **HIGH**: JSON example integration (practical usage)
3. **MEDIUM**: Troubleshooting consolidation (better UX)
4. **MEDIUM**: Manifest/index updates (navigation)
5. **LOW**: README updates (housekeeping)

---

*Use this checklist to ensure complete integration of new documentation into the existing knowledge base.*