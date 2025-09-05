#!/bin/bash

# Add component name mapping tables to remaining field documentation

echo "Adding component mapping tables to field documentation..."

# DateTime Fields
cat > /tmp/datetime-table.txt << 'EOF'
## Component Name Mapping {essential}

| Designer UI Label | JSON component-name | Namespace | Code File | Description |
|------------------|-------------------|-----------|-----------|-------------|
| Date Time Now | DateTimeNow | faims-custom | DateTimeNow.tsx | Auto-populated timestamp |
| Date Time Picker | DateTimePicker | faims-custom | DateTimePicker.tsx | Date and time selection |
| Date Picker | DatePicker | faims-custom | DatePicker.tsx | Date-only selection |
| Month Picker | MonthPicker | faims-custom | MonthPicker.tsx | Month/year selection |

### Critical Naming Issues {important}
- **Auto-population confusion**: DateTimeNow can be configured to NOT auto-populate via checkbox
- **Picker variations**: All pickers look similar in Designer but have different behaviors
- **Format limitations**: Custom formats require JSON configuration
- **Timezone handling**: All dates stored in local time without timezone info
EOF

# Number Fields
cat > /tmp/number-table.txt << 'EOF'
## Component Name Mapping {essential}

| Designer UI Label | JSON component-name | Namespace | Code File | Description |
|------------------|-------------------|-----------|-----------|-------------|
| Number Field | NumberField | faims-custom | NumberField.tsx | Numeric input with validation |
| Basic Auto Incrementer | BasicAutoIncrementer | faims-custom | BasicAutoIncrementer.tsx | Auto-incrementing counter |

### Critical Naming Issues {important}
- **ControlledNumber absence**: Referenced in docs but is actually TextField with type="number"
- **Step increment confusion**: Cannot set step increments in Designer, use BasicAutoIncrementer instead
- **TextField variant**: "Controlled Number" is TextField (formik-material-ui) with numeric configuration
- **Namespace discrepancy**: All number fields use faims-custom namespace
EOF

# Display Field
cat > /tmp/display-table.txt << 'EOF'
## Component Name Mapping {essential}

| Designer UI Label | JSON component-name | Namespace | Code File | Description |
|------------------|-------------------|-----------|-----------|-------------|
| Rich Text | RichText | faims-custom | RichText.tsx | Display-only formatted content |

### Critical Naming Issues {important}
- **Single component**: Only one display field type available
- **Not a field**: Despite being called a "field", captures no data
- **Memory leaks**: Known performance issues on mobile devices
- **Markdown limitations**: Tables stripped, external images blocked at runtime
EOF

# Location Fields
cat > /tmp/location-table.txt << 'EOF'
## Component Name Mapping {essential}

| Designer UI Label | JSON component-name | Namespace | Code File | Description |
|------------------|-------------------|-----------|-----------|-------------|
| Take GPS Point | TakePoint | mapping-plugin | TakePoint.tsx | GPS coordinate capture |
| Map Form Field | MapFormField | mapping-plugin | MapFormField.tsx | Interactive map drawing |

### Critical Naming Issues {important}
- **Plugin namespace**: Both use mapping-plugin, not faims-custom
- **MapForm variations**: Sometimes "MapFormField", sometimes "MapForm" in docs
- **Designer limitations**: MapFormField configuration mostly JSON-only
- **Accuracy confusion**: GPS accuracy thresholds not enforced despite UI
EOF

# Media Fields
cat > /tmp/media-table.txt << 'EOF'
## Component Name Mapping {essential}

| Designer UI Label | JSON component-name | Namespace | Code File | Description |
|------------------|-------------------|-----------|-----------|-------------|
| Take Photo | TakePhoto | faims-custom | TakePhoto.tsx | Camera capture & gallery |
| File Uploader | FileUploader | faims-custom | FileUploader.tsx | General file attachment |

### Critical Naming Issues {important}
- **TakePhoto misnomer**: Also handles gallery selection, not just camera
- **Required validation broken**: Known issue with required field validation
- **File type restrictions**: Cannot actually restrict file types despite settings
- **Silent failures**: Upload errors often fail silently
EOF

# Relationship Field
cat > /tmp/relationship-table.txt << 'EOF'
## Component Name Mapping {essential}

| Designer UI Label | JSON component-name | Namespace | Code File | Description |
|------------------|-------------------|-----------|-----------|-------------|
| Related Record Selector | RelationshipField | faims-custom | RelationshipField.tsx | Record linking |

### Critical Naming Issues {important}
- **Component name mismatch**: Designer shows "Related Record Selector" but component is "RelationshipField"
- **Type confusion**: Returns faims-core::Array, not a custom Relationship type
- **Child vs Linked**: Can switch between modes in Designer but affects behavior significantly
- **Performance critical**: Degrades rapidly with >50 relationships
EOF

# Now insert these tables into the documents

# DateTime
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/datetime-fields-v05.md"
if ! grep -q "## Component Name Mapping" "$file"; then
    echo "Adding component table to datetime-fields..."
    # Find line with "## Overview" and insert after the overview section
    awk '/^## Overview \{essential\}/ {print; getline; print; getline; print; while ((getline line < "/tmp/datetime-table.txt") > 0) {print line}; close("/tmp/datetime-table.txt"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
fi

# Number
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/number-fields-v05.md"
if ! grep -q "## Component Name Mapping" "$file"; then
    echo "Adding component table to number-fields..."
    awk '/^## Overview \{essential\}/ {print; getline; print; getline; print; getline; print; while ((getline line < "/tmp/number-table.txt") > 0) {print line}; close("/tmp/number-table.txt"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
fi

# Display
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/display-field-v05.md"
if ! grep -q "## Component Name Mapping" "$file"; then
    echo "Adding component table to display-field..."
    awk '/^## Overview \{essential\}/ {print; getline; print; getline; print; getline; print; getline; print; while ((getline line < "/tmp/display-table.txt") > 0) {print line}; close("/tmp/display-table.txt"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
fi

# Location
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/location-fields-v05.md"
if ! grep -q "## Component Name Mapping" "$file"; then
    echo "Adding component table to location-fields..."
    awk '/^## Overview \{essential\}/ {print; getline; print; getline; print; getline; print; getline; print; while ((getline line < "/tmp/location-table.txt") > 0) {print line}; close("/tmp/location-table.txt"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
fi

# Media
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/media-fields-v05.md"
if ! grep -q "## Component Name Mapping" "$file"; then
    echo "Adding component table to media-fields..."
    awk '/^## Overview \{essential\}/ {print; getline; print; getline; print; getline; print; getline; print; while ((getline line < "/tmp/media-table.txt") > 0) {print line}; close("/tmp/media-table.txt"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
fi

# Relationship
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/relationship-field-v05.md"
if ! grep -q "## Component Name Mapping" "$file"; then
    echo "Adding component table to relationship-field..."
    awk '/^## Overview \{essential\}/ {print; getline; print; getline; print; getline; print; getline; print; while ((getline line < "/tmp/relationship-table.txt") > 0) {print line}; close("/tmp/relationship-table.txt"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
fi

# Cleanup
rm -f /tmp/datetime-table.txt /tmp/number-table.txt /tmp/display-table.txt /tmp/location-table.txt /tmp/media-table.txt /tmp/relationship-table.txt

echo "Component mapping tables added successfully!"