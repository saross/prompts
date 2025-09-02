# MapFormField – Complete Third-Draft Documentation

## Overview

The MapFormField provides interactive geometry creation through web-based mapping, enabling researchers to delineate spatial features by drawing directly on base map tiles. This field leverages OpenLayers v10.3.1 to support three geometry types – Point, LineString, and Polygon – whilst implementing dual tile caching strategies that balance convenience with reliability. Unlike the metadata-rich TakePoint field, MapFormField prioritises visual spatial delineation over GPS precision, returning pure geometric data without accuracy indicators or temporal stamps. The field's 'mapping-plugin' namespace reflects its semi-integrated status as a sophisticated plugin rather than a core field type, explaining both its powerful capabilities and its limited Designer interface exposure.

The implementation enforces single-feature simplicity through automatic geometry replacement, preventing the accumulation of multiple features that could degrade mobile performance. With GPU acceleration unfortunately disabled and no built-in vertex limits, the field requires disciplined use to maintain responsive performance on resource-constrained devices.

## Common Use Cases

- **Site boundary delineation**: Drawing excavation areas, survey zones, or heritage site perimeters on aerial imagery
- **Linear feature documentation**: Recording walls, roads, trenches, or transect paths requiring multiple vertices
- **Point placement with context**: Selecting precise locations on maps where visual landmarks aid accuracy
- **Area calculations preparation**: Creating polygons for post-processing area/perimeter analysis in GIS
- **Vegetation patch mapping**: Delineating irregular natural features visible on base maps
- **Building footprint capture**: Tracing structures from aerial imagery for heritage documentation
- **Sample grid overlay**: Creating regular or irregular sampling areas over visible terrain
- **Viewshed documentation**: Drawing visible areas from observation points
- **Access route recording**: Mapping paths to remote sites for future navigation

## Core Configuration

### Required Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `component-namespace` | string | Must be `"mapping-plugin"` | `"mapping-plugin"` |
| `component-name` | string | Must be `"MapFormField"` | `"MapFormField"` |
| `name` | string | Internal field identifier | `"site-boundary"` |
| `type-returned` | string | Must be `"faims-core::JSON"` | `"faims-core::JSON"` |
| `featureType` | string | Geometry type | `"Point"`, `"LineString"`, `"Polygon"` |

### Optional Parameters

| Parameter | Type | Default | Description | Designer |
|-----------|------|---------|-------------|----------|
| `label` | string | `"Map Field"` | Display label | ✓ |
| `helperText` | string | `""` | Guidance text | ✓ |
| `zoom` | number | `12` | Initial zoom level | ✓ |
| `required` | boolean | `false` | Mandatory completion | ✓ |
| `fullWidth` | boolean | `false` | Expand to container | ✓ |
| `center` | [number, number] | Sydney CBD | Initial coordinates [lon, lat] | ✗ |
| `projection` | string | `"EPSG:4326"` | Limited to hardcoded options | ✗ |
| `geoTiff` | string | `""` | Not implemented | ✗ |

**Note**: Parameters marked ✗ require JSON editing; Designer only exposes `zoom` and `featureType`.

## Validation Rules

### Critical Validation Gap

**WARNING**: MapFormField has NO error display implementation. Validation schemas can be defined but produce no visual feedback.

| Rule | Configuration | Actual Behaviour | User Experience |
|------|---------------|------------------|-----------------|
| Required | `required: true` | Blocks submission silently | No error message displayed |
| Type validation | `[["yup.object"]]` | Validates structure | No feedback on failure |
| Nullable | `[["yup.nullable"]]` | Allows empty field | Standard behaviour |
| Geometry validation | Not implemented | Accepts invalid geometries | Self-intersecting polygons permitted |

### Working Validation Example
```json
"validationSchema": [
  ["yup.object"],
  ["yup.required", "Location required"],
  ["yup.nullable"]
]
```
**Note**: Message defined but never displayed due to missing error UI.

## Display Behaviour

### Desktop Rendering
- **Dialog presentation**: 95vw × 95vh modal overlay
- **Map controls**: Zoom buttons, center-on-GPS button
- **Drawing tools**: Automatic based on featureType
- **Modification**: Click and drag vertices after drawing
- **Vertex counter**: Real-time display during creation
- **Clear button**: Removes all geometry instantly

### Mobile Rendering

#### iOS Behaviour
- **Touch gestures**: Tap to add vertices, drag to pan
- **Pinch zoom**: Smooth fractional zooming
- **Two-finger rotation**: Enabled by default
- **Known issue**: Rapid tapping may cause vertex disappearance
- **Performance**: Consistent until ~2000 vertices then hard crash

#### Android Behaviour
- **Touch gestures**: Same as iOS but potentially sluggish
- **Performance**: Progressive degradation from ~300 vertices
- **RAM-dependent**: 2GB devices struggle earlier than 8GB
- **No haptic feedback**: No vibration on vertex placement

### Drawing Interface
- **Point**: Single tap places marker, auto-replaces previous
- **LineString**: Sequential taps, double-tap to finish
- **Polygon**: Sequential taps, double-tap or tap first vertex to close
- **Modification**: Tap and drag vertices (no vertex deletion)
- **NO UNDO**: Only complete clear available

## Interaction Patterns

### Map Navigation
| Gesture | Desktop | Mobile | Function |
|---------|---------|--------|----------|
| Single click/tap | ✓ | ✓ | Add vertex/point |
| Double-click/tap | ✓ | ✓ | Finish drawing |
| Drag | ✓ | ✓ | Pan map |
| Scroll wheel/Pinch | ✓ | ✓ | Zoom |
| Right-click/Two fingers | ✓ | ✓ | Rotate |

### Drawing Workflow
1. Open map dialog via field button
2. Navigate to area of interest
3. Select drawing tool (automatic by featureType)
4. Click/tap to create geometry
5. Modify vertices if needed (drag only)
6. Save to commit or Clear to restart
7. Close discards unsaved changes

### Critical Limitations
- **Single feature only**: New drawing clears previous
- **No vertex deletion**: Cannot remove individual vertices
- **No snapping**: No alignment assistance
- **No measuring**: No distance/area display
- **No coordinate display**: Except basic point coordinates

## Conditional Logic Support

Standard conditional field behaviour applies:
```json
"condition": {
  "field": "needs-boundary",
  "operator": "equal",
  "value": true
}
```

MapFormField can be controller or controlled field. Empty geometry evaluates as null for conditions.

## Data Storage and Export

### Storage Structure
Stored as GeoJSON FeatureCollection in field value:

```json
{
  "type": "FeatureCollection",
  "features": [{
    "type": "Feature",
    "geometry": {
      "type": "Polygon",
      "coordinates": [[[lon1,lat1],[lon2,lat2],...,[lon1,lat1]]]
    },
    "properties": null
  }]
}
```

### Key Characteristics
- **Coordinate order**: [longitude, latitude]
- **Projection**: EPSG:4326 (WGS84)
- **Properties**: Always null (no metadata capability)
- **Storage size**: ~50 bytes per vertex
- **No compression**: Plain JSON text

### CSV Export Format
| Geometry Type | Main Column | Latitude Column | Longitude Column |
|---------------|-------------|-----------------|------------------|
| Point | Full GeoJSON string | Decimal value | Decimal value |
| LineString | Full GeoJSON string | Empty string | Empty string |
| Polygon | Full GeoJSON string | Empty string | Empty string |

**Note**: Only Points extract coordinates; complex geometries require post-processing.

## Common Patterns

### Heritage Site Boundary
```json
{
  "site-boundary": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Heritage Site Perimeter",
      "name": "site-boundary",
      "featureType": "Polygon",
      "zoom": 18,
      "helperText": "Draw boundary clockwise. Limit to 500 vertices for performance",
      "fullWidth": true,
      "required": true
    },
    "validationSchema": [
      ["yup.object"],
      ["yup.required", "Site boundary required"]
    ],
    "initialValue": null,
    "meta": {
      "annotation": {"include": true, "label": "boundary_notes"},
      "uncertainty": {"include": true, "label": "accuracy_assessment"}
    }
  }
}
```

### Archaeological Transect Path
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
      "helperText": "Click along walked path. Performance degrades beyond 1000 points",
      "center": [151.1234, -33.5678],
      "fullWidth": true
    },
    "validationSchema": [["yup.object"], ["yup.nullable"]],
    "initialValue": null,
    "meta": {
      "annotation": {"include": true, "label": "deviation_reason"}
    }
  }
}
```
**Note**: `center` parameter requires JSON editing.

### Context-Aware Point Selection
```json
{
  "artifact-location": {
    "component-namespace": "mapping-plugin",
    "component-name": "MapFormField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Find Location",
      "name": "artifact-location",
      "featureType": "Point",
      "zoom": 19,
      "helperText": "Click precise location on map. Consider using TakePoint for GPS metadata"
    },
    "validationSchema": [["yup.object"], ["yup.nullable"]],
    "initialValue": null
  }
}
```

## Troubleshooting Guide

### Common Issues and Solutions

| Issue | Symptoms | Solution | Prevention |
|-------|----------|----------|------------|
| No validation feedback | Required field appears normal when empty | Check form won't submit; no visual indicator available | Document requirement clearly in helperText |
| Performance degradation | Sluggish drawing/modification | Limit polygons <500 vertices, lines <1000 points | Monitor vertex counter during drawing |
| iOS vertex disappearance | Points vanish during rapid tapping | Tap more slowly and deliberately | Train users on platform limitations |
| Offline map unavailable | Grey tiles or loading error | Use Offline Maps feature to pre-download regions | Download all field areas before deployment |
| Geometry lost | Drawing clears unexpectedly | Remember single-feature limit | Save frequently, document in training |
| Cannot undo | Mistake requires complete redraw | No undo available - use Clear button | Practice on test data first |
| Export processing needed | GeoJSON strings in CSV | Post-process to extract geometries | Plan GIS workflow in advance |

### Debug Checklist
1. ✓ Verify internet connection for initial tile loading
2. ✓ Check browser storage quota for tile caching
3. ✓ Confirm featureType matches intended geometry
4. ✓ Monitor vertex count (displayed during drawing)
5. ✓ Test on target devices before deployment
6. ✓ Verify offline maps downloaded if needed
7. ✓ Check JSON syntax if manually edited
8. ✓ Confirm single-feature understanding

### Platform-Specific Workarounds
- **iOS rapid tap issue**: Implement deliberate tapping rhythm
- **Android performance**: Start with simple geometries
- **Missing GPU acceleration**: Keep geometries simple
- **No error display**: Use helperText for all instructions

## Implementation Notes

### Technical Architecture
- **OpenLayers version**: v10.3.1 (modern features available but mostly unused)
- **Namespace**: 'mapping-plugin' indicates semi-integrated plugin status
- **GPU acceleration**: DISABLED via CSS (`will-change: unset !important`)
- **Tile providers**: OpenStreetMap or MapTiler (platform-configured)
- **Storage mechanism**: IndexedDB for tile caching

### Tile Caching Strategies
1. **Opportunistic caching** (automatic but fragile):
   - Tiles cached when viewed online
   - Browser may clear without warning
   - Suitable for areas with intermittent connectivity

2. **Offline maps** (manual but robust):
   - Explicit download via /offline-maps interface
   - Fixed zoom levels 2-14
   - Named regions for organisation
   - Survives browser storage management

### Performance Constraints
**Recommended limits for mobile devices**:
- Points: Single only (enforced)
- Polygons: <500 vertices (250 optimal)
- LineStrings: <1000 points (500 optimal)

**Why performance degrades**:
- GPU acceleration disabled
- Full canvas redraw per vertex
- No viewport culling
- No geometry simplification

### Missing Professional Features
- No measuring tools (distance/area)
- No coordinate format options (DD only)
- No snapping or alignment
- No feature metadata storage
- No multi-geometry support
- No GPS accuracy display
- No import/export beyond CSV

## Best Practice Recommendations

### Deployment Preparation
- **Pre-download offline maps** for all field areas during planning phase
- **Test vertex limits** on actual field devices
- **Document single-feature limitation** prominently in training
- **Plan post-processing workflow** for GeoJSON extraction
- **Set appropriate zoom levels** for the scale of features being mapped

### Field Usage Guidelines
- **Keep geometries simple** - prioritise completion over precision
- **Save frequently** - no auto-save or recovery
- **Document accuracy** in annotation fields
- **Consider TakePoint** for GPS metadata needs
- **Monitor performance** via vertex counter
- **Avoid rapid tapping** on iOS devices

### Data Quality Strategies
- **Verify geometry validity** in post-processing (self-intersection)
- **Document coordinate system** (always WGS84/EPSG:4326)
- **Record environmental conditions** affecting accuracy
- **Plan simplified alternatives** for complex features
- **Establish vertex count guidelines** per feature type

### Training Requirements
1. Explain single-feature replacement behaviour
2. Demonstrate no-undo limitation
3. Practice with target vertex counts
4. Show offline map download process
5. Explain validation silence issue
6. Demonstrate CSV export format

## Cross-References & Dependencies

### Required Companions
- **None**: MapFormField operates independently without required fields

### Common Pairings
- **TakePoint**: Often used together for complementary capture (visual boundary + GPS point)
  - Relationship: Complementary but incompatible data formats
  - Use case: TakePoint for quick coordinates, MapFormField for boundaries
- **TemplatedString**: Generate location-based record identifiers
  - Relationship: Can reference coordinates in ID generation
  - Example: `{{site}}-{{map-location}}-{{auto-increment}}`
- **Annotation fields**: Document spatial data quality
  - Relationship: Annotation captures accuracy/uncertainty notes
  - Critical for recording GPS conditions or drawing precision

### Mutual Exclusions
- **Multiple MapFormFields**: Performance degrades with multiple map fields per form
  - Recommendation: Single MapFormField per section
- **Heavy media fields**: Combining with TakePhoto arrays impacts memory
  - Consider: Separate sections for spatial and media data

### Validation Cascades
- **As controller**: Empty geometry evaluates as null for conditional logic
  - Can show/hide dependent fields based on geometry presence
- **As dependent**: Can be hidden/shown by other field conditions
  - Note: Validation still applies when hidden (blocks submission)

### Dependent Fields
- **No direct dependents**: Other fields cannot reference geometry data
- **Indirect relationships**: 
  - Export processing may expect coordinate columns (Points only)
  - TemplatedString cannot extract coordinates directly
  - Related records may reference location via record ID only

### Data Interchange Limitations
- **Cannot transfer to TakePoint**: Incompatible formats (FeatureCollection vs Feature)
- **Cannot import from FileUploader**: No GeoJSON file import capability
- **No shared validation**: Each location field validates independently
- **Properties always null**: Cannot store or transfer metadata

## Migration and Compatibility Notes

### Version Compatibility
- **Data format**: GeoJSON standard ensures forward compatibility
- **Field type**: `faims-core::JSON` stable across versions
- **Namespace**: 'mapping-plugin' may change in architectural updates

### Migration Considerations
- **Export regularly**: GeoJSON strings preserve full geometry
- **Document projection**: Always WGS84/EPSG:4326 currently
- **Backup tile cache**: Offline maps require re-download after updates
- **Test thoroughly**: Platform updates may affect OpenLayers behaviour

### Future Architecture
The separate namespace and limited Designer integration suggest potential architectural changes. Maintain comprehensive documentation and regular exports for data preservation.