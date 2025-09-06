<!-- concat:boundary:start section="implementation-patterns-guide" -->
<!-- concat:metadata
document_id: implementation-patterns-guide
category: patterns
version: 1.0
last_updated: 2025-01-06
purpose: Comprehensive guide to implementation patterns, troubleshooting, and best practices
source_documents:
  - patterns.md (18KB)
  - troubleshooting-framework-reference.md (9KB)
  - quick-start.md (12KB) - implementation examples only
-->

# Implementation Patterns Guide

## Overview

This guide consolidates implementation patterns, troubleshooting strategies, and best practices for Fieldmark v3. It addresses common technical challenges, performance optimization, data management patterns, and integration approaches discovered across all field types.

## Core System Architecture Patterns

### Distributed, Offline-First Architecture {#distributed-architecture}

**Pattern**: All field types operate within a distributed, offline-capable system with eventual consistency.

**Implications**:
- **Relationships**: Reciprocal updates delayed until sync
- **Auto-incrementers**: Sequence conflicts when multiple offline users
- **Validation**: Client-side only, no server verification
- **Media fields**: Local storage until sync opportunity
- **All fields**: Last-write-wins default, conflicts flagged in Control Centre

**Best Practices**:
1. Plan for sync delays and conflicts
2. Coordinate auto-increment ranges between devices
3. Design validation for offline scenarios
4. Consider battery impact of GPS/media fields
5. Document conflict resolution procedures

### Schema Evolution Flexibility {#schema-evolution}

**Pattern**: System intentionally allows post-deployment schema changes to accommodate emergent field research.

**Safe Changes**:
- Adding new optional fields
- Expanding validation ranges
- Adding vocabulary options
- Increasing field limits

**Breaking Changes**:
- Type changes (string→number)
- Multiple→single selection
- Adding required fields to existing data
- Removing fields with data

**Migration Strategy**:
```json
// Version 1: String field
{
  "site-id": {
    "component-name": "TextField",
    "type-returned": "faims-core::String"
  }
}

// Version 2: Add new numeric field instead of changing
{
  "site-id-legacy": {
    "component-name": "TextField",
    "hidden": true  // Hide but preserve
  },
  "site-id-numeric": {
    "component-name": "NumberField",
    "type-returned": "faims-core::Number"
  }
}
```

## Common Implementation Patterns

### Pattern: Auto-Increment Coordination {#auto-increment}

**Challenge**: Auto-increment fields stored locally, not synchronized.

**Solution**: Device-specific range allocation:

```json
{
  "sample-number": {
    "component-name": "BasicAutoIncrementer",
    "component-parameters": {
      "form_id": "sample-form",
      "label": "Sample Number"
    }
  }
}
```

**Coordination Protocol**:
1. Device A: Range 0001-1000
2. Device B: Range 1001-2000
3. Device C: Range 2001-3000
4. Document ranges in project README
5. Monitor usage and reallocate as needed

### Pattern: Human-Readable IDs {#human-readable-ids}

**Challenge**: Default IDs are cryptic UUIDs.

**Solution**: TemplatedStringField for meaningful identifiers:

```json
{
  "hrid": {
    "component-name": "TemplatedStringField",
    "component-parameters": {
      "template": "{{site-code}}-{{year}}-{{#sample-number}}{{sample-number}}{{/sample-number}}{{^sample-number}}000{{/sample-number}}",
      "label": "Record ID"
    }
  }
}
```

**Best Practices**:
- Include project/site prefix
- Add year for temporal context
- Use auto-incrementer for uniqueness
- Keep under 30 characters for usability

### Pattern: Complex Field Conditions {#complex-conditions}

**Challenge**: Photos, GPS, relationships can't be used in conditions.

**Solution**: Hidden indicator fields:

```json
{
  "photos": {
    "component-name": "TakePhoto"
  },
  "_has_photos": {
    "component-name": "TemplatedStringField",
    "component-parameters": {
      "template": "{{#photos}}yes{{/photos}}{{^photos}}no{{/photos}}",
      "hidden": true
    }
  },
  "photo-description": {
    "component-name": "MultilineTextField",
    "condition": {
      "operator": "equal",
      "field": "_has_photos",
      "value": "yes"
    }
  }
}
```

### Pattern: Performance-Optimized Forms {#performance-optimization}

**Challenge**: Forms may experience performance degradation with many fields per section (estimated ~50-100 based on code analysis).

**Solution**: Strategic form splitting:

```json
{
  "viewsets": {
    "basic-recording": {
      "views": ["essential-fields"],  // 20 fields
      "layout": "inline"
    },
    "detailed-recording": {
      "views": ["section-1", "section-2", "section-3"],  // 30 fields each
      "layout": "tabs"
    },
    "media-recording": {
      "views": ["photos", "files"],  // Separate media
      "layout": "inline"
    }
  }
}
```

## Performance Thresholds and Limits

### Field-Specific Performance Boundaries {#performance-limits}

**Important**: These are approximate thresholds extrapolated from code analysis. Actual performance depends heavily on device capabilities, browser, network conditions, and specific use cases. Test with your actual data and devices.

| Field Type | Estimated Good Performance | Possible Degradation | Likely Issues | Hard Limit |
|------------|---------------------------|---------------------|---------------|------------|
| Relationships | <50 | ~50-100 | >100 | None |
| Select/MultiSelect | <50 | ~50-100 | >100 | None |
| AdvancedSelect | <100 | ~100-500 | >500 | None |
| TakePhoto | <5 | ~5-10 | >10 | 20 (enforced) |
| Fields per section | <30 | ~30-50 | >50 | None |
| Conditional fields | <10 | ~10-20 | >20 | None |

### Optimization Strategies

1. **Split large forms**: Multiple smaller forms vs one large form
2. **Use conditional sections**: Hide irrelevant fields
3. **Separate media**: Dedicated forms for photos/files
4. **Limit options**: Aim for reasonable numbers in selection fields
5. **Avoid deep nesting**: Maximum 3-4 hierarchy levels

## Troubleshooting Framework

### Universal Diagnostic Steps {#diagnostics}

1. **Identify Symptoms** - What exactly is occurring?
2. **Check Console** - Browser/app console for errors
3. **Verify Platform** - iOS, Android, or Web-specific?
4. **Test Isolation** - Minimal test case?
5. **Check Configuration** - Valid JSON?
6. **Review Logs** - Sync, network, validation
7. **Document Pattern** - Reproducible steps

### Common Error Patterns

| Error | Cause | Fix |
|-------|-------|-----|
| `Cannot read property of undefined` | Missing null checks | Add optional chaining |
| `Maximum call stack exceeded` | Infinite loop | Check conditions |
| `Out of memory` | Large data/images | Reduce size |
| `Network timeout` | Slow connection | Retry/offline mode |
| `Permission denied` | Missing permissions | Check settings |

### Platform-Specific Debugging

**iOS**:
```javascript
// Safari Web Inspector
console.log('iOS state:', navigator.userAgent);
// Check memory
performance.memory
```

**Android**:
```javascript
// Chrome DevTools
chrome://inspect
// ADB logs
adb logcat | grep Fieldmark
```

**Web**:
```javascript
// Browser DevTools
debugger; // Breakpoint
console.time('Operation');
// ... operation
console.timeEnd('Operation');
```

## Data Management Patterns

### Export Strategy {#export-patterns}

**Challenge**: CSV exports lose structure, JSON preserves but isn't readable.

**Solution**: Dual export strategy:

1. **For Analysis**: CSV with flattened relationships
2. **For Archive**: JSON with full structure
3. **For Reimport**: JSON only (CSV can't preserve relationships)

### Relationship Export Format

**CSV Format**:
```csv
_id,identifier,relationships
ctx001,CTX-001,"cuts/ctx002;fills/ctx003"
```

**JSON Format**:
```json
{
  "relationships": [
    {
      "record_id": "ctx002",
      "relation_type_vocabPair": ["cuts", "is cut by"]
    }
  ]
}
```

### Database API Integration {#api-integration}

**Pattern**: Direct CouchDB access for external systems.

**Considerations**:
- No import validation exists
- Schema compliance not enforced
- Risk of corruption through malformed imports
- Document structure must match exactly

**Safe Integration**:
```javascript
// Read-only access pattern
const db = new PouchDB('https://server/database');
const doc = await db.get('record-id');

// Validated write pattern
const schema = loadSchema();
if (validateAgainstSchema(newDoc, schema)) {
  await db.put(newDoc);
}
```

## Security and Validation Patterns

### Client-Side Validation Only {#validation-patterns}

**Reality**: No server-side validation exists.

**Implications**:
- Data integrity depends on client
- Malformed data can be synced
- External API writes bypass validation

**Defensive Patterns**:
1. Validate at multiple points
2. Add data integrity checks
3. Document validation rules
4. Test edge cases thoroughly
5. Monitor for anomalies

### File Security Gaps {#security-gaps}

**Issues**:
- FileUploader accepts any file type
- No virus scanning
- Executables not blocked
- EXIF data handling inconsistent

**Mitigation**:
```json
{
  "document-upload": {
    "component-parameters": {
      "accept": ".pdf,.doc,.docx",  // Limit types
      "helperText": "PDF or Word documents only",
      "multiple": false  // Limit quantity
    }
  }
}
```

## Component Selection Patterns

### Choosing Between Similar Components {#component-selection}

| Need | Use | Don't Use | Why |
|------|-----|-----------|-----|
| Single-line text | TextField | FAIMSTextField | TextField is standard |
| Multi-line text | MultilineTextField | TextField with multiline | Clearer intent |
| 2-5 options | RadioGroup | Select | Better UX |
| 5+ options | Select | RadioGroup | Space efficient |
| Many options | AdvancedSelect | MultiSelect | Hierarchical support |
| Numbers | ControlledNumber | NumberField | Better validation |
| Auto ID | BasicAutoIncrementer | Manual entry | Consistency |

### Component Architecture Issues

**Known Problems**:
- TextField/FAIMSTextField duality unclear
- Component reference bugs (wrong error messages)
- TakePhoto and FileUploader overlap
- AdvancedSelect recursive rendering

**Workarounds**:
1. Prefer standard components
2. Test thoroughly on target platforms
3. Monitor memory usage
4. Have fallback options

## Mobile vs Desktop Patterns

### Platform Capability Matrix {#platform-matrix}

| Feature | iOS | Android | Web Desktop | Web Mobile |
|---------|-----|---------|-------------|------------|
| GPS | ✅ | ✅ | ⚠️ Limited | ⚠️ Limited |
| Camera | ✅ | ✅ | ⚠️ Varies | ⚠️ Varies |
| QR Scan | ✅ | ✅ | ❌ | ❌ |
| Offline | ✅ | ✅ | ✅ | ✅ |
| File Upload | ⚠️ | ⚠️ | ✅ | ⚠️ |

### Responsive Design Requirements

**Common Issues**:
- Fixed widths break mobile (500px)
- Touch targets too small (<44px)
- Keyboard types vary

**Solutions**:
```json
{
  "component-parameters": {
    "fullWidth": true,  // Responsive width
    "InputProps": {
      "style": {
        "minHeight": "44px"  // Touch target
      }
    }
  }
}
```

## Workflow Implementation Patterns

### Linear Survey Collection {#linear-workflow}

```json
{
  "sections": ["site", "context", "finds", "photos", "notes"],
  "navigation": "inline",
  "validation": "soft",
  "progress": "per-section"
}
```

**When to use**: Sequential data collection, minimal backtracking

### Hierarchical Recording {#hierarchical-workflow}

```json
{
  "parent": "excavation-unit",
  "children": ["contexts", "samples", "finds"],
  "navigation": "tabs",
  "sticky_fields": ["unit_id", "date"],
  "auto_save": true
}
```

**When to use**: One-to-many relationships, repeated child creation

### Conditional Workflow {#conditional-workflow}

```json
{
  "sections": {
    "basic": {"always": true},
    "archaeological": {"condition": "type == 'archaeological'"},
    "ecological": {"condition": "type == 'ecological'"}
  },
  "navigation": "breadcrumb",
  "skip_hidden": true
}
```

**When to use**: Dynamic forms, role-based sections

## Error Recovery Patterns

### Data Recovery Strategies {#error-recovery}

**Scenario**: Form crashes with unsaved data

**Recovery Steps**:
1. Check browser localStorage
2. Look for draft database entries
3. Check PouchDB: `indexedDB` in DevTools
4. Export any recoverable data
5. Reimport through API if needed

### Sync Conflict Resolution

**Pattern**: While last-write-wins is the default behavior, conflicts are flagged to users after sync.

**Conflict Resolution Process**:
1. Concurrent edits create conflicts during sync
2. Control Centre displays conflicts after sync
3. Users can review both versions
4. Choose winning version in Control Centre
5. Or manually merge and reimport if needed

**Note**: The conflict resolution module in Control Centre allows users to see and resolve conflicts, though the underlying system uses last-write-wins if no manual intervention occurs.

## Integration Patterns

### External System Integration {#integration}

**Current Integrations**:
- RSpace ELN (electronic lab notebook)
- QGIS (GIS software)
- CouchDB API direct access

**Integration Checklist**:
1. Document schema requirements
2. Validate before import
3. Test with minimal data
4. Monitor for conflicts
5. Plan rollback strategy

### API Usage Guidelines

```javascript
// Safe read pattern
async function readData() {
  try {
    const db = new PouchDB('database-url');
    const result = await db.allDocs({
      include_docs: true,
      startkey: 'record_',
      endkey: 'record_\ufff0'
    });
    return result.rows.map(r => r.doc);
  } catch (error) {
    console.error('Read failed:', error);
  }
}

// Validated write pattern
async function writeData(doc) {
  if (!validateDocument(doc)) {
    throw new Error('Invalid document structure');
  }
  return await db.put(doc);
}
```

## Best Practices Summary

### DO:
✅ Coordinate auto-increment ranges  
✅ Use human-readable IDs  
✅ Split large forms strategically  
✅ Test on minimum spec devices  
✅ Document known limitations  
✅ Plan for offline scenarios  
✅ Validate data at multiple points  
✅ Monitor performance metrics  

### DON'T:
❌ Change field types after deployment  
❌ Add excessive fields per section without testing performance  
❌ Use complex fields in conditions directly  
❌ Ignore platform differences  
❌ Skip validation on API writes  
❌ Assume sync is immediate  
❌ Trust client-side validation alone  

## Common Anti-Patterns to Avoid

1. **Monolithic forms**: Single form with excessive fields
2. **Uncoordinated auto-increment**: Duplicate IDs across devices
3. **Type mismatches**: String fields for numbers
4. **Deep hierarchies**: More than 4 levels
5. **Ignored performance testing**: Excessive relationships without testing
6. **No error handling**: Silent failures
7. **Platform assumptions**: Desktop-only testing

## Migration and Maintenance

### Version Migration Strategy

1. **Never change types in place** - Add new fields
2. **Preserve old data** - Hide rather than delete
3. **Document changes** - Maintain changelog
4. **Test thoroughly** - All platforms and scenarios
5. **Plan rollback** - Keep backups

### Maintenance Checklist

**Weekly**:
- Check sync status
- Monitor performance
- Review error logs

**Monthly**:
- Validate data integrity
- Update documentation
- Review usage patterns

**Quarterly**:
- Performance audit
- Security review
- Schema evaluation

## Related Documentation

- [Form Structure Guide](./form-structure-guide.md) - Architecture patterns
- [Dynamic Forms Guide](./dynamic-forms-guide.md) - Validation and conditions
- [Field Selection Guide](./field-selection-guide.md) - Choosing fields
- [Component Reference](../references/component-reference.md) - Technical details
- [Platform Reference](../references/platform-reference.md) - Platform-specific info

<!-- concat:boundary:end section="implementation-patterns-guide" -->