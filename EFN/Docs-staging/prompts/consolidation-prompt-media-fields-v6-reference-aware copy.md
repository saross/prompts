# Reference-Aware Consolidation Prompt: Media Fields (v6)

## Core Directive
Create comprehensive, LLM-optimized documentation for media fields with AWARENESS of extracted reference documents. Focus on media-specific content while linking to universal patterns in reference docs. Extract COMPLETE content from source documents but avoid duplicating reference material.

## Input Documents
1. FileUploader.md - File upload field documentation
2. TakePhoto.md - Photo capture field documentation

## Target Document: media-fields-v05.md

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

### Media-Specific Content to INCLUDE

Focus on what's UNIQUE to media fields:

**FileUploader Specific:**
- File type restrictions and MIME type validation
- Upload size limits and chunking strategies
- Multi-file selection and management
- Progress tracking and cancellation
- Offline upload queue management
- File storage paths and naming conventions
- Thumbnail generation for images
- File metadata extraction

**TakePhoto Specific:**
- Camera API permissions and fallbacks
- Platform-specific camera behaviors
- Image compression and quality settings
- EXIF data handling and privacy
- Orientation correction
- Live preview considerations
- Flash and camera switching
- Burst mode capabilities

## CRITICAL CORRECTIONS FROM PREVIOUS DOCS
1. Component namespace is always `"faims-custom"` for custom fields
2. Component names are case-sensitive: FileUploader, TakePhoto
3. File fields typically return arrays even for single files
4. Verify actual return types from codebase

## REQUIRED STRUCTURE - LLM-OPTIMIZED WITH REFERENCES

```markdown
# Media Fields - Fieldmark v3 Documentation

## Overview {essential}
### DESIGNER QUICK GUIDE
[Media-specific quick reference]

### CRITICAL NAMING DISAMBIGUATION  
[Media field naming clarifications]

### Media Capture Fields (1-N)
[List each media field with one-line description]

### Component Status Summary
[Media-specific status table]

## Designer Usage Guide {essential}
### What to Select in Designer
[Media-specific Designer options]

### When JSON Enhancement is Required
[Media-specific JSON needs]

### Designer Limitations {important}
See [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) for universal constraints.

**Media-Specific Designer Limitations:**
[Only limitations unique to media fields]

## Field Selection Guide {essential}

### Decision Tree
```
Need to capture media?
├─ Static files from device?
│  └─ YES → FileUploader
│     ├─ Returns: faims-core::Array<File>
│     └─ Best for: Documents, existing images
│
├─ Take new photo with camera?
   └─ YES → TakePhoto
      ├─ Returns: faims-core::Array<Photo>
      └─ Best for: Field documentation
```

### Decision Matrix
[Media-specific comparison table]

### Selection Strategy
[Media-specific recommendations]

## ⚠️ Critical Media Security Risks {essential}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for general security patterns.

**Media-Specific Security Concerns:**
- File upload size attacks
- Malicious file type uploads
- EXIF data privacy leaks
- Path traversal via filenames
- JavaScript in SVG uploads
[Media-specific only]

## What These Fields Cannot Do {important}
[Media-specific limitations]

## Common Use Cases {important}
[Media-specific use cases]

## Designer Component Mapping {essential}
[Media field mappings]

## Designer Capabilities vs JSON Enhancement {essential}
[Media-specific Designer vs JSON]

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

**Media-Specific Namespace Issues:**
[Only if unique to media fields]

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Media-Specific Security Notes:**
[Unique to media fields]

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for general limits.

**Media-Specific Performance:**
- File upload timeout: 120 seconds default
- Max file size: Platform-dependent (typically 100MB)
- Image processing limit: 4096x4096 pixels
- Concurrent uploads: 3 maximum
[Media-specific metrics]

### Validation Patterns {important}
See [Validation Timing Reference](../reference-docs/validation-timing-reference.md) for universal behavior.

**Media-Specific Validation:**
- File type validation on selection
- Size validation before upload
- Async validation during upload
[Media-specific patterns]

### Platform Behaviors {important}
[Media-specific platform differences]

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.
[Note if media fields support annotation/uncertainty]

### Export Behavior {important}
See [Data Export Reference](../reference-docs/data-export-reference.md) for universal patterns.

**Media-Specific Export:**
- Binary files: Referenced by path in CSV
- Base64 encoding: In JSON exports
- File sync strategies
[Media-specific export issues]

## Individual Field Reference {essential}

### FileUploader {essential}

#### Purpose {essential}
[Field description]

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | faims-custom::FileUploader |
| Returns | faims-core::Array<File> |
| Designer | ✅ Full support |
| Touch Target | Upload button 44x44px minimum |
| Max File Size | 100MB (configurable) |
| Concurrent | 3 uploads maximum |
| Offline | ✅ Queued for sync |

#### Core Configuration
[Essential examples]

#### Advanced Configuration
[Complex examples]

#### Platform-Specific Behaviors
[Platform differences]

#### Common Issues & Solutions
[Troubleshooting]

### TakePhoto {essential}
[Similar structure]

## Troubleshooting Guide {important}

## JSON Examples {comprehensive}

## Migration and Best Practices {comprehensive}

## Field Quirks Index (2025-08) {comprehensive}

## Performance Thresholds Summary {essential}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for detailed metrics.

**Media-Specific Thresholds:**
[Table of media-specific limits]

## JSON Patterns Cookbook (2025-08) {comprehensive}

## JSON Anti-patterns Quick Index {comprehensive}

## Quick Diagnosis Tables (2025-08) {important}

## Field Interaction Matrix (2025-08) {important}

## Migration Warnings Index (2025-08) {comprehensive}

## See Also {comprehensive}
- **Text Fields**: For text annotations with photos
- **Number Fields**: For GPS coordinate storage
- **Select Fields**: For media categorization
- **Reference Documents**:
  - [Validation Timing Reference](../reference-docs/validation-timing-reference.md)
  - [Data Export Reference](../reference-docs/data-export-reference.md) - Binary data handling
  - [Security Considerations](../reference-docs/security-considerations-reference.md) - Upload vulnerabilities
  - [Performance Thresholds](../reference-docs/performance-thresholds-reference.md) - Upload limits
  - [Accessibility Reference](../reference-docs/accessibility-reference.md) - Camera accessibility

## Error Message Quick Reference {important}
### Media-Specific Errors
[Focus on file upload, camera, permission errors]

## Metadata {comprehensive}
```

## EXTRACTION REQUIREMENTS

### From Source Documents, Extract:
1. All file type tables and MIME type lists
2. All platform-specific camera behaviors
3. All upload size limits and constraints
4. All storage path specifications
5. All offline sync strategies
6. All permission requirements
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
- Document length: ~2,000-2,500 lines (lighter than before)
- Complete media-specific examples
- Platform details for media features
- Specific measurements for media operations
- Links to all 9 reference documents where appropriate

## QUALITY CHECKLIST
- [ ] All fields are H3 under H2 "Individual Field Reference"
- [ ] Designer Usage Guide is at position #2
- [ ] Field Selection Guide is at position #3
- [ ] Links to reference docs use ../reference-docs/ path
- [ ] No duplication of reference content
- [ ] Media-specific content comprehensive
- [ ] Platform behaviors documented
- [ ] Security risks specific to file uploads covered
- [ ] Performance limits for media operations included