# QRCodeFormField Documentation

## Overview

The QRCodeFormField delivers mobile-exclusive barcode scanning functionality through Google's ML Kit, supporting thirteen distinct barcode formats despite its nomenclature suggesting QR-only capability. This component transforms physical barcodes into digital data through a sophisticated ten-scan validation mechanism that ensures reading accuracy whilst operating without user feedback. The field's architecture prioritises data integrity through consecutive scan matching but provides no manual entry fallback, creating a binary operational model: successful scanning or no data entry. Web platform deployment renders the component entirely non-functional, displaying a disabled interface that critically breaks form validation when marked as required. The scanner captures raw decoded values without transformation capabilities, necessitating external processing for substring extraction or format modification.

## Common Use Cases

- **Heritage asset tagging** – Scanning pre-printed inventory barcodes on artefacts, buildings, or equipment
- **Specimen identification** – Reading laboratory-generated labels on collection bags or sample containers
- **Chain of custody tracking** – Capturing custody transfer codes for archaeological materials
- **Equipment checkout systems** – Processing asset tags on field equipment or tools
- **Pre-printed form correlation** – Linking paper context sheets to digital records via barcode
- **Batch processing workflows** – Rapid entry of multiple pre-labelled items
- **Museum accession integration** – Connecting to existing cataloguing systems via barcode
- **Site grid reference** – Scanning pre-deployed location markers for spatial documentation

## Core Configuration

### Required Parameters

```json
{
  "component-namespace": "qrcode",
  "component-name": "QRCodeFormField",
  "type-returned": "faims-core::String"
}
```

### Optional Parameters

```json
{
  "component-parameters": {
    "label": "Scan Barcode",
    "name": "barcode-field",
    "helperText": "Position barcode within frame",
    "fullWidth": true
  },
  "validationSchema": [["yup.string"]],
  "initialValue": "",
  "meta": {
    "annotation": {"include": true, "label": "scan notes"},
    "uncertainty": {"include": false}
  }
}
```

### Critical Configuration Warning

Never configure QRCodeFormField with required validation as this renders forms unsubmittable on web platforms:

```json
// BREAKS WEB COMPATIBILITY - DO NOT USE
"validationSchema": [["yup.required"]]
```

## Validation Rules

| Validation Type | Configuration | Platform Impact | Error Behaviour |
|-----------------|---------------|-----------------|-----------------|
| String type | `["yup.string"]` | All platforms | Base validation, always succeeds |
| Required | `["yup.required"]` | **BREAKS WEB FORMS** | Web users cannot submit form |
| Pattern match | `["yup.matches", "pattern"]` | Validates scanned result | Applies to decoded value only |
| Min length | `["yup.minLength", n]` | Checks decoded string | Validation after successful scan |
| Max length | `["yup.maxLength", n]` | Checks decoded string | Validation after successful scan |

### Validation Limitations
- No barcode-specific validation beyond basic string patterns
- No application-level checksum verification (ML Kit validates internally but silently rejects invalid codes)
- No format enforcement or type restrictions (accepts all 13 supported formats)
- No transformation before validation (raw value validated)
- Web platform cannot satisfy required validation
- Invalid barcodes simply fail to scan rather than producing validation errors

## Display Behaviour

### Mobile Rendering (iOS/Android)

**Active State:**
- Material-UI outlined button labelled with field label
- Tap initiates camera permission request (first use)
- Opens full-screen camera interface upon permission grant
- Displays viewfinder with targeting overlay
- Shows "Stop Scan" button during scanning
- No progress indicator for 10-scan requirement
- Returns to button after successful capture or cancellation

**Permission Denied State:**
- Disabled button (greyed, opacity ~0.38)
- Platform-specific instruction text below button
- No retry mechanism without page reload

**Value Display:**
- Shows decoded text as read-only after successful scan
- Cannot be edited or modified manually

### Desktop/Web Rendering

**Permanent Disabled State:**
```
[Label Text]
[─ Disabled Button ─] (Greyed out, non-interactive)
"Scanning not supported in browsers, mobile only"
{}  (Empty value or previous data)
```

**Styling:**
- MUI disabled button with standard opacity reduction
- Static message immediately visible on page load
- No user interaction possible
- No console errors or warnings generated

## Interaction Patterns

### Scanning Process Flow

The component implements a stringent ten-scan validation protocol without user visibility:

1. **Initiation** – User taps scan button (mobile only)
2. **Permission Check** – System requests camera access if not previously granted
3. **Camera Activation** – Full-screen viewfinder opens with targeting overlay
4. **Detection Loop** – ML Kit continuously attempts barcode detection
5. **Validation Sequence** – Upon first detection, begins counting identical scans:
   - Scan 1: Stores detected value, counter = 1
   - Scans 2-9: If identical, increment counter; if different, reset to 1 with new value
   - Scan 10: If identical to previous 9, accepts value and closes scanner
6. **Value Storage** – Raw decoded string stored without modification
7. **Display Update** – Field shows captured value as read-only text

### Failure Scenarios

**Infinite Scanning Loop Conditions:**
- Multiple barcodes visible causing alternating detections
- Damaged barcode producing inconsistent reads
- Poor lighting creating intermittent detection
- User unaware of 10-scan requirement, moving device prematurely

**Recovery Procedure:**
1. Tap "Stop Scan" to exit scanner
2. Identify and resolve issue (clean barcode, improve lighting, isolate single code)
3. Retry scanning process

### Permission Denial Recovery

**Critical Limitation:** No in-app permission recovery mechanism exists.

**User must:**
1. Navigate to system settings manually
2. Enable camera permission for Fieldmark
3. Close and restart application or reload page
4. Attempt scanning again

## Conditional Logic Support

Standard conditional display rules apply with platform-specific considerations:

```json
{
  "condition": {
    "field": "scan-method",
    "operator": "equal",
    "value": "barcode"
  }
}
```

### Platform Detection Limitations

Platform detection through field configuration is not currently possible. Whilst the system contains platform detection capabilities internally (Capacitor.getPlatform()), no _PLATFORM system variable exists for field access. Designers must employ manual workarounds:

```json
{
  "platform-check": {
    "component-name": "Select",
    "options": ["mobile", "web"],
    "label": "Select your platform",
    "helperText": "Choose mobile if using iOS/Android app"
  },
  "scanner": {
    "component-name": "QRCodeFormField",
    "condition": {
      "field": "platform-check",
      "operator": "equal",
      "value": "mobile"
    }
  }
}
```

**Note:** This relies on user selection accuracy. Automatic platform detection would require codebase modification to expose _PLATFORM as a system variable.

## Data Storage and Export

### Storage Format
- **Type**: Plain string (faims-core::String)
- **Content**: Exact decoded barcode value without modification
- **Encoding**: UTF-8 text
- **Metadata**: No barcode format type stored
- **Persistence**: Maintains value across sessions if form saved

### Export Behaviour
- Exports as plain text string in JSON/CSV
- No indication of scanning vs manual entry (if paired with TextField)
- No timestamp of scan capture
- No barcode format metadata

### Transformation Limitations
The component stores raw decoded values without transformation options:
- Cannot extract substrings from composite barcodes
- Cannot add prefixes or suffixes
- Cannot parse JSON/XML encoded in barcodes
- Cannot normalise format variations

## Common Patterns

### Pattern 1: Basic Mobile-Only Scanning

```json
{
  "specimen-barcode": {
    "component-namespace": "qrcode",
    "component-name": "QRCodeFormField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Specimen Barcode",
      "name": "specimen-barcode",
      "helperText": "Scan label on specimen bag"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
*Expected behaviour:* Mobile users can scan; web users see disabled interface. Field remains optional.

### Pattern 2: Paired Scanner with Manual Entry (Recommended)

```json
{
  "artefact-id-scan": {
    "component-namespace": "qrcode",
    "component-name": "QRCodeFormField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Scan Artefact Tag",
      "name": "artefact-id-scan",
      "helperText": "Use mobile scanner for barcode"
    },
    "initialValue": ""
  },
  "artefact-id-manual": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Or Enter Artefact ID Manually",
      "name": "artefact-id-manual",
      "helperText": "Type ID if scanner unavailable"
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.matches", "^[A-Z]{3}-\\d{4}-\\d{3}$", "Format: ABC-2024-001"]
    ]
  }
}
```
*Expected behaviour:* Provides fallback for web users and scan failure scenarios. Requires data reconciliation logic.

### Pattern 3: Heritage Site Grid Reference

```json
{
  "grid-square": {
    "component-namespace": "qrcode",
    "component-name": "QRCodeFormField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Scan Grid Marker",
      "name": "grid-square",
      "helperText": "Scan QR code on grid stake"
    },
    "meta": {
      "annotation": {
        "include": true,
        "label": "marker condition"
      }
    }
  },
  "manual-grid": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Grid Reference (if marker damaged)",
      "name": "manual-grid",
      "helperText": "Format: [Letter][Number] e.g., A1, B2"
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.matches", "^[A-Z]\\d{1,2}$", "Invalid grid reference"]
    ]
  }
}
```
*Expected behaviour:* Handles common field scenario of damaged markers whilst maintaining data structure consistency.

### Pattern 4: Multi-Format Equipment Tracking

```json
{
  "equipment-scan": {
    "component-namespace": "qrcode",
    "component-name": "QRCodeFormField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Scan Equipment Tag",
      "name": "equipment-scan",
      "helperText": "Accepts QR, Code128, or DataMatrix"
    }
  },
  "equipment-type": {
    "component-namespace": "formik-material-ui",
    "component-name": "Select",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Equipment Category",
      "name": "equipment-type"
    },
    "options": ["GPS Unit", "Camera", "Drone", "Total Station", "Other"]
  },
  "checkout-notes": {
    "component-namespace": "formik-material-ui",
    "component-name": "MultilineTextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Condition Notes",
      "name": "checkout-notes",
      "rows": 3
    }
  }
}
```
*Expected behaviour:* Leverages multi-format scanning capability for mixed equipment labelling systems.

## Troubleshooting Guide

| Issue | Symptoms | Cause | Solution |
|-------|----------|-------|----------|
| Scanner won't complete | Continuous scanning without capture | 10-scan validation not achieved | Ensure single barcode visible, hold steady 3-4 seconds |
| Infinite scanning | Scanner runs indefinitely | Multiple barcodes visible OR damaged code | Isolate single barcode, clean if dirty |
| Permission denied | Button disabled with error text | Camera access blocked | Settings > Apps > Fieldmark > Permissions > Camera > Enable, then reload app |
| Web form won't submit | Validation error on web browser | QRCodeFormField marked required | Remove required validation or implement manual entry field |
| No manual entry | Cannot type barcode value | Component lacks text input | Add separate TextField for manual entry |
| Empty value after scan | Field remains blank post-scanning | Scan cancelled or validation reset | Retry with steady hand, ensure 10 identical reads |
| Platform incompatibility | Feature unavailable message | Accessing via web browser | Use mobile app or provide alternative input method |
| Partial barcode reads | Inconsistent scanning results | Damaged or dirty barcode | Clean barcode, improve lighting, consider manual entry |

### Debug Checklist

When scanner fails to capture:
- [ ] Check single barcode visible in frame
- [ ] Verify adequate lighting (no glare or shadows)
- [ ] Clean barcode surface if dirty
- [ ] Hold device steady for 3-4 seconds
- [ ] Confirm camera permission granted
- [ ] Reload page if permission recently enabled
- [ ] Test with different barcode if available
- [ ] Verify barcode format is supported (13 types)
- [ ] Check for multiple barcodes causing resets
- [ ] Consider manual entry alternative

## Implementation Notes

The QRCodeFormField's architecture reflects a fundamental tension between data integrity and user experience. The ten-scan validation mechanism ensures exceptional accuracy in challenging field conditions but operates without user feedback, creating opacity in the scanning process. The component's inability to provide manual entry necessitates careful form design considering platform deployment contexts.

Critical implementation considerations:
- **Platform Strategy**: Design separate mobile and web form variants, use progressive disclosure (e.g., 'I am using a mobile device' [yes/no]), or pair with TextField
- **Validation Design**: Never use required validation due to web incompatibility
- **Error Recovery**: Implement comprehensive fallback patterns for permission denial and scan failure
- **User Training**: Document the hidden 10-scan requirement for field teams
- **Data Processing**: Plan for external value transformation if substring extraction needed

The component name "QRCodeFormField" constitutes a misnomer – the scanner processes thirteen barcode formats with equal capability, potentially confusing developers expecting QR-specific functionality.

## Best Practices

- **Consider pairing with TextField** for manual entry fallback across all platforms
- **Never mark as required** to maintain web platform compatibility
- **Document scanning requirements** explicitly for end users (steady hold, single barcode)
- **Employ manual platform selection** if conditional display needed (automatic detection unavailable)
- **Design recovery workflows** for permission denial and scan failure scenarios
- **Test on all target platforms** during development to identify compatibility issues
- **Provide clear helper text** indicating mobile-only functionality
- **Consider value transformation needs** early – implement TemplatedStringField for processing
- **Plan data reconciliation** when using paired scanner/manual fields
- **Train field teams** on 10-scan requirement and troubleshooting procedures

## See Also

- **TextField** – Essential pairing for manual entry fallback
- **TemplatedStringField** – For adding prefixes or combining scanned values
- **Select** – Alternative for known finite barcode sets
- **Conditional Logic** – Managing platform-specific field display
- **Platform Considerations** – Broader mobile/web compatibility documentation
- **Validation Rules** – Understanding validation cascade impacts
- **MultilineTextField** – For extensive manual data entry scenarios