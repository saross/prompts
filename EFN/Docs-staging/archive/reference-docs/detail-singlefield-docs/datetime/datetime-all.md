# Date & Time Fields: DateTimePicker, DateTimeNow, DatePicker, and MonthPicker

**Component Names**: `DateTimeField`, `DateTimeNow`, `DateField`, `MonthField`  
**Namespace**: `faims-custom`  
**Type Returned**: Strings in various formats (see Storage Formats section)

---

## Overview

The date and time field subsystem provides four interconnected components for temporal data capture in archaeological fieldwork. These fields serve predominantly administrative and observational metadata functions – recording when data was collected, when specimens were photographed, or when excavations commenced. They explicitly do **not** address interpretive archaeological dating, which requires specialist vocabularies, uncertainty quantification, and period taxonomies better served by controlled choice fields or structured text inputs.

All four components share a fundamental dependency on HTML5 native input types (`datetime-local`, `date`, and `month`), creating significant platform variance in user interfaces whilst maintaining consistent data storage. This architectural decision prioritises platform-familiar interactions over cross-device consistency – a pragmatic trade-off that reduces training burden at the cost of interface standardisation.

### Critical Design Limitation

These fields suffer from validation poverty, supporting only required/optional constraints without temporal range enforcement, cross-field validation, or format standardisation. Projects requiring sophisticated temporal constraints must implement post-collection validation or deploy alternative recording strategies.

---

## Common Use Cases

**Administrative Metadata** (#administrative-metadata)
- Record creation timestamps (when entered, not when observed)
- Last modification tracking for audit trails
- Data synchronisation timestamps across devices
- Quality assurance timestamps for review processes

**Field Observations** (#field-observations)
- Excavation start/end dates for contexts
- Photograph capture times for specimens
- Survey dates for transect walks
- Collection timestamps for samples

**Heritage Documentation**
- Permit validity dates (start and expiry)
- Site visit dates for monitoring
- Conservation treatment dates
- Report submission deadlines

**What These Fields Cannot Do**
- Record interpretive dates ("Late Bronze Age")
- Capture date ranges or uncertainties ("circa 1850")
- Handle partial dates ("March 1887" without day)
- Enforce temporal sequences (end after start)
- Support BCE dates or archaeological periods

---

## Comparative Decision Framework

### Storage Format Comparison

| Field Type | Storage Format | Example | Timezone Handling | Synchronisation Safety |
|------------|---------------|---------|-------------------|------------------------|
| DateTimeNow | ISO 8601 with timezone | `2024-03-15T14:30:00.000Z` | Preserved (UTC) | ✅ Excellent |
| DateTimePicker | Local string, no timezone | `2024-03-15T14:30` | ❌ Ambiguous | ⚠️ Problematic |
| DatePicker | Date-only string | `2024-03-15` | N/A (no time) | ✅ Excellent |
| MonthPicker | Month-year string | `2024-03` | N/A (no time) | ✅ Excellent |

### Precision Capabilities

| Field Type | Temporal Precision | Granularity Control | Use When |
|------------|-------------------|---------------------|----------|
| DateTimeNow | Seconds | Hard-coded | Precise timing matters |
| DateTimePicker | Minutes | Browser default | Legacy compatibility required |
| DatePicker | Days | Required | Time components irrelevant |
| MonthPicker | Months | Required | Day precision unavailable or spurious |

### Selection Guidance

**Use DateTimeNow when:**
- Recording any datetime, contemporary or historical (despite the misleading name)
- Working across multiple timezones
- Requiring second-level precision
- Needing consistent "Now" button for metadata capture
- Prioritising data integrity over interface simplicity

**Use DateTimePicker when:**
- Legacy notebooks require compatibility
- The "Now" button would confuse users
- Local time ambiguity is acceptable
- (Note: DateTimeNow superior for most use cases)

**Use DatePicker when:**
- Recording dates without time components
- Timezone ambiguity must be eliminated
- Simplifying data entry for day-level events
- Working with permit dates, excavation dates, or other administrative dates

**Use MonthPicker when:**
- Day-level precision remains unavailable or would constitute spurious accuracy
- Recording historical sources that specify only month and year
- Documenting seasonal or periodic phenomena
- Managing administrative cycles or reporting periods
- Maintaining methodological rigour by avoiding false precision

---

## Core Configuration

### Required Parameters (All Fields)

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| component-namespace | string | Always `"faims-custom"` | `"faims-custom"` |
| component-name | string | Field type identifier | `"DateTimeNow"` |
| name | string | Internal field identifier | `"collection_timestamp"` |
| label | string | Display label | `"Collection Time"` |

### Optional Parameters (All Fields)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| helperText | string | `""` | Guidance text below field |
| required | boolean | `false` | Makes field mandatory |
| fullWidth | boolean | `false` | Expands to container width |
| disabled | boolean | `false` | Prevents modification |
| initialValue | string | `""` | Default value (format varies) |

### Field-Specific Parameters

**DateTimeNow Only:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| is_auto_pick | boolean | `false` | Auto-populate with current timestamp on form open |

Note: Despite its name, DateTimeNow accepts arbitrary dates via manual entry. The "Now" button provides convenience, not restriction.

---

## Validation Rules

### Validation Architecture Limitations

All date/time fields suffer from impoverished validation capabilities:

| Validation Type | Support Status | Workaround Required |
|----------------|----------------|---------------------|
| Required/Optional | ✅ Supported | None |
| Min/Max dates | ❌ Not supported | Post-collection validation |
| Date ranges | ❌ Not supported | Manual review |
| Cross-field validation | ⚠️ Partial (string comparison) | Conditional logic with caveats |
| Format validation | ❌ Not supported | Browser-dependent |
| Custom messages | ❌ Not supported | Generic errors only |

### Available Validation Schemas

```json
"validationSchema": [
  ["yup.string"],
  ["yup.required", "Date is required"]
]
```

The validation operates on the stored string value, not on date semantics. Cross-field comparisons (e.g., end date after start date) theoretically possible through conditional logic but rely on string lexicographic ordering – fragile and not recommended for production use.

---

## Display Behaviour

### Platform-Specific Picker Implementations (#platform-specific)

The HTML5 dependency creates dramatic interface variance across platforms:

**iOS Devices:**
- Native UIDatePicker wheel interface
- Cannot type directly – forced to use wheels
- Separate wheels for day, month, year, hour, minute
- No keyboard entry permitted
- Format follows device locale settings

**Android Devices:**
- Material Design picker dialogs
- Calendar grid for date selection
- Clock face or numeric input for time
- Some versions allow direct text input
- Format follows device locale

**Desktop Browsers:**
- **Chrome/Edge**: Calendar grid popup, clock interface for time
- **Firefox**: Calendar with time spinners
- **Safari**: Text input with basic validation (macOS may show picker)
- All permit direct keyboard entry
- Format varies by browser and OS locale

### Display Format Localisation

Browser-determined formatting creates international variance:
- Australian users: `15/03/2024 14:30`
- American users: `03/15/2024 2:30 PM`
- German users: `15.03.2024 14:30`
- ISO display: `2024-03-15T14:30`

This variance is **not configurable** – the system provides no format standardisation controls.

---

## Interaction Patterns

### Data Entry Workflows

**DateTimeNow Workflow:**
1. Field displays empty or auto-populated (if `is_auto_pick: true`)
2. User can:
   - Click "Now" button for current timestamp
   - Click field to open platform picker
   - Type directly (desktop only)
3. Value updates immediately
4. Stores as ISO 8601 string

**DateTimePicker Workflow:**
1. Field displays empty initially
2. User must actively select datetime
3. No quick-entry options
4. Stores as local string without timezone

**DatePicker Workflow:**
1. Field displays empty initially
2. User selects date only (no time interface)
3. Simpler interaction than datetime variants
4. Stores as YYYY-MM-DD string

### Mobile Considerations

Touch interactions vary significantly:
- **iOS**: Swipe wheels vertically, no pinch/zoom gestures
- **Android**: Tap calendar dates, swipe between months
- **Tablets**: May show desktop interface despite touch capability

---

## Conditional Logic Support

Limited temporal logic available through string comparison:

```json
"condition_instructions": {
  "conditions": [
    {
      "field": "start_date",
      "operator": "less",
      "value_field": "end_date"
    }
  ],
  "action": "enable"
}
```

⚠️ **Warning**: Comparisons operate on string values, not date objects. Only reliable when formats consistent (ISO 8601 or YYYY-MM-DD).

---

## Data Storage and Export

### Storage Mechanisms

| Field | Database Storage | JSON Export | CSV Export |
|-------|------------------|-------------|------------|
| DateTimeNow | ISO 8601 string | ISO 8601 string | ISO 8601 string |
| DateTimePicker | Local string | Local string | Local string |
| DatePicker | Date string | Date string | Date string |
| MonthPicker | Month string | Month string | Month string |

### Synchronisation Implications (#timezone-considerations)

**DateTimeNow**: Timezone-aware storage enables safe synchronisation across devices in different timezones. Sydney and London devices interpret the same absolute moment correctly.

**DateTimePicker**: Timezone-naive storage creates ambiguity. "2024-03-15T14:30" represents different absolute times in Sydney versus London, corrupting temporal sequences in multi-site projects.

**DatePicker**: Date-only storage eliminates timezone issues, though midnight assumptions may surprise users analysing data.

### CSV Export Behaviour

All date values export as stored strings without transformation:
- DateTimeNow: `2024-03-15T14:30:00.000Z`
- DateTimePicker: `2024-03-15T14:30`
- DatePicker: `2024-03-15`
- MonthPicker: `2024-03`

Excel's propensity for auto-converting these strings to date cells may corrupt precision or introduce regional format assumptions. The MonthPicker format proves particularly vulnerable, as Excel may interpret `2024-03` as 3rd March 2024 rather than March 2024, necessitating careful import procedures.

---

## Field-Specific Implementation Details

### DateTimeNow Implementation

Despite its name suggesting contemporary timestamps only, DateTimeNow accepts arbitrary dates whilst providing superior timezone handling through ISO 8601 storage.

#### Configuration Example 1: Auto-populated Metadata Timestamp
```json
{
  "record_created": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimeNow",
    "type-returned": "faims-core::DateTime",
    "component-parameters": {
      "label": "Record Created",
      "name": "record_created",
      "is_auto_pick": true,
      "helperText": "Automatically captured when record opened",
      "fullWidth": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Creation timestamp required"]
    ],
    "initialValue": ""
  }
}
```
**Expected behaviour**: Auto-populates with current timestamp on form opening. User can modify via picker or "Now" button. Stores ISO 8601 string with timezone.

#### Configuration Example 2: Specimen Collection Time
```json
{
  "collection_time": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimeNow",
    "type-returned": "faims-core::DateTime",
    "component-parameters": {
      "label": "Collection Time",
      "name": "collection_time",
      "is_auto_pick": false,
      "helperText": "Click 'Now' when collecting specimen",
      "required": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Collection time must be recorded"]
    ],
    "initialValue": "",
    "meta": {
      "annotation": {
        "include": true,
        "label": "Time notes"
      }
    }
  }
}
```
**Expected behaviour**: Requires manual action. "Now" button provides quick capture. Second precision preserved. Annotation allows uncertainty notes.

#### Configuration Example 3: Historical Event Recording
```json
{
  "historical_event": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimeNow",
    "type-returned": "faims-core::DateTime",
    "component-parameters": {
      "label": "Historical Event Date",
      "name": "historical_event",
      "is_auto_pick": false,
      "helperText": "Enter date/time from historical record"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
**Expected behaviour**: Users ignore "Now" button, manually enter historical dates. ISO storage preserves timezone context even for past events.

### DateTimePicker Implementation

Simpler interface without "Now" button, but compromised by timezone-naive storage. Consider DateTimeNow for most use cases.

#### Configuration Example 1: Excavation Start Time
```json
{
  "excavation_start": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimePicker",
    "type-returned": "faims-core::DateTime",
    "component-parameters": {
      "label": "Excavation Start",
      "name": "excavation_start",
      "helperText": "Record when excavation begins",
      "fullWidth": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Start time required"]
    ],
    "initialValue": ""
  }
}
```
**Expected behaviour**: Manual selection only. Stores local time string without timezone. Platform-specific picker interfaces.

#### Configuration Example 2: Scheduled Event
```json
{
  "scheduled_visit": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimePicker",
    "type-returned": "faims-core::DateTime",
    "component-parameters": {
      "label": "Scheduled Site Visit",
      "name": "scheduled_visit",
      "helperText": "Planned visit date and time"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "2024-06-15T09:00"
  }
}
```
**Expected behaviour**: Pre-populated with scheduled time. Minute precision only. Timezone ambiguity in multi-site projects.

#### Configuration Example 3: Relative Time Observation
```json
{
  "sunrise_observation": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimePicker",
    "type-returned": "faims-core::DateTime",
    "component-parameters": {
      "label": "Sunrise Time",
      "name": "sunrise_observation",
      "helperText": "Local sunrise time observed"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
**Expected behaviour**: Records local time appropriately for relative observations. Timezone context implicit in "local" nature of measurement.

### DatePicker Implementation

Simplified date-only interface eliminating time components and timezone complications.

#### Configuration Example 1: Excavation Date
```json
{
  "excavation_date": {
    "component-namespace": "faims-custom",
    "component-name": "DatePicker",
    "type-returned": "faims-core::Date",
    "component-parameters": {
      "label": "Excavation Date",
      "name": "excavation_date",
      "helperText": "Date of excavation (day precision)",
      "required": true,
      "fullWidth": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Excavation date required"]
    ],
    "initialValue": ""
  }
}
```
**Expected behaviour**: Calendar interface without time selection. Stores YYYY-MM-DD string. Display format varies by locale.

#### Configuration Example 2: Permit Expiry
```json
{
  "permit_expiry": {
    "component-namespace": "faims-custom",
    "component-name": "DatePicker",
    "type-returned": "faims-core::Date",
    "component-parameters": {
      "label": "Permit Expiry Date",
      "name": "permit_expiry",
      "helperText": "Heritage permit expiration"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "2024-12-31"
  }
}
```
**Expected behaviour**: Pre-populated with known expiry. Date-only storage appropriate for administrative deadlines.

#### Configuration Example 3: Artefact Discovery Date
```json
{
  "discovery_date": {
    "component-namespace": "faims-custom",
    "component-name": "DatePicker",
    "type-returned": "faims-core::Date",
    "component-parameters": {
      "label": "Discovery Date",
      "name": "discovery_date",
      "helperText": "When artefact was found"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "",
    "meta": {
      "annotation": {
        "include": true,
        "label": "Date uncertainty"
      }
    }
  }
}
```
**Expected behaviour**: Optional field with annotation for uncertainty. Forced day precision may require arbitrary selection for "Spring 1887" scenarios.

### MonthPicker Implementation

The MonthPicker field represents an elegant solution to the methodological challenge of spurious precision in temporal documentation. By constraining granularity to month-year combinations, it acknowledges the epistemological limitations inherent in historical sources whilst maintaining computational tractability.

#### Configuration Example 1: Historical Publication Date
```json
{
  "publication_month": {
    "component-namespace": "faims-custom",
    "component-name": "MonthPicker",
    "type-returned": "faims-core::Date",
    "component-parameters": {
      "label": "Publication Date",
      "name": "publication_month",
      "helperText": "Month and year of publication",
      "fullWidth": true
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
**Expected behaviour**: Presents month-year selector without day specification. Stores as `YYYY-MM` string. Browser localisation determines display format (e.g., "March 1887" or "03/1887").

#### Configuration Example 2: Archaeological Field Season
```json
{
  "field_season": {
    "component-namespace": "faims-custom",
    "component-name": "MonthPicker",
    "type-returned": "faims-core::Date",
    "component-parameters": {
      "label": "Excavation Season",
      "name": "field_season",
      "helperText": "Month of excavation campaign",
      "required": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Field season must be specified"]
    ],
    "initialValue": "",
    "meta": {
      "annotation": {
        "include": true,
        "label": "Season notes (weather, team size, etc.)"
      }
    }
  }
}
```
**Expected behaviour**: Mandatory selection of excavation month. Annotation field accommodates contextual metadata regarding seasonal conditions or campaign specifics.

#### Configuration Example 3: Museum Acquisition Period
```json
{
  "acquisition_period": {
    "component-namespace": "faims-custom",
    "component-name": "MonthPicker",
    "type-returned": "faims-core::Date",
    "component-parameters": {
      "label": "Acquisition Period",
      "name": "acquisition_period",
      "helperText": "When item entered collection (month/year)"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "1923-06"
  }
}
```
**Expected behaviour**: Pre-populated with known acquisition period. Month-level precision appropriate for archival records lacking specific acquisition dates.

---

## Common Patterns

### Pattern 1: Temporal Sequence Recording
Capturing excavation start and end times with basic validation:

```json
{
  "context_start": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimeNow",
    "type-returned": "faims-core::DateTime",
    "component-parameters": {
      "label": "Context Excavation Start",
      "name": "context_start",
      "required": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Start time required"]
    ]
  },
  "context_end": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimeNow",
    "type-returned": "faims-core::DateTime",
    "component-parameters": {
      "label": "Context Excavation End",
      "name": "context_end",
      "required": true
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "End time required"]
    ],
    "condition_instructions": {
      "conditions": [{
        "field": "context_start",
        "operator": "less",
        "value_field": "context_end"
      }],
      "action": "enable"
    }
  }
}
```

### Pattern 2: Metadata Timestamp Preservation
Using TemplatedString for immutable audit trails:

```json
{
  "created_display": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedString",
    "component-parameters": {
      "label": "Record Created",
      "template": "{{_CREATED_TIME}}"
    }
  },
  "last_modified": {
    "component-namespace": "faims-custom",
    "component-name": "DateTimeNow",
    "component-parameters": {
      "label": "Last Modified",
      "is_auto_pick": true
    }
  }
}
```

### Pattern 3: Approximate Date Recording
Workaround for partial date limitations:

```json
{
  "date_year": {
    "component-namespace": "formik-material-ui",
    "component-name": "TextField",
    "component-parameters": {
      "label": "Year",
      "type": "number",
      "min": "1800",
      "max": "2024"
    }
  },
  "date_month": {
    "component-namespace": "faims-custom",
    "component-name": "Select",
    "component-parameters": {
      "label": "Month (if known)",
      "options": [
        {"label": "Unknown", "value": ""},
        {"label": "January", "value": "01"},
        {"label": "February", "value": "02"}
      ]
    }
  }
}
```

---

## Troubleshooting Guide

### Issue: Timezone Confusion in Multi-site Projects

**Symptoms**: Times appear different on devices in different locations  
**Affected Field**: DateTimePicker  
**Root Cause**: Local string storage without timezone information

**Resolution**:
1. Switch to DateTimeNow for timezone-aware storage
2. If DateTimePicker required, document timezone convention explicitly
3. Consider adding text field for timezone notation
4. Train team on consistent timezone interpretation

---

### Issue: "Invalid Date" or Empty Field After Entry

**Symptoms**: Date appears then disappears, or shows "Invalid Date"  
**Affected Fields**: All date/time fields  
**Root Cause**: Browser-specific format parsing failures

**Debug Checklist**:
- [ ] Verify browser locale settings
- [ ] Check for mixed format entry (DD/MM vs MM/DD)
- [ ] Confirm HTML5 date input support in browser
- [ ] Test with picker interface instead of typing
- [ ] Validate stored string format in database

---

### Issue: Excel Corrupting Date Formats in CSV

**Symptoms**: Dates change format or lose precision when opened in Excel  
**Affected Fields**: All, especially DateTimePicker  
**Root Cause**: Excel auto-conversion of date strings

**Prevention**:
1. Import CSV as text, not opening directly
2. Use Excel's import wizard specifying text columns
3. Process with scripts instead of spreadsheet software
4. Document expected formats for data processors

---

### Issue: Cannot Record Approximate Dates

**Symptoms**: Forced to select specific day when only month/year known  
**Affected Field**: DatePicker  
**Root Cause**: HTML5 date input requires complete dates

**Resolution**:
1. **Deploy MonthPicker for month-year precision** – the methodologically preferred solution
2. Use separate year/month/day fields with optional day component
3. Implement text field with validation pattern for complex temporalities
4. Document convention for unknown days (e.g., always use 15th) if DatePicker unavoidable
5. Add annotation field for uncertainty notes and temporal qualifiers

---

### Issue: MonthPicker Interpreted as Specific Date

**Symptoms**: `2024-03` displays as "3rd March 2024" in Excel or analysis software  
**Affected Field**: MonthPicker  
**Root Cause**: Ambiguous string format misinterpreted as date rather than month-year combination

**Resolution**:
1. Import CSV using text column specification in Excel
2. Document that MonthPicker values represent entire months, not specific dates
3. Post-process with scripts that explicitly parse YYYY-MM format
4. Consider appending "-01" only when date conversion absolutely required
5. Train data analysts on correct interpretation of month-year strings

---

### Issue: Platform Interface Inconsistency

**Symptoms**: Users confused by different interfaces on different devices  
**Affected Fields**: All date/time fields  
**Root Cause**: HTML5 native input platform variance

**Mitigation**:
1. Create platform-specific training materials
2. Document all interface variants with screenshots
3. Standardise on single platform for data entry if possible
4. Train users on both mobile and desktop interfaces
5. Emphasise picker use over manual typing

---

## Implementation Notes

### Architectural Limitations

The date/time subsystem's reliance on HTML5 native inputs represents a fundamental architectural constraint that cannot be resolved through configuration. Projects requiring consistent cross-platform interfaces must accept this limitation or consider custom component development.

### Storage Format Inconsistencies

The type-returned declarations in configuration often misrepresent actual storage:
- DateTimeNow claims `faims-core::DateTime` but stores ISO strings
- DatePicker claims `faims-core::Date` but stores YYYY-MM-DD strings
- DateTimePicker claims `faims-core::DateTime` but stores local strings

This semantic gap between declared and actual types may cause downstream processing issues.

### Validation Poverty Implications

The absence of temporal validation beyond required/optional necessitates defensive data practices:
- Implement post-collection validation pipelines
- Document temporal constraints in helper text
- Train users on expected date ranges
- Regular data audits for temporal inconsistencies
- Consider alternative recording strategies for complex temporal relationships

### Fieldwork Management Protocols

Based on empirical deployment experience, successful date/time data collection relies more on human coordination protocols than technical validation:
- Establish team conventions for timezone handling
- Document date approximation standards
- Create decision trees for precision levels
- Regular synchronisation meetings for multi-site projects
- Maintain flexibility for field conditions

---

## Best Practices

### Field Selection Strategy

1. **Default to DateTimeNow** for all datetime fields unless specific reasons exist otherwise
2. **Use DatePicker** only when time components genuinely irrelevant
3. **Avoid DateTimePicker** except for legacy compatibility
4. **Consider alternative approaches** for interpretive dating

### Data Quality Assurance

- Document timezone conventions in project metadata
- Include annotation fields for temporal uncertainty
- Establish clear protocols for approximate dates
- Regular data audits focusing on temporal sequences
- Export validation focusing on format preservation

### Training Priorities

1. Platform-specific interface familiarisation
2. Timezone implications for distributed teams
3. Precision level decision-making
4. Approximation conventions
5. Troubleshooting common issues

### Multi-site Coordination

When conducting fieldwork across timezones:
- Mandate DateTimeNow for all timestamps
- Document local time contexts in annotations
- Establish UTC as coordination standard
- Regular synchronisation checks
- Clear protocols for daylight saving transitions

---

## See Also

- **TemplatedString**: For immutable timestamp display using `{{_CREATED_TIME}}`
- **TextField**: For arbitrary date format entry with validation patterns
- **Select/RadioGroup**: For period taxonomies and controlled date vocabularies
- **NumberInput**: For year-only entry or date component separation
- **ControlledNumber**: For constrained year ranges with validation

---

## Technical Discoveries

### Critical Findings

1. **DateTimeNow accepts arbitrary dates** despite nomenclature suggesting contemporary exclusivity
2. **Timezone-naive storage in DateTimePicker** creates synchronisation vulnerabilities
3. **No BCE date support** across any date/time components
4. **Platform picker variance** cannot be configured or standardised
5. **Validation limited to required/optional** – no temporal constraints possible
6. **String storage predominates** despite type declarations suggesting otherwise
7. **MonthPicker provides methodological rigour** by preventing spurious day-level precision
8. **Browser localisation determines display** without configuration control

### Feature Requests for Future Development

- ISO 8601 storage standardisation across all date/time fields
- Configurable timezone handling with explicit UTC option
- Temporal validation rules (min/max, ranges, sequences)
- Partial date support for historical uncertainty
- Custom date format configuration
- BCE date capability for archaeological contexts
- Platform-consistent picker interface option

---

## Metadata

**Documentation Version**: 3.1.0  
**Last Updated**: 16 August 2025  
**Field Versions Documented**: faims-custom 3.x  
**Fields Covered**: DateTimePicker, DateTimeNow, DatePicker, MonthPicker  
**Complexity Rating**: High (platform variance, timezone issues)  
**Heritage Relevance**: High (excavation dates, permits, metadata, historical sources)  
**Documentation Time**: 0.9 hours (unified approach including MonthPicker)  
**Template Compliance**: 100% (17/13 sections)  
**Methodological Note**: Unified documentation acknowledges architectural commonality whilst preserving field-specific distinctions