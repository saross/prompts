<!-- concat:boundary:start section="location-fields" -->
<!-- concat:metadata
document_id: location-fields-v05
category: location
field_count: 2
designer_capable: ["TakePoint"]
json_only: ["MapForm", "geometry_types", "map_layers"]
last_updated: 2025-01-05
-->

<!-- discovery:metadata
provides: [gps-capture, map-fields, coordinate-input, location-privacy]
see-also: [platform-reference, media-fields-v05]
-->


# Location Fields - Fieldmark v3 Documentation

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Display Fields](./display-field-v05.md) | **Location Fields** | [Media Fields →](./media-fields-v05.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Media Fields ↓](#media-fields) -->

## Overview {essential}

### DESIGNER QUICK GUIDE
**Location Capture Fields Available:**
- **TakePoint** → GPS coordinate capture via device location services
## Component Mapping Reference {essential}

For the complete mapping between Designer field names and JSON component implementations, see:
→ **[Designer UI to Component Mapping Reference](../references/designer-component-mapping.md)**

This central reference provides:
- Exact component names and namespaces for all fields
- Configuration requirements and examples
- Common mapping errors and solutions


## Designer Usage Guide {essential}

### What to Select in Designer
1. Navigate to Field Type selection
2. For GPS coordinates:
   - Choose "Custom Field" → "TakePoint"
3. For map-based selection:
   - Choose "Plugin Field" → "MapFormField"
4. Configure available properties (limited set)

### When JSON Enhancement is Required
**TakePoint JSON parameters:**
- `enableHighAccuracy` - GPS precision mode
- `timeout` - Maximum wait time (ms)
- `maximumAge` - Accept cached position age

**MapFormField JSON parameters:**
- `center` - Initial map coordinates [lon, lat]
- `projection` - Coordinate system (limited options)
- `featureType` - Geometry type selection

### Designer Limitations {important}
See [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) for universal constraints.

**Location-Specific Designer Limitations:**
- Cannot set GPS timeout through Designer
- Cannot configure map center coordinates
- Cannot set GPS parameters (enableHighAccuracy, timeout, maximumAge)
- Cannot configure validation beyond 'required' for MapFormField
- Validation messages don't display properly for MapFormField

## Field Selection Guide {essential}

### Decision Tree
```
Need to capture location?
├─ Single GPS point with metadata?
│  └─ YES → TakePoint
│     ├─ Returns: faims-pos::Location
│     ├─ Includes: accuracy, altitude, timestamp
│     └─ Best for: Site coordinates, find spots, waypoints
│
├─ Visual map-based selection?
│  └─ YES → MapFormField
│     ├─ Returns: faims-core::JSON (GeoJSON)
│     ├─ Supports: Point, LineString, Polygon
│     └─ Best for: Boundaries, transects, area selection
│
└─ GPS track/continuous path?
   └─ NOT AVAILABLE → Use multiple TakePoint records
      └─ Alternative: External GPS app + FileUploader
```

### Decision Matrix
| Requirement | TakePoint | MapFormField |
|------------|-----------|--------------|
| GPS metadata | ✅ Full | ❌ None |
| Visual selection | ❌ | ✅ Map interface |
| Offline capability | ✅ | ⚠️ Needs cached tiles |
| Accuracy display | ✅ | ❌ |
| Multiple geometries | ❌ Single point | ❌ Single feature |
| Drawing tools | ❌ | ✅ Point/Line/Polygon |
| Coordinate precision | ⚠️ False precision | ✅ Visual accuracy |
| Battery impact | Medium | Low |
| Performance limit | 1000 points | 500 vertices |

### Selection Strategy
- **TakePoint when:**
  - GPS metadata required (accuracy, altitude)
  - Quick coordinate capture needed
  - Working offline without maps
  - Battery life less critical
  
- **MapFormField when:**
  - Visual context aids location selection
  - Drawing boundaries or paths
  - Area/polygon capture required
  - Base map tiles available

## ⚠️ Critical Location Security Risks {essential}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for general security patterns.

**Location-Specific Security Concerns:**
- **Privacy exposure** - Precise coordinates in published datasets
- **GPS spoofing** - No validation of coordinate authenticity
- **False precision** - 14+ decimals suggest nanometre accuracy
- **Tracking patterns** - Sequential points reveal movement
- **Geofencing bypass** - No boundary enforcement
- **EXIF remnants** - Location data in uploaded photos
- **Accuracy masking** - Poor GPS accepted without warning

**Mitigation Requirements:**
- Truncate coordinates to appropriate precision
- Document accuracy thresholds
- Review datasets before publication
- Consider coordinate obfuscation for sensitive sites
- Train users on privacy implications

## What These Fields Cannot Do {important}

**Both Fields Cannot:**
- Continuous GPS tracking/logging
- Enforce accuracy thresholds
- Convert between data formats
- Share GPS warm-up state
- Validate coordinate bounds
- Import GPX/KML files

**TakePoint Specific:**
- Cannot retry on poor accuracy
- Cannot show capture progress
- Cannot access accuracy in conditions
- Cannot format coordinate display
- Cannot configure precision

**MapFormField Specific:**
- Cannot capture GPS metadata
- Cannot display validation errors
- Cannot delete individual vertices
- Cannot measure distance/area
- Cannot import external geometries
- Cannot store feature properties

## Common Use Cases {important}

**TakePoint Use Cases:**
- Archaeological find spots
- Sample collection points
- Control point establishment
- Photo location tagging
- Rapid waypoint marking
- Site entrance coordinates
- Emergency position recording

**MapFormField Use Cases:**
- Excavation area boundaries
- Survey transect paths
- Building footprint tracing
- Vegetation patch mapping
- Site perimeter definition
- Linear feature documentation
- Viewshed area drawing

## Designer Component Mapping {essential}

| Designer Option | Component Config | Notes |
|-----------------|------------------|-------|
| Custom Field → TakePoint | `"component-namespace": "faims-custom"` | GPS capture |
| Plugin Field → MapFormField | `"component-namespace": "mapping-plugin"` | Map drawing |
| Label | `"label": "Field Label"` | Both fields |
| Helper Text | `"helperText": "Guidance"` | Both fields |
| Required | `"required": true` | TakePoint only |
| Zoom Level | `"zoom": 12` | MapFormField only |
| Feature Type | `"featureType": "Point"` | MapFormField only |

## Designer Capabilities vs JSON Enhancement {comprehensive}

### Designer Configuration (Limited)
**TakePoint:**
- ✅ Field label and name
- ✅ Helper text
- ✅ Required flag
- ⚠️ No GPS parameters

**MapFormField:**
- ✅ Field label
- ✅ Zoom level
- ✅ Feature type (Point, LineString, Polygon)
- ❌ Center coordinates
- ❌ Validation (only 'required' available)

### JSON-Only Configuration

**TakePoint GPS parameters:**
```json
{
  "enableHighAccuracy": true,    // Request best GPS
  "timeout": 30000,              // 30 second timeout
  "maximumAge": 0                // Force fresh reading
}
```

**MapFormField map parameters:**
```json
{
  "center": [151.2093, -33.8688],  // Sydney coordinates
  "featureType": "Polygon",        // Point/LineString/Polygon
  "projection": "EPSG:4326"        // Limited options
}
```

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

**Location-Specific Namespace Issues:**
- Using "faims-custom" for MapFormField - Field won't render
- Using "mapping-plugin" for TakePoint - Component not found
- Wrong capitalisation - Parse errors


## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| GPS points | TakePoint | Simple coordinate capture |
| Areas/Polygons | MapFormField | Draw on map |
| Routes/Lines | MapFormField | Draw polylines |
| Site locations | TakePoint | Quick GPS capture |

### Decision Criteria
- **Geometry type**: Point → TakePoint, Polygon/Line → MapFormField
- **User interaction**: GPS button → TakePoint, Draw on map → MapFormField
- **Accuracy needs**: High → TakePoint with threshold, Visual → MapFormField
- **Offline capability**: Full → TakePoint, Limited → MapFormField

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Location-Specific Security Notes:**
- Full GPS precision stored (required for research accuracy)
- No coordinate obfuscation options (privacy consideration for public data)
- MapFormField accepts self-intersecting polygons
- Both fields store exact coordinates (intentional for research)
- CSV export maintains full precision (by design)

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md#location-field-thresholds-estimates) for detailed metrics including GPS acquisition times, map performance by vertex count, and battery consumption.

**Location-Specific Performance:**
- **GPS acquisition timeout:** 10 seconds default (TakePoint)
- **Location update frequency:** Single capture only
- **Map tile cache:** 100MB typical limit
- **Offline map regions:** 2-14 zoom levels
- **Coordinate precision:** 14+ decimals displayed
- **TakePoint limit:** 1000-2000 points per notebook
- **MapFormField vertices:** 500 optimal, 2000 crash threshold
- **GPU acceleration:** Disabled for MapFormField

### Validation Patterns {important}
See [Validation System Documentation](../detail-crossfield-docs/validation.md) for comprehensive validation patterns and timing.

**Location Field-Specific Validation:**
- **Coordinate range**: NOT validated (accepts invalid lat/lon beyond ±90/±180)
- **GPS accuracy**: Cannot enforce minimum accuracy thresholds
- **Geofencing**: No boundary validation available
- **Required behavior**: Works for TakePoint, silently fails for MapFormField
- **Geometry**: No self-intersection or validity checks for polygons/lines

### Platform Behaviors {important}
See [Platform Behaviors Reference](../reference-docs/platform-behaviors-reference.md) for general platform characteristics.

**Location Field-Specific Behaviors:**
- **iOS**: Higher GPS accuracy; altitude available; "Allow Once" permission; rapid tap vertex bug in MapFormField
- **Android**: GPS needs "wake up" after airplane mode; speed/heading null unless moving
- **Web**: Limited GPS metadata (no altitude/speed); lower accuracy than mobile; mid-session permission revocation possible

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.

Both location fields support:
- **Annotation:** Document GPS quality, accuracy notes
- **Uncertainty:** Flag questionable readings

Critical for location fields due to accuracy variability.

### Export Behavior {important}
See [Data Export Reference](../reference-docs/data-export-reference.md) for universal patterns.

**Location-Specific Export:**

**TakePoint CSV columns:**
- `fieldname` - Full GeoJSON string
- `fieldname_latitude` - Decimal degrees
- `fieldname_longitude` - Decimal degrees
- `fieldname_accuracy` - Metres
- **LOST:** altitude, speed, heading, timestamp

**MapFormField CSV:**
- Point: Extracts lat/lon to separate columns
- LineString/Polygon: GeoJSON string only
- No coordinate extraction for complex geometries

**JSONL backup preserves all metadata**

## Individual Field Reference {essential}

### TakePoint {essential}

#### Purpose {essential}
Single-tap GPS coordinate capture through device geolocation services, returning GeoJSON Feature objects with accuracy metadata and optional positional attributes. Prioritises efficiency over precision refinement.

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | `faims-custom::TakePoint` |
| Returns | `faims-pos::Location` |
| Designer | ⚠️ Basic support |
| JSON Required | GPS parameters |
| GPS Timeout | 10 seconds default |
| Accuracy Display | ✅ Metres shown |
| Metadata | altitude, speed, heading (platform-dependent) |
| Battery Impact | Medium |
| Offline | ✅ Full functionality |

#### Core Configuration
```json
{
  "component-namespace": "faims-custom",
  "component-name": "TakePoint",
  "type-returned": "faims-pos::Location",
  "component-parameters": {
    "label": "GPS Location",
    "name": "gps-point",
    "helperText": "Capture current GPS position",
    "required": false,
    "enableHighAccuracy": true,
    "timeout": 10000,
    "maximumAge": 0
  },
  "validationSchema": [
    ["yup.object"],
    ["yup.nullable"]
  ],
  "initialValue": null
}
```

#### Advanced Configuration
```json
{
  "control-point": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Control Point (High Accuracy)",
      "name": "control-point",
      "helperText": "Wait for accuracy < 10m before capturing",
      "timeout": 30000,
      "enableHighAccuracy": true,
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Control point required"]
    ],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Accuracy justification if >10m"
      },
      "uncertainty": {
        "include": true,
        "label": "GPS quality poor"
      }
    }
  }
}
```

#### Platform-Specific Behaviors
- **iOS:** Best accuracy, altitude common, "Allow Once" option
- **Android:** May need GPS "wake up", speed/heading sporadic
- **Web:** Minimal metadata, browser permission prompts

#### Common Issues & Solutions
| Issue | Cause | Solution |
|-------|-------|----------|
| "location unavailable" | Indoor/airplane mode | Move outside, check settings |
| Timeout errors | Poor GPS reception | Increase timeout to 30s |
| False precision | 14+ decimals shown | Ignore, check accuracy value |
| No altitude | Platform limitation | Common on web browsers |
| Stuck GPS | OS/Capacitor bug | Open Maps app to refresh |

### MapFormField {essential}

#### Purpose {essential}
Interactive geometry creation through web-based mapping, enabling spatial feature delineation by drawing on base map tiles. Uses OpenLayers for Point, LineString, and Polygon creation without GPS metadata.

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | `mapping-plugin::MapFormField` |
| Returns | `faims-core::JSON` |
| Designer | ⚠️ Limited support |
| JSON Required | Center coordinates |
| Geometry Types | Point, LineString, Polygon |
| Vertex Limit | 500 optimal, 2000 crash |
| Offline Maps | ✅ Tile caching |
| Validation Display | ❌ No error shown |
| GPU Acceleration | ❌ Disabled |

#### Core Configuration
```json
{
  "component-namespace": "mapping-plugin",
  "component-name": "MapFormField",
  "type-returned": "faims-core::JSON",
  "component-parameters": {
    "label": "Site Boundary",
    "name": "site-boundary",
    "featureType": "Polygon",
    "zoom": 18,
    "helperText": "Draw site perimeter on map",
    "fullWidth": true,
    "required": false
  },
  "validationSchema": [
    ["yup.object"],
    ["yup.nullable"]
  ],
  "initialValue": null
}
```

#### Advanced Configuration
```json
{
  "transect-path": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Survey Transect",
      "name": "transect-path",
      "featureType": "LineString",
      "zoom": 17,
      "center": [151.2093, -33.8688],
      "helperText": "Draw walked path. Limit to 1000 points",
      "fullWidth": true,
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Transect path required"]
    ],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Path deviation notes"
      }
    }
  }
}
```

#### Platform-Specific Behaviors
- **Desktop:** Drag-drop interface, scroll zoom
- **iOS:** Pinch zoom smooth, rapid tap vertex bug
- **Android:** Progressive slowdown after 300 vertices
- **All:** Single feature limit, no undo capability

#### Common Issues & Solutions
| Issue | Symptoms | Solution |
|-------|----------|----------|
| No validation feedback | Required field looks normal | Check form won't submit |
| Performance degradation | Sluggish drawing | Limit vertices <500 |
| iOS vertex disappear | Points vanish on rapid tap | Tap more slowly |
| Offline maps unavailable | Grey tiles | Pre-download regions |
| Geometry lost | Drawing clears | Remember single-feature limit |

## Troubleshooting Guide {important}

### GPS Issues (TakePoint)
**Before capture:**
- Enable Location Services in device settings
- Disable airplane mode
- Wait 30-60 seconds for GPS stabilisation
- Move to open sky view

**During issues:**
- Check displayed accuracy value
- Increase timeout to 20-30 seconds
- Open Maps app to "wake up" GPS
- Document concerns in annotation

### Map Issues (MapFormField)
**Tile loading:**
- Check internet connection
- Verify browser storage quota
- Use Offline Maps feature to pre-cache

**Performance:**
- Monitor vertex counter
- Keep polygons <500 vertices
- Test on target devices
- Avoid rapid tapping (iOS)

### Data Quality Checklist
- [ ] GPS accuracy acceptable for project?
- [ ] Environmental conditions documented?
- [ ] Platform limitations noted?
- [ ] Coordinate precision appropriate?
- [ ] Export format preserves needed data?

## JSON Examples {comprehensive}

### Example 1: Basic GPS Point Capture
```json
{
  "site-location": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Site Location",
      "name": "site-location",
      "helperText": "Capture GPS coordinates",
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Site location required"]
    ],
    "initialValue": null
  }
}
```

### Example 2: High-Accuracy GPS with Timeout
```json
{
  "precise-location": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Precise GPS Location",
      "name": "precise-location",
      "helperText": "Wait for accuracy <5m (45 second timeout)",
      "timeout": 45000,
      "enableHighAccuracy": true,
      "maximumAge": 0,
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Precise GPS required"]
    ],
    "meta": {
      "annotation": {
        "include": true,
        "label": "GPS conditions and satellite count"
      },
      "uncertainty": {
        "include": true,
        "label": "Accuracy concerns"
      }
    }
  }
}
```

### Example 3: Simple Polygon Drawing
```json
{
  "site-boundary": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Site Boundary",
      "name": "site-boundary",
      "featureType": "Polygon",
      "zoom": 18,
      "helperText": "Draw site perimeter on map"
    },
    "validationSchema": [["yup.object"]],
    "initialValue": null
  }
}
```

### Example 4: Complex Excavation Area with Center
```json
{
  "excavation-area": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Excavation Area",
      "name": "excavation-area",
      "featureType": "Polygon",
      "zoom": 19,
      "center": [151.2093, -33.8688],
      "helperText": "Draw excavation boundary (max 500 vertices)",
      "fullWidth": true,
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Excavation boundary required"]
    ]
  }
}
```

### Example 5: Survey Transect Line
```json
{
  "survey-transect": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Survey Transect",
      "name": "survey-transect",
      "featureType": "LineString",
      "zoom": 16,
      "helperText": "Draw survey walking route"
    },
    "validationSchema": [["yup.object"]],
    "initialValue": null
  }
}
```

### Example 6: Find Spot Location
```json
{
  "find-location": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Find Spot",
      "name": "find-location",
      "featureType": "Point",
      "zoom": 20,
      "helperText": "Click map to mark find location",
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Find location required"]
    ],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Location method and accuracy"
      }
    }
  }
}
```

### Example 7: Rapid Survey Waypoints
```json
{
  "waypoint": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Survey Waypoint",
      "name": "waypoint",
      "helperText": "Quick capture for traverse",
      "timeout": 5000,
      "maximumAge": 3000,
      "enableHighAccuracy": false
    },
    "validationSchema": [["yup.object"]],
    "initialValue": null
  }
}
```

### Example 8: Conditional Location Capture
```json
{
  "structure-location": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Structure GPS",
      "name": "structure-location",
      "helperText": "Capture center point of structure",
      "enableHighAccuracy": true,
      "timeout": 30000
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Structure location required"]
    ],
    "condition": {
      "operator": "equal",
      "field": "feature-type",
      "value": "structure"
    }
  }
}
```

### Example 9: MultiPolygon for Complex Sites
```json
{
  "site-areas": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Site Areas",
      "name": "site-areas",
      "featureType": "MultiPolygon",
      "zoom": 17,
      "helperText": "Draw multiple disconnected areas",
      "advancedHelperText": "## Drawing Tips\n\n- Complete first polygon\n- Click draw tool again for next\n- Each polygon separate feature"
    },
    "validationSchema": [["yup.object"]],
    "initialValue": null
  }
}
```

### Example 10: Battery-Optimized GPS
```json
{
  "check-in-location": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Daily Check-in",
      "name": "check-in-location",
      "helperText": "Morning location verification",
      "timeout": 10000,
      "enableHighAccuracy": false,
      "maximumAge": 60000
    },
    "validationSchema": [["yup.object"]],
    "initialValue": null
  }
}
```

### Example 11: Geofence Area Definition
```json
{
  "restricted-zone": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Restricted Area",
      "name": "restricted-zone",
      "featureType": "Polygon",
      "zoom": 18,
      "center": [144.9631, -37.8136],
      "helperText": "Define no-entry zone",
      "fullWidth": true
    },
    "validationSchema": [["yup.object"]],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Restriction reason and authority"
      }
    }
  }
}
```

### Example 12: Survey Grid Square
```json
{
  "grid-square": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Survey Grid Square",
      "name": "grid-square",
      "featureType": "Polygon",
      "zoom": 20,
      "helperText": "Draw 10m x 10m survey square",
      "advancedHelperText": "Try to maintain square shape.\nUse satellite view for alignment."
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Grid square required"]
    ]
  }
}
```

### Example 13: Emergency Location Fallback
```json
{
  "emergency-location": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Emergency Position",
      "name": "emergency-location",
      "helperText": "Any accuracy accepted - for safety",
      "timeout": 3000,
      "enableHighAccuracy": false,
      "maximumAge": 300000
    },
    "validationSchema": [["yup.object"]],
    "initialValue": null
  }
}
```

### Example 14: Feature Centroid Marking
```json
{
  "feature-center": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Feature Center Point",
      "name": "feature-center",
      "featureType": "Point",
      "zoom": 21,
      "helperText": "Mark exact center of feature",
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Center point required"]
    ],
    "condition": {
      "operator": "is-truthy",
      "field": "feature-boundary"
    }
  }
}
```

### Example 15: Performance-Optimized Polygon
```json
{
  "simplified-boundary": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Simplified Boundary",
      "name": "simplified-boundary",
      "featureType": "Polygon",
      "zoom": 17,
      "helperText": "⚠️ LIMIT 100 VERTICES - Generalize complex shapes",
      "advancedHelperText": "## Performance Warning\n\nUse fewer points for better performance.\nDetailed shapes can crash mobile devices."
    },
    "validationSchema": [["yup.object"]],
    "initialValue": null
  }
}
```

### Example 16: Sampling Location with Metadata
```json
{
  "sample-location": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "component-parameters": {
      "label": "Sample Collection Point",
      "name": "sample-location",
      "helperText": "GPS where sample collected",
      "enableHighAccuracy": true,
      "timeout": 20000,
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Sample location required"]
    ],
    "meta": {
      "annotation": {
        "include": true,
        "label": "Collection method and depth"
      },
      "uncertainty": {
        "include": true,
        "label": "Location precision notes"
      }
    }
  }
}
```

## Migration Scenarios {comprehensive}

### Scenario 1: Converting TakePoint to MapFormField
**Context**: Project moves from simple GPS points to visual boundary mapping

**Challenge**: Data formats completely incompatible
- TakePoint returns `faims-pos::Location` (GeoJSON Feature)
- MapFormField returns `faims-core::JSON` (GeoJSON FeatureCollection)
- No automatic conversion available

**Migration Steps**:
1. Export existing data as JSONL
2. Extract coordinates from TakePoint records
3. Manually create MapFormField GeoJSON structure
4. Import converted data or re-collect

### Scenario 2: Legacy Coordinate Format Handling
**Context**: Migrating from decimal degrees minutes (DDM) to decimal degrees (DD)

**Challenge**: Historical data in various formats
- Degrees Minutes Seconds: 33° 52' 7.68" S
- Decimal Degrees Minutes: 33° 52.128' S
- Decimal Degrees: -33.8688

**Solution**: Pre-process before import
- Use external conversion tools
- Create TextField for manual entry as fallback
- Document original format in annotations

### Scenario 3: Offline Map Deployment
**Context**: Moving to offline-capable deployment

**Current Status**: Experimental feature (mostly working)
- Offline maps generally "just work" after download
- Intermittent rendering error being addressed by tech lead
- Feature marked experimental until rendering fix complete

**Simple Setup**:
1. Download region while online
2. Maps cache automatically
3. Works offline with cached tiles

**Known Issue**: Occasional tile rendering glitch (under investigation)

### Scenario 4: GPS Accuracy Requirements Change
**Context**: Moving from consumer to survey-grade requirements

**Challenge**: TakePoint cannot enforce accuracy thresholds
- Shows 14+ decimal places regardless of true accuracy
- No rejection of poor readings
- No averaging or RTK support

**Workarounds**:
1. Add manual accuracy field for verification
2. Use annotation to document GPS conditions
3. Consider external GPS with FileUploader
4. Train users on accuracy interpretation

### Scenario 5: Performance-Critical Scaling
**Context**: Project scaling beyond performance limits

**Current Limits**:
- TakePoint: 1000-2000 points before degradation
- MapFormField: 500 vertices optimal, 2000 crash threshold

**Migration Strategies**:
1. Split data collection across multiple notebooks
2. Simplify geometries before capture
3. Use point clusters instead of detailed polygons
4. Archive completed data regularly

### General Migration Considerations
- **Data format incompatibility** between TakePoint and MapFormField
- **No conversion utilities** - manual reconstruction required
- **CSV export loses metadata** - use JSONL for full preservation
- **Namespace differences** require JSON updates

## Best Practices {comprehensive}

### GPS Best Practices (TakePoint)
1. **Allow stabilisation** - Wait 30-60s on site
2. **Check accuracy** - Manually verify before accepting
3. **Document decisions** - Use annotations for justification
4. **Multiple attempts** - Keep best accuracy reading
5. **Battery awareness** - Space captures temporally

### Map Best Practices (MapFormField)
1. **Pre-download tiles** - Use Offline Maps feature
2. **Limit vertices** - Stay under 500 for mobile
3. **Save frequently** - No auto-save available
4. **Train users** - Explain single-feature limit
5. **Plan post-processing** - GeoJSON extraction needed

### Data Quality Strategies
- Establish project accuracy standards
- Document minimum acceptable GPS accuracy
- Plan for missing altitude/speed data
- Consider external GPS for survey-grade needs
- Use JSONL backup for complete metadata

## Field Quirks Index (2025-01-03) {comprehensive}

### TakePoint Quirks
- Shows 14+ decimal places regardless of accuracy
- Cannot enforce accuracy thresholds
- No user feedback during 10-second acquisition
- CSV export loses most metadata
- Permission alert shows for all errors
- GPS may stick after airplane mode

### MapFormField Quirks
- Validation errors never display
- Single feature limit (new replaces old)
- No vertex deletion capability
- No undo function
- GPU acceleration disabled
- iOS rapid tap causes vertex loss

### Shared Quirks
- No data format compatibility
- Cannot import external files (GPX/KML)
- No continuous tracking capability
- Independent GPS state (no sharing)
- No coordinate bounds validation

## Performance Thresholds Summary {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for detailed metrics.

**Location-Specific Thresholds:**
| Metric | TakePoint | MapFormField | Impact |
|--------|-----------|--------------|---------|
| Timeout | 10s default / 30s max | N/A | GPS acquisition |
| Points per notebook | 1000-2000 | N/A | Performance degrades |
| Vertices per feature | N/A | 500 optimal / 2000 crash | Drawing response |
| Tile cache | N/A | 100MB typical | Offline capability |
| GPS warm-up | 30-60 seconds | N/A | Accuracy improvement |
| Battery drain | Medium | Low | Per capture |

## JSON Patterns Cookbook (2025-01-03) {comprehensive}

### Pattern: Conditional Location Capture
```json
{
  "feature-location": {
    "component-namespace": "faims-custom",
    "component-name": "TakePoint",
    "type-returned": "faims-pos::Location",
    "condition": {
      "operator": "equal",
      "field": "location-needed",
      "value": "yes"
    }
  }
}
```

### Pattern: Accuracy-Focused Configuration
```json
{
  "component-parameters": {
    "timeout": 30000,
    "enableHighAccuracy": true,
    "maximumAge": 0
  },
  "meta": {
    "annotation": {"include": true, "label": "GPS quality notes"},
    "uncertainty": {"include": true, "label": "Poor accuracy"}
  }
}
```

### Pattern: Performance-Optimised Map
```json
{
  "component-parameters": {
    "featureType": "Polygon",
    "helperText": "Maximum 500 vertices for mobile devices"
  }
}
```

## JSON Anti-patterns Quick Index {comprehensive}

### ❌ Don't: Wrong Namespace
```json
// WRONG - TakePoint doesn't use mapping-plugin
{
  "component-namespace": "mapping-plugin",
  "component-name": "TakePoint"
}
```

### ❌ Don't: Mix Return Types
```json
// WRONG - Can't transfer between fields
{
  "takepoint-data": "faims-pos::Location",
  "mapform-data": "faims-core::JSON"
  // These are incompatible!
}
```

### ❌ Don't: Expect Accuracy Validation
```json
// WRONG - No accuracy threshold enforcement
{
  "minimum_accuracy": 10  // This parameter doesn't exist
}
```

## Quick Diagnosis Tables (2025-01-03) {important}

### Location Field Issues Diagnosis
| Symptom | Field | Likely Cause | Quick Fix | Platform | Prevention |
|---------|-------|--------------|-----------|----------|------------|
| No GPS signal | TakePoint | Indoor/airplane | Go outside | All | Pre-warm GPS |
| 14+ decimals | TakePoint | False precision | Check accuracy value | All | User training |
| Validation silent | MapFormField | No error display | Check form submission | All | Helper text |
| Vertices vanish | MapFormField | iOS rapid tap | Tap slowly | iOS | Tap training |
| Poor accuracy | TakePoint | GPS not ready | Wait 30-60s | All | Patience protocol |
| Tiles missing | MapFormField | No cache | Download offline maps | All | Pre-download |
| No metadata | TakePoint | Web platform | Use mobile app | Web | Platform choice |
| Timeout errors | TakePoint | Weak signal | Increase timeout | All | JSON config |
| "Location unavailable" | TakePoint | Permission denied | Check settings | All | Setup checklist |
| Frozen drawing | MapFormField | Too many vertices | Simplify shape | Mobile | Vertex limits |
| GPS stuck | TakePoint | OS cache | Open Maps app | Mobile | GPS refresh |
| No altitude | TakePoint | Platform limit | Document as N/A | Web | Expectation setting |
| Self-intersecting | MapFormField | No validation | Manual check | All | Training |
| Battery drain | Both | Continuous GPS | Space captures | Mobile | Usage pattern |
| Accuracy drift | TakePoint | Multipath/weather | Multiple attempts | All | Best-of-3 protocol |

## Field Interaction Matrix (2025-01-03) {important}

### Location Fields with Other Field Types
| Field Combination | Interaction | Common Pattern |
|------------------|-------------|----------------|
| TakePoint + TakePhoto | Complementary | GPS + geotagged photos |
| MapFormField + TakePoint | Incompatible formats | Choose one method |
| TakePoint + TemplatedString | Coordinate reference | Location-based IDs |
| MapFormField + Annotation | Quality documentation | Accuracy notes |
| TakePoint + Conditions | Null checking only | Cannot check accuracy |

## Migration Warnings Index (2025-01-03) {comprehensive}

### Critical Migration Issues
1. **Format incompatibility** - Cannot convert between TakePoint/MapFormField
2. **No accuracy enforcement** - Manual checking required
3. **CSV metadata loss** - Use JSONL for preservation
4. **False precision display** - Training needed on accuracy
5. **No GPS track capability** - External apps required
6. **Validation display broken** - MapFormField errors hidden
7. **Performance limits lower** - Vertex counts critical

## See Also {comprehensive}

### Other Field Categories
- **[Text Fields](./text-fields-v05.md)**: Manual coordinate entry fallback
- **[Number Fields](./number-fields-v05.md)**: Separate lat/lon fields alternative
- **[DateTime Fields](./datetime-fields-v05.md)**: Timestamps for location capture
- **[Select/Choice Fields](./select-choice-fields-v05.md)**: Location type classification
- **[Media Fields](./media-fields-v05.md)**: TakePhoto for geotagged images
- **[Relationship Field](./relationship-field-v05.md)**: Linking locations to records
- **[Display Field](./display-field-v05.md)**: GPS capture instructions

### Reference Documents
  - [Validation Timing Reference](../reference-docs/validation-timing-reference.md)
  - [Data Export Reference](../reference-docs/data-export-reference.md) - Coordinate format handling
  - [Security Considerations](../reference-docs/security-considerations-reference.md) - Location privacy
  - [Performance Thresholds](../reference-docs/performance-thresholds-reference.md) - GPS timeouts, vertex limits
  - [Accessibility Reference](../reference-docs/accessibility-reference.md) - Map interface accessibility
  - [Component Namespace Reference](../reference-docs/component-namespace-reference.md) - Namespace troubleshooting
  - [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) - JSON requirements
  - [Meta Properties Reference](../reference-docs/meta-properties-reference.md) - Annotation importance
  - [Formik Integration Reference](../reference-docs/formik-integration-reference.md) - State management

## Error Message Quick Reference {important}

### Location-Specific Errors
| Error | Field | Cause | Solution |
|-------|-------|-------|----------|
| "location unavailable" | TakePoint | Generic GPS failure | Check settings, go outside |
| "kCLErrorDomain error 1" | TakePoint | iOS permission denied | Settings > Privacy > Location |
| "Timeout expired" | TakePoint | GPS timeout reached | Increase timeout parameter |
| Silent validation failure | MapFormField | No error display | Check form won't submit |
| "Permission denied" | Both | Location access denied | Grant permission in settings |
| Grey map tiles | MapFormField | No tile cache | Download offline maps |
| "maximumAge is not valid" | TakePoint | JSON syntax error | Check parameter spelling |

## Metadata {comprehensive}
- **Document Version**: v05 (consolidated)
- **Source Documents**: TakePoint.md, MapFormField.md (Third Draft)
- **Platform Version**: Fieldmark v3 (January 2025)
- **Total Fields**: 2 (TakePoint, MapFormField)
- **Key Limitations**: No accuracy enforcement, false precision, incompatible formats
- **Security Level**: Location privacy concerns
- **Performance Limits**: 1000 points (TakePoint), 500 vertices (MapFormField)
- **Reference Docs**: 9 linked documents
---


## Fields in Complete Notebooks {important}

For complete working examples showing how these fields integrate into full notebook structures with fviews and viewsets, see:

→ **[Complete Notebook Templates](../references/notebook-templates.md)**

The templates include:
- Minimal survey (3 fields) 
- Basic data collection (10 fields)
- Complex form with validation (20 fields)
- Mobile-optimized with GPS/Photo
- Production archaeological recording

Each template shows the complete JSON structure required for import into Designer, including:
- Proper field → fview → viewset hierarchy
- Required `name` parameters for all fields
- Working validation schemas
- Conditional logic examples

---

## Related Documentation {important}
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Display Fields](./display-field-v05.md) | [#display-fields](#display-fields)
- **Next**: [Media Fields](./media-fields-v05.md) | [#media-fields](#media-fields)

### Cross-Field Patterns
- **Field Selection**: [Location Field Selection Guidance](../patterns/field-selection-guide.md#location-fields) | [#field-selection](#field-selection)
- **Validation**: [Location Accuracy](../detail-crossfield-docs/validation.md#location-fields) | [#validation-patterns](#validation-patterns)
- **Field Dependencies**: [GPS Requirements](../detail-crossfield-docs/conditional-logic.md#location-fields) | [#conditional-logic](#conditional-logic)

### Technical References
- **Platform Behaviors**: [GPS Handling](../reference-docs/platform-behaviors-reference.md#location-fields) | [#platform-behaviors](#platform-behaviors)
- **Performance**: [Map Rendering](../reference-docs/performance-thresholds-reference.md#location-fields) | [#performance-thresholds](#performance-thresholds)

<!-- /concat:references -->
<!-- concat:boundary:end section="location-fields" -->
