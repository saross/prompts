# Prompt 4: Structure and Tag Deduplicated Document

Transform the deduplicated document into final structured format matching datetime-fields-revised.md template.

## Instructions

### 1. Apply Complete Structure

```
# Number Input Fields

## Overview {essential}
   - Component list with Designer labels
   - Designer Quick Guide box
   - Component Status Summary table

## Field Selection Guide {essential}
   - Decision tree
   - Quick Decision Matrix table
   - Selection Strategy

## Designer Capabilities vs JSON Enhancement {essential}
   - What Designer Can Configure table
   - When JSON Enhancement is Required
   - Designer Component Mapping table

## Common Characteristics
   ### Configuration Rules {important}
   ### Validation Patterns {important}
   ### Security Considerations {important}
   ### Performance Boundaries {important}
   ### Platform Behaviors {important}
   ### Accessibility Compliance {important}
   ### Export Behavior {important}

## Individual Field Reference
   ### [NumberInput] {essential}
   <!-- keywords: numeric, integer, decimal, validation -->
   #### Purpose {essential}
   #### Key Features {essential}
   #### Configuration Parameters {important}
   #### Field-Specific Troubleshooting {important}
   #### Implementation Examples {comprehensive}
   
   ### [ControlledNumber] {essential}
   <!-- keywords: range, min-max, constrained, numeric -->
   [Same subsection structure]

## Troubleshooting Guide {important}
   ### Critical Issues Table {important}
   ### Common Problems Table {important}  
   ### Quick Fixes Table {important}
   ### Debug Checklists {comprehensive}

## JSON Examples {comprehensive}
   ### Base Patterns
   ### Anti-Patterns
   ### Platform-Specific Configurations
   ### Integration Patterns

## Migration and Best Practices {comprehensive}
   ### Migration Decision Tree
   ### Migration Warnings Index
   ### Migration Script Templates
   ### Training Requirements
   ### Alternative Approaches

## Field Quirks Index (2025-08) {comprehensive}
## Performance Thresholds Table (2025-08) {essential}
## Field Interaction Matrix (2025-08) {important}
## Quick Diagnosis Tables (2025-08) {important}
## Metadata
```

### 2. Depth Tag Requirements

**Mandatory tagging**:
- ALL section headers (##, ###)
- Maintain {essential}/{important}/{comprehensive} hierarchy
- If content was marked [VARIANT], tag as {important}
- If content was [SHARED], verify appropriate tag level

**Tag selection**:
- `{essential}` - Core functionality, must-know
- `{important}` - Common use cases, should-know
- `{comprehensive}` - Complete details, edge cases

### 3. Format Transformations

**Designer Integration**:
- Create "Designer Quick Guide" box near top
- Add Designer UI names in field headers: "### NumberInput (Number Field in Designer)"
- Include Designer mapping table in section 3

**Visual Markers**:
- ⚠️ Security vulnerabilities (top of relevant sections)
- ✅ Recommended practices
- ❌ Anti-patterns
- 🔴 Critical issues / 🟡 Important / 🟢 Minor

**Table Formatting**:
- Troubleshooting: | Symptom | Field | Cause | Solution |
- Performance: | Field | Metric | Threshold | Impact |
- Platform: | Platform | Behavior | Notes |

### 4. Content Organization

**Field Quirks Index Format**:
```
### NumberInput
- `RULE` Default behavior or requirement
- `QUIRK` Unexpected behavior
- `FIX` Solution or workaround
- `VERSION` 2025-08
```

**Cross-References**:
- Use [Section > Subsection] format
- Link shared content back to Common Characteristics
- Connect troubleshooting to specific fields

### 5. Verification Checklist

**Structure Compliance**:
- [ ] All 14 main sections present
- [ ] Every section has depth tag
- [ ] Keywords for each field
- [ ] Designer mapping complete
- [ ] Version markers (2025-08) added

**Content Preservation**:
- [ ] All SHARED content in Common Characteristics
- [ ] All VARIANT differences documented
- [ ] All field-specific content retained
- [ ] Security warnings prominent
- [ ] Platform limitations highlighted

**Format Standards**:
- [ ] Tables for troubleshooting (3 minimum)
- [ ] Visual markers applied
- [ ] Field quirks use RULE/QUIRK/FIX
- [ ] Cross-references formatted correctly

## DO NOT
- ❌ Delete any content
- ❌ Change technical information
- ❌ Skip sections from template
- ❌ Forget version markers
- ❌ Mix regular and anti-patterns

Output the fully structured and tagged document matching datetime-fields-revised.md format.