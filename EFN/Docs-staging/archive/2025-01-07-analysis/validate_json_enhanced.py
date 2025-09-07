#!/usr/bin/env python3
"""
Enhanced JSON Validation Script for Fieldmark Documentation
Handles JSON with comments and common documentation patterns.
"""

import json
import re
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, field
from collections import defaultdict

@dataclass
class ValidationIssue:
    """Represents a validation issue found in JSON"""
    severity: str  # 'error', 'warning', 'info'
    file: str
    line: int
    message: str
    json_snippet: str = ""

@dataclass 
class ValidationStats:
    """Statistics about validation results"""
    total_examples: int = 0
    syntax_valid: int = 0
    schema_compliant: int = 0
    component_valid: int = 0
    security_issues: int = 0
    namespace_usage: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    component_usage: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    type_usage: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    examples_with_comments: int = 0
    examples_with_ellipsis: int = 0

class EnhancedFieldmarkJSONValidator:
    """Enhanced validator that handles documentation patterns"""
    
    # Valid component namespaces from FAIMS3 codebase
    VALID_NAMESPACES = {
        'formik-material-ui',
        'faims-custom', 
        'mapping-plugin',
        'qrcode',
        'faims3'  # Deprecated but still found
    }
    
    # Component registry - expanded based on codebase
    COMPONENT_REGISTRY = {
        'formik-material-ui': ['TextField', 'Select', 'RadioGroup', 'Checkbox'],
        'faims-custom': [
            'TextField', 'MultilineTextField', 'MultipleTextField', 'Select', 'MultiSelect',
            'AdvancedSelect', 'Checkbox', 'RadioGroup', 'RichText', 
            'TakePhoto', 'FileUploader', 'AudioRecorder', 'VideoRecorder',
            'TakePoint', 'MapFormField', 'DatePicker', 'TimePicker', 
            'DateTimePicker', 'DateTimeNow', 'RelatedRecordSelector', 
            'BasicAutoIncrementer', 'TemplatedStringField', 'Address', 
            'ActionButton', 'RandomStyle', 'TemplatedIntegerField', 
            'TemplatedFloatField', 'ControlledNumber'
        ],
        'mapping-plugin': ['MapFormField'],
        'qrcode': ['QRCodeFormField']
    }
    
    # Valid type-returned values - corrected based on actual codebase
    VALID_TYPES = {
        'faims-core::String',
        'faims-core::Integer',
        'faims-core::Float', 
        'faims-core::Bool',
        'faims-pos::Location',
        'faims-attachment::Files'
    }
    
    # Type mappings for common mistakes
    TYPE_CORRECTIONS = {
        'faims-core::Array': 'faims-core::String',  # Arrays are serialized as strings
        'faims-core::JSON': 'faims-core::String',    # JSON is stored as string
        'Array': 'faims-core::String',
        'JSON': 'faims-core::String'
    }
    
    def __init__(self):
        self.issues: List[ValidationIssue] = []
        self.stats = ValidationStats()
        
    def clean_json_string(self, json_str: str) -> Tuple[str, bool, bool]:
        """
        Clean JSON string by removing comments and handling ellipsis
        Returns: (cleaned_json, had_comments, had_ellipsis)
        """
        had_comments = '//' in json_str or '/*' in json_str
        had_ellipsis = '...' in json_str
        
        if had_comments:
            self.stats.examples_with_comments += 1
            
        if had_ellipsis:
            self.stats.examples_with_ellipsis += 1
        
        # Remove single-line comments
        json_str = re.sub(r'//.*?$', '', json_str, flags=re.MULTILINE)
        
        # Remove multi-line comments
        json_str = re.sub(r'/\*.*?\*/', '', json_str, flags=re.DOTALL)
        
        # Handle ellipsis in arrays/objects - replace with empty placeholder
        json_str = re.sub(r',\s*\.\.\.', '', json_str)
        json_str = re.sub(r'\.\.\.', '""', json_str)
        
        # Remove trailing commas before closing brackets
        json_str = re.sub(r',\s*([}\]])', r'\1', json_str)
        
        return json_str, had_comments, had_ellipsis
    
    def extract_json_from_markdown(self, filepath: Path) -> List[Tuple[str, int, str]]:
        """
        Extract JSON blocks from markdown file
        Returns: List of (json_string, line_number, context)
        """
        json_blocks = []
        
        with open(filepath, 'r') as f:
            lines = f.readlines()
            
        in_json_block = False
        json_lines = []
        start_line = 0
        context = ""
        
        for i, line in enumerate(lines, 1):
            # Look for context headers before JSON blocks
            if line.startswith('#') and not in_json_block:
                context = line.strip()
                
            if line.strip() == '```json':
                in_json_block = True
                json_lines = []
                start_line = i
            elif in_json_block and line.strip() == '```':
                in_json_block = False
                if json_lines:
                    json_str = ''.join(json_lines)
                    json_blocks.append((json_str, start_line, context))
            elif in_json_block:
                json_lines.append(line)
                
        return json_blocks
    
    def validate_json_syntax(self, json_str: str, file: str, line: int) -> Optional[Dict]:
        """Validate JSON syntax and return parsed object"""
        # Clean the JSON first
        cleaned_json, had_comments, had_ellipsis = self.clean_json_string(json_str)
        
        try:
            obj = json.loads(cleaned_json)
            self.stats.syntax_valid += 1
            
            # Add info about cleaning if it happened
            if had_comments or had_ellipsis:
                notes = []
                if had_comments:
                    notes.append("contains comments")
                if had_ellipsis:
                    notes.append("contains ellipsis")
                self.issues.append(ValidationIssue(
                    severity='info',
                    file=file,
                    line=line,
                    message=f"JSON cleaned ({', '.join(notes)})",
                    json_snippet=json_str[:50]
                ))
            
            return obj
        except json.JSONDecodeError as e:
            self.issues.append(ValidationIssue(
                severity='error',
                file=file,
                line=line + e.lineno,
                message=f"JSON syntax error after cleaning: {e.msg}",
                json_snippet=cleaned_json[:100]
            ))
            return None
    
    def validate_field_definition(self, obj: Dict, file: str, line: int) -> None:
        """Validate a field definition against schema requirements"""
        # Skip fragments that are just parameters
        if 'component-namespace' not in obj and 'component-name' not in obj:
            # This might be a component-parameters fragment
            return
            
        # Check required properties for full field definitions
        required = {'component-namespace', 'component-name', 'type-returned'}
        present = set(obj.keys())
        
        if 'component-namespace' in obj or 'component-name' in obj:
            # This looks like it should be a complete field definition
            missing = required - present
            if missing:
                self.issues.append(ValidationIssue(
                    severity='warning',
                    file=file,
                    line=line,
                    message=f"Incomplete field definition, missing: {missing}",
                    json_snippet=json.dumps(obj)[:100]
                ))
            else:
                self.stats.schema_compliant += 1
                
        # Validate namespace
        namespace = obj.get('component-namespace', '')
        if namespace:
            self.stats.namespace_usage[namespace] += 1
            if namespace not in self.VALID_NAMESPACES and namespace != 'ANY-namespace':
                self.issues.append(ValidationIssue(
                    severity='error',
                    file=file,
                    line=line,
                    message=f"Invalid namespace '{namespace}'",
                    json_snippet=json.dumps(obj)[:100]
                ))
            elif namespace == 'faims3':
                self.issues.append(ValidationIssue(
                    severity='info',
                    file=file,
                    line=line,
                    message="Namespace 'faims3' is deprecated, use 'faims-custom'",
                    json_snippet=json.dumps(obj)[:100]
                ))
                
        # Validate component
        component = obj.get('component-name', '')
        if component and namespace:
            self.stats.component_usage[component] += 1
            if namespace in self.COMPONENT_REGISTRY:
                valid_components = self.COMPONENT_REGISTRY[namespace]
                if component not in valid_components:
                    # Check if it's a known component in wrong namespace
                    found_in = []
                    for ns, comps in self.COMPONENT_REGISTRY.items():
                        if component in comps:
                            found_in.append(ns)
                    
                    if found_in:
                        self.issues.append(ValidationIssue(
                            severity='warning',
                            file=file,
                            line=line,
                            message=f"Component '{component}' not in '{namespace}', found in: {found_in}",
                            json_snippet=json.dumps(obj)[:100]
                        ))
                    else:
                        self.issues.append(ValidationIssue(
                            severity='info',
                            file=file,
                            line=line,
                            message=f"Unknown component '{component}' for namespace '{namespace}'",
                            json_snippet=json.dumps(obj)[:100]
                        ))
                else:
                    self.stats.component_valid += 1
                    
        # Validate and correct type-returned
        type_returned = obj.get('type-returned', '')
        if type_returned:
            self.stats.type_usage[type_returned] += 1
            
            # Check if it needs correction
            if type_returned in self.TYPE_CORRECTIONS:
                correct_type = self.TYPE_CORRECTIONS[type_returned]
                self.issues.append(ValidationIssue(
                    severity='warning',
                    file=file,
                    line=line,
                    message=f"Invalid type '{type_returned}', should be '{correct_type}'",
                    json_snippet=json.dumps(obj)[:100]
                ))
            elif type_returned not in self.VALID_TYPES:
                self.issues.append(ValidationIssue(
                    severity='error',
                    file=file,
                    line=line,
                    message=f"Unknown type '{type_returned}'",
                    json_snippet=json.dumps(obj)[:100]
                ))
                
        # Check for security issues
        self.check_security_issues(obj, file, line)
        
        # Validate validation schema
        if 'validationSchema' in obj:
            self.validate_validation_schema(obj['validationSchema'], file, line)
            
    def check_security_issues(self, obj: Dict, file: str, line: int) -> None:
        """Check for security vulnerabilities"""
        # Check TemplatedString for XSS
        if obj.get('component-name') == 'TemplatedStringField':
            params = obj.get('component-parameters', {})
            template = params.get('template', '') if isinstance(params, dict) else ''
            
            # Look for typical user input field names in template
            if '{{' in template:
                risky_patterns = [
                    'text', 'description', 'notes', 'comment', 
                    'input', 'user', 'name', 'title', 'custom'
                ]
                for pattern in risky_patterns:
                    if re.search(r'{{\s*\w*' + pattern + r'\w*\s*}}', template, re.IGNORECASE):
                        self.issues.append(ValidationIssue(
                            severity='warning',
                            file=file,
                            line=line,
                            message=f"Potential XSS risk: user input field in template",
                            json_snippet=template[:100]
                        ))
                        self.stats.security_issues += 1
                        break
                        
        # Check QRCodeFormField requirements
        if obj.get('component-name') == 'QRCodeFormField':
            params = obj.get('component-parameters', {})
            if isinstance(params, dict) and params.get('required'):
                self.issues.append(ValidationIssue(
                    severity='warning',
                    file=file,
                    line=line,
                    message="QRCodeFormField with required=true blocks web platform",
                    json_snippet=json.dumps(obj)[:100]
                ))
                
    def validate_validation_schema(self, schema: Any, file: str, line: int) -> None:
        """Validate Yup validation schema array"""
        if not isinstance(schema, list):
            return
            
        if len(schema) > 0 and isinstance(schema[0], list):
            # Check if first element is type declaration
            if len(schema[0]) >= 2 and schema[0][0] == 'yup':
                # Valid type declaration
                pass
            else:
                self.issues.append(ValidationIssue(
                    severity='info',
                    file=file,
                    line=line,
                    message="First validation element should be ['yup', 'type']",
                    json_snippet=str(schema[0])[:100]
                ))
                
    def process_file(self, filepath: Path) -> None:
        """Process a single markdown file"""
        json_blocks = self.extract_json_from_markdown(filepath)
        
        for json_str, line_num, context in json_blocks:
            self.stats.total_examples += 1
            
            # Validate syntax
            obj = self.validate_json_syntax(json_str, str(filepath), line_num)
            if obj is None:
                continue
                
            # Validate based on structure
            if isinstance(obj, dict):
                # Check if it's a field definition
                if 'component-namespace' in obj or 'component-name' in obj:
                    self.validate_field_definition(obj, str(filepath), line_num)
                # Check if it's a collection of fields
                else:
                    for key, value in obj.items():
                        if isinstance(value, dict) and ('component-namespace' in value or 'component-name' in value):
                            self.validate_field_definition(value, str(filepath), line_num)
                            
    def validate_directory(self, directory: Path) -> None:
        """Validate all markdown files in a directory"""
        for filepath in sorted(directory.glob('*.md')):
            self.process_file(filepath)
            
    def generate_report(self) -> str:
        """Generate enhanced validation report"""
        report = []
        report.append("# Enhanced JSON Validation Report\n")
        report.append(f"Validated {self.stats.total_examples} JSON examples\n")
        
        # Summary
        report.append("## Summary\n")
        report.append(f"- Total examples: {self.stats.total_examples}")
        report.append(f"- Syntax valid: {self.stats.syntax_valid}/{self.stats.total_examples}")
        report.append(f"- Examples with comments: {self.stats.examples_with_comments}")
        report.append(f"- Examples with ellipsis: {self.stats.examples_with_ellipsis}")
        report.append(f"- Schema compliant: {self.stats.schema_compliant}")
        report.append(f"- Component valid: {self.stats.component_valid}")
        report.append(f"- Security warnings: {self.stats.security_issues}\n")
        
        # Issues by severity
        errors = [i for i in self.issues if i.severity == 'error']
        warnings = [i for i in self.issues if i.severity == 'warning']
        info = [i for i in self.issues if i.severity == 'info']
        
        if errors:
            report.append(f"## Critical Issues ({len(errors)})\n")
            # Group errors by type
            error_types = defaultdict(list)
            for issue in errors:
                if 'syntax error' in issue.message:
                    error_types['Syntax Errors'].append(issue)
                elif 'Invalid namespace' in issue.message:
                    error_types['Invalid Namespaces'].append(issue)
                elif 'Unknown type' in issue.message:
                    error_types['Invalid Types'].append(issue)
                else:
                    error_types['Other Errors'].append(issue)
                    
            for error_type, issues in error_types.items():
                if issues:
                    report.append(f"\n### {error_type} ({len(issues)})")
                    for issue in issues[:5]:
                        report.append(f"- {issue.file}:{issue.line} - {issue.message}")
                    if len(issues) > 5:
                        report.append(f"  ... and {len(issues) - 5} more\n")
                        
        if warnings:
            report.append(f"\n## Warnings ({len(warnings)})\n")
            # Show unique warning types
            warning_types = defaultdict(int)
            for issue in warnings:
                # Extract warning type
                if 'Invalid type' in issue.message:
                    warning_types['Type corrections needed'] += 1
                elif 'Incomplete field' in issue.message:
                    warning_types['Incomplete field definitions'] += 1
                elif 'XSS risk' in issue.message:
                    warning_types['Potential XSS risks'] += 1
                elif 'QRCodeFormField' in issue.message:
                    warning_types['QRCode platform issues'] += 1
                else:
                    warning_types['Other warnings'] += 1
                    
            for warn_type, count in warning_types.items():
                report.append(f"- {warn_type}: {count}")
                
        # Statistics
        report.append("\n## Statistics\n")
        
        report.append("### Namespace Usage")
        for ns, count in sorted(self.stats.namespace_usage.items()):
            status = "✓" if ns in self.VALID_NAMESPACES and ns != 'faims3' else "⚠️"
            report.append(f"- {status} {ns}: {count}")
            
        report.append("\n### Top Components")
        for comp, count in sorted(self.stats.component_usage.items(), 
                                 key=lambda x: x[1], reverse=True)[:15]:
            report.append(f"- {comp}: {count}")
            
        report.append("\n### Type Distribution")
        for type_val, count in sorted(self.stats.type_usage.items()):
            if type_val in self.VALID_TYPES:
                status = "✓"
            elif type_val in self.TYPE_CORRECTIONS:
                status = "⚠️ (needs correction)"
            else:
                status = "✗"
            report.append(f"- {status} {type_val}: {count}")
            
        # Recommendations
        report.append("\n## Recommendations\n")
        if 'faims-core::Array' in self.stats.type_usage:
            report.append("1. Replace all `faims-core::Array` with `faims-core::String`")
        if 'faims-core::JSON' in self.stats.type_usage:
            report.append("2. Replace all `faims-core::JSON` with `faims-core::String`")
        if self.stats.examples_with_comments > 0:
            report.append(f"3. {self.stats.examples_with_comments} examples use comments - consider separate documentation")
        if self.stats.security_issues > 0:
            report.append(f"4. Review {self.stats.security_issues} potential XSS vulnerabilities in TemplatedString fields")
            
        return '\n'.join(report)

def main():
    """Main execution"""
    validator = EnhancedFieldmarkJSONValidator()
    
    # Process directories
    for dir_name in ['field-categories', 'patterns']:
        dir_path = Path(dir_name)
        if dir_path.exists():
            print(f"Processing {dir_path}...")
            validator.validate_directory(dir_path)
    
    # Generate report
    report = validator.generate_report()
    report_file = Path('validation_report_enhanced.md')
    report_file.write_text(report)
    print(f"\nEnhanced validation report saved to {report_file}")
    
    # Print summary
    print(f"\nSummary:")
    print(f"  Total examples: {validator.stats.total_examples}")
    print(f"  Syntax valid: {validator.stats.syntax_valid}")
    print(f"  With comments: {validator.stats.examples_with_comments}")
    print(f"  With ellipsis: {validator.stats.examples_with_ellipsis}")
    
    errors = [i for i in validator.issues if i.severity == 'error']
    warnings = [i for i in validator.issues if i.severity == 'warning']
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    print(f"  Security issues: {validator.stats.security_issues}")
    
if __name__ == '__main__':
    main()