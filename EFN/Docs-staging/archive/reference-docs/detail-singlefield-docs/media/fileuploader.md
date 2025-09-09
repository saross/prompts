# FileUploader Field – Third Draft Documentation

## Overview

The FileUploader field provides comprehensive file attachment capabilities within Fieldmark notebooks, accepting any file type without restriction whilst offering optional size and quantity constraints configurable exclusively through JSON. This component implements a web-standard approach through React Dropzone, maintaining platform consistency via HTML file input elements rather than native APIs – a deliberate architectural decision that prioritises simplicity over platform-specific optimisation. The field's 211-line implementation operates as a temporary file accumulator, maintaining selected files in component state until form submission triggers PouchDB synchronisation, at which point files transform into `faims-attachment::Files` data structures compatible with Fieldmark's broader attachment architecture. Unlike the functionally similar TakePhoto field, FileUploader neither modifies file content nor implements security controls, accepting executables, scripts, and potentially problematic files without validation – a design philosophy that presumes deployment within trusted research environments with vetted team members.

## Common Use Cases

Deploy FileUploader when requiring:
- **Pre-existing document attachment** – Permits, contracts, maps, protocols, or reference materials essential to field documentation
- **Professional media integration** – DSLR photographs, drone footage, audio recordings, or video files from dedicated equipment
- **Heterogeneous file collections** – Mixed document types (PDFs, spreadsheets, images) within single fields
- **Original format preservation** – Files requiring unmodified storage with intact metadata and structure
- **Unpredictable file types** – Research contexts where file format requirements cannot be predetermined
- **Batch file operations** – Multiple file selection and upload within single interaction sequences
- **Cross-platform document sharing** – Files requiring access across diverse devices and operating systems

Avoid FileUploader when:
- **Security controls are essential** – Public-facing deployments or untrusted user contexts requiring virus scanning or MIME restrictions
- **Immediate photo capture needed** – Use TakePhoto for integrated camera workflows with GPS injection
- **Large files expected** – Individual files exceeding 50MB or collections surpassing 100MB risk performance degradation
- **Required validation crucial** – Current implementation cannot enforce mandatory file uploads reliably
- **User feedback essential** – Silent constraint violations create poor user experience without custom mitigation
- **Storage quotas limited** – No awareness of device or server storage limitations

## Core Configuration

### Required Configuration
```json
{
  "component-namespace": "faims-custom",
  "component-name": "FileUploader",
  "type-returned": "faims-attachment::Files"
}
```

### Optional Parameters
```json
{
  "component-parameters": {
    "label": "Supporting Documents",              // Field label display
    "name": "supporting-docs",                    // Internal identifier
    "id": "supporting-docs-field",                 // Field ID
    "helperText": "Upload permits and maps",      // Guidance text
    "advancedHelperText": "## Extended Help\n...", // Markdown help via BaseFieldEditor
    "required": false,                            // Visual indicator only (validation broken)
    "multiple": true,                             // JSON-only: Allow multiple files
    "maximum_file_size": 52428800,                // JSON-only: 50MB limit in bytes
    "minimum_file_size": 1024,                    // JSON-only: 1KB minimum in bytes
    "maximum_number_of_files": 10                 // JSON-only: Maximum 10 files
  },
  "validationSchema": [                           // Default permits null/empty
    ["yup.mixed"]
  ],
  "initialValue": null,                           // Always null, not empty array
  "meta": {
    "annotation": {
      "include": true,
      "label": "Document notes"
    },
    "uncertainty": {
      "include": false,
      "label": "Quality concerns"
    }
  }
}
```

**Critical limitations**: Parameters `multiple`, `maximum_file_size`, `minimum_file_size`, and `maximum_number_of_files` remain **inaccessible through Designer** – JSON editing required for file-specific constraints.

## Validation Rules

| Rule | Configuration | Actual Behaviour | Error Message |
|------|--------------|------------------|---------------|
| Required field | `"required": true` in parameters | **Non-functional** – visual indicator only | None |
| Required validation | `["yup.required"]` in schema | **Broken** – `yup.mixed()` cannot validate arrays | None displayed |
| Maximum file size | `"maximum_file_size": bytes` | Silent rejection via Dropzone | **None – silent failure** |
| Minimum file size | `"minimum_file_size": bytes` | Silent rejection via Dropzone | **None – silent failure** |
| Maximum file count | `"maximum_number_of_files": n` | Silent rejection when exceeded | **None – silent failure** |
| File type restriction | Not available | Cannot restrict MIME types or extensions | N/A |
| Custom validation | Schema supports syntax | Implementation non-functional | Messages never display |

**Warning**: All constraint violations occur silently without user feedback. Files exceeding limits simply disappear without explanation. Helper text must explicitly communicate all constraints as the interface provides no violation feedback.

## Display Behaviour

### Desktop (Web Browser)
- **Drag-and-drop zone**: Dashed border with hover state colour change
- **Click-to-select**: Standard OS file dialogue via HTML input element
- **File list display**: Reverse chronological order (newest first)
- **Image previews**: Thumbnails (300×200px max) for browser-supported formats
- **Non-image display**: File icon with name and MIME type
- **Delete functionality**: Trash icon per file with confirmation dialogue
- **No count indicators**: Current/maximum files not displayed
- **No progress feedback**: Static interface during all operations

### iOS (Native App)
- **File selection**: iOS document picker accessing iCloud Drive, local storage, third-party apps
- **Drag-and-drop**: Not supported – tap-to-select only
- **Preview limitations**: HEIC images may not render in browser view
- **iCloud behaviour**: Files download transparently but lose cloud reference
- **No camera integration**: Unlike TakePhoto, no direct camera access
- **Storage permissions**: None required – system handles via document picker

### Android (Native App)
- **File selection**: Storage Access Framework without explicit permissions
- **Modern Android (10+)**: Scoped storage compatible
- **File access**: Any user-browsable location accessible
- **Preview support**: Depends on WebView capabilities
- **Platform files**: APK files accepted without warning
- **No optimisations**: Generic file picker without recent files or shortcuts

## Interaction Patterns

### File Selection Flow
1. User clicks dropzone or drags files (desktop only)
2. Platform file selector opens with all files visible
3. Files selected (single or multiple based on configuration)
4. Dropzone validates against size/count constraints
5. Violating files silently rejected without feedback
6. Accepted files appear in reverse-order list
7. Thumbnails generate for images; icons for other types

### File Removal Flow
1. User clicks delete icon on file entry
2. Confirmation dialogue: "Are you sure you want to delete this photo?"
3. Confirmation removes file from array immediately
4. No undo capability after deletion
5. Array index recalculated accounting for reverse display

### Memory Management Issues
- Files held as Blobs in component state
- Object URLs created via `URL.createObjectURL()` but never released
- Memory accumulates until page refresh
- No persistence across browser sessions
- Form submission triggers PouchDB storage

## Conditional Logic Support

FileUploader supports standard Fieldmark conditional logic through Designer configuration:
- **Visibility conditions**: Show/hide based on other field values
- **Conditional requirement**: Make required based on conditions (though validation remains broken)
- **Complex logic**: AND/OR combinations via Designer interface

Limitations:
- Cannot dynamically adjust file constraints based on conditions
- Cannot reference other fields for parameter values
- Static configuration only – no runtime parameter changes

## Data Storage and Export

### Storage Pipeline
1. **Component state**: Files as Blob objects in memory
2. **Form submission**: Blobs convert to attachment documents
3. **Attachment ID**: `att-{uuid}` format with original filename preserved
4. **PouchDB storage**: Base64 encoding with ~33% size overhead
5. **Synchronisation**: Complete document upload without chunking
6. **Server storage**: CouchDB maintains identical structure

### Export Transformation
- **Storage name**: `att-3f2a1b8c-4d5e-6f7a` (UUID)
- **Export name**: `{fieldname}/{hrid}-{fieldname}.{extension}`
- **Example**: `permits/SITE001-permits.pdf`
- **Duplicates**: Append `*1`, `*2` suffixes
- **CSV format**: Multiple files semicolon-separated in cell
- **Unknown types**: Default to `.dat` extension

### Critical Storage Issues
- No cascade deletion – orphaned attachments accumulate
- No garbage collection mechanism
- No direct API access to individual files
- Memory inefficient base64 encoding
- Export destroys original filename references

## Common Patterns

### Example 1: Heritage Site Documentation
```json
{
  "heritage-permits": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Heritage Permits and Approvals",
      "name": "heritage-permits",
      "id": "heritage-permits",
      "helperText": "Upload PDF permits, approval letters, and compliance certificates (max 10MB each, up to 5 files)",
      "required": false,
      "multiple": true,
      "maximum_file_size": 10485760,
      "maximum_number_of_files": 5
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "Permit details and restrictions"
      }
    }
  }
}
```

### Example 2: Archaeological Survey Media
```json
{
  "survey-media": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Survey Documentation",
      "name": "survey-media",
      "helperText": "Maps, drone footage, DSLR photos, or GIS exports",
      "advancedHelperText": "## File Guidelines\n\n- Maximum 50MB per file\n- Unlimited number of files\n- All formats accepted\n- Original filenames preserved until export",
      "multiple": true,
      "maximum_file_size": 52428800
    },
    "validationSchema": [["yup.mixed"]],
    "initialValue": null
  }
}
```

### Example 3: Single Document Upload
```json
{
  "site-report": {
    "component-namespace": "faims-custom",
    "component-name": "FileUploader",
    "type-returned": "faims-attachment::Files",
    "component-parameters": {
      "label": "Final Site Report",
      "name": "site-report",
      "helperText": "Upload single PDF report (required)",
      "required": true,
      "multiple": false,
      "maximum_number_of_files": 1,
      "minimum_file_size": 1024
    },
    "validationSchema": [
      ["yup.mixed"],
      ["yup.required", "Site report is mandatory"]
    ],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "Report version and status"
      }
    }
  }
}
```
**Note**: Required validation non-functional despite configuration.

## Troubleshooting Guide

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Files disappear after selection | Silent size/count constraint violation | Add explicit constraints to helper text |
| Required validation not working | `yup.mixed()` cannot validate file arrays | Use helper text to indicate requirement |
| Large files crash browser | Memory exhaustion from Blob storage | Limit individual files to <50MB |
| Files lost on page refresh | No persistence before form submission | Save form frequently during data entry |
| No upload progress shown | Missing progress indicators | Inform users uploads occur at submission |
| Conflicting size parameters | `min > max` creates impossible constraint | Verify parameter logic before deployment |
| Platform files incompatible | HEIC/proprietary formats accepted | Document acceptable formats in helper text |
| Attachments not syncing | "Get attachments" toggle disabled | Enable in notebook settings (affects all) |

### Debug Checklist
- [ ] Verify `maximum_file_size` > `minimum_file_size`
- [ ] Check browser console for Blob/quota errors
- [ ] Confirm files under 50MB individual size
- [ ] Test with "Get attachments" enabled
- [ ] Monitor browser memory usage during selection
- [ ] Verify IndexedDB quota availability
- [ ] Check network stability for sync operations
- [ ] Review PouchDB sync logs for failures

## Implementation Notes

### Technical Constraints
- **No security controls**: Accepts any file type including executables without validation
- **Memory leaks**: Object URLs created but never released (`revokeObjectURL` missing)
- **Silent failures**: All constraint violations occur without user notification
- **Broken validation**: Required field validation non-functional
- **No chunking**: Large files upload as monolithic base64 documents
- **Performance threshold**: ~50MB before noticeable degradation, ~200MB risks crashes

### Designer vs JSON Configuration
- **Designer provides**: All standard field options via BaseFieldEditor (labels, helpers, annotations, conditions)
- **JSON exclusive**: File-specific parameters (`multiple`, size limits, count limits)
- **Migration trigger**: Need for file constraints requires JSON editing
- **Parity with TakePhoto**: Both media fields use identical Designer configuration

### Architectural Context
- Completely independent from TakePhoto despite similar syntax
- Uses React Dropzone vs TakePhoto's Capacitor Camera
- Web-standard implementation vs native-first approach
- No shared code or abstraction between media fields
- Storage backend identical but processing differs

## Best Practices

### File Size Management
- **Individual files**: Limit to 20–50MB maximum
- **Total per field**: Keep under 100MB combined
- **Per record total**: Avoid exceeding 200MB
- **Helper text**: Always specify size limits explicitly
- **Alternative storage**: Consider external links for large files

### User Communication
- Document all constraints in helper text (size, count, format)
- Explain that files upload during form submission, not immediately
- Warn about page refresh data loss risk
- Clarify that deletion is permanent without undo
- Note that file order displays newest first

### Security Considerations
- Deploy only within trusted research teams
- Avoid public-facing or untrusted user contexts
- Document acceptable file types in helper text
- Consider server-side validation if security critical
- Monitor for unusual file uploads regularly

### Performance Optimisation
- Limit concurrent FileUploader instances
- Save forms frequently to prevent memory accumulation
- Restart browser sessions after extensive uploads
- Enable "Get attachments" selectively for bandwidth management
- Consider TakePhoto for image-specific workflows

## See Also

### Related Fields and Dependencies

**Required Companion Fields**: None – FileUploader operates independently without mandatory field dependencies

**Common Field Pairings**:
- **TakePhoto**: Frequently paired for mixed media workflows where both camera capture and document upload are needed (e.g., site photos via camera plus drone footage via upload)
- **TextField/MultilineTextField**: Paired to capture file descriptions, source attribution, or processing notes that annotation fields cannot accommodate
- **Select/RadioGroup**: Used together to categorise uploaded file types (e.g., "Document Type" select field determining expected file formats)
- **DateTimeNow**: Paired to timestamp when files were collected or uploaded, providing temporal context
- **TakePoint**: Combined for georeferenced documentation (location where documents were collected)
- **TemplatedStringField**: Used to generate systematic identifiers for uploaded files based on other field values

**Mutual Exclusions**: None identified – FileUploader coexists with all field types

**Validation Cascades**: FileUploader's validation state does not affect other fields due to broken required validation. Even when marked required, empty FileUploader fields do not prevent form submission

**Fields Dependent on FileUploader**: None – No fields reference or depend on FileUploader values. The architectural isolation means FileUploader cannot trigger conditional logic in other fields

### Architectural Relationships
- Independent implementation from TakePhoto despite functional overlap
- No dynamic field coordination or conditional parameter adjustment
- Annotation support provides field-level (not file-level) metadata
- Multiple instances possible but create fragmented experiences
- Cannot be referenced by other fields for conditional behaviour
- Does not participate in form-wide validation cascades

---

*Documentation version: Third Draft  
Technical basis: Component version as of January 2025  
Critical limitations documented for research team awareness*