# TakePhoto Field – Third Draft Documentation

## Overview

The TakePhoto field represents Fieldmark's primary photographic documentation mechanism, integrating platform-native camera functionality with gallery selection through a unified interface paradigm. This field type leverages Capacitor's camera plugin to provide cross-platform image capture whilst maintaining platform-specific optimisations – native applications invoke system camera interfaces with full hardware access, whilst web deployments utilise available MediaDevices APIs or fallback to file selection. The implementation's 555 lines of code orchestrate permission management, image processing, and storage coordination, ultimately producing `faims-attachment::Files` data structures compatible with Fieldmark's broader attachment architecture. Unlike the format-agnostic FileUploader, TakePhoto optimises specifically for photographic workflows, providing immediate capture capabilities essential to field documentation whilst acknowledging that device photography serves primarily referential rather than forensic purposes in archaeological contexts.

## Common Use Cases

Deploy TakePhoto when requiring:
- **Site condition documentation** – Capturing environmental context, excavation progress, or stratigraphic profiles using device cameras
- **Specimen photography** – Recording artefacts, samples, or features with immediate visual documentation
- **Progress monitoring** – Sequential photography documenting excavation stages, conservation processes, or site changes
- **Contextual reference imagery** – Quick photographic notes supplementing detailed technical photography
- **Multi-angle documentation** – Capturing objects from various perspectives within a single field instance
- **Annotation-linked photography** – Images requiring descriptive metadata through integrated annotation fields

Avoid TakePhoto when:
- **Technical photography standards apply** – Professional documentation requiring preserved EXIF metadata, RAW formats, or specific camera settings
- **Non-image files required** – Documents, videos, or audio files necessitate FileUploader instead
- **Storage constraints exist** – Limited device storage or bandwidth preclude multiple high-resolution images
- **Validation enforcement critical** – Current implementation cannot enforce required photos or count limits
- **Large image collections expected** – Performance degradation beyond 20 images makes bulk photography impractical

## Core Configuration

### Required Configuration
```json
{
  "component-namespace": "faims-custom",
  "component-name": "TakePhoto",
  "type-returned": "faims-attachment::Files"
}
```

### Optional Parameters
```json
{
  "component-parameters": {
    "label": "Site Photography",           // Field label display
    "name": "site-photos",                 // Internal field identifier
    "helperText": "Capture site context",  // Guidance text below field
    "advancedHelperText": "",              // Extended help information
    "required": false                      // Visual indicator only (see Validation Rules)
  },
  "validationSchema": [                    // Default allows null/empty
    ["yup.array"],
    ["yup.of", [["yup.object"], ["yup.nullable"]]],
    ["yup.nullable"]
  ],
  "initialValue": null,                    // Always null, not empty array
  "meta": {
    "annotation": {
      "include": true,
      "label": "Photo description"
    },
    "uncertainty": {
      "include": false,
      "label": "Image quality"
    }
  }
}
```

**Critical constraint**: Parameters `maximum_file_size`, `minimum_file_size`, and `maximum_number_of_files` are **not supported** despite FileUploader compatibility. These parameters, if included, are silently ignored.

## Validation Rules

### Current Validation Limitations

| Rule | Configuration | Actual Behaviour | Workaround |
|------|---------------|------------------|------------|
| Required field | `"required": true` | Displays asterisk only, allows empty submission | Add `["yup.required", "At least one photo required"]` to validationSchema via JSON |
| Minimum photos | Not exposed in Designer | Not enforced | Add `["yup.min", 1, "Minimum 1 photo"]` manually |
| Maximum photos | Not supported | Unlimited photos allowed | Add `["yup.max", 10, "Maximum 10 photos"]` manually |
| File size limits | Not supported | No size validation | Cannot enforce – architectural limitation |
| Image validity | Not implemented | Corrupt images accepted | No validation available |

### Functional Validation Example
```json
"validationSchema": [
  ["yup.array"],
  ["yup.of", [["yup.object"], ["yup.nullable"]]],
  ["yup.required", "At least one photo required"],
  ["yup.min", 1, "Minimum one photo required"],
  ["yup.max", 20, "Maximum 20 photos to prevent performance issues"]
]
```
**Note**: This configuration requires manual JSON editing; Designer cannot configure validation beyond default schema.

### Validation Cascade Behaviour
- Field validates on blur and form submission
- Validation errors display below field
- Generic error messages without specific image identification
- No corruption or format validation performed

## Display Behaviour

### Desktop Rendering
- **Input presentation**: Button labelled "Take Photo" or "Add Photos"
- **Width behaviour**: Respects container width, not affected by `fullWidth` parameter
- **Image display**: Thumbnails in horizontal scrollable container
- **Interaction method**: Click to trigger camera/file selector modal
- **Webcam support**: Fully functional with desktop webcams via MediaDevices API

### Mobile Rendering

#### iOS Behaviour
- **System prompt**: "Take Photo or Choose from Library" native dialogue
- **Camera interface**: Full iOS camera with standard controls
- **Format handling**: HEIC/HEIF automatically converted to JPEG (quality: 90)
- **Permissions**: Single request for camera and photos together
- **Metadata loss**: ProRAW, Live Photos, Portrait depth data not preserved

#### Android Behaviour
- **System prompt**: Standard Android camera/gallery selector
- **Camera interface**: Device-specific camera application
- **Format handling**: Direct JPEG capture at 90% quality
- **Permissions**: Combined camera/storage permission request
- **Manufacturer consistency**: Behaviour uniform across Samsung, Pixel, others

### Web Platform Behaviour
- **Mobile browsers**: Chrome, Safari (iOS 14.3+), Firefox, Edge all support camera access
- **File selection**: Standard file input with image type filtering
- **EXIF handling**: All metadata stripped during capture
- **Storage format**: Base64 encoding increases memory footprint
- **PWA support**: Functions identically to browser deployment

## Interaction Patterns

### Image Capture Flow
1. User taps "Take Photo" button
2. Platform-specific selector appears (camera/gallery options)
3. Image captured or selected
4. Automatic orientation correction applied
5. GPS coordinates injected (native platforms only, if permitted)
6. Image added to field array
7. Thumbnail generated for display

### Image Management
- **Preview**: Tap thumbnail for full-screen view via FaimsAttachmentManagerDialog
- **Deletion**: Individual image removal through preview interface
- **Reordering**: Not supported – images remain in capture sequence
- **Re-capture**: Not available – must delete and retake

### Permission Handling
- **Initial request**: Triggered on first capture attempt
- **Denial recovery**: No in-app recovery; users must navigate to system settings
- **Error display**: Platform-specific instructions (incorrectly shows LocationPermissionIssue component – known bug)
- **Partial permissions**: Camera denial still allows gallery selection

## Conditional Logic Support

### Field Visibility Conditions
Standard conditional logic applies:
```json
"condition": {
  "operator": "equal",
  "field": "documentation-needed",
  "value": "yes"
}
```

### Performance Considerations
- Conditional evaluation unaffected by image count
- Field hiding preserves captured images
- Re-showing field restores previous images
- Multiple conditional TakePhoto fields compound performance issues

### Interaction with Other Fields
- Can reference other field values in conditions
- Cannot conditionally adjust validation based on other fields
- Image count cannot trigger conditions in other fields

## Data Storage and Export

### Storage Architecture
```javascript
// Native platforms: URI reference
resultType: CameraResultType.Uri
// Web platform: Base64 string
resultType: CameraResultType.Base64

// Both converted to Blob for storage
file_data_to_attachments(avp)  // Shared with FileUploader
```

### Synchronisation Behaviour
- **Upload**: Automatic to server when online
- **Download**: Controlled by "Get attachments from other devices" toggle
- **Offline capture**: Fully functional with automatic queue for sync
- **Storage location**: PouchDB (IndexedDB) for offline persistence

### Export Format
```json
{
  "field-name": {
    "faims_attachments": [
      {
        "attachment_id": "att-uuid-12345",
        "filename": "IMG_20240315_142350.jpg",
        "file_type": "image/jpeg"
      }
    ]
  }
}
```
Images exported as separate files with systematic renaming: `recordID_fieldname_index.jpg`

### Data Integrity
- Missing images silently skipped during export
- No notification of failed image exports
- Original filenames preserved until export
- No EXIF metadata in export package

## Common Patterns

### Example 1: Basic Site Photography
```json
{
  "site-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Site Photography",
      "name": "site-photos",
      "helperText": "Capture site overview and detail shots"
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.of", [["yup.object"], ["yup.nullable"]]],
      ["yup.nullable"]
    ],
    "initialValue": null
  }
}
```
**Behaviour**: Unlimited photos, no validation, optional field. Suitable for supplementary documentation.

### Example 2: Required Documentation with Limits
```json
{
  "artefact-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Artefact Documentation",
      "name": "artefact-photos",
      "helperText": "Minimum 2 angles, maximum 10 photos",
      "required": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.of", [["yup.object"], ["yup.nullable"]]],
      ["yup.required", "Artefact photos required"],
      ["yup.min", 2, "Capture at least 2 angles"],
      ["yup.max", 10, "Maximum 10 photos allowed"]
    ],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "angle and lighting notes"
      }
    }
  }
}
```
**Behaviour**: Enforces 2–10 photos through validation. Annotation captures photographic context. Requires manual JSON configuration.

### Example 3: Conditional Photography with Quality Flags
```json
{
  "damage-documentation": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Damage Documentation",
      "name": "damage-photos",
      "helperText": "Photograph any visible damage"
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.of", [["yup.object"], ["yup.nullable"]]],
      ["yup.nullable"]
    ],
    "initialValue": null,
    "condition": {
      "operator": "equal",
      "field": "damage-present",
      "value": "yes"
    },
    "meta": {
      "annotation": {
        "include": true,
        "label": "damage description"
      },
      "uncertainty": {
        "include": true,
        "label": "image clarity"
      }
    }
  }
}
```
**Behaviour**: Field appears only when damage indicated. Both annotation and uncertainty metadata enabled. Suitable for conditional documentation workflows.

## Troubleshooting Guide

### Common Issues and Solutions

| Issue | Symptoms | Solution | Platform |
|-------|----------|----------|----------|
| Camera permission denied | Error message about permissions | Navigate to Settings > Apps > [App] > Permissions | iOS/Android |
| Required validation not working | Empty field allows submission | Manually add yup.required to validationSchema | All |
| Performance degradation | Form sluggish with many photos | Limit to 20 photos maximum | All |
| Images not syncing | Photos visible locally but not on other devices | Check "Get attachments" toggle in settings | All |
| EXIF data missing | No GPS or camera settings in photos | Expected behaviour – use external camera for technical photos | Web/All |
| Storage full error | Silent failure when adding photos | Clear app cache or delete unnecessary records | All |

### Debug Checklist
1. ✓ Verify camera permissions in system settings
2. ✓ Check available device storage (>100MB recommended)
3. ✓ Confirm network connectivity for sync
4. ✓ Validate JSON syntax if manually edited
5. ✓ Test with fewer images if performance issues
6. ✓ Verify "Get attachments" setting for team collaboration
7. ✓ Check browser console for IndexedDB quota errors
8. ✓ Confirm image files not corrupted

### Platform-Specific Gotchas
- **iOS**: Settings navigation differs by iOS version
- **Android**: Some devices require storage permission separately
- **Web**: Cannot recover permissions without page reload
- **Safari**: Lower storage quota (~1GB) than Chrome (~6GB)

## Implementation Notes

### GPS Coordinate Injection
Native platforms only:
```javascript
await Exif.setCoordinates({
  pathToImage: photoResult.path,
  lat: latitude,
  lng: longitude
});
```
Web platform cannot access or preserve GPS data.

### Image Processing Pipeline
1. Capture via Camera.getPhoto() with quality: 90
2. Orientation correction via correctOrientation: true
3. Format conversion (HEIC→JPEG on iOS)
4. GPS injection (native only)
5. Blob creation for storage
6. PouchDB attachment storage

### EXIF Metadata Limitations
| Metadata | Native | Web | Preserved |
|----------|--------|-----|-----------|
| GPS coordinates | Added if permitted | ✗ | Latitude/Longitude only |
| Timestamp | ✓ | ✗ | Basic datetime |
| Camera settings | ✗ | ✗ | Lost |
| Device info | Partial | ✗ | Limited |
| Orientation | ✓ | ✓ | Via correction |

### Offline Capabilities
- Full offline capture functionality
- Images stored in IndexedDB via PouchDB
- Automatic synchronisation when connection restored
- No storage space checking (fails silently when full)

### Memory Management
Current implementation concatenates all images in memory:
```javascript
const newImages = props.field.value.concat(blob);
```
No lazy loading, thumbnail generation, or pagination implemented. Performance degradation begins around 10 images, severe beyond 20.

## Best Practices

### Image Quantity Management
- **Optimal**: 1–5 images for rapid documentation
- **Acceptable**: 6–15 images for comprehensive recording
- **Maximum**: 20 images before performance impact
- **Avoid**: >20 images in single field (use multiple records)

### Metadata Expectations
- Device photography provides referential documentation only
- GPS coordinates valuable for spatial context (native platforms)
- Technical photography requiring EXIF preservation should use professional cameras with FileUploader
- Document camera settings manually in annotation fields if required

### Offline Workflow Guidance
1. Enable location services before offline work for GPS caching
2. Monitor available storage space proactively
3. Sync regularly when connection available
4. Test offline capture before remote deployment
5. Consider storage implications of image accumulation

### Platform Selection
- **iOS/Android apps**: Preferred for GPS tagging and offline reliability
- **Web browser**: Suitable when GPS not required or desktop webcam needed
- **PWA**: Acceptable alternative with same limitations as web

### Team Collaboration
- Coordinate "Get attachments" settings across team
- Establish naming conventions for image annotations
- Plan for bandwidth when enabling attachment download
- Consider image quantity impact on sync times

## See Also

- **FileUploader**: For document uploads, professional camera images, or files requiring specific metadata preservation
- **TakePoint**: For precise GPS coordinate capture without photography
- **TextField/MultilineTextField**: For detailed photographic descriptions when images not required
- **Annotation fields**: For capturing photographic context, technical notes, or image descriptions
- **TemplatedStringField**: For generating systematic photo identifiers

### Architectural Note
TakePhoto and FileUploader are independent implementations sharing only backend storage infrastructure (`faims-attachment::Files`). They are not variants of a single component but distinct field types optimised for different workflows. Configuration parameters and validation approaches differ substantially between these fields.

---

*Documentation version: Third Draft  
Technical basis: Component version as of January 2025  
Performance recommendations based on production deployment observations*