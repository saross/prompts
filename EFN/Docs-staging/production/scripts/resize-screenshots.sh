#!/bin/bash
# resize-screenshots.sh
# Resize screenshots to max dimension of 2000 pixels while preserving aspect ratio
# Usage: ./resize-screenshots.sh [directory]

# Default to quickstart/raw if no directory specified
DIR="${1:-/home/shawn/Code/prompts/EFN/Docs-staging/production/screenshots/quickstart/raw}"
MAX_DIM=2000

echo "Checking images in: $DIR"
echo "Max dimension: ${MAX_DIM}px"
echo ""

# Counter for resized images
resized=0
total=0

# Process each PNG file
for img in "$DIR"/*.png; do
    if [ ! -f "$img" ]; then
        echo "No PNG files found in $DIR"
        exit 1
    fi

    total=$((total + 1))

    # Get image dimensions
    dimensions=$(identify -format "%wx%h" "$img" 2>/dev/null)
    if [ $? -ne 0 ]; then
        echo "⚠️  Could not read: $(basename "$img")"
        continue
    fi

    width=$(echo $dimensions | cut -d'x' -f1)
    height=$(echo $dimensions | cut -d'x' -f2)

    # Check if either dimension exceeds max
    if [ "$width" -gt "$MAX_DIM" ] || [ "$height" -gt "$MAX_DIM" ]; then
        echo "Resizing: $(basename "$img") (${width}x${height})"

        # Resize image (> flag means only shrink if larger)
        convert "$img" -resize "${MAX_DIM}x${MAX_DIM}>" "$img"

        if [ $? -eq 0 ]; then
            # Get new dimensions
            new_dimensions=$(identify -format "%wx%h" "$img")
            echo "  ✓ Resized to: $new_dimensions"
            resized=$((resized + 1))
        else
            echo "  ✗ Failed to resize"
        fi
    else
        echo "OK: $(basename "$img") (${width}x${height})"
    fi
done

echo ""
echo "Summary:"
echo "  Total images: $total"
echo "  Resized: $resized"
echo "  Unchanged: $((total - resized))"
