#!/bin/bash

# Script to add concatenation-friendly headers and footers to field documentation

echo "Adding navigation headers and footers to field documentation..."

# Function to add header and footer to a document
add_navigation() {
    local file=$1
    local doc_id=$2
    local category=$3
    local field_count=$4
    local section_id=$5
    local prev_doc=$6
    local prev_title=$7
    local prev_section=$8
    local next_doc=$9
    local next_title=${10}
    local next_section=${11}
    
    echo "Processing $file..."
    
    # Create temporary file with new content
    cat > /tmp/nav_header.tmp << EOF
<!-- concat:boundary:start section="$section_id" -->
<!-- concat:metadata
document_id: $doc_id
category: $category
field_count: $field_count
last_updated: 2025-01-05
-->

EOF

    # Add navigation header
    cat >> /tmp/nav_header.tmp << EOF
## Document Navigation
<!-- concat:nav-mode:individual -->
EOF

    # Add individual navigation
    if [ -n "$prev_doc" ]; then
        echo -n "[← $prev_title]($prev_doc) | " >> /tmp/nav_header.tmp
    fi
    echo -n "**$next_title**" >> /tmp/nav_header.tmp
    if [ -n "$next_doc" ]; then
        echo " | [$next_title →]($next_doc)" >> /tmp/nav_header.tmp
    else
        echo "" >> /tmp/nav_header.tmp
    fi
    
    # Add concatenated navigation
    cat >> /tmp/nav_header.tmp << EOF
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index)EOF

    if [ -n "$prev_section" ]; then
        echo -n " | [↑ $prev_title](#$prev_section)" >> /tmp/nav_header.tmp
    fi
    if [ -n "$next_section" ]; then
        echo " | [↓ $next_title](#$next_section) -->" >> /tmp/nav_header.tmp
    else
        echo " -->" >> /tmp/nav_header.tmp
    fi
    
    echo "" >> /tmp/nav_header.tmp
    
    # Create footer
    cat > /tmp/nav_footer.tmp << EOF

---

## Related Documentation
<!-- concat:references -->

### Within Field Categories
EOF

    # Add category navigation
    if [ -n "$prev_doc" ]; then
        echo "- **Previous**: [$prev_title]($prev_doc) | [#$prev_section](#$prev_section)" >> /tmp/nav_footer.tmp
    fi
    if [ -n "$next_doc" ]; then
        echo "- **Next**: [$next_title]($next_doc) | [#$next_section](#$next_section)" >> /tmp/nav_footer.tmp
    fi
    
    # Add standard references
    cat >> /tmp/nav_footer.tmp << EOF

### Cross-Field Patterns
- **Validation**: [Validation Patterns](../detail-crossfield-docs/validation.md#$section_id) | [#validation-patterns](#validation-patterns)
- **Conditional Logic**: [Conditional Logic](../detail-crossfield-docs/conditional-logic.md#$section_id) | [#conditional-logic](#conditional-logic)
- **Best Practices**: [Field Selection](../detail-crossfield-docs/field-selection-best-practices.md#$section_id) | [#field-selection](#field-selection)

### Technical References
- **Designer Limitations**: [Constraints](../reference-docs/designer-limitations-reference.md#$section_id) | [#designer-limitations](#designer-limitations)
- **Performance**: [Thresholds](../reference-docs/performance-thresholds-reference.md#$section_id) | [#performance-thresholds](#performance-thresholds)
- **Security**: [Considerations](../reference-docs/security-considerations-reference.md#$section_id) | [#security-considerations](#security-considerations)

<!-- /concat:references -->
<!-- concat:boundary:end section="$section_id" -->
EOF
    
    # Now modify the actual file
    # Skip if already has concat boundaries
    if grep -q "concat:boundary:start" "$file" 2>/dev/null; then
        echo "  Already has navigation, skipping..."
        return
    fi
    
    # Add header after the title
    awk '
    /^# / && !header_added {
        print $0
        while ((getline line < "/tmp/nav_header.tmp") > 0) {
            print line
        }
        close("/tmp/nav_header.tmp")
        header_added = 1
        next
    }
    {print}
    ' "$file" > /tmp/modified.tmp
    
    # Add footer at the end
    cat /tmp/nav_footer.tmp >> /tmp/modified.tmp
    
    # Replace original file
    mv /tmp/modified.tmp "$file"
    echo "  Done!"
}

# Process all field documents
cd /home/shawn/Code/prompts/EFN/Docs-staging/field-categories

# Note: text-fields already done, skipping it

add_navigation \
    "./select-choice-fields-v05.md" \
    "select-choice-fields-v05" \
    "selection_choice" \
    "5" \
    "selection-fields" \
    "./text-fields-v05.md" \
    "Text Fields" \
    "text-input-fields" \
    "./datetime-fields-v05.md" \
    "Date & Time Fields" \
    "datetime-fields"

add_navigation \
    "./datetime-fields-v05.md" \
    "datetime-fields-v05" \
    "datetime" \
    "4" \
    "datetime-fields" \
    "./select-choice-fields-v05.md" \
    "Selection Fields" \
    "selection-fields" \
    "./number-fields-v05.md" \
    "Numeric Fields" \
    "number-fields"

add_navigation \
    "./number-fields-v05.md" \
    "number-fields-v05" \
    "numeric" \
    "3" \
    "number-fields" \
    "./datetime-fields-v05.md" \
    "Date & Time Fields" \
    "datetime-fields" \
    "./display-field-v05.md" \
    "Display Fields" \
    "display-fields"

add_navigation \
    "./display-field-v05.md" \
    "display-field-v05" \
    "display" \
    "1" \
    "display-fields" \
    "./number-fields-v05.md" \
    "Numeric Fields" \
    "number-fields" \
    "./location-fields-v05.md" \
    "Location Fields" \
    "location-fields"

add_navigation \
    "./location-fields-v05.md" \
    "location-fields-v05" \
    "location" \
    "2" \
    "location-fields" \
    "./display-field-v05.md" \
    "Display Fields" \
    "display-fields" \
    "./media-fields-v05.md" \
    "Media Fields" \
    "media-fields"

add_navigation \
    "./media-fields-v05.md" \
    "media-fields-v05" \
    "media" \
    "2" \
    "media-fields" \
    "./location-fields-v05.md" \
    "Location Fields" \
    "location-fields" \
    "./relationship-field-v05.md" \
    "Relationship Fields" \
    "relationship-fields"

add_navigation \
    "./relationship-field-v05.md" \
    "relationship-field-v05" \
    "relationship" \
    "1" \
    "relationship-fields" \
    "./media-fields-v05.md" \
    "Media Fields" \
    "media-fields" \
    "" \
    "" \
    ""

echo "Navigation headers and footers added successfully!"

# Clean up temp files
rm -f /tmp/nav_header.tmp /tmp/nav_footer.tmp /tmp/modified.tmp

echo "Done!"