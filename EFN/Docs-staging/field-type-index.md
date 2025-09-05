# Fieldmark v3 Field Type Documentation Index

<!-- concat:metadata
version: 3.0.0
last_updated: 2025-01-05
total_field_types: 23
format: LLM_FIRST_CONCATENATABLE
structure: three_tier_depth_tagged
-->

## Documentation Structure

This documentation system serves as both:
1. **Individual Files**: Navigate to specific documents for maintenance and focused editing
2. **Concatenated Reference**: Single comprehensive document for LLM consumption (`reference.md`)

### Depth Tagging System

All content is tagged with one of three depth levels:
- `{essential}` - Core concepts required for basic use (5-minute comprehension target)
- `{important}` - Standard patterns and working knowledge for effective use
- `{comprehensive}` - Complete reference including edge cases, performance implications, and technical details

### Navigation Methods

#### When Using Individual Files
- Click document links below to open specific field category documentation
- Each document contains navigation headers and footers for moving between related content
- Cross-references link to other files in the documentation system

#### When Using Concatenated Reference (reference.md)
- Use section anchors to jump directly to specific field categories
- All cross-references become internal anchor links
- Single file contains complete documentation system

---

## Field Type Catalog

### 1. Text & Input Fields
<!-- concat:section-id="text-input-fields" -->
- **Document**: [text-fields-v05.md](./field-categories/text-fields-v05.md)
- **Anchor**: [#text-input-fields](#text-input-fields) (in concatenated reference)
- **Field Types**: 7 components
  - `TextField` - Single-line text input
  - `FAIMSTextField` - Enhanced text with compute support
  - `MultipleTextField` - Multi-value text entries
  - `TemplatedStringField` - Dynamic string interpolation
  - `AddressField` - Structured address capture
  - `QRCodeFormField` - QR code scanner input
  - `RichText` - Formatted text editor
- **Designer Coverage**: Partial
  - ✅ Designer: TextField, FAIMSTextField, MultipleTextField basic config
  - 🔧 Enhanced: Validation patterns, helper text, conditional display
  - 📝 JSON-only: compute_value, template syntax, regex validation
- **Common Use Cases**: Names, descriptions, codes, addresses, notes, formatted content

### 2. Selection & Choice Fields
<!-- concat:section-id="selection-fields" -->
- **Document**: [select-choice-fields-v05.md](./field-categories/select-choice-fields-v05.md)
- **Anchor**: [#selection-fields](#selection-fields) (in concatenated reference)
- **Field Types**: 5 components
  - `Checkbox` - Multiple choice with checkboxes
  - `Select` - Single choice dropdown
  - `MultiSelect` - Multiple choice dropdown
  - `RadioGroup` - Single choice with radio buttons
  - `AdvancedSelect` - Hierarchical selection with search
- **Designer Coverage**: Full
  - ✅ Designer: All basic configurations including options
  - 🔧 Enhanced: Dynamic options, dependent selects
  - 📝 JSON-only: Option generation, API-driven choices
- **Common Use Cases**: Categories, types, multiple selections, hierarchical data, filters

### 3. Date & Time Fields
<!-- concat:section-id="datetime-fields" -->
- **Document**: [datetime-fields-v05.md](./field-categories/datetime-fields-v05.md)
- **Anchor**: [#datetime-fields](#datetime-fields) (in concatenated reference)
- **Field Types**: 4 components
  - `DateTimeNow` - Auto-populated current timestamp
  - `DateTimePicker` - Date and time selection
  - `DatePicker` - Date-only selection
  - `MonthPicker` - Month/year selection
- **Designer Coverage**: Full
  - ✅ Designer: All date/time configurations
  - 🔧 Enhanced: Custom formats, validation ranges
  - 📝 JSON-only: compute_value for calculated dates
- **Common Use Cases**: Timestamps, event dates, scheduling, date ranges, audit trails

### 4. Numeric Fields
<!-- concat:section-id="number-fields" -->
- **Document**: [number-fields-v05.md](./field-categories/number-fields-v05.md)
- **Anchor**: [#number-fields](#number-fields) (in concatenated reference)
- **Field Types**: 3 components
  - `NumberField` - Numeric input with validation
  - `ControlledNumber` - TextField variant for numbers
  - `BasicAutoIncrementer` - Auto-incrementing counter
- **Designer Coverage**: Partial
  - ✅ Designer: NumberField basic configuration
  - 🔧 Enhanced: Min/max, decimal places, units
  - 📝 JSON-only: Step increments via BasicAutoIncrementer
- **Common Use Cases**: Measurements, counts, IDs, quantities, calculations

### 5. Location & Mapping Fields
<!-- concat:section-id="location-fields" -->
- **Document**: [location-fields-v05.md](./field-categories/location-fields-v05.md)
- **Anchor**: [#location-fields](#location-fields) (in concatenated reference)
- **Field Types**: 2 components
  - `TakePoint` - GPS point capture
  - `MapForm` - Interactive map with geometry drawing
- **Designer Coverage**: Limited
  - ✅ Designer: Basic GPS capture setup
  - 📝 JSON-only: Map configuration, geometry types, layers
- **Common Use Cases**: Site locations, GPS coordinates, areas, routes, spatial data

### 6. Media & File Fields
<!-- concat:section-id="media-fields" -->
- **Document**: [media-fields-v05.md](./field-categories/media-fields-v05.md)
- **Anchor**: [#media-fields](#media-fields) (in concatenated reference)
- **Field Types**: 2 components
  - `TakePhoto` - Camera capture and gallery selection
  - `FileUploader` - General file attachment
- **Designer Coverage**: Full
  - ✅ Designer: All media configurations
  - 🔧 Enhanced: File type restrictions, size limits
  - 📝 JSON-only: Custom upload handlers
- **Common Use Cases**: Photos, documents, audio recordings, evidence collection

### 7. Display Fields
<!-- concat:section-id="display-fields" -->
- **Document**: [display-field-v05.md](./field-categories/display-field-v05.md)
- **Anchor**: [#display-fields](#display-fields) (in concatenated reference)
- **Field Types**: 1 component
  - `RichText` - Display-only formatted content
- **Designer Coverage**: Partial
  - ✅ Designer: Basic rich text content
  - 📝 JSON-only: HTML content, dynamic generation
- **Common Use Cases**: Instructions, warnings, help text, formatted information display

### 8. Relationship Fields
<!-- concat:section-id="relationship-fields" -->
- **Document**: [relationship-field-v05.md](./field-categories/relationship-field-v05.md)
- **Anchor**: [#relationship-fields](#relationship-fields) (in concatenated reference)
- **Field Types**: 1 component
  - `RelationshipField` - Links between records
- **Designer Coverage**: Partial
  - ✅ Designer: Basic relationship setup
  - 📝 JSON-only: Complex relationship rules, cascading
- **Common Use Cases**: Parent-child records, linked entities, hierarchical data

---

## Cross-Field Patterns
<!-- concat:section-id="cross-field-patterns" -->

Documentation covering functionality that spans multiple field types:

### Validation Patterns
- **Document**: [validation.md](./detail-crossfield-docs/validation.md)
- **Anchor**: [#validation-patterns](#validation-patterns) (in concatenated reference)
- **Coverage**: Validation strategies across all field types

### Conditional Logic
- **Document**: [conditional-logic.md](./detail-crossfield-docs/conditional-logic.md)
- **Anchor**: [#conditional-logic](#conditional-logic) (in concatenated reference)
- **Coverage**: Show/hide logic, dependent fields, dynamic behavior

### Form Navigation
- **Document**: [navigation.md](./detail-crossfield-docs/navigation.md)
- **Anchor**: [#form-navigation](#form-navigation) (in concatenated reference)
- **Coverage**: Multi-step forms, progress tracking, navigation patterns

### Notebook Structure
- **Document**: [notebook-structure.md](./detail-crossfield-docs/notebook-structure.md)
- **Anchor**: [#notebook-structure](#notebook-structure) (in concatenated reference)
- **Coverage**: Overall form architecture, sections, organization

### Common Patterns
- **Document**: [patterns.md](./detail-crossfield-docs/patterns.md)
- **Anchor**: [#common-patterns](#common-patterns) (in concatenated reference)
- **Coverage**: Reusable patterns, best practices, common solutions

---

## Technical References
<!-- concat:section-id="technical-references" -->

### Component Reference
- **Documents**: 
  - [component-namespace-reference.md](./reference-docs/component-namespace-reference.md)
  - [meta-properties-reference.md](./reference-docs/meta-properties-reference.md)
  - [formik-integration-reference.md](./reference-docs/formik-integration-reference.md)
- **Anchor**: [#component-reference](#component-reference) (in concatenated reference)
- **Coverage**: Component architecture, properties, integration details

### Platform Reference
- **Documents**:
  - [platform-behaviors-reference.md](./reference-docs/platform-behaviors-reference.md)
  - [performance-thresholds-reference.md](./reference-docs/performance-thresholds-reference.md)
  - [accessibility-reference.md](./reference-docs/accessibility-reference.md)
- **Anchor**: [#platform-reference](#platform-reference) (in concatenated reference)
- **Coverage**: Platform-specific behaviors, performance limits, accessibility

### Operations Reference
- **Documents**:
  - [migration-strategies-reference.md](./reference-docs/migration-strategies-reference.md)
  - [troubleshooting-framework-reference.md](./reference-docs/troubleshooting-framework-reference.md)
  - [data-export-reference.md](./reference-docs/data-export-reference.md)
- **Anchor**: [#operations-reference](#operations-reference) (in concatenated reference)
- **Coverage**: Migration paths, debugging, data management

### Constraints Reference
- **Documents**:
  - [designer-limitations-reference.md](./reference-docs/designer-limitations-reference.md)
  - [security-considerations-reference.md](./reference-docs/security-considerations-reference.md)
  - [validation-timing-reference.md](./reference-docs/validation-timing-reference.md)
- **Anchor**: [#constraints-reference](#constraints-reference) (in concatenated reference)
- **Coverage**: Known limitations, security rules, validation lifecycle

---

## Using This Documentation

### For Individual File Maintenance
1. Navigate to specific documents using the links above
2. Edit individual files for focused updates
3. Use git to track changes per document
4. Cross-references use relative file paths

### For LLM Consumption
1. Run `./scripts/build-reference.sh` to generate `reference.md`
2. Load the single concatenated file into the LLM
3. All documentation is available in one context
4. Cross-references work as internal anchors

### For Human Documentation Generation
Extract subsets based on depth tags:
- **Quick Start Guide**: Extract all `{essential}` sections
- **User Reference**: Extract `{essential}` + `{important}` sections
- **Complete Reference**: Include all sections including `{comprehensive}`

### Documentation Maintenance
1. Always edit individual source files (never edit reference.md directly)
2. Regenerate reference.md after changes using the build script
3. Commit both source files and regenerated reference.md
4. Tag releases when documentation milestones are reached

---

## Quick Reference Matrix

| Field Category | Designer Coverage | Field Count | Primary Use Case |
|---------------|------------------|-------------|------------------|
| Text & Input | Partial | 7 | Text data capture |
| Selection | Full | 5 | Categorical choices |
| Date & Time | Full | 4 | Temporal data |
| Numeric | Partial | 3 | Quantitative data |
| Location | Limited | 2 | Spatial data |
| Media | Full | 2 | File attachments |
| Display | Partial | 1 | Information display |
| Relationship | Partial | 1 | Record linking |

---

## Version History

- **3.0.0** (2025-01-05): Complete reorganization for LLM-first documentation
- **2.0.0** (2024): Addition of NEW format fields (display, location, media, relationship)
- **1.0.0** (2023): Initial documentation for core field types