#!/usr/bin/env python3
"""
Add structured metadata headers to all source documentation files.
This enables better processing and understanding by LLMs and tools.

Usage:
    python add-structured-metadata.py
"""

from pathlib import Path
import re

# Metadata templates for different document types
METADATA_TEMPLATES = {
    'field-categories': {
        'purpose': 'field-configuration',
        'generates': 'json-fields',
        'requires': ['valid-json', 'unique-names', 'fviews-layer'],
        'version': '3.0.0',
        'depth-tags': ['essential', 'important', 'comprehensive']
    },
    'patterns': {
        'purpose': 'implementation-patterns',
        'generates': 'notebook-structures',
        'requires': ['field-definitions', 'form-hierarchy'],
        'version': '3.0.0',
        'depth-tags': ['essential', 'important']
    },
    'references': {
        'purpose': 'technical-reference',
        'generates': 'lookup-tables',
        'requires': ['fieldmark-knowledge'],
        'version': '3.0.0',
        'depth-tags': ['essential']
    }
}

def get_document_type(filepath):
    """Determine document type from path."""
    if 'field-categories' in str(filepath):
        return 'field-categories'
    elif 'patterns' in str(filepath):
        return 'patterns'
    elif 'references' in str(filepath):
        return 'references'
    return None

def create_metadata_header(doc_type, doc_name):
    """Create structured metadata header for a document."""
    
    template = METADATA_TEMPLATES.get(doc_type, {})
    
    # Build metadata comment block
    lines = ["<!-- structured:metadata"]
    
    # Add purpose
    if 'purpose' in template:
        lines.append(f"meta:purpose: {template['purpose']}")
    
    # Add generates
    if 'generates' in template:
        lines.append(f"meta:generates: {template['generates']}")
    
    # Add requires
    if 'requires' in template:
        requires = ', '.join(template['requires'])
        lines.append(f"meta:requires: [{requires}]")
    
    # Add version
    if 'version' in template:
        lines.append(f"meta:version: {template['version']}")
    
    # Add document-specific metadata
    lines.append(f"meta:document: {doc_name}")
    
    # Add depth tags info
    if 'depth-tags' in template:
        tags = ', '.join(template['depth-tags'])
        lines.append(f"meta:depth-tags: [{tags}]")
    
    lines.append("-->")
    
    return '\n'.join(lines)

def add_metadata_to_file(filepath):
    """Add structured metadata to a file if not already present."""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if metadata already exists
    if 'structured:metadata' in content:
        print(f"  - {filepath.name}: Already has metadata")
        return False
    
    # Get document type
    doc_type = get_document_type(filepath)
    if not doc_type:
        print(f"  ⚠ {filepath.name}: Unknown document type")
        return False
    
    # Create metadata header
    doc_name = filepath.stem.replace('-v05', '').replace('-', '_')
    metadata = create_metadata_header(doc_type, doc_name)
    
    # Find where to insert metadata (after title, before first content)
    lines = content.split('\n')
    insert_pos = 0
    
    # Skip the title line
    for i, line in enumerate(lines):
        if line.startswith('# '):
            insert_pos = i + 1
            break
    
    # Skip any existing metadata comments
    while insert_pos < len(lines) and (
        lines[insert_pos].strip() == '' or 
        lines[insert_pos].startswith('<!--') or
        lines[insert_pos].startswith('**')
    ):
        insert_pos += 1
    
    # Insert metadata
    lines.insert(insert_pos, '')
    lines.insert(insert_pos + 1, metadata)
    lines.insert(insert_pos + 2, '')
    
    # Write back
    new_content = '\n'.join(lines)
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"  ✓ {filepath.name}: Added structured metadata")
    return True

def add_reference_numbers(filepath):
    """Add reference numbers to code examples for easy citation."""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Pattern for JSON code blocks
    json_pattern = r'(```json\n)'
    
    # Counter for examples
    example_counter = [1]  # Use list to modify in nested function
    doc_name = filepath.stem.replace('-v05', '')
    
    def add_example_number(match):
        num = example_counter[0]
        example_counter[0] += 1
        return f'{match.group(1)}// Example {doc_name}-{num:02d}\n'
    
    # Add reference numbers to JSON blocks
    new_content = re.sub(json_pattern, add_example_number, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return example_counter[0] - 1
    
    return 0

def main():
    """Add structured metadata to all documentation files."""
    
    production_dir = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production")
    
    print("=" * 70)
    print("ADDING STRUCTURED METADATA TO DOCUMENTATION")
    print("=" * 70)
    
    # Process field-categories
    print("\nProcessing field-categories/:")
    field_docs = sorted((production_dir / "field-categories").glob("*.md"))
    field_count = 0
    for doc in field_docs:
        if add_metadata_to_file(doc):
            field_count += 1
        # Also add reference numbers to examples
        num_examples = add_reference_numbers(doc)
        if num_examples > 0:
            print(f"    Added {num_examples} example references")
    
    # Process patterns
    print("\nProcessing patterns/:")
    pattern_docs = sorted((production_dir / "patterns").glob("*.md"))
    pattern_count = 0
    for doc in pattern_docs:
        if add_metadata_to_file(doc):
            pattern_count += 1
    
    # Process references
    print("\nProcessing references/:")
    reference_docs = sorted((production_dir / "references").glob("*.md"))
    ref_count = 0
    for doc in reference_docs:
        # Skip the auto-generated index files
        if doc.name not in ['field-type-index.md']:
            if add_metadata_to_file(doc):
                ref_count += 1
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Added metadata to:")
    print(f"  - {field_count} field documentation files")
    print(f"  - {pattern_count} pattern files")
    print(f"  - {ref_count} reference files")
    print(f"Total: {field_count + pattern_count + ref_count} files enhanced")
    
    print("\nMetadata enables:")
    print("1. Semantic understanding of document purpose")
    print("2. Dependency tracking between documents")
    print("3. Version control for format changes")
    print("4. Depth-based content filtering")
    print("5. Reference numbering for examples")

if __name__ == "__main__":
    main()