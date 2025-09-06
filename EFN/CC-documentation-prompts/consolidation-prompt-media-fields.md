# LLM-First Consolidation Prompt: Media Fields

## Context
You are consolidating detailed field documentation into LLM-optimized documentation following the successful v05 pattern established for text, datetime, number, and selection fields.

## Input Documents
1. take-photo.md - TakePhoto field documentation
2. file-upload.md - FileUpload field documentation
3. audio-recorder.md - AudioRecorder field documentation  
4. video-recorder.md - VideoRecorder field documentation
5. sketch-form.md - SketchForm field documentation

## Designer UI to Component Mapping (CRITICAL)
| Designer Label | JSON Component | Namespace | Documentation File |
|---|---|---|---|
| Take Photo | TakePhoto | faims-custom | take-photo.md |
| File Upload | FileUpload | faims-custom | file-upload.md |
| Audio Recorder | AudioRecorder | faims-custom | audio-recorder.md |
| Video Recorder | VideoRecorder | faims-custom | video-recorder.md |
| Drawing Pad | SketchForm | faims-custom | sketch-form.md |

## Target Document: media-fields-v05.md

## REQUIRED DOCUMENT STRUCTURE (EXACT ORDER AND TAGS)

```markdown
# Media Capture Fields

## Overview {essential}
### DESIGNER QUICK GUIDE
### CRITICAL NAMING DISAMBIGUATION  
### Media Capture Fields (1-5)
### Component Status Summary

## ⚠️ CRITICAL MEDIA FIELD RISKS {essential}
[Storage limitations, platform restrictions, security concerns]

## What These Fields Cannot Do {important}
### Capture Limitations {important}
### Storage Limitations {important}
### Processing Limitations {important}
### Platform Limitations {important}

## Common Use Cases {important}
### Archaeological Documentation
### Scientific Data Collection
### Field Research Documentation
### Quality Assurance and Verification

## Field Selection Guide {essential}
### Quick Decision Tree
### Quick Decision Matrix
### Selection Strategy
### Platform Considerations

## Designer Usage Guide {essential}
### What to Select in Designer
### When JSON Enhancement is Required
### Quick Use Case Examples

## Designer Capabilities vs JSON Enhancement {essential}
### What Designer CAN Configure
### What Requires JSON Editing
### Designer vs JSON Workflow

## Designer Component Mapping {essential}
### Designer UI vs JSON Component Names
### Designer Limitations Requiring JSON

## Component Selection Decision Tree {important}
### Which Component Should You Use?

## Component Namespace Errors {important}
### Troubleshooting "Component not found" Errors
### Common Namespace Confusion Points

## Common Characteristics {important}
### Storage and Persistence {important}
### File Size Limitations {important}
### Platform-Specific Behaviors {important}
### Offline Capabilities {important}
### Export and Data Recovery {important}

## Individual Field Reference {essential}

### TakePhoto {essential}
#### Purpose {essential}
#### Key Features {essential}
#### Configuration Parameters {important}
#### Platform-Specific Behavior {important}
#### Storage and File Management {important}
#### Field-Specific Troubleshooting {important}
#### JSON Anti-patterns
#### Spec Mapping
#### Implementation Examples {comprehensive}

### FileUpload {essential}
[Same subsection structure as TakePhoto]

### AudioRecorder {essential}
[Same subsection structure as TakePhoto]

### VideoRecorder {essential}
[Same subsection structure as TakePhoto]

### SketchForm {essential}
[Same subsection structure as TakePhoto]

## Troubleshooting Guide {important}
### Storage Issues {important}
### Platform-Specific Problems {important}
### Performance Issues {important}
### Debug Checklists {comprehensive}

## JSON Examples {comprehensive}
### Basic Media Capture Patterns
### Multi-Media Documentation Patterns
### Platform-Specific Configurations
### Storage Optimization Patterns

## Migration and Best Practices {comprehensive}
### Migration Decision Tree
### Storage Management Best Practices
### Platform-Specific Guidelines
### Training Requirements

## Field Quirks Index (2025-08) {comprehensive}
### TakePhoto
### FileUpload
### AudioRecorder
### VideoRecorder
### SketchForm

## Performance Thresholds Table (2025-08) {essential}
[File sizes, capture limits, storage boundaries]

## JSON Patterns Cookbook (2025-08) {comprehensive}
### Photo Documentation Patterns
### Audio Recording Patterns
### Video Capture Patterns
### File Management Patterns
### Sketch Annotation Patterns

## JSON Anti-patterns Quick Index {comprehensive}
### Media Field Anti-patterns

## Quick Diagnosis Tables (2025-08) {important}
### Storage Capacity Issues
### Platform Compatibility
### File Format Support
### Capture Quality Settings

## Field Interaction Matrix (2025-08) {important}
[Media field combinations and conflicts]

## Migration Warnings Index (2025-08) {comprehensive}
### Data Migration Risks
### Storage Migration Considerations
### Platform Change Impacts

## Error Message Quick Reference (2025-08) {important}
### Storage Errors
### Permission Errors
### Platform-Specific Errors
### Capture Failures

## Metadata {comprehensive}
```

## Critical Processing Rules

### 1. SECTION ORDER IS MANDATORY
- Follow the exact section order above
- All H2 sections must have tags {essential}, {important}, or {comprehensive}
- H3 sections under Individual Field Reference do not need tags
- Maintain exact heading levels (H1, H2, H3, H4)

### 2. ZERO CONTENT LOSS - CRITICAL REQUIREMENT
- Preserve EVERY technical detail from source documents
- Include ALL platform-specific behaviors
- Keep ALL JSON examples
- Include ALL file size limits and storage constraints
- Maintain ALL troubleshooting items
- Include ALL platform compatibility notes

### 3. Component Documentation Requirements
All five media components must be fully documented:
- TakePhoto (camera capture for images)
- FileUpload (general file attachments)
- AudioRecorder (audio recording and playback)
- VideoRecorder (video capture and playback)
- SketchForm (drawing/annotation canvas)

### 4. Storage and Persistence Focus
- Document IndexedDB storage limits
- Include offline behavior
- Export/backup procedures
- Data recovery options
- File format specifications

### 5. Platform-Specific Documentation
CRITICAL: Document platform differences:
- iOS vs Android vs Web capabilities
- Permission requirements per platform
- File size limits per platform
- Format support per platform
- Hardware requirements

### 6. Designer Disambiguation
- "Take Photo" vs camera access in FileUpload
- "Drawing Pad" creates SketchForm component
- Audio/Video recorder platform availability

### 7. Critical Limitations to Highlight
- 5MB default file size limits
- IndexedDB quota issues
- No server-side storage
- Platform-specific codec support
- Offline data persistence risks

### 8. Tagging Requirements
- {essential} - Core functionality, storage limits
- {important} - Platform differences, common issues
- {comprehensive} - Edge cases, recovery procedures

## Known Issues to Document

1. **Storage Quota Exceeded** - IndexedDB limits on different browsers
2. **iOS Audio Recording** - Requires user interaction to start
3. **Web Camera Access** - HTTPS requirement, permission prompts
4. **Large File Handling** - Performance degradation with video
5. **Offline Data Loss** - Risk of data loss without sync
6. **Cross-Platform Format** - Codec compatibility issues

## Media-Specific Sections to Emphasize

1. **File Size Limits** - Critical for field deployment
2. **Storage Management** - Quota monitoring and cleanup
3. **Export Procedures** - Data recovery and backup
4. **Permission Requirements** - Platform-specific permissions
5. **Offline Behavior** - Data persistence without network
6. **Quality Settings** - Compression and resolution options

## Content Preservation Checklist
- [ ] ALL sections in exact order from template
- [ ] ALL H2 sections have tags
- [ ] ALL 5 media field types documented
- [ ] Storage limits clearly documented
- [ ] Platform differences highlighted
- [ ] Permission requirements listed
- [ ] File format support specified
- [ ] Offline behavior documented
- [ ] Export/recovery procedures included
- [ ] Performance thresholds defined
- [ ] Target 2500-3500 lines

## Output Format
Single markdown file: `media-fields-v05.md` following the exact structure above, with all sections in the specified order.