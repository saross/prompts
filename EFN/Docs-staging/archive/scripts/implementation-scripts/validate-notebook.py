#!/usr/bin/env python3
"""
Validate test notebook for import compatibility
"""

import json
import sys
from pathlib import Path

# Valid components based on actual FAIMS3 registry
VALID_COMPONENTS = {
    'faims-custom': [
        'FAIMSTextField', 'Select', 'MultiSelect', 'AdvancedSelect',
        'Checkbox', 'RadioGroup', 'RichText', 'TakePhoto', 
        'FileUploader', 'TakePoint', 'DatePicker',
        'DateTimePicker', 'MonthPicker', 'DateTimeNow',
        'RelatedRecordSelector', 'BasicAutoIncrementer',
        'TemplatedStringField', 'AddressField', 'ActionButton',
        'RandomStyle', 'NumberField'
    ],
    'formik-material-ui': [
        'TextField', 'Select', 'RadioGroup', 'Checkbox', 'MultipleTextField'
    ],
    'mapping-plugin': ['MapFormField'],
    'qrcode': ['QRCodeFormField'],
    'core-material-ui': ['Input', 'Checkbox', 'TextField']
}

def validate_notebook(notebook_path):
    """Validate a notebook JSON file"""
    
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
    
    errors = []
    warnings = []
    
    # Check metadata
    if 'metadata' not in notebook:
        errors.append("Missing 'metadata' section")
    
    # Check fields (can be at root or under ui-specification)
    fields = None
    if 'fields' in notebook:
        fields = notebook['fields']
    elif 'ui-specification' in notebook and 'fields' in notebook['ui-specification']:
        fields = notebook['ui-specification']['fields']
    else:
        errors.append("Missing 'fields' section (checked root and ui-specification)")
    
    if fields:
        for field_id, field_def in fields.items():
            # Check component namespace
            namespace = field_def.get('component-namespace')
            component = field_def.get('component-name')
            
            if not namespace:
                errors.append(f"Field '{field_id}': Missing component-namespace")
            elif namespace not in VALID_COMPONENTS:
                errors.append(f"Field '{field_id}': Invalid namespace '{namespace}'")
            
            if not component:
                errors.append(f"Field '{field_id}': Missing component-name")
            elif namespace and namespace in VALID_COMPONENTS:
                if component not in VALID_COMPONENTS[namespace]:
                    errors.append(f"Field '{field_id}': Component '{component}' not valid for namespace '{namespace}'")
            
            # Check type-returned
            if 'type-returned' not in field_def:
                warnings.append(f"Field '{field_id}': Missing type-returned")
            
            # Check component-parameters
            if 'component-parameters' not in field_def:
                warnings.append(f"Field '{field_id}': Missing component-parameters")
    
    # Check viewsets (can be at root or under ui-specification)
    viewsets = None
    if 'viewsets' in notebook:
        viewsets = notebook['viewsets']
    elif 'ui-specification' in notebook and 'viewsets' in notebook['ui-specification']:
        viewsets = notebook['ui-specification']['viewsets']
    else:
        errors.append("Missing 'viewsets' section (checked root and ui-specification)")
    
    # Check ui-specification
    if 'ui-specification' not in notebook:
        errors.append("Missing 'ui-specification' section")
    
    return errors, warnings

def main():
    """Main validation function"""
    
    notebook_path = Path('production/test-notebook-fixed.json')
    
    if not notebook_path.exists():
        print(f"Error: File not found: {notebook_path}")
        sys.exit(1)
    
    print(f"Validating: {notebook_path}")
    print("=" * 60)
    
    errors, warnings = validate_notebook(notebook_path)
    
    if errors:
        print(f"\n❌ Found {len(errors)} ERRORS:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("\n✅ No errors found!")
    
    if warnings:
        print(f"\n⚠️  Found {len(warnings)} WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    if errors:
        print("\n🔴 Notebook may fail to import due to errors")
        sys.exit(1)
    else:
        print("\n🟢 Notebook should import successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()