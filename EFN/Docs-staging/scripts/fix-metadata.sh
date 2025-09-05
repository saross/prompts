#!/bin/bash

# Fix number-fields-v05.md
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/number-fields-v05.md"
sed -i '1,15d' "$file"
sed -i '1i<!-- concat:boundary:start section="number-fields" -->\n<!-- concat:metadata\ndocument_id: number-fields-v05\ncategory: numeric\nfield_count: 3\ndesigner_capable: ["NumberField"]\njson_only: ["BasicAutoIncrementer", "step_increments"]\nlast_updated: 2025-01-05\n-->\n\n# Number Input Fields\n\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Date \& Time Fields](./datetime-fields-v05.md) | **Numeric Fields** | [Display Fields →](./display-field-v05.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Display Fields ↓](#display-fields) -->' "$file"

# Fix display-field-v05.md
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/display-field-v05.md"
sed -i '1,15d' "$file"
sed -i '1i<!-- concat:boundary:start section="display-fields" -->\n<!-- concat:metadata\ndocument_id: display-field-v05\ncategory: display\nfield_count: 1\ndesigner_capable: ["RichText"]\njson_only: ["html_content", "dynamic_generation"]\nlast_updated: 2025-01-05\n-->\n\n# Display Field - Fieldmark v3 Documentation\n\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Numeric Fields](./number-fields-v05.md) | **Display Fields** | [Location Fields →](./location-fields-v05.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Location Fields ↓](#location-fields) -->' "$file"

# Fix location-fields-v05.md
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/location-fields-v05.md"
sed -i '1,15d' "$file"
sed -i '1i<!-- concat:boundary:start section="location-fields" -->\n<!-- concat:metadata\ndocument_id: location-fields-v05\ncategory: location\nfield_count: 2\ndesigner_capable: ["TakePoint"]\njson_only: ["MapForm", "geometry_types", "map_layers"]\nlast_updated: 2025-01-05\n-->\n\n# Location Fields - Fieldmark v3 Documentation\n\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Display Fields](./display-field-v05.md) | **Location Fields** | [Media Fields →](./media-fields-v05.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Media Fields ↓](#media-fields) -->' "$file"

# Fix media-fields-v05.md
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/media-fields-v05.md"
sed -i '1,15d' "$file"
sed -i '1i<!-- concat:boundary:start section="media-fields" -->\n<!-- concat:metadata\ndocument_id: media-fields-v05\ncategory: media\nfield_count: 2\ndesigner_capable: ["TakePhoto", "FileUploader"]\njson_only: ["custom_upload_handlers", "file_type_restrictions"]\nlast_updated: 2025-01-05\n-->\n\n# Media Fields - Fieldmark v3 Documentation\n\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Location Fields](./location-fields-v05.md) | **Media Fields** | [Relationship Fields →](./relationship-field-v05.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Relationship Fields ↓](#relationship-fields) -->' "$file"

# Fix relationship-field-v05.md
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/relationship-field-v05.md"
sed -i '1,15d' "$file"
sed -i '1i<!-- concat:boundary:start section="relationship-fields" -->\n<!-- concat:metadata\ndocument_id: relationship-field-v05\ncategory: relationship\nfield_count: 1\ndesigner_capable: ["RelationshipField"]\njson_only: ["complex_rules", "cascading_relationships"]\nlast_updated: 2025-01-05\n-->\n\n# Relationship Field - Fieldmark v3 Documentation\n\n## Document Navigation\n<!-- concat:nav-mode:individual -->\n[← Media Fields](./media-fields-v05.md) | **Relationship Fields** | [Field Index →](../field-type-index.md)\n<!-- concat:nav-mode:concatenated -->\n<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) -->' "$file"

echo "Metadata sections fixed!"