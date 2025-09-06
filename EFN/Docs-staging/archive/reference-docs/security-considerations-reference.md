# Security Considerations Reference

> **⚠️ DEPRECATED**: This document has been superseded by the consolidated [Constraints Reference](../../reference/constraints-reference.md). This archived version is maintained for reference only.

## Universal Security Guidelines for Fieldmark v3

### Overview

This document consolidates security considerations for all Fieldmark v3 field types. Security in Fieldmark operates on multiple levels: client-side validation (easily bypassed), server-side validation (essential), and data sanitization (critical for preventing attacks). Understanding these layers is essential for deploying secure notebooks.

### Critical Security Vulnerabilities

#### XSS (Cross-Site Scripting) Risks

**Most Critical Vulnerability - TemplatedString Fields**:
- **Issue**: HTML escaping is DISABLED in TemplatedString fields (formUtilities.ts line 27)
- **Risk Level**: CRITICAL
- **Attack Vector**: User input in templates executes as HTML/JavaScript
- **Impact**: Complete session hijacking, data theft, form manipulation
- **Example Attack**:
  ```json
  // Template configuration:
  { "template": "Record: {{user_text_field}}" }
  
  // If user enters in text field:
  <script>alert('XSS')</script>
  
  // Result: Script EXECUTES when template renders
  ```

**Mitigation Requirements**:
1. NEVER include user-input text fields in TemplatedString templates
2. Only use controlled vocabularies (Select, RadioGroup) in templates
3. Use static values or system-generated fields only
4. If user input is essential, implement server-side sanitization

**Safe Pattern**:
```json
{
  "template": "{{site_type}}-{{counter}}-{{date}}",
  // Where:
  // site_type = Select field with predefined options
  // counter = BasicAutoIncrementer
  // date = DatePicker (system controlled)
}
```

**Unsafe Patterns to Avoid**:
```json
// ALL OF THESE CREATE XSS VULNERABILITIES:
{ "template": "Site: {{site_name}}" }      // If site_name is TextField
{ "template": "Notes: {{description}}" }    // If description is MultipleTextField
{ "template": "ID: {{custom_id}}" }         // If custom_id allows user input
{ "template": "{{any_user_editable_field}}" } // ANY user-editable field
```

#### SQL Injection Prevention

**Risk Areas**:
- All text input fields (TextField, MultipleTextField, Email, Address)
- QRCode scanner input
- Imported data from CSV/JSON

**Current State**:
- NO input sanitization at field level
- NO parameterized queries enforced
- Backend validation responsibility

**Required Protections**:
1. Implement parameterized queries in all backend operations
2. Never concatenate user input into SQL strings
3. Validate data types before database operations
4. Use prepared statements for all queries
5. Implement stored procedures where appropriate

#### JSON Injection Risks

**Affected Fields**:
- Address fields (store complex JSON)
- Any field with JSON storage

**Attack Vectors**:
```javascript
// Malicious input in Address field:
{
  "line1": "123 Main\"};alert('XSS');//",
  "city": "Sydney",
  "__proto__": {"isAdmin": true}  // Prototype pollution
}
```

**Protections**:
1. Validate JSON structure before storage
2. Use JSON schema validation
3. Sanitize all string values within JSON
4. Never use eval() or Function() with JSON data

### Field-Specific Security Considerations

#### Text Fields (TextField, MultipleTextField)
- No character limit enforcement at database level
- No input pattern validation beyond client-side
- HTML special characters stored raw
- Recommendation: Implement server-side length limits and pattern validation

#### TemplatedString Fields
- **CRITICAL**: HTML escaping disabled
- Template injection possible through field references
- No recursive reference protection
- Recommendation: Whitelist allowed template variables

#### RichText Fields
- DOMPurify sanitization at runtime
- External images blocked (hardcoded empty array)
- Script tags stripped but other vectors possible
- Tables removed despite Designer support
- Recommendation: Never include user content in RichText

#### QRCodeFormField
- No validation of scanned content
- Accepts any barcode format
- Raw data stored without sanitization
- Recommendation: Validate expected format server-side

#### Address Fields
- Complex JSON structure allows nested attacks
- Race conditions can corrupt data
- No format validation
- Recommendation: Implement JSON schema validation

#### Number Fields
- JavaScript precision limits can cause data corruption
- No server-side range validation
- Scientific notation can bypass validations
- Recommendation: Validate numeric ranges server-side

#### DateTime Fields
- Future dates accepted (backdating possible)
- No temporal sequence validation
- Timezone information leaks user location
- Format string injection possible
- Recommendation: Implement audit trails server-side

#### Selection Fields
- Option values not validated for special characters
- Markdown in options can introduce vectors
- No uniqueness validation on values
- Recommendation: Sanitize option values before storage

### Data Validation Layers

#### Client-Side (Weak)
- Yup validation schemas
- HTML5 input validation
- JavaScript validation logic
- **Easily bypassed** using browser developer tools
- Should be considered UX enhancement only

#### Server-Side (Essential)
- Must duplicate ALL client-side validation
- Implement additional security checks
- Type validation before database operations
- Range and format enforcement
- Rate limiting for rapid submissions

#### Database Level (Critical)
- Constraints on field lengths
- Data type enforcement
- Foreign key relationships
- Stored procedure validation
- Trigger-based audit trails

### Security Best Practices

#### Input Handling
1. **Never trust client data** - Validate everything server-side
2. **Whitelist over blacklist** - Define allowed patterns explicitly
3. **Fail securely** - Reject suspicious input rather than attempting to clean
4. **Log security events** - Track validation failures for analysis
5. **Rate limit** - Prevent rapid submission attacks

#### Template Security
1. **No user input in templates** - Only system-controlled fields
2. **Validate template syntax** - Prevent template injection
3. **Limit template complexity** - Avoid nested conditionals
4. **Audit template changes** - Track who modifies templates
5. **Test with malicious input** - Include security testing in QA

#### Testing for Security

**Test with these malicious inputs**:
```javascript
// XSS attempts
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
javascript:alert('XSS')
<svg onload=alert('XSS')>

// SQL injection attempts
'; DROP TABLE records; --
' OR '1'='1
admin'--
' UNION SELECT * FROM users--

// Template injection
{{constructor.constructor('alert(1)')()}}
${alert('XSS')}
{{__proto__.isAdmin = true}}

// JSON injection
{"__proto__": {"isAdmin": true}}
{"line1": "test\"};alert('x');//"}
```

### Authentication & Authorization

#### Current Limitations
- No field-level permissions
- No encryption at rest for sensitive fields
- No audit trail for data changes
- Session tokens in local storage (XSS accessible)

#### Recommendations
1. Implement field-level encryption for sensitive data
2. Add audit logging for all data modifications
3. Use httpOnly cookies for session management
4. Implement role-based field access
5. Add data classification levels

### Data Protection

#### Sensitive Data Handling
- PII (Personally Identifiable Information) stored in plain text
- No automatic data masking
- Export functions include all field data
- No redaction capabilities

#### Recommended Protections
1. Identify sensitive fields during design
2. Implement encryption for sensitive data
3. Add data masking for display
4. Control export permissions
5. Implement data retention policies

### Security Incident Response

#### If XSS is Discovered
1. Immediately disable affected templates
2. Audit all TemplatedString configurations
3. Review server logs for exploitation
4. Reset all user sessions
5. Implement content security policy headers

#### If Injection is Suspected
1. Review server logs for unusual patterns
2. Audit database for unauthorized changes
3. Validate all recent data entries
4. Implement additional validation
5. Consider security audit

### Compliance Considerations

#### GDPR/Privacy
- Right to deletion not automatically supported
- No automatic PII detection
- Export includes all user data
- No consent management

#### Security Standards
- No automatic OWASP compliance checking
- Limited security headers by default
- No built-in penetration testing
- Manual security review required

### Security Checklist

Before deploying any notebook:
- [ ] No user text fields in TemplatedString templates
- [ ] Server-side validation implemented for all fields
- [ ] SQL queries use parameterized statements
- [ ] JSON structures validated before storage
- [ ] Rate limiting configured
- [ ] Security headers implemented
- [ ] Audit logging enabled
- [ ] Sensitive data identified and protected
- [ ] Export permissions configured
- [ ] Security testing completed

### Reporting Security Issues

If you discover a security vulnerability:
1. Do NOT publish details publicly
2. Contact the Fieldmark security team immediately
3. Provide detailed reproduction steps
4. Allow time for patching before disclosure
5. Follow responsible disclosure practices

### Related Documentation
- Individual field documentation for field-specific security notes
- Designer Limitations Reference for configuration constraints
- Validation Timing Reference for validation behavior
- Performance Thresholds Reference for DoS prevention

### Version
Last updated: 2025-09-03
Applies to: Fieldmark v3 (all versions)
Security review: Required before production deployment