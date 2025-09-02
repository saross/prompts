# LLM-First Consolidation Prompt: Media Fields (v2 - Enhanced)

## Context
You are consolidating detailed field documentation into LLM-optimized documentation following the successful v05 pattern with enhanced content generation.

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

## REQUIRED DOCUMENT STRUCTURE (EXACT ORDER AND TAGS)

```markdown
# Media Capture Fields

## Overview {essential}
### DESIGNER QUICK GUIDE
### CRITICAL NAMING DISAMBIGUATION  
### Media Capture Fields (1-5)
### Component Status Summary

## ⚠️ CRITICAL SECURITY VULNERABILITIES {essential}
[Or CRITICAL MEDIA FIELD RISKS - storage, permissions, data loss]

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
[Full documentation for each media field]

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

## ENHANCED CONTENT GENERATION RULES

### 1. What These Fields Cannot Do - DETAILED EXPLANATIONS
For media fields, focus on:
- **Capture Limitations**: Resolution limits, format restrictions, duration caps
- **Storage Limitations**: IndexedDB quotas, offline limits, sync issues  
- **Processing Limitations**: No server-side processing, no automatic compression
- **Platform Limitations**: iOS vs Android vs Web differences

Example format:
```markdown
### Storage Limitations {important}
- **Server-side storage** - All media stored locally in IndexedDB only. No automatic cloud backup or server upload without explicit sync
- **Storage quotas** - Browser-dependent limits (typically 50% of free disk on Chrome, 1GB on Safari). No warning before quota exceeded
- **Cross-device access** - Media files not accessible from other devices until synced. Risk of data loss if device fails
```

### 2. Common Use Cases - MEDIA-SPECIFIC SCENARIOS
Structure for media fields:
```markdown
### Archaeological Documentation

**Site Photography**:
- **Overview shots** → TakePhoto with multiple captures enabled, 5MB limit per photo
- **Detail photography** → TakePhoto with annotation enabled via paired SketchForm
- **Video walkthroughs** → VideoRecorder with 30-second limit for storage efficiency
- **Voice notes** → AudioRecorder for quick observations, 2-minute maximum

**Evidence Chain**:
- **Photo verification** → TakePhoto with GPS metadata preserved
- **Sketch annotations** → SketchForm overlaid on photos for marking features
```

### 3. Field Selection Guide - MEDIA DECISION TREE
```markdown
### Quick Decision Tree
What type of media capture?
│
├─ Still images?
│  ├─ From camera? → TakePhoto
│  └─ From files? → FileUpload (accepts images)
│
├─ Audio recording?
│  └─ YES → AudioRecorder
│     ├─ <2 min → Optimal performance
│     └─ >2 min → Consider chunking
│
├─ Video recording?
│  └─ YES → VideoRecorder
│     └─ ⚠️ Check storage quota first
│
└─ Drawings/Annotations?
   └─ YES → SketchForm
      ├─ Over photos → Paired with TakePhoto
      └─ Standalone → Independent sketches
```

### 4. Storage Management Tables
Critical for media fields:
```markdown
### Storage Capacity by Platform
| Platform | IndexedDB Limit | Typical Free Space | Media Impact |
|----------|----------------|-------------------|--------------|
| Chrome Desktop | 50% of free disk | 10-100GB | ✅ Good |
| Safari iOS | 1GB total | 1GB | ⚠️ Limited |
| Chrome Android | 6% of free space | 2-6GB | ⚠️ Variable |

### File Size Recommendations
| Media Type | Optimal | Maximum | Compression | Quality Impact |
|------------|---------|---------|-------------|----------------|
| Photo | <2MB | 5MB | 80% JPEG | Minimal |
| Audio | <5MB | 10MB | 128kbps | Acceptable |
| Video | <20MB | 50MB | 720p H.264 | Noticeable |
```

### 5. Error Message Quick Reference - MEDIA-SPECIFIC
Categories for media errors:
```markdown
### Storage Errors
| Error Message | Field Type(s) | Root Cause | Quick Fix | Prevention |
|---------------|---------------|------------|-----------|------------|
| "QuotaExceededError" | All media | IndexedDB full | Clear old records | Monitor storage |
| "NotAllowedError" | TakePhoto, Audio, Video | Permission denied | Request permission | Check HTTPS |

### Capture Errors
| Error Message | Field Type(s) | Symptoms | Resolution |
|---------------|---------------|----------|------------|
| "No camera found" | TakePhoto | Black screen | Check device | Provide FileUpload fallback |
| "Microphone not available" | AudioRecorder | Silent recording | Check permissions | Test before deployment |
```

### 6. JSON Patterns Cookbook - MEDIA PATTERNS
Media-specific patterns:
```markdown
**Photo Documentation with Annotation**:
```json
{
  "site-photo": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "component-parameters": {
      "label": "Site Photography",
      "multiple": true,
      "maxFiles": 5
    }
  },
  "photo-annotation": {
    "component-namespace": "faims-custom",
    "component-name": "SketchForm",
    "component-parameters": {
      "label": "Mark features on photo"
    },
    "condition": {
      "field": "site-photo",
      "operator": "not-empty"
    }
  }
}
```

### 7. Platform-Specific Sections
Essential for media fields:
```markdown
### iOS-Specific Behaviors
- **Camera**: Requires user gesture to activate
- **Audio**: No background recording
- **Storage**: Hard 1GB IndexedDB limit
- **Export**: Photos save to camera roll

### Android-Specific Behaviors
- **Camera**: Multiple permission prompts
- **Audio**: Background recording possible
- **Storage**: Variable quota based on free space
- **Export**: Downloads folder access

### Web-Specific Requirements
- **HTTPS Required**: All media APIs need secure context
- **No Background**: Recording stops on tab switch
- **Storage**: Most generous quotas
- **Export**: Download prompts for each file
```

### 8. Quick Diagnosis Tables - MEDIA FOCUS
```markdown
### Platform Media Support
| Feature | iOS Safari | Android Chrome | Desktop Chrome | Firefox |
|---------|------------|---------------|----------------|---------|
| Camera Access | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Audio Record | ⚠️ Limited | ✅ Full | ✅ Full | ✅ Full |
| Video Record | ⚠️ Limited | ✅ Full | ✅ Full | ⚠️ Limited |
| Drawing | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| File Upload | ⚠️ Photos only | ✅ Full | ✅ Full | ✅ Full |
```

### 9. Performance Thresholds - MEDIA SPECIFIC
```markdown
## Performance Thresholds Table (2025-08) {essential}

| Field Type | Optimal | Acceptable | Degraded | Unusable | Limiting Factor |
|------------|---------|------------|----------|----------|-----------------|
| **TakePhoto** | 1-3 photos | 4-10 photos | 11-20 photos | >20 | Memory & storage |
| **FileUpload** | <10MB total | 10-50MB | 50-100MB | >100MB | Upload processing |
| **AudioRecorder** | <2 min | 2-5 min | 5-10 min | >10 min | File size & RAM |
| **VideoRecorder** | <30 sec | 30-60 sec | 1-2 min | >2 min | Storage quota |
| **SketchForm** | 1-3 drawings | 4-8 drawings | 9-15 | >15 | Canvas memory |

### Storage Impact
| Total Media | Storage Used | Sync Time | Export Time | Risk Level |
|-------------|--------------|-----------|-------------|------------|
| <100MB | 2% typical | <1 min | <30 sec | 🟢 Low |
| 100-500MB | 10% typical | 1-5 min | 1-3 min | 🟡 Medium |
| 500MB-1GB | 20% typical | 5-15 min | 3-10 min | 🔴 High |
| >1GB | Quota risk | >15 min | >10 min | 🔴 Critical |
```

## MEDIA-SPECIFIC REQUIREMENTS

### Storage Documentation
- Always document IndexedDB limits
- Include quota monitoring guidance
- Provide cleanup procedures
- Document export methods

### Permission Requirements
- List all permissions per platform
- Include permission request timing
- Document fallback options
- Provide testing procedures

### Offline Behavior
- Document what works offline
- Explain sync requirements
- Detail data persistence
- Include recovery procedures

### Quality Settings
- Default quality/compression
- How to adjust settings
- Impact on file size
- Platform differences

## Target Metrics
- Total document: 2,500-3,500 lines
- Storage documentation: 200+ lines
- Platform specifics: 300+ lines
- Media patterns: 20+ examples
- Troubleshooting: 200+ lines
- Performance tables: 5+ tables

## Output Format
Single markdown file: `media-fields-v05.md` with all enhanced sections automatically generated.