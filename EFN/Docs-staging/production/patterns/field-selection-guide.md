<!-- concat:boundary:start section="field-selection-guide" -->
<!-- concat:metadata
document_id: field-selection-guide
category: patterns
version: 1.0
last_updated: 2025-01-06
purpose: Comprehensive field selection guidance consolidating best practices, comparison matrix, and practical examples
source_documents:
  - field-selection-best-practices.md (26KB)
  - summary-table.md (12KB) 
  - quick-start.md (12KB) - selection examples only
-->

<!-- discovery:metadata
provides: [decision-matrices, selection-guidance, comparison-tables, use-case-mapping]
see-also: [all-field-categories, platform-reference]
-->


# Field Selection Guide for Fieldmark Notebooks {essential}

📚 [Field Documentation](../field-type-index.md) > Patterns > Field Selection Guide

## Overview {essential}

This comprehensive guide consolidates field selection principles, practical patterns, and the complete field comparison matrix to support informed decision-making when designing Fieldmark notebooks. Content has been extracted and integrated from field-selection-best-practices, summary-table, and quick-start documentation.

## Table of Contents {essential}
1. [Core Design Principles](#core-design-principles)
2. [Field Type Comparison Matrix](#field-type-comparison-matrix)
3. [Decision Framework by Data Type](#decision-framework-by-data-type)
4. [Field-Specific Selection Guidance](#field-specific-selection-guidance)
5. [Discipline-Specific Patterns](#discipline-specific-patterns)
6. [Performance Considerations](#performance-considerations)
7. [Common Implementation Patterns](#common-implementation-patterns)
8. [Anti-Patterns and Mistakes](#anti-patterns-and-mistakes)

## Core Design Principles {essential}

### Principle 1: Minimise Recording Friction
- **Automate everything the system can know**: User identity, timestamps, location, parent context
- **Design for environmental extremes**: Assume bright sunlight, rain, cold fingers, wet screens
- **Optimise for common cases**: Make frequent tasks exceptionally fast
- **Respect device constraints**: Avoid extensive scrolling or precise touch targets on mobile

### Principle 2: Prefer Structure Over Unstructured Data
Controlled vocabularies should be deployed wherever feasible:
- **Immediate validation**: Preventing errors at collection point
- **Cross-project comparability**: Enabling meta-analysis
- **Computational readiness**: Supporting analysis without cleaning
- **Multilingual accessibility**: Interface translation with data integrity
- **Query efficiency**: Rapid filtering and aggregation

### Principle 3: Design for Data Lifecycle
Consider the entire lifecycle from collection through analysis to preservation:
- **Capture provenance automatically**: Who, when, where, under what project
- **Maintain referential integrity**: Navigable relationships between entities
- **Enable progressive enhancement**: Rapid capture with subsequent detail
- **Support versioning and correction**: Acknowledge interpretive evolution

### Principle 4: Automate System-Knowable Information
Replace manual entry with system variables:
- ❌ Text field for "Recorder name" → ✅ {{_CREATED_BY}} in template
- ❌ DateTime field for "Entry time" → ✅ {{_CREATED_TIME}} in template
- ❌ Manual context copying → ✅ Parent-child inheritance

### Principle 5: Design for Progressive Disclosure
Complex scenarios benefit from conditional logic:
- **Binary Gateway**: Checkbox controlling detailed field visibility
- **Type-Specific Recording**: Radio button revealing relevant field sets
- **Confidence Cascades**: Uncertainty triggering documentation requirements
- **Other Specification**: Controlled vocabulary with conditional free text

## Field Type Comparison Matrix {essential}

### Text and Identifier Fields

| Field Type | Purpose | Examples | Technical Specs | Validation | Platform Notes |
|------------|---------|----------|-----------------|------------|----------------|
| **Single-line Text** | Brief textual entries | "North wall", "Sandy matrix" | ~255 char limit<br/>Returns: String | Pattern matching<br/>Length constraints | Universal compatibility |
| **Multi-line Text** | Extended descriptions | Context descriptions, observations | No practical limit<br/>Returns: String | Length validation<br/>No pattern matching | Touch keyboard challenges |
| **Email** | Validated email addresses | "pi@university.edu" | RFC 5322 validation<br/>Returns: String | Email format validation | Email keyboard on mobile |
| **Address** | Structured physical addresses | Site locations, property details | Multiple sub-fields<br/>Returns: Object | Component validation | Auto-complete varies |
| **Templated String** | Auto-generated identifiers | "SITE1-2024-CTX045" | Mustache.js templating<br/>Read-only | Not user-editable | Essential for HRIDs |
| **QR/Barcode Scanner** | Camera-based code capture | Specimen barcodes, equipment tags | Multiple formats<br/>Returns: String | Format validation | **Mobile only** |

### Numeric Fields

| Field Type | Purpose | Examples | Technical Specs | Validation | Platform Notes |
|------------|---------|----------|-----------------|------------|----------------|
| **Number Field** (Deprecated) | Basic numeric entry | Simple counts | JavaScript number<br/>Returns: Number | Type checking only | Use Controlled Number instead |
| **Controlled Number** | Numeric with boundaries | pH (0-14), percentage (0-100) | Min/max enforcement<br/>Returns: Number | Range validation | Supports sticky behaviour |
| **Auto-incrementing** | Sequential identifiers | Context numbers (001, 002...) | Configurable padding<br/>Returns: String | Uniqueness guaranteed | Cannot reset mid-project |

### Date and Time Fields

| Field Type | Purpose | Examples | Technical Specs | Validation | Platform Notes |
|------------|---------|----------|-----------------|------------|----------------|
| **Date Picker** | Calendar date selection | Excavation date, sample date | ISO 8601 format<br/>Returns: Date string | Min/max date ranges | Native pickers on mobile |
| **DateTime Picker** | Date and time selection | Precise event timing | ISO 8601 with time<br/>Returns: DateTime | Date/time ranges | Platform-specific UI |
| **DateTime Now** | Current timestamp capture | Record creation time | Automatic capture<br/>Returns: DateTime | Always valid | Device clock dependency |
| **Month Picker** | Year and month only | Seasonal data | YYYY-MM format<br/>Returns: String | Year range limits | Simplified interface |

### Selection Fields

| Field Type | Purpose | Examples | Technical Specs | Validation | Platform Notes |
|------------|---------|----------|-----------------|------------|----------------|
| **Checkbox** | Binary true/false | "Sample collected?" | Returns: Boolean<br/>Default: false | Required completion | Large touch target |
| **Radio Buttons** | Single choice (2-7 options) | Preservation state | All options visible<br/>Returns: String | Required selection | Excellent mobile UX |
| **Dropdown (Select)** | Single choice (many options) | Species list (50+ items) | Conserves space<br/>Returns: String | Required selection | Scrolling challenges |
| **Multi-select** | Multiple selections | Observed behaviours | Checkbox list<br/>Returns: Array | Min/max selections | Touch selection hard |
| **AdvancedSelect** | Hierarchical categories | Taxonomies | Tree navigation<br/>Returns: Path/leaf | Depth validation | Complex on mobile |

### Spatial Fields

| Field Type | Purpose | Examples | Technical Specs | Validation | Platform Notes |
|------------|---------|----------|-----------------|------------|----------------|
| **Take GPS Point** | Single coordinate | Find spots, sample locations | GeoJSON point<br/>Includes metadata | Accuracy thresholds | Mobile GPS superior |
| **Map Drawing** | Visual feature creation | Site boundaries, transects | Points/lines/polygons<br/>Returns: GeoJSON | Geometry validation | **Requires internet** (offline experimental) |

### Media Fields

| Field Type | Purpose | Examples | Technical Specs | Validation | Platform Notes |
|------------|---------|----------|-----------------|------------|----------------|
| **Take Photo** | Camera capture | Context photos, specimens | JPEG/PNG<br/>EXIF preserved | File size limits | Compression settings |
| **File Upload** | File attachment | PDFs, spreadsheets, audio | Any file type<br/>Returns: Reference | Type restrictions | Upload time varies |

### Relationship Fields

| Field Type | Purpose | Examples | Technical Specs | Validation | Platform Notes |
|------------|---------|----------|-----------------|------------|----------------|
| **Related Records** | Inter-record connections | Stratigraphic relationships | Parent-child/peer<br/>Returns: Array | Cardinality limits | Performance >50 relations |

### Display Fields

| Field Type | Purpose | Examples | Technical Specs | Validation | Platform Notes |
|------------|---------|----------|-----------------|------------|----------------|
| **Rich Text** | Formatted instructions | Warnings, procedures | Markdown support<br/>Display only | Not applicable | Responsive rendering |

## Decision Framework by Data Type {important}

### Textual Data Capture {#text-fields}

Hierarchical decision process:

1. **Can the value be generated automatically?**
   - YES → Use Templated String field
   - NO → Continue to question 2

2. **Does a controlled vocabulary exist or could one be developed?**
   - YES → Use Select/RadioGroup/MultiSelect as appropriate
   - NO → Continue to question 3

3. **Is the text predictably brief (<100 characters)?**
   - YES → Use Single-line text
   - NO → Use Multi-line text

4. **Does the field require specific validation?**
   - Email format → Email field
   - Physical address → Address field  
   - Barcode scanning → QR/Barcode scanner (mobile only)

### Numeric Data Capture {#number-fields}

Selection based on precision and constraints:

1. **Are there known valid ranges?**
   - YES → Controlled Number field with min/max
   - NO → Continue to question 2

2. **Is this a sequential identifier?**
   - YES → Auto-incrementing field
   - NO → Controlled Number field (avoid deprecated Number Field)

3. **Consider additional factors:**
   - Decimal precision requirements
   - Default values to accelerate entry
   - Sticky behaviour for environmental constants
   - Unit specification in field labels

### Temporal Data Capture {#datetime-fields}

Temporal granularity determines selection:
- **Date only** → Date Picker (excavation date, sample date)
- **Date and time** → DateTime Picker (precise events)
- **Current moment** → DateTime Now (observation timestamp)
- **Month/year only** → Month Picker (seasonal data)

⚠️ **Important**: Use DateTime Now for timezone-aware timestamps. DateTime Picker is discouraged when timezone accuracy matters.

### Choice Field Selection {#select-fields}

Number of options and selection constraints:

**Single Selection:**
- 2 options → Checkbox (if binary) or RadioGroup (if strings needed)
- 3-7 options → RadioGroup (all visible)
- 8-20 options → Select dropdown
- >20 options OR hierarchical → AdvancedSelect

**Multiple Selection:**
- Always use MultiSelect
- Enable expandedChecklist for <10 options
- Configure exclusiveOptions for mutually incompatible choices

### Spatial Data Capture {#location-fields}

Spatial requirements determine fields:
- **Single point** → Take GPS Point
- **Boundaries/areas** → Map Field (internet required for initial tile load, offline maps experimental)
- **Both needed** → Combine both field types
- **Manual coordinates** → Text field with validation

### Media Capture {#media-fields}

Platform and purpose considerations:
- **Field photos** → Take Photo (integrated camera workflow)
- **Document upload** → File Upload (any file type)
- **Mobile-specific** → Take Photo preferred over File Upload
- **Desktop-specific** → File Upload for diverse media types

### Relationship Management {#relationship-field}

Connection type determines approach:
- **Parent-child hierarchy** → Form structure with Related Records
- **Peer relationships** → Related Records with vocabulary pairs
- **Simple references** → Consider Select from existing records
- **Complex networks** → Multiple Related Records (watch performance)

## Field-Specific Selection Guidance {important}

### Text Field Selection Guidance {#text-field-selection}

**Use Single-line Text when:**
- Input is predictably brief (<100 characters)
- No controlled vocabulary is appropriate
- Pattern validation might be needed
- Mobile keyboard efficiency matters

**Use Multi-line Text when:**
- Extended narrative is expected
- Paragraph formatting is beneficial
- Desktop data entry predominates
- Voice-to-text might be used

**Use Templated String when:**
- Creating human-readable identifiers (HRIDs)
- Combining multiple field values automatically
- Ensuring consistent formatting
- Reducing manual entry errors

**Annotation Guidance for Text Fields:**
- Free-text fields typically don't need annotations (already provide space for elaboration)
- Single-line text fields benefit from annotations when capturing structured data that might need qualification
- Consider annotations for identifier fields where generation method or exception needs noting

### Number Field Selection Guidance {#number-field-selection}

**Use Controlled Number when:**
- Valid ranges are known (pH: 0-14)
- Precision requirements are defined
- Default values accelerate entry
- Sticky behaviour benefits workflow

**Use Auto-incrementing when:**
- Sequential identifiers are needed
- Uniqueness must be guaranteed
- Team coordination is established
- Reset is never required

**Avoid Number Field (deprecated):**
- No range validation available
- Use Controlled Number instead

**Annotation Guidance for Number Fields:**
- Always enable annotations for measurements (method, instrument, conditions)
- Essential for counts and quantities (sampling area, estimation method)
- Critical for derived values (calculation method, source data)
- Use uncertainty marking for estimates and approximations

### DateTime Field Selection Guidance {#datetime-field-selection}

**Use DateTime Now when:**
- Recording observation moments
- Timezone accuracy matters
- One-tap capture speeds workflow
- Current timestamp suffices

**Use Date Picker when:**
- Time component unnecessary
- Historical dates recorded
- Date ranges need validation
- Calendar selection helps users

**Avoid DateTime Picker when:**
- Timezone accuracy critical
- Use DateTime Now instead

**Annotation Guidance for DateTime Fields:**
- Enable annotations for "circa" or approximate dates
- Useful for recording temporal uncertainty (season, decade)
- Important for noting calendar system or dating method
- Consider uncertainty marking for provisional dates

### Selection Field Guidance {#selection-field-guidance}

**Use RadioGroup when:**
- 2-7 options need visibility
- Touch targets must be large
- Mobile usage predominates
- Options rarely change

**Use Select Dropdown when:**
- 8-20 options exist
- Screen space is limited
- Desktop usage common
- Scrolling acceptable

**Use AdvancedSelect when:**
- Hierarchical structure exists
- >20 options available
- Search functionality needed
- Taxonomy navigation required

**Annotation Guidance for Selection Fields:**
- Essential for fields with "Other" option (specify what "other" means)
- Important for ambiguous classifications (explain choice reasoning)
- Valuable for multiple valid options (note alternatives considered)
- Critical for provisional identifications pending specialist review

### Location Field Guidance {#location-field-guidance}

**Annotation Guidance for Location Fields:**
- Enable annotations for accuracy notes (GPS signal quality, obstacles)
- Important for method documentation (handheld GPS, map estimation, known coordinates)
- Valuable for environmental conditions affecting accuracy
- Essential when coordinates are estimated or derived

### Media Field Guidance {#media-field-guidance}

**Annotation Guidance for Media Fields:**
- Enable annotations for photo subject identification
- Important for recording photo conditions (lighting, angle, scale)
- Essential for noting what's outside frame but relevant
- Valuable for documenting processing or enhancements applied

## Discipline-Specific Patterns {important}

### Archaeological Recording Patterns {#archaeological-patterns}

**Stratigraphic Relationships:**
- Temporal sequences (earlier than, later than)
- Physical relationships (cuts, cut by, fills)
- Spatial relationships (above, below, abuts)
- Implementation: RelatedRecordSelector with vocabulary pairs

**Contextual Inheritance:**
- Finds inherit context properties
- Samples inherit environmental conditions
- Photos inherit spatial coordinates
- Implementation: Parent-child relationships

**Human-Readable IDs:**
- Pattern: `{{site}}-{{trench}}-{{type}}-{{number}}`
- Example: "MP24-T5-C023"

### Ecological Survey Patterns {#ecological-patterns}

**Transect-Based Observation:**
- Sequential observation points
- Repeated measures at intervals
- Implementation: Auto-incrementing with GPS

**Abundance Estimation:**
- Percentage cover for vegetation
- Count estimates for species
- Categorical abundance (DAFOR scale)
- Implementation: Controlled number fields

**Human-Readable IDs:**
- Pattern: `{{transect}}-{{point}}-{{date}}`
- Example: "T1-P5-20240315"

### Geological Sampling Patterns {#geological-patterns}

**Sample Hierarchies:**
- Outcrop → Sample → Subsample → Analysis
- Maintaining provenance through processing
- Implementation: Deep parent-child relationships

**Orientation Data:**
- Strike and dip measurements
- Plunge and trend for linear features
- Implementation: Grouped number fields

**Human-Readable IDs:**
- Pattern: `{{project}}-{{location}}-{{sample}}`
- Example: "GEO2024-OUT3-S045"

## Performance Considerations {comprehensive}

### Cognitive Performance Factors
- **Recognition over recall**: Select from lists vs remember codes
- **Progressive disclosure**: Show complex options only when needed
- **Consistent patterns**: Same interaction patterns throughout
- **Clear feedback**: Immediate validation with actionable errors

### Technical Performance Constraints

**Battery Consumption:**
- GPS fields: 10-15% per hour continuous use
- Camera operations drain during processing
- Screen brightness for outdoor visibility
- Design workflows allowing GPS/camera activation only when needed

**Processing Limitations:**
- Complex conditional logic causes lag on older devices
- Large vocabularies (>100 items) slow dropdown rendering
- Multiple photo captures require processing time
- Implement progressive loading for large datasets

**Documented Performance Thresholds:**
- Relationship fields: <50 optimal, 50-100 noticeable lag, >200 unusable
- Form complexity: <30 fields for mobile, <10 fields per section
- Option lists: Consider hierarchical beyond 20 items
- Media sync: Device-specific download toggles essential

## Common Implementation Patterns {comprehensive}

### The Measurement Pattern
Combine fields for comprehensive documentation:
1. Measurement type (RadioGroup/Select)
2. Numeric value (Controlled Number with range)
3. Units (in label or separate Select)
4. Uncertainty/precision (annotation field)

### The Identification Pattern
Support confident and provisional identifications:
1. Quick identification (Select from common options)
2. Confidence level (RadioGroup: Certain/Probable/Possible)
3. Requires verification (Checkbox, conditional)
4. Detailed notes (Multi-line text, conditional)

### The Observation Pattern
Structure complex observations efficiently:
1. Observation type (RadioGroup for branching)
2. Type-specific fields (conditional groups)
3. Standard metadata (automatic via templates)
4. Media documentation (Take Photo with annotation)

### The Progressive Detail Pattern
Use conditional logic for optional complexity:
1. Gateway question (Checkbox: "Record detailed measurements?")
2. Basic fields (always visible)
3. Detailed fields (conditionally revealed)
4. Maintains form simplicity while enabling depth

### The Other Specification Pattern
Handle exceptions in controlled vocabularies:
1. Main selection (Select/RadioGroup with "Other" option)
2. Specification field (Text field, conditional on "Other")
3. Preserves structure while allowing flexibility

## Anti-Patterns and Mistakes {comprehensive}

### Common Selection Mistakes

**❌ Using free text when vocabularies exist**
- Creates inconsistent data requiring extensive cleaning
- Prevents immediate analysis and aggregation
- Solution: Develop controlled vocabularies with "Other" options

**❌ Requiring unnecessary precision**
- Demanding exact measurements when estimates suffice
- Creating friction without analytical benefit
- Solution: Match precision to actual research needs

**❌ Ignoring platform constraints**
- Using QR scanners in web-only deployments
- Requiring precise map drawing on phones
- Solution: Design for your actual deployment platform

**❌ Over-using required fields**
- Marking fields required "just in case"
- Preventing record submission for minor omissions
- Solution: Only require truly essential fields

**❌ Creating deep hierarchies**
- Nesting relationships beyond 3-4 levels
- Making navigation cumbersome in field
- Solution: Flatten structures where possible

### Performance Anti-Patterns

**❌ Unlimited relationship fields**
- Allowing hundreds of relationships per record
- Causing severe performance degradation
- Solution: Design data model to limit relationships

**❌ Complex conditional logic chains**
- Multiple nested conditions slowing form rendering
- Creating unpredictable form behaviour
- Solution: Simplify logic, use sections

**❌ Ignoring mobile constraints**
- Designing exclusively for desktop
- Using tiny touch targets and dense layouts
- Solution: Test on actual field devices

## Migration Paths Between Field Types {comprehensive}

### Text to Controlled Vocabulary
When unstructured text reveals patterns:
1. Analyse existing text entries for common values
2. Develop vocabulary from frequent entries
3. Add "Other" option for exceptions
4. Map historical data to new vocabulary

### Simple to Hierarchical Selection
When flat lists become unwieldy:
1. Identify natural groupings in options
2. Create hierarchical structure
3. Migrate to AdvancedSelect
4. Maintain backward compatibility

### Single to Multiple Selection
When exclusive choices prove limiting:
1. Convert RadioGroup/Select to MultiSelect
2. Review data model implications
3. Update validation rules
4. Plan data migration strategy

## Critical Implementation Considerations {essential}

### Human-Readable Identifiers (HRIDs)
**Essential for every form** - without HRIDs, system defaults to opaque UUIDs (e.g., "rec-5f8a9b3c"), substantially complicating:
- Data management and navigation
- Export interpretation
- Team communication
- Quality assurance

Configure using Templated String field with meaningful patterns combining semantic components.

### Conditional Logic Architecture
Fields capable of controlling logic can trigger visibility conditions through:
- Standard operators (equal, not-equal, greater-than, less-than)
- Complex conditions using AND/OR combinations
- Controller fields require `logic_select` property
- Performance impacts with multiple controllers

### Platform-Specific Limitations
Critical disparities requiring careful consideration:
- QR/Barcode scanning: Mobile applications only
- Map fields: Require internet for initial tile loading (offline maps experimental with intermittent rendering issues)
- GPS accuracy: Significantly better on mobile
- Touch interfaces: Challenge precise selection

### Validation Limitations
Current architecture constraints:
- No cross-field validation (cannot compare fields)
- No custom validation functions
- No mathematical operations between fields
- No prevention of logical contradictions
- Client-side validation with limited server verification

### Export Considerations
Design with post-processing in mind:
- Each entity type exports as separate CSV
- Relationships preserved through identifier columns
- Relationship semantics maintained (e.g., "cuts/CTX-042")
- Manual reconstruction required for hierarchical analysis
- Plan vocabularies for export requirements

## Related Documentation {important}

### Field Type Documentation
- [Text & Input Fields](../field-categories/text-fields-v05.md)
- [Number Fields](../field-categories/number-fields-v05.md)
- [Date & Time Fields](../field-categories/datetime-fields-v05.md)
- [Selection Fields](../field-categories/select-choice-fields-v05.md)
- [Location Fields](../field-categories/location-fields-v05.md)
- [Media Fields](../field-categories/media-fields-v05.md)
- [Relationship Field](../field-categories/relationship-field-v05.md)
- [Display Fields](../field-categories/display-field-v05.md)

### Pattern Guides
- [Form Structure Guide](./form-structure-guide.md)
- [Dynamic Forms Guide](./dynamic-forms-guide.md)
- [Implementation Patterns](./implementation-patterns-guide.md)

### Technical References
- [Component Reference](../references/component-reference.md)
- [Platform Reference](../references/platform-reference.md)
- [Constraints Reference](../references/constraints-reference.md)

---

## Navigation {essential}
[← Field Index](../field-type-index.md) | [Pattern Guides](../field-type-index.md#pattern-guides) | [Form Structure Guide →](./form-structure-guide.md)

<!-- concat:boundary:end section="field-selection-guide" -->