# Data Export Reference

> **⚠️ DEPRECATED**: This document has been superseded by the consolidated [Operations Reference](../../reference/operations-reference.md). This archived version is maintained for reference only.

## Universal Export Behavior for All Fieldmark v3 Fields

### Overview

Fieldmark supports two primary export formats: CSV (for spreadsheets) and JSON (for data interchange). Export behavior is consistent across field types, with specific handling for data types and special characters.

### Export Formats

#### CSV Export
- **Format**: Comma-separated values with headers
- **Encoding**: UTF-8 with BOM
- **Line endings**: Unix (LF) or Windows (CRLF)
- **Quote character**: Double quotes (")
- **Escape character**: Double quotes ("")
- **Null representation**: Empty cell

#### JSON Export  
- **Format**: Valid JSON with proper escaping
- **Encoding**: UTF-8
- **Structure**: Nested objects preserving relationships
- **Null representation**: `null` value
- **Arrays**: Preserved as JSON arrays
- **Objects**: Preserved as nested objects

### Field Type Export Mapping

#### Text Fields
| Field Type | CSV Export | JSON Export | Special Considerations |
|------------|------------|-------------|------------------------|
| TextField | Plain text string | String | Quoted if contains commas |
| MultipleTextField | Text with line breaks | String | May break CSV readers |
| FAIMSTextField | Plain text string | String | Same as TextField |
| TemplatedString | Generated value only | String | Template not exported |
| Email | Plain text string | String | No validation on export |
| Address | JSON string in cell | Object | Requires parsing |
| QRCode | Scanned value | String | No scan metadata |
| RichText | **Not exported** | **Not exported** | Definition only |

#### Number Fields
| Field Type | CSV Export | JSON Export | Special Considerations |
|------------|------------|-------------|------------------------|
| NumberField | Numeric value | Number | Scientific notation possible |
| ControlledNumber | Numeric value | Number | Same as NumberField |
| BasicAutoIncrementer | String with zeros | String | Excel strips leading zeros |
| Integer fields | Integer value | Number | No decimal places |

#### DateTime Fields
| Field Type | CSV Export | JSON Export | Special Considerations |
|------------|------------|-------------|------------------------|
| DateTime | ISO 8601 string | String | With timezone |
| DateTimeNow | ISO 8601 string | String | Capture timestamp |
| DatePicker | YYYY-MM-DD | String | No time component |
| MonthPicker | YYYY-MM | String | Excel misinterprets |

#### Selection Fields
| Field Type | CSV Export | JSON Export | Special Considerations |
|------------|------------|-------------|------------------------|
| Checkbox | true/false | Boolean | Not "TRUE"/"FALSE" |
| RadioGroup | Selected value | String | Single value only |
| Select | Selected value | String | Value not label |
| MultiSelect | Comma-joined | Array | Nested commas problematic |
| AdvancedSelect | Path string | String | " > " delimiter |

#### Media Fields
| Field Type | CSV Export | JSON Export | Special Considerations |
|------------|------------|-------------|------------------------|
| TakePhoto | Filename(s) | Array | No binary data |
| FileUploader | Filename(s) | Array | Paths only |

#### Location Fields
| Field Type | CSV Export | JSON Export | Special Considerations |
|------------|------------|-------------|------------------------|
| TakePoint | Lat,Long string | Object | GeoJSON format |
| MapFormField | GeoJSON string | Object | Complex structure |

### Meta Properties Export

Meta properties create additional columns/fields:

#### CSV Additional Columns
- `fieldname_annotation` - Annotation text
- `fieldname_uncertainty` - true/false
- `fieldname_timestamp` - If timestamped

#### JSON Additional Properties
```json
{
  "fieldname": "value",
  "fieldname_annotation": "annotation text",
  "fieldname_uncertainty": true,
  "fieldname_timestamp": "2024-03-15T10:30:00Z"
}
```

### Special Character Handling

#### CSV Special Characters
| Character | Handling | Example |
|-----------|----------|---------|
| Comma (,) | Quote entire field | `"Smith, John"` |
| Quote (") | Double the quote | `"She said ""Hello"""` |
| Newline | Quote entire field | `"Line 1\nLine 2"` |
| Tab | Quote entire field | `"Col1\tCol2"` |
| Leading = | Quote to prevent formula | `"=1+2"` |

#### JSON Special Characters
Automatically escaped per JSON specification:
- `"` becomes `\"`
- `\` becomes `\\`
- Newline becomes `\n`
- Tab becomes `\t`
- Unicode properly encoded

### Excel/Spreadsheet Issues

#### Common Problems
1. **Leading zeros stripped**: BasicAutoIncrementer "00042" becomes 42
2. **Scientific notation**: Large numbers like 123456789012345
3. **Date auto-conversion**: 2024-03 becomes March 3, 2024
4. **Formula injection**: Fields starting with =, +, -, @
5. **Regional settings**: DD/MM vs MM/DD confusion
6. **Unicode corruption**: Special characters mangled

#### Prevention Strategies
1. **Use Text Import Wizard**: Don't double-click CSV
2. **Set column types**: Explicitly set text for IDs
3. **Pre-format columns**: Format before pasting
4. **Use JSON for complex data**: Avoids Excel parsing
5. **Document formats**: Provide import instructions

### Null and Empty Value Handling

#### CSV Representation
| Value Type | Representation | Notes |
|------------|----------------|-------|
| null | Empty cell | No quotes |
| Empty string | `""` | Two quotes |
| Zero | `0` | Numeric zero |
| false | `false` | Boolean false |
| Empty array | Empty cell | Lost on import |
| Empty object | `{}` | JSON string |

#### JSON Representation
| Value Type | Representation | Notes |
|------------|----------------|-------|
| null | `null` | JSON null |
| Empty string | `""` | Empty string |
| Zero | `0` | Numeric zero |
| false | `false` | Boolean false |
| Empty array | `[]` | Empty array |
| Empty object | `{}` | Empty object |

### Array Export Behavior

#### MultiSelect Arrays
**CSV**: Comma-joined with issues
```csv
"Option1,Option2,Option3"
```
**Problem**: If options contain commas: `"Red, Green, and Blue,Yellow"`

**JSON**: Proper array
```json
["Option1", "Option2", "Option3"]
```

#### File Arrays (Media)
**CSV**: Semicolon-separated
```csv
"photo1.jpg;photo2.jpg;photo3.jpg"
```

**JSON**: Array of objects
```json
[
  {"filename": "photo1.jpg", "size": 1234567},
  {"filename": "photo2.jpg", "size": 2345678}
]
```

### Hierarchical Data Export

#### AdvancedSelect Paths
**CSV**: Delimited string
```csv
"Kingdom > Phylum > Class > Order > Family > Genus > Species"
```

**JSON**: Same (not hierarchical)
```json
"Kingdom > Phylum > Class > Order > Family > Genus > Species"
```

#### Address Components
**CSV**: JSON in cell
```csv
"{""line1"":""123 Main St"",""city"":""Sydney"",""postcode"":""2000""}"
```

**JSON**: Nested object
```json
{
  "line1": "123 Main St",
  "city": "Sydney",
  "postcode": "2000"
}
```

### Export Performance

#### Performance by Record Count
| Records | CSV Generation | JSON Generation | Download Time |
|---------|---------------|-----------------|---------------|
| <100 | Instant | Instant | <1s |
| 100-1000 | <2s | <1s | 1-5s |
| 1000-10000 | 5-10s | 2-5s | 5-30s |
| >10000 | May timeout | 10-30s | >30s |

#### Memory Considerations
- CSV: Entire file in memory
- JSON: Streamed if supported
- Large exports: Use pagination
- Binary data: Never inline

### Platform-Specific Behavior

#### Web Browser
- Download to default folder
- Memory limited by browser
- May show progress bar

#### Mobile App
- Save to app storage first
- Then share/export
- Memory constraints tighter

#### API Export
- Supports streaming
- Pagination available
- Format negotiation

### Best Practices

#### For Developers
1. **Document export format**: Provide examples
2. **Include import instructions**: Especially for Excel
3. **Test with special characters**: Commas, quotes, newlines
4. **Validate round-trip**: Export → Import → Export
5. **Consider data types**: Preserve types where possible

#### For Users
1. **Use JSON for complex data**: Preserves structure
2. **Use CSV for simple tables**: Excel-compatible
3. **Document Excel settings**: Regional, date formats
4. **Backup before import**: Excel auto-conversion is destructive
5. **Use Text Import Wizard**: Never double-click CSV

### Common Export Issues

#### Issue: Commas in MultiSelect Options
**Problem**: CSV parsing breaks
**Solution**: Use different delimiter or JSON export

#### Issue: Excel Stripping Zeros
**Problem**: IDs like "00042" become 42
**Solution**: Import as text or use TemplatedString wrapper

#### Issue: Date Format Confusion  
**Problem**: MM/DD vs DD/MM
**Solution**: Use ISO 8601 format (YYYY-MM-DD)

#### Issue: Large Numbers in Excel
**Problem**: Converted to scientific notation
**Solution**: Format as text before import

#### Issue: Unicode Characters Lost
**Problem**: Excel default encoding
**Solution**: Specify UTF-8 on import

### Export Validation

#### Checklist for Testing
- [ ] Null values export correctly
- [ ] Special characters preserved
- [ ] Arrays handled appropriately
- [ ] Dates in correct format
- [ ] Numbers maintain precision
- [ ] Meta properties included
- [ ] Unicode preserved
- [ ] Large datasets work

### Related Documentation
- Field-specific export notes in category docs
- Meta Properties Reference for annotation/uncertainty export
- Platform specifications for device-specific limits
- API documentation for programmatic export

### Version
Last updated: 2025-09-03
Applies to: Fieldmark v3 (all versions)
Export version: 2.0 (current format)