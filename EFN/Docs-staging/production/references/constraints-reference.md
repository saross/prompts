# Constraints Reference
## Designer Limitations and Security Considerations for Fieldmark v3

### Overview

This reference consolidates critical constraints that affect Fieldmark v3 deployment:
- Designer interface limitations that impact development workflow
- Security vulnerabilities and protection requirements
- Testing and validation constraints
- Compliance and data protection considerations

Understanding these constraints is essential for successful and secure notebook deployment.

---

## Part 1: Designer Interface Limitations

### Testing & Preview Constraints

#### Limited Designer Preview
- **Field appearance**: No preview of how fields will render on different platforms
- **Conditional logic**: Conditions must be tested in deployed notebooks, not Designer preview
- **Validation behavior**: Cannot verify validation schemas work as intended
- **Mobile usability**: No way to test touch interactions or mobile-specific behaviors
- **Export formats**: Cannot preview CSV/JSON export behavior with sample data

#### Effective Testing Workflow
While the Designer lacks built-in preview, a practical workflow exists:
1. Keep Designer open in one browser tab
2. Keep web application open in another tab for testing
3. Make changes in Designer and deploy
4. Test immediately in web app (updates are rapid)
5. Iterate quickly between tabs

This dual-tab workflow provides near-real-time testing capability, though it requires deployment to see changes rather than in-Designer preview.

### Validation Customization Constraints

#### Error Message Limitations
- **Cannot customize validation messages**: Stuck with Yup validation library defaults
  - Example: "This field is required" cannot be changed to "Please enter specimen ID"
  - Example: Email validation shows generic "Invalid email" rather than context-specific message
- **Cannot control error display positioning**: Errors always appear below fields
- **Cannot style error messages**: Red text styling is fixed
- **Cannot create contextual help**: Errors cannot reference other field values

#### Cross-Field Validation
Designer cannot create validation rules that reference multiple fields:
- Password confirmation matching
- Date range validation (start date before end date)
- Conditional required fields based on other field values
- Sum validation across numeric fields
- Duplicate checking across array fields

These require JSON editing with custom Yup schemas.

### Performance & Warning Gaps

#### No Performance Indicators
Designer provides no warnings when configurations will cause issues:
- **Option count limits**: No warning when Select/RadioGroup exceeds 20 options (may cause lag with markdown processing)*
- **Character limits**: No indication when text fields approach performance thresholds*
- **Memory usage**: No warnings about large file uploads or image captures
- **Render complexity**: No indication when forms become too complex for mobile devices (~100 fields recommended limit)*

*Note: All performance thresholds are estimated/extrapolated from code analysis and represent approximate guidelines only. Real-world feedback is welcomed to improve accuracy of these thresholds.

#### Missing Accessibility Warnings
- No WCAG compliance indicators
- No color contrast warnings
- No touch target size validation (44×44px minimum)
- No screen reader compatibility checks
- No keyboard navigation testing

#### Platform-Specific Issues Not Flagged
- QRCodeFormField required on web (will block form submission)
- Browser-specific validation conflicts
- Mobile keyboard behavior issues

### Field Management Restrictions

#### Type Conversion Limitations
- **Cannot convert between field types in Designer**: Must delete and recreate in Designer interface
  - Example: Cannot change RadioGroup to Select in Designer
  - Example: Cannot convert TextField to MultipleTextField in Designer
  - JSON editing may allow type changes but requires careful data migration
  - Some conversions (e.g., TextField to MultipleTextField) may preserve data
  - Always backup data before attempting field type changes

#### Bulk Operations Not Supported
- Cannot edit multiple fields simultaneously
- Cannot copy validation rules between fields
- Cannot apply consistent styling across field groups
- Cannot search and replace across field labels/helpers

#### Configuration Constraints
- **Character limits**: Cannot enforce maximum character counts
- **Input patterns**: Cannot restrict input format (phone numbers, postal codes)
- **Input masks**: Cannot create formatted input (credit cards, dates)
- **Auto-formatting**: Cannot enable automatic formatting as user types

### Advanced Features Requiring JSON

Despite Designer improvements, some features still require JSON editing:

#### Complex Hierarchies
While AdvancedSelect provides a JSON editor window, complex hierarchies still require careful manual construction:
- Multi-level taxonomies
- Conditional branches in hierarchies
- Large option trees (>100 nodes)

#### Component Parameters
Many component-specific parameters are not exposed in Designer:
- Platform-specific configurations
- Advanced Material-UI properties
- Custom CSS classes
- Performance optimizations

#### Meta Properties
While basic meta properties are available, advanced configurations require JSON:
- Custom annotation labels
- Conditional meta property display
- Meta property validation rules

### Workaround Strategies

#### For Testing Limitations
1. Maintain a staging deployment for rapid testing
2. Use device emulators for basic mobile testing
3. Create test notebooks with all field types
4. Document test cases for manual verification

#### For Validation Constraints
1. Use helper text to clarify requirements
2. Document validation rules in field labels
3. Create separate documentation for complex validation
4. Train users on expected formats

#### For Performance Issues
1. Monitor browser console during testing
2. Test with maximum expected data volumes
3. Document performance thresholds
4. Plan for progressive form complexity

### Impact on Development Workflow

These limitations affect different user groups:

**Notebook Designers**: Must plan for multiple deployment cycles and maintain external documentation for complex requirements.

**Developers**: Need to switch between Designer and JSON editing, maintaining synchronization between visual and code representations.

**End Users**: May encounter generic error messages and validation behaviors that don't match their domain expectations.

---

## Part 2: Security Constraints and Vulnerabilities

### Critical Security Vulnerabilities

#### XSS (Cross-Site Scripting) Risks

**Most Critical Vulnerability - TemplatedString Fields**:
- **Issue**: HTML escaping is DISABLED in TemplatedString fields (formUtilities.ts line 27)
- **Risk Level**: CRITICAL
- **Attack Vector**: User input in templates executes as HTML/JavaScript
- **Impact**: Complete session hijacking, data theft, form manipulation

**Example Attack**:
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
- **Recommendation**: Implement server-side length limits and pattern validation

#### TemplatedString Fields
- **CRITICAL**: HTML escaping disabled
- Template injection possible through field references
- No recursive reference protection
- **Recommendation**: Whitelist allowed template variables

#### RichText Fields
- DOMPurify sanitization at runtime
- External images blocked (hardcoded empty array)
- Script tags stripped but other vectors possible
- Tables removed despite Designer support
- **Recommendation**: Never include user content in RichText

#### QRCodeFormField
- No validation of scanned content
- Accepts any barcode format
- Raw data stored without sanitization
- **Recommendation**: Validate expected format server-side

#### Address Fields
- Complex JSON structure allows nested attacks
- Race conditions can corrupt data
- No format validation
- **Recommendation**: Implement JSON schema validation

#### Number Fields
- JavaScript precision limits can cause data corruption
- No server-side range validation
- Scientific notation can bypass validations (e.g., `1e308` causes infinity overflow)
- **BasicAutoIncrementer enumeration risk**: Sequential IDs expose data patterns, enable scraping
- **Integer vs Float confusion**: All numbers stored as floats, causing rounding errors
- **Type coercion attacks**: JavaScript coercion bypasses validation (`"10" + 0`, `true + 1`)
- **Recommendation**: Validate numeric ranges server-side, use UUIDs for sensitive IDs

#### DateTime Fields
- Future dates accepted (backdating possible)
- No temporal sequence validation (start/end date logic not enforced)
- Timezone information leaks user location (reveals geographic position, travel patterns)
- Format string injection possible (malformed dates stored as strings)
- **DateTimePicker timezone loss**: Silent data corruption, 10+ hour shifts possible
- **Audit trail note**: User-editable datetime fields are for data collection, not forensics. PouchDB maintains revision history (_rev) and server typically adds trusted timestamps during sync for true audit trails.
- **Recommendation**: Use DateTimeNow for timezone-critical data, rely on server timestamps for audit trails

#### Selection Fields
- Option values not validated for special characters
- Markdown in options can introduce vectors (JavaScript URLs in RadioGroup)
- No uniqueness validation on values
- **CSV Formula Injection**: Excel executes formulas in exported data (`=SUM(A1:A100)`, `=cmd|'/c calc'!A1`)
- **Option validation bypass (LOW RISK)**: While the UI prevents invalid selections, client could theoretically submit values not in option list via browser DevTools or API manipulation. Defense-in-depth principle suggests server-side validation.
- **AdvancedSelect path traversal**: Delimiter injection with " > " corrupts hierarchy
- **Conditional logic bypass**: Browser DevTools can enable disabled fields
- **Recommendation**: Server should validate all selections against option lists as best practice, prefix CSV exports with `'`

#### Location Fields
- **GPS precision (PRIVACY CONSIDERATION)**: Full coordinates stored for research accuracy. Consider obfuscation options for public dataset releases.
- **No coordinate validation**: Self-intersecting polygons accepted
- **CSV export**: Maintains full precision (intentional for research)
- **Recommendation**: Implement privacy controls for public data sharing, validate geometries server-side

#### Media Fields  
- **File type validation**: Accepts any file type including executables (research may require various formats)
- **EXIF data (FEATURE)**: Location metadata preserved intentionally for research purposes. Users should be aware when sharing publicly.
- **Base64 encoding**: Increases storage by ~33%
- **Orphaned attachments**: No automatic cleanup
- **Recommendation**: Implement virus scanning for public deployments, educate users about EXIF privacy

#### Relationship Fields
- **Access control**: Operates at notebook level, not field level. Users with edit permissions can modify all relationships; read-only users cannot.
- **No granular permissions**: Cannot restrict relationship editing while allowing other field edits
- **Orphan creation**: Deleting parent records leaves child relationships
- **No cascade delete**: Manual cleanup required
- **Recommendation**: Suitable for trusted research teams; implement cleanup procedures for orphans

#### Display Fields
- **DOMPurify configuration**: Hardcoded whitelist cannot be customized
- **External resources**: All external domains blocked
- **Base64 images**: Potential vector if user-supplied
- **Recommendation**: Use for trusted content only

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

---

## Security Incident Response

### If XSS is Discovered
1. Immediately disable affected templates
2. Audit all TemplatedString configurations
3. Review server logs for exploitation
4. Reset all user sessions
5. Implement content security policy headers

### If Injection is Suspected
1. Review server logs for unusual patterns
2. Audit database for unauthorized changes
3. Validate all recent data entries
4. Implement additional validation
5. Consider security audit

---

## Compliance Considerations

### GDPR/Privacy
- Right to deletion not automatically supported
- No automatic PII detection
- Export includes all user data
- No consent management

### Security Standards
- No automatic OWASP compliance checking
- Limited security headers by default
- No built-in penetration testing
- Manual security review required

---

## Pre-Deployment Security Checklist

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

---

## Designer Best Practices

1. **Start Simple**: Build basic structure in Designer, enhance with JSON
2. **Test Early**: Deploy frequently to catch issues before complex dependencies develop
3. **Document Thoroughly**: Maintain external documentation for validation rules and conditional logic
4. **Plan Iterations**: Budget time for the deploy-test-refine cycle
5. **Use Templates**: Create reusable patterns for common configurations

---

## Reporting Security Issues

If you discover a security vulnerability:
1. Do NOT publish details publicly
2. Contact the Fieldmark security team immediately
3. Provide detailed reproduction steps
4. Allow time for patching before disclosure
5. Follow responsible disclosure practices

---

## Summary of Critical Constraints

### Designer Limitations
- No pre-deployment testing capability
- Cannot customize validation messages
- No performance warnings or indicators
- Cannot convert between field types
- Many features require JSON editing

### Security Vulnerabilities
- **CRITICAL**: TemplatedString XSS vulnerability
- No server-side validation by default
- No input sanitization at field level
- Session tokens vulnerable to XSS
- No field-level encryption

### Compliance Gaps
- No automatic GDPR compliance
- No PII detection or protection
- No audit trails by default
- Export includes all data

### Performance Constraints
- ~100 field recommended limit
- 20+ options cause markdown lag
- No memory usage warnings
- Platform-specific issues not flagged

---

## Metadata
- **Document Version**: 1.0
- **Last Updated**: 2025-01-06
- **Applies to**: Fieldmark v3 (all versions), Designer (current web interface)
- **Purpose**: Consolidate constraints affecting Fieldmark deployment and security
- **Sources**: Unified from designer-limitations and security-considerations references