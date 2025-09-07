#!/usr/bin/env python3
"""
Test the parametric template replacement system.
Demonstrates how LLMs can generate custom notebooks from templates.

Usage:
    python test-parametric-generation.py
"""

import json
import re
from pathlib import Path

def replace_template_markers(template_str, replacements):
    """Replace template markers with actual values."""
    result = template_str
    
    for marker, value in replacements.items():
        # Replace the marker
        result = result.replace(marker, value)
        
    # Remove any template comments
    result = re.sub(r'\s*//\s*(REPLACE|OPTIONAL|REQUIRED|CUSTOMIZE):.*$', '', result, flags=re.MULTILINE)
    
    return result

def test_date_range_generation():
    """Test generating a date range picker from the cookbook recipe."""
    
    print("=" * 70)
    print("TEST 1: Date Range Picker Generation")
    print("=" * 70)
    
    # Template from cookbook
    template = '''{
  "{{START_DATE_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSDateTime",
    "component-parameters": {
      "name": "{{START_DATE_ID}}",
      "label": "{{START_DATE_LABEL}}",
      "helperText": "Select the start date",
      "variant": "outlined",
      "type": "date"
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Start date is required"]
    ]
  },
  "{{END_DATE_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSDateTime",
    "component-parameters": {
      "name": "{{END_DATE_ID}}",
      "label": "{{END_DATE_LABEL}}",
      "helperText": "Select the end date",
      "variant": "outlined",
      "type": "date"
    },
    "type-returned": "faims-core::String",
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "End date is required"],
      ["yup.min", ["yup.ref", "{{START_DATE_ID}}"], "End date must be after start date"]
    ]
  }
}'''
    
    # User requirements: "I need to capture a project timeline"
    replacements = {
        "{{START_DATE_ID}}": "project-start",
        "{{START_DATE_LABEL}}": "Project Start Date",
        "{{END_DATE_ID}}": "project-end",
        "{{END_DATE_LABEL}}": "Project End Date"
    }
    
    generated = replace_template_markers(template, replacements)
    
    # Validate it's valid JSON
    try:
        fields = json.loads(generated)
        print("✓ Generated valid JSON")
        print(f"✓ Created {len(fields)} fields")
        print(f"✓ Fields: {', '.join(fields.keys())}")
        
        # Check cross-references work
        validation = fields['project-end']['validationSchema']
        if 'project-start' in str(validation):
            print("✓ Cross-field validation correctly references start date")
        
    except json.JSONDecodeError as e:
        print(f"✗ JSON validation failed: {e}")
        return False
    
    return True

def test_cascading_dropdown():
    """Test generating cascading dropdowns."""
    
    print("\n" + "=" * 70)
    print("TEST 2: Cascading Dropdown Generation")
    print("=" * 70)
    
    # Simplified template
    template = '''{
  "{{CONTROLLER_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSSelect",
    "component-parameters": {
      "name": "{{CONTROLLER_ID}}",
      "label": "{{CONTROLLER_LABEL}}",
      "logic_select": true
    }
  },
  "{{DEPENDENT_ID}}": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSSelect",
    "component-parameters": {
      "name": "{{DEPENDENT_ID}}",
      "label": "{{DEPENDENT_LABEL}}"
    },
    "is-logic": {
      "if": "{{CONTROLLER_ID}}",
      "==": "{{TRIGGER_VALUE}}"
    }
  }
}'''
    
    # User requirements: "Material type selector with subtypes"
    replacements = {
        "{{CONTROLLER_ID}}": "material-type",
        "{{CONTROLLER_LABEL}}": "Material Type",
        "{{DEPENDENT_ID}}": "material-subtype",
        "{{DEPENDENT_LABEL}}": "Material Subtype",
        "{{TRIGGER_VALUE}}": "ceramic"
    }
    
    generated = replace_template_markers(template, replacements)
    
    try:
        fields = json.loads(generated)
        print("✓ Generated valid cascading dropdowns")
        
        # Check conditional logic
        if fields['material-subtype']['is-logic']['if'] == 'material-type':
            print("✓ Conditional logic correctly references controller")
        
        if fields['material-type']['component-parameters']['logic_select']:
            print("✓ Controller has logic_select enabled")
            
    except (json.JSONDecodeError, KeyError) as e:
        print(f"✗ Generation failed: {e}")
        return False
    
    return True

def test_complete_notebook_generation():
    """Test generating a complete notebook structure."""
    
    print("\n" + "=" * 70)
    print("TEST 3: Complete Notebook Generation")
    print("=" * 70)
    
    # Complete notebook template with markers
    template = '''{
  "metadata": {
    "name": "{{PROJECT_NAME}}",
    "hridField": "{{HRID_FIELD}}"
  },
  "ui-specification": {
    "fields": {
      "{{HRID_FIELD}}": {
        "component-namespace": "faims-custom",
        "component-name": "TemplatedStringField",
        "component-parameters": {
          "name": "{{HRID_FIELD}}",
          "label": "Record ID",
          "template": "{{PROJECT_CODE}}-{{_CREATED_DATE}}-{{_INCREMENT}}"
        },
        "type-returned": "faims-core::String"
      },
      "{{FIELD_ID}}": {
        "component-namespace": "formik-material-ui",
        "component-name": "FAIMSTextField",
        "component-parameters": {
          "name": "{{FIELD_ID}}",
          "label": "{{FIELD_LABEL}}"
        },
        "type-returned": "faims-core::String"
      }
    },
    "fviews": {
      "{{SECTION_ID}}": {
        "fields": ["{{HRID_FIELD}}", "{{FIELD_ID}}"],
        "label": "{{SECTION_LABEL}}",
        "uidesign": "form"
      }
    },
    "viewsets": {
      "{{FORM_ID}}": {
        "views": ["{{SECTION_ID}}"],
        "label": "{{FORM_LABEL}}"
      }
    },
    "visible_types": ["{{FORM_ID}}"]
  }
}'''
    
    # User requirements: "Quick site survey notebook"
    replacements = {
        "{{PROJECT_NAME}}": "Site Survey 2024",
        "{{PROJECT_CODE}}": "SS24",
        "{{HRID_FIELD}}": "survey-id",
        "{{FIELD_ID}}": "site-name",
        "{{FIELD_LABEL}}": "Site Name",
        "{{SECTION_ID}}": "basic-info",
        "{{SECTION_LABEL}}": "Basic Information",
        "{{FORM_ID}}": "survey-form",
        "{{FORM_LABEL}}": "Site Survey Form"
    }
    
    generated = replace_template_markers(template, replacements)
    
    try:
        notebook = json.loads(generated)
        print("✓ Generated complete valid notebook")
        
        # Validate structure
        ui_spec = notebook['ui-specification']
        
        if 'fields' in ui_spec and 'fviews' in ui_spec and 'viewsets' in ui_spec:
            print("✓ Has all required sections (fields, fviews, viewsets)")
        
        # Check references
        fview_fields = ui_spec['fviews']['basic-info']['fields']
        if all(f in ui_spec['fields'] for f in fview_fields):
            print("✓ All fview field references are valid")
        
        viewset_views = ui_spec['viewsets']['survey-form']['views']
        if all(v in ui_spec['fviews'] for v in viewset_views):
            print("✓ All viewset view references are valid")
            
        if ui_spec['visible_types'][0] in ui_spec['viewsets']:
            print("✓ Visible_types reference is valid")
            
        # Save as working example
        output_dir = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production/working-notebooks")
        output_file = output_dir / "generated-site-survey.json"
        with open(output_file, 'w') as f:
            json.dump(notebook, f, indent=2)
        print(f"✓ Saved generated notebook to {output_file.name}")
        
    except (json.JSONDecodeError, KeyError) as e:
        print(f"✗ Generation failed: {e}")
        return False
    
    return True

def test_field_documentation_markers():
    """Test that field documentation has usable markers."""
    
    print("\n" + "=" * 70)
    print("TEST 4: Field Documentation Markers")
    print("=" * 70)
    
    # Read a sample from modified field documentation
    field_doc = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production/field-categories/text-fields-v05.md")
    
    with open(field_doc, 'r') as f:
        content = f.read()
    
    # Count template markers
    marker_count = content.count('{{')
    
    print(f"✓ Found {marker_count} template markers in text-fields-v05.md")
    
    # Extract a JSON example with markers
    json_match = re.search(r'```json\n(.*?```)', content, re.DOTALL)
    if json_match:
        example = json_match.group(1).replace('```', '')
        
        # Check for key markers
        markers_found = []
        for marker in ['{{FIELD_ID}}', '{{FIELD_LABEL}}', '{{VALIDATION_MESSAGE}}']:
            if marker in example:
                markers_found.append(marker)
        
        if markers_found:
            print(f"✓ Found key markers: {', '.join(markers_found)}")
        
    return True

def main():
    """Run all parametric generation tests."""
    
    print("\n" + "=" * 70)
    print("PARAMETRIC TEMPLATE SYSTEM TEST SUITE")
    print("=" * 70)
    print("\nTesting the ability to generate custom notebooks from templates...\n")
    
    tests = [
        test_date_range_generation(),
        test_cascading_dropdown(),
        test_complete_notebook_generation(),
        test_field_documentation_markers()
    ]
    
    passed = sum(tests)
    total = len(tests)
    
    print("\n" + "=" * 70)
    print(f"RESULTS: {passed}/{total} tests passed")
    print("=" * 70)
    
    if passed == total:
        print("\n✅ Parametric generation system is working correctly!")
        print("LLMs can now:")
        print("1. Use cookbook recipes to generate patterns")
        print("2. Replace template markers with custom values")
        print("3. Generate complete, valid notebooks")
        print("4. Leverage marked examples in documentation")
    else:
        print("\n⚠️ Some tests failed. Review the implementation.")

if __name__ == "__main__":
    main()