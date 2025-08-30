# Text Input Fields

## Overview {essential}

The Fieldmark ecosystem provides seven text-related field types for comprehensive data capture and display needs:

### DESIGNER QUICK GUIDE
When using the Designer interface:
- 📝 **Single-line text**: Choose **"FAIMS Text Field"**
- 📄 **Multi-line text**: Choose **"Text Field"**
- ✉️ **Email input**: Choose **"Email"**

### CRITICAL NAMING DISAMBIGUATION
⚠️ **Designer UI names differ from component names**:
- **"FAIMS Text Field"** in Designer = single-line text (component: FAIMSTextField)
- **"Text Field"** in Designer = multi-line text area (component: MultipleTextField)
- **"Email"** in Designer = single-line with validation (component: TextField with email config)

Note: TextField (formik-material-ui) is the base component but is not directly selectable in Designer for plain text input.

This naming inconsistency is a known issue that creates significant confusion. Always verify the component-name in JSON when troubleshooting.

### Data Capture Fields (1-6)

1. **FAIMSTextField** (appears as "FAIMS Text Field" in Designer) - Single-line text input for brief, unconstrained textual data (50 character recommendation). Implemented through the `faims-custom/FAIMSTextField` component with enhanced advanced help capabilities.

2. **MultipleTextField** (appears as "Text Field" in Designer) - Extended text entry for narrative content and detailed observations (10,000 character recommendation). Maintains fixed-height presentation with internal scrolling mechanisms. Despite both using FormikTextField internally, MultipleTextField is configured with `multiline: true` and `rows: 4` parameters.

3. **TextField** (used by "Email" in Designer) - Base single-line component, primarily used with email configuration. When "Email" is selected in Designer, it creates a TextField component with `InputProps: {type: 'email'}` configuration. Not directly accessible through Designer for general text input.

4. **TemplatedString** - Auto-generated text from Mustache templates, critical for Human-Readable Identifiers (HRIDs). **⚠️ CRITICAL REQUIREMENT**: Every notebook MUST include at least one TemplatedString field configured as the `hridField`. Without HRIDs, records display only as cryptic UUIDs (e.g., `a7f3b2c1-d4e5-6789-0abc`), making field data management impossible. **⚠️ SECURITY WARNING**: TemplatedString has HTML escaping DISABLED (formUtilities.ts line 27), creating XSS vulnerabilities if user input is included in templates without sanitization.

5. **Address Field** - Provides structured address capture through a specialised interface storing data in GeocodeJSON-compliant format, facilitating both human-readable display and future geocoding integration. **Beta feature** implementing dual storage – maintaining both structured components and concatenated display strings within a JSON object. Currently optimised for Australian address formats with technical users comfortable with JSON data extraction.

6. **QRCodeFormField** - Delivers **mobile-exclusive** barcode scanning functionality through ML Kit barcode scanning, supporting thirteen distinct barcode formats despite its nomenclature suggesting QR-only capability. Uses sophisticated ten-scan validation mechanism ensuring reading accuracy whilst operating without user feedback. **⚠️ PLATFORM WARNING**: Web platform deployment renders the component entirely non-functional, displaying a disabled interface that critically breaks form validation when marked as required.

### Display Field (7)

7. **RichText Field** - Provides formatted instructional content and headings within forms through markdown rendering. Purely presentational—displays static content without capturing or storing user input. Exists within field architecture for consistency but does not participate in form validation, data storage, or export operations. Content rendered through markdown-it parser with aggressive DOMPurify sanitization. **⚠️ MEMORY WARNING**: Critical limitations include memory leaks on mobile devices, no accessibility implementation, and feature discrepancies between Designer editing and runtime display.

### Component Status Summary
- TextField, MultipleTextField, TemplatedString: Stable, production ready
- Email: Stable (TextField configuration variant)
- Address: Beta Feature
- QRCodeFormField: Mobile-only
- RichText: Display-only (no data capture)

---

## Field Selection Guide {essential}

### Quick Decision Tree

What type of text data do you need?
│
├─ Display-only content?
│  └─ YES → RichText
│
├─ Auto-generated identifier or derived value?
│  └─ YES → TemplatedString
│     └─ Configure as hridField for record identification
│
├─ Barcode/QR code scanning?
│  └─ YES → QRCodeFormField (mobile only)
│     └─ Pair with TextField for web fallback
│
├─ Structured data capture?
│  ├─ Email address?
│  │  └─ YES → Email (TextField with type="email")
│  │
│  └─ Street address?
│     └─ YES → Address (JSON storage)
│
└─ User-entered text?
   ├─ Brief content (<50 characters)?
   │  └─ YES → TextField
   │     └─ Consider FAIMSTextField variant if rich help needed
   │
   └─ Extended content (>50 characters)?
      └─ YES → MultilineText
         └─ Configure rows based on expected content

### Quick Decision Matrix

| Field Type | Storage | Max Length | Use When | Avoid When |
|------------|---------|------------|----------|------------|
| **TextField** | String | ~200 chars (recommended) | Names, codes, identifiers | Long narratives |
| **MultilineText** | String | 10,000 chars* | Descriptions, notes, observations | Single identifiers |
| **TemplatedString** | String | Auto-generated | HRIDs, derived identifiers | User input needed |
| **Email** | String | Email format | Contact information | Non-email data |
| **Address** | JSON | Complex object | Structured addresses | Simple text sufficient |
| **QRCodeFormField** | String | Scanned value | Mobile barcode capture | Web platform |
| **RichText** | None | Display only | Instructions, headers | Data capture |

*See [Common Characteristics > Performance Boundaries] for performance implications beyond 10,000 characters

### Selection Strategy

1. **Default to TextField** for most text input unless specific reasons exist
2. **Use MultilineText** only when narratives exceed single line  
3. **Deploy TemplatedString** as hridField (mandatory for every notebook)
4. **Consider structured fields** (Email, Address) only when structure adds value
5. **Avoid QRCodeFormField** unless mobile-only deployment confirmed
6. **Reserve RichText** for static instructions only (no data capture)

---

## Designer Usage Guide {essential}

### What to Select in Designer

When using the Designer interface, follow these simple rules:

📝 **For single-line text input**: Select **"FAIMS Text Field"**
- Use for: identifiers, names, brief labels, codes
- Creates: FAIMSTextField component
- Helper text in Designer: "Single-line text input for free-form entries"

📄 **For multi-line text input**: Select **"Text Field"**  
- Use for: descriptions, notes, observations, narratives
- Creates: MultipleTextField component
- Helper text in Designer: "Multi-line text area for longer notes"

✉️ **For email addresses**: Select **"Email"**
- Use for: validated email input
- Creates: TextField component with email configuration
- Includes automatic email validation

---

## Designer Component Mapping {essential}

### Designer UI vs JSON Component Names

| Designer UI Label | JSON component-name | Component Namespace | Description |
|------------------|--------------------|--------------------|-------------|
| FAIMS Text Field | FAIMSTextField | faims-custom | Enhanced single-line with advanced help |
| Text Field | MultipleTextField | formik-material-ui | Multi-line text area |
| Email | TextField | formik-material-ui | Single-line with email validation |
| Templated String Field | TemplatedStringField | faims-custom | Auto-generated text |
| Scan QR Code | QRCodeFormField | qrcode | Mobile-only scanner |
| Address | AddressField | faims-custom | Structured address input |

⚠️ **Critical Notes**:
- There is NO Designer element that creates a plain TextField without configuration
- "FAIMS Text Field" creates FAIMSTextField (not TextField)
- "Text Field" creates MultipleTextField (not MultilineText)
- Only "Email" uses the base TextField component

This mapping table is essential for:
- Debugging field behaviour issues (see [Troubleshooting Guide > Critical Issues Table])
- Writing JSON configurations manually
- Understanding error messages that reference component names
- Migrating between Designer versions

---

## Component Selection Decision Tree {important}

### Which Component Should You Use?

```
Need text input?
├─ Single line?
│  ├─ Email validation needed?
│  │  └─ Use: Email field → TextField (formik-material-ui) with email config
│  └─ General text?
│     └─ Use: FAIMS Text Field → FAIMSTextField (faims-custom)
└─ Multiple lines?
   └─ Use: Text Field → MultipleTextField (formik-material-ui)
```

### Manual JSON Configuration

If writing JSON directly (not using Designer):
- **Single-line with advanced help**: FAIMSTextField (faims-custom)
- **Single-line basic**: TextField (formik-material-ui) - but not available in Designer
- **Multi-line**: MultipleTextField (formik-material-ui) with multiline:true
- **Email**: TextField (formik-material-ui) with email InputProps

⚠️ **TextField Component Access Warning**: 
The base TextField component (formik-material-ui) cannot be created directly through Designer. 
It's only used internally by the Email field. For general single-line text, always use 
FAIMSTextField via "FAIMS Text Field" in Designer. If you encounter a plain TextField in 
existing JSON, it likely needs migration to FAIMSTextField.

---

## Component Namespace Errors {important}

### Troubleshooting "Component not found" Errors

If you see "Component not found" or similar errors, verify the namespace matches the component:

| Component | Required Namespace | Common Error |
|-----------|-------------------|--------------|
| FAIMSTextField | faims-custom | Using formik-material-ui causes failure |
| MultipleTextField | formik-material-ui | Using faims-custom causes failure |
| TextField | formik-material-ui | Only works with Email configuration |
| TemplatedStringField | faims-custom | Using formik-material-ui causes failure |
| QRCodeFormField | qrcode | Using faims-custom causes failure |
| AddressField | faims-custom | Using formik-material-ui causes failure |

**Quick Fix Pattern**:
```json
// ❌ Wrong namespace
{
  "component-namespace": "formik-material-ui",
  "component-name": "FAIMSTextField"  // Will fail!
}

// ✅ Correct namespace
{
  "component-namespace": "faims-custom",
  "component-name": "FAIMSTextField"  // Works!
}
```

### Technical Implementation Note

Both TextField and MultipleTextField components in the formik-material-ui namespace use the same underlying FormikTextField component from the formik-mui library. The difference lies in their configuration parameters:
- **TextField**: Standard single-line configuration
- **MultipleTextField**: Includes `multiline: true` and `rows` parameters

This explains why both components share similar behavior but present differently in the interface.

---

## Common Characteristics

### Security Considerations {important}

#### Input Sanitization {important}
**All text input fields (TextField, MultipleTextField, TemplatedString, Email, Address, QRCodeFormField)**:
- No input sanitisation by default
- XSS prevention relies entirely on display layer
- SQL injection prevention requires backend validation

#### Field-Specific Security Issues {important}
- **TemplatedString CRITICAL**: HTML escaping disabled (formUtilities.ts line 27), creating injection risk
- **QRCodeFormField**: No validation of scanned content
- **RichText**: Aggressive DOMPurify sanitization at runtime, external images blocked (hardcoded empty array)

**Recommendation**: Consider field-level encryption for sensitive data

#### Security Best Practices {comprehensive}

For TemplatedString templates with user input:
```javascript
1. Validate against allowed pattern
2. Strip HTML/JavaScript characters
3. Use controlled vocabularies where possible
4. Never include free-text fields in templates
5. Test with malicious input:
   - <script>alert('XSS')</script>
   - '; DROP TABLE records; --
   - ${evil.code}
```

### Performance Boundaries {important}

| Field Type | Recommended Limit | Enforced Limit | Impact Beyond Limit |
|------------|-------------------|------------|-------------------|
| TextField | 50 characters | None | Mobile viewport issues |
| MultilineText | 10,000 characters | ~1MB | Performance degradation |
| TemplatedString | 50 variables | None tested | Form responsiveness |
| Email | 254 characters (RFC) | None enforced | Compatibility issues |
| Address | No limits | None | JSON payload size increase |
| QRCodeFormField | Raw barcode length | Device memory | Scan may fail |
| RichText | 50 words per field | 1000 total words | Performance degradation, mobile crashes |

#### Form Design Guidelines {important}
- Maximum 30 text fields per section
- Maximum 3 TemplatedString fields per form
- Maximum 10 RichText fields per notebook
- Use conditional logic to hide unused fields
- Paginate forms with >50 total fields
- Monitor sync payload with large text content

#### Content Limits by Context {comprehensive}
| Context | TextField | MultilineText | TemplatedString | RichText |
|---------|-----------|---------------|-----------------|----------|
| Mobile Form | 30 chars | 2,000 chars | 2-3 components | 50 words |
| Desktop Form | 50 chars | 10,000 chars | 3-4 components | 50 words |
| Paper Label | 15 chars | N/A | 2 components | N/A |
| Export | 254 chars* | No limit | As generated | Never exported |

*Shapefile DBF limitation

### Common Validation Patterns {important}

#### Standard Validation Rules {important}
| Rule | Schema | Purpose | Fields |
|------|--------|---------|--------|
| required | `["yup.required", "Field required"]` | Mandatory content | TextField, MultipleTextField, TemplatedString, Email, Address |
| min length | `["yup.min", N, "Minimum N characters"]` | Enforce minimum | TextField, MultipleTextField |
| max length | `["yup.max", N, "Maximum N characters"]` | Prevent excess | TextField, MultipleTextField |
| pattern | `["yup.matches", "regex", "message"]` | Format enforcement | TextField, MultipleTextField, TemplatedString |
| email | `["yup.email", "Invalid email"]` | Email validation | TextField with type="email", Email field |
| object | `["yup.object"]` | JSON structure | Address field |

#### Validation Behavior {important}
**Touch-Based Validation (TextField, MultipleTextField, TemplatedString, Email, Address)**:
- Errors display only after field is "touched" (focused then blurred)
- Required validation prevents form submission
- Pattern validation occurs on every value change
- Field must gain focus then blur to show errors

**TemplatedString Specific**:
- Validates output, not template syntax
- Silent failure for invalid templates

**No User Validation (QRCodeFormField, RichText)**:
- QRCodeFormField: 10-scan hardware validation only, no user feedback
- RichText: Display-only, never validates

### Platform Behaviors {important}

#### Cross-Platform Consistency {important}
- **TextField, MultipleTextField, TemplatedString**: Behave identically across iOS, Android, and web
- **Touch targets**: Maintain 44×44px minimum (WCAG compliance) except Address edit button
- **Font size**: Minimum 16px prevents iOS zoom on focus
- **Tab navigation**: Follows DOM order
- **TemplatedString**: Evaluation identical on all platforms
- **QRCodeFormField**: Mobile-only, completely non-functional on web
- **RichText**: Stable on desktop, memory issues on mobile

#### iOS Behaviors {comprehensive}
| Field | Keyboard | Auto-correction | Special Features |
|-------|----------|-----------------|------------------|
| TextField/MultilineText/TemplatedString | Standard text | Active, predictive text | Long-press selection, may cover fields |
| Email | Email-optimised, @ key prominent | Disabled | Domain shortcuts (.com, .org, .net) |
| Address | Standard text | Active on all fields | Applies to state abbreviations |
| QRCodeFormField | N/A | N/A | Full-screen ML Kit camera |
| RichText | N/A | N/A | Memory leak with 10+ fields |

#### Android Behaviors {comprehensive}
| Field | Keyboard | Voice Input | Performance Notes |
|-------|----------|-------------|-------------------|
| TextField/MultilineText/TemplatedString | Standard text | Extended dictation, gesture typing | Voice may create run-on text |
| Email | Email layout, @ symbol | Available, struggles with @ | Space bar often hidden |
| Address | Text keyboard | Standard | Validation lag on older devices |
| QRCodeFormField | N/A | N/A | Full-screen scanner |
| RichText | N/A | N/A | Slower parsing than iOS |

#### Web/Desktop Behaviors {important}
- **Full functionality**: TextField, MultipleTextField, TemplatedString
- **Email**: Browser may display envelope icon, native validation supplements Yup
- **Address**: Full keyboard navigation in expanded state
- **QRCodeFormField**: Completely non-functional, shows disabled interface
- **RichText**: Stable rendering, minimal performance impact

### Shared Limitations {important}

#### Designer Interface Constraints {important}
- Cannot switch component variants via GUI (TextField variants)
- Advanced features require JSON editing
- No visual preview of validation behaviour
- Pattern validation requires manual regex entry
- Template syntax not validated (TemplatedString)
- Row count requires numeric input (MultilineText)
- MDX Editor accepts invalid markdown without warning (RichText)
- Table Editor available but tables removed at runtime (RichText)

#### Export Behavior {important}

| Field | CSV Export | JSON Export | Special Handling |
|-------|------------|-------------|------------------|
| TextField | Plain text string | String value | Quoted if contains commas |
| MultilineText | Plain text with line breaks | String value | May need specific CSV reader settings |
| TemplatedString | Generated value | String value | As generated from template |
| Email | Plain text string | String value | Quoted if contains commas |
| Address | Complete JSON in single column | Nested object | Requires post-processing |
| QRCodeFormField | Plain text string | String value | No metadata about scan |
| RichText | **Never exported** | **Never exported** | Content only in notebook definition |

#### Component Architecture {comprehensive}

**Standard Components**:
- **TextField/MultilineText**: formik-material-ui components
- **Email**: TextField with `type="email"` configuration

**Custom Components**:
- **TemplatedString**: `faims-custom::TemplatedStringField`
- **Address**: `faims-custom::AddressField` with complex JSON storage
- **QRCodeFormField**: `qrcode::QRCodeFormField` with ML Kit integration
- **RichText**: `faims-custom::RichText` with markdown rendering

**Display-Only Architecture (RichText)**:
- Requires full field definition despite no data operations
- Maintains `type-returned` and `validationSchema` for consistency
- Never participates in form data or validation

#### Accessibility Compliance {important}

**Compliant Fields** (WCAG 2.1 Level AA):
- TextField, MultipleTextField, TemplatedString, Email
- Minimum touch target size (44×44px)
- Proper label association
- Keyboard navigation support
- Screen reader compatibility
- Error message announcement
- Sufficient color contrast (3:1 minimum)

**Non-Compliant Fields**:
- Address: Edit button below WCAG minimum touch target
- RichText: Complete absence of ARIA attributes and accessibility features
- QRCodeFormField: No manual entry alternative

#### Testing Guidelines {comprehensive}

**Pre-Deployment Testing Checklist**:
- [ ] Test with empty data (all fields blank)
- [ ] Test with partial data (some fields filled)
- [ ] Test with maximum content length
- [ ] Test special characters and Unicode
- [ ] Test on minimum supported devices
- [ ] Test offline/sync scenarios
- [ ] Verify export formats preserve data
- [ ] Check accessibility with screen reader
- [ ] Test with malicious input (security)
- [ ] Monitor performance with typical load

---

## Individual Field Reference

### TextField / FAIMSTextField (FAIMS Text Field in Designer) {essential}
<!-- keywords: single-line, text, input, brief -->
**Designer Label**: FAIMS Text Field
**Component Name**: FAIMSTextField (enhanced) or TextField (base - Email only)
**Namespace**: faims-custom (FAIMSTextField) or formik-material-ui (TextField)

Note: Designer's "FAIMS Text Field" creates FAIMSTextField. The base TextField is only accessible through "Email" field configuration.

#### Purpose {essential}
Single-line text input for brief, unconstrained textual data. Primary choice for codes, identifiers, and short annotations.

#### Core Configuration {essential}
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "site-code",
    "label": "Site Code",
    "helperText": "Enter 3-letter site code",
    "required": true
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Site code is required"],
    ["yup.matches", "^[A-Z]{3}$", "Must be 3 capital letters"]
  ],
  "initialValue": ""
}
```

#### TextField Variants {important}
1. **Standard TextField** (formik-material-ui): Default with basic features
2. **FAIMSTextField** (faims-custom): Enhanced with expandable help, resizable UI

#### TextField-Specific Validation {important}
See [Common Characteristics > Common Validation Patterns] for standard rules

#### TextField-Specific Issues {important}
For solutions, see [Troubleshooting Guide > Quick Fixes Table]
- Users exceed 50 character recommendation
- Mobile keyboards cover input
- Pattern validation errors unclear
- No character counter displayed
- Mobile keyboard wrong type: Configure InputProps.type (`"email"`, `"tel"`, `"url"`)
- FAIMSTextField features missing: Check namespace and advancedHelperText

### MultilineText / MultipleTextField (Text Field in Designer) {essential}
<!-- keywords: multiline, textarea, paragraph, narrative -->
**Designer Label**: Text Field  
**Component Name**: MultipleTextField
**Namespace**: formik-material-ui

Note: Despite the confusing name, Designer's "Text Field" creates a multi-line text area (MultipleTextField component).

#### Purpose {essential}
Extended text entry for narrative content, detailed observations, and interpretative discourse exceeding single-line constraints. Fixed-height field with internal scrolling.

#### Core Configuration {essential}
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "MultipleTextField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "site-description",
    "label": "Site Description",
    "multiline": true,
    "InputProps": {
      "rows": 4
    }
  }
}
```

#### Row Configuration {important}
- **Default**: 4 rows
- **Recommended**: 4-6 for general use
- **Maximum practical**: 8-10 for extensive content
- Fixed height - no auto-expansion

#### Content Handling {important}
- Preserves all formatting (tabs, spaces, line breaks)
- Whitespace-only input converts to empty string
- Internal scrolling when content exceeds visible area
- No rich text formatting - plain text only
- Performance degrades beyond 10,000 characters (see [Common Characteristics > Performance Boundaries])

#### MultilineText-Specific Features {important}
- Enter key creates new lines (not form submission)
- Touch scrolling within field boundaries
- Voice dictation supports paragraph breaks
- Can be used in conditional logic despite length

#### MultilineText-Specific Issues {important}
- Users may not notice internal scrollbar
- Fixed height can hide content
- Performance degrades beyond 10,000 characters (see [Common Characteristics > Performance Boundaries])
- Line breaks may not preserve in some exports
- Voice input creates run-on text (Android): Manual paragraph breaks needed (see [Troubleshooting Guide > Common Problems Table])

### TemplatedString (Templated String Field in Designer) {essential}
<!-- keywords: hrid, template, mustache, auto-generate, identifier -->
**Designer Label**: Templated String Field
**Component Name**: TemplatedStringField
**Namespace**: faims-custom

Note: Every notebook must have at least one TemplatedString configured as the hridField.

#### Purpose {essential}
Auto-generates text values from other fields using Mustache templates. **MANDATORY** for Human-Readable Identifiers (HRIDs) - every notebook must have at least one configured as `hridField`.

#### Core Configuration {essential}
```json
{
  "component-namespace": "faims-custom",
  "component-name": "TemplatedStringField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "record-id",
    "template": "{{site}}-{{date}}-{{counter}}",
    "readOnly": true
  }
}
```

#### Template Syntax {important}
- **Variable substitution**: `{{fieldName}}`
- **Conditional sections**: `{{#field}}content{{/field}}`
- **Inverted sections**: `{{^field}}if empty{{/field}}`
- **System variables**: `{{_CREATED_BY}}`, `{{_CREATED_TIME}}`
- **Parent fields**: `{{_PARENT_.fieldname}}`

#### Critical Implementation Notes {important}
- Must be in same form as referenced fields
- Updates automatically when source fields change
- Deep equality comparison for complex fields
- Cannot reference other TemplatedStrings (circular reference)
- HTML escaping disabled - security risk with user input (see [Common Characteristics > Security Considerations])

#### TemplatedString-Specific Troubleshooting {important}
- **Template returns empty**: Verify field names match (case-sensitive), check console
- **Shows [object Object]**: Using complex field types - only use for conditional checking
- **Not updating**: Check for circular references between templates

### Email {essential}
<!-- keywords: email, validation, address, contact -->

#### Core Configuration {essential}
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::Email",
  "component-parameters": {
    "name": "email-field",
    "label": "Email Address",
    "InputProps": {
      "type": "email"
    }
  }
}
```

#### Email-Specific Validation {important}
| Rule | Schema | Purpose | Error Message |
|------|--------|---------|---------------|
| required | `["yup.required", "Email is required"]` | Mandatory field | "Email is required" |
| email format | `["yup.email", "Enter a valid email"]` | Format validation | "Enter a valid email" |
| string type | `["yup.string"]` | Type enforcement | Type error (rare) |

**Accepted Formats**: user@domain.com, user+tag@domain.com, first.last@domain.com, user_name@domain.com, user-name@domain-name.com, user@mail.company.com, user123@domain.com

**Rejected Formats**: Missing @ symbol or domain, spaces within address, double @ symbols, leading/trailing dots, missing top-level domain

#### Email-Specific Limitations {important}
- No multiple emails (array input not supported)
- No domain restrictions without custom validation
- No contact integration (device contacts)
- No verification (format only, not deliverability)
- No auto-lowercase (case preserved as entered)
- No duplicate checking

#### Email-Specific Troubleshooting {important}
Also see [Troubleshooting Guide > Common Problems Table] for general validation issues
- **Validation too strict**: Actually permissive; check for spaces
- **Plus addresses rejected**: Supported; check other issues
- **Keyboard missing @**: Ensure `InputProps.type` set to "email"

### Address {essential}
<!-- keywords: address, geocode, json, australian, beta -->

#### Core Configuration {essential}
```json
{
  "component-namespace": "faims-custom",
  "component-name": "AddressField",
  "name": "site-address",
  "type-returned": "faims-core::JSON"
}
```

#### Address-Specific Storage {important}
```json
{
  "display_name": "123 Main St, Parramatta, NSW, 2150",
  "address": {
    "house_number": "123",
    "road": "Main St",
    "town": "",
    "suburb": "Parramatta",
    "municipality": "",
    "state": "NSW",
    "postcode": "2150",
    "country": "",
    "country_code": ""
  }
}
```

**CSV Export**: Complete JSON in single column, requires post-processing:
```python
import pandas as pd
import json
df = pd.read_csv('export.csv')
df['address_data'] = df['site_address'].apply(json.loads)
df['postcode'] = df['address_data'].apply(lambda x: x['address']['postcode'])
```

#### Address-Specific Interactions {important}
1. Collapsed field shows current value or "Empty"
2. Click/tap edit icon to expand
3. Enter data across five optional fields
4. System generates display name
5. Field collapses on blur

**⚠️ Race Condition Warning**: Rapid tabbing between fields may trigger data loss. Allow 500ms pause between field entries.

#### Address-Specific Issues {important}
- **Beta Feature Status**: Commissioned functionality for specific client
- **No country field in UI**: Only 5 of 9 data fields exposed
- **JSON expertise required**: Post-processing needed for analysis
- **Touch target concern**: Edit button below WCAG minimum

### QRCodeFormField {essential}
<!-- keywords: barcode, scanner, mobile-only, qrcode -->

#### Core Configuration {essential}
```json
{
  "component-namespace": "qrcode",
  "component-name": "QRCodeFormField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "label": "Scan Barcode",
    "name": "barcode-field",
    "helperText": "Position barcode within frame",
    "fullWidth": true
  }
}
```

#### Supported Barcode Formats {important}
1. QR Code – Most common 2D format
2. Code 128 – High-density linear barcode
3. Code 39 – Alphanumeric linear format
4. Code 93 – Compact linear barcode
5. Codabar – Numeric with special characters
6. Data Matrix – Compact 2D format
7. EAN-13 – European Article Number
8. EAN-8 – Shortened EAN variant
9. ITF – Interleaved 2 of 5
10. UPC-E – Compressed UPC format
11. UPC-A – Standard retail barcode
12. PDF417 – Multi-row 2D format
13. Aztec – Compact 2D format

#### QRCode-Specific Validation {important}
- **10-scan mechanism**: Must read identical value 10 consecutive times
- **No user feedback**: Silent validation process
- **Silent reset**: Different barcode during validation resets counter
- **⚠️ CRITICAL**: Never mark as required (breaks web forms completely)

#### Mobile Scanning Workflow {important}
1. Tap blue "Scan barcode" button
2. Camera permission requested on first use
3. Full-screen scanner launches
4. Position barcode in frame
5. **Hidden**: Scanner validates 10 consecutive identical reads
6. Success: Value captured, returns to form
7. Different barcode: Counter resets silently
8. Cancel: Back button leaves field empty

#### QRCode-Specific Issues {important}
- **Scanner won't complete**: Ensure single barcode visible, hold steady 3-4 seconds
- **Web platform**: Completely non-functional, disabled interface
- **No manual entry**: Pair with TextField for fallback

### RichText {essential}
<!-- keywords: display, markdown, instructions, static, memory-leak -->

#### Core Configuration {essential}
```json
{
  "component-namespace": "faims-custom",
  "component-name": "RichText",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-id",
    "content": "# Heading\n\nInstructional text with **markdown** formatting."
  },
  "validationSchema": [["yup.string"]],
  "initialValue": ""
}
```

#### RichText-Specific Behavior {important}

**Rendering Pipeline**:
1. markdown-it processes content with `typographer: true`
2. DOMPurify strips dangerous elements with hardcoded whitelist
3. Sanitized HTML inserted via `dangerouslySetInnerHTML`
4. **No caching**: Re-executes entire pipeline on every render

**Security Filtering** - Allowed Elements:
- Text: `<p>`, `<span>`, `<strong>`, `<em>`, `<u>`, `<s>`, `<code>`, `<pre>`
- Headers: `<h1>` through `<h6>`
- Lists: `<ul>`, `<ol>`, `<li>`
- Links: `<a>` (with href, title, target="_blank")
- Images: `<img>` (Base64 only, external URLs blocked)

**Blocked at Runtime** (despite Designer support):
- Tables: `<table>`, `<tr>`, `<td>`, `<th>`
- Blockquotes: `<blockquote>`
- All scripts, forms, media, styles

#### RichText-Specific Limitations {important}
- **Memory leak**: Never releases parsed HTML, crashes mobile with 10+ fields
- **No accessibility**: Complete absence of ARIA attributes
- **Designer-runtime mismatch**: Tables/blockquotes disappear
- **No memoization**: Reparsed on every render (20-50ms overhead)
- **Error display**: Shows only "Error" with no diagnostics
- **No RTL support**: No bidirectional text handling
- **Export invisibility**: Never appears in any export format
- **No dynamic content**: Cannot reference field values
- **No interactivity**: Pure display component

---

## Troubleshooting Guide {important}

### Validation Issues {important}

#### Validation Not Displaying {important}
**Affects**: TextField, MultipleTextField, TemplatedString, Email, Address  
**Symptom**: Required field not showing error  
**Cause**: Field hasn't been "touched"  
**Solution**: Field must gain focus then blur to show errors  
See [Common Characteristics > Validation Patterns > Validation Behavior]

#### Cannot Submit Form on Web {important}
**Affects**: QRCodeFormField  
**Symptom**: Validation error on web browser  
**Cause**: QRCodeFormField marked required  
**Solution**: Remove required validation or implement manual entry field

### Critical Issues Table {important}

| Symptom | Field Type | Cause | Immediate Action | Fix | Prevent |
|---------|------------|-------|------------------|-----|---------|
| Form cannot be submitted on web | QRCodeFormField | Required validation breaks web platform | Remove required validation | Never mark QRCodeFormField as required | Pair with TextField for web fallback |
| Maximum call stack exceeded | TemplatedString | Circular reference between templates | Remove circular references | Templates cannot reference other TemplatedStrings | Validate template references before deployment |
| App crashes with multiple fields | RichText | Memory leak accumulation (>10 fields) | Restart app immediately | Limit to <10 RichText fields, <1000 total words | Monitor RichText count and content volume |
| XSS vulnerability exposed | TemplatedString | HTML escaping disabled with user input | Remove user text fields from templates | Use controlled vocabularies only | Never include free-text fields in templates |
| Data disappears while typing | Address | Race condition when tabbing quickly | Save form immediately | Allow 500ms pause between field entries | Train users on deliberate entry |
| Form won't load | Any field | Wrong component name or namespace | Check browser console | Verify exact component names and namespaces | Use documentation component mapping |
| Field permanently shows "Empty" | Address | initialValue set to "" instead of null | Change initialValue to null | Address must use null not empty string | Check all JSON field types |
| Scanner never completes | QRCodeFormField | Multiple barcodes or movement during scan | Isolate single barcode | Hold steady 3-4 seconds for 10-scan validation | Train on scanning requirements |
| Validation prevents all edits | Any field | Required added to populated field | Remove required temporarily | Test validation before applying to existing data | Add validation only to new fields |

### Common Problems Table {important}

| Symptom | When | Why | Try This | If That Fails | Long Term |
|---------|------|-----|----------|---------------|-----------|
| Required field not showing error | After form submission attempt | Field hasn't been "touched" | Click field then click away | Check validation schema order | Train users on validation timing |
| Email validation too strict | Entering institutional addresses | Actually permissive - check for spaces | Remove all spaces from email | Check for typos in address | Document accepted formats |
| Content exceeds field boundaries | TextField >50 chars | Single-line limitation | Switch to MultilineText | Reduce content length | Set character limits upfront |
| Tables/blockquotes disappear | RichText at runtime | DOMPurify strips unsupported elements | Use formatted lists or Base64 images | Create image of complex content | Document runtime limitations |
| External images don't display | RichText content | Security blocks external URLs | Convert to Base64 embedded images | Use images <100KB only | Train on image requirements |
| Line breaks lost in export | MultilineText CSV export | Reader settings issue | Configure CSV reader for multiline | Use specific delimiter settings | Document export requirements |
| JSON in single column | Address CSV export | Complex object export behavior | Post-process with Python/scripts | Extract needed fields only | Provide extraction scripts |
| @ symbol missing on keyboard | Email field mobile | Wrong keyboard type | Ensure InputProps.type="email" | Type @ manually | Test on target devices |
| Performance degrades | >30 text fields per section | Form evaluation overhead | Paginate form sections | Reduce fields per section | Design with limits in mind |
| No character counter shown | TextField/MultilineText | Not built into component | Add count to helperText | Use FAIMSTextField variant | Set expectations clearly |

### Quick Fixes Table {important}

| Want To | Use This | Not This | Because | Example |
|---------|----------|----------|---------|---------|
| Single-line text in Designer | FAIMS Text Field | Text Field | "Text Field" creates multiline | FAIMSTextField component |
| Multi-line text in Designer | Text Field | FAIMS Text Field | Despite confusing name | MultipleTextField component |
| Email with validation | Email field | Custom TextField config | Email field pre-configured | Includes type="email" automatically |
| Manual barcode entry | Paired TextField | QRCodeFormField alone | QRCode is mobile-only | Add fallback TextField |
| Display instructions | RichText | TemplatedString | RichText for static content | TemplatedString needs field references |
| Structured address | Address field | Multiple TextFields | Unless JSON complexity an issue | Consider data extraction needs |
| Character limit enforcement | validationSchema with yup.max | inputProps.maxLength alone | Validation provides user feedback | ["yup.max", 50, "Maximum 50 characters"] |
| Template with user input | Controlled vocabulary fields | Free text fields | XSS vulnerability risk | Use Select/RadioGroup in templates |
| Fix "Empty" Address display | initialValue: null | initialValue: "" | Address requires null | JSON fields need null not empty string |
| Prevent race condition | 500ms pause between fields | Rapid tabbing | Address field state updates | Train deliberate data entry |

### Debug Checklists {comprehensive}

#### General Field Checklist {comprehensive}
- [ ] Field name unique within form
- [ ] component-namespace matches component type
- [ ] type-returned is correct type
- [ ] initialValue is "" not null (or null for Address)
- [ ] Label concise and clear

#### Field-Specific Checks {comprehensive}

**TemplatedString**:
- [ ] Template syntax uses `{{field}}`
- [ ] All referenced fields exist
- [ ] hridField configured in viewset
- [ ] No circular template references
- [ ] User input sanitized if included

**TextField/Email**:
- [ ] Correct variant (standard vs FAIMS)
- [ ] InputProps.type appropriate
- [ ] Validation schema complete

**MultilineText**:
- [ ] multiline: true set
- [ ] InputProps.rows configured
- [ ] Content limits documented

**Address**:
- [ ] Component-namespace is "faims-custom"
- [ ] Type-returned is "faims-core::JSON"
- [ ] Team trained in data extraction

**QRCodeFormField**:
- [ ] Never marked as required
- [ ] Manual fallback field provided
- [ ] Platform compatibility documented

**RichText**:
- [ ] Content brief (<50 words per field)
- [ ] No tables or blockquotes
- [ ] Images Base64 encoded
- [ ] Test on mobile for memory issues

### Field-Specific Issues {important}

#### Address Field Race Condition {important}
**Symptom**: Data disappears when quickly tabbing between fields  
**Cause**: State update race condition  
**Solution**: 
- Allow 500ms pause between entries
- Use Tab key rather than mouse
- Save form frequently
- Consider separate TextFields for critical data

#### QRCodeFormField Scanner Issues {important}
**Scanner won't complete**: 
- Ensure single barcode visible
- Hold steady 3-4 seconds
- Clean barcode if dirty
- Isolate from other barcodes

**Permission denied**:
- Settings > Apps > Fieldmark > Permissions > Camera > Enable
- Reload app after permission grant

---

## JSON Examples {important}

### TextField Examples {important}

#### Basic Site Code {important}
```json
{
  "site-code": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "site-code",
      "label": "Site Code",
      "helperText": "3-letter site identifier",
      "placeholder": "e.g., SYD",
      "required": true,
      "fullWidth": false,
      "variant": "outlined"
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Site code is required"],
      ["yup.matches", "^[A-Z]{3}$", "Must be exactly 3 capital letters"]
    ],
    "initialValue": ""
  }
}
```

#### FAIMSTextField with Advanced Help {comprehensive}
```json
{
  "unit-designation": {
    "component-namespace": "faims-custom",
    "component-name": "FAIMSTextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "unit-designation",
      "label": "Excavation Unit",
      "helperText": "Format: [Area]-T[Trench]-[Unit]",
      "advancedHelperText": "# Unit Designation System\n\nEach excavation unit follows a three-part code:\n\n1. Area: Single letter (A-Z)\n2. Trench: T + number\n3. Unit: 3-digit with leading zeros",
      "required": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Unit designation required"],
      ["yup.matches", "^[A-Z]-T\\d+-\\d{3}$", "Invalid format"]
    ],
    "initialValue": ""
  }
}
```

### MultilineText Example {important}

#### Detailed Interpretation Field {important}
```json
{
  "interpretation": {
    "component-namespace": "formik-material-ui",
    "component-name": "MultipleTextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "interpretation",
      "label": "Site Interpretation",
      "helperText": "Provide detailed interpretative narrative (minimum 200 characters)",
      "placeholder": "Describe the site significance, cultural context, and preliminary interpretations...",
      "required": true,
      "fullWidth": true,
      "multiline": true,
      "InputProps": {
        "rows": 6
      }
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Interpretation is required"],
      ["yup.min", 200, "Please provide at least 200 characters"],
      ["yup.max", 10000, "Maximum 10,000 characters"]
    ],
    "initialValue": "",
    "meta": {
      "uncertainty": {
        "include": true,
        "label": "Interpretation confidence"
      }
    }
  }
}
```

### TemplatedString Examples {important}

#### Complex HRID with System Variables {important}
For security considerations with user variables, see [Common Characteristics > Security Considerations]
```json
{
  "record-identifier": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "record-identifier",
      "template": "{{site}}-{{_CREATED_TIME}}-{{excavator}}-{{counter}}",
      "readOnly": true
    }
  }
}
```

#### Conditional Template with Boolean Logic {comprehensive}
```json
{
  "_has_photos": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "component-parameters": {
      "name": "_has_photos",
      "template": "{{#photos}}true{{/photos}}{{^photos}}false{{/photos}}",
      "hidden": true
    },
    "initialValue": "false"
  }
}
```

### Email Field Pattern {important}
```json
{
  "principal-investigator-email": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::Email",
    "component-parameters": {
      "label": "Principal Investigator Email",
      "name": "principal-investigator-email",
      "helperText": "Required for data access requests",
      "required": true,
      "InputProps": {
        "type": "email"
      }
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.email", "Valid email required"],
      ["yup.required", "PI email is mandatory"]
    ],
    "initialValue": ""
  }
}
```

### Address Field Pattern {important}
```json
{
  "site-street-address": {
    "component-namespace": "faims-custom",
    "component-name": "AddressField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Site Street Address",
      "name": "site-street-address",
      "helperText": "Enter the formal street address for site access",
      "required": false,
      "fullWidth": true
    },
    "validationSchema": [["yup.object"], ["yup.nullable"]],
    "initialValue": null,
    "meta": {
      "annotation": {
        "include": true,
        "label": "Address notes (e.g., alternative access points)"
      }
    }
  }
}
```

### QRCodeFormField with Manual Fallback {important}
```json
{
  "artefact-id-scan": {
    "component-namespace": "qrcode",
    "component-name": "QRCodeFormField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Scan Artefact Tag",
      "name": "artefact-id-scan",
      "helperText": "Use mobile scanner for barcode"
    },
    "initialValue": ""
  },
  "artefact-id-manual": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Or Enter Artefact ID Manually",
      "name": "artefact-id-manual",
      "helperText": "Type ID if scanner unavailable"
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.matches", "^[A-Z]{3}-\\d{4}-\\d{3}$", "Format: ABC-2024-001"]
    ]
  }
}
```

### RichText Conditional Instructions {important}
```json
{
  "excavation-warning": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "excavation-warning",
      "content": "⚠️ **STOP**: Consult heritage officer before excavation.\n\nThis site requires special permits."
    },
    "condition": {
      "field": "heritage-status",
      "operator": "equal",
      "value": "protected"
    }
  }
}
```

---

## Migration and Best Practices {comprehensive}

### Migration Decision Tree {comprehensive}

Reviewing existing text fields?
│
├─ Missing HRID field?
│  └─ YES → URGENT: Add TemplatedString as hridField
│
├─ TextField with long content?
│  └─ YES → Migrate to MultilineText
│     └─ Update rows parameter
│
├─ MultilineText with brief content?
│  └─ YES → Consider TextField for efficiency
│
├─ QRCodeFormField on web?
│  └─ YES → Add paired TextField fallback
│
└─ RichText with data capture need?
└─ YES → Replace with appropriate input field

### Migration Warnings Index

#### Safe Migrations (No Data Loss)
- `SAFE` TextField → MultilineText when content exceeds limits
- `SAFE` Adding TemplatedString to existing notebook
- `SAFE` Adding validation patterns to TextField
- `SAFE` Increasing MultilineText rows parameter

#### Breaking Changes (Data Loss Risk)  
- `BREAKS` Changing field names (orphans all data)
- `BREAKS` MultilineText → TextField if content >200 chars
- `BREAKS` Adding required validation to populated fields
- `BREAKS` Modifying TemplatedString pattern after data collection

### Migration Procedures
For ready-to-use scripts, see [Migration Script Templates] below

#### Designer Version Migration {comprehensive}

**Component Architecture Clarification**:
- FAIMSTextField: Enhanced single-line (Designer: "FAIMS Text Field")
- TextField: Base component, only via Email field in Designer
- MultipleTextField: Multi-line text area (Designer: "Text Field")

**Legacy Patterns to Avoid**:
```json
// ❌ Old pattern - TextField with multiline:true
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "component-parameters": {
    "multiline": true  // Deprecated approach
  }
}

// ✅ Current pattern - Use MultipleTextField
{
  "component-namespace": "formik-material-ui", 
  "component-name": "MultipleTextField",
  "component-parameters": {
    "multiline": true,
    "InputProps": {"rows": 4}
  }
}
```

**Pre-2024 Notebooks**: May use different component naming:
- Legacy "TextFormField" → migrate to "FAIMSTextField"  
- Legacy "TextArea" → migrate to "MultipleTextField"
- Legacy plain "TextField" → migrate to "FAIMSTextField" or configure as Email

#### TextField to MultilineText Migration
When content regularly exceeds 50 characters:
1. Change component-name to "MultipleTextField"
2. Add `multiline: true`
3. Set appropriate `InputProps.rows`
4. Adjust validation thresholds
5. Update helper text expectations

#### Adding TemplatedString to Existing Notebook {comprehensive}
1. Define HRID pattern based on existing data
2. Add TemplatedString field configuration
3. Set as `hridField` in viewset
4. Test with sample data
5. Note: Existing records won't auto-update

### Training Requirements {important}

#### Basic Training (All Users)
- Platform-specific keyboard behaviors
- Understanding validation timing
- When to use annotations vs main field
- Character limit awareness

#### Advanced Training (Data Managers)
- JSON structure of Address fields
- TemplatedString pattern design
- Export format handling
- QRCodeFormField platform limitations

#### Field Supervisor Training
- Choosing appropriate text field types
- Vocabulary development strategies
- Quality assurance protocols

### Migration Script Templates {comprehensive}

Ready-to-use migration scripts for common text field conversions:

#### Template 1: TextField to MultilineText Migration
```javascript
// Complete migration script for expanding single-line to multi-line fields
const migrateTextFieldToMultiline = (records, fieldName) => {
  const migrated = [];
  const oversized = [];
  
  records.forEach((record, index) => {
    const content = record[fieldName];
    if (content && content.length > 50) {
      oversized.push({
        index,
        recordId: record._id,
        length: content.length,
        preview: content.substring(0, 100) + '...'
      });
    }
    // Content migrates as-is, just the field config changes
    migrated.push(record);
  });
  
  console.log(`Total records: ${records.length}`);
  console.log(`Oversized content (>50 chars): ${oversized.length}`);
  
  // Update field configuration
  const newConfig = {
    "component-namespace": "formik-material-ui",
    "component-name": "MultipleTextField",  // Changed from TextField
    "component-parameters": {
      "multiline": true,
      "InputProps": {
        "rows": 4  // Adjust based on average content length
      }
    }
  };
  
  return {migrated, oversized, newConfig};
};

// Usage
const results = migrateTextFieldToMultiline(allRecords, 'description_field');
if (results.oversized.length > 0) {
  console.log('Records with long content:', results.oversized);
}
```

#### Template 2: Adding TemplatedString HRID to Existing Notebook
```javascript
// Script to generate HRIDs for existing records without them
const addHRIDsToExistingRecords = (records, pattern) => {
  const updated = [];
  const conflicts = [];
  const usedHRIDs = new Set();
  
  // First pass: collect existing HRIDs if any
  records.forEach(record => {
    if (record.hrid_field) {
      usedHRIDs.add(record.hrid_field);
    }
  });
  
  // Second pass: generate HRIDs for records without them
  records.forEach((record, index) => {
    if (!record.hrid_field) {
      // Generate HRID based on pattern and existing fields
      let hrid = pattern
        .replace('{{site}}', record.site || 'UNKNOWN')
        .replace('{{date}}', record.date || new Date().toISOString().split('T')[0])
        .replace('{{counter}}', String(index + 1).padStart(4, '0'));
      
      // Check for conflicts
      let suffix = 1;
      const baseHRID = hrid;
      while (usedHRIDs.has(hrid)) {
        hrid = `${baseHRID}-${suffix}`;
        suffix++;
        conflicts.push({recordId: record._id, attemptedHRID: baseHRID, finalHRID: hrid});
      }
      
      record.hrid_field = hrid;
      usedHRIDs.add(hrid);
      updated.push({recordId: record._id, newHRID: hrid});
    }
  });
  
  console.log(`Generated HRIDs for ${updated.length} records`);
  if (conflicts.length > 0) {
    console.log(`Resolved ${conflicts.length} HRID conflicts`);
  }
  
  return {records, updated, conflicts};
};

// Usage
const hridPattern = '{{site}}-{{date}}-{{counter}}';
const results = addHRIDsToExistingRecords(allRecords, hridPattern);
```

#### Template 3: Address Field JSON Data Extraction
```python
import pandas as pd
import json

def extract_address_components(csv_file, address_field='site_address'):
    """
    Extract structured address data from JSON-stored Address fields
    """
    # Read CSV with Address field as string
    df = pd.read_csv(csv_file, dtype={address_field: str})
    
    # Initialize component columns
    components = ['house_number', 'road', 'suburb', 'state', 'postcode', 'display_name']
    for component in components:
        df[f'addr_{component}'] = ''
    
    # Process each row
    processed = 0
    errors = []
    
    for idx, row in df.iterrows():
        try:
            if pd.notna(row[address_field]) and row[address_field]:
                # Parse JSON
                addr_data = json.loads(row[address_field])
                
                # Extract display name
                if 'display_name' in addr_data:
                    df.at[idx, 'addr_display_name'] = addr_data['display_name']
                
                # Extract address components
                if 'address' in addr_data:
                    addr = addr_data['address']
                    for component in ['house_number', 'road', 'suburb', 'state', 'postcode']:
                        if component in addr:
                            df.at[idx, f'addr_{component}'] = addr[component]
                
                processed += 1
        except json.JSONDecodeError as e:
            errors.append({'row': idx, 'error': str(e)})
        except Exception as e:
            errors.append({'row': idx, 'error': str(e)})
    
    print(f"Successfully processed {processed} address fields")
    if errors:
        print(f"Errors in {len(errors)} rows: {errors[:5]}")  # Show first 5 errors
    
    # Save processed data
    output_file = csv_file.replace('.csv', '_addresses_extracted.csv')
    df.to_csv(output_file, index=False)
    print(f"Saved to: {output_file}")
    
    return df

# Usage
df = extract_address_components('export.csv', 'site_address')

# Additional analysis examples
print("\nAddress Statistics:")
print(f"Records with addresses: {df['addr_display_name'].notna().sum()}")
print(f"Unique suburbs: {df['addr_suburb'].nunique()}")
print(f"State distribution:\n{df['addr_state'].value_counts()}")
```

#### Template 4: Sanitizing User Input for TemplatedString
```javascript
// Sanitize user text fields before including in templates
const sanitizeForTemplate = (record, fieldName) => {
  let value = record[fieldName] || '';
  
  // Remove HTML/Script tags
  value = value.replace(/<[^>]*>/g, '');
  
  // Remove potential template injection
  value = value.replace(/{{.*?}}/g, '');
  
  // Remove SQL injection characters
  value = value.replace(/['";\\]/g, '');
  
  // Keep only alphanumeric, spaces, and basic punctuation
  value = value.replace(/[^a-zA-Z0-9\s\-_.,]/g, '');
  
  // Trim and limit length
  value = value.trim().substring(0, 50);
  
  return value;
};

// Batch sanitization before template evaluation
const sanitizeAllTextFields = (records, textFields) => {
  const sanitized = records.map(record => {
    const clean = {...record};
    textFields.forEach(field => {
      if (clean[field]) {
        clean[`${field}_raw`] = clean[field];  // Keep original
        clean[field] = sanitizeForTemplate(clean, field);
      }
    });
    return clean;
  });
  
  return sanitized;
};

// Usage
const textFieldsToSanitize = ['user_notes', 'description', 'comments'];
const safeRecords = sanitizeAllTextFields(records, textFieldsToSanitize);

// Now safe to use in templates:
// "{{site}}-{{sanitized_user_notes}}-{{counter}}"
```

#### Template 5: Character Limit Validation Check
```javascript
// Pre-migration check for character limits
const validateCharacterLimits = (records, limits) => {
  const violations = [];
  
  Object.entries(limits).forEach(([fieldName, maxLength]) => {
    records.forEach((record, index) => {
      const value = record[fieldName];
      if (value && value.length > maxLength) {
        violations.push({
          recordId: record._id || index,
          field: fieldName,
          currentLength: value.length,
          maxLength: maxLength,
          preview: value.substring(0, 100) + '...',
          overflow: value.length - maxLength
        });
      }
    });
  });
  
  // Group violations by field
  const byField = violations.reduce((acc, v) => {
    if (!acc[v.field]) acc[v.field] = [];
    acc[v.field].push(v);
    return acc;
  }, {});
  
  // Summary report
  console.log('\n=== Character Limit Validation Report ===');
  Object.entries(byField).forEach(([field, items]) => {
    console.log(`\n${field} (max: ${limits[field]} chars):`);
    console.log(`  - Violations: ${items.length}`);
    console.log(`  - Max overflow: ${Math.max(...items.map(i => i.overflow))} chars`);
    console.log(`  - Affected records: ${items.slice(0, 3).map(i => i.recordId).join(', ')}...`);
  });
  
  return violations;
};

// Usage
const fieldLimits = {
  'site_code': 50,      // TextField recommended
  'description': 10000, // MultilineText maximum
  'email': 254,         // RFC compliance
  'identifier': 30      // Custom limit
};

const violations = validateCharacterLimits(allRecords, fieldLimits);
if (violations.length > 0) {
  console.log(`\nAction required for ${violations.length} field values`);
}

### Field-Specific Best Practices {comprehensive}

#### Email Field {comprehensive}
- Provide clear helper text indicating email purpose
- Use placeholder sparingly to avoid confusion
- Consider privacy implications
- Document retention policies
- Test validation with institution-specific formats
- Include data protection notices where appropriate

#### Address Field {comprehensive}
**For Australian Projects**:
- Leverage optimised Australian format
- Use annotation fields for access notes
- Standardise state abbreviations (NSW, VIC, QLD)
- Include postcode for regional analysis

**For International Projects**:
- Add separate country TextField
- Document country codes in guidelines
- Consider separate TextFields for flexibility
- Establish clear data entry conventions

**For High-Volume Entry**:
- Enter data deliberately to avoid race conditions
- Use desktop platforms when possible
- Implement regular save routines
- Consider bulk import via JSON

#### QRCodeFormField {comprehensive}
- Consider pairing with TextField for manual entry fallback
- Never mark as required (web compatibility)
- Document scanning requirements explicitly
- Employ manual platform selection if needed
- Design recovery workflows for permission denial
- Test on all target platforms
- Provide clear helper text about mobile-only functionality
- Consider value transformation needs early
- Plan data reconciliation for paired fields
- Train field teams on 10-scan requirement

#### RichText {comprehensive}
**Content Guidelines**:
- Keep content brief: <50 words per field, <1000 total
- Use semantic headers: h2/h3 for navigation
- Embed critical images: Base64 for essential diagrams
- Write accessible content: Clear language, logical flow
- Test in runtime: Verify Designer content displays

**Performance Optimization**:
- Limit field count: Maximum 10 RichText fields
- Avoid conditional toggling: Minimize visibility changes
- Monitor mobile memory: Test on lowest-spec devices
- Batch related content: Combine instructions

**Common Anti-Patterns to Avoid**:
- ❌ Using RichText for dynamic content
- ❌ Creating tables (won't display)
- ❌ Embedding large images (>100KB)
- ❌ Writing documentation essays
- ❌ Conditional visibility on frequently-changing fields
- ❌ Assuming external images will work
- ❌ Ignoring memory accumulation on mobile

### Implementation Notes {comprehensive}

#### TextField/MultilineText Implementation {comprehensive}
Standard formik-material-ui components with predictable behavior across platforms.

#### TemplatedString Implementation {comprehensive}
Critical for notebook functionality. Must be in same form as referenced fields. Updates automatically when source fields change. Deep equality comparison for complex fields. Cannot reference other TemplatedStrings.

#### Email Field Implementation {comprehensive}
Not a distinct component but rather a TextField with email-specific configuration. This design pattern reduces code duplication whilst maintaining consistent behaviour across text input variants.

#### Address Field Implementation {comprehensive}
**Beta Feature Status**: Commissioned functionality for specific client requirements. Prioritises structured data capture over analytical convenience. Technical users can extract components through post-processing.

**Performance Considerations**:
- Form validation triggers on every keystroke
- Deep cloning occurs during updates
- Large addresses increase JSON payload size
- No character limits may impact database performance

#### QRCodeFormField Implementation {comprehensive}
Architecture reflects fundamental tension between data integrity and user experience. Ten-scan validation ensures exceptional accuracy but operates without user feedback.

**Critical considerations**:
- Platform Strategy: Design separate mobile and web form variants, or pair with TextField
- Validation Design: Never use required validation due to web incompatibility
- Error Recovery: Implement comprehensive fallback patterns
- User Training: Document the hidden 10-scan requirement
- Data Processing: Plan for external value transformation

Component name "QRCodeFormField" is a misnomer – scanner processes thirteen barcode formats with equal capability.

#### RichText Implementation {comprehensive}
Requirement for full field definition despite non-participation in data operations reveals fundamental tensions in Fieldmark's architecture. Treating display elements as fields ensures consistent handling but imposes unnecessary overhead.

**Rendering Inconsistencies**: Synchronous parsing and sanitisation pipeline executes on every render without memoisation, prioritising security over performance.

**Export Invisibility**: Exclusion from all export formats creates documentation gaps when notebooks serve as methodological records.

**Image Restrictions**: External image whitelist configuration (empty by default) effectively prohibits external image embedding.

### Cross-References Between Fields {comprehensive}
- **TextField** ↔ **MultilineText**: Migration when content exceeds 50 chars
- **TextField** → **Email**: Configuration for email capture
- **TextField** ↔ **FAIMSTextField**: Enhanced variant with advanced help
- **TemplatedString** → **All fields**: Can reference any field for templates
- **QRCodeFormField** → **TextField**: Essential pairing for manual fallback
- **Address** → **TextField**: Alternative for simple address storage
- **RichText** → **TemplatedString**: For dynamic vs static content

### External Documentation {comprehensive}
- BasicAutoIncrementer - Sequential numbering for templates
- Select/RadioGroup - Controlled vocabularies for templates
- TakePhoto - Referenced in TemplatedString examples
- Conditional Logic Guide - Visibility patterns
- Form Design Best Practices - Optimizing form performance
- Memory Management Guide - Mobile optimization strategies
- Accessibility Compliance - WCAG requirements and workarounds

---

## Field Quirks Index (2025-08) {comprehensive}

### TextField
- `RULE` Maximum 50 characters recommended for optimal display
- `RULE` 254 character limit for Shapefile DBF export compatibility
- `QUIRK` No character counter displayed to users
- `QUIRK` iOS keyboard may cover fields with predictive text
- `QUIRK` Voice input creates run-on text without punctuation
- `FIX` Implement character counter in helperText:
  ```json
  "component-parameters": {
    "helperText": "Site identifier (max 50 characters)",
    "inputProps": { "maxLength": 50 }  // Hard limit
  }
  ```
  For dynamic counter, use FAIMSTextField with: `"helperText": "Enter description (recommended: 20-50 characters)"`
- `VERSION` 2025-08

### MultilineText  
- `RULE` Component name is "MultipleTextField" not "MultilineTextField"
- `RULE` Use InputProps.rows to set visible height
- `QUIRK` Fixed height display - no auto-expansion
- `QUIRK` Performance degrades beyond 10,000 characters
- `QUIRK` CSV export may need specific reader settings for line breaks
- `FIX` Configure rows based on content type:
  - Brief notes (100-200 chars): `rows: 3`
  - Descriptions (200-500 chars): `rows: 5`
  - Detailed observations (500-1000 chars): `rows: 8`
  - Extensive narratives (1000+ chars): `rows: 10`
  - Set as: `"InputProps": { "rows": 5 }`  // Most common
- `FIX` Add validation for content length:
  ```json
  "validationSchema": [
    ["yup.string"],
    ["yup.max", 10000, "Content exceeds 10,000 character recommendation"],
    ["yup.test", "word-count", "Maximum 2000 words", 
      "value => !value || value.split(/\\s+/).length <= 2000"]
  ]
  ```
  Monitor in browser console: `formik.values['field-name'].length`
- `VERSION` 2025-08

### TemplatedString
- `RULE` Must exist as hridField in every notebook
- `RULE` Cannot reference other TemplatedString fields
- `RULE` Must be in same form as referenced fields
- `QUIRK` HTML escaping disabled (formUtilities.ts line 27) [Security Risk]
- `QUIRK` Shows [object Object] for complex fields
- `QUIRK` Shows [object Blob] for file/photo fields
- `QUIRK` Template syntax not validated in Designer
- `QUIRK` Silent failure for invalid templates
- `FIX` Handle complex fields with Mustache conditionals:
  - Photos: `{{#photos}}has-photos{{/photos}}{{^photos}}no-photos{{/photos}}`
  - Relationships: `{{#relationship}}linked{{/relationship}}`
  - Files: `{{#attachment}}attached{{/attachment}}`
  - Never direct reference: `{{photos}}` shows "[object Blob]"
  - Alternative: Create hidden boolean field for complex logic
- `FIX` Sanitize user input before template inclusion:
  - Basic HTML escape: `.replace(/[<>'"&]/g, '')`
  - Alphanumeric only: `.replace(/[^a-zA-Z0-9\s-]/g, '')`
  - SQL-safe: `.replace(/['";\\]/g, '')`
  - Best practice: Use Select/RadioGroup instead of free text
  - Never use TextField values directly in templates
- `FIX` Test templates systematically:
  1. In Designer > Preview, enter test values:
     - Empty fields: verify fallback behavior
     - Special chars: test with &, <, >, ", '
     - Max length: use expected maximum values
  2. Export test records to verify output format
  3. Document expected outputs: `"{{site}}-{{date}}"` → `"SITE01-2025-08"`
  4. Test edge cases: null, undefined, empty string
- `VERSION` 2025-08

### Email
- `RULE` Is TextField configuration with type="email", not separate component
- `RULE` Uses HTML5 email validation plus Yup patterns
- `QUIRK` Space bar often hidden on mobile keyboards
- `QUIRK` Voice input struggles with @ symbol
- `QUIRK` Browser may display envelope icon inconsistently
- `FIX` Use explicit email helper text:
  ```
  "helperText": "Institutional email only (e.g., name@university.edu.au)"
  // Or for specific requirements:
  "helperText": "Project contact email (no spaces, lowercase recommended)"
  // For multiple domains:
  "helperText": "Accepted domains: @uni.edu.au, @museum.gov.au"
  ```
- `FIX` Add domain-specific email validation:
  ```json
  // Australian institutions:
  ["yup.matches", "@[\\w.-]+\\.edu\\.au$", "Must be .edu.au email"]
  // Government only:
  ["yup.matches", "@[\\w.-]+\\.gov\\.au$", "Must be .gov.au email"]
  // Multiple allowed domains:
  ["yup.matches", "@(uni\\.edu|museum\\.gov|dept\\.org)\\.au$", 
    "Must be institutional email"]
  ```
- `VERSION` 2025-08

### QRCodeFormField
- `RULE` Mobile-only functionality - no web support
- `RULE` Never mark as required (breaks web forms completely)
- `RULE` Supports 13 barcode formats despite name
- `QUIRK` 10-scan validation mechanism with no user feedback
- `QUIRK` Web platform shows disabled interface that breaks validation
- `QUIRK` Silent counter reset when different barcode detected
- `QUIRK` No manual entry option built-in
- `FIX` Implement scanner/manual field pairing:
  ```json
  {
    "barcode-scan": {
      "component-namespace": "qrcode",
      "component-name": "QRCodeFormField",
      "component-parameters": {
        "label": "Scan Barcode (Mobile Only)",
        "name": "barcode-scan"
      }
    },
    "barcode-manual": {
      "component-namespace": "formik-material-ui",
      "component-name": "TextField",
      "component-parameters": {
        "label": "Or Enter Barcode Manually",
        "name": "barcode-manual",
        "helperText": "Type if scanner unavailable"
      }
    }
  }
  ```
  Data reconciliation: Check both fields, prefer scan if present
- `FIX` Add explicit scanning instructions:
  ```
  "helperText": "Hold device steady for 3-4 seconds. Ensure single barcode visible. Mobile app only - use manual entry on web."
  ```
  For training materials: `"helperText": "Scanner requires: 1) Mobile device 2) Camera permission 3) Good lighting 4) Clean barcode 5) Steady hold"`
- `FIX` Implement platform-aware conditional display:
  ```json
  // Add platform detection field:
  {
    "is-mobile": {
      "component-name": "RadioGroup",
      "component-parameters": {
        "label": "Device Type",
        "options": [
          {"value": "mobile", "label": "Mobile (iOS/Android)"},
          {"value": "web", "label": "Web Browser"}
        ]
      }
    }
  }
  // Then use conditions:
  "condition": {"field": "is-mobile", "operator": "equal", "value": "mobile"}
  ```
- `VERSION` 2025-08

### Address
- `RULE` Beta feature - prioritises structure over convenience
- `RULE` Stores data as GeocodeJSON-compliant format
- `QUIRK` Edit button below WCAG minimum touch target (44×44px)
- `QUIRK` Exports as complete JSON in single CSV column
- `QUIRK` Race condition when quickly tabbing between fields
- `QUIRK` No character limits may impact database performance
- `QUIRK` Validation triggers on every keystroke
- `FIX` Prevent Address race condition:
  1. Train users: "Tab once, pause, continue"
  2. Or implement debounced saving: Designer > Advanced > Set debounce: 500
  3. Alternative workaround: Enter all data in one field first, copy-paste to others
  4. For bulk entry: Use CSV import instead
- `FIX` Extract Address components from CSV:
  ```python
  import pandas as pd
  import json
  
  # Read CSV
  df = pd.read_csv('export.csv')
  
  # Parse JSON column
  df['addr'] = df['site_address'].apply(
      lambda x: json.loads(x) if pd.notna(x) else {}
  )
  
  # Extract nested fields
  df['street'] = df['addr'].apply(
      lambda x: x.get('address', {}).get('road', '')
  )
  df['suburb'] = df['addr'].apply(
      lambda x: x.get('address', {}).get('suburb', '')
  )
  df['postcode'] = df['addr'].apply(
      lambda x: x.get('address', {}).get('postcode', '')
  )
  
  # Save processed data
  df.to_csv('processed_addresses.csv', index=False)
  ```
- `FIX` Replace Address field with TextFields for international use:
  ```json
  {
    "addr-line-1": {
      "component-name": "TextField",
      "label": "Address Line 1"
    },
    "addr-line-2": {
      "component-name": "TextField",
      "label": "Address Line 2"
    },
    "addr-city": {
      "component-name": "TextField",
      "label": "City/Town"
    },
    "addr-state": {
      "component-name": "TextField",
      "label": "State/Province/Region"
    },
    "addr-postcode": {
      "component-name": "TextField",
      "label": "Post/ZIP Code"
    },
    "addr-country": {
      "component-name": "Select",
      "label": "Country",
      "options": [/* country list */]
    }
  }
  ```
- `VERSION` 2025-08

### RichText
- `RULE` Display-only component - no data capture
- `RULE` Never exported in any format
- `RULE` Requires full field definition despite no data operations
- `QUIRK` Memory leak on mobile - never releases parsed HTML
- `QUIRK` Tables/blockquotes disappear at runtime despite Designer support
- `QUIRK` External images blocked (hardcoded empty whitelist)
- `QUIRK` No accessibility implementation (missing ARIA)
- `QUIRK` Re-parses content on every render without memoization
- `QUIRK` Shows only "Error" with no diagnostics on failure
- `FIX` Monitor and limit RichText content:
  - Word count: `content.split(/\s+/).length`
  - Character count: `content.length`
  - Limits: Per field: 50 words (350 characters), Per form: 1000 words total (7000 characters), Mobile safe: 10 fields maximum
  - Designer helper: `"content": "## Instructions (35 words)\n\nYour content here..."`
- `FIX` Convert images to Base64 for RichText:
  1. Check size first: image should be <100KB (ideally <50KB)
  2. Online tool: https://base64.guru/converter/encode/image
  3. Command line: Mac/Linux: `base64 -i image.png | pbcopy`, Windows: `certutil -encode image.png tmp.b64 && type tmp.b64`
  4. In RichText content: `"content": "![Diagram](data:image/png;base64,iVBORw0KGgo...)"`
  5. Size calculation: Base64 length × 0.75 = approx bytes
  6. Optimize first: Use tinypng.com to reduce size
- `FIX` Optimize RichText for memory:
  1. Count RichText fields: Designer > Field List > Filter by "RichText"
  2. If >10 fields needed, use pagination: Section 1: Fields 1-5 (page 1), Section 2: Fields 6-10 (page 2)
  3. Or use conditional visibility: `"condition": {"field": "show-instructions", "value": "true"}`
  4. Monitor in mobile app: iOS: Settings > Fieldmark > Documents & Data, Android: Settings > Apps > Fieldmark > Storage
  5. Clear cache if >100MB
- `FIX` Replace tables with structured lists:
  ```
  // Instead of table:
  | Column1 | Column2 |
  
  // Use formatted list:
  "content": "**Data Summary**\n\n• **Item 1**: Value 1\n• **Item 2**: Value 2\n\n---\n\n"
  
  // Or use preformatted text:
  "content": "```\nColumn1    Column2\n-------    -------\nValue1     Value2\n```"
  
  // Or create image of table and embed as Base64
  ```
- `VERSION` 2025-08

---

## Performance Thresholds Table (2025-08) {essential}

| Field Type | Metric | Threshold | Consequence | Platform | Version |
|------------|--------|-----------|-------------|----------|---------|
| TextField | Character count | 50 chars | Mobile viewport issues | Mobile | 2025-08 |
| TextField | Character count | 254 chars | Shapefile DBF export limit | All | 2025-08 |
| TextField | Fields per section | 30 fields | Form lag begins | All | 2025-08 |
| MultilineText | Character count | 10,000 chars | Performance degradation | All | 2025-08 |
| MultilineText | Character count | ~1MB | CouchDB document limit | All | 2025-08 |
| MultilineText | Row display | >10 rows | Scrolling issues | Mobile | 2025-08 |
| TemplatedString | Variables referenced | 50 vars | Form responsiveness degrades | All | 2025-08 |
| TemplatedString | Fields per form | 3 fields | Recommended maximum | All | 2025-08 |
| Email | Character count | 254 chars | RFC 5321 compatibility limit | All | 2025-08 |
| Address | JSON payload | No limit | Database performance impact | All | 2025-08 |
| Address | Field updates | <500ms gap | Race condition data loss | All | 2025-08 |
| QRCodeFormField | Scan attempts | 10 scans | Required for validation | Mobile | 2025-08 |
| QRCodeFormField | Hold duration | 3-4 seconds | Scanner completion time | Mobile | 2025-08 |
| RichText | Fields per notebook | 10 fields | Memory issues begin | Mobile | 2025-08 |
| RichText | Total word count | 1000 words | App crash likely | Mobile | 2025-08 |
| RichText | Words per field | 50 words | Performance impact | Mobile | 2025-08 |
| RichText | Image size | 100KB | Rendering delay | All | 2025-08 |
| RichText | Parse time | 20-50ms | Per-render overhead | All | 2025-08 |
| All text fields | Fields per section | 30 fields | Form lag | All | 2025-08 |
| All fields | Total per form | 50 fields | Requires pagination | All | 2025-08 |
| All fields | Sync payload | >5MB | Sync failures possible | Mobile | 2025-08 |

---

## JSON Patterns Cookbook (2025-08) {comprehensive}

### TextField Patterns

```json
// BASE PATTERN (all TextField variants inherit this)
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-name",
    "label": "Field Label"
  },
  "validationSchema": [["yup.string"]],
  "initialValue": ""
}

// VARIANT: Required with validation
+ "component-parameters": {
+   "required": true,
+   "helperText": "This field is mandatory"
+ }
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.required", "Field is required"]
+ ]

// VARIANT: Pattern validation (e.g., site codes)
+ "component-parameters": {
+   "helperText": "Format: ABC-123",
+   "placeholder": "e.g., SYD-001"
+ }
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.matches", "^[A-Z]{3}-\\d{3}$", "Invalid format"]
+ ]

// VARIANT: Email configuration
+ "component-parameters": {
+   "InputProps": {"type": "email"}
+ }
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.email", "Invalid email address"]
+ ]

// VARIANT: FAIMSTextField with rich help
- "component-namespace": "formik-material-ui"
+ "component-namespace": "faims-custom"
- "component-name": "TextField"
+ "component-name": "FAIMSTextField"
+ "component-parameters": {
+   "advancedHelperText": "## Detailed Instructions\n\nMarkdown formatted help..."
+ }

// VARIANT: Length constraints
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.min", 3, "Minimum 3 characters"],
+   ["yup.max", 50, "Maximum 50 characters"]
+ ]
```

### MultilineText Patterns

```json
// BASE PATTERN (using MultipleTextField component)
{
  "component-namespace": "formik-material-ui",
  "component-name": "MultipleTextField",  // Note the component name!
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "description",
    "label": "Description",
    "multiline": true,
    "InputProps": {
      "rows": 4  // Default rows
    }
  },
  "validationSchema": [["yup.string"]],
  "initialValue": ""
}

// VARIANT: Extended text with validation
+ "component-parameters": {
+   "InputProps": {
-     "rows": 4
+     "rows": 8  // More rows for longer content
+   },
+   "required": true,
+   "helperText": "Provide detailed description (200-10000 chars)"
+ }
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.required", "Description required"],
+   ["yup.min", 200, "Minimum 200 characters"],
+   ["yup.max", 10000, "Maximum 10,000 characters"]
+ ]

// VARIANT: With uncertainty metadata
+ "meta": {
+   "uncertainty": {
+     "include": true,
+     "label": "Confidence level"
+   }
+ }

// VARIANT: With annotation capability
+ "meta": {
+   "annotation": {
+     "include": true,
+     "label": "Additional notes"
+   }
+ }
```

### TemplatedString Patterns

```json
// BASE: Human-Readable Identifier (HRID)
{
  "component-namespace": "faims-custom",
  "component-name": "TemplatedStringField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "record-id",
    "label": "Record ID",
    "template": "{{field1}}-{{field2}}"
  },
  "validationSchema": [["yup.string"]],
  "initialValue": ""
}

// VARIANT: With auto-incrementer
  "template": "{{site}}-{{year}}-{{counter}}"
  // where counter is BasicAutoIncrementer field

// VARIANT: System variables
  "template": "{{_CREATOR_NAME}}-{{_CREATED_TIME}}-{{id}}"

// VARIANT: Conditional sections
  "template": "{{#type}}{{type}}-{{/type}}{{^type}}UNTYPED-{{/type}}{{number}}"

// VARIANT: Complex nested conditionals
  "template": "{{project}}{{#location}}-{{location}}{{/location}}{{#specimen}}-{{specimen}}{{#subspecimen}}/{{subspecimen}}{{/specimen}}{{/specimen}}"

// VARIANT: Hidden boolean for complex logic
+ "component-parameters": {
+   "hidden": true,  // Not shown in UI
+   "template": "{{#photos}}true{{/photos}}{{^photos}}false{{/photos}}"
+ }

// VARIANT: With validation on generated value
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.required", "ID generation failed"],
+   ["yup.min", 10, "ID too short"]
+ ]
```

### Email Patterns

```json
// EMAIL is a TextField variant with type="email"
{
  "component-namespace": "formik-material-ui",
  "component-name": "TextField",  // Still TextField!
  "type-returned": "faims-core::String",  // Note: NOT Email type
  "component-parameters": {
    "name": "contact-email",
    "label": "Contact Email",
    "InputProps": {
      "type": "email"  // This makes it an email field
    }
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.email", "Invalid email format"]
  ],
  "initialValue": ""
}

// VARIANT: Required institutional email
+ "component-parameters": {
+   "required": true,
+   "helperText": "Use institutional email only"
+ }
+ "validationSchema": [
+   ["yup.string"],
+   ["yup.required", "Email is required"],
+   ["yup.email", "Invalid email format"],
+   ["yup.matches", "@(uni\\.edu|gov\\.au)$", "Must use institutional email"]
+ ]
```

### Address Patterns

```json
// BASE: Australian-optimized address
{
  "component-namespace": "faims-custom",
  "component-name": "AddressField",
  "type-returned": "faims-core::JSON",  // Returns JSON not String!
  "component-parameters": {
    "name": "site-address",
    "label": "Site Address",
    "fullWidth": true
  },
  "validationSchema": [
    ["yup.object"],
    ["yup.nullable"]  // Allow null/empty
  ],
  "initialValue": null  // Not empty string!
}

// VARIANT: Required address
+ "component-parameters": {
+   "required": true,
+   "helperText": "Physical address required for access"
+ }
- "validationSchema": [
-   ["yup.object"],
-   ["yup.nullable"]
- ]
+ "validationSchema": [
+   ["yup.object"],
+   ["yup.required", "Address is required"]
+ ]

// VARIANT: With annotation
+ "meta": {
+   "annotation": {
+     "include": true,
+     "label": "Access notes (gate codes, etc.)"
+   }
+ }
```

### QRCodeFormField Patterns

```json
// BASE: Scanner only (mobile-only!)
{
  "component-namespace": "qrcode",
  "component-name": "QRCodeFormField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "barcode-scan",
    "label": "Scan Barcode"
  },
  "validationSchema": [["yup.string"]],  // NEVER add required!
  "initialValue": ""
}

// VARIANT: With helper text
+ "component-parameters": {
+   "helperText": "Position barcode in frame (mobile only)",
+   "fullWidth": true
+ }

// PAIRED PATTERN: Scanner + Manual fallback (recommended)
{
  "barcode-scan": {
    "component-namespace": "qrcode",
    "component-name": "QRCodeFormField",
    "component-parameters": {
      "name": "barcode-scan",
      "label": "Scan Barcode (Mobile)"
    },
    "initialValue": ""
  },
  "barcode-manual": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "component-parameters": {
      "name": "barcode-manual",
      "label": "Or Enter Manually",
      "helperText": "Type barcode if scanner unavailable"
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.matches", "^[A-Z0-9]{8,12}$", "Invalid barcode format"]
    ],
    "initialValue": ""
  }
}
```

### RichText Patterns

```json
// BASE: Display-only instructional content
{
  "component-namespace": "faims-custom",
  "component-name": "RichText",
  "type-returned": "faims-core::String",  // Required but never used
  "component-parameters": {
    "name": "instructions",
    "content": "# Instructions\n\n**Important**: Follow these steps..."
  },
  "validationSchema": [["yup.string"]],  // Required but never validates
  "initialValue": ""  // Required but never stores data
}

// VARIANT: Conditional display warning
+ "component-parameters": {
+   "content": "⚠️ **WARNING**: Heritage site - requires permits"
+ }
+ "condition": {
+   "field": "site-type",
+   "operator": "equal",
+   "value": "heritage"
+ }

// VARIANT: With embedded image (Base64 only!)
+ "component-parameters": {
+   "content": "![Diagram](data:image/png;base64,iVBORw0KGg...)"
+ }

// VARIANT: Complex markdown formatting
  "content": "## Section Header\n\n1. First item\n2. Second item\n\n```\nCode block\n```\n\n> Note: Blockquote (won't render at runtime!)"
```

### Common Patterns Across Types

```json
// CONDITIONAL VISIBILITY (any field)
+ "condition": {
+   "field": "trigger-field",
+   "operator": "equal",  // or: not-equal, contains, not-contains
+   "value": "specific-value"
+ }

// METADATA EXTENSIONS (text fields)
+ "meta": {
+   "uncertainty": {
+     "include": true,
+     "label": "Confidence"
+   },
+   "annotation": {
+     "include": true,
+     "label": "Notes"
+   }
+ }

// FULL WIDTH LAYOUT
+ "component-parameters": {
+   "fullWidth": true
+ }

// VISUAL VARIANTS (Material-UI fields)
+ "component-parameters": {
+   "variant": "outlined"  // or: filled, standard
+ }

// DISABLED/READ-ONLY
+ "component-parameters": {
+   "disabled": true  // or InputProps: { readOnly: true }
+ }
```

### Inheritance Hierarchy

```
TextField (base)
├── Email (type="email" variant)
├── FAIMSTextField (namespace change)
└── URL (type="url" variant - undocumented)

MultipleTextField
└── (no variants, but supports rows configuration)

TemplatedStringField
└── (no variants, template complexity varies)

AddressField
└── (no variants, beta feature)

QRCodeFormField
└── (no variants, mobile-only)

RichText
└── (no variants, display-only)
```

---

## JSON Anti-Patterns - What NOT to Do (2025-08) {comprehensive}

### Critical Mistakes That Break Forms

#### Component Name Confusion {important}

⚠️ **CRITICAL: Designer names ≠ Component names**

❌ **NEVER: Assume Designer names match JSON**
```json
{
  "component-name": "FAIMS Text Field"  // ERROR: Not a valid component name
}
```
✅ **ALWAYS: Use actual component names**
```json
{
  "component-namespace": "faims-custom",
  "component-name": "FAIMSTextField"  // Correct for Designer's "FAIMS Text Field"
}
```

❌ **NEVER: Use Designer's "Text Field" as component name**
```json
{
  "component-name": "Text Field"  // ERROR: Not a valid component name
}
```
✅ **ALWAYS: Use MultipleTextField for multi-line**
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "MultipleTextField"  // Correct for Designer's "Text Field"
}
```

❌ **NEVER: Try to create plain TextField through Designer**
```json
{
  "component-name": "TextField"  // Only available via Email field
}
```
✅ **ALWAYS: Use FAIMSTextField for single-line or Email for validated input**
```json
{
  "component-namespace": "faims-custom",
  "component-name": "FAIMSTextField"  // For general single-line text
}
```

#### TextField Anti-Patterns

❌ **NEVER: Wrong initialValue type**
```json
{
  "component-name": "TextField",
  "initialValue": null  // ERROR: "Cannot read property 'length' of null"
}
```
✅ **ALWAYS: Use empty string for text fields**
```json
{
  "initialValue": ""  // Correct for all string-type fields
}
```

❌ **NEVER: Validation schema in wrong order**
```json
{
  "validationSchema": [
    ["yup.required", "Required"],  // ERROR: "yup.required is not a function"
    ["yup.string"]
  ]
}
```
✅ **ALWAYS: Type declaration first**
```json
{
  "validationSchema": [
    ["yup.string"],  // Type first
    ["yup.required", "Required"]  // Then constraints
  ]
}
```

❌ **NEVER: Wrong component name for enhanced variant**
```json
{
  "component-namespace": "faims-custom",
  "component-name": "TextField"  // ERROR: Component not found
}
```
✅ **ALWAYS: Match namespace to component**
```json
{
  "component-namespace": "faims-custom",
  "component-name": "FAIMSTextField"  // Correct name for custom namespace
}
```

#### MultilineText Anti-Patterns

❌ **NEVER: Wrong component name**
```json
{
  "component-name": "MultilineTextField",  // ERROR: Component doesn't exist
  "component-parameters": {
    "multiline": true
  }
}
```
❌ **NEVER: Use "MultilineText" as component name**
```json
{
  "component-name": "MultilineText",  // ERROR: Not the actual component name
}
```
✅ **ALWAYS: Use MultipleTextField**
```json
{
  "component-name": "MultipleTextField",  // Correct component name
  "component-parameters": {
    "multiline": true,
    "InputProps": {"rows": 4}
  }
}
```

❌ **NEVER: Missing multiline flag**
```json
{
  "component-name": "MultipleTextField",
  "component-parameters": {
    "rows": 4  // ERROR: rows alone doesn't work
  }
}
```
✅ **ALWAYS: Set multiline and use InputProps.rows**
```json
{
  "component-parameters": {
    "multiline": true,
    "InputProps": {"rows": 4}  // Correct structure
  }
}
```

#### TemplatedString Anti-Patterns

❌ **NEVER: User text input without sanitization (CRITICAL SECURITY RISK)**
```json
{
  "template": "Record: {{user-text-field}}"
  // If user enters: <script>alert('XSS')</script>
  // HTML escaping is DISABLED (formUtilities.ts line 27) - script WILL execute!
}
```
✅ **ALWAYS: Use controlled vocabularies or sanitize**
```json
{
  "template": "{{record-type}}-{{counter}}"  // record-type is a Select field
  // OR implement sanitization in preprocessing layer
}
```

❌ **NEVER: Reference another TemplatedString**
```json
{
  "template": "{{other-template}}-{{number}}"  // ERROR: Circular reference risk
  // where other-template is also a TemplatedString
}
```
✅ **ALWAYS: Reference only non-template fields**
```json
{
  "template": "{{site}}-{{date}}-{{counter}}"  // All are basic input fields
}
```

❌ **NEVER: Reference fields from different forms**
```json
{
  "template": "{{parent.field}}-{{local-field}}"  // ERROR: Can't access parent
}
```
✅ **ALWAYS: Keep all referenced fields in same form**
```json
{
  "template": "{{field1}}-{{field2}}"  // Both in same form
}
```

#### Email Anti-Patterns

❌ **NEVER: Wrong type-returned**
```json
{
  "component-name": "TextField",
  "type-returned": "faims-core::Email",  // ERROR: Mismatched types
  "component-parameters": {
    "InputProps": {"type": "email"}
  }
}
```
✅ **ALWAYS: Email fields return String**
```json
{
  "type-returned": "faims-core::String",  // Correct - emails are strings
  "component-parameters": {
    "InputProps": {"type": "email"}
  }
}
```

❌ **NEVER: Create custom Email component**
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "Email"  // ERROR: No such component
}
```
✅ **ALWAYS: Use TextField with email type**
```json
{
  "component-name": "TextField",
  "component-parameters": {
    "InputProps": {"type": "email"}
  }
}
```

#### Address Anti-Patterns

❌ **NEVER: Wrong initialValue for Address**
```json
{
  "component-name": "AddressField",
  "initialValue": ""  // ERROR: Field shows "Empty" permanently
}
```
✅ **ALWAYS: Use null for Address fields**
```json
{
  "component-name": "AddressField",
  "initialValue": null  // Correct for JSON-type fields
}
```

❌ **NEVER: Wrong validation schema**
```json
{
  "validationSchema": [
    ["yup.string"]  // ERROR: Address returns JSON object
  ]
}
```
✅ **ALWAYS: Use object validation**
```json
{
  "validationSchema": [
    ["yup.object"],
    ["yup.nullable"]  // Allow empty state
  ]
}
```

❌ **NEVER: Wrong type-returned**
```json
{
  "component-name": "AddressField",
  "type-returned": "faims-core::String"  // ERROR: Returns complex object
}
```
✅ **ALWAYS: Address returns JSON**
```json
{
  "type-returned": "faims-core::JSON"  // Correct type
}
```

#### QRCodeFormField Anti-Patterns

❌ **NEVER: Mark as required (CRITICAL PLATFORM ISSUE)**
```json
{
  "component-name": "QRCodeFormField",
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Scan required"]  // ERROR: Breaks ALL web users!
  ]
}
```
✅ **ALWAYS: Keep optional or pair with TextField**
```json
{
  "component-name": "QRCodeFormField",
  "validationSchema": [["yup.string"]]  // Never add required
  // Pair with TextField for web fallback
}
```

❌ **NEVER: Assume cross-platform functionality**
```json
{
  "component-name": "QRCodeFormField",
  "component-parameters": {
    "helperText": "Scan or type barcode"  // ERROR: No typing capability
  }
}
```
✅ **ALWAYS: Document platform limitation**
```json
{
  "component-parameters": {
    "helperText": "Scan barcode (mobile only)"
  }
}
```

#### RichText Anti-Patterns

❌ **NEVER: Expect data storage**
```json
{
  "component-name": "RichText",
  "component-parameters": {
    "name": "important-data",  // ERROR: Never stores data
    "content": "Enter notes here"
  }
}
```
✅ **ALWAYS: Use only for display**
```json
{
  "component-name": "RichText",
  "component-parameters": {
    "content": "## Instructions\n\nThis is display-only text"
  }
}
```

❌ **NEVER: External image URLs**
```json
{
  "content": "![Diagram](https://example.com/image.png)"  
  // ERROR: External images blocked by security
}
```
✅ **ALWAYS: Use Base64 embedded images**
```json
{
  "content": "![Diagram](data:image/png;base64,iVBORw0KGg...)"
  // Images must be <100KB for performance
}
```

❌ **NEVER: Tables in content**
```json
{
  "content": "| Header | Value |\n|--------|-------|\n| Data | 123 |"
  // Tables stripped at runtime despite Designer support
}
```
✅ **ALWAYS: Use lists or embedded images**
```json
{
  "content": "**Data Values:**\n- Header: 123\n- Other: 456"
  // Or embed table as Base64 image
}
```

### The Most Expensive Mistakes

1. **QRCodeFormField with required validation** = Web users permanently blocked from submission
2. **TemplatedString with user text fields** = XSS vulnerability, security breach possible
3. **Circular TemplatedString references** = Form crashes with stack overflow
4. **RichText >10 fields on mobile** = Memory leak causes app crash, data loss
5. **Address with initialValue: ""** = Field becomes permanently invalid, no recovery
6. **MultilineText wrong component name** = Field doesn't render, form incomplete
7. **Email as custom component** = Component not found, form won't load
8. **TextField with null initialValue** = Runtime errors, validation fails
9. **Validation schema wrong order** = No validation applied, data integrity compromised
10. **External images in RichText** = Content missing, user confusion
11. **Designer name as component name** = Component not found, form fails to load
12. **Wrong namespace for component** = Component not found errors, debugging confusion

### Prevention Checklist

Before deploying any notebook:
- [ ] All text fields use `initialValue: ""`
- [ ] Address fields use `initialValue: null`
- [ ] No QRCodeFormField has required validation
- [ ] All TemplatedStrings avoid user text input
- [ ] MultilineText uses "MultipleTextField" component
- [ ] Email fields are TextField with type="email"
- [ ] RichText has no tables or external images
- [ ] Validation schemas have type declaration first
- [ ] No circular template references exist
- [ ] Platform limitations documented in helper text

---

## Quick Diagnosis Tables (2025-08) {important}

### When Designer Labels Don't Match Behaviour

| Designer Shows | Expected | Actual Behaviour | Diagnosis | Fix |
|---------------|----------|------------------|-----------|-----|
| FAIMS Text Field | Single line | Multi-line area | Wrong component | Check JSON: should be FAIMSTextField not MultipleTextField |
| Text Field | Multi-line | Single line | Wrong component | Check JSON: should be MultipleTextField not FAIMSTextField |
| Text Field | Multi-line | Nothing renders | Invalid component name | Ensure component-name is "MultipleTextField" |
| FAIMS Text Field | Single line | Error: component not found | Namespace issue | Ensure namespace is "faims-custom" for FAIMSTextField |
| Email | Email validation | Plain text | Missing configuration | TextField needs email-specific parameters |

### When Generation Fails

| Symptom | Field Type | Likely Cause | Quick Fix | Version |
|---------|------------|--------------|-----------|---------|
| Empty HRID displayed | TemplatedString | Missing referenced field | Check field names (case-sensitive) | 2025-08 |
| Shows [object Object] | TemplatedString | Using relationship/complex field | Use only for conditionals {{#field}} | 2025-08 |
| Shows [object Blob] | TemplatedString | Photo/file field in template | Use only for existence checking | 2025-08 |
| Shows "Unknown User" | TemplatedString | System variable null | _CREATOR_NAME may be undefined | 2025-08 |
| Template not updating | TemplatedString | Circular reference | Templates can't reference each other | 2025-08 |
| Template shows literal {{}} | TemplatedString | Field not in same form | All referenced fields must be in same form | 2025-08 |
| Scanner won't complete | QRCodeFormField | Multiple barcodes visible | Isolate single barcode in frame | 2025-08 |
| Scanner won't complete | QRCodeFormField | Not holding steady | Hold 3-4 seconds for 10 scans | 2025-08 |
| Scanner disabled | QRCodeFormField | Web platform | Mobile-only - pair with TextField | 2025-08 |
| Address shows "Empty" | Address | Wrong initialValue | Use null not "" for Address field | 2025-08 |

### When Validation Fails

| Symptom | Field Type | Pattern | Fix | Version |
|---------|------------|---------|-----|---------|
| Required not showing error | All text inputs | Field not "touched" | Field must gain focus then blur | 2025-08 |
| Required field not validating | All text inputs | Wrong schema order | Use [["yup.string"], ["yup.required"]] | 2025-08 |
| Email always invalid | Email | Missing email validation | Add ["yup.email", "Invalid email"] | 2025-08 |
| Email rejecting valid addresses | Email | Actually permissive | Check for spaces or typos | 2025-08 |
| Pattern never matches | TextField | Regex not escaped | Double-escape in JSON: "\\\\d" for \d | 2025-08 |
| Pattern validation on template | TemplatedString | Validates output not template | Pattern applies to generated value | 2025-08 |
| Form won't submit on web | QRCodeFormField | Field marked required | Never use required on QRCodeFormField | 2025-08 |
| Address validation fails | Address | Wrong type | Use [["yup.object"], ["yup.nullable"]] | 2025-08 |
| Validation on empty template | TemplatedString | Template evaluates to "" | Add fallback values in template | 2025-08 |
| Max length exceeded | TextField | >254 chars for Shapefile | Enforce 254 char limit if using Shapefile | 2025-08 |

### When Display Issues Occur

| Symptom | Field Type | Cause | Solution | Version |
|---------|------------|-------|----------|---------|
| Field cut off on mobile | TextField | >50 characters | Switch to MultilineText | 2025-08 |
| No scrollbar visible | MultilineText | Content exceeds rows | Increase InputProps.rows value | 2025-08 |
| Keyboard covers field | TextField | iOS predictive text | Configure InputProps.type | 2025-08 |
| Tables disappear | RichText | DOMPurify strips tables | Use image or formatted list | 2025-08 |
| Blockquotes missing | RichText | Runtime sanitization | Use indented paragraphs instead | 2025-08 |
| Images don't load | RichText | External URLs blocked | Use Base64 embedded images only | 2025-08 |
| Address shows "Empty" | Address | initialValue is "" | Set initialValue to null | 2025-08 |
| @ symbol missing | Email | Wrong keyboard type | Set InputProps.type = "email" | 2025-08 |
| Wrong component name shown | MultilineText | Common confusion | Component is "MultipleTextField" | 2025-08 |
| Edit button too small | Address | Below WCAG minimum | Known issue - use desktop | 2025-08 |

### When Export Issues Occur

| Symptom | Field Type | Format | Issue | Solution | Version |
|---------|------------|--------|-------|----------|---------|
| Leading zeros lost | TemplatedString | CSV in Excel | Excel converts to number | Prefix with letters: "ID-0001" | 2025-08 |
| Line breaks lost | MultilineText | CSV | Reader settings | Configure CSV reader for multiline | 2025-08 |
| JSON in single column | Address | CSV | Complex object export | Post-process with Python/script | 2025-08 |
| Field missing from export | RichText | Any format | Display-only field | Content only in notebook definition | 2025-08 |
| Data truncated | TextField | Shapefile | 254 char DBF limit | Keep under 254 characters | 2025-08 |
| Email truncated | Email | Shapefile | 254 char limit | Use abbreviated addresses | 2025-08 |
| Template shows formula | TemplatedString | CSV | Not the issue | Exports generated value correctly | 2025-08 |
| Special chars corrupted | All text | CSV | Encoding issue | Use UTF-8 encoding | 2025-08 |
| Commas break columns | TextField | CSV | Delimiter conflict | Values auto-quoted if contains comma | 2025-08 |
| Barcode values missing | QRCodeFormField | Any format | No scan metadata | Only raw value exported | 2025-08 |

### When Performance Issues Occur

| Symptom | Field Type | Threshold | Solution | Version |
|---------|------------|-----------|----------|---------|
| Form lag on input | TextField/MultilineText | >30 per section | Paginate form sections | 2025-08 |
| Typing lag | MultilineText | >10,000 chars | Reduce content or use attachments | 2025-08 |
| Mobile app crashes | RichText | >10 fields | Limit to <10 RichText fields | 2025-08 |
| Mobile app crashes | RichText | >1000 total words | Reduce to <1000 words total | 2025-08 |
| Template evaluation slow | TemplatedString | >50 variables | Simplify template logic | 2025-08 |
| Template evaluation slow | TemplatedString | >3 complex templates | Reduce template count per form | 2025-08 |
| Address entry lag | Address | Every keystroke | Known issue - type slowly | 2025-08 |
| Sync fails | All text fields | >5MB total | Reduce content or split forms | 2025-08 |
| Form freezes | All fields | >50 total fields | Implement pagination | 2025-08 |
| Memory exhaustion | RichText | Frequent toggling | Avoid conditional visibility | 2025-08 |

### When Input Issues Occur

| Symptom | Field Type | Context | Solution | Version |
|---------|------------|---------|----------|---------|
| Cannot type value | QRCodeFormField | Any platform | No text input - add TextField | 2025-08 |
| Cannot type value | RichText | Any platform | Display-only - working as designed | 2025-08 |
| Cannot edit template | TemplatedString | Any platform | Read-only - edit source fields | 2025-08 |
| Voice input fails | Email | Android | @ symbol issue - type manually | 2025-08 |
| Voice creates run-on text | MultilineText | Mobile | Add punctuation manually | 2025-08 |
| Data disappears | Address | Fast typing | Race condition - pause 500ms | 2025-08 |
| Space bar hidden | Email | Mobile keyboard | Known issue - use @ key | 2025-08 |
| Auto-caps unwanted | TextField | iOS | Configure autocapitalize attribute | 2025-08 |
| Scanner won't start | QRCodeFormField | First use | Grant camera permission | 2025-08 |
| Permission stuck | QRCodeFormField | After denial | Settings > Apps > Camera > Enable | 2025-08 |

### When Security Issues Occur

| Symptom | Field Type | Risk | Mitigation | Version |
|---------|------------|------|------------|---------|
| XSS vulnerability | TemplatedString | HTML injection | Never include user text fields | 2025-08 |
| Script in template | TemplatedString | Code execution | HTML escaping disabled - sanitize | 2025-08 |
| Malicious barcode | QRCodeFormField | No validation | Add pattern validation to paired field | 2025-08 |
| External content blocked | RichText | Not a bug | Security feature - use Base64 | 2025-08 |
| SQL injection risk | All text inputs | Backend vulnerability | Implement backend validation | 2025-08 |
| Data exposure | Email | Privacy concern | Add retention policy notice | 2025-08 |

---

## Field Interaction Matrix (2025-08) {important}

### Critical Incompatibilities
- `BREAKS` QRCodeFormField + Required validation = Web forms become permanently unsubmittable
- `BREAKS` Multiple RichText (>10) + Mobile = Memory leak accumulation causes app crash
- `BREAKS` TemplatedString referencing another TemplatedString = Circular reference error, silent failure
- `BREAKS` RichText with conditional visibility + Frequent toggling = Memory accumulation crash
- `BREAKS` Address field + Rapid tabbing = Race condition data loss
- `BREAKS` QRCodeFormField + Web platform = Complete functionality loss, disabled interface
- `VERSION` 2025-08

### Required Pairings
- `REQUIRED` Every notebook MUST have at least one TemplatedString configured as hridField
- `REQUIRED` QRCodeFormField MUST pair with TextField for web platform fallback
- `REQUIRED` TemplatedString MUST be in same form as all referenced fields
- `RECOMMENDED` Address field should pair with annotation field for access notes
- `RECOMMENDED` Email field should pair with privacy notice (RichText)
- `VERSION` 2025-08

### Data Type Interactions
- `FORMAT` TemplatedString + BasicAutoIncrementer = String format "0001" not number
- `FORMAT` TemplatedString + Select/RadioGroup = Uses value not label in template
- `FORMAT` TemplatedString + MultiSelect = Shows comma-separated values
- `FORMAT` TemplatedString + Checkbox = String "true"/"false" not boolean
- `FORMAT` TemplatedString + TakePhoto/FileUploader = Shows "[object Blob]" - use only for conditionals
- `FORMAT` TemplatedString + RelationshipField = Shows "[object Object]" - use only for conditionals
- `FORMAT` TemplatedString + Address = Shows full JSON string - requires post-processing
- `FORMAT` TemplatedString + DateTimeField = ISO 8601 format string
- `VERSION` 2025-08

### Platform-Specific Combinations
- `MOBILE-ONLY` QRCodeFormField functional only on iOS/Android
- `WEB-ISSUE` RichText + Tables = Tables stripped at runtime despite Designer support
- `WEB-ISSUE` RichText + External images = Blocked by hardcoded empty whitelist
- `PERFORMANCE` Multiple TemplatedStrings (>3) = Form evaluation lag on all platforms
- `PERFORMANCE` TextField + MultilineText (>30 total) = Form lag begins
- `PERFORMANCE` RichText (>1000 total words) + Mobile = Critical performance impact
- `MOBILE-ISSUE` Email keyboard + Voice input = @ symbol recognition failure
- `MOBILE-ISSUE` TextField predictive text + Short forms = Keyboard covers fields
- `VERSION` 2025-08

### Validation Cascades
- `CASCADE` Required TemplatedString + Empty referenced field = Form submission blocked
- `CASCADE` Required QRCodeFormField on web = Form permanently invalid
- `CASCADE` Pattern validation on TemplatedString = Validates output not template
- `CASCADE` Email validation + Institution formats = May reject valid institutional addresses
- `CASCADE` Address validation + Every keystroke = Performance impact
- `VERSION` 2025-08

### Export Interactions
- `EXPORT` Address in CSV = Complete JSON in single column, requires post-processing
- `EXPORT` MultilineText in CSV = Line breaks may require specific reader settings
- `EXPORT` TemplatedString = Exports generated value, not template
- `EXPORT` RichText = Never exported, content only in notebook definition
- `EXPORT` TextField > 254 chars in Shapefile = Data truncation
- `VERSION` 2025-08

---

## Migration Warnings Index (2025-08) {essential}

### Safe Migrations (No Data Loss)
- `SAFE` TextField → MultilineText when all existing content <10,000 chars
- `SAFE` TextField → FAIMSTextField variant (enhanced help features)
- `SAFE` Adding optional fields to existing forms
- `SAFE` Increasing MultilineText row count (display only)
- `SAFE` Adding helperText to any field
- `SAFE` Removing pattern validation (makes validation less strict)
- `SAFE` Adding TemplatedString as new hridField (doesn't affect existing records)
- `VERSION` 2025-08

### Breaking Changes (Data Loss or Corruption Risk)
- `BREAKS` String type → Number type = Existing string data becomes invalid
- `BREAKS` Adding required validation to populated field = Blocks editing existing records
- `BREAKS` Changing field name/id = Orphans all existing data
- `BREAKS` TextField → Email with strict validation = May invalidate existing entries
- `BREAKS` Removing hridField designation = Records become UUID-only, unidentifiable
- `BREAKS` QRCodeFormField → Any other type = No migration path exists
- `BREAKS` Any field → QRCodeFormField = Manual data cannot be migrated
- `BREAKS` Adding pattern validation to populated field = May invalidate existing data
- `BREAKS` MultilineText → TextField with data >50 chars = Display issues, possible truncation
- `BREAKS` Changing TemplatedString template = New format only for new records
- `BREAKS` Component namespace change = Complete field incompatibility
- `VERSION` 2025-08

### Conditional Migrations (Context Dependent)
- `CONDITIONAL` MultilineText → TextField = Safe only if ALL content <50 characters
- `CONDITIONAL` Changing validation patterns = Safe if all existing data passes new pattern
- `CONDITIONAL` Address field restructuring = Requires JSON transformation scripts
- `CONDITIONAL` Email validation tightening = Test against all institutional formats first
- `CONDITIONAL` Adding character limits = Safe if no existing data exceeds limit
- `CONDITIONAL` TextField type="text" → type="email" = Safe if all entries are valid emails
- `CONDITIONAL` Removing fields from TemplatedString = Safe but changes future HRIDs
- `CONDITIONAL` Adding fields to TemplatedString = Only affects new records
- `VERSION` 2025-08

---

## Error Message Quick Reference (2025-08) {important}

### Critical Errors (Form Breaking)

| Error Message | Field Type(s) | Root Cause | Quick Fix | Prevention |
|---------------|---------------|------------|-----------|------------|
| "Maximum call stack size exceeded" | TemplatedString | Circular template reference | Remove circular refs between templates | Never reference other TemplatedStrings |
| "Form cannot be submitted" | QRCodeFormField | Required validation on web platform | Remove ["yup.required"] from schema | Never mark QRCodeFormField as required |
| "Cannot read property 'length' of null" | TextField, MultipleTextField, Email | initialValue is null instead of string | Change to initialValue: "" | Always use "" for string-type fields |
| "Cannot read property 'address' of undefined" | Address | initialValue is "" or undefined | Change to initialValue: null | Always use null for Address fields |
| "yup.required is not a function" | All fields | Validation schema wrong order | Put ["yup.string"] before ["yup.required"] | Type declaration must come first |
| "Component not found" | All fields | Wrong component name | Check exact component name | Reference documentation for names |
| "Memory quota exceeded" | RichText | >10 fields or >1000 words total | Reduce RichText count/content | Monitor total RichText usage |
| "IndexedDB quota exceeded" | TakePhoto, FileUploader | Storage full | Clear app cache or delete records | Monitor device storage |
| "UI Spec had an undefined field" | All fields | Field ID doesn't exist | Create field or remove from section | Validate all field references |

### Validation Errors (User Facing)

| Error Message | Field Type(s) | Root Cause | Quick Fix | Prevention |
|---------------|---------------|------------|-----------|------------|
| "Field is required" | All input fields | Empty required field | Fill in the field | Clear labeling of required fields |
| "Invalid email" or "Invalid email format" | Email | Missing @ or malformed | Check for spaces and format | Provide format example in helper |
| "Must be 3 capital letters" | TextField | Pattern mismatch | Match specified regex | Show pattern example in placeholder |
| "Minimum N characters" | TextField, MultipleTextField | Content too brief | Add more content | Set realistic minimums |
| "Maximum N characters" | TextField, MultipleTextField | Content too long | Reduce content | Display character counter |
| "At least one photo required" | TakePhoto | Empty photo array | Capture at least one photo | Clear requirement in label |
| "Invalid format" | TextField, Email | Regex pattern failure | Match expected pattern | Document pattern in helperText |

### Component Errors (Configuration)

| Error Message | Field Type(s) | Root Cause | Quick Fix | Prevention |
|---------------|---------------|------------|-----------|------------|
| "Unknown component MultilineTextField" | MultilineText | Wrong component name | Use "MultipleTextField" | Check documentation |
| "Component EmailField not found" | Email | No EmailField component exists | Use TextField with type="email" | Email is TextField variant |
| "Component FAIMSTextField not found" | TextField | Wrong namespace | Use namespace: "faims-custom" | Match namespace to component |
| "LocationPermissionIssue" (wrong error) | TakePhoto | Shows location instead of camera error | Known bug - ignore message | Grant camera permission |

### Display Errors (Visual Issues)

| Error Message | Field Type(s) | Root Cause | Quick Fix | Prevention |
|---------------|---------------|------------|-----------|------------|
| "[object Object]" | TemplatedString | Complex field in template | Use conditionals {{#field}} only | Document field return types |
| "[object Blob]" | TemplatedString | File/photo field in template | Use for existence check only | Mark binary fields clearly |
| "Unknown User" | TemplatedString | System variable is null | Check _CREATOR_NAME exists | Handle null in template |
| "Unknown Time" | TemplatedString | System variable is null | Check _CREATED_TIME exists | Provide fallback values |
| "Error" (literal text) | RichText | Invalid markdown syntax | Fix markdown in Designer | Validate markdown syntax |

### Silent Failures (No Error Message Shown)

| Symptom (No Error) | Field Type(s) | Root Cause | Quick Fix | Prevention |
|--------------------|---------------|------------|-----------|------------|
| Template shows {{field}} literally | TemplatedString | Field doesn't exist | Check field name spelling | Validate all references |
| Red field, no text | RadioGroup, Select, others (14 types) | Missing error display component | Known bug - check console | Manual validation check |
| Scanner never completes | QRCodeFormField | Multiple barcodes or unstable | Isolate single barcode | Train proper scanning |
| Validation doesn't trigger | All fields | Field not "touched" | Focus then blur field | Explain validation timing |
| Address shows "Empty" with data | Address | Display issue with stored data | Check data structure | Test with sample data |
| Tables disappear | RichText | DOMPurify strips tables | Use lists or images instead | Document runtime limits |
| Images don't load | RichText | External URLs blocked | Use Base64 embedding | Only embed images <100KB |
| Form won't save (no error) | Any field | Hidden required field | Check all required fields | Avoid required on conditional |

---

## Metadata

**Documentation Version**: 2025-08-29 v0.2 
**Components**: TextField, MultipleTextField, TemplatedString, Email, Address, QRCodeFormField, RichText  
**Platform Version**: Fieldmark 2025  
**Last Updated**: August 2025  
**Status**: Complete consolidated, deduplicated, structured, and tagged documentation for all text input fields

### Component Status Summary
- **Production Ready**: TextField, MultipleTextField, TemplatedString
- **Stable Configuration**: Email (TextField variant)
- **Beta Feature**: Address (JSON storage complexity)
- **Mobile-Only**: QRCodeFormField (platform limitations)
- **Display-Only**: RichText (no data capture, memory issues)

### Quality Verification
- ✔ All 7 fields documented completely with keywords
- ✔ Every section has appropriate depth tags
- ✔ Security warnings prominent at top
- ✔ Platform limitations clearly marked
- ✔ Beta status noted for Address field
- ✔ Structure matches template exactly
- ✔ Common characteristics properly tagged
- ✔ All field names tagged {essential}
- ✔ Keywords added for each field (3-5 terms)
- ✔ No content lost during restructuring
- ✔ Clear navigation with depth indicators
- ✔ Testing guidelines tagged {comprehensive}
- ✔ Designer disambiguation complete

### Revision History
- **v0.1**: Initial consolidated documentation with Designer disambiguation
- **v0.2**: Added migration patterns and training requirements (2025-08)