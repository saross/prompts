# Fieldmark Field Type Summary Reference Table

## Text Fields
| Field Name | Description | Recommended Use |
|------------|-------------|-----------------|
| FAIMS Text Field | Single-line unconstrained text input | Brief labels, free-text values, or descriptions (under 100 characters) |
| Email | Structured email address input with validation (@, domain) | Contact information for team members, collaborators, or informants |
| Text Field | Multi-line text area for extended content entry | Longer field notes, descriptions, interpretations, or other narrative text |
| Templated String Field | Generates text from template combining values from current record, constants, and system variables (record author; record creation time) | Automatically generate human-readable IDs for record; automated display of record author or creation time |
| Scan QR Code | Camera-based scanner for QR codes and barcodes (mobile only) | Capturing code from pre-printed sample labels, equipment tags, specimen barcodes |
| Address | Structured address input with validation for street addresses | Site locations, institutional addresses, contact information for team members or collaborators |

## Numbers
| Field Name | Description | Recommended Use |
|------------|-------------|-----------------|
| Number Field | Integer input without constraints | Simple counts, whole number quantities, measurements or dimensions with one or two decimal places |
| Controlled Number | Numeric input with enforced min/max range validation | Measurements with known bounds (pH: 0–14, percentages: 0–100) |
| Auto Incrementing Field | Generates sequential numbers automatically (configurable starting point and digit count) | Locally unique sequential record IDs, sample numbers, feature numbers |
| Number Input (Floating Point) | Decimal number entry for precise values | Coordinates, precise measurements, other scientific data requiring decimals |

## Date & Time
| Field Name | Description | Recommended Use |
|------------|-------------|-----------------|
| Date Time Picker | Select both calendar date and specific time | Precise event timing, scheduled observations, timed sampling or sample testing |
| Date Picker | Calendar date selection without time component | Daily records, excavation dates, general temporal data |
| Month Picker | Select month and year only | Seasonal data, approximate dates offered by interviewees, historical records |
| Date and Time with Now Button | Date-time input with one-tap current timestamp option | Recording precise time when a data point was collected, time-sensitive observations |

## Media
| Field Name | Description | Recommended Use |
|------------|-------------|-----------------|
| Upload a File | Attach multiple files of any type (PDFs, documents, audio, video) | Permits, reports, dSLR photos, audio recordings, supporting documents |
| Take Photo | Capture images via device camera or upload existing photos | Field photography, sample or specimen images, environmental context documentation |

## Location
| Field Name | Description | Recommended Use |
|------------|-------------|-----------------|
| Map Field | Interactive map for drawing points, lines, or polygons; display of GPS points collected (requires internet to load maps, which are then cached) | Site boundaries, transect lines, area definitions, offset location selection when location cannot be reached to capture GPS point |
| Take Point | Captures device GPS coordinates with accuracy metadata | Single location points, find spots, current position recording |

## Choice
| Field Name | Description | Recommended Use |
|------------|-------------|-----------------|
| Checkbox | Boolean toggle for yes/no values | Presence/absence, true/false questions, protocol checklist, simple binary choices |
| Select Multiple | Display list allowing multiple selections (all options visible) | Multiple attributes, co-occurring features, material types present |
| Select One Option | Radio button set showing mutually exclusive options (all options visible) | Single choice from small set, exclusive categorisation |
| Select Field | Dropdown list for single selection (also configurable for multiple) | Longer lists, standardised or shared vocabularies |
| Select Field (Hierarchical) | Nested dropdown navigation through category hierarchies | Biological taxonomies, artefact typologies, classification systems |

## Relationship
| Field Name | Description | Recommended Use |
|------------|-------------|-----------------|
| Add Related Record | Create or link child records or other relationships with semantic qualification | Parent-child hierarchies (Site→Feature→Artefact), stratigraphic relationships (temporal and/or spatial) |

## Display
| Field Name | Description | Recommended Use |
|------------|-------------|-----------------|
| Rich Text | Static formatted text | Section headers, instructions, warnings, explanatory text, workflow guidance |

---

## Key Considerations for Field Selection

### Platform Requirements
- **Mobile-only**: Scan QR Code
- **Internet required for initial download**: Map Field (for base map tiles; cached for offline use after initial download)
- **All platforms**: All other field types

### Data Synchronisation
- All fields synchronise automatically
- Media files (photos/uploads) always sync 'up' to server, but have device-specific 'on'/'off' download toggle (toggle 'off' to save space or mobile data)
- Text, numbers, and structured data always sync bi-directionally

### Efficiency Features
- Fields with sticky behaviour maintain values across records
- Auto-incrementing and templated fields eliminate manual entry
- System variables (record author; record creation time) capture metadata automatically
- Media files automatically renamed on export based on record data