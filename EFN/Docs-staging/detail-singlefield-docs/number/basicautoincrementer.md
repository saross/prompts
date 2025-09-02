# BasicAutoIncrementer Field (Sequential Identifier Generation)

## Overview

The BasicAutoIncrementer field represents a sophisticated response to the fundamental challenge of generating unique sequential identifiers within distributed, offline-capable data collection environments. Unlike conventional auto-increment implementations that rely upon centralised sequence management, this component employs a range allocation architecture that enables multiple devices to generate guaranteed-unique identifiers whilst operating in complete network isolation for extended periods. The field's most consequential design decision – returning string rather than numeric types – reflects its primary purpose as an identifier generator rather than a computational value provider. This architectural choice, whilst initially counterintuitive to those expecting numeric sequences, enables critical features such as zero-padding preservation (maintaining "00001" rather than degrading to "1") and eliminates the ambiguity that arises when identifier semantics become conflated with mathematical operations.

The implementation philosophy prioritises human coordination over technical complexity, acknowledging that successful field research depends more upon robust operational protocols than automated conflict resolution mechanisms. Where centralised systems might employ complex synchronisation algorithms or conflict detection heuristics, BasicAutoIncrementer deliberately delegates range management to human teams, recognising that field researchers possess contextual knowledge about deployment patterns, team structures, and operational constraints that no algorithm could reliably infer. This design decision – refined through a decade of production deployments – reflects the empirical reality that attempted automation of range coordination consistently proved more fragile than well-documented human protocols.

Within the broader Fieldmark ecosystem, BasicAutoIncrementer typically functions as a component within larger identifier strategies, most commonly feeding into TemplatedString fields that compose complex human-readable identifiers. This compositional approach not only provides semantic richness (transforming "00042" into "SITE-A-00042-2024") but also serves as a critical mitigation strategy against downstream tools – particularly Microsoft Excel – that aggressively strip leading zeros from unprotected numeric strings.

## Common Use Cases

- **Specimen cataloguing in biological surveys** where sequential numbering maintains collection order whilst zero-padding ensures consistent identifier length across thousands of samples
- **Archaeological feature numbering** where each excavation unit requires unique identifiers that persist through post-excavation analysis and publication
- **Artefact registration sequences** providing systematic numbering that integrates with museum cataloguing systems expecting fixed-width identifiers
- **Photographic documentation series** where images require sequential numbering that preserves chronological ordering even when sorted alphabetically
- **Plot or transect identifiers in ecological studies** where consistent numbering facilitates data integration across multiple sampling periods
- **Sample bag numbering for geological fieldwork** maintaining chain-of-custody through sequential identification resistant to transcription errors
- **Component identifiers within hierarchical numbering schemes** where BasicAutoIncrementer provides the sequential element within complex identifiers like "TRENCH-B-CONTEXT-00234"

## Core Configuration

### Required Properties

```json
{
  "component-namespace": "faims-custom",
  "component-name": "BasicAutoIncrementer",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "unique-field-identifier",
    "label": "Specimen Number",
    "num_digits": 5,
    "form_id": "specimen-form"
  }
}
```

**Critical Clarification**: Despite generating sequential numbers, this field returns `faims-core::String` rather than numeric types. This deliberate design decision preserves zero-padding, prevents mathematical operations on identifiers, and maintains format consistency across export cycles.

### Optional Properties

```json
{
  "component-parameters": {
    "variant": "outlined",
    "helperText": "Auto-generated specimen number",
    "disabled": false
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Specimen number is mandatory"]
  ],
  "initialValue": "",
  "persistent": false,
  "meta": {
    "annotation": {"include": false},
    "uncertainty": {"include": false}
  }
}
```

### Property Specifications

#### Essential Configuration
- **component-namespace** (`string`): Invariably "faims-custom" for this implementation
- **component-name** (`string`): Exactly "BasicAutoIncrementer" (case-sensitive)
- **type-returned** (`string`): Always "faims-core::String" – not configurable despite numeric appearance
- **name** (`string`): Unique identifier within the form; used for field referencing and data binding
- **label** (`string`): Hidden from users but required for system processing

#### Behavioural Parameters
- **num_digits** (`integer`): Zero-padding width (default: 4, range: 1–10)
  - Value of 5 produces: "00001", "00042", "10000"
  - Padding occurs via JavaScript's `padStart()` function
  - Excess digits display without truncation
- **form_id** (`string`): Counter isolation key enabling independent sequences per form type
  - "specimen-form" and "feature-form" maintain separate counters
  - Enables multiple numbering schemes within single notebook
  - Counter persists even if form temporarily removed

#### Compositional Integration
BasicAutoIncrementer lacks native prefix/suffix capabilities, requiring TemplatedString composition for complex identifiers:

```json
{
  "auto_number": {
    "component-name": "BasicAutoIncrementer",
    "component-parameters": {
      "num_digits": 5,
      "form_id": "artefact"
    }
  },
  "artefact_id": {
    "component-name": "TemplatedStringField",
    "component-parameters": {
      "template": "ART-{{auto_number}}-{{year}}"
    }
  }
}
```

## Validation Rules

### Validation Architecture

BasicAutoIncrementer implements minimal validation, reflecting its role as an identifier generator rather than a user input field:

| Validation Layer | Behaviour | Configuration | Notes |
|-----------------|-----------|---------------|--------|
| **Type Validation** | String type enforcement | Automatic | Cannot be overridden |
| **Required Field** | Configurable requirement | `["yup.required"]` | Blocks form submission if empty |
| **Format Validation** | None | N/A | No pattern matching available |
| **Uniqueness Check** | None | N/A | Relies on range allocation |
| **Range Validation** | Internal only | Automatic | Prevents generation beyond allocated range |

### Range Exhaustion Handling

When allocated ranges deplete, the system implements sophisticated modal intervention:

1. **Automatic Detection**: Upon attempting to generate beyond range boundaries
2. **Modal Dialog Display**: Immediate UI blocking with configuration interface
3. **User Options**:
   - Add new range with custom start/stop values
   - View existing ranges with usage status
   - Disable exhausted ranges (cannot delete)
4. **Continuation**: After range allocation, generation proceeds immediately

### Critical Validation Gaps

The system deliberately omits several validation mechanisms:
- **No duplicate detection** across devices or forms
- **No range overlap prevention** during allocation
- **No server-side validation** of uniqueness
- **No referential integrity checking** with related records

These omissions reflect the offline-first philosophy where human coordination supersedes technical enforcement.

## Display Behaviour

### Interface Implementation

BasicAutoIncrementer employs a hidden field architecture, remaining invisible to users during normal data entry:

```javascript
// Rendering configuration from implementation
readOnly={true}
type={'hidden'}
```

#### Desktop Behaviour
- **Field Visibility**: Completely hidden from form interface
- **Value Display**: Only visible in read-only record views
- **Interaction**: None – purely programmatic generation
- **Settings Access**: Via notebook configuration interface

#### Mobile Platform Behaviour

##### iOS Implementation
- **Settings Access**: Through app settings menu
- **Range Management**: Native iOS modal presentation
- **Touch Targets**: Enlarged buttons for range configuration
- **Keyboard**: Not applicable (hidden field)

##### Android Implementation
- **Settings Access**: Via overflow menu or settings
- **Range Management**: Material Design bottom sheet
- **Touch Optimisation**: Follows Material Design specifications
- **Voice Input**: Not applicable (hidden field)

### Range Management Interface

The configuration modal provides comprehensive range control:

```
┌─────────────────────────────────────┐
│ Edit Settings for specimen_number   │
├─────────────────────────────────────┤
│ Current Ranges:                     │
│                                      │
│ 1-999    [In Use] [Disable]         │
│ 1000-1999 [Reserved] [Remove]       │
│ 2000-2999 [Fully Used]              │
│                                      │
│ [Add new range]                     │
│                                      │
│ Start: [____] End: [____]           │
│                                      │
│ [Cancel] [Done]                     │
└─────────────────────────────────────┘
```

## Interaction Patterns

### Generation Logic

The field implements sophisticated one-time generation with state preservation:

```javascript
// Simplified generation flow
if (current_value === null || current_value === '' || current_value === undefined) {
  // Generate new identifier
  const next_id = getNextAvailableId();
  if (next_id !== null) {
    setValue(next_id.toString().padStart(num_digits, '0'));
    setReadOnly(true);
  } else {
    // Trigger range allocation dialog
    openRangeManagementModal();
  }
} else {
  // Preserve existing value
  maintainReadOnlyState();
}
```

### Multi-Form Coordination

When multiple forms utilise auto-incrementers:

1. **Independent Counters**: Each form_id maintains separate sequence
2. **Shared Instance Counters**: Multiple instances of same form share counter
3. **No Cross-Form Conflicts**: Different forms can use identical ranges
4. **Persistent State**: Counters survive form deletion/restoration

### Range Allocation Workflow

The allocation process follows a specific interaction pattern:

1. **Initial Setup**: User allocates range before first record
2. **Progressive Usage**: Counter increments with each record
3. **Exhaustion Detection**: System detects range depletion
4. **Modal Intervention**: Immediate prompt for new range
5. **Continuation**: Seamless progression with new range

## Data Storage and Export

### Local Storage Architecture

Range allocations persist in PouchDB's local_state database with structured keys:

```
Storage Key Pattern:
local-autoincrement-state-[project_id]-[form_id]-[field_id]

Example:
local-autoincrement-state-heritage2024-specimen-form-spec_num

Storage Structure:
{
  ranges: [
    {
      start: 1,
      stop: 999,
      using: true,
      fully_used: false,
      last_used_id: 234
    }
  ]
}
```

**Critical Limitation**: Range state exists exclusively in local storage without cloud synchronisation, creating vulnerability to device loss.

### CSV Export Behaviour

The string type declaration introduces critical export considerations:

#### Excel Vulnerability
Without explicit quotation, Excel strips leading zeros:
- Database: "00042" (string)
- CSV export: 00042 (unquoted)
- Excel import: 42 (converted to number)
- Data integrity: **COMPROMISED**

#### Mitigation Strategy
Embed auto-incremented values within TemplatedString compositions:
```json
"template": "SPEC-{{auto_number}}-2024"
// Produces: "SPEC-00042-2024" (Excel preserves)
```

#### Export Format Preservation
Current implementation lacks forced string quotation:
```javascript
// Current (vulnerable):
stringify({columns, header: true, escape_formulas: true});

// Required (safe):
stringify({columns, header: true, escape_formulas: true, quoted_string: true});
```

## Common Patterns

### Pattern 1: Team-Based Range Allocation

For multi-team deployments with offline periods:

```json
{
  "specimen_id": {
    "component-namespace": "faims-custom",
    "component-name": "BasicAutoIncrementer",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "specimen_id",
      "label": "Specimen ID",
      "num_digits": 6,
      "form_id": "biological_specimen"
    },
    "validationSchema": [["yup.string"], ["yup.required"]],
    "initialValue": ""
  }
}
```

**Range Allocation Protocol**:
- Team Alpha: 100000–199999
- Team Beta: 200000–299999
- Team Gamma: 300000–399999
- Reserve: 400000–999999

### Pattern 2: Hierarchical Identifier Composition

For complex archaeological contexts:

```json
{
  "context_number": {
    "component-namespace": "faims-custom",
    "component-name": "BasicAutoIncrementer",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "context_number",
      "label": "Context Number",
      "num_digits": 4,
      "form_id": "archaeological_context"
    }
  },
  "full_context_id": {
    "component-namespace": "faims-custom",
    "component-name": "TemplatedStringField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "template": "{{site_code}}-{{trench}}-CTX{{context_number}}"
    }
  }
}
```

**Expected Output**: "SITE01-TR5-CTX0042"

### Pattern 3: Temporal Range Distribution

For long-term monitoring projects:

```json
{
  "sample_number": {
    "component-namespace": "faims-custom",
    "component-name": "BasicAutoIncrementer",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "sample_number",
      "label": "Sample Number",
      "num_digits": 5,
      "form_id": "water_sample"
    },
    "validationSchema": [["yup.string"], ["yup.required"]]
  }
}
```

**Annual Range Allocation**:
- 2024: 10000–19999
- 2025: 20000–29999
- 2026: 30000–39999

## Troubleshooting Guide

### Common Issues and Resolutions

#### Issue: "Cannot generate new identifier"
**Cause**: Range exhausted without user awareness  
**Solution**: 
1. Modal dialog should appear automatically
2. If not, access notebook settings manually
3. Allocate new range ensuring no overlap with existing allocations
4. Document new range in external log

#### Issue: Duplicate identifiers across devices
**Cause**: Overlapping range allocation between teams  
**Solution**:
1. Immediate: Continue data collection (duplicates won't block)
2. Post-fieldwork: Export data and add device prefix
3. Prevention: Implement rigorous range allocation protocol
4. Long-term: Compose with device identifier in TemplatedString

#### Issue: Leading zeros lost in Excel
**Cause**: Unquoted numeric strings in CSV export  
**Solution**:
1. Always embed in TemplatedString with alpha prefix
2. Post-process CSV with: `sed 's/,\([0-9]\{5\}\),/,"\1",/g'`
3. Import as text column in Excel
4. Train teams on Excel import procedures

#### Issue: Counter reset after app reinstallation
**Cause**: Local storage cleared with app data  
**Solution**:
1. Consult external range allocation log
2. Manually set new range starting from last used + 1
3. Update external documentation
4. Consider implementing local backup protocol

### Debug Checklist

- [ ] Verify `form_id` matches exactly across all instances
- [ ] Confirm `num_digits` consistent across deployment
- [ ] Check range allocation in device settings
- [ ] Inspect local_state database for orphaned ranges
- [ ] Validate no overlapping ranges across devices
- [ ] Ensure TemplatedString composition if Excel export required
- [ ] Verify external range documentation current
- [ ] Confirm all team members aware of allocation protocol

## Implementation Notes

### String Type Implications

The deliberate return of string rather than numeric types creates specific behavioural patterns that must be understood:

1. **Sorting Behaviour**: Alphabetical rather than numeric
   - "0002" precedes "0010" (correct when string-sorted)
   - "2" follows "10" (incorrect if zero-padding lost)
   - Recommendation: Maintain consistent padding width

2. **Computational Restrictions**: No mathematical operations
   - Cannot sum, average, or calculate with identifiers
   - Cannot use in numeric comparisons without parsing
   - Design intention: Identifiers aren't quantities

3. **Format Preservation**: Zero-padding maintained
   - Database stores exact string representation
   - Display maintains leading zeros
   - Critical for systems expecting fixed-width identifiers

### Performance Characteristics

- **Generation Speed**: Instantaneous (< 10ms)
- **Range Check Overhead**: Negligible (single comparison)
- **Storage Impact**: ~200 bytes per range allocation
- **Synchronisation Load**: None (local-only storage)
- **Memory Footprint**: Minimal (single counter per form)

### Architectural Constraints

The implementation embodies several immutable constraints:
- No server-side range coordination
- No automatic conflict resolution
- No range synchronisation between devices
- No backup mechanism for range state
- No prefix/suffix configuration within component
- No ability to edit generated values via UI

## Fieldwork Management Protocols

### Range Allocation Protocol

Successful deployment requires rigorous external coordination:

#### Centralised Allocation Registry

Maintain a cloud-accessible spreadsheet with mandatory fields:

| Device ID | User | Form ID | Range Start | Range End | Date Allocated | Status | Notes |
|-----------|------|---------|-------------|-----------|----------------|--------|-------|
| iPad-A001 | J. Smith | specimen | 1 | 999 | 2024-01-15 | Active | Site A deployment |
| iPad-A001 | J. Smith | specimen | 1000 | 1999 | 2024-03-20 | Reserved | Contingency |
| Phone-B002 | M. Jones | feature | 1 | 500 | 2024-01-15 | Exhausted | Completed 2024-02-10 |
| Phone-B002 | M. Jones | feature | 501 | 1000 | 2024-02-10 | Active | Current range |

#### Allocation Procedures

1. **Pre-Deployment Planning**
   - Estimate maximum records per device per form
   - Allocate ranges with 50% buffer for contingency
   - Document allocation in shared registry
   - Distribute registry to all team members

2. **During Fieldwork**
   - Check registry before any range modification
   - Update registry immediately upon allocation
   - Communicate changes via agreed channel
   - Maintain local copy for offline reference

3. **Post-Deployment Reconciliation**
   - Audit actual usage against allocations
   - Archive exhausted ranges
   - Plan future allocations based on usage patterns
   - Update procedures based on lessons learned

### Team Coordination Standards

#### Communication Requirements

Establish clear protocols for range management communication:

1. **Synchronous Communication** (when network available)
   - Instant messaging for immediate allocation needs
   - Video calls for allocation planning sessions
   - Real-time spreadsheet updates

2. **Asynchronous Coordination** (offline periods)
   - Pre-allocated range buffers
   - Written protocols for emergency allocation
   - Scheduled synchronisation windows

#### Conflict Resolution Procedures

When duplicate identifiers are discovered:

1. **Detection Phase**
   - Regular data audits during synchronisation
   - Automated duplicate detection scripts
   - Cross-reference with allocation registry

2. **Resolution Strategy**
   - Maintain both records (no data loss)
   - Add device suffix to disambiguate
   - Document in incident log
   - Adjust future allocation to prevent recurrence

### Device Loss Mitigation

Given local-only range storage, implement protective measures:

1. **Preventive Documentation**
   - Daily range status reports
   - End-of-day backup protocol
   - Photograph device settings screens
   - Maintain paper backup of allocations

2. **Recovery Procedures**
   - Consult allocation registry for last known state
   - Estimate lost range based on daily collection rate
   - Allocate new range with safety buffer
   - Document incident for audit trail

### Audit Trail Maintenance

Maintain comprehensive documentation for data integrity:

1. **Required Documentation**
   - Range allocation decisions and rationale
   - Daily usage statistics per device
   - Incident reports for conflicts or losses
   - Change log for allocation modifications

2. **Retention Policy**
   - Maintain during active fieldwork
   - Archive with project data
   - Preserve for data publication requirements
   - Include in data management plan

## Best Practices

- **Reserve ranges strategically** with 50–100% buffers to accommodate unexpected collection intensity whilst avoiding premature exhaustion
- **Document allocation rationale** to facilitate future projects with similar collection patterns and team structures
- **Implement device-specific prefixes** via TemplatedString composition when absolute uniqueness is critical
- **Establish range checkpoints** at natural project phases (weekly, per site, per campaign) to assess usage and adjust allocations
- **Train all team members** on range allocation protocols, ensuring redundant knowledge in case of personnel changes
- **Use power-of-10 boundaries** (1000s, 10000s) for human-readable range delimitation that minimises allocation errors
- **Compose identifiers defensively** against downstream tools by embedding numeric sequences within alphanumeric strings
- **Maintain allocation registry version control** to preserve decision history and enable allocation audit trails
- **Plan for device failure** by keeping recent range status documentation accessible to all team members
- **Standardise num_digits project-wide** to ensure consistent identifier formatting across all devices and forms

## See Also

- **TemplatedStringField**: For composing complex identifiers incorporating auto-incremented values with prefixes, suffixes, and contextual information
- **NumberInput**: When actual numeric values requiring mathematical operations are needed rather than sequential identifiers
- **TextField**: For non-sequential unique identifiers such as specimen codes, sample IDs from external systems, or barcoded labels
- **QRCodeFormField**: For capturing pre-existing identifiers via barcode scanning rather than generating new sequences
- **Select**: When identifiers must conform to predefined controlled vocabularies rather than sequential generation