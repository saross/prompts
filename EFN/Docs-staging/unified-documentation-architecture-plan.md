# Unified Documentation Architecture Plan

## Executive Summary
Plan to unify Fieldmark v3 field documentation into a cohesive, three-tier knowledge system that maintains both educational and production-ready content while enabling seamless navigation between related topics.

## Current Documentation Landscape

### Field-Specific Documentation (8 files, ~13,000 lines)
- **OLD Format** (4 docs): text-fields, select-choice-fields, datetime-fields, number-fields
  - Educational JSON examples with inline comments
  - Comprehensive reference style (avg ~564 lines/field)
- **NEW Format** (4 docs): display-field, location-fields, media-fields, relationship-field
  - Valid, copy-paste ready JSON
  - Template-strict format (avg ~705 lines/field)

### Cross-Field Documentation (8 files)
- conditional-logic.md (37KB) - Cross-field dependencies and logic
- validation.md (33KB) - Validation strategies across field types
- navigation.md (19KB) - Form navigation patterns
- notebook-structure.md (34KB) - Overall form architecture
- patterns.md (18KB) - Common implementation patterns
- field-selection-best-practices.md (26KB) - Choosing appropriate fields
- quick-start.md (12KB) - Getting started guide
- summary-table.md (12KB) - Field comparison matrix

### Reference Documentation (14 files)
- **Component**: namespace, meta-properties, formik-integration
- **Platform**: behaviors, performance-thresholds, accessibility
- **Operations**: migration-strategies, troubleshooting, data-export
- **Constraints**: designer-limitations, security-considerations, validation-timing

## Recommended Architecture: Three-Tier System

### Tier 1: Field Type Reference (Foundation Layer)
The 8 field category documents remain the authoritative source for field-specific information, enhanced with:
- Consistent component name mapping tables
- Standardized JSON example sections
- Bidirectional cross-references
- Direct links to applicable patterns and references

### Tier 2: Cross-Field Patterns (Integration Layer)
Workflow-based guides showing how fields work together:
1. **Getting Started Guide** - Orientation and quick wins
2. **Field Selection Guide** - Decision trees and comparisons
3. **Form Structure Guide** - Architecture and navigation
4. **Dynamic Forms Guide** - Validation and conditional logic
5. **Common Patterns Guide** - Reusable implementation patterns

### Tier 3: Technical References (Knowledge Layer)
Consolidated technical documentation:
1. **Component Reference** - Namespaces, meta-properties, Formik integration
2. **Platform Reference** - Behaviors, performance, accessibility
3. **Operations Reference** - Migration, troubleshooting, data export
4. **Constraints Reference** - Designer limitations, security, validation timing

## Implementation Phases

### Phase 1: Navigation Infrastructure (4 hours)

#### 1.1 Create Master Index
```
/field-type-index.md
├── Field Types (8 documents)
│   ├── Text & Input Fields
│   ├── Selection Fields
│   ├── Date & Time Fields
│   ├── Numeric Fields
│   ├── Location Fields
│   ├── Media Fields
│   ├── Display Fields
│   └── Relationship Fields
├── Cross-Field Patterns (5 guides)
│   ├── Getting Started
│   ├── Field Selection
│   ├── Form Structure
│   ├── Dynamic Forms
│   └── Common Patterns
└── Technical References (4 references)
    ├── Components
    ├── Platform
    ├── Operations
    └── Constraints
```

#### 1.2 Add Navigation Elements
**Header Template:**
```markdown
📚 [Field Documentation](../field-type-index.md) > [Category] > Current Document
```

**Footer Template:**
```markdown
---
## Navigation
[← Previous Field] | [Field Index](../field-type-index.md) | [Next Field →]

### Related Documentation
- **Patterns**: [Validation](../patterns/validation.md) | [Conditional Logic](../patterns/conditional.md)
- **References**: [Designer Limits](../references/constraints.md#field-name) | [Performance](../references/platform.md#field-name)
```

### Phase 2: Field Document Standardization (6 hours)

#### 2.1 Component Name Mapping Table
Add to all 8 field documents:
```markdown
## Component Name Mapping

| Designer UI Label | JSON component-name | Code File | Namespace |
|------------------|-------------------|-----------|-----------|
| Single-line Text | TextField | TextField.tsx | formik-material-ui |
| Text Field | FAIMSTextField | FAIMSTextField.tsx | faims-custom |
| Template | TemplatedStringField | TemplatedString.tsx | faims-custom |
```

#### 2.2 JSON Example Harmonization

**For OLD Format Docs:**
- Preserve educational examples with comments
- Add new section: "### Production-Ready Examples"
- Use `💡 **Note:**` for explanatory text outside JSON blocks

**For NEW Format Docs:**
- Keep valid JSON examples
- Add "### Understanding the Configuration" explanations
- Link to educational examples in OLD format docs where applicable

#### 2.3 Cross-Reference Sections
Standardized section for all field docs:
```markdown
## Related Documentation

### Within This Category
- **Similar Fields**: [TextField](#), [FAIMSTextField](#)
- **Alternative Approaches**: [RichText for formatting](#)

### Cross-Field Patterns
- **Validation**: [Field Validation Strategies](../patterns/validation.md#text-fields)
- **Conditional Display**: [Show/Hide Logic](../patterns/conditional.md#text-fields)
- **Performance**: [Large Text Handling](../patterns/performance.md#text-optimization)

### Technical References
- **Designer Limitations**: [Text Field Constraints](../references/constraints.md#text-fields)
- **Security**: [XSS Prevention](../references/security.md#text-input)
- **Migration**: [From v2 to v3](../references/migration.md#text-fields)
```

### Phase 3: Cross-Field Document Integration (3 hours)

#### 3.1 Consolidation Map
- `quick-start.md` + `summary-table.md` → `getting-started-guide.md`
- `field-selection-best-practices.md` → `field-selection-guide.md` (enhanced)
- `notebook-structure.md` + `navigation.md` → `form-structure-guide.md`
- `validation.md` + `conditional-logic.md` → `dynamic-forms-guide.md`
- `patterns.md` → `common-patterns-guide.md` (enhanced)

#### 3.2 Add Field-Specific Anchors
Each consolidated guide includes field-specific sections:
```markdown
## Text Field Validation {#text-fields}
Specific validation patterns for text-based inputs...

## Number Field Validation {#number-fields}
Numeric validation strategies...
```

### Phase 4: Reference Document Consolidation (3 hours)

#### 4.1 Consolidation Structure
**component-reference.md:**
- Component Namespaces
- Meta Properties
- Formik Integration
- Field-specific sections with anchors

**platform-reference.md:**
- Platform Behaviors
- Performance Thresholds
- Accessibility Guidelines
- Device-specific considerations

**operations-reference.md:**
- Migration Strategies
- Troubleshooting Framework
- Data Export Formats
- Backup and Recovery

**constraints-reference.md:**
- Designer Limitations (by field type)
- Security Considerations
- Validation Timing
- Known Issues

#### 4.2 Field-Specific Sections
Each reference includes targeted sections:
```markdown
## Designer Limitations

### Text Fields {#text-fields}
- Single-line text: No multiline in Designer
- Template strings: JSON-only configuration
...

### Number Fields {#number-fields}
- Step increments require BasicAutoIncrementer
- Validation limited to min/max
...
```

## Execution Timeline

### Week 1: Foundation (Days 1-5)
- **Day 1**: Create master index, establish folder structure
- **Day 2-3**: Add navigation headers/footers to all 8 field docs
- **Day 4-5**: Create component mapping tables for all fields

### Week 2: Enhancement (Days 6-10)
- **Day 6-7**: Harmonize JSON examples across all docs
- **Day 8-9**: Add cross-reference sections
- **Day 10**: Create unified type system reference

### Week 3: Integration (Days 11-15)
- **Day 11-12**: Consolidate cross-field documentation
- **Day 13-14**: Consolidate reference documentation
- **Day 15**: Update all internal cross-links

### Week 4: Polish (Days 16-20)
- **Day 16-17**: Standardize warning/security formats
- **Day 18**: Add migration path sections
- **Day 19**: Navigation testing and verification
- **Day 20**: Final review and adjustments

## Success Criteria

### Navigation
- ✅ Maximum 3 clicks to any related content
- ✅ Every document has clear breadcrumbs
- ✅ Bidirectional linking between all tiers

### Content Quality
- ✅ JSON examples clearly marked as educational or production
- ✅ Component names consistently mapped across all docs
- ✅ Security warnings prominently displayed
- ✅ Designer limitations accurately documented

### Completeness
- ✅ All 23 field types documented
- ✅ Cross-field patterns cover common use cases
- ✅ Reference docs address all technical concerns
- ✅ Migration paths from old approaches documented

## Benefits

### For Developers
- Clear navigation between related topics
- Both learning (educational) and doing (production) resources
- Comprehensive cross-references reduce search time
- Consistent terminology and structure

### For Maintainers
- Modular structure enables targeted updates
- Clear separation of concerns (field/pattern/reference)
- Reduced duplication through shared references
- Scalable architecture for new fields

### For the Documentation
- Transforms isolated documents into interconnected knowledge system
- Preserves valuable educational content while adding production resources
- Creates clear information hierarchy
- Enables multiple learning paths

## Risk Mitigation

### Backward Compatibility
- No documents deleted, only enhanced
- Existing URLs preserved through redirects if needed
- Git history maintains all previous versions

### Quality Assurance
- Automated link checking before deployment
- JSON validation for all examples
- Review checklist for each phase
- User testing with sample workflows

## Maintenance Plan

### Regular Updates
- Monthly review of Designer limitations
- Quarterly update of migration strategies
- Security advisories as needed
- Performance threshold adjustments based on metrics

### Expansion Framework
- New fields follow established template
- Pattern guides updated with new use cases
- Reference docs expanded with platform updates
- Cross-links added systematically

## Conclusion

This plan transforms the current collection of field documentation into a unified, navigable knowledge system. By maintaining both educational and production content, organizing documents into clear tiers, and establishing comprehensive cross-references, we create documentation that serves both learning and implementation needs effectively.

The three-tier architecture (Field Types → Cross-Field Patterns → Technical References) provides clear mental models for users while enabling maintainers to update specific aspects without affecting the whole system.

Total estimated effort: **16 hours** of focused work, best executed over 4 weeks to allow for review and refinement between phases.