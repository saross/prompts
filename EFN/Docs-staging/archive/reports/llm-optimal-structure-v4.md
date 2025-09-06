# LLM-Optimal Documentation Structure v4
## For Fieldmark v3 Category Documentation

### Purpose
This document defines the LLM-optimal structure developed for field category documentation (text-fields, number-fields, datetime-fields, select-choice-fields, media-fields). This structure prioritizes early practical context, decision support, and hierarchical clarity for both human readers and LLM processing.

## Key Principles

### 1. Early Practical Context
- Designer Usage Guide at position #2 (immediately after Overview)
- Field Selection Guide at position #3 (decision support before deep dive)
- Critical security vulnerabilities at position #4 (safety first)

### 2. Hierarchical Clarity
- Individual Field Reference as H2 section header
- Individual fields as H3 subsections under it
- Consistent subsection structure within each field

### 3. Content Organization
- Quick Reference boxes with key metrics immediately visible
- Core Configuration examples right after Purpose
- Common Characteristics with [affects: Field] notation
- Distributed anti-patterns (not centralized)

## Standard Section Order (23 sections)

### H1: Category Title
`# [Category] Fields - Fieldmark v3 Documentation`

### H2 Sections in Order:

1. **Overview {essential}**
   - Introduction paragraph
   - Key terminology definitions
   - Component namespace information

2. **Designer Usage Guide {essential}**
   - Creating fields step-by-step
   - Designer limitations table
   - Visual workflow description

3. **Field Selection Guide {essential}**
   - Decision matrix/flowchart
   - Field comparison table
   - Use case recommendations

4. **⚠️ CRITICAL SECURITY VULNERABILITIES {essential}**
   - Known security issues
   - Risk assessment
   - Mitigation strategies

5. **What These Fields Cannot Do {important}**
   - Explicit limitations
   - Common misconceptions
   - Alternative approaches

6. **Common Use Cases {important}**
   - Real-world scenarios
   - Best fit examples
   - Domain-specific applications

7. **Designer Component Mapping {essential}**
   - Designer name → JSON component table
   - Type return mappings
   - Namespace requirements

8. **Designer Capabilities vs JSON Enhancement {essential}**
   - What Designer can/cannot do
   - JSON-only features
   - Enhancement strategies

9. **Component Namespace Errors {important}**
   - Common error messages
   - Namespace troubleshooting
   - Prevention strategies

10. **Common Characteristics {important}**
    - Shared behaviors [affects: All fields]
    - Validation timing behavior
    - Platform differences
    - State management

11. **Individual Field Reference {essential}**
    - H3 subsections for each field
    - Consistent internal structure per field

12. **Troubleshooting Guide {important}**
    - Common issues table
    - Field-specific problems
    - Resolution strategies

13. **JSON Examples {comprehensive}**
    - Complete working examples
    - Complex configurations
    - Integration patterns

14. **Migration and Best Practices {comprehensive}**
    - From deprecated components
    - Version migration paths
    - Optimization strategies

15. **Field Quirks Index (2025-08) {comprehensive}**
    - Unexpected behaviors
    - Platform-specific issues
    - Workarounds

16. **Performance Thresholds Table (2025-08) {essential}**
    - Specific numeric limits
    - Degradation points
    - Optimization triggers

17. **JSON Patterns Cookbook (2025-08) {comprehensive}**
    - Common patterns
    - Advanced techniques
    - Reusable templates

18. **JSON Anti-patterns Quick Index {comprehensive}**
    - Common mistakes
    - Why they fail
    - Correct approaches

19. **Quick Diagnosis Tables (2025-08) {important}**
    - Symptom → Cause → Fix
    - Decision trees
    - Rapid troubleshooting

20. **Field Interaction Matrix (2025-08) {important}**
    - Field dependencies
    - Conditional relationships
    - Data flow patterns

21. **Migration Warnings Index (2025-08) {comprehensive}**
    - Breaking changes
    - Deprecation notices
    - Timeline information

22. **Error Message Quick Reference (2025-08) {important}**
    - Error code → meaning
    - Common causes
    - Resolution steps

23. **Metadata {comprehensive}**
    - Document version
    - Last updated
    - Related documents

## Individual Field Structure (H3 level)

Each field under "Individual Field Reference" follows this structure:

### Field Name (Designer Name) {importance} [status if applicable]

#### Quick Reference Box
```markdown
| Property | Details |
|----------|---------|
| Component | faims-custom::ComponentName |
| Type Return | faims-core::Type |
| Designer | ✅ Full support / ⚠️ Partial / ❌ Not available |
| Required | Works with validation |
| Default | [default value behavior] |
| Touch Targets | [specific measurements] |
| Performance | [thresholds with numbers] |
| Storage | [data format] |
```

#### Purpose
Brief description of field's primary use case

#### Key Features
- Feature bullets with inline measurements/thresholds
- Platform-specific behaviors noted inline
- Performance implications stated explicitly

#### Core Configuration
```json
// Minimal working example
```

#### Designer Configuration
Step-by-step Designer instructions

#### Validation
- Timing behavior (mount/change/blur/submit)
- Available validators
- Error display behavior

#### Advanced Configuration
- Additional parameters
- Complex scenarios
- Integration patterns

#### Common Issues
- Platform-specific problems
- Known limitations
- Workarounds

#### Implementation Examples
Multiple named examples with complete JSON:
- Basic usage example
- Advanced configuration example
- Migration example
- Domain-specific examples

## Content Guidelines

### Line Targets
- Category documents: ~2,200-2,500 lines (lean, focused)
- Offload technical details to standalone documents
- Preserve all critical information

### Style Requirements
- Complete working JSON examples
- Specific measurements (pixels, counts, thresholds)
- Platform differences inline (not separate sections)
- [affects: Field] notation in Common Characteristics
- {importance} tags on all H2 sections

### Anti-pattern Distribution
- Include field-specific anti-patterns within each field section
- Not centralized in one location
- Show incorrect approach → explain why → show correct approach

## Migration Notes for Existing Documents

### To upgrade text-fields-v05.md:
1. Move Designer Usage Guide from position #11 to #2
2. Move Field Selection Guide to position #3
3. Ensure Individual Field Reference is H2 with fields as H3
4. Add Quick Reference boxes to all fields
5. Add inline measurements and thresholds

### To upgrade number-fields-v05.md:
1. Already follows most of v4 structure
2. Verify Quick Reference boxes have all 3 new rows
3. Add Validation Timing Behavior to Common Characteristics
4. Ensure anti-patterns distributed per field

### To upgrade datetime-fields-v05.md:
1. Already follows most of v4 structure
2. Add Quick Reference box enhancements
3. Verify inline measurements present
4. Check for missing named examples

## Implementation Checklist

When creating or updating a category document:

- [ ] H1 title follows format
- [ ] All 23 H2 sections present in order
- [ ] All H2 sections have {importance} tags
- [ ] Individual Field Reference is H2, not H1
- [ ] All fields are H3 under Individual Field Reference
- [ ] Quick Reference boxes have 8+ rows including new metrics
- [ ] Designer Usage Guide at position #2
- [ ] Field Selection Guide at position #3
- [ ] Anti-patterns distributed per field
- [ ] [affects: Field] notation in Common Characteristics
- [ ] Validation Timing Behavior subsection added
- [ ] All examples have complete working JSON
- [ ] Inline measurements and thresholds throughout
- [ ] Platform-specific notes inline, not separate
- [ ] Document stays under 2,700 lines

## Related Documents
- `consolidation-prompt-choice-fields-v4-llm-optimal.md` - Prompt using this structure
- `consolidation-prompt-choice-fields-v5-lossless.md` - Enhanced for complete extraction
- `standalone-documents-proposal.md` - Offloading strategy
- `structure-alignment-analysis.md` - Cross-document comparison