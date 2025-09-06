# Reference-Aware Transformation Prompt: Display Field (v6)

## Core Directive
Transform single-field documentation for RichText into LLM-optimized format with AWARENESS of extracted reference documents. Focus on display-specific content while linking to universal patterns in reference docs. Extract COMPLETE display patterns but avoid duplicating reference material.

## Input Document
1. display.md - RichText field documentation

## Target Document: display-field-v05.md (singular)

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

### Display-Specific Content to INCLUDE

Focus on what's UNIQUE to display fields:

**RichText Specific:**
- Static HTML content rendering
- Markdown to HTML conversion
- Read-only display behavior
- Styling limitations and overrides
- Image embedding capabilities
- Link handling and security
- Content sanitization rules
- Typography and formatting options
- Responsive display behaviors
- Print-friendly rendering
- No data storage (display only)
- Form instruction use cases
- Section headers and dividers
- Warning and notice displays

**Note:** This is NOT TemplatedStringField (which generates dynamic identifiers). RichText is purely static display.

## CRITICAL CORRECTIONS FROM PREVIOUS DOCS
1. Component namespace is always `"faims-custom"` for RichText
2. Component name is case-sensitive: RichText
3. Returns `faims-core::String` but stores empty string always
4. Not for dynamic content (use TemplatedStringField for that)
5. HTML content requires careful sanitization

## REQUIRED STRUCTURE - LLM-OPTIMIZED SINGLE FIELD

```markdown
# Display Field - Fieldmark v3 Documentation

## Overview {essential}
### DESIGNER QUICK GUIDE
[Single field quick reference for RichText]

### CRITICAL NAMING DISAMBIGUATION  
[RichText vs TemplatedStringField clarification]

### Field Capabilities Summary
[One-paragraph overview of display capabilities]

### Component Status
[Status table for single field]

## Designer Usage Guide {essential}
### What to Select in Designer
[Designer selection path]

### When JSON Enhancement is Required
[Display-specific JSON needs]

### Designer Limitations {important}
See [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) for universal constraints.

**Display-Specific Designer Limitations:**
[Only limitations unique to RichText]

## Display Content Guide {essential}

### Content Type Decision Tree
```
Need to display content?
├─ Static instructions/warnings?
│  └─ YES → RichText
│     ├─ HTML/Markdown support
│     └─ Best for: Form help, section headers
│
├─ Dynamic identifiers?
│  └─ NO → Use TemplatedStringField
│
└─ User-editable content?
   └─ NO → Use TextField/MultilineTextField
```

### Content Format Support
[HTML vs Markdown capabilities]

### Styling Options
[Typography and formatting]

## ⚠️ Critical Security Risks {essential}
- XSS via unsanitized HTML
- Script injection attempts
- Malicious link insertion
- Mitigation strategies

## What This Field Cannot Do {important}
[Display-specific limitations]

## Common Use Cases {important}
[Display-specific use cases]

## Designer Component Mapping {essential}
[Display field mapping]

## Designer Capabilities vs JSON Enhancement {essential}
[Display-specific Designer vs JSON]

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Display-Specific Security Notes:**
- HTML sanitization requirements
- Script tag prevention
- Link validation needs
[Unique to display fields]

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for general limits.

**Display-Specific Performance:**
- Content length limits
- Image loading impacts
- Rendering performance
[Display-specific metrics]

### Validation Patterns {important}
See [Validation Timing Reference](../reference-docs/validation-timing-reference.md) for universal behavior.

**Display-Specific Validation:**
- No validation (read-only)
- Always returns empty string
[Display validation patterns]

### Platform Behaviors {important}
[Platform-specific rendering differences]

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.

Note: RichText fields typically don't support annotations/uncertainty (display only)

### Export Behavior {important}
See [Data Export Reference](../reference-docs/data-export-reference.md) for universal patterns.

**Display-Specific Export:**
- Always exports empty string
- Not included in data exports
- Display-only purpose
[Display export behavior]

## Field Reference {essential}

### RichText {essential}

#### Purpose {essential}
[Field description - static display]

#### Quick Reference
[Properties table]

#### Core Configuration
[Essential examples]

#### Advanced Configuration
[Complex HTML/Markdown examples]

#### Platform-Specific Behaviors
[Rendering differences]

#### Common Issues & Solutions
[Troubleshooting]

## Troubleshooting Guide {important}

## JSON Examples {comprehensive}

### Example: Form Instructions
[JSON with HTML content]

### Example: Section Divider
[JSON with styled header]

### Example: Warning Notice
[JSON with formatted alert]

### Example: Multi-paragraph Help
[JSON with Markdown content]

## Migration and Best Practices {comprehensive}

## Field Quirks Index (2025-01) {comprehensive}

## Performance Thresholds Summary {essential}

## JSON Patterns Cookbook (2025-01) {comprehensive}

## JSON Anti-patterns Quick Index {comprehensive}

## Quick Diagnosis Tables (2025-01) {important}

## Field Interaction Matrix (2025-01) {important}

## Migration Warnings Index (2025-01) {comprehensive}

## See Also {comprehensive}
- **TemplatedStringField**: For dynamic content generation
- **TextField**: For user-editable content
- **Other Field Categories**: Links to other v05 docs
- **Reference Documents**: All 9 references

## Error Message Quick Reference {important}

## Metadata {comprehensive}
```

## EXTRACTION REQUIREMENTS

### From Source Document, Extract:
1. All HTML tag support and restrictions
2. All Markdown syntax support
3. All styling options and limitations
4. All security sanitization rules
5. All image embedding patterns
6. All link handling behaviors
7. All responsive display rules
8. All complete JSON examples

### Link to References For:
1. Generic validation timing (even though read-only)
2. Universal namespace errors
3. Basic CSV/JSON export
4. Common security patterns
5. Form-wide performance limits
6. Standard meta properties
7. General Designer limitations
8. Basic Formik integration
9. WCAG compliance standards

## TARGET METRICS
- Document length: ~500-700 lines (single display field)
- Complete HTML/Markdown examples
- Security warnings prominent
- Clear differentiation from TemplatedStringField
- Links to all 9 reference documents

## QUALITY CHECKLIST
- [ ] Designer Usage Guide is at position #2
- [ ] Display Content Guide at position #3
- [ ] Links to reference docs use ../reference-docs/ path
- [ ] No duplication of reference content
- [ ] Display-specific content comprehensive
- [ ] Security risks clearly stated
- [ ] HTML/Markdown examples included
- [ ] Differentiation from dynamic fields clear