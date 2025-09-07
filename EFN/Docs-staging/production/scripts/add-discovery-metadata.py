#!/usr/bin/env python3
"""
Add discovery metadata to all source documents for better LLM navigation.
"""

import os
from pathlib import Path

# Metadata mappings for each document type
METADATA_MAPPINGS = {
    # Field documentation
    "text-fields-v05.md": {
        "provides": "text-input, email-validation, template-syntax, address-structure, qr-scanning",
        "see-also": "field-selection-guide, platform-reference, constraints-reference"
    },
    "select-choice-fields-v05.md": {
        "provides": "selection-fields, radio-groups, dropdowns, hierarchical-select, multi-select",
        "see-also": "field-selection-guide, dynamic-forms-guide"
    },
    "datetime-fields-v05.md": {
        "provides": "date-pickers, time-input, datetime-now, month-picker, timezone-handling",
        "see-also": "field-selection-guide, platform-reference"
    },
    "number-fields-v05.md": {
        "provides": "numeric-input, controlled-number, auto-increment, validation-ranges",
        "see-also": "field-selection-guide, constraints-reference"
    },
    "display-field-v05.md": {
        "provides": "richtext-display, markdown-rendering, static-content",
        "see-also": "text-fields-v05"
    },
    "location-fields-v05.md": {
        "provides": "gps-capture, map-fields, coordinate-input, location-privacy",
        "see-also": "platform-reference, media-fields-v05"
    },
    "media-fields-v05.md": {
        "provides": "photo-capture, file-upload, exif-handling, size-limits",
        "see-also": "platform-reference, location-fields-v05"
    },
    "relationship-field-v05.md": {
        "provides": "record-relationships, parent-child, peer-links, access-control",
        "see-also": "form-structure-guide, dynamic-forms-guide"
    },
    
    # Pattern guides
    "field-selection-guide.md": {
        "provides": "decision-matrices, selection-guidance, comparison-tables, use-case-mapping",
        "see-also": "all-field-categories, platform-reference"
    },
    "form-structure-guide.md": {
        "provides": "viewsets, fviews, multi-section-forms, navigation-patterns",
        "see-also": "notebook-format-guide, relationship-field-v05"
    },
    "dynamic-forms-guide.md": {
        "provides": "conditional-visibility, validation-rules, computed-values, form-logic",
        "see-also": "select-choice-fields-v05, implementation-patterns-guide"
    },
    "implementation-patterns-guide.md": {
        "provides": "common-patterns, error-handling, performance-tips, best-practices",
        "see-also": "all-pattern-guides, constraints-reference"
    },
    
    # References
    "designer-component-mapping.md": {
        "provides": "field-mappings, component-names, namespaces, designer-to-json",
        "see-also": "all-field-categories, component-reference"
    },
    "component-reference.md": {
        "provides": "namespaces, formik-integration, component-types, technical-details",
        "see-also": "designer-component-mapping, all-field-categories"
    },
    "constraints-reference.md": {
        "provides": "security-issues, designer-limitations, vulnerabilities, workarounds",
        "see-also": "platform-reference, operations-reference"
    },
    "operations-reference.md": {
        "provides": "migration-procedures, troubleshooting, deployment, maintenance",
        "see-also": "constraints-reference, platform-reference"
    },
    "platform-reference.md": {
        "provides": "platform-behaviors, mobile-issues, browser-differences, offline-support",
        "see-also": "location-fields, media-fields, constraints-reference"
    },
    "notebook-format-guide.md": {
        "provides": "json-structure, notebook-requirements, fviews-structure, validation",
        "see-also": "form-structure-guide, designer-component-mapping"
    },
    "file-organization-guide.md": {
        "provides": "project-structure, file-layout, documentation-organization",
        "see-also": "manifest"
    },
    "field-type-index.md": {
        "provides": "navigation, document-structure, depth-tagging",
        "see-also": "llm-navigation-manifest"
    },
    "llm-navigation-manifest.md": {
        "provides": "document-discovery, purpose-tables, quick-navigation, content-matrix",
        "see-also": "field-type-index, all-documents"
    }
}

def add_metadata_to_file(filepath, metadata):
    """Add discovery metadata to a file after the existing metadata block."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find where to insert (after existing concat:metadata block if present)
    insert_index = 0
    in_metadata = False
    
    for i, line in enumerate(lines):
        if "<!-- concat:metadata" in line:
            in_metadata = True
        elif in_metadata and "-->" in line:
            insert_index = i + 1
            break
    
    # If no existing metadata, add after first heading
    if insert_index == 0:
        for i, line in enumerate(lines):
            if line.startswith("# "):
                insert_index = i + 1
                break
    
    # Create metadata block
    metadata_block = [
        "\n",
        "<!-- discovery:metadata\n",
        f"provides: [{metadata['provides']}]\n",
        f"see-also: [{metadata['see-also']}]\n",
        "-->\n",
        "\n"
    ]
    
    # Check if discovery metadata already exists
    content = ''.join(lines)
    if "<!-- discovery:metadata" in content:
        print(f"  - Discovery metadata already exists, skipping")
        return False
    
    # Insert metadata
    lines[insert_index:insert_index] = metadata_block
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"  - Added discovery metadata")
    return True

def main():
    """Process all documentation files."""
    base_dir = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production")
    
    print("Adding discovery metadata to documentation...")
    print("-" * 50)
    
    files_updated = 0
    
    # Process field-categories
    print("\nField Documentation:")
    for filename, metadata in METADATA_MAPPINGS.items():
        if filename.endswith("-v05.md") or filename.endswith("-field-v05.md"):
            filepath = base_dir / "field-categories" / filename
            if filepath.exists():
                print(f"  {filename}:")
                if add_metadata_to_file(filepath, metadata):
                    files_updated += 1
    
    # Process patterns
    print("\nPattern Guides:")
    for filename, metadata in METADATA_MAPPINGS.items():
        if filename.endswith("-guide.md"):
            filepath = base_dir / "patterns" / filename
            if filepath.exists():
                print(f"  {filename}:")
                if add_metadata_to_file(filepath, metadata):
                    files_updated += 1
    
    # Process references
    print("\nTechnical References:")
    for filename, metadata in METADATA_MAPPINGS.items():
        if filename.endswith("-reference.md") or filename.endswith("-index.md") or filename.endswith("-manifest.md") or filename == "notebook-format-guide.md" or filename == "file-organization-guide.md":
            filepath = base_dir / "references" / filename
            if filepath.exists():
                print(f"  {filename}:")
                if add_metadata_to_file(filepath, metadata):
                    files_updated += 1
    
    print("\n" + "=" * 50)
    print(f"Summary: Added metadata to {files_updated} files")

if __name__ == "__main__":
    main()