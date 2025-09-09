#!/usr/bin/env python3
"""
Fix incorrect component names in JSON examples.
The documentation text is correct - it describes Designer fields.
The JSON examples incorrectly use component names that don't exist.
"""

import re
from pathlib import Path

def fix_component_names(content):
    """Fix incorrect component names in JSON examples"""
    
    # Track what we're changing for reporting
    changes = []
    
    # Fix TemplatedIntegerField -> NumberField
    if 'TemplatedIntegerField' in content:
        count = content.count('TemplatedIntegerField')
        content = content.replace(
            '"component-name": "TemplatedIntegerField"',
            '"component-name": "NumberField"'
        )
        changes.append(f"  - Fixed {count} TemplatedIntegerField -> NumberField")
    
    # Fix TemplatedFloatField -> NumberField
    if 'TemplatedFloatField' in content:
        count = content.count('TemplatedFloatField')
        content = content.replace(
            '"component-name": "TemplatedFloatField"',
            '"component-name": "NumberField"'
        )
        changes.append(f"  - Fixed {count} TemplatedFloatField -> NumberField")
    
    # Fix ControlledNumber -> TextField (with namespace fix)
    # This is tricky because ControlledNumber uses TextField from formik-material-ui
    if '"component-name": "ControlledNumber"' in content:
        # Count occurrences
        pattern = r'(\s*"component-namespace":\s*"[^"]+",\s*\n\s*"component-name":\s*"ControlledNumber")'
        matches = re.findall(pattern, content)
        
        # Replace with correct namespace and component
        content = re.sub(
            r'"component-namespace":\s*"[^"]+",(\s*\n\s*)"component-name":\s*"ControlledNumber"',
            r'"component-namespace": "formik-material-ui",\1"component-name": "TextField"',
            content
        )
        changes.append(f"  - Fixed {len(matches)} ControlledNumber -> TextField (formik-material-ui)")
    
    # Fix TimePicker -> DateTimePicker (best alternative)
    if 'TimePicker' in content:
        count = content.count('"component-name": "TimePicker"')
        content = content.replace(
            '"component-name": "TimePicker"',
            '"component-name": "DateTimePicker"'
        )
        changes.append(f"  - Fixed {count} TimePicker -> DateTimePicker (no standalone time picker)")
    
    # Fix Email component -> TextField
    if '"component-name": "Email"' in content:
        count = content.count('"component-name": "Email"')
        content = content.replace(
            '"component-name": "Email"',
            '"component-name": "TextField"'
        )
        changes.append(f"  - Fixed {count} Email -> TextField")
    
    # Fix MultilineText -> MultipleTextField
    if '"component-name": "MultilineText"' in content:
        count = content.count('"component-name": "MultilineText"')
        content = content.replace(
            '"component-name": "MultilineText"',
            '"component-name": "MultipleTextField"'
        )
        changes.append(f"  - Fixed {count} MultilineText -> MultipleTextField")
    
    # Fix NumberInput -> NumberField
    if '"component-name": "NumberInput"' in content:
        count = content.count('"component-name": "NumberInput"')
        content = content.replace(
            '"component-name": "NumberInput"',
            '"component-name": "NumberField"'
        )
        changes.append(f"  - Fixed {count} NumberInput -> NumberField")
    
    # Fix namespace for NumberField if needed
    # NumberField should be faims-custom, not formik-material-ui
    pattern = r'"component-namespace":\s*"formik-material-ui",(\s*\n\s*)"component-name":\s*"NumberField"'
    if re.search(pattern, content):
        content = re.sub(
            pattern,
            r'"component-namespace": "faims-custom",\1"component-name": "NumberField"',
            content
        )
        changes.append(f"  - Fixed NumberField namespace to faims-custom")
    
    return content, changes

def process_file(filepath):
    """Process a single markdown file"""
    content = filepath.read_text()
    original = content
    
    content, changes = fix_component_names(content)
    
    if content != original:
        filepath.write_text(content)
        print(f"\n✅ Fixed {filepath.name}:")
        for change in changes:
            print(change)
        return True
    return False

def main():
    """Fix component names in production documentation"""
    
    print("Fixing incorrect component names in JSON examples...")
    print("=" * 60)
    
    production_dir = Path('field-categories')
    fixed_count = 0
    
    # Files that likely need fixes based on our analysis
    priority_files = [
        'number-fields-v05.md',
        'datetime-fields-v05.md', 
        'text-fields-v05.md'
    ]
    
    # Process priority files first
    for filename in priority_files:
        filepath = production_dir / filename
        if filepath.exists():
            if process_file(filepath):
                fixed_count += 1
    
    # Then process any other files
    for filepath in production_dir.glob('*.md'):
        if filepath.name not in priority_files:
            if process_file(filepath):
                fixed_count += 1
    
    print("\n" + "=" * 60)
    print(f"Summary: Fixed {fixed_count} files")
    
    # Now check archive directory if it exists
    archive_dir = Path('../archive')
    if archive_dir.exists():
        print("\n" + "=" * 60)
        print("Checking archive directory...")
        archive_fixed = 0
        
        for subdir in archive_dir.iterdir():
            if subdir.is_dir():
                for filepath in subdir.glob('*.md'):
                    original = filepath.read_text()
                    content, changes = fix_component_names(original)
                    if content != original:
                        filepath.write_text(content)
                        print(f"\n✅ Fixed archive/{subdir.name}/{filepath.name}:")
                        for change in changes:
                            print(change)
                        archive_fixed += 1
        
        if archive_fixed > 0:
            print(f"\nFixed {archive_fixed} archive files")
    
    print("\n" + "=" * 60)
    print("Fix complete!")
    print("\nNote: The documentation TEXT is correct (describes Designer fields).")
    print("Only the JSON component names were wrong.")

if __name__ == '__main__':
    main()