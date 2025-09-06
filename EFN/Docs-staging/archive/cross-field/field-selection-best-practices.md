<!-- DEPRECATED: This document has been consolidated into patterns/field-selection-guide.md -->
<!-- Archived: 2025-01-06 for disaster recovery only -->
<!-- DO NOT UPDATE: Make changes to the consolidated guide instead -->

# Fieldmark Design Principles and Best Practices for Field Research

## Introduction: Theory and Practice in Digital Field Recording

The design of digital field recording systems requires careful consideration of how data entry mechanisms shape both the quality of collected data and the efficiency of fieldwork. This comprehensive guide provides both theoretical foundations and practical implementation strategies for Fieldmark notebook design, drawing upon a decade of deployment experience across archaeological, ecological, and geoscientific research contexts.

We address two fundamental tensions in field data collection: the need for structured, high-quality data that supports computational analysis and long-term reuse, and the practical constraints of kinetic fieldwork where recording mechanisms must not impede observation and interpretation. We further consider how design decisions impact data FAIRness (Findability, Accessibility, Interoperability, and Reusability) without imposing undue burden on fieldworkers.

The selection of appropriate field types represents more than technical implementation – it embodies methodological decisions about data structure, analytical possibilities, and research outcomes. Poor field choices cascade through the entire research lifecycle, whilst thoughtful selection enhances both immediate usability and long-term research value.

## Theoretical Foundations

### Transparent Interaction in Field Contexts

The concept of "transparent interaction" (Weiser, 1991) suggests that the most profound technologies are those that disappear, weaving themselves into the fabric of everyday life until they are indistinguishable from it. In field recording, this means the technology should become an extension of the researcher's observational practice, not an impediment to it. Every design choice should reduce the cognitive and temporal distance between observation and record completion.

In kinetic fieldwork – where researchers move continuously through landscapes whilst making observations – the recording system must 'fade into the background' (Pascoe et al., 1998), allowing focus to remain on the archaeological or environmental phenomena under study. This theoretical foundation underpins our practical principles and implementation strategies.

### The Kinetic Fieldwork Context

Field recording occurs under conditions that would be considered hostile for most data entry tasks:

**Environmental and Physical Constraints:**
- Visual challenges: Direct sunlight making screens unreadable, dust and rain obscuring displays
- Physical impediments: Muddy or wet hands, thick gloves in cold conditions, carrying equipment
- Attention demands: Maintaining awareness of surroundings for safety and observation
- Time pressure: Limited site access, weather windows, or daylight hours
- Cognitive load: Complex interpretive decisions whilst managing recording

These constraints necessitate interface designs that prioritise robustness over sophistication. A simple radio button that works reliably with muddy fingers proves more valuable than an elegant multi-touch gesture that fails in wet conditions.

**The Temporality of Field Observation:**

Field observation exhibits distinct temporal patterns that recording systems must accommodate:
1. **Burst recording**: Intense periods of rapid data entry alternating with movement or excavation
2. **Progressive refinement**: Initial rapid capture followed by detailed documentation
3. **Retrospective correction**: Reinterpretation based on subsequent discoveries
4. **Collaborative elaboration**: Multiple team members contributing observations

These patterns argue for recording systems that support both rapid initial capture and subsequent enhancement, rather than enforcing comprehensive documentation at first encounter.

## Core Design Principles

### Principle 1: Minimise Recording Friction

This principle manifests in several practical imperatives:
- **Automate everything the system can know**: If information exists within the system (user identity, timestamp, location, parent record context), never require manual re-entry
- **Design for environmental extremes**: Assume bright sunlight, rain, cold fingers, wet screens, gloved hands, and exhausted fieldworkers at hour eight
- **Optimise for common cases**: Make frequent tasks exceptionally fast, even if rare tasks require slightly more effort
- **Respect device constraints**: On mobile devices with limited screen space, avoid UI patterns that demand extensive scrolling or precise touch targets

### Principle 2: Prefer Structure Over Unstructured Data

Controlled vocabularies – implemented through choice fields – should be deployed wherever feasible in preference to free-text entry. This preference stems not from technological determinism but from empirical observation: unstructured text collected in the field rarely achieves the analytical utility promised by its apparent flexibility.

**The False Dichotomy of Flexibility:**

The apparent trade-off between controlled vocabularies and descriptive freedom represents a false dichotomy. Fieldmark's annotation and uncertainty mechanisms provide sophisticated means to capture nuance, qualification, and contextual detail whilst maintaining structural integrity. A ceramic sherd can be classified as "Fine Ware" whilst simultaneously annotated with observations about unusual characteristics, preservation conditions, or interpretive uncertainty.

**Benefits of Structured Capture:**
- Immediate validation: Preventing data entry errors at the point of collection
- Cross-project comparability: Enabling meta-analysis across datasets
- Computational readiness: Supporting statistical analysis without extensive cleaning
- Multilingual accessibility: Allowing interface translation whilst maintaining data integrity
- Query efficiency: Enabling rapid filtering and aggregation

### Principle 3: Design for Data Lifecycle, Not Just Collection

Field recording systems must consider the entire data lifecycle from collection through analysis to long-term preservation and reuse:
- **Capture provenance automatically**: Who collected data, when, where, and under what project
- **Maintain referential integrity**: Ensure relationships between entities remain navigable
- **Enable progressive enhancement**: Allow initial rapid capture with subsequent detailed documentation
- **Support versioning and correction**: Acknowledge that field interpretations evolve

## FAIR Data Principles in Field Recording

### Findability Through Systematic Identification

The FAIR principles (Wilkinson et al., 2016) emphasise that data should be Findable, Accessible, Interoperable, and Reusable. In field recording, findability begins with systematic identification schemes that persist across the data lifecycle.

**Implementation Strategy:**
- Deploy TemplatedStringField for human-readable identifiers combining semantic components
- Implement hierarchical identification (project → site → context → sample)
- Consider persistent identifier schemes (DOI, IGSN) for samples and datasets
- Maintain identifier stability even as interpretations change

### Accessibility Through Structured Export

Accessibility requires that data can be retrieved in formats suitable for diverse analytical tools:
- **Tabular export**: CSV for statistical analysis, preserving relationships through foreign keys
- **Spatial export**: GeoJSON for GIS integration, maintaining coordinate system metadata
- **Hierarchical export**: JSON for complex nested relationships (when available)
- **Semantic export**: RDF or JSON-LD for knowledge graph integration (future capability)

### Interoperability Through Controlled Vocabularies

Interoperability emerges from the systematic use of shared vocabularies and ontologies:
- Adopt disciplinary standards where they exist (Getty AAT, PeriodO, Darwin Core)
- Document local vocabularies with clear definitions and mapping to standards
- Implement hierarchical vocabularies that allow both specific and general classification
- Maintain vocabulary versioning to track semantic evolution

### Reusability Through Comprehensive Metadata

Reusability depends upon rich contextual information:
- **Collection context**: Project goals, methodologies, sampling strategies
- **Technical metadata**: Device types, software versions, coordinate systems
- **Quality indicators**: Confidence levels, validation status, known limitations
- **Rights and attribution**: Licenses, embargoes, citation requirements

## Practical Implementation Principles

### Principle 4: Automate System-Knowable Information

Any information the system can determine should never require manual entry. This principle reduces errors, accelerates recording, and ensures consistency across datasets.

**System Variables Available:**
- `{{_CREATED_BY}}` – Current user (eliminates "Recorded by" fields)
- `{{_CREATED_TIME}}` – Timestamp of record creation
- Current GPS location via Take GPS Point
- Sequential identifiers through Auto-incrementing fields
- Parent record context through inheritance

**Implementation Patterns:**
Replace manual entry fields with automated capture:
- ❌ Text field for "Recorder name" → ✓ System variable in HRID
- ❌ DateTime field for "Entry time" → ✓ {{_CREATED_TIME}} in template
- ❌ Manual context copying → ✓ Parent-child relationships with inheritance

### Principle 5: Design for Progressive Disclosure

Complex recording scenarios benefit from conditional logic that reveals detail progressively based on initial assessments. This approach maintains form simplicity whilst enabling comprehensive documentation when necessary.

**Effective Patterns:**
1. **Binary Gateway**: Checkbox controlling detailed field visibility
2. **Type-Specific Recording**: Radio button selection revealing relevant field sets
3. **Confidence Cascades**: Uncertainty triggering additional documentation requirements
4. **Other Specification**: Controlled vocabulary with conditional free text for exceptions

### Principle 6: Optimise for Device Constraints

Field selection must acknowledge the realities of mobile data collection – small screens, touch interfaces, variable connectivity, and environmental challenges.

**Mobile-Optimised Selections:**
- Radio buttons over dropdowns for ≤7 options (larger touch targets)
- Checkbox for binary decisions (clear visual state)
- DateTime Now for timestamp capture (single tap)
- Take Photo over File Upload (integrated camera workflow)

**Desktop-Optimised Selections:**
- Multi-line text for extended narrative
- Hierarchical dropdowns for complex taxonomies
- Map drawing for precise spatial data
- File upload for diverse media types

### Principle 7: Maintain Human-Readable Identifiers

Whilst technically optional, human-readable identifiers (HRIDs) prove essential for practical data management. Without HRIDs, users confront opaque system identifiers (e.g., "rec-5f8a9b3c") that impede navigation, complicate analysis, and frustrate collaboration.

**HRID Design Patterns:**
- Archaeological: `{{site}}-{{trench}}-{{type}}-{{number}}`
- Ecological: `{{transect}}-{{point}}-{{date}}`
- Geological: `{{project}}-{{location}}-{{sample}}`

## Performance Considerations

### Cognitive Performance Factors

Before considering technical performance, we must acknowledge cognitive performance – the speed and accuracy with which fieldworkers can complete recording tasks:
- **Recognition over recall**: Select from lists rather than remember codes
- **Progressive disclosure**: Show complex options only when needed
- **Consistent patterns**: Use the same interaction patterns throughout
- **Clear feedback**: Immediate validation with actionable error messages

### Technical Performance Constraints

Field devices impose constraints that influence design decisions:

**Battery Consumption:**
- GPS fields consume significant power (10–15% per hour of continuous use)
- Camera operations drain battery during processing
- Screen brightness for outdoor visibility increases consumption
- Recommendation: Design workflows that allow GPS/camera activation only when needed

**Processing Limitations:**
- Complex conditional logic may cause visible lag on older devices
- Large vocabularies (>100 items) slow dropdown rendering
- Multiple photo captures require processing time between shots
- Recommendation: Implement progressive loading for large datasets

**Network Constraints:**
- Assume intermittent or absent connectivity
- Design for offline-first operation with opportunistic synchronisation
- Implement differential sync to minimise data transfer
- Cache all essential resources locally

### Documented Performance Thresholds

**Relationship Field Limits:**
- <50 relationships: Optimal performance
- 50–100 relationships: Noticeable lag
- 100–200 relationships: Significant delays
- >200 relationships: Effectively unusable

**Form Complexity:**
- Keep forms under 30 fields for mobile usability
- Limit sections to 10 fields for cognitive load
- Use conditional logic to reduce visible field count
- Consider splitting complex forms into multiple linked forms

## Field Type Selection Decision Framework

### Textual Data Capture

We present a hierarchical decision process for text field selection:

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

### Numeric Data Capture

Selection depends upon precision requirements and constraints:

1. **Are there known valid ranges?**
   - YES → Controlled Number field with min/max
   - NO → Continue to question 2

2. **Is this a sequential identifier?**
   - YES → Auto-incrementing field
   - NO → Basic Number field

3. **Consider additional factors:**
   - Decimal precision requirements
   - Default values to accelerate entry
   - Sticky behaviour for environmental constants
   - Unit specification in field labels

### Temporal Data Capture

Temporal granularity determines field selection:
- **Date only** → Date Picker (excavation date, sample date)
- **Date and time** → DateTime Picker (precise events)
- **Current moment** → DateTime Now (observation timestamp)
- **Month/year only** → Month Picker (seasonal data)

### Choice Field Selection

The number of options and selection constraints guide choice:

**Single Selection:**
- 2 options → Checkbox (if binary) or RadioGroup (if strings needed)
- 3–7 options → RadioGroup (all visible)
- 8–20 options → Select dropdown
- >20 options OR hierarchical → AdvancedSelect

**Multiple Selection:**
- Always use MultiSelect
- Enable expandedChecklist for <10 options
- Configure exclusiveOptions for mutually incompatible choices

### Spatial Data Capture

Spatial requirements determine appropriate fields:
- **Single point** → Take GPS Point
- **Boundaries/areas** → Map Field (requires internet)
- **Both needed** → Combine both field types
- **Manual coordinates** → Text field with validation

## Discipline-Specific Design Patterns

### Archaeological Recording Patterns

Archaeological recording exhibits specific characteristics that inform design decisions:

**Stratigraphic Relationships:**
- Temporal sequences (earlier than, later than, contemporary with)
- Physical relationships (cuts, cut by, fills, filled by)
- Spatial relationships (above, below, abuts, bonded to)
- Implementation: RelatedRecordSelector with semantic qualification

**Contextual Inheritance:**
- Finds inherit context properties (period, phase, grid square)
- Samples inherit environmental conditions
- Photos inherit spatial coordinates
- Implementation: Automatic property cascade in parent-child relationships

**Interpretive Uncertainty:**
- Provisional identifications pending specialist analysis
- Alternative interpretations of ambiguous features
- Confidence levels for dating and classification
- Implementation: Annotation fields and uncertainty qualifiers

### Ecological Survey Patterns

Ecological recording presents different requirements:

**Transect-Based Observation:**
- Sequential observation points along predetermined routes
- Repeated measures at fixed intervals
- Distance-based or time-based sampling
- Implementation: Auto-incrementing with location capture

**Abundance Estimation:**
- Percentage cover for vegetation
- Count estimates for mobile species
- Categorical abundance (DAFOR scale)
- Implementation: Controlled number fields with standard ranges

**Environmental Conditions:**
- Weather conditions affecting observations
- Phenological state of observed species
- Habitat characteristics
- Implementation: Sticky fields for conditions that remain constant

### Geological Sampling Patterns

Geological fieldwork requires specific accommodations:

**Sample Hierarchies:**
- Outcrop → Sample → Subsample → Analysis
- Maintaining provenance through processing
- Tracking splits and derivatives
- Implementation: Deep parent-child relationships with inheritance

**Orientation Data:**
- Strike and dip measurements
- Plunge and trend for linear features
- Multiple measurements per feature
- Implementation: Grouped number fields with validation

**Field Measurements:**
- Grain size, sorting, rounding
- Colour against standard charts
- Hardness, reaction to acid
- Implementation: Controlled vocabularies with standard scales

## Common Implementation Patterns

### The Measurement Pattern

Combine multiple fields for comprehensive measurement documentation:
1. Measurement type (RadioGroup/Select)
2. Numeric value (Controlled Number with range)
3. Units (incorporated in label or separate Select)
4. Uncertainty/precision (annotation or dedicated field)

### The Identification Pattern

Support confident and provisional identifications:
1. Quick identification (Select from common options)
2. Confidence level (RadioGroup: Certain/Probable/Possible)
3. Requires verification (Checkbox, conditional on confidence)
4. Detailed notes (Multi-line text, conditional on uncertainty)

### The Observation Pattern

Structure complex observations efficiently:
1. Observation type (RadioGroup for workflow branching)
2. Type-specific fields (conditional field groups)
3. Standard metadata (automatic via templates)
4. Media documentation (Take Photo with annotation)

## Advanced Capabilities and Their Implications

### Three-Tier Metadata Architecture

Fieldmark implements metadata at three levels, each serving distinct purposes:
1. **Record Metadata**: Who, when, where for every record (automatic capture)
2. **Field Metadata**: Annotation and uncertainty for individual observations
3. **Relationship Metadata**: Qualification of connections between entities

This architecture acknowledges that uncertainty and interpretation operate at multiple scales. A stratigraphic relationship might be certain whilst the dating of both contexts remains provisional.

### Semantic Relationship Qualification

Beyond simple parent-child relationships, Fieldmark enables semantic qualification of relationships:
- **Temporal**: "earlier than", "contemporary with", "redeposited from"
- **Physical**: "cuts", "bonds with", "same as"
- **Interpretive**: "possibly related to", "probably derived from"

This sophistication allows the recording system to capture interpretive reasoning, not just observational data.

### Automatic Versioning and Conflict Resolution

The append-only datastore provides complete version history without user intervention:
- Every change is preserved with timestamp and author
- Conflicting edits are resolved through merge strategies
- Previous interpretations remain accessible
- No data is ever truly deleted

This approach acknowledges that field interpretation is iterative and collaborative, with understanding emerging through discussion and revision.

## Vocabulary Development and Management

### Initial Development Process

1. **Literature Review**: Compile disciplinary standard terms
2. **Stakeholder Consultation**: Include local terminology
3. **Hierarchical Organisation**: Structure related terms appropriately
4. **Comprehensiveness vs Usability**: Balance completeness with efficiency

### Iterative Refinement Cycle

1. **Deploy Comprehensive Initial Vocabulary**
2. **Monitor Usage** (after 100+ records)
3. **Identify Rarely-Used Terms** (<5% selection rate)
4. **Relocate to "Other"** with annotation capability
5. **Document Changes** for data integration

### Vocabulary Versioning Strategy

- Maintain vocabulary change logs
- Preserve mappings between versions
- Plan for post-collection harmonisation
- Consider vocabulary expansion vs refinement

## Quality Assurance Through Field Design

### Validation Strategy

Implement validation at appropriate levels:
- **Field level**: Format, range, pattern matching
- **Section level**: Completeness checks
- **Form level**: Cross-field consistency (limited)
- **Workflow level**: Parent-child relationships

### Error Prevention Patterns

- Use controlled inputs over free text
- Provide clear helper text and examples
- Set appropriate default values
- Enable sticky fields for constants
- Mark only essential fields as required

### Data Integrity Measures

- Configure HRIDs for every form
- Establish clear parent-child hierarchies
- Document vocabulary semantics
- Plan for orphan management
- Design for export requirements

## Platform-Specific Adaptations

### Mobile-First Fields

When mobile devices predominate:
- Prefer touch-optimised inputs
- Minimise text entry requirements
- Leverage device sensors (GPS, camera)
- Design for offline resilience
- Account for screen size constraints

### Desktop-Enhanced Fields

When desktop entry is available:
- Enable complex text composition
- Support precise spatial drawing
- Facilitate bulk operations
- Leverage keyboard efficiency
- Utilise screen real estate

### Platform Parity Strategies

For mixed-device deployments:
- Identify platform-exclusive features
- Provide alternative workflows
- Document platform requirements
- Train users on platform differences
- Plan for data integration

## Recommendations for System Design

### For Notebook Designers

1. **Start with relationships**: Define entity relationships before designing forms
2. **Prioritise human-readable IDs**: Every entity needs meaningful identification
3. **Layer complexity**: Enable simple rapid capture with optional detail
4. **Test in conditions**: Evaluate designs outdoors, with gloves, in rain
5. **Document decisions**: Record why specific patterns were chosen

### For System Developers

1. **Optimise for common paths**: Make frequent operations exceptionally fast
2. **Fail gracefully**: Provide clear feedback when operations cannot complete
3. **Cache aggressively**: Assume network unreliability
4. **Respect battery**: Minimise GPS and camera activation
5. **Support correction**: Make it easy to fix mistakes

### For Project Managers

1. **Invest in vocabulary development**: Time spent on controlled vocabularies pays dividends
2. **Plan for data lifecycle**: Consider analysis and archiving from the start
3. **Train thoroughly**: Ensure teams understand both how and why
4. **Monitor usage**: Track which fields are used and which are skipped
5. **Iterate based on evidence**: Refine designs based on actual usage patterns

## Conclusion: Synthesis of Theory and Practice

Effective digital field recording emerges from the synthesis of theoretical understanding and practical experience. The principles articulated here – minimising friction, preferring structure, designing for lifecycle – provide the conceptual framework, whilst the specific patterns and recommendations translate these principles into actionable guidance.

The sophistication of Fieldmark's capabilities – particularly its relationship management, automatic versioning, granular metadata, and intelligent synchronisation – positions it as an exemplar of research-driven software development. These capabilities did not emerge from abstract software engineering but from sustained engagement with the realities of field research.

By understanding both the theoretical foundations and practical implications of design decisions, we can create digital recording systems that genuinely serve field research. The goal is not to digitise paper forms but to reimagine how digital tools can enhance our ability to observe, record, interpret, and share our understanding of the world.

The key to success lies not in dogmatic application of these principles, but in thoughtful adaptation to specific project contexts. Each design decision should consider the nature of the phenomena under study, the conditions of collection, the capabilities of available devices, and the ultimate analytical goals. When these factors align, digital field recording can simultaneously improve data quality and reduce fieldworker burden – achieving the long-sought goal of making technology truly serve, rather than constrain, field research.

Through careful attention to these principles and patterns, we enable the creation of robust, usable, and analytically powerful field recording systems. The iterative refinement of field selections, informed by actual usage patterns and emerging research questions, ensures that digital recording systems evolve alongside research programmes.

---

*This guide reflects current Fieldmark capabilities and deployment experience through 2024–2025. As the platform evolves and deployment experience accumulates, these recommendations will require periodic revision. We encourage notebook designers to document their own patterns and contribute to the collective understanding of effective field selection strategies.*