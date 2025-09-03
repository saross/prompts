# Display Field - Fieldmark v3 Documentation

## Overview {essential}

### DESIGNER QUICK GUIDE
**Display Field Available:**
- **RichText** → Static formatted content and instructions

**Component Namespace:** `"faims-custom"`
**Component Name:** `RichText` (case-sensitive)
**Return Type:** `faims-core::String` (never actually returns values)
**Designer Support:** Full MDX editor with visual/source modes

### CRITICAL NAMING DISAMBIGUATION
- **RichText** - Static display-only content (NOT data capture)
- **NOT TemplatedStringField** - That's for dynamic identifier generation
- **NOT TextField/MultilineText** - Those capture user input
- Component uses namespace `"faims-custom"` despite being display-only
- Returns empty string always - no data storage

### Field Capabilities Summary
Provides formatted instructional content and section headings through markdown rendering. Purely presentational component that displays static content without capturing user input. Content defined in notebook configuration, parsed with markdown-it, and sanitized with DOMPurify. Critical performance issues with content over 1000 words total due to lack of memoization.

### Component Status
| Property | Status | Notes |
|----------|--------|-------|
| Designer Support | ✅ Full | MDX editor with preview |
| JSON Enhancement | Minimal | Content editing mainly |
| Validation | N/A | Display only |
| Performance | ⚠️ Poor | No memoization |
| Memory | ❌ Leaks | No cleanup on unmount |
| Accessibility | ❌ None | No ARIA support |

## Designer Usage Guide {essential}

### What to Select in Designer
1. Navigate to Field Type selection
2. Choose "Custom Field" category
3. Select "RichText"
4. Use MDX editor to create content:
   - Visual mode for WYSIWYG
   - Source mode for markdown
   - Toggle between modes

### When JSON Enhancement is Required
**Rarely needed - Designer handles most cases**
- Complex markdown structures
- Escaped special characters
- Multi-line content formatting
- Conditional visibility logic

### Designer Limitations {important}
See [Designer Limitations Reference](../reference-docs/designer-limitations-reference.md) for universal constraints.

**Display-Specific Designer Limitations:**
- Tables appear in Designer but stripped at runtime
- External images blocked despite Designer acceptance
- No content validation or syntax checking
- No performance warnings for large content
- Feature mismatch between edit and display

## Display Content Guide {essential}

### Content Type Decision Tree
```
Need to display content?
├─ Static instructions/warnings?
│  └─ YES → RichText
│     ├─ Markdown/HTML support
│     ├─ Security sanitized
│     └─ Best for: Headers, help text, warnings
│
├─ Dynamic identifiers?
│  └─ NO → Use TemplatedStringField instead
│
├─ User-editable content?
│  └─ NO → Use TextField/MultilineTextField instead
│
└─ Complex documentation?
   └─ NO → Consider PDF attachments
      └─ RichText degrades >1000 words
```

### Content Format Support
**Markdown Features:**
- Headers (H1-H6) ✅
- Bold/Italic ✅
- Ordered/Unordered lists ✅
- Links ✅
- Code blocks ✅
- Horizontal rules ✅

**Blocked Features:**
- Tables ❌ (stripped by sanitizer)
- Blockquotes ❌ (stripped)
- External images ❌ (security)
- JavaScript ❌ (all blocked)
- Custom HTML ❌ (sanitized)

### Styling Options
- Typography via markdown headers
- Bold/italic for emphasis
- Lists for structure
- Base64 embedded images only
- No custom CSS permitted
- Font varies by platform (iOS/Android)

## ⚠️ Critical Security Risks {essential}
**Security Implementation:**
- DOMPurify with aggressive whitelist
- All JavaScript blocked
- Event handlers stripped
- External URLs blocked for images
- Custom attributes removed

**Remaining Risks:**
- Base64 image size attacks
- Memory exhaustion via content
- Markdown parser DoS potential
- No content size limits enforced

**Mitigation:**
- Limit total content <1000 words
- Restrict Base64 images <100KB
- Monitor memory on mobile
- Test with production content

## What This Field Cannot Do {important}
- **Capture user input** - Display only
- **Store data** - Always returns empty
- **Display tables** - Stripped at runtime
- **Show external images** - Security blocked
- **Update dynamically** - Static content only
- **Support accessibility** - No ARIA attributes
- **Clean up memory** - Leaks on unmount
- **Cache parsed content** - Reparses every render

## Common Use Cases {important}
- **Section headings** - Organize form structure
- **Brief instructions** - 1-3 sentence guidance
- **Safety warnings** - Hazard notifications
- **Data guidelines** - Format requirements
- **Conditional help** - Context-sensitive text
- **Visual separators** - Between sections
- **Copyright notices** - Attribution text
- **Quick references** - Field team guides

## Designer Component Mapping {essential}
| Designer Option | JSON Configuration | Notes |
|-----------------|-------------------|-------|
| Field Type → RichText | `"component-name": "RichText"` | |
| MDX Editor Content | `"content": "markdown"` | Visual/source modes |
| Field Name | `"name": "field-id"` | Required despite no data |
| Conditions | `"condition": {}` | Standard visibility |

## Designer Capabilities vs JSON Enhancement {essential}

### Designer Configuration
- ✅ Full MDX editor
- ✅ Visual WYSIWYG mode
- ✅ Source markdown mode
- ✅ Image upload (Base64)
- ✅ Preview toggle
- ⚠️ Table editor (stripped runtime)

### JSON-Only Configuration
```json
{
  "content": "Complex\nmulti-line\nmarkdown",
  "condition": {
    "operator": "equal",
    "field": "other-field",
    "value": true
  }
}
```

## Component Namespace Errors {important}
See [Component Namespace Reference](../reference-docs/component-namespace-reference.md) for troubleshooting.

**Common Display Errors:**
- Using "RichTextDisplay" instead of "RichText"
- Confusing with TemplatedStringField
- Wrong return type expectations

## Common Characteristics {important}

### Security Considerations {important}
See [Security Considerations Reference](../reference-docs/security-considerations-reference.md) for comprehensive guidelines.

**Display-Specific Security Notes:**
- DOMPurify hardcoded whitelist
- No configuration override possible
- External domains empty array
- All JavaScript blocked
- Base64 images potential vector
- No CSP headers for embedded content

### Performance Boundaries {important}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for general limits.

**Display-Specific Performance:**
| Content Size | Parse Time | Impact |
|-------------|------------|---------|
| <500 words | 20-40ms | Acceptable |
| 500-1000 words | 40-80ms | Noticeable mobile |
| 1000-2000 words | 80-160ms | Significant lag |
| >2000 words | >160ms | Severe issues |

**Reparse Triggers:**
- Any field value change
- Parent re-render
- Visibility toggle
- Browser resize

### Validation Patterns {important}
See [Validation Timing Reference](../reference-docs/validation-timing-reference.md) for universal behavior.

**Display-Specific Validation:**
- No validation performed
- Always considered valid
- Cannot be required
- Schema ignored if present
- Never triggers errors

### Platform Behaviors {important}
**All Platforms:**
- WebView HTML rendering
- No platform optimizations
- Memory leaks universal

**Platform Differences:**
- iOS: San Francisco font
- Android: Roboto font
- iOS: Generally faster WebView
- Android: Slower parse times

### Meta Properties {important}
See [Meta Properties Reference](../reference-docs/meta-properties-reference.md) for configuration.

**Note:** RichText fields do not support annotations or uncertainty (display-only purpose)

### Export Behavior {important}
See [Data Export Reference](../reference-docs/data-export-reference.md) for universal patterns.

**Display-Specific Export:**
- **CSV**: Not included (no data)
- **JSON**: Not in record data
- **Notebook**: Content in definition
- **PDF**: Requires custom implementation
- Always exports empty string if referenced

## Field Reference {essential}

### RichText {essential}

#### Purpose {essential}
Provides formatted instructional content and section headings within forms through markdown rendering. Purely presentational component for static content display without data capture or storage capabilities.

#### Quick Reference
| Property | Details |
|----------|---------|
| Component | `faims-custom::RichText` |
| Returns | `faims-core::String` (always empty) |
| Designer | ✅ Full MDX editor |
| Data Storage | ❌ None |
| Performance | ⚠️ No caching |
| Memory | ❌ Leaks |
| Accessibility | ❌ No ARIA |
| Security | ✅ DOMPurify sanitized |

#### Core Configuration
```json
{
  "component-namespace": "faims-custom",
  "component-name": "RichText",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "instructions",
    "content": "## Recording Instructions\n\nCapture all visible features before excavation."
  },
  "validationSchema": [["yup.string"]],
  "initialValue": ""
}
```

#### Advanced Configuration
```json
{
  "safety-warning": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "safety-warning",
      "content": "# ⚠️ SAFETY WARNING\n\n**STOP** - Hazardous site requires:\n\n- Full PPE including respirator\n- Confined space certification\n- Gas monitoring equipment\n- Emergency evacuation plan\n\nContact supervisor before entry.\n\n---\n\n*Failure to comply may result in serious injury or death.*"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "",
    "condition": {
      "operator": "equal",
      "field": "site-classification",
      "value": "hazardous"
    }
  }
}
```

#### Platform-Specific Behaviors
- **Desktop**: Full markdown rendering
- **Mobile**: Memory accumulation issues
- **All**: No cleanup mechanisms
- **Performance**: Degrades with content size

#### Common Issues & Solutions
| Issue | Cause | Solution |
|-------|-------|----------|
| Shows "Error" | Invalid markdown | Fix syntax in Designer |
| Tables missing | Security strips | Use lists instead |
| App crashes | Memory leak | Limit to <1000 words |
| Images missing | External URLs blocked | Use Base64 only |
| Slow form | Content reparsing | Reduce RichText count |

## Troubleshooting Guide {important}

### Performance Issues
1. Count total words across all RichText
2. Check conditional visibility frequency
3. Monitor browser memory usage
4. Test on target mobile devices
5. Consider splitting content

### Display Problems
- Verify markdown syntax
- Check for unclosed tags
- Test in notebook preview
- Review browser console
- Confirm Base64 images

### Memory Management
- Restart app periodically
- Limit field count <10
- Keep content brief
- Avoid large images
- Monitor mobile memory

## JSON Examples {comprehensive}

### Section Header
```json
{
  "section-header": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "component-parameters": {
      "name": "section-header",
      "content": "# Site Documentation\n\nComplete all required fields below."
    }
  }
}
```

### Conditional Instructions
```json
{
  "method-instructions": {
    "component-parameters": {
      "content": "### Excavation Method\n\nUse 10cm spits for mechanical excavation."
    },
    "condition": {
      "operator": "equal",
      "field": "excavation-type",
      "value": "mechanical"
    }
  }
}
```

### Multi-section Guide
```json
{
  "recording-guide": {
    "component-parameters": {
      "content": "## Recording Standards\n\n### Photography\n- Multiple angles\n- Include scale\n\n### Measurements\n- Metric only\n- Nearest cm"
    }
  }
}
```

### Warning with Emphasis
```json
{
  "critical-warning": {
    "component-parameters": {
      "content": "**⚠️ CRITICAL**\n\nDo NOT proceed without safety officer present.\n\n*This is a mandatory requirement.*"
    }
  }
}
```

## Migration and Best Practices {comprehensive}

### Content Guidelines
- **Length**: <100 words per field
- **Total**: <1000 words all fields
- **Structure**: Use markdown headers
- **Images**: <100KB Base64 only
- **Tables**: Avoid completely

### Performance Optimization
- Maximum 10-15 RichText per form
- Avoid frequent visibility toggles
- Split large content across forms
- Test on actual mobile devices
- Monitor memory consumption

### Authoring Workflow
1. Write in Designer visual mode
2. Verify in source mode
3. Test in notebook preview
4. Check browser console
5. Verify on mobile devices

### Common Anti-patterns
- ❌ Using for dynamic content
- ❌ Creating tables
- ❌ Large images (>100KB)
- ❌ Long documentation
- ❌ Frequent conditional toggling
- ❌ External image URLs
- ❌ Ignoring mobile memory

## Field Quirks Index (2025-01) {comprehensive}
- Tables stripped despite Designer support
- External images blocked silently
- Memory leaks never cleaned
- Content reparsed every render
- No accessibility implementation
- "Error" display for invalid markdown
- Base64 images inline in JSON
- No content size validation

## Performance Thresholds Summary {essential}
See [Performance Thresholds Reference](../reference-docs/performance-thresholds-reference.md) for detailed metrics.

**Display-Specific Thresholds:**
| Metric | Threshold | Impact |
|--------|-----------|---------|
| Parse time | >80ms | User notices lag |
| Total content | >1000 words | Performance degrades |
| Field count | >15 | Memory issues |
| Image size | >100KB | Slow rendering |
| Reparse frequency | >10/sec | Severe lag |

## JSON Patterns Cookbook (2025-01) {comprehensive}

### Pattern: Conditional Help Text
```json
{
  "condition": {
    "operator": "is-truthy",
    "field": "needs-help"
  }
}
```

### Pattern: Section Separator
```json
{
  "content": "---\n\n## Next Section"
}
```

### Pattern: Embedded Image
```json
{
  "content": "![Icon](data:image/png;base64,iVBORw...)"
}
```

## JSON Anti-patterns Quick Index {comprehensive}

### ❌ Don't: Large Content Blocks
```json
// WRONG - Performance killer
{
  "content": "2000+ word essay..."
}
```

### ❌ Don't: External Images
```json
// WRONG - Will be blocked
{
  "content": "![Image](https://external.com/image.jpg)"
}
```

### ❌ Don't: Tables
```json
// WRONG - Stripped at runtime
{
  "content": "| Col1 | Col2 |\n|------|------|\n| Data | Data |"
}
```

## Quick Diagnosis Tables (2025-01) {important}

### Display Issues Diagnosis
| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| Shows "Error" | Invalid markdown | Check syntax |
| No tables | Security strips | Use lists |
| Missing images | External URLs | Use Base64 |
| Slow render | Large content | Reduce words |
| Memory crash | Leak accumulation | Restart app |

## Field Interaction Matrix (2025-01) {important}

### RichText with Other Fields
| Field Combination | Interaction | Pattern |
|------------------|-------------|---------|
| RichText + Conditions | Performance impact | Reparse on toggle |
| RichText + Any field | No data interaction | Display only |
| Multiple RichText | Memory accumulation | Limit count |
| RichText + TemplatedString | Different purposes | Static vs dynamic |

## Migration Warnings Index (2025-01) {comprehensive}

### Critical Migration Issues
1. **Tables won't display** - Designer shows but runtime strips
2. **Memory leaks accumulate** - No cleanup implemented
3. **Performance degrades** - No content caching
4. **External images fail** - Security blocks all
5. **No accessibility** - Screen readers unsupported
6. **Base64 size matters** - Impacts JSON size
7. **Content in notebook** - Not in record data

## See Also {comprehensive}
- **TemplatedStringField**: For dynamic content generation
- **TextField**: For user text input
- **MultilineTextField**: For paragraph input
- **Reference Documents:**
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

### Display-Specific Errors
| Error | Cause | Solution |
|-------|-------|----------|
| "Error" display | Malformed markdown | Fix syntax |
| Console parse error | Invalid content | Check markdown |
| Memory warning | Leak accumulation | Reduce content |
| Blank field | Content property empty | Add content |
| Performance warning | Too much content | Split fields |

## Metadata {comprehensive}
- **Document Version**: v05 (transformed)
- **Source Document**: display.md (Third Draft - RichText)
- **Platform Version**: Fieldmark v3 (January 2025)
- **Field Count**: 1 (RichText)
- **Key Limitations**: Memory leaks, no caching, tables stripped, no accessibility
- **Performance Critical**: Yes - degrades with content
- **Reference Docs**: 9 linked documents