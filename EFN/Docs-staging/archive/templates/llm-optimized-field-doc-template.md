# LLM-Optimized Field Documentation Template

## Purpose
This template ensures consistency across all Fieldmark v3 field documentation. It provides detailed structure for sections that need expansion, particularly Platform Behaviors, Troubleshooting, and Diagnosis Tables.

## Document Structure with Priority Markers

### Priority Markers
- `{essential}` - Critical for basic usage
- `{important}` - Needed for effective implementation  
- `{comprehensive}` - Complete reference information

---

# [Field Category] Fields - Fieldmark v3 Documentation

## Overview {essential}
[Brief description of field category and components]

### DESIGNER QUICK GUIDE
[Key information for Designer users]

### CRITICAL NAMING DISAMBIGUATION
[Clarify confusing similar fields]

### Field Capabilities Summary
[One paragraph overview]

### Component Status
[Status table for all fields in category]

## Designer Usage Guide {essential}
### What to Select in Designer
[Designer selection instructions]

### When JSON Enhancement is Required
[JSON-only parameters]

### Designer Limitations {important}
[Link to Designer Limitations Reference]
[Category-specific limitations]

## Field Selection Guide {essential}
[Decision tree or selection criteria]

## ⚠️ Critical Security Risks {essential}
[Security warnings specific to field category]

## What This Field Cannot Do {important}
[Clear limitations]

## Common Use Cases {important}
[Typical usage patterns]

## Designer Component Mapping {essential}

### Designer UI vs JSON Component Names

| Designer UI Label | JSON component-name | Component Namespace | Description |
|------------------|--------------------|--------------------|-------------|
| [UI Name] | [JSON name] | [namespace] | [Brief description] |

### Designer Configuration Options

| Designer Option | JSON Parameter | Values | Description |
|----------------|----------------|---------|-------------|
| [Option] | `parameter` | [values] | [Description] |

⚠️ **Critical Notes**:
- [Important mapping notes]
- [Common confusion points]

## Designer Capabilities vs JSON Enhancement {essential}

### Designer Configuration
- ✅ [What Designer can configure]
- ⚠️ [Partial capability]
- ❌ [What requires JSON]

### JSON-Only Configuration
```json
{
  "parameter": "value"
}
```

## Component Namespace Errors {important}
[Link to Component Namespace Reference]
[Category-specific namespace errors]

## Common Characteristics {important}

### Security Considerations {important}
[Link to Security Considerations Reference]
**Category-Specific Security Notes:**
- [Unique security concerns]

### Performance Boundaries {important}
[Link to Performance Thresholds Reference]
**Category-Specific Performance:**
- [Performance metrics]
- [Thresholds]
- [Optimization triggers]

### Validation Patterns {important}
[Link to Validation Timing Reference]
**Category-Specific Validation:**
- [Validation behaviors]
- [Common patterns]

### Platform Behaviors {important}

#### iOS Specific Behavior
##### Camera and Media
- HEIC automatic conversion to JPG
- Camera permission prompts timing
- Photo Library vs Camera selection
- Memory limits (~200MB before crash)

##### GPS and Location  
- Location Services permission cascade
- Background GPS battery drain
- Accuracy stabilization time (30-60s)
- Altitude always 0 in simulator

##### UI Differences
- Touch targets: 36px (below 44px WCAG)
- Picker controls full-screen
- Keyboard avoidance automatic
- Safe area constraints

##### Performance
- WebView memory limits
- JavaScript execution time
- Local storage: 50MB limit
- Slower than native by ~2x

#### Android Specific Behavior
##### Permissions
- Runtime permission requests
- Storage access framework
- Location permission levels
- Camera2 API variations

##### File System
- External storage paths
- MediaStore integration  
- File size limitations
- URI vs File path issues

##### UI Differences
- Back button handling
- Material Design compliance
- Keyboard behavior variations
- WebView implementation differences

##### Performance
- Device fragmentation impact
- Memory management aggressive
- Background service restrictions
- Battery optimization interference

#### Web/Desktop Specific
##### Browser Differences
- Chrome: Full support
- Safari: IndexedDB limits
- Firefox: Camera API differences
- Edge: Legacy compatibility

##### Capabilities
- Drag-and-drop support
- Clipboard access
- File system access limited
- No native GPS (uses IP/WiFi)

##### Performance
- No memory constraints
- Faster processing
- Better debugging tools
- Network latency impacts

### Meta Properties {important}
[Link to Meta Properties Reference]
**Category-Specific Meta:**
- [Annotation usage]
- [Uncertainty patterns]

### Export Behavior {important}
[Link to Data Export Reference]
**Category-Specific Export:**
- [Export format]
- [Data structure]
- [Limitations]

## Field Reference {essential}

### [Field Name 1] {essential}

#### Purpose {essential}
[Field description]

#### Quick Reference
| Property | Required | Type | Default | Notes |
|----------|----------|------|---------|-------|
| [prop] | Yes/No | [type] | [default] | [notes] |

#### Core Configuration
```json
{
  "component-namespace": "faims-custom",
  "component-name": "ComponentName",
  "type-returned": "faims-core::Type",
  "component-parameters": {
    "name": "field-name",
    "label": "Field Label"
  }
}
```

#### Advanced Configuration
[Complex configuration examples]

#### Platform-Specific Behaviors
[Platform differences]

#### Common Issues & Solutions
[Troubleshooting specific to this field]

### [Field Name 2] {essential}
[Repeat structure for each field in category]

## Troubleshooting Guide {important}

### Common Issues

#### Issue: [Descriptive Problem Name]
**Symptoms**: 
- User sees: [exact behavior]
- Console shows: [error message if any]
- Occurs when: [trigger conditions]

**Affected Platforms**: iOS | Android | Web | All

**Root Causes**:
1. [Technical cause with explanation]
2. [Secondary cause if applicable]

**Diagnosis Steps**:
1. Check [specific thing]
2. Verify [configuration/setting]
3. Test [isolation step]

**Solutions**:
##### Quick Fix
```json
{
  "component-parameters": {
    "setting": "value"
  }
}
```

##### Permanent Solution
1. [Step-by-step instructions]
2. [Configuration changes needed]
3. [Testing verification]

**Prevention**:
- [Best practice]
- [Configuration guideline]
- [Testing recommendation]

**Related Issues**: 
- See [Other Issue Name]
- Check [Reference Document]

## JSON Examples {comprehensive}

### Example 1: [Basic Configuration Name]
```json
{
  "field-name": {
    "component-namespace": "faims-custom",
    "component-name": "ComponentName",
    "type-returned": "faims-core::Type",
    "component-parameters": {
      "name": "field-name",
      "label": "Field Label",
      "helperText": "Help text"
    },
    "validationSchema": [["yup.type"]],
    "initialValue": null
  }
}
```

### Example 2-20: [Various Use Cases]
[15-20 comprehensive examples showing different configurations]

## Migration Scenarios {comprehensive}

### Scenario 1: [Specific Migration Type]
**Context**: [When this migration is needed]

**Challenge**: [What makes this migration complex]
- [Specific technical issues]
- [Data format incompatibilities]  
- [Configuration changes required]

**Migration Steps**:
1. [Step-by-step process]
2. [With specific actions]
3. [And validation checks]

**Solution/Workaround**: [How to handle the migration]

### Scenario 2: [Another Migration Type]
**Context**: [Different migration need]

**Challenge**: [Different complexity]

**Solution**: [Approach to resolve]

[3-5 scenarios covering common field-specific migrations within Fieldmark v3]
[Note: FAIMS2 migrations moved to separate document]

## Best Practices {comprehensive}

### Design Principles
- [Field-specific design guidance]
- [Architectural recommendations]
- [Performance considerations]
- [User experience patterns]

### Performance Optimization
- [Field-specific optimizations]
- [Threshold management]
- [Resource usage patterns]
- [Scaling strategies]

### Data Quality Strategies  
- [Validation approaches]
- [Error prevention]
- [Consistency patterns]
- [Accuracy improvements]

### Common Patterns
- [Recommended workflows]
- [Integration approaches]
- [Configuration patterns]
- [Usage guidelines]

## Field Quirks Index (2025-01-03) {comprehensive}

### [Field Name] Quirks
- [Quirk 1 with explanation]
- [Quirk 2 with explanation]
- [Workaround if available]

## Performance Thresholds Summary {essential}

| Component | Threshold | Impact | Optimization |
|-----------|-----------|---------|--------------|
| [Component] | [Limit] | [What happens] | [How to optimize] |

## JSON Patterns Cookbook (2025-01-03) {comprehensive}

### Pattern: [Pattern Name]
**Use Case**: [When to use]
**Configuration**:
```json
{
  // Pattern implementation
}
```
**Notes**: [Important considerations]

## JSON Anti-patterns Quick Index {comprehensive}

### ❌ Anti-pattern: [Name]
**Why It's Bad**: [Explanation]
**What Happens**: [Consequences]
**Do Instead**: [Correct approach]

## Quick Diagnosis Tables (2025-01-03) {important}

### Symptom-Based Diagnosis
| Symptom | Field | Platform | Likely Cause | Quick Fix | Prevention |
|---------|-------|----------|--------------|-----------|------------|
| [User-visible problem] | [Component] | iOS/Android/All | [Root cause] | [Immediate action] | [Best practice] |

### Error Message Reference  
| Error Message | Component | Cause | Solution |
|--------------|-----------|-------|----------|
| "Cannot read property..." | [Component] | Null reference | Add null checks |

### Performance Degradation Patterns
| Scenario | Threshold | Impact | Optimization |
|----------|-----------|---------|--------------|
| [Scenario] | [Limit] | [Impact] | [Solution] |

## Field Interaction Matrix (2025-01-03) {important}

| Field | Commonly Paired With | Integration Pattern | Notes |
|-------|---------------------|-------------------|-------|
| [Field] | [Other fields] | [How they work together] | [Considerations] |

## Migration Warnings Index (2025-01-03) {comprehensive}

### Critical Migration Issues
1. **[Issue Name]**: [Description and impact]
2. **[Issue Name]**: [Description and impact]

## See Also {comprehensive}

### Other Field Categories
- **[Text Fields](./text-fields-v05.md)**: [Relationship description]
- **[Number Fields](./number-fields-v05.md)**: [Relationship description]
- **[DateTime Fields](./datetime-fields-v05.md)**: [Relationship description]
- **[Select/Choice Fields](./select-choice-fields-v05.md)**: [Relationship description]
- **[Media Fields](./media-fields-v05.md)**: [Relationship description]
- **[Location Fields](./location-fields-v05.md)**: [Relationship description]
- **[Relationship Field](./relationship-field-v05.md)**: [Relationship description]
- **[Display Field](./display-field-v05.md)**: [Relationship description]

### Reference Documents
- [Validation Timing Reference](../reference-docs/validation-timing-reference.md)
- [Component Namespace Reference](../reference-docs/component-namespace-reference.md)
- [Data Export Reference](../reference-docs/data-export-reference.md)
- [Security Considerations Reference](../reference-docs/security-considerations-reference.md)
- [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md)
- [Meta Properties Reference](../reference-docs/meta-properties-reference.md)
- [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md)
- [Formik Integration Reference](../reference-docs/formik-integration-reference.md)
- [Accessibility Reference](../reference-docs/accessibility-reference.md)

## Error Message Quick Reference {important}

### Category-Specific Errors
| Error | Field | Cause | Solution |
|-------|-------|-------|----------|
| [Error message] | [Field] | [Cause] | [Fix] |

## Metadata {comprehensive}
- **Document Version**: v05
- **Last Updated**: 2025-01-03
- **Status**: [Draft/Review/Final]
- **Target Audience**: Developers, Implementers, LLM Systems
- **Maintenance Notes**: [Any special maintenance requirements]

---

## Template Usage Notes

### When Creating New Documentation
1. Copy this template
2. Replace all [bracketed] placeholders
3. Remove sections not applicable to the field category
4. Ensure all examples are tested and working
5. Verify cross-references are correct
6. Update date stamps to current date

### Section Priorities
- Never skip {essential} sections
- Include all {important} sections for production docs
- {comprehensive} sections can be built incrementally

### Consistency Requirements
- Use exact section headings
- Maintain priority markers
- Keep table formats consistent
- Use same JSON formatting style
- Follow naming conventions

### Special Sections by Field Type

#### Media Fields Should Include
- File size and format specifics
- Upload/download behaviors
- Sync considerations
- Binary data handling

#### Location Fields Should Include
- Coordinate system details
- GPS accuracy information
- Offline map considerations
- Privacy implications

#### Relationship Fields Should Include
- Hierarchy patterns
- Vocabulary pair management
- Reciprocal update timing
- Performance with large datasets

#### Display Fields Should Include
- Content sanitization
- Memory leak details
- Rendering performance
- Markdown/HTML limitations