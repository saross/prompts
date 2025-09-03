# LLM-Optimized LOSSLESS Consolidation Prompt: Media Fields (v5)

## Core Directive
Create comprehensive, LLM-optimized documentation with COMPLETE LOSSLESS extraction from source documents. The goal is to amalgamate, de-duplicate, and enhance WITHOUT losing ANY content from the source documents. Every technical detail, measurement, example, and note must be preserved.

## Input Documents
1. FileUploader.md - File upload field documentation
2. TakePhoto.md - Photo capture field documentation
3. [Additional media field documents as available]

## Target Document: media-fields-v05.md

## CRITICAL CORRECTIONS FROM CHOICE FIELDS
**IMPORTANT**: Based on codebase verification, ensure these are correct:
1. Use `"faims-core::Bool"` NOT `"faims-core::Boolean"` for boolean types
2. Use `["yup.bool"]` NOT `["yup.boolean"]` for boolean validation
3. Component namespace is always `"faims-custom"` for these fields
4. Component names must match EXACTLY (case-sensitive): FileUploader, TakePhoto, etc.
5. Verify error display implementation - some components may lack FormHelperText

## CRITICAL EXTRACTION REQUIREMENTS

### LOSSLESS CONTENT PRESERVATION
You MUST extract and preserve:

1. **Every Named Example** - Extract ALL examples with their EXACT titles
2. **Every Technical Specification** including:
   - File size limits and upload constraints
   - Image resolution and compression settings
   - Camera API specifications
   - Storage paths and file naming conventions
   - Platform-specific camera behaviors
   - EXIF data handling

3. **Every Table** with ALL columns:
   - File type support tables
   - Platform capability matrices
   - Storage quota specifications
   - Error handling tables

4. **Every Section** from source including:
   - Media processing pipelines
   - Offline storage strategies
   - Sync and conflict resolution
   - Thumbnail generation
   - Metadata extraction

5. **Every Platform-Specific Detail**:
   - iOS camera permissions and behaviors
   - Android camera API differences
   - Web browser file upload constraints
   - Progressive Web App capabilities

## REQUIRED STRUCTURE - LLM-OPTIMIZED ORDER

```markdown
# Media Fields - Fieldmark v3 Documentation

## Overview {essential}
### DESIGNER QUICK GUIDE
### CRITICAL NAMING DISAMBIGUATION  
### Media Capture Fields (1-N)
### Component Status Summary

## Designer Usage Guide {essential}
[POSITION #2 - CRITICAL for LLM-optimal structure]
### Creating Fields Step-by-Step
### Designer Limitations Table
### Visual Workflow Description

## Field Selection Guide {essential}
[POSITION #3 - Early decision support]
### Quick Decision Tree
### Quick Decision Matrix
### Selection Strategy
### Platform Considerations

## ⚠️ CRITICAL SECURITY VULNERABILITIES {essential}
[POSITION #4 - Safety first]

## What These Fields Cannot Do {important}

## Common Use Cases {important}

## Designer Component Mapping {essential}

## Designer Capabilities vs JSON Enhancement {essential}

## Component Namespace Errors {important}

## Common Characteristics {important}
### Validation Timing Behavior [affects: All fields] {important}
[REQUIRED - Add this subsection with mount/change/blur/submit timing]

## Individual Field Reference {essential}
[THIS MUST BE H2, not H1]

### FileUploader (File Uploader in Designer) {essential}
[Each field MUST be H3 under Individual Field Reference]

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | faims-custom::FileUploader |
| Type Return | [verify from codebase] |
| Designer | ✅ Full support / ⚠️ Partial / ❌ Not available |
| Touch Targets | [specific measurements] |
| Performance | [thresholds with numbers] |
| Storage | [data format] |

[Continue with standard field structure]

## Troubleshooting Guide {important}

## JSON Examples {comprehensive}

## Migration and Best Practices {comprehensive}

## Field Quirks Index (2025-08) {comprehensive}

## Performance Thresholds Table (2025-08) {essential}

## JSON Patterns Cookbook (2025-08) {comprehensive}

## JSON Anti-patterns Quick Index {comprehensive}

## Quick Diagnosis Tables (2025-08) {important}

## Field Interaction Matrix (2025-08) {important}

## Migration Warnings Index (2025-08) {comprehensive}

## Error Message Quick Reference (2025-08) {important}

## Metadata {comprehensive}
```

## ENHANCED QUICK REFERENCE REQUIREMENTS
Each field's Quick Reference box MUST include these 8+ rows:
1. Component (namespace::name)
2. Type Return (faims-core::Type)
3. Designer Support Level
4. Required Field Support
5. Default Value Behavior
6. **Touch Targets** (specific pixel measurements)
7. **Performance** (numeric thresholds)
8. **Storage** (data format and constraints)

## VALIDATION REQUIREMENTS
1. Check all type-returned values against codebase patterns
2. Verify validation schema syntax matches yup patterns
3. Confirm component names are exactly correct
4. Note which components have error display vs silent validation

## ANTI-PATTERN DISTRIBUTION
- Include field-specific anti-patterns within each field section
- Do NOT centralize all anti-patterns in one location
- Show: incorrect approach → explain why → correct approach

## TARGET METRICS
- Document length: ~2,200-2,500 lines (lean, focused)
- Complete working JSON examples for every pattern
- Platform-specific details inline (not separate sections)
- Specific measurements and thresholds throughout
- 85-90% content coverage from source documents minimum

## QUALITY CHECKLIST
Before finalizing:
- [ ] All fields are H3 under H2 "Individual Field Reference"
- [ ] Designer Usage Guide is at position #2
- [ ] Field Selection Guide is at position #3
- [ ] Quick Reference boxes have all 8 rows
- [ ] Validation Timing Behavior subsection added
- [ ] All type-returned values verified
- [ ] All component names exactly match codebase
- [ ] Anti-patterns distributed per field
- [ ] All 23 H2 sections present with {importance} tags