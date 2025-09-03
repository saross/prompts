# Reference-Aware Consolidation Prompt: Location Fields (v6)

## Core Directive
Create comprehensive, LLM-optimized documentation for location fields with AWARENESS of extracted reference documents. Focus on location-specific content while linking to universal patterns in reference docs. Extract COMPLETE content from source documents but avoid duplicating reference material.

## Input Documents
1. MapForm.md - Map-based location selection field
2. TakePoint.md - GPS point capture field
3. [Additional location field documents as available]

## Target Document: location-fields-v05.md

## REFERENCE DOCUMENT AWARENESS

### Content Already Extracted to References - DO NOT DUPLICATE

The following content exists in reference documents. Link to these instead of duplicating:

1. **[Validation Timing Reference](../reference-docs/validation-timing-reference.md)**
   - Universal mount/change/blur/submit behavior
   - Formik touched state management
   - Generic validation lifecycle

2. **[Component Namespace Reference](../reference-docs/component-namespace-reference.md)**
   - Namespace troubleshooting procedures
   - Case sensitivity rules
   - Generic namespace errors

3. **[Data Export Reference](../reference-docs/data-export-reference.md)**
   - CSV/JSON format basics
   - Universal special character handling
   - Generic Excel issues

4. **[Security Considerations Reference](../reference-docs/security-considerations-reference.md)**
   - XSS prevention patterns
   - SQL injection mitigation
   - Generic input sanitization

5. **[Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md)**
   - Form-wide performance limits
   - Universal render thresholds
   - Generic optimization triggers

6. **[Meta Properties Reference](../reference-docs/meta-properties-reference.md)**
   - Annotation configuration
   - Uncertainty fields
   - Persistent settings

7. **[Designer Limitations Reference](../reference-docs/designer-limitations-reference.md)**
   - Universal Designer constraints
   - JSON-only configurations
   - Testing limitations

8. **[Formik Integration Reference](../reference-docs/formik-integration-reference.md)**
   - Generic Formik state management
   - Field array handling basics
   - Validation integration patterns

9. **[Accessibility Reference](../reference-docs/accessibility-reference.md)**
   - WCAG compliance standards
   - Universal touch target requirements
   - Generic screen reader support

### Location-Specific Content to INCLUDE

Focus on what's UNIQUE to location fields:

**MapForm Specific:**
- Map provider integration (Mapbox, Google Maps, OSM)
- Tile caching and offline map support
- Map interaction modes (pan, zoom, select)
- Polygon/polyline drawing capabilities
- Coordinate system transformations
- Map layer management
- Geospatial search functionality
- Map styling and customization
- Boundary validation and geofencing

**TakePoint Specific:**
- GPS hardware access patterns
- Location accuracy thresholds
- GPS fix acquisition time
- Battery optimization impacts
- Indoor/outdoor positioning fallbacks
- Platform-specific location services
- Coordinate format options (DD, DMS, UTM)
- Altitude and bearing capture
- Location permission workflows

**Common Location Patterns:**
- Coordinate validation ranges
- Datum and projection handling
- Location privacy considerations
- Offline location strategies
- Location update frequencies
- Accuracy vs battery trade-offs
- Location spoofing detection
- Geographic boundary enforcement

## CRITICAL CORRECTIONS FROM PREVIOUS DOCS
1. Component namespace is always `"faims-custom"` for custom fields
2. Component names are case-sensitive: MapForm, TakePoint
3. Location fields return specific coordinate types
4. Verify actual return types from codebase
5. GPS accuracy varies significantly by platform and environment

## REQUIRED STRUCTURE - LLM-OPTIMIZED WITH REFERENCES

```markdown
# Location Fields - Fieldmark v3 Documentation

## Overview {essential}
### DESIGNER QUICK GUIDE
[Location-specific quick reference]

### CRITICAL NAMING DISAMBIGUATION  
[Location field naming clarifications]

### Location Capture Fields (1-N)
[List each location field with one-line description]

### Component Status Summary
[Location-specific status table]

## Designer Usage Guide {essential}
### What to Select in Designer
[Location-specific Designer options]

### When JSON Enhancement is Required
[Location-specific JSON needs]

### Designer Limitations {important}
See [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) for universal constraints.

**Location-Specific Designer Limitations:**
[Only limitations unique to location fields]

## Field Selection Guide {essential}

### Decision Tree
```
Need to capture location?
├─ Single GPS point?
│  └─ YES → TakePoint
│     ├─ Returns: faims-core::Location
│     └─ Best for: Site coordinates, find spots
│
├─ Map-based selection?
│  └─ YES → MapForm
│     ├─ Returns: faims-core::GeoJSON
│     └─ Best for: Area boundaries, visual selection
│
└─ GPS track/path?
   └─ NOT AVAILABLE → Use multiple TakePoint
      └─ Consider: External GPS app + FileUploader
```

### Decision Matrix
[Location-specific comparison table]

### Selection Strategy
[Location-specific recommendations]

## ⚠️ Critical Location Security Risks {essential}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for general security patterns.

**Location-Specific Security Concerns:**
- Location privacy in published data
- GPS spoofing vulnerabilities
- Coordinate precision revealing exact positions
- Location tracking patterns
- Geofencing bypass attempts
[Location-specific only]

## What These Fields Cannot Do {important}
[Location-specific limitations]

## Common Use Cases {important}
[Location-specific use cases]

## Designer Component Mapping {essential}
[Location field mappings]

## Designer Capabilities vs JSON Enhancement {essential}
[Location-specific Designer vs JSON]

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

**Location-Specific Namespace Issues:**
[Only if unique to location fields]

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Location-Specific Security Notes:**
[Unique to location fields]

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for general limits.

**Location-Specific Performance:**
- GPS acquisition timeout: 30 seconds default
- Location update frequency: 1Hz maximum
- Map tile cache: 100MB typical limit
- Offline map regions: Platform-dependent
- Coordinate precision: 6 decimal places
[Location-specific metrics]

### Validation Patterns {important}
See [Validation Timing Reference](../reference-docs/validation-timing-reference.md) for universal behavior.

**Location-Specific Validation:**
- Coordinate range validation (-90 to 90, -180 to 180)
- Accuracy threshold validation
- Boundary/geofence validation
- Required location validation
[Location-specific patterns]

### Platform Behaviors {important}
[Location-specific platform differences]

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.
[Note if location fields support annotation/uncertainty]

### Export Behavior {important}
See [Data Export Reference](../reference-docs/data-export-reference.md) for universal patterns.

**Location-Specific Export:**
- Coordinate formats in CSV (decimal degrees)
- GeoJSON structure in JSON exports
- KML/GPX export options
- Coordinate precision handling
[Location-specific export issues]

## Individual Field Reference {essential}

### MapForm {essential}

#### Purpose {essential}
[Field description]

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | faims-custom::MapForm |
| Returns | faims-core::GeoJSON |
| Designer | ⚠️ Limited support |
| Touch Target | Map controls 44x44px minimum |
| Offline Maps | ✅ Tile caching |
| Accuracy | Visual selection |
| Battery Impact | Low |

#### Core Configuration
[Essential examples]

#### Advanced Configuration
[Complex examples]

#### Platform-Specific Behaviors
[Platform differences]

#### Common Issues & Solutions
[Troubleshooting]

### TakePoint {essential}
[Similar structure]

## Troubleshooting Guide {important}

## JSON Examples {comprehensive}

## Migration and Best Practices {comprehensive}

## Field Quirks Index (2025-01) {comprehensive}

## Performance Thresholds Summary {essential}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for detailed metrics.

**Location-Specific Thresholds:**
[Table of location-specific limits]

## JSON Patterns Cookbook (2025-01) {comprehensive}

## JSON Anti-patterns Quick Index {comprehensive}

## Quick Diagnosis Tables (2025-01) {important}

## Field Interaction Matrix (2025-01) {important}

## Migration Warnings Index (2025-01) {comprehensive}

## See Also {comprehensive}
- **Media Fields**: For geotagged photos
- **Text Fields**: For coordinate manual entry
- **Number Fields**: For latitude/longitude as separate fields
- **Reference Documents**:
  - [Validation Timing Reference](../reference-docs/validation-timing-reference.md)
  - [Data Export Reference](../reference-docs/data-export-reference.md) - Coordinate formats
  - [Security Considerations](../reference-docs/security-considerations-reference.md) - Location privacy
  - [Performance Thresholds](../reference-docs/performance-thresholds-reference.md) - GPS timeouts
  - [Accessibility Reference](../reference-docs/accessibility-reference.md) - Map accessibility

## Error Message Quick Reference {important}
### Location-Specific Errors
[Focus on GPS, permission, accuracy errors]

## Metadata {comprehensive}
```

## EXTRACTION REQUIREMENTS

### From Source Documents, Extract:
1. All coordinate format specifications
2. All GPS accuracy thresholds and settings
3. All map configuration options
4. All platform-specific location behaviors
5. All offline map capabilities
6. All permission requirements and workflows
7. All boundary/geofencing implementations
8. All complete JSON examples for location fields

### Link to References For:
1. Generic validation timing
2. Universal namespace errors
3. Basic CSV/JSON export
4. Common security patterns
5. Form-wide performance limits
6. Standard meta properties
7. General Designer limitations
8. Basic Formik integration
9. WCAG compliance standards

## TARGET METRICS
- Document length: ~1,500-2,000 lines (appropriate for 2-3 location fields)
- Complete location-specific examples
- Platform details for GPS/map features
- Specific measurements for location operations
- Links to all 9 reference documents where appropriate

## QUALITY CHECKLIST
- [ ] All fields are H3 under H2 "Individual Field Reference"
- [ ] Designer Usage Guide is at position #2
- [ ] Field Selection Guide is at position #3
- [ ] Links to reference docs use ../reference-docs/ path
- [ ] No duplication of reference content
- [ ] Location-specific content comprehensive
- [ ] Platform behaviors documented
- [ ] Security risks specific to location data covered
- [ ] Performance limits for GPS/map operations included