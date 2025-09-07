#!/usr/bin/env python3
"""
Add notebook context references to all field documentation files.
"""

import os
from pathlib import Path

# Reference text to add before Related Documentation section
NOTEBOOK_REFERENCE = """
## Fields in Complete Notebooks {important}

For complete working examples showing how these fields integrate into full notebook structures with fviews and viewsets, see:

→ **[Complete Notebook Templates](../references/notebook-templates.md)**

The templates include:
- Minimal survey (3 fields) 
- Basic data collection (10 fields)
- Complex form with validation (20 fields)
- Mobile-optimized with GPS/Photo
- Production archaeological recording

Each template shows the complete JSON structure required for import into Designer, including:
- Proper field → fview → viewset hierarchy
- Required `name` parameters for all fields
- Working validation schemas
- Conditional logic examples

"""

def add_notebook_reference(filepath):
    """Add notebook reference section to a field documentation file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if reference already exists
    if "Fields in Complete Notebooks" in content or "Complete Notebook Templates" in content:
        print(f"  - Reference already exists, skipping")
        return False
    
    # Find where to insert (before Related Documentation or at end)
    if "## Related Documentation" in content:
        # Insert before Related Documentation
        new_content = content.replace(
            "## Related Documentation",
            NOTEBOOK_REFERENCE + "---\n\n## Related Documentation"
        )
    elif "---\n\n## " in content:
        # Find the last major section
        parts = content.rsplit("---\n\n## ", 1)
        if len(parts) == 2:
            new_content = parts[0] + NOTEBOOK_REFERENCE + "---\n\n## " + parts[1]
        else:
            # Just add at the end
            new_content = content + "\n\n---\n\n" + NOTEBOOK_REFERENCE
    else:
        # Add at the end
        new_content = content + "\n\n---\n\n" + NOTEBOOK_REFERENCE
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  - Added notebook reference section")
    return True

def main():
    """Process all field documentation files."""
    base_dir = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production/field-categories")
    
    if not base_dir.exists():
        print(f"Error: Directory {base_dir} not found")
        return
    
    print("Adding notebook references to field documentation...")
    print("-" * 50)
    
    files_updated = 0
    
    for filepath in sorted(base_dir.glob("*-v05.md")):
        print(f"\n{filepath.name}:")
        if add_notebook_reference(filepath):
            files_updated += 1
    
    print("\n" + "=" * 50)
    print(f"Summary: Updated {files_updated} files")

if __name__ == "__main__":
    main()