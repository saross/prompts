#!/bin/bash

# Build concatenated reference documentation from individual files
# Output: reference.md - Single comprehensive document for LLM consumption

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Base directory
BASE_DIR="/home/shawn/Code/prompts/EFN/Docs-staging"
OUTPUT_FILE="$BASE_DIR/reference.md"

echo -e "${GREEN}Building Fieldmark v3 Reference Documentation${NC}"
echo "================================================"

# Start with the index
echo -e "${YELLOW}Adding master index...${NC}"
cat "$BASE_DIR/field-type-index.md" > "$OUTPUT_FILE"

# Add separator
echo -e "\n\n<!-- ============================================ -->" >> "$OUTPUT_FILE"
echo "<!-- FIELD TYPE DOCUMENTATION -->" >> "$OUTPUT_FILE"
echo "<!-- ============================================ -->" >> "$OUTPUT_FILE"

# Add field category documents in order
echo -e "${YELLOW}Adding field documentation...${NC}"
FIELD_DOCS=(
    "text-fields-v05"
    "select-choice-fields-v05"
    "datetime-fields-v05"
    "number-fields-v05"
    "display-field-v05"
    "location-fields-v05"
    "media-fields-v05"
    "relationship-field-v05"
)

for doc in "${FIELD_DOCS[@]}"; do
    if [ -f "$BASE_DIR/field-categories/${doc}.md" ]; then
        echo "  - Adding ${doc}.md"
        echo -e "\n\n<!-- concat:document:${doc} -->" >> "$OUTPUT_FILE"
        cat "$BASE_DIR/field-categories/${doc}.md" >> "$OUTPUT_FILE"
    else
        echo "  ⚠ Warning: ${doc}.md not found"
    fi
done

# Add separator
echo -e "\n\n<!-- ============================================ -->" >> "$OUTPUT_FILE"
echo "<!-- CROSS-FIELD PATTERNS -->" >> "$OUTPUT_FILE"
echo "<!-- ============================================ -->" >> "$OUTPUT_FILE"

# Add cross-field pattern documents if they exist
echo -e "${YELLOW}Adding cross-field patterns...${NC}"
PATTERN_DOCS=(
    "field-selection-best-practices"
    "quick-start"
    "summary-table"
    "validation"
    "conditional-logic"
    "navigation"
    "notebook-structure"
    "patterns"
)

for doc in "${PATTERN_DOCS[@]}"; do
    if [ -f "$BASE_DIR/detail-crossfield-docs/${doc}.md" ]; then
        echo "  - Adding ${doc}.md"
        echo -e "\n\n<!-- concat:pattern:${doc} -->" >> "$OUTPUT_FILE"
        cat "$BASE_DIR/detail-crossfield-docs/${doc}.md" >> "$OUTPUT_FILE"
    else
        echo "  ⚠ Warning: ${doc}.md not found in detail-crossfield-docs"
    fi
done

# Add separator
echo -e "\n\n<!-- ============================================ -->" >> "$OUTPUT_FILE"
echo "<!-- TECHNICAL REFERENCES -->" >> "$OUTPUT_FILE"
echo "<!-- ============================================ -->" >> "$OUTPUT_FILE"

# Add technical reference documents
echo -e "${YELLOW}Adding technical references...${NC}"
REFERENCE_DOCS=(
    "component-namespace-reference"
    "meta-properties-reference"
    "formik-integration-reference"
    "platform-behaviors-reference"
    "performance-thresholds-reference"
    "accessibility-reference"
    "migration-strategies-reference"
    "troubleshooting-framework-reference"
    "data-export-reference"
    "designer-limitations-reference"
    "security-considerations-reference"
    "validation-timing-reference"
)

for doc in "${REFERENCE_DOCS[@]}"; do
    if [ -f "$BASE_DIR/reference-docs/${doc}.md" ]; then
        echo "  - Adding ${doc}.md"
        echo -e "\n\n<!-- concat:reference:${doc} -->" >> "$OUTPUT_FILE"
        cat "$BASE_DIR/reference-docs/${doc}.md" >> "$OUTPUT_FILE"
    else
        echo "  ⚠ Warning: ${doc}.md not found in reference-docs"
    fi
done

# Add footer with metadata
echo -e "\n\n<!-- ============================================ -->" >> "$OUTPUT_FILE"
echo "<!-- DOCUMENT METADATA -->" >> "$OUTPUT_FILE"
echo "<!-- ============================================ -->" >> "$OUTPUT_FILE"
echo -e "\n## Document Metadata\n" >> "$OUTPUT_FILE"
echo "- **Generated**: $(date -Iseconds)" >> "$OUTPUT_FILE"
echo "- **Total Lines**: $(wc -l < "$OUTPUT_FILE")" >> "$OUTPUT_FILE"
echo "- **Field Documents**: ${#FIELD_DOCS[@]}" >> "$OUTPUT_FILE"
echo "- **Pattern Documents**: $(ls -1 $BASE_DIR/detail-crossfield-docs/*.md 2>/dev/null | wc -l)" >> "$OUTPUT_FILE"
echo "- **Reference Documents**: $(ls -1 $BASE_DIR/reference-docs/*.md 2>/dev/null | wc -l)" >> "$OUTPUT_FILE"
echo "- **Format**: LLM-optimized concatenated reference" >> "$OUTPUT_FILE"

# Generate anchor index
echo -e "\n## Quick Jump Index\n" >> "$OUTPUT_FILE"
echo "### Field Types" >> "$OUTPUT_FILE"
echo "- [Text & Input Fields](#text-input-fields)" >> "$OUTPUT_FILE"
echo "- [Selection & Choice Fields](#selection-fields)" >> "$OUTPUT_FILE"
echo "- [Date & Time Fields](#datetime-fields)" >> "$OUTPUT_FILE"
echo "- [Numeric Fields](#number-fields)" >> "$OUTPUT_FILE"
echo "- [Display Fields](#display-fields)" >> "$OUTPUT_FILE"
echo "- [Location Fields](#location-fields)" >> "$OUTPUT_FILE"
echo "- [Media Fields](#media-fields)" >> "$OUTPUT_FILE"
echo "- [Relationship Fields](#relationship-fields)" >> "$OUTPUT_FILE"

echo -e "\n### Patterns" >> "$OUTPUT_FILE"
echo "- [Field Selection](#field-selection-best-practices)" >> "$OUTPUT_FILE"
echo "- [Validation](#validation)" >> "$OUTPUT_FILE"
echo "- [Conditional Logic](#conditional-logic)" >> "$OUTPUT_FILE"
echo "- [Navigation](#navigation)" >> "$OUTPUT_FILE"
echo "- [Notebook Structure](#notebook-structure)" >> "$OUTPUT_FILE"
echo "- [Common Patterns](#patterns)" >> "$OUTPUT_FILE"

echo -e "\n### References" >> "$OUTPUT_FILE"
echo "- [Component Namespace](#component-namespace-reference)" >> "$OUTPUT_FILE"
echo "- [Platform Behaviors](#platform-behaviors-reference)" >> "$OUTPUT_FILE"
echo "- [Performance Thresholds](#performance-thresholds-reference)" >> "$OUTPUT_FILE"
echo "- [Designer Limitations](#designer-limitations-reference)" >> "$OUTPUT_FILE"
echo "- [Security Considerations](#security-considerations-reference)" >> "$OUTPUT_FILE"

# Final statistics
echo ""
echo -e "${GREEN}✓ Documentation concatenated successfully!${NC}"
echo "================================================"
echo "Output file: $OUTPUT_FILE"
echo "Total size: $(wc -l < "$OUTPUT_FILE") lines"
echo "File size: $(du -h "$OUTPUT_FILE" | cut -f1)"
echo ""
echo "The reference.md file is ready for LLM consumption."
echo ""
echo "To extract subsets by depth tag:"
echo "  - Essential only: grep -E '^#.*{essential}|^[^#]' reference.md"
echo "  - Essential + Important: grep -E '^#.*{essential}|^#.*{important}|^[^#]' reference.md"
echo "  - All content: cat reference.md"