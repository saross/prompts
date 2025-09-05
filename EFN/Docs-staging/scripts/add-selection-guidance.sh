#!/bin/bash

# Add field selection guidance to all field documentation

echo "Adding field selection guidance sections..."

# Text Fields
cat > /tmp/text-selection.txt << 'EOF'

## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| Short identifiers (<50 chars) | FAIMSTextField | Single-line, clean display |
| Long descriptions | MultipleTextField | Multi-line with scrolling |
| Email addresses | TextField (Email) | Built-in validation |
| Auto-generated IDs | TemplatedStringField | Consistent formatting |
| Physical addresses | AddressField | Structured components |
| Barcode scanning | QRCodeFormField | Mobile camera integration |
| Instructions/Help | RichText | Formatted display only |

### Decision Criteria
- **Data length**: <50 chars → FAIMSTextField, >50 chars → MultipleTextField
- **Validation needed**: Email → TextField, Pattern → TemplatedStringField
- **User input**: Yes → FAIMSTextField/MultipleTextField, No → RichText
- **Mobile scanning**: Required → QRCodeFormField
- **Address structure**: Needed → AddressField
EOF

# Selection Fields  
cat > /tmp/selection-selection.txt << 'EOF'

## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| Yes/No questions | Checkbox | Clear boolean state |
| Single choice (<10 options) | Select | Compact dropdown |
| Single choice (>10 options) | Select | Searchable dropdown |
| Multiple choices | MultiSelect | Multi-select dropdown |
| Hierarchical categories | AdvancedSelect | Tree navigation |
| ~~Visible options~~ | ~~RadioGroup~~ | Deprecated - use Select |

### Decision Criteria
- **Number of options**: <10 → Select, >10 → Select with search, Hierarchical → AdvancedSelect
- **Selection count**: Single → Select, Multiple → MultiSelect, Boolean → Checkbox
- **Visibility**: All dropdowns hide options until opened (RadioGroup deprecated)
- **Data structure**: Flat → Select/MultiSelect, Tree → AdvancedSelect
EOF

# DateTime Fields
cat > /tmp/datetime-selection.txt << 'EOF'

## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| Timestamps/Audit trails | DateTimeNow | Auto-populated |
| Event scheduling | DateTimePicker | Full date+time |
| Dates only (no time) | DatePicker | Cleaner for date-only |
| Month/Year selection | MonthPicker | Period selection |

### Decision Criteria
- **Auto-population**: Required → DateTimeNow, Manual → Pickers
- **Time component**: Needed → DateTimePicker, Not needed → DatePicker
- **Granularity**: Day → DatePicker, Month → MonthPicker, Minute → DateTimePicker
- **User editing**: Never → DateTimeNow, Sometimes → Pickers
EOF

# Number Fields
cat > /tmp/number-selection.txt << 'EOF'

## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| General numeric input | NumberField | Full validation support |
| Sequential IDs | BasicAutoIncrementer | Auto-increment |
| Controlled input | TextField with type="number" | When NumberField insufficient |

### Decision Criteria
- **Auto-generation**: Needed → BasicAutoIncrementer
- **Validation complexity**: Simple → NumberField, Complex → TextField variant
- **Step increments**: Not in Designer → Use BasicAutoIncrementer
- **Display format**: Standard → NumberField, Custom → BasicAutoIncrementer
EOF

# Location Fields
cat > /tmp/location-selection.txt << 'EOF'

## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| GPS points | TakePoint | Simple coordinate capture |
| Areas/Polygons | MapFormField | Draw on map |
| Routes/Lines | MapFormField | Draw polylines |
| Site locations | TakePoint | Quick GPS capture |

### Decision Criteria
- **Geometry type**: Point → TakePoint, Polygon/Line → MapFormField
- **User interaction**: GPS button → TakePoint, Draw on map → MapFormField
- **Accuracy needs**: High → TakePoint with threshold, Visual → MapFormField
- **Offline capability**: Full → TakePoint, Limited → MapFormField
EOF

# Media Fields
cat > /tmp/media-selection.txt << 'EOF'

## When to Use These Fields {essential}

### Field Selection Matrix

| Use Case | Recommended Field | Why |
|----------|------------------|-----|
| Photo documentation | TakePhoto | Camera optimized |
| Document uploads | FileUploader | Any file type |
| Mixed media | FileUploader | More flexible |
| Evidence photos | TakePhoto | Direct camera access |

### Decision Criteria
- **File type**: Photos only → TakePhoto, Any type → FileUploader
- **Camera access**: Required → TakePhoto, Optional → FileUploader
- **File source**: Camera → TakePhoto, Existing files → FileUploader
- **Validation**: Neither properly validates required fields (known issue)
EOF

# Now add these to the documents
for doc in text select datetime number location media; do
    if [ "$doc" = "text" ]; then
        file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/text-fields-v05.md"
        table="/tmp/text-selection.txt"
    elif [ "$doc" = "select" ]; then
        file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/select-choice-fields-v05.md"
        table="/tmp/selection-selection.txt"
    elif [ "$doc" = "datetime" ]; then
        file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/datetime-fields-v05.md"
        table="/tmp/datetime-selection.txt"
    elif [ "$doc" = "number" ]; then
        file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/number-fields-v05.md"
        table="/tmp/number-selection.txt"
    elif [ "$doc" = "location" ]; then
        file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/location-fields-v05.md"
        table="/tmp/location-selection.txt"
    elif [ "$doc" = "media" ]; then
        file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/media-fields-v05.md"
        table="/tmp/media-selection.txt"
    fi
    
    if ! grep -q "## When to Use These Fields" "$file"; then
        echo "Adding selection guidance to $doc fields..."
        # Find "## Common Characteristics" and insert before it
        if grep -q "## Common Characteristics" "$file"; then
            awk '/^## Common Characteristics/ {while ((getline line < "'$table'") > 0) {print line}; close("'$table'"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
        else
            # If no Common Characteristics section, add at end before Related Documentation
            awk '/^## Related Documentation/ {while ((getline line < "'$table'") > 0) {print line}; close("'$table'"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
        fi
    fi
done

# Display and Relationship fields need special handling
# Display Field (only one field)
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/display-field-v05.md"
if ! grep -q "## When to Use This Field" "$file"; then
    echo "Adding selection guidance to display field..."
    cat > /tmp/display-selection.txt << 'EOF'

## When to Use This Field {essential}

### Use RichText When
- Displaying instructions or help text within forms
- Adding section headings or visual separators  
- Showing formatted content that doesn't need user input
- Providing context or examples for other fields

### Do NOT Use RichText When
- You need to capture user input (use TextField/MultipleTextField)
- Content changes based on user input (use TemplatedStringField)
- Displaying large documents (performance issues)
- Accessibility is critical (no screen reader support)
EOF
    awk '/^## Common Characteristics/ {while ((getline line < "/tmp/display-selection.txt") > 0) {print line}; close("/tmp/display-selection.txt"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
fi

# Relationship Field
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/relationship-field-v05.md"
if ! grep -q "## When to Use This Field" "$file"; then
    echo "Adding selection guidance to relationship field..."
    cat > /tmp/relationship-selection.txt << 'EOF'

## When to Use This Field {essential}

### Use RelationshipField When
- Linking parent records to child records (hierarchical data)
- Creating associations between peer records (many-to-many)
- Building specimen/sample hierarchies
- Connecting related observations

### Do NOT Use RelationshipField When
- You have >50 relationships per record (performance degrades)
- Relationships might exceed 200 (becomes unusable)
- You need one-way relationships (always bidirectional)
- Simple foreign key reference sufficient (use Select instead)

### Relationship Type Selection
- **Child**: Hierarchical parent-child with cascade operations
- **is-related-to**: Peer relationships with semantic vocabulary
EOF
    awk '/^## Common Characteristics/ {while ((getline line < "/tmp/relationship-selection.txt") > 0) {print line}; close("/tmp/relationship-selection.txt"); print ""} {print}' "$file" > /tmp/temp.md && mv /tmp/temp.md "$file"
fi

# Cleanup
rm -f /tmp/*-selection.txt

echo "Field selection guidance added successfully!"