<!-- concat:boundary:start section="media-fields" -->
<!-- concat:metadata
document_id: media-fields-v05
category: media
field_count: 2
designer_capable: ["TakePhoto", "FileUploader"]
json_only: ["custom_upload_handlers", "file_type_restrictions"]
last_updated: 2025-01-05
-->

# Media Fields - Fieldmark v3 Documentation

## Document Navigation
<!-- concat:nav-mode:individual -->
[← Location Fields](./location-fields-v05.md) | **Media Fields** | [Relationship Fields →](./relationship-field-v05.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Relationship Fields ↓](#relationship-fields) -->


## Overview {essential}

### DESIGNER QUICK GUIDE
**Media Capture Fields Available:**
- **FileUploader** → Upload any existing files from device
## Component Name Mapping {essential}

| Designer UI Label | JSON component-name | Namespace | Code File | Description |
|------------------|-------------------|-----------|-----------|-------------|
| Take Photo | TakePhoto | faims-custom | TakePhoto.tsx | Camera capture & gallery |
| File Uploader | FileUploader | faims-custom | FileUploader.tsx | General file attachment |

### Critical Naming Issues {important}
- **TakePhoto misnomer**: Also handles gallery selection, not just camera
- **Required validation broken**: Known issue with required field validation
- **File type restrictions**: Cannot actually restrict file types despite settings
- **Silent failures**: Upload errors often fail silently

- **FileUploader** (capital F, capital U) - NOT "fileuploader" or "File Uploader"
- **TakePhoto** (capital T, capital P) - NOT "takephoto" or "Take Photo"
- Both components use namespace `"faims-custom"` - never "core" or "basic"
- Return type is `faims-attachment::Files` for both - maintains compatibility

### Media Capture Fields (2 total)
1. **FileUploader** - Upload existing files of any type from device storage
2. **TakePhoto** - Capture new photos using device camera with gallery fallback

### Component Status Summary
| Field | Designer | JSON Enhancement | Validation | Platform Support |
|-------|----------|------------------|------------|------------------|
| FileUploader | ✅ Basic | Required for constraints | ⚠️ Broken required | All platforms |
| TakePhoto | ✅ Full | Optional for validation | ⚠️ Manual required | All platforms |

## Designer Usage Guide {essential}

### What to Select in Designer
1. Navigate to Field Type selection
2. Choose "Custom Field" category
3. Select either:
   - **FileUploader** for document/file uploads
   - **TakePhoto** for camera capture
4. Configure standard properties (label, helper text, annotations)

### When JSON Enhancement is Required
**FileUploader JSON-only parameters:**
- `multiple` - Allow multiple file selection
- `maximum_file_size` - Size limit in bytes
- `minimum_file_size` - Minimum size in bytes  
- `maximum_number_of_files` - File count limit

**TakePhoto JSON-only validation:**
- Required validation via `yup.required`
- Min/max photo counts via `yup.min`/`yup.max`

### Designer Limitations {important}
See [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) for universal constraints.

**Media-Specific Designer Limitations:**
- Cannot configure file size limits through Designer
- Cannot set multiple file selection toggle
- Cannot enforce photo count limits
- Required validation not enforced (TakePhoto shows asterisk, FileUploader doesn't, neither enforces)
- No file type restrictions available in Designer

## Field Selection Guide {essential}

### Decision Tree
```
Need to capture media?
├─ Static files from device?
│  └─ YES → FileUploader
│     ├─ Returns: faims-attachment::Files (array)
│     ├─ Accepts: Any file type without restriction
│     └─ Best for: Documents, maps, professional photos, mixed media
│
└─ Take new photo with camera?
   └─ YES → TakePhoto
      ├─ Returns: faims-attachment::Files (array)
      ├─ Output: JPEG at 90% quality
      └─ Best for: Field documentation, quick reference photos
```

### Decision Matrix
| Requirement | FileUploader | TakePhoto |
|------------|--------------|-----------|
| Camera access | ❌ | ✅ |
| Gallery selection | ✅ | ✅ |
| Multiple files | ✅ Configurable | ✅ Always |
| File type restriction | ❌ | ✅ Images only |
| Size limits | ✅ JSON config | ❌ |
| GPS injection | ❌ | ✅ Native only |
| EXIF preservation | ❌ Stripped | ❌ Stripped |
| Offline capture | ✅ | ✅ |
| Progress indicators | ❌ | ❌ |

### Selection Strategy
- **FileUploader when:**
  - Uploading pre-existing files
  - Need mixed media types
  - Professional camera images required
  - Document management workflows
  
- **TakePhoto when:**
  - Immediate photo capture needed
  - GPS coordinates valuable
  - Camera workflow integration required
  - Quick reference documentation

## ⚠️ Critical Media Security Risks {essential}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for general security patterns.

**Media-Specific Security Concerns:**
- **FileUploader accepts ANY file type** including executables, scripts, malware
- **No virus scanning** on uploaded files
- **Path traversal risks** via malicious filenames
- **JavaScript execution** possible in SVG uploads
- **EXIF privacy leaks** - Location data in uploaded photos
- **Memory exhaustion** - No client-side size validation
- **Storage attacks** - Unlimited uploads can fill device/server
- **No content validation** - Corrupt or malicious files accepted

**Mitigation Requirements:**
- Deploy only in trusted research environments
- Implement server-side validation if public-facing
- Document acceptable file types in helper text
- Monitor unusual upload patterns
- Set explicit size/count limits via JSON

## What These Fields Cannot Do {important}

**Both Fields Cannot:**
- Preserve EXIF metadata (stripped on upload)
- Show upload/processing progress
- Validate file content integrity
- Scan for viruses or malware
- Enforce required validation reliably
- Reorder captured/uploaded files
- Edit images after capture
- Generate consistent thumbnails

**FileUploader Specific:**
- Cannot restrict file types
- Cannot access device camera
- Cannot inject GPS coordinates
- Cannot provide user feedback on constraint violations

**TakePhoto Specific:**
- Cannot capture RAW images
- Cannot preserve camera settings
- Cannot upload existing files directly
- Cannot configure image quality/compression

## Common Use Cases {important}

**FileUploader Use Cases:**
- Heritage permit documentation (PDFs)
- Drone footage and aerial photography
- Laboratory analysis reports
- Historical maps and plans
- Audio recordings and interviews
- DSLR professional photography
- Mixed media archaeological records

**TakePhoto Use Cases:**
- Excavation progress documentation
- Artefact field photography
- Site condition monitoring
- Stratigraphic profile capture
- Feature documentation
- Environmental context photos
- Quick reference imagery

## Designer Component Mapping {essential}

| Designer Option | Component Config | Notes |
|-----------------|------------------|-------|
| Custom Field → FileUploader | `"component-namespace": "faims-custom"` | Upload files |
| Custom Field → TakePhoto | `"component-namespace": "faims-custom"` | Camera capture |
| Label | `"label": "Field Label"` | Both fields |
| Helper Text | `"helperText": "Guidance"` | Both fields |
| Required | `"required": true` | Visual only |
| Advanced Helper | `"advancedHelperText": "## Markdown"` | Both fields |

## Designer Capabilities vs JSON Enhancement {essential}

### Designer Configuration (Both Fields)
- ✅ Field labels and naming
- ✅ Helper text (basic and advanced)
- ✅ Conditional visibility
- ✅ Annotation fields
- ✅ Uncertainty fields
- ⚠️ Required indicator (visual only)

### JSON-Only Configuration

**FileUploader:**
```json
{
  "multiple": true,                    // Allow multiple files
  "maximum_file_size": 10485760,       // 10MB limit
  "minimum_file_size": 1024,           // 1KB minimum
  "maximum_number_of_files": 5         // Max 5 files
}
```

**TakePhoto:**
```json
{
  "validationSchema": [
    ["yup.array"],
    ["yup.required", "Photos required"],
    ["yup.min", 1, "Minimum 1 photo"],
    ["yup.max", 10, "Maximum 10 photos"]
  ]
}
```

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

**Media-Specific Namespace Issues:**
- Using "core" instead of "faims-custom" - Fields won't render
- Lowercase component names - Component not found errors
- Space in component name - Parse errors


## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| Photo documentation | TakePhoto | Camera optimized |
| Document uploads | FileUploader | Any file type |
| Mixed media | FileUploader | More flexible |
| Evidence photos | TakePhoto | Direct camera access |

### Decision Criteria
- **File type**: Photos only → TakePhoto, Any type → FileUploader
- **Camera access**: Required → TakePhoto, Optional → FileUploader
- **File source**: Camera → TakePhoto, Existing files → FileUploader
- **Validation**: Neither properly validates required fields (known issue)

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Media-Specific Security Notes:**
- FileUploader accepts executables without validation
- No client-side content scanning
- Base64 encoding increases memory usage 33%
- Orphaned attachments accumulate without cleanup
- EXIF location data exposed in original files

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for general limits.

**Media-Specific Performance:**
- **File upload timeout:** 120 seconds default
- **Max individual file:** 50MB recommended, 100MB absolute
- **Image processing limit:** 4096×4096 pixels
- **Concurrent uploads:** 3 maximum
- **TakePhoto images:** 20 maximum before degradation
- **Memory overhead:** ~33% for base64 encoding
- **Browser storage:** 1GB Safari, 6GB Chrome
- **Sync bandwidth:** Consider with "Get attachments" enabled

### Validation Patterns {important}
See [Validation System Documentation](../detail-crossfield-docs/validation.md) for comprehensive validation patterns and timing.

**Media Field-Specific Validation:**
- **File type**: Validated at selection (TakePhoto only)
- **File size**: Silent rejection without error message (FileUploader)
- **Required files**: Broken in Designer, needs JSON validation schema
- **File count**: Via `yup.array.min/max` only
- **Content scanning**: Not performed (no virus/malware checks)
- **Async validation**: Not supported during upload process

### Platform Behaviors {important}
See [Platform Behaviors Reference](../reference-docs/platform-behaviors-reference.md) for general platform characteristics.

**Media Field-Specific Behaviors:**
- **iOS**: HEIC→JPEG auto-conversion; combined camera/photo permissions; ProRAW/Live Photos metadata lost
- **Android**: Storage Access Framework (no permissions); manufacturer camera variations; direct JPEG capture
- **Web**: MediaDevices API or file input; no GPS in EXIF; IndexedDB storage limits

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.

Both media fields support:
- **Annotation:** Field-level notes (not per-file)
- **Uncertainty:** Quality/confidence indicators

Note: Annotations apply to entire field, not individual files.

### Export Behavior {important}
See [Data Export Reference](../reference-docs/data-export-reference.md) for universal patterns.

**Media-Specific Export:**
- **Binary files:** Separate files in export package
- **CSV reference:** Semicolon-separated filenames
- **JSON format:** Full attachment metadata
- **Filename pattern:** `{recordID}_{fieldname}_{index}.ext`
- **Duplicate handling:** Append `*1`, `*2` suffixes
- **Missing files:** Silently skipped
- **Original names:** Lost during export
- **Storage IDs:** `att-{uuid}` format

## Individual Field Reference {essential}

### FileUploader {essential}

#### Purpose {essential}
Provides comprehensive file attachment capabilities accepting any file type without restriction. Implements web-standard approach through React Dropzone, operating as temporary file accumulator until form submission triggers PouchDB synchronisation.

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | `faims-custom::FileUploader` |
| Returns | `faims-attachment::Files` |
| Designer | ✅ Basic support |
| JSON Required | File constraints |
| Touch Target | Upload button 44×44px minimum |
| Max File Size | 50MB recommended (JSON config) |
| Concurrent | 3 uploads maximum |
| Offline | ✅ Queued for sync |
| Security | ⚠️ No validation |

#### Core Configuration
```json
{
  "component-namespace": "faims-custom",
  "component-name": "FileUploader",
  "type-returned": "faims-attachment::Files",
  "component-parameters": {
    "label": "Upload Documents",
    "name": "documents",
    "helperText": "Upload permits, maps, reports (max 10MB each)",
    "required": false,
    "multiple": true,
    "maximum_file_size": 10485760,
    "maximum_number_of_files": 5
  },
  "validationSchema": [["yup.mixed"]],
  "initialValue": null
}
```

#### Advanced Configuration
```json
{
  "survey-media": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Survey Documentation",
      "name": "survey-media",
      "helperText": "DSLR photos, drone footage, GIS exports",
      "advancedHelperText": "## Accepted Formats\n- Images: JPG, PNG, TIFF, RAW\n- Documents: PDF, DOCX\n- Data: CSV, SHP, KML\n- Video: MP4, MOV (max 50MB)",
      "multiple": true,
      "maximum_file_size": 52428800,
      "minimum_file_size": 1024
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "File descriptions"
      }
    }
  }
}
```

#### Platform-Specific Behaviors
- **Desktop:** Drag-and-drop with hover states, click-to-select
- **iOS:** Document picker accessing iCloud Drive, local storage
- **Android:** Storage Access Framework, no permissions required
- **Web:** Standard HTML file input element

#### Common Issues & Solutions
| Issue | Cause | Solution |
|-------|-------|----------|
| Files disappear | Silent size/count violation | Document limits in helper text |
| Required not working | yup.mixed() can't validate arrays | Use helper text to indicate |
| Browser crash | Memory exhaustion >50MB files | Limit file sizes via JSON |
| Files lost on refresh | No persistence before submission | Save form frequently |
| No upload progress | Missing indicators | Inform users about submission timing |

### TakePhoto {essential}

#### Purpose {essential}
Integrates platform-native camera functionality with gallery selection through unified interface. Leverages Capacitor's camera plugin for cross-platform image capture with GPS injection on native platforms.

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | `faims-custom::TakePhoto` |
| Returns | `faims-attachment::Files` |
| Designer | ✅ Full support |
| JSON Required | Validation only |
| Touch Target | Camera button 44×44px minimum |
| Image Quality | JPEG 90% |
| GPS Support | ✅ Native platforms only |
| Max Photos | 20 before performance impact |
| Offline | ✅ Full functionality |

#### Core Configuration
```json
{
  "component-namespace": "faims-custom",
  "component-name": "TakePhoto",
  "type-returned": "faims-attachment::Files",
  "component-parameters": {
    "label": "Site Photos",
    "name": "site-photos",
    "helperText": "Capture site overview and details",
    "required": false
  },
  "validationSchema": [
    ["yup.array"],
    ["yup.of", [["yup.object"], ["yup.nullable"]]],
    ["yup.nullable"]
  ],
  "initialValue": null
}
```

#### Advanced Configuration
```json
{
  "artefact-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Artefact Documentation",
      "name": "artefact-photos",
      "helperText": "Capture 2-10 photos from multiple angles",
      "required": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.of", [["yup.object"], ["yup.nullable"]]],
      ["yup.required", "Artefact photos required"],
      ["yup.min", 2, "Minimum 2 angles required"],
      ["yup.max", 10, "Maximum 10 photos"]
    ],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "Angle and lighting notes"
      },
      "uncertainty": {
        "include": true,
        "label": "Image quality"
      }
    }
  }
}
```

#### Platform-Specific Behaviors
- **iOS:** "Take Photo or Choose from Library" prompt, HEIC→JPEG conversion
- **Android:** Standard camera/gallery selector, direct JPEG capture
- **Web:** MediaDevices API with file input fallback, no GPS
- **All:** Automatic orientation correction applied

#### Common Issues & Solutions
| Issue | Symptoms | Solution |
|-------|----------|----------|
| Permission denied | Error about permissions | Settings > Apps > Permissions |
| Required not working | Empty submission allowed | Add yup.required to schema |
| Performance slow | Many photos lag form | Limit to 20 photos maximum |
| No GPS coordinates | Web platform limitation | Use native apps for GPS |
| EXIF data missing | Expected - always stripped | Use FileUploader for EXIF |
| Images not syncing | Local only visibility | Enable "Get attachments" |

## Troubleshooting Guide {important}

### Issue 1: Silent File Rejection (FileUploader)
**Symptoms**: Files appear to upload but disappear without error message

**Diagnosis Steps**:
1. Check browser console for size limit messages
2. Count existing files in field
3. Verify file size in bytes
4. Test with smaller file

**Common Causes & Solutions**:
- **File too large**: `maximum_file_size` exceeded silently
  - Solution: Add explicit size limits to helper text
  - Example: "Maximum 10MB per file" 
- **Too many files**: `maximum_number_of_files` reached
  - Solution: Document limit clearly, consider increasing
- **File too small**: `minimum_file_size` not met (rare)
  - Solution: Check for 0-byte files

**Prevention**: Always specify limits in helper text since validation doesn't show errors

### Issue 2: Required Validation Not Working (Both Fields)
**Symptoms**: Form submits with empty required media fields

**Root Cause**: 
- FileUploader uses `yup.mixed()` which cannot validate arrays
- TakePhoto requires manual `yup.required` addition

**Solutions**:

For FileUploader (use helper text workaround):
```json
{
  "validationSchema": [["yup.mixed"]],
  "helperText": "⚠️ REQUIRED: Upload at least one document"
}
```

For TakePhoto (manual validation configuration):
```json
{
  "validationSchema": [
    ["yup.array"],
    ["yup.required", "Photos required"],
    ["yup.min", 1, "At least one photo required"]
  ]
}
```

### Issue 3: Browser Memory Exhaustion
**Symptoms**: Browser tab crashes or becomes unresponsive during upload

**Diagnosis**:
1. Open browser DevTools → Performance Monitor
2. Watch memory usage during file selection
3. Check if files exceed 50MB each
4. Count total size of all uploads

**Solutions by File Size**:
- **<10MB**: Should work on all devices
- **10-50MB**: May struggle on older mobile devices
- **50-100MB**: High crash risk, desktop only
- **>100MB**: Not recommended, will likely fail

**Mitigation Strategies**:
1. Compress images before upload
2. Split large PDFs into sections
3. Use external links for very large files
4. Process files in smaller batches

### Issue 4: Camera Permission Denied (TakePhoto)
**Symptoms**: Camera button disabled or "Permission denied" error

**Platform-Specific Recovery**:

**iOS**:
1. Settings → Privacy & Security → Camera
2. Find app in list and toggle ON
3. May need to fully quit and restart app
4. "Allow Once" requires re-permission each session

**Android**:
1. Settings → Apps → [App Name] → Permissions
2. Enable Camera permission
3. Check "Don't ask again" wasn't selected
4. Clear app cache if permission stuck

**Web Browser**:
1. Click padlock icon in address bar
2. Reset camera permission
3. Reload page
4. Accept permission prompt

### Issue 5: Photos Not Syncing (TakePhoto)
**Symptoms**: Photos visible locally but not on other devices

**Diagnosis Checklist**:
- [ ] Check sync status indicator
- [ ] Verify "Get attachments" setting enabled
- [ ] Confirm network connectivity
- [ ] Check available cloud storage

**Common Causes**:
1. **"Get attachments" disabled**: Enable in notebook settings
2. **Sync timeout**: Photos >10MB may timeout
3. **Quota exceeded**: Check CouchDB attachment limits
4. **Network interruption**: Retry sync manually

**Solutions**:
1. Enable "Get attachments" in sync settings
2. Reduce photo quality if consistently failing
3. Sync over WiFi for large photo sets
4. Check server attachment quota

## JSON Examples {comprehensive}

### Example 1: Basic File Upload with Size Limits
```json
{
  "supporting-documents": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Supporting Documents",
      "name": "supporting-documents",
      "helperText": "Upload permits, maps, protocols (max 10MB each)",
      "multiple": true,
      "maximum_file_size": 10485760,
      "minimum_file_size": 1024
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null
  }
}
```

### Example 2: Required Single Photo Capture
```json
{
  "artifact-photo": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Artifact Photo",
      "name": "artifact-photo",
      "helperText": "Photograph artifact with scale",
      "required": true,
      "multiple": false
    },
    "validationSchema": [
      ["yup.mixed"],
      ["yup.required", "Artifact photo required"]
    ],
    "initialValue": null
  }
}
```

### Example 3: Multiple File Upload with Count Restriction
```json
{
  "site-documentation": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Site Documentation",
      "name": "site-documentation",
      "helperText": "Upload up to 5 files (photos, PDFs, spreadsheets)",
      "advancedHelperText": "## File Requirements\n\n- Maximum 5 files total\n- Each file max 25MB\n- Accepted: JPG, PNG, PDF, XLSX, CSV",
      "multiple": true,
      "maximum_file_size": 26214400,
      "maximum_number_of_files": 5
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null
  }
}
```

### Example 4: Conditional Photo Documentation
```json
{
  "damage-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Damage Documentation",
      "name": "damage-photos",
      "helperText": "Photograph all damaged areas",
      "multiple": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 1, "At least one damage photo required"]
    ],
    "initialValue": null,
    "condition": {
      "operator": "equal",
      "field": "condition-assessment",
      "value": "damaged"
    }
  }
}
```

### Example 5: PDF-Only Document Upload
```json
{
  "permits": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Heritage Permits",
      "name": "permits",
      "helperText": "Upload PDF permits only (max 10MB each)",
      "advancedHelperText": "⚠️ **PDF Files Only**\n\nPlease convert all documents to PDF before uploading.\nNon-PDF files will need to be removed.",
      "multiple": true,
      "maximum_file_size": 10485760
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "Permit conditions and restrictions"
      }
    }
  }
}
```

### Example 6: Staged Photography Workflow
```json
{
  "before-excavation": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Before Excavation",
      "name": "before-excavation",
      "helperText": "Document initial state (2-5 photos)",
      "required": true,
      "multiple": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.required", "Before photos required"],
      ["yup.min", 2, "Minimum 2 photos"],
      ["yup.max", 5, "Maximum 5 photos"]
    ],
    "initialValue": null
  },
  "after-excavation": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "After Excavation",
      "name": "after-excavation",
      "helperText": "Document final state (2-5 photos)"
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 2, "Minimum 2 photos"]
    ],
    "initialValue": null,
    "condition": {
      "operator": "is-truthy",
      "field": "before-excavation"
    }
  }
}
```

### Example 7: Large Media Files with Warning
```json
{
  "video-documentation": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Video Documentation",
      "name": "video-documentation",
      "helperText": "Upload video files (max 100MB)",
      "advancedHelperText": "## ⚠️ Large File Warning\n\n- Files over 50MB may cause sync delays\n- Ensure stable WiFi before syncing\n- Consider compressing videos first",
      "multiple": false,
      "maximum_file_size": 104857600
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null
  }
}
```

### Example 8: Mixed Media Documentation
```json
{
  "excavation-media": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Excavation Media",
      "name": "excavation-media",
      "helperText": "Photos, videos, plans (max 25MB each, 10 files total)",
      "multiple": true,
      "maximum_file_size": 26214400,
      "maximum_number_of_files": 10
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null
  }
}
```

### Example 9: Progressive Photo Requirements
```json
{
  "context-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Context Photos",
      "name": "context-photos",
      "helperText": "North, South, East, West views plus overhead",
      "multiple": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.required", "Context photos required"],
      ["yup.min", 5, "Need all 5 standard views"]
    ],
    "initialValue": null
  }
}
```

### Example 10: Data Files with Metadata
```json
{
  "analysis-data": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Analysis Data Files",
      "name": "analysis-data",
      "helperText": "Upload CSV, XLSX data files",
      "multiple": true,
      "maximum_file_size": 5242880,
      "maximum_number_of_files": 3
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "Data collection methods and parameters"
      },
      "uncertainty": {
        "include": true,
        "label": "Data quality concerns"
      }
    }
  }
}
```

### Example 11: Emergency Documentation Mode
```json
{
  "salvage-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Salvage Documentation",
      "name": "salvage-photos",
      "helperText": "Quick capture - as many as needed",
      "multiple": true
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null,
    "condition": {
      "operator": "equal",
      "field": "recording-type",
      "value": "emergency-salvage"
    }
  }
}
```

### Example 12: Structured Upload Workflow
```json
{
  "plans": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Site Plans",
      "name": "plans",
      "helperText": "Upload georeferenced plans (PDF/TIFF)",
      "multiple": true,
      "maximum_file_size": 52428800,
      "maximum_number_of_files": 3
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null
  },
  "sections": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Section Drawings",
      "name": "sections",
      "helperText": "Upload section drawings (PDF/JPG)",
      "multiple": true,
      "maximum_file_size": 26214400,
      "maximum_number_of_files": 5
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null,
    "condition": {
      "operator": "is-truthy",
      "field": "plans"
    }
  }
}
```

### Example 13: Performance-Optimized Configuration
```json
{
  "field-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Field Photos",
      "name": "field-photos",
      "helperText": "Max 10 photos to prevent sync issues",
      "multiple": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.max", 10, "Maximum 10 photos for performance"]
    ],
    "initialValue": null
  }
}
```

### Example 14: Compliance Documentation
```json
{
  "compliance-docs": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Compliance Documentation",
      "name": "compliance-docs",
      "helperText": "Safety certificates, insurance, permits",
      "advancedHelperText": "## Required Documents\n\n1. Public liability insurance\n2. Safety management plan\n3. Heritage permit\n4. Landowner consent",
      "required": true,
      "multiple": true,
      "maximum_file_size": 10485760,
      "minimum_file_size": 1024,
      "maximum_number_of_files": 10
    },
    "validationSchema": [
      ["yup.mixed"],
      ["yup.required", "Compliance documentation required"]
    ],
    "initialValue": null
  }
}
```

### Example 15: Artifact Photography Standards
```json
{
  "artifact-images": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Artifact Photography",
      "name": "artifact-images",
      "helperText": "Multiple angles with scale",
      "advancedHelperText": "## Photography Requirements\n\n- Front view with scale\n- Back view\n- Profile views if relevant\n- Detail shots of diagnostic features",
      "required": true,
      "multiple": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.required", "Artifact photos required"],
      ["yup.min", 2, "Minimum front and back views"]
    ],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "Photography conditions and issues"
      }
    }
  }
}
```

### Example 16: Conditional Document Upload
```json
{
  "permit-documents": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Permit Documentation",
      "name": "permit-documents",
      "helperText": "Upload permits and approvals (Max 10MB each)",
      "multiple": true,
      "maximum_file_size": 10485760,
      "maximum_number_of_files": 5
    },
    "validationSchema": [["yup.mixed"]],
    "condition": {
      "operator": "equal",
      "field": "site-type",
      "value": "restricted"
    }
  }
}
```

### Example 17: Large File Warning Configuration
```json
{
  "video-documentation": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Video Files",
      "name": "video-documentation",
      "helperText": "⚠️ WARNING: Max 100MB per file. Videos will impact sync performance.",
      "advancedHelperText": "## Video Guidelines\n\n- Compress videos before upload\n- Consider frame extraction for analysis\n- Upload will timeout after 120 seconds",
      "multiple": false,
      "maximum_file_size": 104857600,
      "minimum_file_size": 1024
    },
    "validationSchema": [["yup.mixed"]],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Video content description"
      }
    }
  }
}
```

### Example 18: Multi-Stage Photo Workflow
```json
{
  "excavation-progress": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Excavation Stage Photos",
      "name": "excavation-progress",
      "helperText": "Document each 10cm level",
      "advancedHelperText": "## Photo Protocol\n\n1. Overview from fixed photo point\n2. Plan view with north arrow\n3. Representative profile\n4. Any features or finds in situ",
      "multiple": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.min", 3, "Minimum 3 photos per level"],
      ["yup.max", 20, "Maximum 20 photos for performance"]
    ],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Depth and stage notes"
      },
      "uncertainty": {
        "include": true,
        "label": "Photo quality issues"
      }
    }
  }
}
```

### Example 19: Emergency Documentation Fallback
```json
{
  "emergency-capture": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Emergency Documentation",
      "name": "emergency-capture",
      "helperText": "Quick capture - quality secondary to speed",
      "multiple": true
    },
    "validationSchema": [["yup.array"]],
    "condition": {
      "operator": "equal",
      "field": "documentation-type",
      "value": "emergency"
    }
  }
}
```

### Example 20: Mixed Media Archive Upload
```json
{
  "archive-materials": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Archive Materials",
      "name": "archive-materials",
      "helperText": "PDFs, images, spreadsheets accepted. Max 50MB each.",
      "advancedHelperText": "## Accepted Formats\n\n- Documents: PDF, DOC, DOCX\n- Images: JPG, PNG, TIFF\n- Data: CSV, XLS, XLSX\n- Archives: ZIP (under 50MB)",
      "multiple": true,
      "maximum_file_size": 52428800,
      "maximum_number_of_files": 10
    },
    "validationSchema": [["yup.mixed"]],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Archive catalog numbers and descriptions"
      }
    }
  }
}
```

## Migration Scenarios {comprehensive}

### Scenario 1: File Size Limit Changes
**Context**: Project needs stricter file size limits due to sync performance issues

**Challenge**: Existing records have files exceeding new limits
- Current files may be 100MB+
- New limit needs to be 50MB
- No retroactive validation available

**Migration Steps**:
1. Export existing data with attachment metadata
2. Identify files exceeding new limits
3. Compress or split large files externally
4. Update FileUploader configuration with new `maximum_file_size`
5. Document compression requirements in helper text

### Scenario 2: Moving from FileUploader to TakePhoto
**Context**: Project shifts from accepting any images to requiring in-field capture only

**Challenge**: Data structure differences
- FileUploader accepts any file type
- TakePhoto produces only JPEG at 90% quality
- GPS metadata available only with TakePhoto on native apps

**Migration Steps**:
1. Extract image files from FileUploader records
2. Document which images need recapture
3. Update field configuration to TakePhoto
4. Train users on camera-only workflow
5. Consider keeping FileUploader for historical data

### Scenario 3: Photo Quality/Compression Requirements
**Context**: Storage constraints require reducing photo sizes

**Challenge**: TakePhoto has fixed 90% JPEG quality
- No in-app compression settings
- Files typically 2-5MB each
- Need <1MB per photo

**Workarounds**:
1. External compression before upload (FileUploader)
2. Reduce camera resolution in device settings
3. Post-process photos after sync
4. Consider using FileUploader with compressed images
5. Document size requirements clearly

### Scenario 4: Handling Orphaned Attachments
**Context**: Database has accumulated orphaned media files from deleted records

**Challenge**: No automatic cascade deletion
- Attachments remain after record deletion
- Storage quota being consumed
- No built-in cleanup tools

**Migration Steps**:
1. Audit attachment references in database
2. Identify orphaned files (no parent record)
3. Backup orphaned files before deletion
4. Manual cleanup via database tools
5. Implement deletion procedures to prevent future orphans

### Scenario 5: Multiple to Single File Fields
**Context**: Simplifying form to accept only one file instead of multiple

**Challenge**: Existing records have arrays of files
- Current: `multiple: true` with file arrays
- Target: `multiple: false` with single file
- Validation schema changes required

**Migration Steps**:
1. Export existing multi-file data
2. Decide which file to keep (first, largest, most recent)
3. Update field configuration to `multiple: false`
4. Change validation from `yup.array` to `yup.mixed`
5. Re-import with single file per record

## Best Practices {comprehensive}

### Performance Best Practices
- **FileUploader:** Limit individual files to 50MB
- **TakePhoto:** Maximum 20 photos per field
- **Total per record:** Keep under 200MB combined
- **Helper text:** Always specify size/count limits
- **Sync strategy:** Disable "Get attachments" for bandwidth
- **Batch uploads:** Process in groups to avoid timeouts

### Security Best Practices
- **Deployment:** Trusted research teams only
- **Documentation:** List acceptable file types
- **Monitoring:** Review uploads regularly
- **Server validation:** Implement if public-facing
- **Storage limits:** Set maximum sizes via JSON

### Storage Management Best Practices
- **Pre-fieldwork:** Check device storage availability
- **Size limits:** Document in helper text clearly
- **Sync strategy:** Consider "Get attachments" setting impact
- **Regular cleanup:** Remove orphaned attachments periodically
- **Compression:** Train users on image optimization

## Field Quirks Index (2025-01-03) {comprehensive}

### FileUploader Quirks
- Required validation completely broken
- Silent rejection without user feedback
- Memory leaks from unreleased Object URLs
- No cascade deletion creates orphaned attachments
- Accepts executables without warning

### TakePhoto Quirks
- Required validation needs manual JSON configuration
- GPS injection native platforms only
- EXIF data always stripped
- Performance degradation after 20 photos
- Permission error shows wrong component (LocationPermissionIssue)

### Shared Quirks
- No progress indicators during upload
- Original filenames lost in export
- Base64 encoding 33% overhead
- No file-level annotations (field-level only)
- Export filename pattern inconsistent

## Performance Thresholds Summary {essential}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for detailed metrics.

**Media-Specific Thresholds:**
| Metric | FileUploader | TakePhoto | Impact |
|--------|--------------|-----------|---------|
| Individual file | 50MB soft / 100MB hard | N/A | Browser crash risk |
| Total per field | 200MB | 20 photos | Form sluggish |
| Concurrent operations | 3 uploads | 1 capture | UI blocks |
| Memory overhead | +33% base64 | +33% base64 | Quota exhaustion |
| Sync timeout | 120 seconds | 120 seconds | Upload fails |
| Storage quota | 1GB Safari / 6GB Chrome | Same | Capture fails |

## JSON Patterns Cookbook (2025-01-03) {comprehensive}

### Pattern: Conditional Media Requirements
```json
{
  "damage-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "condition": {
      "operator": "and",
      "conditions": [
        {"operator": "equal", "field": "damage-present", "value": "yes"},
        {"operator": "greater-than", "field": "damage-severity", "value": 5}
      ]
    }
  }
}
```

### Pattern: Size-Limited Document Upload
```json
{
  "permits": {
    "component-parameters": {
      "maximum_file_size": 5242880,  // 5MB
      "maximum_number_of_files": 3,
      "helperText": "Max 3 files, 5MB each. Larger files will disappear without warning."
    }
  }
}
```

### Pattern: Required Photo Documentation
```json
{
  "validationSchema": [
    ["yup.array"],
    ["yup.required", "Photos are mandatory"],
    ["yup.test", "file-check", "Invalid photo array", 
      ["yup.ref", "$"], 
      "function(value) { return value && value.length > 0; }"]
  ]
}
```

## JSON Anti-patterns Quick Index {comprehensive}

### ❌ Don't: Mix Parameters
```json
// WRONG - TakePhoto doesn't support file size limits
{
  "component-name": "TakePhoto",
  "component-parameters": {
    "maximum_file_size": 10485760  // Ignored!
  }
}
```

### ❌ Don't: Wrong Namespace
```json
// WRONG - Must be faims-custom
{
  "component-namespace": "core",
  "component-name": "FileUploader"
}
```

### ❌ Don't: Invalid Initial Value
```json
// WRONG - Must be null, not empty array
{
  "initialValue": []
}
```

## Quick Diagnosis Tables (2025-01-03) {important}

### Media Field Issues Diagnosis
| Symptom | Field | Likely Cause | Quick Fix | Platform | Prevention |
|---------|-------|--------------|-----------|----------|------------|
| Field not rendering | Both | Wrong namespace | Use `faims-custom` | All | Check spelling |
| Files disappearing | FileUploader | Size limit exceeded | Check maximum_file_size | All | Document limits |
| Can't require field | Both | Validation broken | Add yup.required manually | All | Use helper text |
| No camera option | FileUploader | Wrong field type | Use TakePhoto instead | All | Field selection |
| No GPS coordinates | TakePhoto | Web platform | Use native app | Web | Platform choice |
| Slow form | TakePhoto | Too many photos | Limit to 20 maximum | Mobile | Set max validation |
| Upload fails | Both | Network timeout | Check file sizes | All | <50MB files |
| Permission denied | TakePhoto | Camera access blocked | Check settings | All | Pre-setup |
| Memory crash | Both | Files too large | Reduce file size | Mobile | Compress first |
| No progress bar | Both | Not implemented | Inform users to wait | All | Set expectations |
| EXIF stripped | Both | Security feature | Cannot preserve | All | Document separately |
| Sync timeout | Both | Large attachments | Use WiFi, smaller files | Mobile | Batch uploads |
| Photos local only | TakePhoto | "Get attachments" off | Enable in settings | All | Check settings |
| Wrong component | Both | Copy-paste error | Verify component-name | All | Double-check |
| Empty array error | Both | Wrong initial value | Use null not [] | All | Correct init |

## Field Interaction Matrix (2025-01-03) {important}

### Media Fields with Other Field Types
| Field Combination | Interaction | Common Pattern |
|------------------|-------------|----------------|
| FileUploader + TakePhoto | Independent | Mixed media workflows |
| TakePhoto + TakePoint | Complementary | Photo with GPS reference |
| FileUploader + Select | Categorization | Document type selection |
| TakePhoto + Annotation | Metadata | Photo descriptions |
| FileUploader + TextField | Description | File source notes |
| Media + TemplatedString | Identification | Generate file identifiers |

## Migration Warnings Index (2025-01-03) {comprehensive}

### Critical Migration Issues
1. **Required validation breaks** - Must use helper text instead
2. **File type restrictions** not available - No MIME filtering
3. **Progress indicators** missing - Users wait without feedback
4. **EXIF preservation** not possible - Stripped on upload
5. **Bulk operations** require manual configuration
6. **Performance limits** strict - 50MB files, 20 photos maximum
7. **Orphaned attachments** accumulate without cleanup

## See Also {comprehensive}

### Other Field Categories
- **[Text Fields](./text-fields-v05.md)**: For detailed media descriptions and captions
- **[Number Fields](./number-fields-v05.md)**: For file size tracking and GPS coordinates
- **[DateTime Fields](./datetime-fields-v05.md)**: For capture timestamps
- **[Select/Choice Fields](./select-choice-fields-v05.md)**: For media type categorization
- **[Location Fields](./location-fields-v05.md)**: For georeferenced photo locations
- **[Relationship Field](./relationship-field-v05.md)**: For linking media to records
- **[Display Field](./display-field-v05.md)**: For media capture instructions

### Reference Documents
  - [Validation Timing Reference](../reference-docs/validation-timing-reference.md)
  - [Data Export Reference](../reference-docs/data-export-reference.md) - Binary data handling
  - [Security Considerations](../reference-docs/security-considerations-reference.md) - Upload vulnerabilities
  - [Performance Thresholds](../reference-docs/performance-thresholds-reference.md) - Upload limits
  - [Accessibility Reference](../reference-docs/accessibility-reference.md) - Camera accessibility
  - [Component Namespace Reference](../reference-docs/component-namespace-reference.md) - Troubleshooting
  - [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) - JSON requirements
  - [Meta Properties Reference](../reference-docs/meta-properties-reference.md) - Annotations
  - [Formik Integration Reference](../reference-docs/formik-integration-reference.md) - State management

## Error Message Quick Reference {important}

### Media-Specific Errors
| Error | Field | Cause | Solution |
|-------|-------|-------|----------|
| "Component not found" | Both | Wrong namespace/name | Check capitalisation |
| "Permission denied" | TakePhoto | Camera access denied | System settings |
| "Quota exceeded" | Both | IndexedDB full | Clear cache/data |
| Silent failure | FileUploader | Size/count limit | Check JSON parameters |
| "Cannot read property" | Both | Null initial value issue | Ensure null not [] |
| Memory warning | Both | Large files in memory | Reduce file sizes |
| Sync timeout | Both | Files too large | Limit to 50MB |

## Metadata {comprehensive}
- **Document Version**: v05 (consolidated)
- **Source Documents**: FileUploader.md, TakePhoto.md (Third Draft)
- **Platform Version**: Fieldmark v3 (January 2025)
- **Total Fields**: 2 (FileUploader, TakePhoto)
- **Key Limitations**: Required validation broken, no file type restrictions, silent failures
- **Security Level**: Trusted environments only
- **Performance Limits**: 50MB files, 20 photos maximum
- **Reference Docs**: 9 linked documents
---

## Related Documentation
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Location Fields](./location-fields-v05.md) | [#location-fields](#location-fields)
- **Next**: [Relationship Fields](./relationship-field-v05.md) | [#relationship-fields](#relationship-fields)

### Cross-Field Patterns
- **Validation**: [File Size Limits](../detail-crossfield-docs/validation.md#media-fields) | [#validation-patterns](#validation-patterns)
- **Platform Specific**: [Camera Access](../detail-crossfield-docs/patterns.md#platform-specific) | [#common-patterns](#common-patterns)

### Technical References
- **Platform Behaviors**: [Media Handling](../reference-docs/platform-behaviors-reference.md#media-fields) | [#platform-behaviors](#platform-behaviors)
- **Performance**: [Upload Limits](../reference-docs/performance-thresholds-reference.md#media-fields) | [#performance-thresholds](#performance-thresholds)
- **Security**: [File Validation](../reference-docs/security-considerations-reference.md#media-fields) | [#security-considerations](#security-considerations)

<!-- /concat:references -->
<!-- concat:boundary:end section="media-fields" -->
