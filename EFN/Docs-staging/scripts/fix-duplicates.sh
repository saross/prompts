#!/bin/bash

echo "Fixing duplicate content in field documentation..."

# Fix location-fields
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/location-fields-v05.md"
echo "Fixing location-fields..."
sed -i '37,45d' "$file"  # Remove duplicate content

# Fix display-field
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/display-field-v05.md"
echo "Fixing display-field..."
sed -i '37,46d' "$file"  # Remove duplicate content

# Fix media-fields
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/media-fields-v05.md"
echo "Fixing media-fields..."
sed -i '38,46d' "$file"  # Remove duplicate content

# Fix relationship-field
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/relationship-field-v05.md"
echo "Fixing relationship-field..."
sed -i '37,46d' "$file"  # Remove duplicate content

echo "Duplicate content removed!"