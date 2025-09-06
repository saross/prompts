# LLM-First Consolidation Prompt: Media Fields (v3.1 - Comprehensive)

## Core Directive
Extract and consolidate ALL technical content from source documents into a comprehensive, enhanced reference following the v05 pattern. Focus on COMPLETE knowledge transfer - no content should be lost. Media fields have unique storage, permission, and platform considerations that must be thoroughly documented.

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

## ⚠️ CRITICAL SECURITY VULNERABILITIES {essential}
[Or CRITICAL MEDIA FIELD RISKS - storage quota, data loss, permissions]

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
### Compliance and Evidence Recording

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
### Designer Limitations {important}

## Designer Component Mapping {essential}
### Designer UI vs JSON Component Names
### Designer Limitations Requiring JSON
### Technical Implementation Note

## Component Selection Decision Tree {important}
### Which Component Should You Use?
### Manual JSON Configuration

## Component Namespace Errors {important}
### Troubleshooting "Component not found" Errors
### Common Namespace Confusion Points

## Common Characteristics {important}
### Storage and Persistence {important}
#### IndexedDB Storage {important}
#### Quota Management {important}
#### Offline Persistence {important}
### File Size Limitations {important}
#### Platform-Specific Limits {important}
#### Compression and Quality {important}
### Permission Requirements {important}
#### Camera Permissions {important}
#### Microphone Permissions {important}
#### Storage Permissions {important}
### Platform-Specific Behaviors {important}
#### Cross-Platform Consistency {important}
#### iOS Behaviors {comprehensive}
#### Android Behaviors {comprehensive}
#### Web/Desktop Behaviors {important}
### Export and Data Recovery {important}
#### Export Methods {important}
#### Backup Procedures {important}
#### Data Recovery {comprehensive}
### Security Considerations {important}
#### HTTPS Requirements {important}
#### Cross-Origin Restrictions {important}
#### Data Privacy {comprehensive}
### Performance Boundaries {important}
#### Memory Limitations {important}
#### Processing Constraints {important}
### Accessibility Compliance {important}
### Testing Guidelines {comprehensive}

## Individual Field Reference {essential}

### TakePhoto {essential}
<!-- keywords: photo, camera, image, capture, picture -->
**Designer Label**: Take Photo
**Component Name**: TakePhoto
**Namespace**: faims-custom
**Type Returned**: faims-core::Array (of image objects)

#### Purpose {essential}
[Extract from take-photo.md]

#### Key Features {essential}
[Extract from take-photo.md]

#### Core Configuration {essential}
```json
[Complete JSON example from source]
```

#### Configuration Parameters {important}
[Extract complete parameter documentation]

#### TakePhoto-Specific Capture {important}
[Camera access, capture workflow, image processing]

#### Platform-Specific Behavior {important}
[iOS, Android, Web differences for camera]

#### Storage and File Management {important}
[IndexedDB storage, file naming, cleanup]

#### TakePhoto-Specific Issues {important}
[All known issues and limitations]

#### Field-Specific Troubleshooting {important}
[Troubleshooting table from source]

#### JSON Anti-patterns
[All anti-patterns from source]

#### Common Spec Mappings
[Designer to JSON mappings]

#### Implementation Examples {comprehensive}
[ALL examples from source - Site Photography, Evidence Chain, etc.]

### FileUpload {essential}
<!-- keywords: file, upload, attachment, document -->
[Same detailed structure as TakePhoto]

### AudioRecorder {essential}
<!-- keywords: audio, recording, voice, sound -->
[Same detailed structure]

### VideoRecorder {essential}
<!-- keywords: video, recording, movie, capture -->
[Same detailed structure]

### SketchForm {essential}
<!-- keywords: drawing, sketch, annotation, canvas -->
[Same detailed structure]

## Troubleshooting Guide {important}
### Storage Issues {important}
#### Quota Exceeded Errors {important}
#### IndexedDB Failures {important}
#### Cleanup Procedures {important}
### Permission Issues {important}
#### Camera Access Denied {important}
#### Microphone Access Denied {important}
#### HTTPS Requirements {important}
### Platform-Specific Problems {important}
#### iOS Limitations {important}
#### Android Issues {important}
#### Browser Compatibility {important}
### Performance Issues {important}
#### Memory Exhaustion {important}
#### Large File Handling {important}
### Error Message Reference {important}
### Quick Reference Matrix {important}
### Debug Checklists {comprehensive}
#### General Media Field Checklist {comprehensive}
#### Field-Specific Checks {comprehensive}

## JSON Examples {comprehensive}
### TakePhoto Examples {important}
#### [Named examples from source]
### FileUpload Examples {important}
#### [Named examples from source]
### AudioRecorder Examples {important}
#### [Named examples from source]
### VideoRecorder Examples {important}
#### [Named examples from source]
### SketchForm Examples {important}
#### [Named examples from source]

## Migration and Best Practices {comprehensive}
### Storage Management Best Practices
#### Quota Monitoring
#### Cleanup Strategies
#### Backup Procedures
### Platform-Specific Guidelines
#### iOS Deployment
#### Android Deployment
#### Web Deployment
### Migration Decision Tree {comprehensive}
### Migration Warnings Index
#### Storage Migration Risks
#### Platform Change Impacts
### Training Requirements {important}
#### Basic Training (All Users)
#### Advanced Training (Data Managers)
### Implementation Notes {comprehensive}
### Cross-References Between Fields {comprehensive}
### External Documentation {comprehensive}

## Field Quirks Index (2025-08) {comprehensive}
### TakePhoto
[All quirks with QUIRK, FIX, RULE, VERSION tags]
### FileUpload
### AudioRecorder
### VideoRecorder
### SketchForm

## Performance Thresholds Table (2025-08) {essential}
### Storage Thresholds
[IndexedDB limits, file counts, total size]
### Capture Thresholds
[Resolution, duration, quality settings]
### Platform-Specific Thresholds
[iOS, Android, Web differences]

## JSON Patterns Cookbook (2025-08) {comprehensive}
### Photo Documentation Patterns
### Audio Recording Patterns
### Video Capture Patterns
### File Management Patterns
### Sketch Annotation Patterns
### Multi-Media Workflows

## JSON Anti-patterns Quick Index {comprehensive}
### Media Field Anti-patterns
[Storage, permissions, quality settings]

## Quick Diagnosis Tables (2025-08) {important}
### Storage Capacity by Platform
### File Format Support
### Capture Quality Matrix
### Permission Requirements
### Platform Feature Support

## Field Interaction Matrix (2025-08) {important}
[Media field combinations, conflicts, dependencies]

## Migration Warnings Index (2025-08) {comprehensive}
### Data Migration Risks
### Storage Migration Considerations
### Platform Change Impacts
### Format Compatibility Issues

## Error Message Quick Reference (2025-08) {important}
### Storage Errors
### Permission Errors
### Capture Errors
### Platform-Specific Errors
### Silent Failures

## Metadata {comprehensive}
### Component Status Summary
### Platform Support Matrix
### Quality Verification
### Documentation Version
### Revision History
```

## COMPREHENSIVE EXTRACTION REQUIREMENTS

### 1. ZERO CONTENT LOSS - ABSOLUTE REQUIREMENT
From each source document, extract:
- **EVERY** storage limit and quota detail
- **EVERY** permission requirement per platform
- **EVERY** file format specification
- **EVERY** quality setting and compression option
- **EVERY** platform-specific behavior
- **EVERY** offline capability and limitation
- **EVERY** data recovery procedure
- **EVERY** performance threshold
- **EVERY** error condition and message
- **EVERY** implementation example

### 2. MEDIA-SPECIFIC ENHANCEMENTS

#### For Storage Documentation
```markdown
### Storage and Persistence {important}
#### IndexedDB Storage {important}
- **Quota calculation** - Browser allocates typically 50% of free disk space on Chrome, but Safari iOS hard-limits to 1GB total. This quota is shared across all browser storage including localStorage and cache.
- **Persistence modes** - Default storage can be evicted under pressure. Use navigator.storage.persist() for critical data, though iOS ignores this request.
- **File storage format** - Media stored as Blob objects with metadata in separate IndexedDB object stores. Each media file consumes roughly 1.3x its size due to encoding overhead.
[Continue with complete details]
```

#### For Permission Requirements
```markdown
### Permission Requirements {important}
#### Camera Permissions {important}
Platform-specific requirements:
- **iOS Safari**: Requires user gesture to initiate. Shows system prompt "example.com Would Like to Access the Camera". Cannot be pre-requested or cached.
- **Android Chrome**: Two-tier permission - first browser prompt, then system dialog. Permission persists per origin but resets on HTTP (not HTTPS).
- **Desktop browsers**: Single prompt per origin, persists indefinitely unless manually revoked. Some browsers show indicator when camera active.
[Include permission flow diagrams]
```

#### For Platform Behaviors
```markdown
### iOS-Specific Behaviors
#### Camera Capture
- **Gesture requirement**: Must be triggered by user tap, not programmable
- **Full-screen takeover**: Camera UI covers entire screen, no customization
- **Photo Library access**: Can select from library or capture new
- **HEIC conversion**: Automatically converts HEIC to JPEG for web compatibility
- **Memory pressure**: Aggressive memory management may clear large images

#### Storage Limitations
- **1GB hard limit**: Total for all web storage including cache
- **No persistence API**: Cannot request persistent storage
- **Safari Private Mode**: No storage at all, operations fail silently
[Continue with all iOS-specific details]
```

#### For Error Documentation
```markdown
### Storage Errors
| Error Message | Field Type(s) | Condition | User Impact | Recovery | Prevention |
|---------------|---------------|-----------|-------------|----------|------------|
| "QuotaExceededError" | All media | IndexedDB full | Cannot save | Clear old data | Monitor usage |
| "NotAllowedError" | TakePhoto, AudioRecorder | No permission | Cannot capture | Re-request | Check HTTPS |
| "AbortError" | VideoRecorder | User cancelled | No video | Retry | Normal behavior |
[Include ALL errors from source documents]
```

#### For Performance Thresholds
```markdown
## Performance Thresholds Table (2025-08) {essential}

### Storage Impact by Media Type
| Media Type | Single Item | Typical Size | 10 Items | 100 Items | Quota Impact |
|------------|-------------|--------------|----------|-----------|--------------|
| Photo (2MP) | 500KB-1MB | 750KB | 7.5MB | 75MB | Low |
| Photo (8MP) | 2-4MB | 3MB | 30MB | 300MB | Medium |
| Audio (1min) | 500KB-1MB | 750KB | 7.5MB | 75MB | Low |
| Video (30sec) | 5-15MB | 10MB | 100MB | 1GB | High |
| Sketch | 50-200KB | 100KB | 1MB | 10MB | Minimal |

### Platform-Specific Limits
| Platform | Storage Quota | Practical Limit | Media Count | Risk Level |
|----------|---------------|-----------------|-------------|------------|
| iOS Safari | 1GB total | 500MB media | ~50 photos | 🔴 High |
| Android Chrome | 6% free space | 2-6GB | ~500 photos | 🟡 Medium |
| Desktop Chrome | 50% free disk | 10-100GB | ~5000 photos | 🟢 Low |
```

### 3. MEDIA-SPECIFIC SECTIONS

#### Storage Management
Document thoroughly:
- IndexedDB quota monitoring techniques
- Storage.estimate() API usage
- Cleanup strategies for old media
- Compression settings impact
- Export before cleanup workflows
- Recovery from quota errors

#### Permission Flows
Include complete flows:
- Initial permission request timing
- Re-request after denial patterns
- Platform-specific prompt text
- Permission persistence rules
- HTTPS requirements
- Fallback strategies

#### Quality Settings
Detail all options:
- Image resolution options
- JPEG quality percentages
- Audio bitrate settings
- Video resolution/framerate
- Canvas resolution for sketches
- Size vs quality tradeoffs

#### Offline Behavior
Comprehensive coverage:
- What works offline (capture, storage)
- What requires network (sync, export)
- Data persistence guarantees
- Cache behavior
- Service worker interactions

### 4. SPECIAL HANDLING

#### Platform Divergence
When platforms differ significantly:
```markdown
#### [Feature Name]
**iOS**: [Specific iOS behavior]
**Android**: [Specific Android behavior]
**Web**: [Desktop browser behavior]
**Critical differences**: [What developers must know]
```

#### Storage Warnings
Include prominent boxes:
```markdown
⚠️ **STORAGE WARNING**
iOS Safari limits ALL web storage to 1GB total. With 50% overhead for encoding and metadata, practical limit is ~500MB of media. Plan accordingly for iOS deployment.
```

#### Permission Failures
Document fallbacks:
```markdown
📝 **Permission Denied Fallback**
If camera permission denied:
1. Show FileUpload as alternative
2. Explain how to reset permissions
3. Provide Settings > Safari > Camera path
4. Consider progressive enhancement
```

### 5. QUALITY CHECKS

Ensure the output includes:
- [ ] ALL storage limits and quotas per platform
- [ ] ALL permission requirements and flows
- [ ] ALL file format specifications
- [ ] ALL quality/compression settings
- [ ] ALL offline behaviors documented
- [ ] ALL platform-specific differences
- [ ] ALL error messages and recovery procedures
- [ ] ALL performance thresholds
- [ ] Complete data recovery procedures
- [ ] Export/backup workflows

### 6. DO NOT

- Do NOT set target line counts
- Do NOT omit platform-specific details
- Do NOT skip storage calculations
- Do NOT simplify permission flows
- Do NOT combine similar errors
- Do NOT remove redundant warnings

## OUTPUT

Single markdown file: `media-fields-v05.md` with COMPLETE extraction of all source content plus media-specific enhancements per patterns above.