# Fieldmark v3 Documentation Structure

<!-- concat:metadata
version: 3.0.0
last_updated: 2025-01-07
format: LLM_FIRST_CONCATENATABLE
structure: three_tier_depth_tagged
purpose: navigation_and_structure_only
-->

## Documentation System Overview

This documentation serves as both:
1. **Individual Files**: Modular documents for specific topics
2. **Concatenated Reference**: Single comprehensive document for LLM consumption (`reference.md`)

### Depth Tagging System

All content uses three depth levels:
- `{essential}` - Core concepts for basic understanding
- `{important}` - Standard patterns and working knowledge
- `{comprehensive}` - Complete reference with edge cases

### Navigation Structure

#### Field Documentation (`/field-categories/`)
Detailed documentation for each field type category:
- `text-fields-v05.md` - Text and string input fields
- `select-choice-fields-v05.md` - Selection and choice fields
- `datetime-fields-v05.md` - Date and time fields
- `number-fields-v05.md` - Numeric input fields
- `display-field-v05.md` - Display-only fields
- `location-fields-v05.md` - GPS and mapping fields
- `media-fields-v05.md` - Photo and file upload fields
- `relationship-field-v05.md` - Record relationship fields

#### Pattern Guides (`/patterns/`)
Cross-field patterns and implementation guidance:
- `field-selection-guide.md` - Choosing appropriate field types
- `form-structure-guide.md` - Form architecture patterns
- `dynamic-forms-guide.md` - Conditional logic and validation
- `implementation-patterns-guide.md` - Common implementation patterns

#### Technical References (`/references/`)
Core technical documentation:
- **`designer-component-mapping.md`** - 🔑 **PRIMARY REFERENCE** for all field mappings
- `component-reference.md` - Component namespaces and types
- `constraints-reference.md` - Security and Designer limitations
- `operations-reference.md` - Migration and troubleshooting
- `platform-reference.md` - Platform-specific behaviors
- `notebook-format-guide.md` - Notebook JSON structure
- `file-organization-guide.md` - Project structure

### For Complete Field Information

→ **See [Designer UI to Component Mapping Reference](./designer-component-mapping.md)**

This comprehensive reference contains:
- All Designer field names and their component mappings
- Complete component lists by namespace
- Configuration examples for each field type
- Common errors and solutions
- Migration guidance

---

## Building the Concatenated Reference

To generate `reference.md`:
```bash
./scripts/build-reference.sh
```

The build process:
1. Starts with this navigation structure
2. Adds all field-categories documents
3. Includes pattern guides
4. Appends technical references
5. Generates navigation anchors

Output: Single ~27,000 line reference optimized for LLM consumption.