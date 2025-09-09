#!/usr/bin/env python3
"""Auto-fix common JSON issues in documentation"""
import re
from pathlib import Path

def fix_namespace(content):
    # Update deprecated namespace
    return content.replace('"component-namespace": "faims3"',
                          '"component-namespace": "faims-custom"')

def add_initial_values(content):
    # Add initialValue to required fields
    # This is complex and needs manual review
    return content

def fix_file(filepath):
    content = filepath.read_text()
    original = content
    content = fix_namespace(content)
    content = add_initial_values(content)
    if content != original:
        filepath.write_text(content)
        print(f'Fixed: {filepath}')

if __name__ == '__main__':
    for md_file in Path('.').rglob('*.md'):
        fix_file(md_file)