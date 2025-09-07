#!/usr/bin/env python3
"""
Add concise summary metadata tags to all documentation files.
This enables LLMs to quickly understand content without full parsing.

Usage:
    python add-summary-metadata.py
"""

from pathlib import Path
import re

# Document summaries - carefully crafted one-liners
SUMMARIES = {
    # Field categories
    'text-fields-v05': 'Seven components for text input, display, and auto-generation, including critical HRID handling and XSS security considerations.',
    'select-choice-fields-v05': 'Nine selection components from dropdowns to multi-select, with complex conditional logic and platform-specific behaviors.',
    'datetime-fields-v05': 'Four date/time components with critical format warnings, Excel corruption issues, and timezone handling requirements.',
    'number-fields-v05': 'Two number input components (BasicAutoIncrementer and TextField variants) with validation patterns and increment strategies.',
    'display-field-v05': 'Display-only RichText component for instructions and headers, with markdown support but no data capture.',
    'location-fields-v05': 'Two GPS/mapping components (TakePoint and MapFormField) with mobile-first design and accuracy requirements.',
    'media-fields-v05': 'Three media capture components (TakePhoto, AnnotationFormField, AudioFormField) with platform limitations.',
    'relationship-field-v05': 'RelationshipField for complex record linking with performance limits and hierarchical structure support.',
    
    # Patterns
    'field-selection-guide': 'Decision trees and matrices for choosing the right field component based on data requirements.',
    'form-structure-guide': 'Three-tier architecture (fields→fviews→viewsets) requirements and structural patterns.',
    'dynamic-forms-guide': 'Conditional visibility patterns using is-logic for creating adaptive forms.',
    'implementation-patterns-guide': 'Common patterns for validation, workflows, and complex form behaviors.',
    'cookbook': 'Ten parametric recipes for generating common notebook patterns with template markers.',
    
    # References
    'designer-component-mapping': 'Complete mapping table from Designer UI names to actual JSON component names.',
    'component-reference': 'Technical specifications for namespaces, types, and component parameters.',
    'constraints-reference': 'System limitations, performance boundaries, and security considerations.',
    'operations-reference': 'Migration procedures, deployment strategies, and operational guidelines.',
    'platform-reference': 'Platform-specific behaviors for web, iOS, and Android deployments.',
    'notebook-format-guide': 'Complete JSON structure specification with required sections and hierarchy.',
    'notebook-templates': 'Five complete working notebook examples from minimal to production complexity.',
    'troubleshooting-index': 'Error-to-solution mapping with diagnostic flowcharts covering 95% of common issues.',
    'file-organization-guide': 'Project structure and file naming conventions for Fieldmark documentation.',
    'navigation-index': 'Bidirectional link registry and cross-reference validation checklist.',
    'llm-navigation-manifest': 'Purpose-driven document discovery tables for LLM content navigation.',
}

def add_summary_to_file(filepath):
    """Add summary metadata to a file."""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if summary already exists
    if 'meta:summary:' in content:
        print(f"  - {filepath.name}: Already has summary")
        return False
    
    # Get the document key
    doc_key = filepath.stem
    summary = SUMMARIES.get(doc_key)
    
    if not summary:
        print(f"  ⚠ {filepath.name}: No summary defined")
        return False
    
    # Find the structured:metadata block
    metadata_pattern = r'(<!-- structured:metadata.*?\n)(.*?)(-->)'
    
    def add_summary(match):
        prefix = match.group(1)
        metadata = match.group(2)
        suffix = match.group(3)
        
        # Add summary after meta:purpose
        lines = metadata.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if 'meta:purpose:' in line:
                new_lines.append(f'meta:summary: {summary}')
        
        return prefix + '\n'.join(new_lines) + suffix
    
    # Apply the replacement
    new_content = re.sub(metadata_pattern, add_summary, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"  ✓ {filepath.name}: Added summary")
        return True
    else:
        # No structured metadata found, add after discovery metadata if present
        discovery_pattern = r'(<!-- discovery:metadata.*?-->)'
        
        def add_after_discovery(match):
            discovery = match.group(1)
            metadata_block = f'\n\n<!-- structured:metadata\nmeta:summary: {summary}\n-->'
            return discovery + metadata_block
        
        new_content = re.sub(discovery_pattern, add_after_discovery, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"  ✓ {filepath.name}: Added summary (after discovery)")
            return True
    
    return False

def main():
    """Add summary metadata to all documentation files."""
    
    production_dir = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production")
    
    print("=" * 70)
    print("ADDING SUMMARY METADATA TO DOCUMENTATION")
    print("=" * 70)
    print("\nAdding one-line summaries for LLM quick comprehension...\n")
    
    total_added = 0
    
    # Process field-categories
    print("Processing field-categories/:")
    for doc in sorted((production_dir / "field-categories").glob("*.md")):
        if add_summary_to_file(doc):
            total_added += 1
    
    # Process patterns
    print("\nProcessing patterns/:")
    for doc in sorted((production_dir / "patterns").glob("*.md")):
        if add_summary_to_file(doc):
            total_added += 1
    
    # Process references
    print("\nProcessing references/:")
    for doc in sorted((production_dir / "references").glob("*.md")):
        if doc.name != 'field-type-index.md':  # Skip index
            if add_summary_to_file(doc):
                total_added += 1
    
    print("\n" + "=" * 70)
    print(f"SUMMARY: Added {total_added} summary metadata tags")
    print("=" * 70)
    
    print("\nBenefits:")
    print("1. LLMs can instantly understand document content")
    print("2. Faster content discovery and navigation")
    print("3. More consistent high-level descriptions")
    print("4. Reduced processing time for overview queries")

if __name__ == "__main__":
    main()