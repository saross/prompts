# IMPORTANT - System-Wide Patterns for Documentation Consolidation

**Purpose**: Track system-level patterns, design philosophy, and common limitations discovered during field documentation that require centralized documentation in Phase 2.

**Last Updated**: January 2025  
**Phase**: Discovered during Phase 1 (Field Documentation), to be addressed in Phase 2 (Structural Documentation)

### 2.7 Static Configuration Limitation

**Pattern**: Most fields limited to static configuration with no dynamic data loading.

**Affected Fields**:
- Select/RadioGroup: Static options only
- AdvancedSelect: Static hierarchy only
- MultiSelect: Static options only
- Vocabularies: No external API loading
- Validation: No async validation

**Missing Capabilities**:
- No REST API integration for options
- No conditional vocabulary loading
- No user-role-based options
- No location-based filtering
- No progressive loading

**Documentation Needed**:
- Static configuration requirements
- Workarounds for dynamic needs
- Update strategies for vocabularies
- Implications for long projects

---

## 1. Core System Architecture Patterns

### 1.1 Distributed, Offline-First Architecture

**Pattern**: All field types operate within a distributed, offline-capable system with eventual consistency.

**Implications Across Fields**:
- Relationships: Reciprocal updates delayed until sync
- Auto-incrementers: Sequence conflicts when multiple offline users
- Validation: Client-side only, no server verification
- Media fields: Local storage until sync opportunity
- All fields: Last-write-wins conflict resolution

**Documentation Needed**:
- "Working with Distributed Data Collection" guide
- Sync behaviour expectations
- Conflict resolution strategies
- Multi-user coordination patterns
- Why last-write-wins is intentional, not a bug

### 1.2 Schema Evolution Flexibility

**Pattern**: System intentionally allows post-deployment schema changes to accommodate emergent field research.

**Implications Across Fields**:
- Type changes can break existing data (string→number)
- Multiple→single loses data silently
- Validation additions may invalidate existing records
- Vocabulary modifications don't update existing data
- Required fields added later create incomplete records

**Documentation Needed**:
- "Schema Evolution and Field Research Reality" guide
- Safe vs breaking changes matrix
- Backup and versioning strategies
- Testing changes before deployment
- When to modify vs start fresh

### 1.4 Auto-Increment Coordination

**Pattern**: Auto-increment ranges require manual coordination between devices.

**Critical Issues**:
- Local-only storage (not synchronized)
- No device-specific namespacing
- No conflict detection for duplicates
- No range sharing mechanism
- Complete reliance on human coordination

**Impact on System**:
- Duplicate IDs when ranges overlap
- HRIDs can become non-unique
- Relationships may reference wrong records
- Data integrity compromised silently

**Documentation Needed**:
- Multi-device coordination protocols
- Range allocation strategies
- HRID uniqueness patterns
- Team communication requirements
- Recovery from duplicate scenarios

**Pattern**: Not all configuration options available in Designer GUI; JSON editing often required.

**Affected Fields**:
- RelationshipField: Vocabulary pairs
- AdvancedSelect: Hierarchy structure
- MapFormField: Advanced map options
- Conditional logic: Complex conditions
- Validation: Custom rules

**Documentation Needed**:
- "Designer Limitations and JSON Workflows" guide
- Which features require JSON
- Safe JSON editing practices
- Migration and validation tools

---

## 2. Common Technical Limitations

### 2.1 Performance Boundaries

**Pattern**: All complex fields have undocumented performance cliffs and hard-coded limits.

**Specific Thresholds**:
- Relationships: 50 comfortable, 200 unusable
- Select/MultiSelect: 100 options degraded
- AdvancedSelect: 100 nodes noticeable lag, 1000 nodes frozen
- TakePhoto: 20 photos performance cliff, 50 hard failure
- MapFormField: GPU acceleration actively disabled
- TakePoint: Continuous GPS causes battery drain
- Conditional logic: Multiple controllers lag

**Hard-Coded Limits Discovered**:
- TakePhoto: Maximum 20 images enforced
- AdvancedSelect: 300px fixed height viewport
- MapFormField: Single feature limitation (auto-clears previous)

**Documentation Needed**:
- Performance planning guide with specific thresholds
- Hard limit documentation
- Optimisation strategies
- Alternative patterns for large datasets
- Battery impact warnings for GPS fields

### 2.2 Validation Limitations

**Pattern**: Validation is limited to Yup schema, no custom functions. Type declarations often don't match enforcement.

**Common Gaps**:
- No cross-field validation
- No async validation
- No conditional requirements
- No mathematical validation
- No relationship consistency checks
- Generic error messages only

**Type Declaration vs Enforcement Mismatches**:
- ControlledNumber: Declares "faims-core::Integer" but accepts decimals
- BasicAutoIncrementer: Returns strings despite numeric appearance
- Designer enforces empty strings where nulls expected
- Mixed string/integer storage prevents field type changes

**Documentation Needed**:
- Validation capabilities matrix
- Type enforcement reality vs declarations
- Workaround patterns
- Error message customisation

### 2.3 Database API Access & Re-importation

**Pattern**: After sync, data is in CouchDB and accessible via standard APIs, but lacks guardrails.

**The Real Challenge**:
- CouchDB API allows direct database manipulation
- External systems (RSpace ELN, QGIS) can read/write
- No import validator to ensure schema compliance
- Missing JSON schema documentation
- Risk of database corruption through malformed imports

**Integration Points Under Development**:
- RSpace ELN (cloud-based electronic lab notebook)
- QGIS (desktop GIS software)
- Other external systems via CouchDB API

**What's Needed**:
- JSON database schema documentation
- Import validators/guardrails
- Schema requirements documentation
- API usage guidelines
- Round-trip integrity checks

**This is NOT about**:
- CSV re-import (that's a separate issue)
- Export format limitations
- File format conversions

**Documentation Needed**:
- CouchDB JSON schema specifications
- Field type requirements in database
- Relationship integrity rules
- Required properties per document type
- API best practices for external systems

### 2.4 CSV Export Limitations (Separate Issue)

**Pattern**: CSV exports lose structure and cannot be re-imported with relationships intact.

**Specific Issues**:
- Relationships export as strings, can't re-import
- Hierarchies flatten
- Metadata (annotations) lost
- Media files referenced not embedded
- No CSV import that reconstructs relationships

**This is separate from CouchDB API access** - even with API access, CSV round-trip doesn't work.

**Documentation Needed**:
- CSV format specifications
- Manual reconstruction procedures
- Which data is preserved vs lost

**Pattern**: Multiple fields fail silently without user feedback.

**Common Silent Failures**:
- FileUploader: Upload errors give no feedback
- TakePhoto: Size/count parameters silently ignored
- Select/RadioGroup: Validation errors not displayed
- AdvancedSelect: Cannot clear selection once made
- MapFormField: No validation error display
- Configuration parameters accepted but ignored

**Security Gaps**:
- FileUploader: No file type validation or virus scanning
- FileUploader: Accepts executable files without warning
- TakePhoto: EXIF data stripped inconsistently
- No MIME type restrictions enforced

**Documentation Needed**:
- Error handling expectations
- Security considerations guide
- Workarounds for missing feedback
- Data validation best practices

### 2.5 Component Architecture Issues

**Pattern**: Component duplication and architectural confusion creates inconsistency.

**Specific Issues**:
- TextField/FAIMSTextField duality with unclear deprecation
- MultipleTextField vs TextField with multiline:true
- Component reference bugs (LocationPermissionIssue shown for camera)
- TakePhoto and FileUploader completely separate despite overlap
- AdvancedSelect recursive rendering without optimization

**Rendering Problems**:
- AdvancedSelect: Renders entire tree immediately (no virtualization)
- MapFormField: GPU acceleration disabled harming performance
- TakePhoto: Memory leaks in preview generation loops
- No lazy loading across complex components

**Documentation Needed**:
- Component selection decision tree
- Deprecation roadmap
- Performance implications of component choices
- Memory management strategies

### 3.1 Mobile-Desktop Divergence

**Pattern**: Significant capability differences between platforms.

**Common Issues**:
- Fixed widths break mobile (500px)
- Touch targets too small (<44px)
- Camera/GPS mobile-only
- Keyboard types vary
- Offline behaviour differs

**Documentation Needed**:
- Platform capability matrix
- Responsive design requirements
- Progressive enhancement strategies

### 3.2 Accessibility Systematic Gaps

**Pattern**: Most fields fail WCAG 2.1 standards.

**Common Failures**:
- Touch targets undersized
- Missing ARIA labels
- No keyboard navigation
- Poor error announcement
- Color contrast issues

**Documentation Needed**:
- Accessibility compliance status
- Workarounds for critical issues
- Roadmap for improvements

---

## 4. Design Philosophy Implications

### 4.1 Flexibility Over Rigidity

**Principle**: System prioritizes adaptability for emergent research over data integrity guarantees.

**Trade-offs**:
- Can adapt to discoveries BUT can break existing data
- Can modify in field BUT requires careful planning
- Can work offline BUT creates sync conflicts
- Can handle complexity BUT has performance limits

**Documentation Approach**:
- Acknowledge trade-offs explicitly
- Provide clear guidance on risks
- Offer mitigation strategies
- Don't hide limitations

### 4.2 Archaeological/Research-Driven Design

**Principle**: Features designed for research realities, not ideal scenarios.

**Examples**:
- Annotations for field notes (margins)
- Uncertainty flags throughout
- Flexible relationships
- Schema evolution support
- Offline-first architecture

**Documentation Approach**:
- Explain research scenarios
- Provide discipline-specific examples
- Acknowledge messiness of fieldwork

---

## 5. Repeated Warnings Across Fields

### Common Warnings to Centralize

1. **"Changes to this configuration may affect existing data"**
2. **"Performance degrades with large datasets"**
3. **"Offline edits may create conflicts requiring resolution"**
4. **"Designer cannot configure this - JSON editing required"**
5. **"Mobile experience differs from desktop"**
6. **"Validation occurs client-side only"**
7. **"Export format requires manual reconstruction"**
8. **"Battery usage may be significant"** (GPS/camera fields)
9. **"Error messages may not display properly"** (choice fields)

### Field Category Patterns

**Choice Fields (RadioGroup, Select, Checkbox) - Shared Limitations:**
- All lack proper error display (varying degrees)
- All missing comprehensive accessibility support
- All limited to static options (no dynamic loading)
- All have performance issues with large option sets
- Designer cannot preview any of them properly
- None support field type conversion after deployment

**Media Fields (TakePhoto, FileUploader) - Shared Issues:**
- Security validation gaps
- Silent failure modes
- Metadata handling inconsistencies
- Performance limits undocumented

**Location Fields (MapFormField, TakePoint) - Common Problems:**
- Battery impact not documented
- GPS accuracy variations
- Metadata export limitations
- Platform-specific behaviors

### Field-Specific Variations

Track which warnings apply to which fields:
- Performance warnings: Relationship, Select, MultiSelect, AdvancedSelect
- JSON-only warnings: Relationship, AdvancedSelect, MapFormField
- Mobile issues: All fields with complex UI
- Export limitations: Relationship, AdvancedSelect, Media fields

---

## 6. Documentation Structure Recommendations

### Phase 2 Priorities

1. **System Architecture Documentation** (Week 1)
   - Distributed systems guide
   - Schema evolution guide
   - Platform capabilities matrix

2. **Common Patterns Documentation** (Week 2)
   - Performance planning
   - Validation strategies
   - Export/import workflows

3. **Field Documentation Consolidation** (Weeks 3-4)
   - Remove redundant warnings
   - Add cross-references to system docs
   - Standardize terminology
   - **Unified documentation for related fields** (e.g., all date fields together)

### Cross-Referencing Strategy

Each field should reference system docs:
```markdown
> **System Consideration**: This field operates within Fieldmark's 
> distributed architecture. See [Working with Distributed Data] for 
> sync behaviour and conflict resolution.
```

### Warning Standardization

Create standard warning blocks:
```markdown
> ⚠️ **Schema Change Warning**: Modifying this configuration after 
> data collection may result in data loss. See [Schema Evolution Guide] 
> for safe change practices.
```

## 10. Compound Failure Modes

### Systemic Interactions

When multiple documented issues combine, they create emergent failure modes worse than individual problems:

1. **Auto-increment + Relationships**: Duplicate IDs from poor coordination corrupt relationship networks
2. **Type Mismatches + Schema Evolution**: String/integer inconsistencies prevent field type changes
3. **Performance + Offline**: Large forms become unusable precisely when offline (no server optimization)
4. **Silent Failures + Distributed System**: Errors propagate across devices without detection
5. **Export Limitations + Validation**: Can't reimport exported data due to validation changes

### Cascading Effects

**Example Cascade**: 
1. Auto-increment conflict creates duplicate IDs
2. Relationships reference wrong records
3. Export flattens relationship structure
4. Can't detect error in CSV
5. Reimport fails or corrupts data further

### Risk Multiplication

Individual bugs become critical when combined:
- 10 relationship fields × 30 relationships each = 300 metadata fetches
- Add 5 MultiSelect fields with 50 options = 400+ UI elements
- Add offline sync overhead = 30+ second load times
- Result: Form unusable in field conditions

**Documentation Needed**:
- Common failure cascades
- Risk assessment matrices
- Mitigation strategies for compound issues
- Testing protocols for interaction effects

---

## 11. Questions for Technical Team

### Architecture Clarifications Needed

1. Is last-write-wins the only conflict resolution strategy?
2. Are there any server-side validations we're missing?
3. What's the roadmap for Designer GUI enhancements?
4. Are performance thresholds being addressed?
5. Is WCAG compliance planned?

### Documentation Priorities

1. Which limitations are being fixed vs documented?
2. What level of technical detail for JSON editing?
3. Should we document workarounds or wait for fixes?
4. How much about future roadmap to include?

---

## 8. Action Items for Consolidation

### Immediate (During Field Documentation)
- [ ] Flag system patterns in each field doc
- [ ] Track repeated warnings
- [ ] Note Designer limitations
- [ ] Document performance thresholds

### Phase 2 (Structural Documentation)
- [ ] Create system architecture guides
- [ ] Consolidate common warnings
- [ ] Build cross-reference network
- [ ] Standardize terminology

### Phase 3 (Refinement)
- [ ] Remove redundancy from field docs
- [ ] Ensure consistent messaging
- [ ] Validate all cross-references
- [ ] Test with users

---

## 9. Critical Insights Summary

### What We've Learned

1. **The system is well-architected for research** but implementation has gaps
2. **Flexibility is intentional** but requires user education
3. **Distributed behaviour is complex** but necessary for fieldwork
4. **Performance limits exist** and many are hard-coded, not configurable
5. **Platform differences are significant** but manageable with planning
6. **Type enforcement is inconsistent** creating migration barriers
7. **Silent failures are common** requiring defensive design
8. **Security gaps exist** particularly in file handling
9. **Choice fields share systematic problems** suggesting architectural issues
10. **Battery and resource impacts** are undocumented for field deployment

### Documentation Philosophy

- Be honest about limitations and hard limits
- Explain the why behind design choices
- Provide practical workarounds
- Document battery and performance impacts explicitly
- Warn about security considerations
- Focus on research success, not just technical correctness
- Group similar limitations (e.g., all choice fields)

### Emerging Meta-Patterns

1. **Implementation vs Architecture Gap**: Good architecture undermined by implementation bugs
2. **Progressive Degradation**: Fields work well up to specific thresholds, then fail dramatically
3. **Desktop-First Design**: Mobile often an afterthought despite "mobile-first" claims
4. **Validation Display Crisis**: Systematic failure across multiple field categories
5. **Configuration Ignored**: Many parameters accepted but not honored

---

*This tracking document should be continuously updated as more patterns emerge during field documentation. It will form the foundation for Phase 2's structural documentation work.*

*Last comprehensively updated: January 2025*
*Sessions reviewed for patterns:*
- RelationshipField discovery and documentation
- AdvancedSelect complete documentation  
- MultiSelect documentation research
- RichText field discovery (revealed StaticImage doesn't exist)
- RadioGroup, Select, Checkbox documentation
- TakePhoto, FileUploader, MapFormField, TakePoint documentation
- ControlledNumber documentation
- BasicAutoIncrementer synchronization analysis
- Date/Time fields unified documentation
- Choice fields consolidated analysis
- All text fields (TextField, MultilineText, Email, TemplatedString, QRCodeFormField, Address)
- All number fields (NumberField, NumberInput, ControlledNumber, BasicAutoIncrementer)

*Total fields analyzed: ALL existing field types (24 total - StaticImage was a hallucination)*
