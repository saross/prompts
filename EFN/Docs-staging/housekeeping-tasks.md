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
- [x] **Standardized security sections across all 8 field docs** ✅ COMPLETED 2025-01-06
  - Moved detailed security content to constraints-reference.md
  - All field docs now have consistent brief security notes (5 bullets)
  - Proper reference links to centralized security documentation
  - No duplication of general security content

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

## Maintenance Plan (from architecture plan)

### Regular Updates
- [ ] **Monthly review of Designer limitations**
  - Check for new Designer features/fixes
  - Update constraints-reference.md accordingly
  - Priority: Low (schedule-based)

- [ ] **Quarterly update of migration strategies**
  - Review migration patterns for effectiveness
  - Add new migration scenarios as discovered
  - Priority: Low (schedule-based)

- [ ] **Security advisories as needed**
  - Monitor for new security issues
  - Update security sections immediately when found
  - Priority: High (when applicable)

- [ ] **Performance threshold adjustments**
  - Update based on real-world metrics
  - Note: All current thresholds are estimated/extrapolated
  - Priority: Medium (when data available)

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

### Unified Documentation Architecture Plan (Phases 1-4)
- ✅ Phase 1: Navigation Infrastructure (master index, headers/footers)
- ✅ Phase 2: Field Document Standardization (component mapping, cross-references)
- ✅ Phase 3: Cross-Field Document Integration (4 pattern guides created)
- ✅ Phase 4: Reference Document Consolidation (4 reference guides created)
- Note: All structural phases complete - remaining work is content enhancement

### 2025-01-06 Session (Morning)
- ✅ Phase 3B consolidation completed (4 reference guides)
- ✅ All production docs moved to `/production/` folder
- ✅ Archive organized with comprehensive manifest (78 files documented)
- ✅ JSON cleanup: 429 inline comments removed from OLD format docs
- ✅ All JSON examples now executable
- ✅ Technical validation against FAIMS3 codebase complete

### 2025-01-06 Session (Afternoon)
- ✅ Security sections standardized across all 8 field docs
- ✅ Security concerns contextualized (privacy vs security, features vs bugs)
- ✅ Constraints-reference.md updated with nuanced explanations
- ✅ Archive MANIFEST and README updated (78 files catalogued)
- ✅ Production MANIFEST and README created
- ✅ Reference.md regenerated (24,407 lines, 868KB)

## Notes

- Most structural work is complete
- Focus on content enhancement over reorganization
- JSON examples are highest priority (direct user impact)
- Security sections are important for production use
- QA tasks are optional unless issues discovered

## Tracking

Use this document to track ongoing maintenance work. Check off items as completed and add new tasks as discovered.