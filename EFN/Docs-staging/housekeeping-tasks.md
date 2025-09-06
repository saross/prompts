# Ongoing Housekeeping Tasks
**Created**: 2025-01-06  
**Purpose**: Track remaining documentation maintenance and enhancement tasks

## Quality Assurance Tasks

### Content Verification
- [ ] **Diff check archived vs consolidated docs**
  - Compare original archived files with consolidated versions
  - Ensure no critical content was lost during consolidation
  - Tools: `diff -u archive/[file] production/[consolidated]`
  - Priority: Low (spot checks indicate high quality)

### Navigation & Links
- [ ] **Verify all field-specific anchors work**
  - Test anchors: #text-fields, #number-fields, #datetime-fields, #select-fields, etc.
  - Check in: pattern guides, reference guides
  - Initial check: ✅ Working in pattern guides
  - Priority: Low (already partially verified)

- [ ] **Check for broken cross-references**
  - Verify links between field docs and pattern guides
  - Test bidirectional navigation
  - Check relative paths after production folder move
  - Priority: Medium

### Technical Validation
- [x] **Validate all JSON examples parse correctly** ✅ COMPLETED 2025-01-06
  - Removed 429 inline JSON comments from 4 OLD format docs
  - All component names validated against FAIMS3 codebase
  - All type-returned values confirmed valid
  - JSON now executable without cleanup
  - Files: All 8 field category docs in `/production/field-categories/`

## Content Enhancement Tasks

### JSON Examples (High Priority)
- [ ] **Add 15-20 production-ready JSON examples per field doc**
  - Media fields: FileUploader validation, TakePhoto workflows
  - Location fields: MapFormField configs, TakePoint accuracy
  - Relationship field: Complex vocabulary pairs, nested structures
  - Display field: Markdown structures, conditional display
  - Total needed: ~60-80 examples across all docs

### Security Documentation
- [ ] **Add Critical Security Risks sections**
  - Files needing updates:
    - text-fields-v05.md
    - number-fields-v05.md
    - datetime-fields-v05.md
    - select-choice-fields-v05.md
  - Format: `### ⚠️ SECURITY: [Specific Risk]`
  - Include: Affected fields, risk description, mitigation

### Platform-Specific Details
- [ ] **Expand platform behaviors**
  - iOS: HEIC conversion, permission handling
  - Android: Storage permissions, camera access
  - Web: File size limits, browser constraints
  - PWA: Offline capabilities, sync behavior
  - Priority: Medium

### Troubleshooting Expansion
- [ ] **Enhance troubleshooting sections**
  - Memory exhaustion scenarios
  - Permission recovery workflows
  - Sync failure patterns
  - Add 5-10 rows to Quick Diagnosis tables
  - Priority: Medium

## Minor Cleanup Tasks

### Standardization
- [ ] **Update date suffixes**
  - Change all (2025-08) to (2025-01)
  - Files: Early field docs (text, number, datetime, select)
  - Priority: Low

- [ ] **Security warning format standardization**
  - Ensure consistent format across all 8 field docs
  - Template: `### ⚠️ SECURITY: [Risk Name]`
  - Priority: Low

### Documentation Structure
- [ ] **Add migration path suggestions**
  - Between old/new field approaches
  - Field type conversion guidance
  - Data preservation strategies
  - Priority: Low

- [ ] **Extract repetitive patterns**
  - Identify patterns repeated across multiple field docs
  - Move to reference guides if universal
  - Priority: Low

## Optional Tasks

### Performance Metrics
- [ ] **Add quantified performance measurements**
  - GPS acquisition times by platform
  - Map tile cache sizes
  - Vertex count impacts
  - Battery drain metrics
  - Priority: Optional (nice to have)

### Accessibility Improvements
- [ ] **Document accessibility workarounds**
  - Screen reader alternatives for RichText
  - ARIA attribute injection attempts
  - RTL text handling
  - Priority: Optional

## Completed Major Milestones

### 2025-01-06 Session
- ✅ Phase 3B consolidation completed (4 reference guides)
- ✅ All production docs moved to `/production/` folder
- ✅ Archive organized with comprehensive manifest
- ✅ JSON cleanup: 429 inline comments removed from OLD format docs
- ✅ All JSON examples now executable
- ✅ Technical validation against FAIMS3 codebase complete

## Notes

- Most structural work is complete
- Focus on content enhancement over reorganization
- JSON examples are highest priority (direct user impact)
- Security sections are important for production use
- QA tasks are optional unless issues discovered

## Tracking

Use this document to track ongoing maintenance work. Check off items as completed and add new tasks as discovered.