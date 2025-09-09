#!/bin/bash

# Process number-fields
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/number-fields-v05.md"
if ! grep -q "concat:boundary:start" "$file"; then
  # Add header
  sed -i '1s/^/<!-- concat:boundary:start section="number-fields" -->\n<!-- concat:metadata\ndocument_id: number-fields-v05\ncategory: numeric\nfield_count: 3\ndesigner_capable: ["NumberField"]\njson_only: ["BasicAutoIncrementer", "step_increments"]\nlast_updated: 2025-01-05\n-->\n\n/' "$file"
  sed -i '5a\\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Date \& Time Fields](./datetime-fields-v05.md) | **Numeric Fields** | [Display Fields →](./display-field-v05.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Display Fields ↓](#display-fields) -->' "$file"
  # Add footer
  echo '
---

## Related Documentation
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Date & Time Fields](./datetime-fields-v05.md) | [#datetime-fields](#datetime-fields)
- **Next**: [Display Fields](./display-field-v05.md) | [#display-fields](#display-fields)

### Cross-Field Patterns
- **Validation**: [Number Validation](../detail-crossfield-docs/validation.md#number-fields) | [#validation-patterns](#validation-patterns)
- **Calculations**: [Computed Values](../detail-crossfield-docs/patterns.md#calculations) | [#common-patterns](#common-patterns)

### Technical References
- **Designer Limitations**: [Number Constraints](../reference-docs/designer-limitations-reference.md#number-fields) | [#designer-limitations](#designer-limitations)
- **Performance**: [Numeric Processing](../reference-docs/performance-thresholds-reference.md#number-fields) | [#performance-thresholds](#performance-thresholds)

<!-- /concat:references -->
<!-- concat:boundary:end section="number-fields" -->' >> "$file"
fi

# Process display-field
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/display-field-v05.md"
if ! grep -q "concat:boundary:start" "$file"; then
  sed -i '1s/^/<!-- concat:boundary:start section="display-fields" -->\n<!-- concat:metadata\ndocument_id: display-field-v05\ncategory: display\nfield_count: 1\ndesigner_capable: ["RichText"]\njson_only: ["html_content", "dynamic_generation"]\nlast_updated: 2025-01-05\n-->\n\n/' "$file"
  sed -i '5a\\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Numeric Fields](./number-fields-v05.md) | **Display Fields** | [Location Fields →](./location-fields-v05.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Location Fields ↓](#location-fields) -->' "$file"
  echo '
---

## Related Documentation
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Numeric Fields](./number-fields-v05.md) | [#number-fields](#number-fields)
- **Next**: [Location Fields](./location-fields-v05.md) | [#location-fields](#location-fields)
- **Similar**: [Text Fields - RichText](./text-fields-v05.md#richtext) | [#text-input-fields](#text-input-fields)

### Cross-Field Patterns
- **Instructions**: [Form Help Text](../detail-crossfield-docs/patterns.md#instructions) | [#common-patterns](#common-patterns)
- **Conditional Display**: [Dynamic Content](../detail-crossfield-docs/conditional-logic.md#display-fields) | [#conditional-logic](#conditional-logic)

### Technical References
- **Security**: [HTML Sanitization](../reference-docs/security-considerations-reference.md#display-fields) | [#security-considerations](#security-considerations)
- **Performance**: [Rendering Limits](../reference-docs/performance-thresholds-reference.md#display-fields) | [#performance-thresholds](#performance-thresholds)

<!-- /concat:references -->
<!-- concat:boundary:end section="display-fields" -->' >> "$file"
fi

# Process location-fields
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/location-fields-v05.md"
if ! grep -q "concat:boundary:start" "$file"; then
  sed -i '1s/^/<!-- concat:boundary:start section="location-fields" -->\n<!-- concat:metadata\ndocument_id: location-fields-v05\ncategory: location\nfield_count: 2\ndesigner_capable: ["TakePoint"]\njson_only: ["MapForm", "geometry_types", "map_layers"]\nlast_updated: 2025-01-05\n-->\n\n/' "$file"
  sed -i '5a\\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Display Fields](./display-field-v05.md) | **Location Fields** | [Media Fields →](./media-fields-v05.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Media Fields ↓](#media-fields) -->' "$file"
  echo '
---

## Related Documentation
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Display Fields](./display-field-v05.md) | [#display-fields](#display-fields)
- **Next**: [Media Fields](./media-fields-v05.md) | [#media-fields](#media-fields)

### Cross-Field Patterns
- **Validation**: [Location Accuracy](../detail-crossfield-docs/validation.md#location-fields) | [#validation-patterns](#validation-patterns)
- **Field Dependencies**: [GPS Requirements](../detail-crossfield-docs/conditional-logic.md#location-fields) | [#conditional-logic](#conditional-logic)

### Technical References
- **Platform Behaviors**: [GPS Handling](../reference-docs/platform-behaviors-reference.md#location-fields) | [#platform-behaviors](#platform-behaviors)
- **Performance**: [Map Rendering](../reference-docs/performance-thresholds-reference.md#location-fields) | [#performance-thresholds](#performance-thresholds)

<!-- /concat:references -->
<!-- concat:boundary:end section="location-fields" -->' >> "$file"
fi

# Process media-fields
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/media-fields-v05.md"
if ! grep -q "concat:boundary:start" "$file"; then
  sed -i '1s/^/<!-- concat:boundary:start section="media-fields" -->\n<!-- concat:metadata\ndocument_id: media-fields-v05\ncategory: media\nfield_count: 2\ndesigner_capable: ["TakePhoto", "FileUploader"]\njson_only: ["custom_upload_handlers", "file_type_restrictions"]\nlast_updated: 2025-01-05\n-->\n\n/' "$file"
  sed -i '5a\\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Location Fields](./location-fields-v05.md) | **Media Fields** | [Relationship Fields →](./relationship-field-v05.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Relationship Fields ↓](#relationship-fields) -->' "$file"
  echo '
---

## Related Documentation
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Location Fields](./location-fields-v05.md) | [#location-fields](#location-fields)
- **Next**: [Relationship Fields](./relationship-field-v05.md) | [#relationship-fields](#relationship-fields)

### Cross-Field Patterns
- **Validation**: [File Size Limits](../detail-crossfield-docs/validation.md#media-fields) | [#validation-patterns](#validation-patterns)
- **Platform Specific**: [Camera Access](../detail-crossfield-docs/patterns.md#platform-specific) | [#common-patterns](#common-patterns)

### Technical References
- **Platform Behaviors**: [Media Handling](../reference-docs/platform-behaviors-reference.md#media-fields) | [#platform-behaviors](#platform-behaviors)
- **Performance**: [Upload Limits](../reference-docs/performance-thresholds-reference.md#media-fields) | [#performance-thresholds](#performance-thresholds)
- **Security**: [File Validation](../reference-docs/security-considerations-reference.md#media-fields) | [#security-considerations](#security-considerations)

<!-- /concat:references -->
<!-- concat:boundary:end section="media-fields" -->' >> "$file"
fi

# Process relationship-field
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/relationship-field-v05.md"
if ! grep -q "concat:boundary:start" "$file"; then
  sed -i '1s/^/<!-- concat:boundary:start section="relationship-fields" -->\n<!-- concat:metadata\ndocument_id: relationship-field-v05\ncategory: relationship\nfield_count: 1\ndesigner_capable: ["RelationshipField"]\njson_only: ["complex_rules", "cascading_relationships"]\nlast_updated: 2025-01-05\n-->\n\n/' "$file"
  sed -i '5a\\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Media Fields](./media-fields-v05.md) | **Relationship Fields** | [Field Index →](../field-type-index.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) -->' "$file"
  echo '
---

## Related Documentation
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Media Fields](./media-fields-v05.md) | [#media-fields](#media-fields)
- **Index**: [Field Documentation Index](../field-type-index.md) | [#fieldmark-v3-field-type-documentation-index](#fieldmark-v3-field-type-documentation-index)

### Cross-Field Patterns
- **Hierarchical Data**: [Parent-Child Records](../detail-crossfield-docs/patterns.md#hierarchical) | [#common-patterns](#common-patterns)
- **Conditional Logic**: [Dependent Records](../detail-crossfield-docs/conditional-logic.md#relationship-fields) | [#conditional-logic](#conditional-logic)

### Technical References
- **Designer Limitations**: [Relationship Constraints](../reference-docs/designer-limitations-reference.md#relationship-fields) | [#designer-limitations](#designer-limitations)
- **Data Export**: [Relationship Handling](../reference-docs/data-export-reference.md#relationships) | [#data-export](#data-export)

<!-- /concat:references -->
<!-- concat:boundary:end section="relationship-fields" -->' >> "$file"
fi

echo "Navigation added to all documents!"