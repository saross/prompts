# TakePoint Field – Complete Third-Draft Documentation

## Overview

The TakePoint field provides single-tap GPS coordinate capture through device geolocation services, returning GeoJSON Feature objects enriched with accuracy metadata and optional positional attributes. This field type implements streamlined coordinate acquisition without visual map interface, prioritising capture efficiency over spatial precision refinement. Unlike MapFormField's interactive geometry creation, TakePoint executes immediate position capture using the device's current GPS reading within a configurable timeout window. The field's implementation through Capacitor's Geolocation API ensures cross-platform consistency whilst accessing native GPS capabilities, though with significant limitations: no accuracy threshold enforcement, no user feedback during acquisition, and misleading precision display that suggests nanometre accuracy when actual uncertainty may exceed 50 metres. The returned `faims-pos::Location` structure incorporates coordinates plus temporal, altitudinal, and kinematic metadata where available, though platform inconsistencies mean these auxiliary fields frequently return null.

## Common Use Cases

- **Find spot documentation** – Recording GPS coordinates where artefacts or features are discovered
- **Sample point collection** – Capturing locations of soil samples, botanical specimens, or geological observations  
- **Waypoint marking** – Recording sequential points along survey transects or walking routes
- **Control point establishment** – Setting reference locations for site grids or excavation areas
- **Photo location tagging** – Documenting where photographs were taken for later GIS integration
- **Rapid traverse mapping** – Quick coordinate capture at regular intervals without visual confirmation
- **Emergency position recording** – Fast location capture in situations requiring immediate documentation
- **Backup location method** – Alternative when MapFormField base maps unavailable or cached tiles exhausted

## Core Configuration

### Required Parameters

```json
{
  "component-namespace": "faims-custom",
  "component-name": "TakePoint",
  "type-returned": "faims-pos::Location",
  "component-parameters": {
    "name": "take-gps-point",
    "id": "take-gps-point",
    "label": "GPS Location"
  }
}
```

### Optional Parameters

```json
{
  "component-parameters": {
    "helperText": "Click to save current location",
    "fullWidth": true,
    "enableHighAccuracy": true,
    "timeout": 10000,
    "maximumAge": 0,
    "required": false
  },
  "validationSchema": [["yup.object"], ["yup.nullable"]],
  "initialValue": null,
  "meta": {
    "annotation": {
      "include": true,
      "label": "GPS quality notes"
    },
    "uncertainty": {
      "include": true,
      "label": "location uncertain"
    }
  }
}
```

### GPS-Specific Parameters

| Parameter | Type | Default | Description | Limitations |
|-----------|------|---------|-------------|-------------|
| enableHighAccuracy | boolean | true | Requests best available GPS precision | No fallback to low accuracy |
| timeout | number | 10000 | Maximum milliseconds to wait for position | No user feedback during wait |
| maximumAge | number | 0 | Maximum age of cached position (ms) | 0 forces fresh reading always |

**Critical Missing Parameters**: No accuracy threshold, no retry attempts, no coordinate precision control, no format options, no continuous tracking, no validation of GPS quality.

## Validation Rules

### Built-in Validation

| Validation Type | Implementation | Effect | Platform Impact |
|-----------------|----------------|--------|-----------------|
| Type validation | `faims-pos::Location` | Accepts Feature objects | All platforms |
| Object validation | `["yup.object"]` | Ensures object type | All platforms |
| Nullable | `["yup.nullable"]` | Allows null during editing | All platforms |
| Required | Auto-added if `required: true` | Prevents null submission | All platforms |

### Configurable Validation

| Rule | Condition | Error Message | Platform Impact |
|------|-----------|---------------|-----------------|
| required | Field marked `required: true` | "This field is required" | All platforms |
| GPS timeout | Exceeds timeout parameter | "Timeout expired" / platform-specific | iOS: kCLErrorDomain; Android: "location unavailable" |
| Permission denied | User denies location access | OS permission error (varies) | iOS/Android: native dialog; Web: browser prompt |
| GPS unavailable | Location services disabled | "location unavailable" | All platforms, cryptic messages |

### What CANNOT Be Validated

| Missing Validation | Impact | Workaround | Platform Variance |
|-------------------|--------|------------|-------------------|
| Accuracy thresholds | Accepts 5m to 5000m | Manual check + annotation | None - all platforms affected |
| Coordinate bounds | No lat/lon range checking | Post-processing validation | None - all platforms affected |
| Metadata presence | Cannot require altitude/heading | Document platform limits | Web usually null; mobile varies |
| Temporal constraints | No timestamp validation | None available | All platforms affected |
| Precision limits | Shows 14+ decimals | Ignore extra decimals | All platforms show false precision |

## Display Behaviour

### Desktop Rendering
- **Button style**: Material-UI outlined variant, full width, primary color
- **Coordinate display**: Raw precision (14+ decimals) despite accuracy limitations
- **Format**: `Lat: -33.86881209472629; Long: 151.20930485726183; Acc: 10`
- **Metadata display**: Shows altitude/altitude_accuracy when available
- **Error display**: Raw error messages below button
- **Permission alert**: Red alert box for any error (misleadingly suggests permission issue)

### Mobile Rendering

#### iOS Behaviour
- **GPS precision**: Generally higher accuracy than Android
- **Metadata availability**: Altitude usually present on newer devices
- **Permission options**: "Allow Once", "Allow While Using App", "Don't Allow"
- **Error messages**: `"The operation couldn't be completed. (kCLErrorDomain error 1.)"`
- **Timeout behaviour**: Silent 10-second wait

#### Android Behaviour  
- **Permissions required**: Both ACCESS_FINE_LOCATION and ACCESS_COARSE_LOCATION
- **Metadata gaps**: Speed/heading often null unless moving
- **Error messages**: `"location unavailable"` for most failures
- **GPS quirks**: May need another app to "wake up" GPS after airplane mode

#### Web Behaviour
- **Limited metadata**: Altitude, speed, heading usually null
- **Browser prompts**: "[domain] wants to know your location"
- **Revocation**: Can revoke mid-session via browser settings
- **Accuracy**: Generally worse than mobile platforms

## Interaction Patterns

### Capture Workflow
1. User taps "Take Point" button
2. **No visual feedback for up to 10 seconds** (critical UX issue)
3. GPS acquisition attempts with high accuracy
4. On success: Coordinates display with excessive precision
5. On failure: Raw error message and misleading permission alert

### Multiple Captures
- **No debouncing** – Rapid taps create parallel GPS requests
- **Race conditions** – Last request to complete wins
- **No warm start benefit** – maximumAge=0 forces fresh reading
- **Battery drain** – Each tap is independent GPS activation

### Permission Flows
- **Initial prompt**: Platform-specific permission dialog
- **Denial handling**: Sets error state, shows permission alert
- **Recovery**: No automatic retry, user must tap again
- **"Allow Once" (iOS)**: Works for single capture only

## Conditional Logic Support

### Current Capabilities
- **Null checking**: Can test if location captured or not
- **Example**: `{"operator": "not-equal", "field": "site-location", "value": null}`

### Critical Limitations
- **Cannot access nested properties** – No accuracy checking
- **Cannot validate quality** – Can't branch on GPS accuracy
- **No coordinate bounds** – Can't check if within area
- **No metadata conditions** – Can't test altitude presence

### Workarounds
- Add manual checkbox "High accuracy GPS?" for conditional logic
- Use annotation field to document accuracy concerns
- Cannot implement quality-based workflow branching

## Data Storage and Export

### Storage Format
```json
{
  "type": "Feature",
  "properties": {
    "timestamp": 1699234567890,
    "altitude": 234.5,           // Often null
    "speed": 1.2,                 // Often null
    "heading": 45.6,              // Often null
    "accuracy": 8.3,
    "altitude_accuracy": 12.1    // Often null
  },
  "geometry": {
    "type": "Point",
    "coordinates": [151.20930485726183, -33.86881209472629]
  }
}
```

### CSV Export – MAJOR DATA LOSS
For field named "site-location":
- ✅ `site-location` – Full JSON string
- ✅ `site-location_latitude` – Number
- ✅ `site-location_longitude` – Number  
- ✅ `site-location_accuracy` – Number
- ❌ **NOT EXPORTED**: altitude, speed, heading, timestamp, altitude_accuracy

### JSONL Backup
- Preserves complete Feature object with all metadata
- No data loss during backup/restore cycle
- No native GeoJSON export despite storing GeoJSON Features

### Storage Impact
- ~500-600 bytes per location (including PouchDB overhead)
- Performance degradation at 1000-2000 points
- Sync handles up to 10,000 documents per cycle

## Common Patterns

### Example 1: Basic Location Capture
```json
{
  "site-gps": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Site Location",
      "name": "site-gps",
      "helperText": "Capture GPS coordinates"
    },
    "validationSchema": [["yup.object"], ["yup.nullable"]],
    "initialValue": null
  }
}
```
**Behaviour**: Single button tap, 10-second timeout, displays raw coordinates with 14+ decimal places.

### Example 2: Required High-Accuracy Capture
```json
{
  "control-point": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Control Point (Required)",
      "name": "control-point",
      "helperText": "Wait for accuracy < 10m before capturing",
      "timeout": 30000,
      "enableHighAccuracy": true,
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Control point GPS required"]
    ],
    "meta": {
      "annotation": {"include": true, "label": "accuracy notes"},
      "uncertainty": {"include": true, "label": "uncertain"}
    }
  }
}
```
**Note**: Cannot enforce 10m accuracy threshold. Users must manually check displayed accuracy and use annotation to document if accepting poor readings.

### Example 3: Rapid Waypoint Collection
```json
{
  "waypoint": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint", 
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Quick Waypoint",
      "name": "waypoint",
      "helperText": "Fast capture for traverse",
      "timeout": 5000,           // Reduced timeout for speed
      "maximumAge": 3000,         // Accepts 3-second cached positions
      "enableHighAccuracy": false // Trades accuracy for battery/speed
    }
  }
}
```
**Trade-off**: Accepts 3-second old cached positions and lower accuracy for speed. Still no accuracy validation.

### Example 4: Platform-Specific Web Configuration
```json
{
  "web-location": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Browser GPS",
      "name": "web-location",
      "helperText": "Note: Altitude/speed/heading unavailable in browsers",
      "timeout": 15000,           // Longer timeout for browser GPS
      "enableHighAccuracy": true, // Still request best available
      "required": false           // Optional due to browser limitations
    },
    "meta": {
      "annotation": {
        "include": true,
        "label": "browser limitations noted"
      }
    }
  }
}
```
**Platform consideration**: Web browsers rarely provide altitude/speed/heading. Longer timeout accounts for browser permission prompts. Annotation field essential for documenting platform limitations.

## Troubleshooting Guide

### Common Issues and Solutions

| Issue | Symptoms | Likely Cause | Solution |
|-------|----------|--------------|----------|
| No GPS signal | "location unavailable" error | Indoor/airplane mode | Move outside, disable airplane mode |
| Timeout errors | "Timeout expired" after 10s | Poor GPS reception | Increase timeout to 20-30 seconds |
| Permission errors | "Location access restricted" | Permission denied | Check device location settings |
| Excessive precision | 14+ decimal places shown | Precision/accuracy mismatch | Ignore extra decimals, check accuracy value |
| Poor accuracy | Accuracy > 20m | Environmental factors | Wait for GPS stabilisation, clear sky view |
| No altitude | Altitude shows "Not captured" | Platform limitation | Common on web, some Android devices |
| Stuck GPS | Continues failing after GPS enabled | Capacitor/OS bug | Open Google Maps to refresh GPS, restart app |

### Debug Checklist

**Before Capture:**
- [ ] GPS/Location Services enabled in device settings?
- [ ] App has location permission granted?
- [ ] Clear view of sky (for best accuracy)?
- [ ] Waited 30-60 seconds for GPS stabilisation?
- [ ] Airplane mode disabled?

**During Issues:**
- [ ] Check accuracy value – is it acceptable for your needs?
- [ ] Try increasing timeout parameter to 20-30 seconds
- [ ] Open another GPS app (Maps) to "wake up" GPS
- [ ] Document accuracy concerns in annotation field
- [ ] Consider MapFormField if visual placement needed

**Data Quality:**
- [ ] Review captured accuracy values
- [ ] Note environmental conditions in annotations
- [ ] Flag uncertain readings with uncertainty checkbox
- [ ] Plan for altitude/speed/heading being null
- [ ] Remember CSV export loses most metadata

## Implementation Notes

### Technical Architecture
- Uses Capacitor Geolocation API directly (not React Query like MapFormField)
- Each button tap creates new `getCurrentPosition()` call
- No caching between captures (maximumAge: 0)
- No shared state between multiple TakePoint fields
- Completely independent from MapFormField despite same package

### Critical Limitations
1. **Cannot enforce accuracy thresholds** – Accepts any GPS quality
2. **No user feedback during acquisition** – 10-second silent wait
3. **Misleading precision display** – Shows 14+ decimals for 10m accuracy
4. **CSV export data loss** – Only lat/lon/accuracy exported
5. **No conditional logic on accuracy** – Can't access nested properties
6. **Battery drain with multiple fields** – No GPS coordination

### Performance Considerations
- Each field maintains independent React state
- No GPS warm-up sharing between fields
- Storage: ~500-600 bytes per location
- Performance degradation at 1000-2000 points per notebook
- Sync batches limited to 10,000 documents

### Known Bugs
- Permission alert shows for all errors, not just permission issues
- GPS may stick after airplane mode toggle (requires app restart)
- No debouncing allows parallel GPS requests from rapid taps
- Precision/accuracy mismatch in display and export

## Best Practices

### Capture Strategy
- **Allow GPS stabilisation** – Wait 30-60 seconds after arriving on site
- **Check accuracy values** – Manually verify before accepting
- **Document decisions** – Use annotation field for accuracy justification
- **Multiple attempts** – Take several readings, keep best accuracy
- **Environmental awareness** – Note sky visibility, building proximity

### Configuration Guidelines
- Set timeout to 20-30 seconds for important captures
- Keep maximumAge at 0 for scientific data
- Always include annotation field for quality notes
- Consider uncertainty checkbox for flagging issues
- Use required validation sparingly (blocks form without GPS)

### Data Quality Management
- Document why poor accuracy was accepted
- Export JSONL backups to preserve all metadata
- Monitor notebook size (keep under 1000 points)
- Create multiple notebooks rather than one huge dataset
- Plan for missing altitude/speed/heading on some platforms

### Battery Conservation
- Avoid multiple TakePoint fields in same form section
- Space out captures temporally
- Warn users about battery impact
- Consider MapFormField for multiple related points
- Don't use rapid repeated captures (no accuracy benefit)

## See Also

### Required Companions
- None - TakePoint operates independently

### Common Pairings
- **[TakePhoto](./TakePhoto.md)** – Often paired for geotagged photography. TakePhoto's GPS injection provides alternate location capture
- **[TemplatedString](./TemplatedString.md)** – Can reference TakePoint coordinates in templates for location-based identifiers
- **[Annotation Fields](./Annotation.md)** – Essential for documenting GPS quality decisions when accuracy is poor

### Mutual Exclusions  
- **[MapFormField](./MapFormField.md)** – Incompatible data formats (`faims-pos::Location` vs `faims-core::JSON`). Choose one location method per record type

### Validation Cascades
- When TakePoint is required, form cannot save without GPS capture
- TakePoint null state affects conditional logic for dependent fields
- No validation cascade TO other fields (TakePoint validation is self-contained)

### Dependent Fields
- Fields using conditional logic based on TakePoint presence/absence
- TemplatedString fields referencing TakePoint coordinates
- Cannot reference TakePoint accuracy or metadata in conditions (limitation)

### Alternative Approaches
- **[FileUploader](./FileUploader.md)** – Cannot import GPX/KML files (not supported)
- **[Map Tab](./MapTab.md)** – Viewing all captured locations across notebook (read-only)
- **[Offline Maps Feature](../guides/OfflineMaps.md)** – Not applicable to TakePoint (MapFormField only)

### Data Flow
- **[Data Export Guide](../guides/DataExport.md)** – Critical: CSV export loses altitude/speed/heading/timestamp metadata
- **[JSONL Backup](../guides/Backup.md)** – Only method preserving complete Location metadata

## Migration and Compatibility Notes

### Format Incompatibility
- **Cannot transfer** between TakePoint and MapFormField
- **Different types**: `faims-pos::Location` vs `faims-core::JSON`
- **No conversion** utilities available
- **Manual reconstruction** required if switching field types

### Future Roadmap (Per Development Team)
- Precision adjustment based on accuracy (acknowledged issue)
- Possible accuracy threshold enforcement
- Better user feedback during GPS acquisition
- Potential metadata preservation in CSV export

### Researcher Recommendations
- Design notebooks with single TakePoint per form section
- Train users on accuracy checking before acceptance
- Establish project accuracy standards
- Document minimum acceptable accuracy in helperText
- Use JSONL backup for full metadata preservation
- Consider external GPS devices for survey-grade precision (not currently supported)