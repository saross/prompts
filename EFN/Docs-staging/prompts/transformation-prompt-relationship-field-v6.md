# Reference-Aware Transformation Prompt: Relationship Field (v6)

## Core Directive
Transform single-field documentation for RelatedRecordSelector into LLM-optimized format with AWARENESS of extracted reference documents. Focus on relationship-specific content while linking to universal patterns in reference docs. Extract COMPLETE relationship patterns but avoid duplicating reference material.

## Input Document
1. relationship.md - RelatedRecordSelector field documentation

## Target Document: relationship-field-v05.md (singular)

## REFERENCE DOCUMENT AWARENESS

### Content Already Extracted to References - DO NOT DUPLICATE

The following content exists in reference documents. Link to these instead of duplicating:

1. **[Validation Timing Reference](../reference-docs/validation-timing-reference.md)**
   - Universal mount/change/blur/submit behavior
   - Formik touched state management
   - Generic validation lifecycle

2. **[Component Namespace Reference](../reference-docs/component-namespace-reference.md)**
   - Namespace troubleshooting procedures
   - Case sensitivity rules
   - Generic namespace errors

3. **[Data Export Reference](../reference-docs/data-export-reference.md)**
   - CSV/JSON format basics
   - Universal special character handling
   - Generic Excel issues

4. **[Security Considerations Reference](../reference-docs/security-considerations-reference.md)**
   - XSS prevention patterns
   - SQL injection mitigation
   - Generic input sanitization

5. **[Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md)**
   - Form-wide performance limits
   - Universal render thresholds
   - Generic optimization triggers

6. **[Meta Properties Reference](../reference-docs/meta-properties-reference.md)**
   - Annotation configuration
   - Uncertainty fields
   - Persistent settings

7. **[Designer Limitations Reference](../reference-docs/designer-limitations-reference.md)**
   - Universal Designer constraints
   - JSON-only configurations
   - Testing limitations

8. **[Formik Integration Reference](../reference-docs/formik-integration-reference.md)**
   - Generic Formik state management
   - Field array handling basics
   - Validation integration patterns

9. **[Accessibility Reference](../reference-docs/accessibility-reference.md)**
   - WCAG compliance standards
   - Universal touch target requirements
   - Generic screen reader support

### Relationship-Specific Content to INCLUDE

Focus on what's UNIQUE to relationship fields:

**RelatedRecordSelector Specific:**
- Relationship types (Child vs Linked)
- Bidirectional update mechanisms
- Vocabulary pair configuration
- Relationship cardinality (1:1, 1:N, N:N)
- Performance with large relationship sets
- Soft-delete orphaning behavior
- Offline reciprocal update delays
- Query performance optimization
- UI selection patterns (modal, dropdown)
- Circular relationship prevention
- Data coherence strategies
- Relationship qualification vocabulary

## CRITICAL CORRECTIONS FROM PREVIOUS DOCS
1. Component namespace is always `"faims-custom"` for RelatedRecordSelector
2. Component name is case-sensitive: RelatedRecordSelector
3. Returns `faims-core::Relationship` type
4. Performance degrades at 50+ relationships, unusable at 200+
5. Vocabulary pairs are JSON-only configuration

## REQUIRED STRUCTURE - LLM-OPTIMIZED SINGLE FIELD

```markdown
# Relationship Field - Fieldmark v3 Documentation

## Overview {essential}
### DESIGNER QUICK GUIDE
[Single field quick reference]

### CRITICAL NAMING DISAMBIGUATION  
[RelatedRecordSelector naming clarification]

### Field Capabilities Summary
[One-paragraph overview]

### Component Status
[Status table for single field]

## Designer Usage Guide {essential}
### What to Select in Designer
[Designer selection path]

### When JSON Enhancement is Required
[Relationship-specific JSON needs]

### Designer Limitations {important}
See [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) for universal constraints.

**Relationship-Specific Designer Limitations:**
[Only limitations unique to relationships]

## Relationship Types Guide {essential}

### Decision Tree
```
Need to connect records?
├─ Parent owns children?
│  └─ YES → Child relationship
│     ├─ Cascade delete: Yes
│     └─ Best for: Components, samples
│
└─ Equal partnership?
   └─ YES → Linked relationship
      ├─ Cascade delete: No
      └─ Best for: Cross-references
```

### Relationship Type Matrix
[Child vs Linked comparison]

### Vocabulary Pairs
[Bidirectional labeling system]

## ⚠️ Critical Performance Risks {essential}
- 50+ relationships: Noticeable lag
- 100+ relationships: Severe degradation
- 200+ relationships: Unusable
- Mitigation strategies

## What This Field Cannot Do {important}
[Relationship-specific limitations]

## Common Use Cases {important}
[Relationship-specific use cases]

## Designer Component Mapping {essential}
[Relationship field mapping]

## Designer Capabilities vs JSON Enhancement {essential}
[Relationship-specific Designer vs JSON]

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Relationship-Specific Security Notes:**
[Unique to relationships]

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for general limits.

**Relationship-Specific Performance:**
[Detailed performance metrics]

### Validation Patterns {important}
See [Validation Timing Reference](../reference-docs/validation-timing-reference.md) for universal behavior.

**Relationship-Specific Validation:**
[Relationship validation patterns]

### Platform Behaviors {important}
[Platform-specific differences]

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.

### Export Behavior {important}
See [Data Export Reference](../reference-docs/data-export-reference.md) for universal patterns.

**Relationship-Specific Export:**
[Relationship export format]

## Field Reference {essential}

### RelatedRecordSelector {essential}

#### Purpose {essential}
[Field description]

#### Quick Reference
[Properties table]

#### Core Configuration
[Essential examples]

#### Advanced Configuration
[Complex examples with vocabulary pairs]

#### Platform-Specific Behaviors
[Platform differences]

#### Common Issues & Solutions
[Troubleshooting]

## Troubleshooting Guide {important}

## JSON Examples {comprehensive}

## Migration and Best Practices {comprehensive}

## Field Quirks Index (2025-01) {comprehensive}

## Performance Thresholds Summary {essential}

## JSON Patterns Cookbook (2025-01) {comprehensive}

## JSON Anti-patterns Quick Index {comprehensive}

## Quick Diagnosis Tables (2025-01) {important}

## Field Interaction Matrix (2025-01) {important}

## Migration Warnings Index (2025-01) {comprehensive}

## See Also {comprehensive}
- **Other Field Categories**: Links to other v05 docs
- **Reference Documents**: All 9 references

## Error Message Quick Reference {important}

## Metadata {comprehensive}
```

## EXTRACTION REQUIREMENTS

### From Source Document, Extract:
1. All relationship type definitions and behaviors
2. All vocabulary pair configurations
3. All performance thresholds and measurements
4. All cascade delete behaviors
5. All offline synchronization patterns
6. All UI selection modes
7. All error messages and solutions
8. All complete JSON examples

### Link to References For:
1. Generic validation timing
2. Universal namespace errors
3. Basic CSV/JSON export
4. Common security patterns
5. Form-wide performance limits
6. Standard meta properties
7. General Designer limitations
8. Basic Formik integration
9. WCAG compliance standards

## TARGET METRICS
- Document length: ~600-800 lines (single field)
- Complete relationship examples
- Performance measurements specific
- Vocabulary pair patterns documented
- Links to all 9 reference documents

## QUALITY CHECKLIST
- [ ] Designer Usage Guide is at position #2
- [ ] Relationship Types Guide at position #3
- [ ] Links to reference docs use ../reference-docs/ path
- [ ] No duplication of reference content
- [ ] Relationship-specific content comprehensive
- [ ] Performance limits clearly stated
- [ ] Vocabulary pairs explained with examples
- [ ] Soft-delete behavior documented