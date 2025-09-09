# Email Field

## Overview

The Email field represents a specialised configuration of the TextField component, optimised for electronic mail address capture through the application of email-specific input attributes and validation constraints. Whilst not a distinct component within the Fieldmark architecture, this field type leverages HTML5 email input capabilities combined with Yup's email validation patterns to ensure data quality at the point of entry. The implementation accepts common email formats with permissive validation, rejecting only clearly malformed addresses whilst accommodating contemporary addressing conventions including subdomains and plus-addressing schemes.

## Common Use Cases

- **Team member contacts**: Recording email addresses for project personnel, collaborators, and stakeholders
- **Institutional correspondence**: Capturing official contact points for organisations, museums, or government agencies
- **Data management contacts**: Documenting responsible parties for data access requests and long-term stewardship
- **Participant information**: Recording contact details for survey respondents or research participants (with appropriate consent)
- **Alert notifications**: Collecting addresses for automated system notifications or report distribution
- **Administrative metadata**: Preserving contact information for permit holders, landowners, or regulatory authorities

## Core Configuration

### Required Properties
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

### Optional Properties
```json
{
  "component-parameters": {
    "helperText": "Enter a valid email address",
    "placeholder": "user@example.com",
    "required": false,
    "fullWidth": true,
    "variant": "outlined",
    "disabled": false
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.email", "Enter a valid email address"]
  ],
  "initialValue": "",
  "meta": {
    "annotation": {"include": false, "label": "annotation"},
    "uncertainty": {"include": false, "label": "uncertainty"}
  }
}
```

### Property Specifications

#### Required Properties
- **component-namespace** (`string`): Must be "formik-material-ui"
- **component-name** (`string`): Always "TextField" (not a separate component)
- **type-returned** (`string`): "faims-core::Email" for semantic clarity
- **InputProps.type** (`string`): Must be "email" to trigger appropriate behaviour
- **name** (`string`): Unique field identifier
- **label** (`string`): Human-readable label for the field

#### Optional Properties
- **helperText** (`string`): Guidance text, typically "Enter a valid email address"
- **placeholder** (`string`): Example format shown in empty field
- **required** (`boolean`): Enforces non-empty submission
- **fullWidth** (`boolean`): Expands to container width
- **variant** (`string`): Visual style – "outlined", "filled", or "standard"

## Validation Rules

### Built-in Validation
- **HTML5 email validation**: Browser-native format checking via type="email"
- **Yup email validation**: Pattern matching for common email formats
- **Permissive acceptance**: Validates most real-world email addresses
- **Touched-first display**: Errors appear only after field interaction

### Configurable Validation
| Rule | Schema | Purpose | Error Message |
|------|--------|---------|---------------|
| required | `["yup.required", "Email is required"]` | Mandatory field | "Email is required" |
| email format | `["yup.email", "Enter a valid email"]` | Format validation | "Enter a valid email" |
| string type | `["yup.string"]` | Type enforcement | Type error (rare) |

### Accepted Email Formats
The Yup 0.28.3 implementation accepts:
- **Standard format**: user@domain.com
- **Plus addressing**: user+tag@domain.com (Gmail-style filtering)
- **Dots in username**: first.last@domain.com
- **Underscores**: user_name@domain.com
- **Hyphens**: user-name@domain-name.com
- **Subdomains**: user@mail.company.com
- **Numeric elements**: user123@domain.com or 123@domain.com

### Rejected Email Formats
- Missing @ symbol or domain
- Spaces within address components
- Double @ symbols
- Leading/trailing dots in any component
- Missing top-level domain (.com, .org, etc.)

### Error Messages
| Validation State | Message | User Action | Visual Indication |
|-----------------|---------|-------------|-------------------|
| Empty required | "Email is required" | Enter any email | Red border and text |
| Invalid format | "Enter a valid email" | Check @ and domain | Red border and text |
| Missing @ | "Enter a valid email" | Add @ and domain | Red border and text |
| Valid format | (none) | Continue | Normal appearance |

## Display Behaviour

### Desktop Rendering
- **Input type**: HTML5 email input field
- **Browser enhancements**: Some browsers display envelope icon
- **Autocomplete**: Browser may suggest previously entered emails
- **Validation**: Native browser validation supplements Yup validation
- **Error display**: Red border and helper text for invalid formats

### Mobile Rendering
#### iOS Behaviour
- **Keyboard layout**: Email-optimised with prominent @ key
- **Domain shortcuts**: Quick access to .com, .org, .net keys
- **Auto-capitalisation**: Disabled for email fields
- **Auto-correction**: Disabled to prevent email mangling
- **Predictive text**: Disabled for email addresses

#### Android Behaviour
- **Keyboard type**: Email layout with accessible @ symbol
- **No spaces**: Space bar often disabled or hidden
- **Voice input**: Available but may struggle with @ symbol
- **Domain completion**: Some keyboards offer domain suggestions
- **Auto-correction**: Typically disabled for email type

### Responsive Considerations
- Full width recommended to accommodate longer email addresses
- Minimum 16px font size prevents iOS zoom on focus
- Clear error messages positioned below field
- Touch target maintains 44×44px minimum

## Interaction Patterns

### User Input Methods
- **Direct typing**: Primary input method with email-optimised keyboard
- **Paste operations**: Full support for clipboard content
- **Browser autocomplete**: Previously entered emails may be suggested
- **Voice input**: Platform-dependent, may struggle with special characters
- **No contact integration**: Does not access device contacts

### Validation Timing
- **On mount**: No initial validation display
- **On change**: Validates after each keystroke once touched
- **On blur**: Field becomes touched, enabling error display
- **On submit**: Final validation before form submission

### State Transitions
- **Pristine**: No interaction, no errors shown
- **Focused**: Email keyboard activated on mobile
- **Touched + Invalid**: Red border and error message
- **Touched + Valid**: Normal appearance, ready for submission

## Conditional Logic Support

Email fields support standard conditional logic:

```json
{
  "condition": {
    "operator": "is_not",
    "field": "contact-preference",
    "value": "no-contact"
  }
}
```

Can serve as controller for dependent fields:
```json
{
  "condition": {
    "operator": "matches",
    "field": "researcher-email",
    "value": "@university.edu$"
  }
}
```

## Data Storage and Export

### Internal Storage
- **Type**: Stored as UTF-8 string
- **Case preservation**: Maintains case as entered (no auto-lowercase)
- **Trimming**: Leading/trailing whitespace removed
- **Single value**: No array support for multiple emails

### Export Formats
- **CSV**: Quoted if contains commas
- **JSON**: String value, case preserved
- **Database**: Stored as varchar/text
- **No normalisation**: Export maintains original capitalisation

### Limitations
- **Single email only**: No comma-separated multiple emails
- **No verification**: Validity not verified beyond format
- **No uniqueness checking**: Duplicates not prevented

## Common Patterns

### Pattern: Required Contact Email
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

### Pattern: Optional Notification Email
```json
{
  "notification-email": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::Email",
    "component-parameters": {
      "label": "Notification Email (Optional)",
      "name": "notification-email",
      "placeholder": "Leave blank if no notifications needed",
      "required": false,
      "InputProps": {
        "type": "email"
      }
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.email", "If provided, must be valid"]
    ],
    "initialValue": ""
  }
}
```

## Troubleshooting Guide

### Common Issues

#### Email validation too strict
**Cause**: Valid edge-case emails rejected  
**Solution**: Yup validation is actually permissive; check for spaces or missing components

#### Plus addresses rejected
**Cause**: Misconception about validation  
**Solution**: Plus addressing (user+tag@domain.com) is supported; check for other issues

#### Keyboard doesn't show @ symbol
**Cause**: InputProps.type not set to "email"  
**Solution**: Ensure configuration includes `"InputProps": {"type": "email"}`

#### Cannot enter multiple emails
**Cause**: Field designed for single email only  
**Solution**: Create separate fields for additional emails or implement custom solution

#### Autocomplete not working
**Cause**: Browser autocomplete disabled or no previous emails  
**Solution**: Email field relies on browser defaults; cannot force autocomplete

### Platform-Specific Issues

#### iOS: Capital letters appearing
Verify InputProps includes type="email" which should disable auto-capitalisation

#### Android: Space bar visible
Confirm type="email" is set; some keyboards may still show space but it typically won't input

#### Desktop: Browser validation conflicts
Browser validation supplements Yup validation; both must pass

### Debug Checklist
- [ ] InputProps.type set to "email"
- [ ] Component-name is "TextField" not "EmailField"
- [ ] Validation includes ["yup.email"] schema
- [ ] Type-returned is "faims-core::Email"
- [ ] No spaces in email validation test
- [ ] Field name unique in notebook

## Implementation Notes

### Technical Architecture
The Email field is not a distinct component but rather a TextField with email-specific configuration. This design pattern reduces code duplication whilst maintaining consistent behaviour across text input variants. The configuration-based approach allows future enhancements without component proliferation.

### Limitations and Constraints
- **No multiple emails**: Array input not supported; requires multiple fields
- **No domain restrictions**: Cannot limit to specific domains without custom validation
- **No contact integration**: Does not access device contact lists
- **No verification**: Format validation only, not deliverability
- **No auto-lowercase**: Case preserved as entered
- **No duplicate checking**: Same email can be entered multiple times

### Future Enhancement Opportunities
Potential improvements requiring custom implementation:
- Domain allowlists/blocklists for institutional requirements
- Multiple email input with chip display
- Integration with contact APIs
- Real-time deliverability verification
- Automatic normalisation options

## Best Practices

- Provide clear helper text indicating email purpose
- Use placeholder sparingly to avoid confusion with actual values
- Consider privacy implications when collecting email addresses
- Document retention policies for contact information
- Test email validation with institution-specific formats
- Avoid assuming single email per person (though field limits to one)
- Include data protection notices where appropriate

## See Also

- **TextField**: Base component providing email field functionality
- **MultilineTextField**: For longer text content
- **TemplatedStringField**: For generating email addresses programmatically
- **Select**: When email should be chosen from predefined list
- **Relationship Field**: For linking to contact records with multiple fields

---

*The Email field provides essential contact information capture through a specialised TextField configuration, balancing validation stringency with real-world email format diversity whilst acknowledging its limitations for advanced email handling scenarios.*