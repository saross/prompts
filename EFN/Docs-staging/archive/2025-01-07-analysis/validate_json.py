#!/usr/bin/env python3
"""
JSON Validation Script for Fieldmark Documentation
Validates all JSON examples in field-categories and patterns documentation
against FAIMS3 notebook schema requirements.
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

class FieldmarkJSONValidator:
    """Validates JSON examples from Fieldmark documentation"""
    
    # Valid component namespaces from FAIMS3 codebase
    VALID_NAMESPACES = {
        'formik-material-ui',
        'faims-custom',
        'mapping-plugin',
        'qrcode',
        'faims3'  # Deprecated but still found
    }
    
    # Component registry from bundle_components.ts
    COMPONENT_REGISTRY = {
        'formik-material-ui': ['TextField', 'Select', 'RadioGroup'],
        'faims-custom': [
            'TextField', 'MultilineTextField', 'Select', 'MultiSelect', 
            'AdvancedSelect', 'Checkbox', 'RadioGroup', 'RichText',
            'TakePhoto', 'FileUploader', 'AudioRecorder', 'VideoRecorder',
            'TakePoint', 'MapFormField', 'DateTimePicker', 'DateTimeNow',
            'RelatedRecordSelector', 'BasicAutoIncrementer', 'TemplatedStringField',
            'Address', 'ActionButton', 'RandomStyle'
        ],
        'mapping-plugin': ['MapFormField'],
        'qrcode': ['QRCodeFormField']
    }
    
    # Valid type-returned values
    VALID_TYPES = {
        'faims-core::String',
        'faims-core::Integer', 
        'faims-core::Float',
        'faims-core::Bool',
        'faims-pos::Location',
        'faims-attachment::Files'
    }
    
    # Required field properties
    REQUIRED_FIELD_PROPS = {'component-namespace', 'component-name', 'type-returned'}
    
    # Notebook structure required properties
    REQUIRED_NOTEBOOK_PROPS = {
        'top': {'metadata', 'ui-specification'},
        'ui-spec': {'fields', 'fviews', 'viewsets', 'visible_types'}
    }
    
    def __init__(self):
        self.issues: List[ValidationIssue] = []
        self.stats = ValidationStats()
        
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
        try:
            obj = json.loads(json_str)
            self.stats.syntax_valid += 1
            return obj
        except json.JSONDecodeError as e:
            self.issues.append(ValidationIssue(
                severity='error',
                file=file,
                line=line + e.lineno,
                message=f"JSON syntax error: {e.msg}",
                json_snippet=json_str[:100]
            ))
            return None
    
    def is_field_definition(self, obj: Any) -> bool:
        """Check if JSON object is a field definition"""
        if not isinstance(obj, dict):
            return False
        # Field definitions have component-namespace or component-name
        return 'component-namespace' in obj or 'component-name' in obj
    
    def is_notebook_structure(self, obj: Any) -> bool:
        """Check if JSON object is a notebook structure"""
        if not isinstance(obj, dict):
            return False
        # Notebook structures have metadata or ui-specification or fviews/viewsets
        return any(key in obj for key in ['metadata', 'ui-specification', 'fviews', 'viewsets', 'fields'])
    
    def validate_field_definition(self, obj: Dict, file: str, line: int) -> None:
        """Validate a field definition against schema requirements"""
        # Check required properties
        missing_props = self.REQUIRED_FIELD_PROPS - set(obj.keys())
        if missing_props:
            self.issues.append(ValidationIssue(
                severity='error',
                file=file,
                line=line,
                message=f"Missing required properties: {missing_props}",
                json_snippet=json.dumps(obj)[:100]
            ))
        else:
            self.stats.schema_compliant += 1
            
        # Validate namespace
        namespace = obj.get('component-namespace', '')
        if namespace:
            self.stats.namespace_usage[namespace] += 1
            if namespace not in self.VALID_NAMESPACES:
                self.issues.append(ValidationIssue(
                    severity='error',
                    file=file,
                    line=line,
                    message=f"Invalid namespace '{namespace}'. Valid: {self.VALID_NAMESPACES}",
                    json_snippet=json.dumps(obj)[:100]
                ))
            elif namespace == 'faims3':
                self.issues.append(ValidationIssue(
                    severity='warning',
                    file=file,
                    line=line,
                    message="Namespace 'faims3' is deprecated, use 'faims-custom'",
                    json_snippet=json.dumps(obj)[:100]
                ))
            else:
                # Validate component name
                component = obj.get('component-name', '')
                if component:
                    self.stats.component_usage[component] += 1
                    valid_components = self.COMPONENT_REGISTRY.get(namespace, [])
                    if component not in valid_components and namespace in self.COMPONENT_REGISTRY:
                        self.issues.append(ValidationIssue(
                            severity='warning',
                            file=file,
                            line=line,
                            message=f"Component '{component}' not in registry for namespace '{namespace}'",
                            json_snippet=json.dumps(obj)[:100]
                        ))
                    else:
                        self.stats.component_valid += 1
                        
        # Validate type-returned
        type_returned = obj.get('type-returned', '')
        if type_returned:
            self.stats.type_usage[type_returned] += 1
            if type_returned not in self.VALID_TYPES:
                self.issues.append(ValidationIssue(
                    severity='error',
                    file=file,
                    line=line,
                    message=f"Invalid type-returned '{type_returned}'. Valid: {self.VALID_TYPES}",
                    json_snippet=json.dumps(obj)[:100]
                ))
                
        # Check for security issues
        self.check_security_issues(obj, file, line)
        
        # Validate validation schema if present
        if 'validationSchema' in obj:
            self.validate_validation_schema(obj['validationSchema'], file, line)
            
        # Check initialValue for required fields
        if 'component-parameters' in obj:
            params = obj['component-parameters']
            if isinstance(params, dict) and params.get('required') and 'initialValue' not in obj:
                self.issues.append(ValidationIssue(
                    severity='warning',
                    file=file,
                    line=line,
                    message="Required field missing initialValue",
                    json_snippet=json.dumps(obj)[:100]
                ))
    
    def validate_notebook_structure(self, obj: Dict, file: str, line: int) -> None:
        """Validate notebook-level structure"""
        # Check for top-level structure
        if 'metadata' in obj or 'ui-specification' in obj:
            missing = self.REQUIRED_NOTEBOOK_PROPS['top'] - set(obj.keys())
            if missing:
                self.issues.append(ValidationIssue(
                    severity='info',
                    file=file,
                    line=line,
                    message=f"Notebook structure missing: {missing}",
                    json_snippet=json.dumps(obj)[:100]
                ))
                
        # Check ui-specification structure
        if 'ui-specification' in obj:
            ui_spec = obj['ui-specification']
            if isinstance(ui_spec, dict):
                missing = self.REQUIRED_NOTEBOOK_PROPS['ui-spec'] - set(ui_spec.keys())
                if missing:
                    self.issues.append(ValidationIssue(
                        severity='info',
                        file=file,
                        line=line,
                        message=f"UI specification missing: {missing}",
                        json_snippet=json.dumps(ui_spec)[:100]
                    ))
                    
        # Validate fields within notebook
        if 'fields' in obj:
            for field_id, field_def in obj.get('fields', {}).items():
                if isinstance(field_def, dict):
                    self.validate_field_definition(field_def, file, line)
                    
        # Validate conditions
        if 'condition' in obj:
            self.validate_condition(obj['condition'], file, line)
    
    def validate_condition(self, condition: Any, file: str, line: int) -> None:
        """Validate conditional logic structure"""
        if not isinstance(condition, dict):
            return
            
        operator = condition.get('operator')
        if operator in ['and', 'or']:
            # Validate nested conditions
            conditions = condition.get('conditions', [])
            if not isinstance(conditions, list):
                self.issues.append(ValidationIssue(
                    severity='error',
                    file=file,
                    line=line,
                    message=f"Operator '{operator}' requires 'conditions' array",
                    json_snippet=json.dumps(condition)[:100]
                ))
            else:
                for cond in conditions:
                    self.validate_condition(cond, file, line)
        elif operator in ['equal', 'not_equal', 'greater', 'less']:
            # Validate simple condition
            if 'field' not in condition:
                self.issues.append(ValidationIssue(
                    severity='error',
                    file=file,
                    line=line,
                    message=f"Condition missing 'field' property",
                    json_snippet=json.dumps(condition)[:100]
                ))
    
    def validate_validation_schema(self, schema: Any, file: str, line: int) -> None:
        """Validate Yup validation schema array"""
        if not isinstance(schema, list):
            self.issues.append(ValidationIssue(
                severity='error',
                file=file,
                line=line,
                message="validationSchema must be an array",
                json_snippet=str(schema)[:100]
            ))
            return
            
        if len(schema) > 0:
            # First element should be type declaration
            first = schema[0]
            if not isinstance(first, list) or len(first) < 2:
                self.issues.append(ValidationIssue(
                    severity='warning',
                    file=file,
                    line=line,
                    message="First validation schema element should be type declaration [yup, type]",
                    json_snippet=str(first)[:100]
                ))
    
    def check_security_issues(self, obj: Dict, file: str, line: int) -> None:
        """Check for security vulnerabilities"""
        # Check for XSS in TemplatedString
        if obj.get('component-name') == 'TemplatedStringField':
            template = obj.get('component-parameters', {}).get('template', '')
            # Look for user input field references
            if '{{' in template:
                # This is a simplified check - would need field registry for full validation
                user_input_patterns = ['text', 'description', 'notes', 'comment', 'input']
                for pattern in user_input_patterns:
                    if pattern.lower() in template.lower():
                        self.issues.append(ValidationIssue(
                            severity='error',
                            file=file,
                            line=line,
                            message=f"SECURITY: Potential XSS - user input field in template: {template}",
                            json_snippet=json.dumps(obj)[:100]
                        ))
                        self.stats.security_issues += 1
                        break
                        
        # Check QRCodeFormField on web
        if obj.get('component-name') == 'QRCodeFormField':
            params = obj.get('component-parameters', {})
            if params.get('required'):
                self.issues.append(ValidationIssue(
                    severity='warning',
                    file=file,
                    line=line,
                    message="QRCodeFormField with required=true will block web platform",
                    json_snippet=json.dumps(obj)[:100]
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
                
            # Determine type and validate accordingly
            if self.is_field_definition(obj):
                self.validate_field_definition(obj, str(filepath), line_num)
            elif self.is_notebook_structure(obj):
                self.validate_notebook_structure(obj, str(filepath), line_num)
            else:
                # Could be a fragment or example
                # Check if it's a dict with fields inside
                for key, value in obj.items() if isinstance(obj, dict) else []:
                    if isinstance(value, dict) and self.is_field_definition(value):
                        self.validate_field_definition(value, str(filepath), line_num)
    
    def validate_directory(self, directory: Path) -> None:
        """Validate all markdown files in a directory"""
        for filepath in directory.glob('*.md'):
            self.process_file(filepath)
    
    def generate_report(self) -> str:
        """Generate validation report"""
        report = []
        report.append("# JSON Validation Report\n")
        report.append(f"Validated {self.stats.total_examples} JSON examples\n")
        
        # Summary
        report.append("## Summary\n")
        report.append(f"- Total examples: {self.stats.total_examples}")
        report.append(f"- Syntax valid: {self.stats.syntax_valid}/{self.stats.total_examples}")
        report.append(f"- Schema compliant: {self.stats.schema_compliant}/{self.stats.total_examples}")
        report.append(f"- Component valid: {self.stats.component_valid}/{self.stats.total_examples}")
        report.append(f"- Security issues: {self.stats.security_issues}\n")
        
        # Issues by severity
        errors = [i for i in self.issues if i.severity == 'error']
        warnings = [i for i in self.issues if i.severity == 'warning']
        info = [i for i in self.issues if i.severity == 'info']
        
        if errors:
            report.append(f"## Critical Issues ({len(errors)})\n")
            for issue in errors[:20]:  # Limit to first 20
                report.append(f"- **{issue.file}:{issue.line}** - {issue.message}")
            if len(errors) > 20:
                report.append(f"... and {len(errors) - 20} more errors\n")
                
        if warnings:
            report.append(f"\n## Warnings ({len(warnings)})\n")
            for issue in warnings[:20]:
                report.append(f"- **{issue.file}:{issue.line}** - {issue.message}")
            if len(warnings) > 20:
                report.append(f"... and {len(warnings) - 20} more warnings\n")
                
        # Statistics
        report.append("\n## Statistics\n")
        
        report.append("### Namespace Usage")
        for ns, count in sorted(self.stats.namespace_usage.items()):
            status = "✓" if ns in self.VALID_NAMESPACES and ns != 'faims3' else "⚠️"
            report.append(f"- {status} {ns}: {count}")
            
        report.append("\n### Top Components")
        for comp, count in sorted(self.stats.component_usage.items(), key=lambda x: x[1], reverse=True)[:10]:
            report.append(f"- {comp}: {count}")
            
        report.append("\n### Type Distribution")
        for type_val, count in sorted(self.stats.type_usage.items()):
            status = "✓" if type_val in self.VALID_TYPES else "✗"
            report.append(f"- {status} {type_val}: {count}")
            
        return '\n'.join(report)
    
    def generate_fix_script(self) -> str:
        """Generate Python script to fix common issues"""
        script = []
        script.append("#!/usr/bin/env python3")
        script.append('"""Auto-fix common JSON issues in documentation"""')
        script.append("import re")
        script.append("from pathlib import Path\n")
        
        script.append("def fix_namespace(content):")
        script.append("    # Update deprecated namespace")
        script.append('    return content.replace(\'"component-namespace": "faims3"\',')
        script.append('                          \'"component-namespace": "faims-custom"\')\n')
        
        script.append("def add_initial_values(content):")
        script.append("    # Add initialValue to required fields")
        script.append("    # This is complex and needs manual review")
        script.append("    return content\n")
        
        script.append("def fix_file(filepath):")
        script.append("    content = filepath.read_text()")
        script.append("    original = content")
        script.append("    content = fix_namespace(content)")
        script.append("    content = add_initial_values(content)")
        script.append("    if content != original:")
        script.append("        filepath.write_text(content)")
        script.append("        print(f'Fixed: {filepath}')\n")
        
        script.append("if __name__ == '__main__':")
        script.append("    for md_file in Path('.').rglob('*.md'):")
        script.append("        fix_file(md_file)")
        
        return '\n'.join(script)

def main():
    """Main execution"""
    validator = FieldmarkJSONValidator()
    
    # Process field-categories
    field_dir = Path('field-categories')
    if field_dir.exists():
        print(f"Processing {field_dir}...")
        validator.validate_directory(field_dir)
    
    # Process patterns
    patterns_dir = Path('patterns')
    if patterns_dir.exists():
        print(f"Processing {patterns_dir}...")
        validator.validate_directory(patterns_dir)
    
    # Generate and save report
    report = validator.generate_report()
    report_file = Path('validation_report.md')
    report_file.write_text(report)
    print(f"\nValidation report saved to {report_file}")
    
    # Generate fix script if issues found
    if validator.issues:
        fix_script = validator.generate_fix_script()
        fix_file = Path('fix_json.py')
        fix_file.write_text(fix_script)
        print(f"Fix script saved to {fix_file}")
    
    # Print summary
    print(f"\nSummary:")
    print(f"  Total examples: {validator.stats.total_examples}")
    print(f"  Errors: {len([i for i in validator.issues if i.severity == 'error'])}")
    print(f"  Warnings: {len([i for i in validator.issues if i.severity == 'warning'])}")
    print(f"  Security issues: {validator.stats.security_issues}")
    
    # Exit with error if critical issues
    if any(i.severity == 'error' for i in validator.issues):
        sys.exit(1)
    
if __name__ == '__main__':
    main()