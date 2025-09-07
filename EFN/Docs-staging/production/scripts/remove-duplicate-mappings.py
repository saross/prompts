#!/usr/bin/env python3
"""
Remove Component Name Mapping sections from field-categories docs
and replace with cross-reference to designer-component-mapping.md
"""

import os
import re

# Cross-reference text to insert
CROSS_REFERENCE = """## Component Mapping Reference {essential}

For the complete mapping between Designer field names and JSON component implementations, see:
→ **[Designer UI to Component Mapping Reference](../references/designer-component-mapping.md)**

This central reference provides:
- Exact component names and namespaces for all fields
- Configuration requirements and examples
- Common mapping errors and solutions
"""

def process_field_doc(filepath):
    """Remove mapping section and add cross-reference"""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find and remove the Component Name Mapping section
    # Pattern matches from ## Component Name Mapping to the next ## section
    pattern = r'## Component Name Mapping.*?(?=\n##[^#]|\Z)'
    
    if re.search(pattern, content, re.DOTALL):
        # Replace with cross-reference
        new_content = re.sub(pattern, CROSS_REFERENCE + '\n', content, flags=re.DOTALL)
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        
        return True
    return False

# Process all field category documents
field_dir = 'field-categories'
processed = []
skipped = []

for filename in os.listdir(field_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(field_dir, filename)
        if process_field_doc(filepath):
            processed.append(filename)
            print(f"✅ Processed: {filename}")
        else:
            skipped.append(filename)
            print(f"⏭️  Skipped: {filename} (no mapping section found)")

print(f"\nSummary:")
print(f"  Processed: {len(processed)} files")
print(f"  Skipped: {len(skipped)} files")
print(f"\nAll field docs now reference the central mapping document.")