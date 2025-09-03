# Media Fields - Reference Document Update Checklist
## Content to Add to Existing Reference Documents
Date: 2025-09-03

This checklist identifies media-specific content that should be ADDED to existing reference documents after creating media-fields-v05.md.

---

## 1. accessibility-reference.md

### ADD to Touch Target Standards section:
- [ ] **Camera capture button**: Minimum 56×56px for gloved operation
- [ ] **File upload button**: 44×44px minimum, 56×56px recommended
- [ ] **Gallery thumbnail selection**: Touch targets in multi-select mode
- [ ] **Map interaction targets**: Zoom controls, pin placement

### ADD to Screen Reader Support section:
- [ ] **Camera interface**: VoiceOver/TalkBack camera control announcements
- [ ] **Upload progress**: Aria-live regions for upload percentage
- [ ] **File selection**: Multi-file selection announcement patterns
- [ ] **Map navigation**: Coordinate announcement for visually impaired

### ADD to Platform-Specific Accessibility:
- [ ] **iOS camera**: VoiceOver gestures for camera controls
- [ ] **Android camera**: TalkBack camera shortcuts
- [ ] **Web file upload**: Keyboard-only file selection

### ADD to Field Operation Accessibility:
- [ ] **Gloved camera operation**: Larger capture button requirement
- [ ] **Bright sunlight**: High contrast camera overlay needs
- [ ] **Wet conditions**: Water on screen affects camera controls

---

## 2. component-namespace-reference.md

### ADD to Component Listing:
```json
{
  "component-namespace": "faims-custom",
  "component-name": "FileUploader",
  "designer-label": "File Uploader",
  "return-type": "faims-core::Array<File>"
}
{
  "component-namespace": "faims-custom", 
  "component-name": "TakePhoto",
  "designer-label": "Take Photo",
  "return-type": "faims-core::Array<Photo>"
}
{
  "component-namespace": "faims-custom",
  "component-name": "MapForm",
  "designer-label": "Map Selection",
  "return-type": "faims-core::GeoJSON"
}
{
  "component-namespace": "faims-custom",
  "component-name": "TakePoint",
  "designer-label": "Take GPS Point",
  "return-type": "faims-core::Coordinates"
}
```

### ADD to Troubleshooting:
- [ ] FileUpload vs FileUploader naming confusion
- [ ] TakePhoto vs CapturePhoto vs Camera variations
- [ ] MapForm vs MapField ambiguity

---

## 3. data-export-reference.md

### ADD new section "Binary Data Export":
- [ ] **File references in CSV**: Path-only export strategy
- [ ] **Base64 in JSON**: Size limitations and encoding overhead
- [ ] **Binary sync protocols**: Separate file sync from metadata
- [ ] **Chunked uploads**: Handling large files in exports
- [ ] **Thumbnail generation**: Export preview images separately

### ADD to CSV Export Issues:
- [ ] **File paths with commas**: Path escaping requirements
- [ ] **Multiple files per field**: Array serialization in CSV
- [ ] **Relative vs absolute paths**: Path resolution in exports
- [ ] **Missing files**: Handling deleted/moved files in export

### ADD to JSON Export Issues:
- [ ] **Base64 size explosion**: ~33% size increase
- [ ] **Memory limits**: Large images crash export
- [ ] **Streaming alternatives**: JSONL for large media sets
- [ ] **Embedded vs referenced**: Tradeoff documentation

### ADD to Platform-Specific Export:
- [ ] **iOS photo library**: Export permission requirements
- [ ] **Android scoped storage**: Path access restrictions
- [ ] **Web download limits**: Browser file size constraints

---

## 4. designer-limitations-reference.md

### ADD to Configuration Constraints:
- [ ] **File types**: Cannot configure allowed MIME types in Designer
- [ ] **Upload size**: Cannot set max file size in Designer
- [ ] **Camera quality**: Cannot set compression in Designer
- [ ] **Multi-file limits**: Cannot set max file count in Designer

### ADD to Testing Limitations:
- [ ] **Camera testing**: Desktop Designer shows disabled state
- [ ] **Upload testing**: No drag-and-drop in Designer preview
- [ ] **GPS testing**: No location simulation in Designer
- [ ] **Offline testing**: Cannot test sync queue in Designer

### ADD JSON-Only Configurations:
```json
{
  "component-parameters": {
    "maxFileSize": 10485760,  // 10MB in bytes
    "acceptedFileTypes": ["image/*", "application/pdf"],
    "maxFiles": 5,
    "compressionQuality": 0.8,
    "enableGallery": true
  }
}
```

---

## 5. formik-integration-reference.md

### ADD new section "File Field Integration":
- [ ] **File array management**: How Formik handles file arrays
- [ ] **Async upload validation**: Validation during upload
- [ ] **Progress state**: Tracking upload percentage in form state
- [ ] **Cleanup on unmount**: Cancelling uploads when navigating

### ADD to Field State Structure:
```javascript
{
  values: {
    photoField: [
      {
        uri: "file://path/to/photo.jpg",
        type: "image/jpeg",
        size: 2048576,
        uploadProgress: 0.75,
        uploadStatus: "uploading"
      }
    ]
  },
  errors: {
    photoField: "File size exceeds 10MB limit"
  },
  touched: {
    photoField: true
  }
}
```

### ADD to Validation Examples:
- [ ] File size validation
- [ ] File type validation
- [ ] Required file validation
- [ ] Multi-file count validation

---

## 6. meta-properties-reference.md

### ADD to Field Support Matrix:
| Field Type | Annotation | Uncertainty | Both | Persistent |
|------------|------------|-------------|------|------------|
| FileUploader | ✅ | ❌ | ❌ | ✅ |
| TakePhoto | ✅ | ❌ | ❌ | ✅ |
| MapForm | ✅ | ✅ | ✅ | ❌ |
| TakePoint | ✅ | ✅ | ✅ | ❌ |

### ADD Media-Specific Examples:
- [ ] Photo annotation for quality notes
- [ ] GPS uncertainty radius configuration
- [ ] File annotation for processing notes

---

## 7. performance-thresholds-reference.md

### ADD to Performance Limits Table:
| Operation | Threshold | Impact | Mitigation |
|-----------|-----------|--------|------------|
| File upload size | 100MB | Timeout/crash | Chunk large files |
| Concurrent uploads | 3 | Queue delays | Limit simultaneous |
| Image processing | 4096×4096px | Memory crash | Resize before process |
| Gallery thumbnails | 20 images | Render lag | Paginate gallery |
| Map markers | 500 points | Map freezes | Cluster markers |
| Photo compression | 0.7 quality | Balanced size/quality | User configurable |
| Upload timeout | 120 seconds | Failed upload | Retry mechanism |

### ADD Platform-Specific Limits:
- [ ] **iOS**: Photo library permission performance
- [ ] **Android**: Scoped storage access speed
- [ ] **Web**: FileReader API limitations
- [ ] **PWA**: Service worker cache limits

---

## 8. security-considerations-reference.md

### ADD new section "File Upload Security":

#### Vulnerabilities:
- [ ] **Path traversal**: ../../../etc/passwd in filenames
- [ ] **File type spoofing**: .exe renamed to .jpg
- [ ] **Zip bombs**: Compressed files that expand massively
- [ ] **JavaScript in SVG**: XSS via SVG uploads
- [ ] **EXIF data leaks**: GPS coordinates in photos
- [ ] **Malicious PDFs**: Embedded scripts in PDFs

#### Mitigations:
- [ ] Sanitize filenames (remove path characters)
- [ ] Verify MIME types (not just extensions)
- [ ] Set maximum decompression ratios
- [ ] Strip EXIF data or warn users
- [ ] Sandbox PDF rendering
- [ ] Virus scan integration points

#### Implementation:
```javascript
// Example sanitization
function sanitizeFilename(filename) {
  return filename
    .replace(/[^a-zA-Z0-9.-]/g, '_')
    .replace(/\.{2,}/g, '_');
}
```

---

## 9. validation-timing-reference.md

### ADD to Change Event section:
- [ ] **File selection**: Validates immediately on file choose
- [ ] **Photo capture**: Validates after camera confirms
- [ ] **Map selection**: Validates on pin drop
- [ ] **GPS reading**: Validates when accuracy threshold met

### ADD Async Validation Patterns:
- [ ] **Upload progress validation**: Continuous during upload
- [ ] **File type verification**: After file header read
- [ ] **Image dimension check**: After image load
- [ ] **GPS accuracy wait**: Delayed until accuracy sufficient

### ADD to Platform Variations:
- [ ] **iOS**: File validation before upload starts
- [ ] **Android**: Validation during chunked upload
- [ ] **Web**: FileReader async validation pattern

---

## Implementation Order

### Priority 1 (Security-Critical):
1. security-considerations-reference.md - File upload vulnerabilities
2. data-export-reference.md - Binary data handling

### Priority 2 (Functional):
3. performance-thresholds-reference.md - Upload limits
4. validation-timing-reference.md - Async patterns
5. formik-integration-reference.md - File state management

### Priority 3 (Completeness):
6. component-namespace-reference.md - Component listings
7. designer-limitations-reference.md - Configuration limits
8. meta-properties-reference.md - Support matrix
9. accessibility-reference.md - Camera/upload accessibility

---

## Validation Checklist

After updates complete, verify:
- [ ] No duplication between media-fields-v05.md and references
- [ ] All media-specific content added to appropriate references
- [ ] Cross-references work in both directions
- [ ] Examples compile and are accurate
- [ ] Security vulnerabilities comprehensively documented
- [ ] Performance thresholds include actual numbers
- [ ] Platform differences clearly noted

---

## Notes

- Keep reference documents universal while adding media-specific subsections
- Maintain consistent formatting with existing reference content
- Test all code examples for accuracy
- Include platform-specific details where behavior varies
- Add "See media-fields-v05.md" cross-references where appropriate