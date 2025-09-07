#!/bin/bash

# Build concatenated reference documentation from individual files
# Output: reference.md - Single comprehensive document for LLM consumption

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Base directory - relative to script location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
OUTPUT_FILE="$BASE_DIR/reference.md"

echo -e "${GREEN}Building Fieldmark v3 Reference Documentation${NC}"
echo "================================================"

# Start with the index from references directory
echo -e "${YELLOW}Adding master index...${NC}"
cat "$BASE_DIR/references/field-type-index.md" > "$OUTPUT_FILE"

# Add LLM navigation manifest for content discovery
echo -e "${YELLOW}Adding LLM navigation manifest...${NC}"
if [ -f "$BASE_DIR/references/llm-navigation-manifest.md" ]; then
    echo "  - Adding llm-navigation-manifest.md"
    echo -e "\n\n<!-- concat:reference:llm-navigation-manifest -->" >> "$OUTPUT_FILE"
    cat "$BASE_DIR/references/llm-navigation-manifest.md" >> "$OUTPUT_FILE"
else
    echo "  ⚠ Warning: llm-navigation-manifest.md not found"
fi

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

# Add cross-field pattern documents from patterns directory
echo -e "${YELLOW}Adding cross-field patterns...${NC}"
PATTERN_DOCS=(
    "field-selection-guide"
    "form-structure-guide"
    "dynamic-forms-guide"
    "implementation-patterns-guide"
)

for doc in "${PATTERN_DOCS[@]}"; do
    if [ -f "$BASE_DIR/patterns/${doc}.md" ]; then
        echo "  - Adding ${doc}.md"
        echo -e "\n\n<!-- concat:pattern:${doc} -->" >> "$OUTPUT_FILE"
        cat "$BASE_DIR/patterns/${doc}.md" >> "$OUTPUT_FILE"
    else
        echo "  ⚠ Warning: ${doc}.md not found in patterns"
    fi
done

# Add separator
echo -e "\n\n<!-- ============================================ -->" >> "$OUTPUT_FILE"
echo "<!-- TECHNICAL REFERENCES -->" >> "$OUTPUT_FILE"
echo "<!-- ============================================ -->" >> "$OUTPUT_FILE"

# Add consolidated technical reference documents
echo -e "${YELLOW}Adding consolidated technical references...${NC}"

# Add all references from the 'references' directory
# Note: field-type-index is added separately at the beginning
REFERENCE_DOCS=(
    "glossary"                    # Key terms and concepts
    "designer-component-mapping"  # Primary field mapping reference
    "component-reference"          # Namespaces and types
    "constraints-reference"        # Limitations and security
    "operations-reference"         # Migration and troubleshooting
    "platform-reference"          # Platform-specific behaviors
    "notebook-format-guide"       # JSON structure guide
    "notebook-templates"          # Complete working examples
    "troubleshooting-index"       # Error solutions and diagnostics
    "file-organization-guide"     # Project structure
    "navigation-index"            # Bidirectional link registry
)

for doc in "${REFERENCE_DOCS[@]}"; do
    if [ -f "$BASE_DIR/references/${doc}.md" ]; then
        echo "  - Adding ${doc}.md"
        echo -e "\n\n<!-- concat:reference:${doc} -->" >> "$OUTPUT_FILE"
        cat "$BASE_DIR/references/${doc}.md" >> "$OUTPUT_FILE"
    else
        echo "  ⚠ Warning: ${doc}.md not found in references"
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
echo "- **Pattern Documents**: $(ls -1 $BASE_DIR/patterns/*.md 2>/dev/null | wc -l)" >> "$OUTPUT_FILE"
echo "- **Reference Documents**: $(ls -1 $BASE_DIR/references/*.md 2>/dev/null | wc -l)" >> "$OUTPUT_FILE"
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
echo "- [Field Selection Guide](#field-selection-guide)" >> "$OUTPUT_FILE"
echo "- [Form Structure Guide](#form-structure-guide)" >> "$OUTPUT_FILE"
echo "- [Dynamic Forms Guide](#dynamic-forms-guide)" >> "$OUTPUT_FILE"
echo "- [Implementation Patterns](#implementation-patterns-guide)" >> "$OUTPUT_FILE"

echo -e "\n### References" >> "$OUTPUT_FILE"
echo "- [Component Reference](#component-reference)" >> "$OUTPUT_FILE"
echo "- [Platform Reference](#platform-reference)" >> "$OUTPUT_FILE"
echo "- [Operations Reference](#operations-reference)" >> "$OUTPUT_FILE"
echo "- [Constraints Reference](#constraints-reference)" >> "$OUTPUT_FILE"

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