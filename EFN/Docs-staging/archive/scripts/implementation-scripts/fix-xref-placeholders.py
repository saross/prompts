#!/usr/bin/env python3
"""
Fix broken XREF placeholders in field documentation.
Replaces generic XREF tags with proper section anchors or document references.
"""

import os
import re
from pathlib import Path

# Mapping of XREF patterns to their replacements
XREF_MAPPINGS = {
    # Text field references
    r"`XREF` See \[JSON Examples > TextField Examples\]": 
        "See [TextField Configuration](#textfield-configuration)",
    
    r"`XREF` See \[JSON Examples > TemplatedString Examples\]": 
        "See [TemplatedString Configuration](#templatedstring-configuration)",
    
    r"`XREF` See \[JSON Examples > QRCodeFormField with Manual Fallback\]": 
        "See [QRCodeFormField Configuration](#qrcodefield-configuration)",
    
    r"`XREF` See \[Field Quirks Index > Email\]": 
        "See [Email Field Quirks](#email-quirks)",
    
    r"`XREF` See \[Field Quirks Index > RichText\]": 
        "See [RichText Display Limitations](#display-limitations)",
    
    r"`XREF` See \[Troubleshooting Guide > Address Field Race Condition\]": 
        "See [Address Field Issues](#address-specific-issues)",
    
    # Number field references
    r"`XREF` See \[Common Characteristics > Platform Behaviors.*?\]": 
        "See [Platform-Specific Behaviors](../references/platform-reference.md)",
    
    r"`XREF` See \[Common Characteristics > Configuration Rules\]": 
        "See [Configuration Rules](#configuration-rules)",
    
    r"`XREF` See \[Common Characteristics > Validation Patterns\]": 
        "See [Validation Patterns](#validation-patterns)",
    
    r"`XREF` See \[Common Characteristics > Data Type Specifications\]": 
        "See [Data Type Specifications](#data-types)",
    
    r"`XREF` See \[Common Characteristics > Voice Input Requirements\]": 
        "See [Platform Notes](#platform-notes)",
    
    r"`XREF` See \[Common Characteristics > Accessibility Compliance\]": 
        "See [Accessibility Considerations](#accessibility)",
    
    r"`XREF` See \[Common Characteristics > Performance Boundaries\]": 
        "See [Performance Considerations](#performance-considerations)",
    
    r"`XREF` See \[Migration and Best Practices > Known Limitations\]": 
        "See [Known Limitations](#known-limitations)",
    
    r"`XREF` See \[Overview > Designer Quick Guide\]": 
        "See [Designer Quick Guide](#designer-quick-guide)",
    
    r"`XREF` See \[Overview > CRITICAL: Deprecated Field Warning\]": 
        "See [Deprecated Field Warning](#deprecated-warning)",
    
    r"`XREF` See \[Individual Field Reference > .*?\]": 
        "See field details above",
    
    r"`XREF` See \[Field Interaction Matrix > .*?\]": 
        "See [Field Interactions](#field-interactions)",
    
    r"`XREF` See \[Performance Thresholds Table\]": 
        "See [Performance Thresholds](#performance-thresholds)",
    
    r"`XREF` See \[Troubleshooting Guide > Detailed Issue Matrix\]": 
        "See [Troubleshooting](../references/troubleshooting-index.md)",
    
    # DateTime field references
    r"`XREF` See \[Field Reference > DateTimeNow\]": 
        "See [DateTimeNow Configuration](#datetimenow-configuration)",
    
    r"`XREF` See \[Field Reference > DatePicker\]": 
        "See [DatePicker Configuration](#datepicker-configuration)",
    
    r"`XREF` See \[Field Reference > MonthPicker\]": 
        "See [MonthPicker Configuration](#monthpicker-configuration)",
    
    r"`XREF` See \[Troubleshooting Guide > Critical Issues\]": 
        "See [Critical Issues](#critical-issues)",
    
    r"`XREF` See \[Troubleshooting Guide > Excel Date Format Corruption\]": 
        "See [Excel Export Issues](#excel-export-issues)",
    
    r"`XREF` See \[Troubleshooting Guide > When Format Issues Occur\]": 
        "See [Format Issues](#format-issues)",
    
    r"`XREF` See \[Migration Warnings Index > Safe Migrations\]": 
        "See [Migration Guide](../references/operations-reference.md)",
    
    r"`XREF` See \[Field Selection Guide > Quick Decision Matrix\]": 
        "See [Field Selection Guide](../patterns/field-selection-guide.md)",
    
    r"`XREF` See \[JSON Examples > Integration Patterns\]": 
        "See [Integration Patterns](#integration-patterns)",
}

def fix_xrefs_in_file(filepath):
    """Fix XREF placeholders in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    replacements = 0
    
    for pattern, replacement in XREF_MAPPINGS.items():
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0:
            content = new_content
            replacements += count
            print(f"  - Replaced {count} instances of: {pattern[:50]}...")
    
    if replacements > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Total: {replacements} XREFs fixed in {filepath.name}")
        return replacements
    return 0

def main():
    """Process all field documentation files."""
    base_dir = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production/field-categories")
    
    if not base_dir.exists():
        print(f"Error: Directory {base_dir} not found")
        return
    
    print("Fixing XREF placeholders in field documentation...")
    print("-" * 50)
    
    total_fixes = 0
    files_processed = 0
    
    for filepath in sorted(base_dir.glob("*.md")):
        print(f"\nProcessing: {filepath.name}")
        fixes = fix_xrefs_in_file(filepath)
        if fixes > 0:
            files_processed += 1
            total_fixes += fixes
    
    print("\n" + "=" * 50)
    print(f"Summary: Fixed {total_fixes} XREFs across {files_processed} files")

if __name__ == "__main__":
    main()