# Address Field

**Component**: `AddressField`  
**Status**: Beta Feature  
**Type Returned**: `faims-core::JSON`  
**Namespace**: `faims-custom`

## Overview

The Address field provides structured address capture through a specialised interface storing data in GeocodeJSON-compliant format, facilitating both human-readable display and future geocoding integration. Developed to specification for anchor client requirements, this beta feature implements dual storage – maintaining both structured components and concatenated display strings within a JSON object. Whilst currently optimised for Australian address formats with technical users comfortable with JSON data extraction, the architecture anticipates international expansion and enhanced analytical capabilities.

The field's sophisticated storage pattern preserves granular address components whilst automatically generating formatted display text, enabling projects that require both structured data analysis and consistent presentation formats. Heritage organisations with technical capacity benefit from the GeocodeJSON compliance that positions their data for future spatial analysis workflows.

## Common Use Cases

- **Institutional addresses**: Museums, archives, and heritage organisations with consistent street addresses
- **Site access points**: Recording formal entry addresses for heritage sites with conventional street access
- **Contact management**: Structured storage of stakeholder addresses for correspondence and mapping
- **Regional analysis preparation**: Capturing addresses in a format suitable for post-processing geocoding workflows
- **Compliance documentation**: Meeting requirements for structured address data in government systems
- **Data migration projects**: Standardising legacy address data into consistent JSON structures

## Core Configuration

### Required Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `component-namespace` | string | Must be `"faims-custom"` | `"faims-custom"` |
| `component-name` | string | Must be `"AddressField"` | `"AddressField"` |
| `name` | string | Internal field identifier | `"site-address"` |
| `type-returned` | string | Must be `"faims-core::JSON"` | `"faims-core::JSON"` |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `label` | string | `""` | Display label above field |
| `helperText` | string | `""` | Guidance text below field |
| `required` | boolean | `false` | Whether field completion is mandatory |
| `fullWidth` | boolean | `false` | Expand to container width |
| `meta.annotation` | object | `null` | Enable annotation capability |
| `meta.uncertainty` | object | `null` | Enable uncertainty flags |
| `initialValue` | object/null | `null` | Pre-populated address data |

## Validation Rules

| Validation Type | Implementation | Behaviour | Error Message |
|----------------|----------------|-----------|---------------|
| Required Field | `required: true` | Checks if JSON object exists | "This field is required" |
| Type Validation | `[['yup.object'], ['yup.nullable']]` | Ensures value is object or null | "Invalid address format" |
| Component Validation | Not implemented | All subfields optional | N/A |
| Length Limits | Not implemented | Unlimited text in all fields | N/A |
| Format Validation | Not implemented | Any string accepted in any field | N/A |

**Note**: The Address field currently implements minimal validation, accepting any text in any component field. Projects requiring specific validation patterns should consider using separate TextField components with individual validation rules.

## Display Behaviour

### Desktop Presentation
- **Collapsed state**: Shows display name or "Empty" placeholder with edit icon
- **Expanded state**: Vertical stack of five text fields with full keyboard navigation
- **Edit icon**: Positioned right, standard click target size
- **Field width**: Respects fullWidth parameter or container constraints

### Mobile iOS
- **Touch targets**: Edit button requires precise tapping (accessibility consideration)
- **Auto-capitalisation**: Applies to all fields including state abbreviations
- **Keyboard**: Standard text keyboard for all fields including postcode
- **Scrolling**: Expanded form may require vertical scrolling on smaller devices

### Mobile Android
- **Keyboard behaviour**: Text keyboard persists across all fields
- **Autofill**: Currently unsupported due to missing semantic attributes
- **Input latency**: Validation on keystroke may cause lag on older devices
- **Field focus**: Maintained during expansion/collapse transitions

## Interaction Patterns

### Standard Workflow
1. User encounters collapsed field showing current value or empty state
2. Clicks/taps edit icon to expand input interface
3. Enters data across five fields in any order:
   - House Number (optional)
   - Street Name (optional)
   - Suburb (optional)
   - State (optional)
   - Postcode (optional)
4. System generates display name from populated fields
5. Field collapses on blur or manual collapse

### Partial Completion
The field supports incomplete addresses through intelligent concatenation:
- Only populated fields appear in display name
- Empty fields are filtered from concatenation
- No requirement for specific field combinations
- Suitable for unconventional locations (e.g., "5km north of township")

### Rapid Entry Considerations
**Warning**: Rapid tabbing between fields may trigger race conditions. Users should allow brief pauses between field changes to ensure data persistence.

## Conditional Logic Support

The Address field participates in conditional logic as both trigger and target:

### As Trigger
```javascript
// Show heritage assessment if address contains specific suburb
"conditional_source": "site-address",
"condition": "contains",
"value": "Parramatta"
```

### As Target
```javascript
// Hide address field for remote sites
"conditional_target": "site-address",
"condition": "!=",
"source_field": "site-type",
"value": "remote"
```

**Note**: Conditional logic evaluates against the entire JSON object, not individual components.

## Data Storage and Export

### Storage Format
The field stores a nested JSON object with dual representation:
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

### CSV Export Behaviour
**Critical Note**: Address data exports as a single column containing the complete JSON structure:
```csv
site_address
"{""display_name"":""123 Main St, Parramatta, NSW, 2150"",""address"":{""house_number"":""123"",""road"":""Main St"",""suburb"":""Parramatta"",""state"":""NSW"",""postcode"":""2150""}}"
```

### Data Extraction Requirements
Post-processing requires JSON parsing to extract components:
```python
import pandas as pd
import json

df = pd.read_csv('export.csv')
df['address_data'] = df['site_address'].apply(json.loads)
df['postcode'] = df['address_data'].apply(lambda x: x['address']['postcode'])
df['suburb'] = df['address_data'].apply(lambda x: x['address']['suburb'])
```

## Common Patterns

### Pattern 1: Australian Heritage Site
```json
{
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
```

### Pattern 2: Museum/Institution Address
```json
{
  "component-namespace": "faims-custom",
  "component-name": "AddressField",
  "type-returned": "faims-core::JSON",
  "component-parameters": {
    "label": "Institution Address",
    "name": "institution-address",
    "helperText": "Repository or museum street address",
    "required": true,
    "fullWidth": true
  },
  "validationSchema": [["yup.object"], ["yup.required", "Institution address required"]],
  "initialValue": {
    "display_name": "",
    "address": {
      "state": "NSW"
    }
  }
}
```

### Pattern 3: International Project Workaround
```json
{
  "site-address": {
    "component-namespace": "faims-custom",
    "component-name": "AddressField",
    "type-returned": "faims-core::JSON",
    "component-parameters": {
      "label": "Site Address",
      "name": "site-address",
      "helperText": "Street address (add country in separate field below)",
      "fullWidth": true
    },
    "validationSchema": [["yup.object"], ["yup.nullable"]],
    "initialValue": null
  },
  "site-country": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Country",
      "name": "site-country",
      "helperText": "Project country for international sites",
      "required": true
    },
    "validationSchema": [["yup.string"], ["yup.required", "Country required"]],
    "initialValue": ""
  }
}
```

### Pattern 4: Remote Site Description
```json
{
  "component-namespace": "faims-custom",
  "component-name": "AddressField",
  "type-returned": "faims-core::JSON",
  "component-parameters": {
    "label": "Location Reference",
    "name": "location-reference",
    "helperText": "Use Street Name field for descriptions like '5km north of township'",
    "fullWidth": true
  },
  "validationSchema": [["yup.object"], ["yup.nullable"]],
  "initialValue": null,
  "meta": {
    "annotation": {
      "include": true,
      "label": "Location finding notes"
    }
  }
}
```

## Troubleshooting Guide

### Issue: Address Data Lost During Rapid Entry
**Symptoms**: Entered data disappears when quickly tabbing between fields  
**Cause**: Race condition in state updates during rapid editing  
**Solution**: 
- Allow 500ms pause between field entries
- Use Tab key rather than mouse clicking
- Save form frequently during data entry
- Consider using separate TextField components for critical data

### Issue: Cannot Enter Country Information
**Symptoms**: No country field visible in interface  
**Cause**: Current UI only exposes five of nine data model fields  
**Solution**:
- Add separate TextField for country (see Pattern 3)
- Include country in State field as temporary workaround
- Note limitation in project documentation

### Issue: CSV Export Shows JSON Instead of Columns
**Symptoms**: Address data appears as complex JSON string in single column  
**Cause**: Address field stores structured JSON without flattening  
**Solution**:
- Use Python/R script for extraction (see Data Storage section)
- Consider separate TextField components if Excel analysis required
- Train team in JSON extraction techniques
- Document extraction workflow in project materials

### Issue: Mobile Postcode Entry Inefficient
**Symptoms**: Text keyboard appears for numeric postcode entry  
**Cause**: Missing inputMode attribute on postcode field  
**Solution**:
- Switch manually to numeric keyboard
- Enter postcodes on desktop when possible
- Copy-paste from notes app with numeric keyboard
- Report as feature request for improvement

### Issue: Display Name Shows 'undefined'
**Symptoms**: Undefined values appear in concatenated display  
**Cause**: Null handling issue in display generation  
**Solution**:
- Ensure all fields either have values or are completely empty
- Avoid entering spaces in empty fields
- Clear and re-enter address if issue persists

## Implementation Notes

### Technical Architecture
- **Component**: Custom React component using Material-UI TextField elements
- **State Management**: Local useState with Formik integration
- **Storage Type**: `faims-core::JSON` with GeocodeJSON-inspired structure
- **Validation**: Minimal validation through Yup schema (object type only)
- **Display Generation**: Automatic concatenation with comma separation

### Data Model vs UI Divergence
The underlying data model supports nine fields:
- house_number, road, town, suburb, municipality, state, postcode, country, country_code

However, the current UI only exposes five:
- house_number, road, suburb, state, postcode

This divergence anticipates future internationalisation whilst meeting current client requirements.

### Performance Considerations
- Form validation triggers on every keystroke
- Deep cloning occurs during updates (memory consideration)
- Large addresses increase JSON payload size
- No character limits may impact database performance

### Beta Feature Status
This field represents commissioned functionality meeting specific client requirements. The current implementation prioritises structured data capture over analytical convenience, with the understanding that technical users can extract required components through post-processing.

## Best Practices

### For Australian Projects
- Leverage the optimised Australian format as designed
- Use annotation fields for access notes and alternatives
- Standardise state abbreviations (NSW, VIC, QLD) for consistency
- Include postcode for all addresses to enable regional analysis

### For International Projects
- Add separate country TextField as standard practice
- Document country codes in project guidelines
- Consider using entirely separate TextFields for maximum flexibility
- Establish clear data entry conventions for team consistency

### For Remote Sites
- Utilise the Street Name field for descriptive locations
- Leave house number empty for non-street locations
- Use annotation field for detailed finding instructions
- Consider pairing with TakePoint field for GPS coordinates

### For Data Analysis Projects
- Document JSON extraction workflow before data collection
- Train team in Python/R extraction techniques
- Consider separate TextField components if programming expertise unavailable
- Plan for post-processing time in project schedules

### For High-Volume Data Entry
- Enter data deliberately to avoid race conditions
- Use desktop platforms when possible for efficiency
- Implement regular save routines
- Consider bulk import via JSON if available

## Feature Requests and Roadmap

### Priority Enhancements
1. **Country selector**: Dropdown or text field for country selection
2. **CSV export flattening**: Automatic column separation for address components
3. **Validation options**: Configurable validation for postcodes and required fields
4. **Address autocompletion**: Integration with geocoding services
5. **Numeric keyboard**: Automatic numeric input for postcode field

### Internationalisation Features
- Configurable address formats by country
- Dynamic field labels based on locale
- RTL language support for Arabic/Hebrew addresses
- International postcode validation patterns

### Analytical Improvements
- Built-in geocoding to coordinates
- Address verification against postal databases
- Duplicate address detection
- Bulk address standardisation tools

### Accessibility Enhancements
- Improved touch targets for mobile edit button
- ARIA labels for screen readers
- Keyboard shortcuts for expansion/collapse
- Autofill semantic attributes

## See Also

- **TextField**: Alternative for simple address storage or validated components
- **MultilineTextField**: For free-text address descriptions
- **TakePoint**: For GPS coordinate capture alongside addresses
- **Select**: For choosing from predefined address lists
- **TemplatedStringField**: For generating formatted address labels
- **Relationship Field**: For linking to separate address entities

---

*The Address field provides structured address capture optimised for Australian formats and technical users, with clear pathways for international adaptation and future enhancement. Projects should assess whether JSON post-processing capabilities align with team expertise before deployment.*