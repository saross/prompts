#!/bin/bash

echo "Fixing field status mischaracterizations in documentation..."

# Fix RadioGroup status in select-choice-fields
echo "Fixing RadioGroup status..."
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/select-choice-fields-v05.md"

# Remove deprecated status from RadioGroup
sed -i 's/RadioGroup for visible single selection (deprecated)/RadioGroup for visible single selection/g' "$file"
sed -i 's/RadioGroup.*🟡 DEPRECATED/RadioGroup/g' "$file"
sed -i 's/Radio buttons (deprecated)/Radio buttons/g' "$file"
sed -i 's/RadioGroup deprecation: Still available in Designer but deprecated - use Select instead/RadioGroup: Visible radio button selection for when all options should be displayed/g' "$file"
sed -i 's/| RadioGroup | 🟡 Deprecated/| RadioGroup | ✅ Production/g' "$file"
sed -i 's/4\. \*\*RadioGroup\*\* 🟡 DEPRECATED/4. **RadioGroup** ✅ PRODUCTION/g' "$file"
sed -i 's/"Select one option" in Designer.*🟡 DEPRECATED/"Select one option" in Designer → `faims-custom::RadioGroup`/g' "$file"
sed -i 's/⚠️ \*\*DEPRECATED COMPONENT\*\*/### RadioGroup Details/g' "$file"
sed -i 's/\*\*Status\*\*: Deprecated due to no error message display and critical accessibility violations/**Status**: Production - Known issues with error display and accessibility are on roadmap/g' "$file"

# Fix field selection guidance for RadioGroup
sed -i 's/~~Visible options~~ | ~~RadioGroup~~ | Deprecated - use Select/Visible options (2-5) | RadioGroup | All options visible/g' "$file"
sed -i 's/RadioGroup deprecated)/RadioGroup for visible options)/g' "$file"

# Fix DateTimeNow status in datetime-fields
echo "Fixing DateTimeNow status..."
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/datetime-fields-v05.md"

# Change DateTimeNow from discouraged to recommended
sed -i 's/\*\*This field is DISCOURAGED but not deprecated\*\*/**This field is RECOMMENDED for proper timezone handling**/g' "$file"
sed -i 's/DateTimeNow.*Auto-populated timestamp/DateTimeNow | Timestamp with timezone support/g' "$file"

# Add note about timezone benefits
if ! grep -q "DateTimeNow properly handles timezones" "$file"; then
    sed -i '/## When to Use These Fields/a\
### Timezone Handling {important}\
- **DateTimeNow**: RECOMMENDED - Properly handles timezones\
- **DateTimePicker**: Stores local time without timezone (use DateTimeNow when timezone matters)\
- The "now" button in DateTimeNow is optional - field works fine for manual entry too\
' "$file"
fi

# Fix AdvancedSelect status
echo "Fixing AdvancedSelect status..."
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/select-choice-fields-v05.md"

sed -i 's/AdvancedSelect stability: Beta feature with JSON builder but incomplete Designer support/AdvancedSelect: New feature with JSON configuration via Designer input field (template provided)/g' "$file"
sed -i 's/| AdvancedSelect | 🔴 Beta | ❌ None | ❌ Mobile broken | Hierarchical vocabularies/| AdvancedSelect | 🔟 New | ❌ Limited | ⚠️ In progress | Hierarchical vocabularies/g' "$file"
sed -i 's/AdvancedSelect.*🔴 BETA.*Hierarchical trees/AdvancedSelect 🔟 NEW - Hierarchical trees/g' "$file"

# Fix RichText memory leak claims
echo "Fixing RichText descriptions..."
file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/display-field-v05.md"

sed -i 's/Memory leaks: Known performance issues on mobile devices/Performance: No known issues in production use/g' "$file"
sed -i 's/\*\*⚠️ MEMORY WARNING\*\*: Critical limitations include memory leaks on mobile devices/**Note**: Tables and external images not yet supported/g' "$file"

file="/home/shawn/Code/prompts/EFN/Docs-staging/field-categories/text-fields-v05.md"
sed -i 's/\*\*⚠️ MEMORY WARNING\*\*: Critical limitations include memory leaks on mobile devices/**Note**: Tables and external images not yet supported/g' "$file"

# Fix Number Field status (keep as deprecated - this one is correct)
echo "Number Field remains correctly marked as deprecated"

# Clean up any stray deprecated references to RadioGroup
for file in /home/shawn/Code/prompts/EFN/Docs-staging/field-categories/*.md; do
    sed -i 's/RadioGroup (deprecated)/RadioGroup/g' "$file"
    sed -i 's/Deprecated.*RadioGroup/RadioGroup/g' "$file"
done

echo "Field status corrections complete!"