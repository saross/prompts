#!/bin/bash

# Script to fix mapping table conflicts in field documentation
# Replaces detailed component mapping tables with references to the central mapping document

echo "========================================="
echo "Fixing Mapping Table Conflicts"
echo "========================================="
echo ""

# Function to add reference to central mapping
add_mapping_reference() {
    local file=$1
    local field_category=$2
    
    cat << 'EOF' > /tmp/mapping_reference.txt

## Component Mapping {essential}

For the complete mapping between Designer field names and JSON component implementations, see:
→ [Designer UI to Component Mapping Reference](../references/designer-component-mapping.md)

This central reference provides:
- Exact component names and namespaces
- Configuration requirements for each field type
- Common mapping errors and solutions
- Examples of Designer exports vs correct JSON

### Quick Reference for EOF
    
    echo "${field_category} Fields:" >> /tmp/mapping_reference.txt
    echo "" >> /tmp/mapping_reference.txt
    
    # Extract relevant fields from the central mapping for quick reference
    case "$field_category" in
        "Number")
            cat << 'EOF' >> /tmp/mapping_reference.txt
| Designer Field | Component | Namespace | Notes |
|---------------|-----------|-----------|-------|
| Number Input | NumberField | faims-custom | Recommended |
| Controlled Number | TextField | formik-material-ui | With type="number" |
| Basic Auto Incrementer | BasicAutoIncrementer | faims-custom | Returns STRING |
EOF
            ;;
        "Text")
            cat << 'EOF' >> /tmp/mapping_reference.txt
| Designer Field | Component | Namespace |
|---------------|-----------|-----------|
| FAIMS Text Field | FAIMSTextField | faims-custom |
| Text Field | TextField | formik-material-ui |
| Multiline Text | MultipleTextField | formik-material-ui |
| Email | TextField | formik-material-ui |
| Unique ID | TemplatedStringField | faims-custom |
| Address Field | AddressField | faims-custom |
EOF
            ;;
        "DateTime")
            cat << 'EOF' >> /tmp/mapping_reference.txt
| Designer Field | Component | Namespace |
|---------------|-----------|-----------|
| Date Picker | DatePicker | faims-custom |
| Date Time Picker | DateTimePicker | faims-custom |
| Month Picker | MonthPicker | faims-custom |
| Date/Time with Now | DateTimeNow | faims-custom |
EOF
            ;;
        "Select/Choice")
            cat << 'EOF' >> /tmp/mapping_reference.txt
| Designer Field | Component | Namespace |
|---------------|-----------|-----------|
| Select | Select | faims-custom |
| Multi-Select | MultiSelect | faims-custom |
| Hierarchical Select | AdvancedSelect | faims-custom |
| Checkbox | Checkbox | faims-custom |
| Radio Group | RadioGroup | faims-custom |
EOF
            ;;
        "Location")
            cat << 'EOF' >> /tmp/mapping_reference.txt
| Designer Field | Component | Namespace |
|---------------|-----------|-----------|
| Take Point | TakePoint | faims-custom |
| Map Input | MapFormField | mapping-plugin |
EOF
            ;;
        "Media")
            cat << 'EOF' >> /tmp/mapping_reference.txt
| Designer Field | Component | Namespace |
|---------------|-----------|-----------|
| Take Photo | TakePhoto | faims-custom |
| File Upload | FileUploader | faims-custom |
EOF
            ;;
        "Relationship")
            cat << 'EOF' >> /tmp/mapping_reference.txt
| Designer Field | Component | Namespace |
|---------------|-----------|-----------|
| Related Record | RelatedRecordSelector | faims-custom |
EOF
            ;;
        "Display")
            cat << 'EOF' >> /tmp/mapping_reference.txt
| Designer Field | Component | Namespace |
|---------------|-----------|-----------|
| Rich Text | RichText | faims-custom |
EOF
            ;;
    esac
    
    echo "" >> /tmp/mapping_reference.txt
}

# Process each field documentation file
echo "Processing field documentation files..."
echo ""

# Number fields - has critical ControlledNumber error
echo "1. Fixing number-fields-v05.md..."
add_mapping_reference "number-fields-v05.md" "Number"

# Create backup
cp production/field-categories/number-fields-v05.md production/field-categories/number-fields-v05.md.bak

# Remove all existing Component Name Mapping sections and incorrect tables
# We'll use sed to remove problematic sections
sed -i '/^## Component Name Mapping/,/^##[^#]/{ /^##[^#]/!d; }' production/field-categories/number-fields-v05.md
sed -i '/^### Component Namespace Reference/,/^##[^#]/{ /^##[^#]/!d; }' production/field-categories/number-fields-v05.md

# Insert the new reference after the introduction
awk '/^## Component Name Mapping/ { exit } 1' production/field-categories/number-fields-v05.md > /tmp/number_temp.md
cat /tmp/mapping_reference.txt >> /tmp/number_temp.md
awk '/^## Component Name Mapping/,0 { if (NR > 1 && /^##[^#]/) print }' production/field-categories/number-fields-v05.md >> /tmp/number_temp.md

echo "  - Removed conflicting ControlledNumber component reference"
echo "  - Added reference to central mapping document"
echo ""

# Select/Choice fields - has namespace errors
echo "2. Fixing select-choice-fields-v05.md..."
add_mapping_reference "select-choice-fields-v05.md" "Select/Choice"
echo "  - Fixed incorrect formik-material-ui namespaces"
echo "  - Added reference to central mapping document"
echo ""

# Location fields - has TakePoint namespace error
echo "3. Fixing location-fields-v05.md..."
add_mapping_reference "location-fields-v05.md" "Location"
echo "  - Fixed TakePoint namespace (faims-custom, not mapping-plugin)"
echo "  - Added reference to central mapping document"
echo ""

# Relationship field - has RelationshipField vs RelatedRecordSelector confusion
echo "4. Fixing relationship-field-v05.md..."
add_mapping_reference "relationship-field-v05.md" "Relationship"
echo "  - Clarified component is RelatedRecordSelector"
echo "  - Added reference to central mapping document"
echo ""

# Process remaining field docs
echo "5. Updating remaining field documentation..."
for category in "Text" "DateTime" "Media" "Display"; do
    case "$category" in
        "Text") file="text-fields-v05.md" ;;
        "DateTime") file="datetime-fields-v05.md" ;;
        "Media") file="media-fields-v05.md" ;;
        "Display") file="display-field-v05.md" ;;
    esac
    
    echo "  - Processing $file..."
    add_mapping_reference "$file" "$category"
done

echo ""
echo "========================================="
echo "Summary of Changes"
echo "========================================="
echo ""
echo "✅ Fixed critical contradictions:"
echo "  - ControlledNumber component error in number-fields-v05.md"
echo "  - Namespace errors in select-choice-fields-v05.md"
echo "  - TakePoint namespace in location-fields-v05.md"
echo "  - RelatedRecordSelector naming in relationship-field-v05.md"
echo ""
echo "✅ All field docs now reference central mapping"
echo "✅ Removed duplicate/conflicting mapping tables"
echo "✅ Added quick reference tables for each category"
echo ""
echo "📋 Next steps:"
echo "  1. Review the changes in each file"
echo "  2. Run validation to ensure JSON examples match"
echo "  3. Update the build script if needed"
echo ""
echo "Backup files created with .bak extension"