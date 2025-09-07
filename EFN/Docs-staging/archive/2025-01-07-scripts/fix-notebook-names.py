#!/usr/bin/env python3
"""
Fix missing 'name' parameters in test notebook
"""

import json
import sys

def fix_notebook(input_file, output_file):
    """Add missing name parameters to all fields"""
    
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    fixed_count = 0
    
    # Fix fields
    if 'ui-specification' in data and 'fields' in data['ui-specification']:
        fields = data['ui-specification']['fields']
        for field_id, field_def in fields.items():
            params = field_def.get('component-parameters', {})
            
            # Add name if missing
            if 'name' not in params:
                params['name'] = field_id
                fixed_count += 1
                print(f"Added name='{field_id}' to field '{field_id}'")
            
            # Ensure component-parameters exists
            field_def['component-parameters'] = params
    
    # Write fixed version
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\nFixed {fixed_count} fields")
    print(f"Output written to: {output_file}")
    
    return fixed_count

if __name__ == "__main__":
    input_file = "production/test-notebook-fixed.json"
    output_file = "production/test-notebook-with-names.json"
    
    print("Fixing missing name parameters in test notebook...")
    print("=" * 60)
    
    fixed = fix_notebook(input_file, output_file)
    
    if fixed > 0:
        print("\n✅ Notebook fixed successfully!")
        print("Try importing: test-notebook-with-names.json")
    else:
        print("\n✓ No fixes needed - all fields already have names")