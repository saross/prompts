# Media Fields - Fieldmark v3 Documentation

## Overview {essential}

### DESIGNER QUICK GUIDE
**Media Capture Fields Available:**
- **FileUploader** → Upload any existing files from device
- **TakePhoto** → Capture photos using device camera

**Component Namespace:** Always `"faims-custom"` for both fields
**Component Names:** Case-sensitive - `FileUploader`, `TakePhoto`
**Return Type:** Both return `faims-attachment::Files` arrays
**Designer Support:** Full support for basic configuration, JSON required for file constraints

### CRITICAL NAMING DISAMBIGUATION
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
- Required validation visual only (asterisk) without JSON enhancement
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
See [Validation Timing Reference](../reference-docs/validation-timing-reference.md) for universal behavior.

**Media-Specific Validation:**
- **File type validation:** Selection time (TakePhoto only)
- **Size validation:** Silent rejection (FileUploader)
- **Required validation:** Broken for both fields without JSON
- **Count validation:** Via yup schema only
- **Content validation:** Not performed
- **Async validation:** Not supported during upload

### Platform Behaviors {important}

**iOS Specific:**
- HEIC→JPEG automatic conversion
- Combined camera/photo permissions
- ProRAW/Live Photos metadata lost
- Settings navigation varies by version

**Android Specific:**
- Storage Access Framework (no permissions)
- Manufacturer camera apps vary
- Direct JPEG capture
- Scoped storage compatible (10+)

**Web Platform:**
- MediaDevices API or file input fallback
- No GPS coordinate access
- EXIF stripped on capture
- IndexedDB storage limits apply

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

### Silent Failures Diagnostic
**FileUploader Silent Rejections:**
1. Check `maximum_file_size` vs actual file
2. Verify `maximum_number_of_files` not exceeded
3. Confirm `minimum_file_size` met
4. Add explicit limits to helper text

**TakePhoto Performance Issues:**
1. Count existing photos in field
2. Check available device storage
3. Monitor browser memory usage
4. Verify IndexedDB quota available

### Validation Not Working
```json
// FileUploader - Required validation broken
"validationSchema": [["yup.mixed"]]  // Cannot validate arrays

// TakePhoto - Manual validation required
"validationSchema": [
  ["yup.array"],
  ["yup.required", "Photos required"]  // Add manually
]
```

### Platform Permission Recovery
- **iOS:** Settings → Privacy → Camera → [App Name]
- **Android:** Settings → Apps → [App] → Permissions
- **Web:** Reload page and accept permission prompt

## JSON Examples {comprehensive}

### Mixed Media Documentation
```json
{
  "excavation-media": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Excavation Media",
      "name": "excavation-media",
      "helperText": "Upload photos, videos, plans (max 25MB each, up to 10 files)",
      "advancedHelperText": "## Accepted Files\n\n**Images:** JPG, PNG, TIFF\n**Video:** MP4, MOV\n**Documents:** PDF plans, CSV data\n\nFiles over 25MB will be silently rejected.",
      "multiple": true,
      "maximum_file_size": 26214400,
      "maximum_number_of_files": 10,
      "minimum_file_size": 100
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null,
    "condition": {
      "operator": "equal",
      "field": "excavation-complete",
      "value": "yes"
    }
  }
}
```

### Staged Photography Workflow
```json
{
  "before-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Before Excavation",
      "name": "before-photos",
      "helperText": "Document initial conditions (2-5 photos)",
      "required": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.required", "Before photos required"],
      ["yup.min", 2, "Minimum 2 photos"],
      ["yup.max", 5, "Maximum 5 photos"]
    ],
    "initialValue": null
  },
  "after-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "After Excavation",
      "name": "after-photos",
      "helperText": "Document final state (2-5 photos)",
      "required": true
    },
    "validationSchema": [
      ["yup.array"],
      ["yup.required", "After photos required"],
      ["yup.min", 2, "Minimum 2 photos"],
      ["yup.max", 5, "Maximum 5 photos"]
    ],
    "initialValue": null,
    "condition": {
      "operator": "is-truthy",
      "field": "before-photos"
    }
  }
}
```

## Migration and Best Practices {comprehensive}

### Migration from FAIMS2
- FAIMS2 file attachments → Use FileUploader
- FAIMS2 camera → Use TakePhoto
- File type restrictions → Not available, use helper text
- Progress indicators → Not available, inform users
- Batch operations → Configure `multiple: true`

### Performance Best Practices
1. **FileUploader:** Limit individual files to 50MB
2. **TakePhoto:** Maximum 20 photos per field
3. **Total per record:** Keep under 200MB combined
4. **Helper text:** Always specify size/count limits
5. **Sync strategy:** Disable "Get attachments" for bandwidth
6. **Storage monitoring:** Check device space before fieldwork

### Security Best Practices
1. **Deployment:** Trusted research teams only
2. **Documentation:** List acceptable file types
3. **Monitoring:** Review uploads regularly
4. **Server validation:** Implement if public-facing
5. **Storage limits:** Set maximum sizes via JSON

## Field Quirks Index (2025-01) {comprehensive}

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

## JSON Patterns Cookbook (2025-01) {comprehensive}

### Pattern: Conditional Media Requirements
```json
{
  "damage-photos": {
    "component-namespace": "faims-custom",
    "component-name": "TakePhoto",
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

## Quick Diagnosis Tables (2025-01) {important}

### Media Field Issues Diagnosis
| Symptom | Field | Likely Cause | Quick Fix |
|---------|-------|--------------|-----------|
| Field not rendering | Both | Wrong namespace | Use `faims-custom` |
| Files disappearing | FileUploader | Size limit exceeded | Check maximum_file_size |
| Can't require field | Both | Validation broken | Add yup.required manually |
| No camera option | FileUploader | Wrong field type | Use TakePhoto instead |
| No GPS coordinates | TakePhoto | Web platform | Use native app |
| Slow form | TakePhoto | Too many photos | Limit to 20 maximum |
| Upload fails | Both | Network timeout | Check file sizes |

## Field Interaction Matrix (2025-01) {important}

### Media Fields with Other Field Types
| Field Combination | Interaction | Common Pattern |
|------------------|-------------|----------------|
| FileUploader + TakePhoto | Independent | Mixed media workflows |
| TakePhoto + TakePoint | Complementary | Photo with GPS reference |
| FileUploader + Select | Categorization | Document type selection |
| TakePhoto + Annotation | Metadata | Photo descriptions |
| FileUploader + TextField | Description | File source notes |
| Media + TemplatedString | Identification | Generate file identifiers |

## Migration Warnings Index (2025-01) {comprehensive}

### Critical Migration Issues
1. **Required validation breaks** when moving to Fieldmark
2. **File type restrictions** not available (FAIMS2 had MIME filtering)
3. **Progress indicators** removed in current version
4. **EXIF preservation** not possible (stripped on upload)
5. **Bulk operations** require manual configuration
6. **Performance limits** more restrictive than FAIMS2
7. **Orphaned attachments** accumulate without cleanup

## See Also {comprehensive}
- **Text Fields**: For detailed media descriptions
- **Number Fields**: For GPS coordinate manual entry
- **Select Fields**: For media categorization
- **Location Fields**: For precise georeferencing
- **Reference Documents:**
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