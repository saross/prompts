# Operations Reference

<!-- discovery:metadata
provides: [migration-procedures, troubleshooting, deployment, maintenance]
see-also: [constraints-reference, platform-reference]
-->

## Migration, Export, and Troubleshooting Guide for Fieldmark v3 {essential}

## Overview {essential}

This reference consolidates operational guidance for Fieldmark v3, covering:
- Migration strategies and procedures
- Data export formats and behaviors
- Troubleshooting framework and diagnostics

---

## Part 1: Migration Operations {essential}

### Migration Planning Framework

#### Pre-Migration Checklist
- [ ] **Identify scope** - Which forms, fields, and records affected
- [ ] **Assess risk** - Data loss potential, user impact, rollback complexity
- [ ] **Backup data** - Complete export before any changes
- [ ] **Document current state** - Screenshots, JSON exports, configuration
- [ ] **Test migration path** - Verify in development environment
- [ ] **Prepare rollback plan** - Know how to revert if needed
- [ ] **Schedule window** - Minimize user disruption
- [ ] **Communicate changes** - Notify all stakeholders

#### Risk Assessment Matrix

| Migration Type | Risk Level | Backup Required | Testing Required | Rollback Difficulty |
|---------------|------------|-----------------|------------------|-------------------|
| Add new field | Low | Optional | Minimal | Easy |
| Modify validation | Medium | Yes | Moderate | Easy |
| Change field type | High | Critical | Extensive | Moderate |
| Restructure relationships | Critical | Critical | Extensive | Difficult |
| Delete fields | Critical | Critical | Moderate | Impossible |

### Universal Migration Patterns

#### Pattern 1: Parallel Field Migration
**When to use**: Changing field types or major restructuring

```
1. Create new field alongside old field
2. Run both fields in parallel during transition
3. Migrate data progressively
4. Hide old field once migration complete
5. Delete old field after verification period
```

**Benefits**: No data loss, gradual transition, easy rollback, user training period

#### Pattern 2: In-Place Modification
**When to use**: Minor configuration changes, validation updates

```
1. Export current configuration
2. Test modifications in development
3. Apply changes during maintenance window
4. Monitor for issues
5. Rollback if problems detected
```

**Benefits**: Faster implementation, less complexity, immediate effect
**Risks**: Potential data loss, harder rollback, user disruption

#### Pattern 3: Staged Migration
**When to use**: Large-scale changes affecting multiple forms

```
1. Divide migration into phases
2. Complete Phase 1, verify, stabilize
3. Proceed to next phase only after validation
4. Maintain compatibility between phases
5. Complete final cutover
```

**Benefits**: Reduced risk, learning between phases, easier troubleshooting, gradual user adaptation

### Backup and Recovery Procedures

#### Complete Project Backup
```bash
# Export all project data
1. Navigate to Project Settings
2. Export → Download all data (CSV)
3. Export → Download project configuration (JSON)
4. Store in version-controlled location
5. Verify export integrity
```

#### Selective Field Backup
```json
// Save specific field configurations
{
  "backup_date": "2025-01-03",
  "field_name": "original-field",
  "configuration": {
    // Complete field JSON
  },
  "sample_data": [
    // Representative data samples
  ]
}
```

#### Rollback Decision Tree
```
Issue Detected
├─ Data corruption?
│  └─ YES → Immediate rollback
│
├─ Functional failure?
│  ├─ Critical? → Immediate rollback
│  └─ Minor? → Hotfix attempt
│
└─ Performance issue?
   ├─ Severe? → Rollback
   └─ Moderate? → Optimize first
```

#### Rollback Steps
1. **Stop all user access** - Maintenance mode
2. **Restore configuration** - Upload backed-up JSON
3. **Verify structure** - Check all fields present
4. **Restore data** - Import CSV if needed
5. **Test functionality** - Verify core features
6. **Re-enable access** - Remove maintenance mode

### Testing Methodologies

#### Test Coverage Requirements

| Migration Component | Test Type | Required Coverage |
|-------------------|-----------|-------------------|
| Field structure | Unit | 100% |
| Data integrity | Integration | 100% |
| Validation rules | Functional | 100% |
| User workflows | E2E | Critical paths |
| Performance | Load | Representative load |
| Platform compatibility | Cross-platform | All target platforms |

#### Validation Checklist
- [ ] All existing data accessible
- [ ] New fields function correctly
- [ ] Validation rules apply properly
- [ ] Export/import maintains integrity
- [ ] Sync operations complete
- [ ] Performance acceptable (~100 fields recommended limit)
- [ ] Mobile platforms stable
- [ ] User permissions preserved

### Data Preservation Strategies

#### Pre-Migration Preservation
1. **Export everything** - Even seemingly unrelated data
2. **Document relationships** - Parent-child, linked records
3. **Capture metadata** - Timestamps, user info, annotations
4. **Screenshot complex data** - Visual layouts, configurations
5. **Version control** - Track all configuration changes

#### Type Conversion Matrix
| From Type | To Type | Data Preservation Method |
|-----------|---------|-------------------------|
| Text | Number | Parse with fallback |
| Number | Text | ToString with format |
| Single | Multiple | Wrap in array |
| Multiple | Single | Take first/concatenate |
| Rich text | Plain text | Strip HTML/Markdown |
| Date | Text | ISO format string |

### Migration Timing Best Practices

#### Optimal Windows
- **Best**: Weekend early morning (minimal users)
- **Good**: After hours weekday (low activity)
- **Acceptable**: Lunch hour (brief changes only)
- **Avoid**: Monday morning, end of month, deadlines

#### Time Estimation Formula
```
Migration Time = 
  Export Time +
  (Backup Time × 2) +
  Migration Execution +
  (Verification Time × 2) +
  Buffer (50% of total)
```

### Communication Templates

#### Pre-Migration Notice
```markdown
Subject: Scheduled Field Migration - [Date]

Team,

We will be migrating [field/form names] on [date] at [time].

**What's Changing:**
- [Specific changes]

**Impact:**
- Expected downtime: [duration]
- Affected users: [groups]
- Data effects: [any data changes]

**Action Required:**
- Complete pending work by [deadline]
- Export any critical data before [time]

**Questions:** Contact [person]
```

#### Post-Migration Report
```markdown
Subject: Migration Complete - [Field/Form]

Status: ✅ Successful / ⚠️ Partial / ❌ Rolled Back

**Completed Changes:**
- [What was done]

**Issues Encountered:**
- [Any problems and resolutions]

**Verification Steps:**
- [How users can verify]

**Support:** [Contact for issues]
```

---

## Part 2: Data Export Operations {important}

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

### Export Validation Checklist
- [ ] Null values export correctly
- [ ] Special characters preserved
- [ ] Arrays handled appropriately
- [ ] Dates in correct format
- [ ] Numbers maintain precision
- [ ] Meta properties included
- [ ] Unicode preserved
- [ ] Large datasets work

---

## Part 3: Troubleshooting Operations {important}

### Quick Diagnosis Framework

#### Universal Diagnostic Steps
1. **Identify Symptoms** - What exactly is the user experiencing?
2. **Check Console** - Browser/app console for JavaScript errors
3. **Verify Platform** - iOS, Android, or Web-specific issue?
4. **Test Isolation** - Does it occur in a minimal test case?
5. **Check Configuration** - Valid JSON and parameters?
6. **Review Logs** - Sync logs, network requests, validation errors
7. **Document Pattern** - Reproducible steps and conditions

### Common Issue Categories

| Category | Frequency | Impact | Typical Resolution Time |
|----------|-----------|--------|------------------------|
| Configuration | High | Medium | 5-15 minutes |
| Platform-specific | Medium | High | 15-30 minutes |
| Performance | Medium | High | 30-60 minutes |
| Data validation | High | Low | 5-10 minutes |
| Sync/Network | Low | Critical | Variable |
| Permissions | Medium | Critical | 10-20 minutes |

### Universal Error Patterns

#### JavaScript Errors
| Error Pattern | Common Cause | Quick Fix |
|--------------|--------------|-----------|
| `Cannot read property of undefined` | Missing null checks | Add optional chaining |
| `Maximum call stack exceeded` | Infinite loop/recursion | Check conditions |
| `Out of memory` | Large data/images | Reduce size/pagination |
| `Network timeout` | Slow connection | Retry/offline mode |
| `Permission denied` | Missing permissions | Check platform settings |

#### Silent Failures
**Indicators:**
- No error message but unexpected behavior
- Console warnings without errors
- Partial functionality
- Platform-specific differences

**Common Causes:**
- Sanitization removing content
- Validation preventing saves
- Platform API differences
- Race conditions

### Diagnostic Tools and Techniques

#### Browser DevTools
```javascript
// Essential console commands
console.log('Component state:', this.state);
console.table(validationErrors);
console.time('Operation'); // ... console.timeEnd('Operation');
debugger; // Breakpoint
```

#### Network Inspection
- Check request/response payloads
- Verify API endpoints
- Monitor request timing
- Identify failed requests
- Check CORS headers

#### Mobile Debugging

**iOS**
- Safari Web Inspector
- Console.app for native logs
- Simulator vs device testing
- Memory profiler

**Android**
- Chrome DevTools remote
- adb logcat filtering
- Android Studio profiler
- WebView debugging

### Issue Resolution Framework

#### Severity Levels
1. **Critical** - Data loss, app crash, security issue
2. **High** - Feature unusable, widespread impact
3. **Medium** - Workaround available, limited impact
4. **Low** - Cosmetic, rare occurrence

#### Resolution Workflow
```
Issue Reported
├─ Critical?
│  ├─ Yes → Immediate Hotfix
│  └─ No → Diagnose Root Cause
│      ├─ Known Issue?
│      │  ├─ Yes → Apply Known Fix
│      │  └─ No → Investigate
│      │      ├─ Reproducible?
│      │      │  ├─ Yes → Create Fix → Test → Deploy
│      │      │  └─ No → Gather More Info
```

### Common Troubleshooting Scenarios

#### Scenario 1: Field Not Displaying
**Diagnostic Path:**
1. Check console for errors
2. Verify component name spelling
3. Confirm namespace correct
4. Check conditions if applicable
5. Verify JSON syntax
6. Test in different notebook

**Common Fixes:**
- Correct component-name case
- Fix namespace typo
- Resolve condition logic
- Fix JSON syntax error

#### Scenario 2: Validation Always Failing
**Diagnostic Path:**
1. Check validation schema syntax
2. Verify field type matches validation
3. Test with minimal validation
4. Check for conflicting validations
5. Review initialValue compatibility

**Common Fixes:**
- Match array/string validation to field
- Correct yup method names
- Fix validation parameters
- Align with multiple setting

#### Scenario 3: Performance Degradation
**Diagnostic Path:**
1. Profile with DevTools
2. Count active components (~100 field recommendation)
3. Measure data size
4. Check render frequency
5. Monitor memory usage

**Common Fixes:**
- Reduce active field count
- Implement pagination
- Optimize images/data
- Add debouncing
- Clear unused data

#### Scenario 4: Platform-Specific Issues
**Diagnostic Path:**
1. Identify affected platforms
2. Check platform-specific APIs
3. Review permission states
4. Test on multiple devices
5. Check version compatibility

**Common Fixes:**
- Add platform detection
- Implement fallbacks
- Request permissions properly
- Update WebView/browser
- Add polyfills

### Error Message Decoder

| Error Message | Likely Cause | Resolution |
|--------------|--------------|------------|
| "Required field" | Validation without value | Provide value or remove validation |
| "Invalid type" | Type mismatch | Check type-returned vs validation |
| "Component not found" | Wrong name/namespace | Verify component registration |
| "Permission denied" | Platform permission | Request in app settings |
| "Network error" | Connection issue | Check connectivity/CORS |
| "Memory exhausted" | Too much data | Reduce/paginate data |
| "Sync conflict" | Concurrent edits | Choose version/merge |
| "Invalid configuration" | JSON syntax/schema | Validate JSON structure |

### Prevention Strategies

#### Design-Time Prevention
- Validate JSON before deployment
- Test on minimum spec devices
- Set realistic data limits (~100 fields)
- Plan for offline scenarios
- Document known limitations

#### Runtime Prevention
- Add comprehensive error handling
- Implement retry mechanisms
- Provide user feedback
- Add performance monitoring
- Include diagnostic logging

#### Testing Prevention
- Cross-platform testing
- Edge case coverage
- Performance testing
- Permission denial testing
- Network condition testing

### Escalation Procedures

#### When to Escalate
- Data loss occurring
- Security vulnerability found
- Widespread platform issue
- No known workaround
- Regression from update

#### Escalation Path
1. **Level 1**: Check documentation and known issues
2. **Level 2**: Community forum/discussion
3. **Level 3**: GitHub issue creation
4. **Level 4**: Direct support contact

#### Issue Report {important} Template
```markdown
## Issue Report {important}
**Environment:**
- Platform: [iOS/Android/Web]
- Version: [Fieldmark version]
- Device: [Model/Browser]

**Issue:**
- Expected: [What should happen]
- Actual: [What does happen]
- Steps: [How to reproduce]

**Diagnostics:**
- Console errors: [Any errors]
- Network failures: [Failed requests]
- Configuration: [Relevant JSON]

**Attempts:**
- Tried: [What you've tried]
- Result: [What happened]
```

### Quick Reference Tables

#### Diagnostic Command Reference
| Platform | Command | Purpose |
|----------|---------|---------|
| All | `console.log()` | Debug output |
| Web | `debugger;` | Breakpoint |
| iOS | `Safari Inspector` | Remote debug |
| Android | `chrome://inspect` | Remote debug |
| All | `JSON.stringify()` | Inspect objects |

#### Time to Resolution Guidelines
| Issue Type | Target Time | Maximum Time |
|------------|-------------|--------------|
| Configuration | 15 min | 1 hour |
| Validation | 10 min | 30 min |
| Platform | 30 min | 2 hours |
| Performance | 1 hour | 4 hours |
| Data corruption | Immediate | 1 hour |

---

## Common Migration Pitfalls {comprehensive}

### Top 10 Pitfalls to Avoid
1. **No backup** - Always backup, even for "simple" changes
2. **Untested migration** - Never migrate without testing
3. **Peak time migration** - Schedule during low usage
4. **No rollback plan** - Always have escape route
5. **Poor communication** - Over-communicate changes
6. **Ignoring dependencies** - Check all relationships
7. **Skipping verification** - Always verify post-migration
8. **Rushed timeline** - Allow buffer time
9. **Single person knowledge** - Document for team
10. **No monitoring** - Watch for delayed issues

### Recovery from Failed Migrations

#### Immediate Actions
1. **Don't panic** - Follow rollback plan
2. **Communicate** - Inform users immediately
3. **Assess damage** - What data affected?
4. **Execute rollback** - Use prepared procedure
5. **Document failure** - For post-mortem

#### Post-Recovery Analysis
- What went wrong?
- What wasn't tested?
- How to prevent recurrence?
- Update procedures
- Share learnings

---

## Best Practices Summary {comprehensive}

### For Developers
1. **Document export format**: Provide examples
2. **Include import instructions**: Especially for Excel
3. **Test with special characters**: Commas, quotes, newlines
4. **Validate round-trip**: Export → Import → Export
5. **Consider data types**: Preserve types where possible

### For Users
1. **Use JSON for complex data**: Preserves structure
2. **Use CSV for simple tables**: Excel-compatible
3. **Document Excel settings**: Regional, date formats
4. **Backup before import**: Excel auto-conversion is destructive
5. **Use Text Import Wizard**: Never double-click CSV

### Platform Considerations
- **Web Browser**: Download to default folder, memory limited
- **Mobile App**: Save to app storage first, tighter memory constraints
- **API Export**: Supports streaming, pagination available

---

## Version Compatibility {comprehensive}

| Fieldmark Version | Migration Support | Breaking Changes | Notes |
|------------------|-------------------|------------------|--------|
| v3.0.x | Baseline | - | Starting point |
| v3.1.x | Enhanced backup | Field type changes | Test thoroughly |
| v3.2.x | Batch operations | Validation syntax | Review all validations |
| v3.3.x | Current | Namespace updates | Update components |

### Version-Specific Considerations
- Always migrate to latest stable version first
- Test on version before implementing
- Check release notes for migration guides
- Maintain version documentation

---

## Performance Guidelines {comprehensive}

### Recommended Limits
- **Fields per form**: ~100 (approximate)
- **Export size**: <10,000 records for reliable performance
- **Migration batch size**: 500-1000 records
- **Test environment**: Match production specs

### Performance Monitoring
- Use browser DevTools Performance tab
- Monitor memory usage during operations
- Track migration execution times
- Document performance baselines

---

## Metadata {comprehensive}
- **Document Version**: 1.0
- **Last Updated**: 2025-01-06
- **Applies to**: Fieldmark v3 (all versions)
- **Purpose**: Consolidate operational guidance for migration, export, and troubleshooting
- **Sources**: Unified from migration-strategies, data-export, and troubleshooting-framework references