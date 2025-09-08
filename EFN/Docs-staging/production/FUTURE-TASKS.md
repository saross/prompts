# Future Tasks and Maintenance Plan

**Created**: 2025-09-07  
**Purpose**: Consolidated list of future enhancements and maintenance tasks  
**Status**: Post-LLM optimization project completion

## Context

Following the successful completion of the LLM optimization project (95/100 score achieved), this document consolidates all remaining and future tasks for the Fieldmark documentation system. These tasks focus on content enhancement, maintenance, and continuous improvement rather than structural changes.

## Priority Tasks

### 1. Production Testing & Validation
- [ ] **Test notebook generation with optimized reference.md**
  - Generate 5+ different notebook types
  - Validate parametric template system
  - Document any generation failures
  - Priority: **HIGH** - Critical for validation

- [ ] **Monitor LLM performance metrics**
  - Track generation accuracy
  - Measure response times
  - Collect error patterns
  - Priority: **HIGH** - Ongoing

### 2. Content Enhancement

#### Dashboard Documentation Tasks (Added 2025-09-08)
- [ ] **Document roles/permissions/privileges**
  - System-wide roles vs notebook-specific roles
  - Team roles and their capabilities
  - Permission inheritance and precedence
  - Create comprehensive matrix of all permissions
  - Priority: **HIGH** - Critical for user understanding

- [ ] **Document notebook metadata/'Info' page in Designer**
  - All fields available in the Info section
  - Version numbering approach (manual versioning)
  - Metadata that affects notebook behaviour
  - How metadata is used in deployment
  - Priority: **HIGH** - Core functionality

- [ ] **Document photo renaming fallback**
  - What happens when no HRID is present
  - Default naming convention for exported photos
  - How to configure photo export behaviour
  - Priority: **MEDIUM** - Important for data management

#### Designer/Editor Naming Update (Added 2025-09-08)
- [ ] **Review and update Designer references to Editor**
  - Verify current naming in UI (appears to be "Editor" now)
  - Search and replace "Designer" with "Editor" throughout docs
  - Update Designer Component Mapping title if needed
  - Maintain backward compatibility notes for existing users
  - Priority: **HIGH** - Accuracy and consistency

#### JSON Examples Expansion
- [ ] **Add 15-20 production-ready examples per field doc**
  - Media fields: FileUploader validation, TakePhoto workflows
  - Location fields: MapFormField configs, TakePoint accuracy
  - Relationship field: Complex vocabulary pairs, nested structures
  - Display field: Markdown structures, conditional display
  - Total needed: ~60-80 examples
  - Priority: **HIGH** - Direct user impact

#### Platform-Specific Documentation
- [ ] **Expand platform behaviors**
  - iOS: HEIC conversion, permission handling
  - Android: Storage permissions, camera access
  - Web: File size limits, browser constraints
  - PWA: Offline capabilities, sync behavior
  - Priority: **MEDIUM**

#### Troubleshooting Expansion
- [ ] **Enhance troubleshooting coverage**
  - Memory exhaustion scenarios
  - Permission recovery workflows
  - Sync failure patterns
  - Add 5-10 rows to Quick Diagnosis tables
  - Priority: **MEDIUM**

## Maintenance Tasks

### Regular Reviews
- [ ] **Monthly: Designer limitations review**
  - Check for new Designer features/fixes
  - Update constraints-reference.md
  - Verify component mappings still accurate

- [ ] **Quarterly: Migration strategies update**
  - Review migration patterns effectiveness
  - Add new migration scenarios
  - Update based on user feedback

- [ ] **As needed: Security advisories**
  - Monitor for new security issues
  - Update immediately when found
  - Priority: **HIGH** when applicable

### Documentation Quality
- [ ] **Cross-reference verification**
  - Verify all internal links work
  - Test bidirectional navigation
  - Check anchor consistency
  - Priority: **LOW** - Already mostly verified

- [ ] **Performance metrics updates**
  - Replace estimates with real measurements
  - GPS acquisition times by platform
  - Map tile cache sizes
  - Battery drain metrics
  - Priority: **LOW** - When data available

## Enhancement Opportunities

### Cookbook Expansion
- [ ] **Add more parametric recipes**
  - Based on common user patterns
  - Complex validation scenarios
  - Advanced conditional logic
  - Multi-step workflows

### Glossary Updates
- [ ] **Expand terminology as needed**
  - New features/components
  - User-suggested terms
  - Platform-specific terminology

### Template Library Growth
- [ ] **Create specialized notebook templates**
  - Industry-specific templates
  - Advanced feature demonstrations
  - Best practice showcases

## Optional Improvements

### Accessibility Documentation
- [ ] **Document accessibility workarounds**
  - Screen reader alternatives for RichText
  - ARIA attribute injection attempts
  - RTL text handling
  - Keyboard navigation patterns

### Performance Optimization
- [ ] **Create "lite" reference version**
  - Essential content only (<15K lines)
  - Faster LLM processing
  - Mobile-optimized size

### Migration Guides
- [ ] **Detailed migration paths**
  - Between old/new field approaches
  - Field type conversion guidance
  - Data preservation strategies

## Completed Milestones (Archived)

### LLM Optimization Project (2025-01-07)
- ✅ All 5 phases completed successfully
- ✅ Score: 95/100 achieved
- ✅ 1,509 template markers added
- ✅ Comprehensive glossary created
- ✅ Troubleshooting index with 95% coverage
- ✅ 5 working notebook templates
- ✅ 10 parametric cookbook recipes

### Documentation Architecture (2025-01-06)
- ✅ Phase 1: Navigation infrastructure
- ✅ Phase 2: Field document standardization
- ✅ Phase 3: Cross-field integration
- ✅ Phase 4: Reference consolidation
- ✅ JSON validation and cleanup
- ✅ Security standardization

## Success Metrics

Track these metrics to measure ongoing success:

1. **Notebook Generation Success Rate**
   - Target: >95%
   - Current: TBD (needs testing)

2. **Error Resolution Speed**
   - Target: <2 minutes average
   - Current: TBD (needs measurement)

3. **Documentation Currency**
   - Target: <30 days lag from feature release
   - Current: Up to date

4. **User Satisfaction**
   - Target: >4.5/5 rating
   - Current: TBD (needs feedback)

## Next Actions

### Immediate (This Week)
1. Test notebook generation with real use cases
2. Collect initial performance metrics
3. Document any discovered issues

### Short Term (This Month)
1. Add high-priority JSON examples
2. Expand troubleshooting based on test results
3. Update cookbook with discovered patterns

### Long Term (Quarterly)
1. Review and update all documentation
2. Expand templates based on usage
3. Optimize based on performance data

## Notes

- Structural work is complete - focus on content
- Prioritize based on user impact
- Maintain backward compatibility
- Keep reference.md under 35K lines
- Always test changes with actual generation

---

## Designer/Editor Visual Documentation Strategy (Added 2025-09-08)

### Context
Based on our experience documenting the Dashboard interfaces, we've identified the need for a systematic approach to adding visual documentation to the Designer/Editor interface. The availability of llama3.2-vision:11b-instruct locally provides opportunities for automated visual analysis.

### Proposed Approach

#### 1. Screenshot Capture Strategy
- **Systematic Coverage**: Capture each Designer panel state
  - Empty state (new template)
  - Partially filled (mid-creation)
  - Complete template
  - Error states
  - Each field type configuration panel
  
- **Naming Convention**:
  ```
  designer-{panel}-{state}-{field-type}.png
  Examples:
  - designer-left-panel-metadata-empty.png
  - designer-center-panel-textfield-config.png
  - designer-right-panel-validation-error.png
  ```

#### 2. Dual Documentation Approach

**For Each Screenshot**:
1. **Visual File**: Store in `/production/dashboard/images/designer/`
2. **Textual Description**: Embedded in markdown with structured format:

```markdown
### [Component Name] Configuration

![Designer TextField Configuration](./images/designer/designer-right-panel-textfield-config.png)

**Visual Elements**:
- Panel Location: Right
- Field Type: TextField
- Configuration Options Visible:
  - Field Name: {{FIELD_ID}}
  - Label: {{FIELD_LABEL}}
  - Helper Text: {{HELPER_TEXT}}
  - Required: Checkbox
  - Validation: Expandable section

**Key Interactions**:
- Drag handle for reordering (top left)
- Delete button (top right)
- Expand/collapse sections (chevron icons)

**Common Issues Shown**:
- Red outline indicates validation error
- Warning icon for missing required fields
```

#### 3. LLama3.2-Vision Integration Workflow

**Automated Description Generation**:
```bash
# Process each screenshot through llama3.2-vision
for image in designer-*.png; do
  llama3.2-vision analyze "$image" \
    --prompt "Describe UI elements, layout, interactive components, and any error states visible" \
    --output "${image%.png}-description.md"
done
```

**Human Review & Enhancement**:
1. Review auto-generated descriptions
2. Add context about functionality
3. Insert template markers where appropriate
4. Link to relevant JSON configuration

#### 4. Integration Points

**Where to Add Visual Documentation**:

1. **templates-interface.md**:
   - Designer overview screenshot
   - Panel layout diagram
   - Field palette visual reference

2. **New File: designer-visual-guide.md**:
   - Comprehensive visual reference
   - Step-by-step visual workflows
   - Before/after configuration examples

3. **Field Category Docs**:
   - Add "Designer Configuration" section to each
   - Show specific configuration panel for that field type
   - Visual validation examples

4. **dashboard-troubleshooting.md**:
   - Visual error states
   - Common UI problems with screenshots
   - Side-by-side correct/incorrect examples

#### 5. Structured Visual Annotation Format

For optimal LLM consumption, use consistent annotation:

```markdown
<!-- visual:metadata
image: designer-field-config.png
panel: right
component: TextField
state: configuration
annotations: [
  {element: "field-name-input", value: "{{FIELD_ID}}", required: true},
  {element: "label-input", value: "{{FIELD_LABEL}}", required: false},
  {element: "validation-section", expanded: false, contains: "validation-rules"}
]
-->
```

#### 6. Accessibility Considerations

For each visual element, provide:
- Alt text for screen readers
- Textual description of functionality
- Keyboard navigation notes
- Alternative text-only instructions

#### 7. Implementation Phases

**Phase 1: Core Designer Panels** (Priority: HIGH)
- [ ] Capture 3 main panels in various states
- [ ] Generate descriptions with llama3.2-vision
- [ ] Create designer-visual-guide.md
- [ ] Add to templates-interface.md

**Phase 2: Field Configuration Panels** (Priority: HIGH)
- [ ] Capture each field type configuration (8 categories)
- [ ] Add to respective field documentation
- [ ] Create visual index of all field configs

**Phase 3: Workflow Sequences** (Priority: MEDIUM)
- [ ] Step-by-step template creation
- [ ] Field validation setup
- [ ] Conditional logic configuration
- [ ] Error resolution sequences

**Phase 4: Troubleshooting Visuals** (Priority: MEDIUM)
- [ ] Common error states
- [ ] UI glitches and their fixes
- [ ] Browser-specific issues

#### 8. Technical Considerations

**Image Optimisation**:
- PNG format for UI screenshots
- Compress without quality loss
- Target <200KB per image
- Consider WebP for web deployment

**Version Control**:
- Store images in repository
- Document Designer version in metadata
- Update screenshots when UI changes

**Search & Discovery**:
- Create image manifest file
- Tag images with searchable metadata
- Build visual component index

#### 9. Success Metrics

- Coverage: 100% of Designer UI elements documented visually
- Descriptions: All images have LLM-consumable text descriptions
- Integration: Visual docs linked from relevant text docs
- Accessibility: Alternative text for all visual content
- Maintenance: Process for updating when UI changes

#### 10. Tools & Resources Needed

- **Screenshot tool**: For consistent captures
- **llama3.2-vision:11b-instruct**: For description generation
- **Image editor**: For annotations if needed
- **Markdown preview**: To verify rendering
- **Storage**: ~50-100MB for comprehensive coverage

### Benefits of This Approach

1. **Dual Consumption**: Humans see visuals, LLMs read descriptions
2. **Searchability**: Text descriptions make visuals discoverable
3. **Maintainability**: Structured format enables updates
4. **Automation**: llama3.2-vision reduces manual work
5. **Completeness**: Systematic coverage ensures nothing missed

### Next Steps

1. Create `/production/dashboard/images/designer/` directory
2. Capture initial Designer overview screenshots
3. Test llama3.2-vision workflow with sample images
4. Create designer-visual-guide.md template
5. Begin Phase 1 implementation

---

*This document consolidates tasks from the completed llm-optimization-implementation-plan.md and housekeeping-tasks.md, both now archived.*