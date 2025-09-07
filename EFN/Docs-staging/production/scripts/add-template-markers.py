#!/usr/bin/env python3
"""
Add template markers to JSON examples in field documentation.
This enables parametric code generation by LLMs.

Usage:
    python add-template-markers.py
    
This script will:
1. Find all JSON code blocks in field documentation
2. Add template markers ({{VARIABLE_NAME}}) with explanatory comments
3. Preserve original examples while making them generation-ready
"""

import re
from pathlib import Path
import json

def add_markers_to_json(json_str, field_type):
    """Add template markers to a JSON string based on field type."""
    
    # Common replacements for all field types
    replacements = [
        # Field identifiers
        (r'"([a-z0-9-]+)"(\s*:\s*{[^}]*"component-name")', r'"{{FIELD_ID}}"  // REPLACE: unique field identifier\2'),
        
        # Labels and text
        (r'"label":\s*"[^"]*"', r'"label": "{{FIELD_LABEL}}"  // REPLACE: user-visible label'),
        (r'"helperText":\s*"[^"]*"', r'"helperText": "{{HELPER_TEXT}}"  // OPTIONAL: field guidance'),
        
        # Name parameters (must match field ID)
        (r'"name":\s*"[^"]*"', r'"name": "{{FIELD_ID}}"  // REQUIRED: must match field identifier'),
        
        # Section names
        (r'"([a-z0-9-]+)"(\s*:\s*{[^}]*"fields"\s*:\s*\[)', r'"{{SECTION_ID}}"  // REPLACE: section identifier\2'),
        
        # Form names
        (r'"([a-z0-9-]+)"(\s*:\s*{[^}]*"views"\s*:\s*\[)', r'"{{FORM_ID}}"  // REPLACE: form identifier\2'),
        
        # Validation messages
        (r'\["yup\.[^"]+",\s*"([^"]+)"\]', lambda m: f'["yup.{m.group(1)}", "{{VALIDATION_MESSAGE}}"]  // CUSTOMIZE: error message'),
    ]
    
    # Field-specific replacements
    if 'Select' in field_type or 'Dropdown' in field_type:
        replacements.extend([
            (r'"option[0-9]+"', r'"{{OPTION_VALUE}}"  // REPLACE: option value'),
            (r'"Option [0-9]+"', r'"{{OPTION_LABEL}}"  // REPLACE: option display text'),
        ])
    
    if 'Relationship' in field_type:
        replacements.extend([
            (r'"relation_type":\s*"[^"]*"', r'"relation_type": "{{RELATION_TYPE}}"  // REPLACE: relationship type'),
            (r'"relation_name":\s*"[^"]*"', r'"relation_name": "{{RELATION_NAME}}"  // REPLACE: relationship name'),
        ])
    
    if 'TakePhoto' in field_type or 'TakePoint' in field_type:
        replacements.extend([
            (r'"variant_label":\s*"[^"]*"', r'"variant_label": "{{VARIANT_LABEL}}"  // REPLACE: capture button text'),
        ])
    
    # Apply replacements
    result = json_str
    for pattern, replacement in replacements:
        if callable(replacement):
            result = re.sub(pattern, replacement, result)
        else:
            result = re.sub(pattern, replacement, result)
    
    return result

def process_markdown_file(filepath):
    """Process a markdown file to add template markers to JSON examples."""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract field type from filename or content
    field_type = filepath.stem.replace('-v05', '').replace('-', ' ').title()
    
    # Find all JSON code blocks
    json_pattern = r'(```json\n)(.*?)(```)'
    
    def replace_json_block(match):
        prefix = match.group(1)
        json_content = match.group(2)
        suffix = match.group(3)
        
        # Skip if already has template markers
        if '{{' in json_content:
            return match.group(0)
        
        # Skip small snippets (less than 5 lines)
        if json_content.count('\n') < 5:
            return match.group(0)
        
        # Add markers
        marked_content = add_markers_to_json(json_content, field_type)
        
        # Add comment header if substantial changes were made
        if marked_content != json_content:
            header = "// Template markers added for parametric generation\n"
            return prefix + header + marked_content + suffix
        
        return match.group(0)
    
    # Replace all JSON blocks
    new_content = re.sub(json_pattern, replace_json_block, content, flags=re.DOTALL)
    
    # Count changes
    changes = new_content.count('{{') - content.count('{{')
    
    if changes > 0:
        # Save the modified content
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"  ✓ {filepath.name}: Added {changes} template markers")
    else:
        print(f"  - {filepath.name}: No changes needed")
    
    return changes

def main():
    """Add template markers to all field documentation."""
    
    production_dir = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production")
    field_categories_dir = production_dir / "field-categories"
    
    print("=" * 70)
    print("ADDING TEMPLATE MARKERS TO JSON EXAMPLES")
    print("=" * 70)
    print("\nThis enables parametric code generation by LLMs.\n")
    
    # Process all markdown files in field-categories
    field_docs = sorted(field_categories_dir.glob("*-v05.md"))
    
    total_changes = 0
    for doc in field_docs:
        changes = process_markdown_file(doc)
        total_changes += changes
    
    print("\n" + "=" * 70)
    print(f"SUMMARY: Added {total_changes} template markers across {len(field_docs)} files")
    print("=" * 70)
    
    print("\nTemplate markers enable LLMs to:")
    print("1. Generate customized field configurations")
    print("2. Replace placeholders with actual values")
    print("3. Create complete notebooks from patterns")
    print("\nExample usage:")
    print('  Replace {{FIELD_ID}} with "site-name"')
    print('  Replace {{FIELD_LABEL}} with "Site Name"')
    print('  Replace {{VALIDATION_MESSAGE}} with "Site name is required"')

if __name__ == "__main__":
    main()