# RichText Field - Third Draft Documentation

## Overview

RichText (`faims-custom::RichText`) provides formatted instructional content and headings within forms through markdown rendering. Unlike data fields, RichText is purely presentational—it displays static content without capturing or storing user input. This component exists within the field architecture for consistency but does not participate in form validation, data storage, or export operations. Content is defined in the notebook configuration and rendered through a markdown-it parser with aggressive DOMPurify sanitization, prioritizing security over feature completeness. The implementation lacks memoization, causing content to be reparsed on every render, creating cumulative performance impact across multiple RichText fields.

Despite its `type-returned` declaration of `faims-core::String`, RichText never returns values—this declaration exists solely for architectural consistency. The field serves as the primary mechanism for providing methodological guidance, safety warnings, and section headings within data collection workflows. Critical limitations include memory leaks on mobile devices, no accessibility implementation, and feature discrepancies between Designer editing and runtime display.

## Common Use Cases

- Section headings to organize form structure (e.g., "Site Details", "Artifact Recording")
- Brief methodological instructions (1-3 sentences typical)
- Safety warnings and hazard notifications
- Data entry guidelines and formatting requirements
- Conditional help text responding to field selections
- Visual separators between form sections
- Copyright notices and attribution statements
- Quick reference information for field teams

**Not suitable for**:
- Long-form documentation (performance degrades over 1000 total words)
- Dynamic content generation (use TemplatedString instead)
- User input capture (use TextField or MultilineText)
- Complex tables or structured data (tables filtered at runtime)
- External image display (security blocks all external URLs)
- Content requiring frequent updates (stored in notebook definition)

## Core Configuration

### Required Parameters
```json
{
  "component-namespace": "faims-custom",
  "component-name": "RichText",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-id",
    "content": "# Heading\n\nInstructional text with **markdown** formatting."
  },
  "validationSchema": [["yup.string"]],
  "initialValue": ""
}
```

### Parameter Specifications
- **name**: Must match field ID (architectural requirement despite non-participation in data operations)
- **content**: Markdown-formatted string edited via Designer's MDX editor
- **type-returned**: Always `"faims-core::String"` (never actually returns values)
- **validationSchema**: Conventionally `[["yup.string"]]` but meaningless for display-only component
- **initialValue**: Always empty string `""` (no runtime value exists)

### Designer Interface
- **MDX Editor**: Full WYSIWYG markdown editor with dual-mode capability
- **Visual Mode**: Rich toolbar with formatting buttons
- **Source Mode**: Direct markdown editing with syntax highlighting
- **Toggle**: Switch between visual and source modes
- **Image Upload**: Converts to Base64 (external URLs blocked at runtime)
- **Table Editor**: Available but tables removed at runtime
- **No Validation**: Editor accepts invalid markdown without warning

## Validation Rules

**Not Applicable** - RichText is display-only and does not participate in validation.

Despite the presence of `validationSchema` in configuration, RichText:
- Never validates user input (no input exists)
- Always considered "valid" in form validation
- Cannot be "required" (no runtime value to validate)
- Does not trigger validation errors
- Ignores all validation rules if specified

The `validationSchema` property exists solely for architectural consistency with other field types but has no functional effect.

## Display Behaviour

### Rendering Pipeline
1. **Markdown Parsing**: markdown-it processes content with `typographer: true`
2. **HTML Sanitization**: DOMPurify strips dangerous elements with hardcoded whitelist
3. **DOM Injection**: Sanitized HTML inserted via `dangerouslySetInnerHTML`
4. **Re-rendering**: Process repeats on EVERY render without caching

### Platform Consistency
- **Desktop/iOS/Android**: Identical HTML rendering via WebView
- **No platform optimizations**: Same code path all platforms
- **Font differences**: iOS (San Francisco), Android (Roboto)
- **Performance varies**: iOS WebView generally faster than Android

### Memory Management Issues
**⚠️ CRITICAL**: No cleanup mechanisms implemented
- Parsed HTML accumulates in memory
- Previous forms' content not released
- Multiple large fields can crash mobile apps
- No garbage collection triggers
- Memory leaks compound with navigation

### Performance Characteristics
Content reparsed on every render (no memoization):

| Total Words Across All Fields | Parse Time | Impact |
|-------------------------------|------------|---------|
| <500 words | ~20-40ms | Acceptable |
| 500-1000 words | ~40-80ms | Noticeable on mobile |
| 1000-2000 words | ~80-160ms | Significant lag |
| >2000 words | >160ms | Severe performance issues |

**Triggers for reparse**:
- Any form field value change
- Parent component re-render
- Visibility condition changes
- Browser resize events

### Initial Load Impact
- Content included in initial payload (not lazy-loaded)
- All RichText fields parsed on form mount
- 10 fields × 50KB each = 500KB parsed immediately
- Mobile devices struggle with >1MB total content

## Interaction Patterns

**Not Applicable** - RichText provides no user interaction capabilities.

The field is purely presentational:
- No click handlers or interactive elements
- No hover states or tooltips
- No text selection restrictions
- No copy/paste handling
- Links in content are clickable (standard HTML behavior)

## Conditional Logic Support

### Visibility Conditions
```json
{
  "condition": {
    "operator": "equal",
    "field": "show-instructions",
    "value": true
  }
}
```

### Supported Features
- Standard operators: equal, not-equal, contains, etc.
- Complex conditions: AND/OR/NOT via nested conditions
- Can reference any field in current form
- Controller field pattern works normally

### Performance Warning
Each visibility toggle triggers full content reparse:
```json
// AVOID - causes reparse on every keystroke
"condition": {
  "operator": "contains",
  "field": "text-input-field",
  "value": "keyword"
}
```

## Data Storage and Export

### Storage Behavior
- **Location**: Notebook definition, NOT in record data
- **Sync**: With notebook updates, not record sync
- **Persistence**: Static content in configuration
- **Updates**: Require notebook redeployment

### Export Characteristics
- **CSV Export**: Not included (no data to export)
- **JSON Export**: Not included in record data
- **Notebook Export**: Content included in notebook definition
- **PDF Reports**: Would require custom implementation

### Offline Storage
- Counts against PouchDB storage limits (~50MB browser)
- Part of notebook metadata, not record data
- Large content affects notebook sync performance
- Mobile storage limits device-dependent

## Common Patterns

### Example 1: Section Header with Instructions
```json
{
  "recording-header": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "recording-header",
      "content": "## Site Recording\n\nRecord all visible features before excavation. Include photographic documentation from multiple angles."
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
*Behavior*: Displays formatted header with brief instructions. Content remains static, unaffected by form state. Parses ~10ms on each render.

### Example 2: Conditional Safety Warning
```json
{
  "hazard-warning": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "hazard-warning",
      "content": "### ⚠️ HAZARD WARNING\n\n**STOP** - This site requires:\n- Full PPE including respirator\n- Confined space certification\n- Gas monitoring equipment\n\nContact supervisor before entry."
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "",
    "condition": {
      "operator": "equal",
      "field": "site-type",
      "value": "confined-space"
    }
  }
}
```
*Behavior*: Displays only when site-type equals "confined-space". Each visibility toggle triggers ~15ms reparse. Emoji renders as Unicode character.

### Example 3: Multiple Brief Instructions
```json
{
  "measurement-guide": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "measurement-guide",
      "content": "**Measurement Protocol**\n\n1. Use metric units only\n2. Record to nearest centimeter\n3. Include uncertainty estimates"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
*Behavior*: Simple numbered list renders reliably. Brief content (~25 words) has minimal performance impact (~2ms parse time).

### Example 4: Form Introduction
```json
{
  "form-intro": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "form-intro",
      "content": "# Heritage Site Assessment\n\nThis form captures condition data for heritage structures.\n\n**Required**: GPS unit, camera, measuring tape"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```
*Behavior*: Provides context at form start. Bold text for emphasis. No interaction with other fields.

## Troubleshooting Guide

### Issue: Display Shows "Error"
**Symptoms**: Field displays literal text "Error" instead of content

**Causes**:
- Invalid markdown syntax
- Unclosed markdown tags
- Malformed HTML in content

**Debug Steps**:
1. Check browser console for parse errors
2. Review content in Designer source mode
3. Test problematic sections in external markdown validator
4. Common problems: Unclosed code blocks, malformed tables

**Solution**: Fix markdown syntax in Designer. No runtime recovery possible.

### Issue: Tables Disappear at Runtime
**Symptoms**: Tables visible in Designer but not in notebook

**Cause**: DOMPurify strips table tags for security

**Workaround Options**:
1. Use formatted lists instead of tables
2. Create image of table and embed as Base64
3. Use indented text with clear spacing
4. Consider PDF attachment for complex tables

### Issue: Mobile App Crashes
**Symptoms**: App crashes or becomes unresponsive with multiple RichText fields

**Causes**:
- Memory leak accumulation
- No cleanup of parsed HTML
- Large total content size

**Solutions**:
1. Limit total content to <1000 words across all RichText fields
2. Reduce number of RichText fields (<10 recommended)
3. Split large content across conditional fields
4. Restart app periodically to clear memory

### Issue: External Images Don't Display
**Symptoms**: Images show in Designer but not runtime

**Cause**: Security blocks all external image URLs (hardcoded)

**Solution**: Use Base64 embedded images only:
1. Keep images <100KB for performance
2. Use Designer's image upload tool
3. Optimize images before embedding
4. Consider icon fonts for simple graphics

### Issue: Performance Degradation
**Symptoms**: Form lag, slow response to input

**Diagnosis Checklist**:
- [ ] Count total words across all RichText fields
- [ ] Check for frequently toggling conditional visibility
- [ ] Monitor browser memory usage
- [ ] Test on target mobile devices

**Optimization Steps**:
1. Reduce content length (target <50 words per field)
2. Minimize conditional RichText fields
3. Avoid visibility conditions on frequently-changing fields
4. Consider static display for critical instructions

## Implementation Notes

### Technical Architecture
- **Parser**: markdown-it with `typographer: true` for smart quotes
- **Sanitizer**: DOMPurify with hardcoded whitelist
- **No Memoization**: Content reparsed every render
- **No Cleanup**: Memory leaks on component unmount
- **Security-First**: Cannot configure sanitization rules

### Designer Capabilities
**MDX Editor Features**:
- Visual WYSIWYG editing
- Source/preview toggle
- Rich formatting toolbar
- Table editor (though tables filtered at runtime)
- Image upload with Base64 conversion
- No content validation or error checking

### Designer-Runtime Feature Mismatch
| Feature | Designer Support | Runtime Display |
|---------|-----------------|-----------------|
| Tables | ✅ Full editor | ❌ Stripped |
| Blockquotes | ✅ Supported | ❌ Stripped |
| External Images | ✅ URL input | ❌ Blocked |
| Base64 Images | ✅ Upload tool | ✅ Displayed |
| Bold/Italic | ✅ Toolbar | ✅ Rendered |
| Headers | ✅ H1-H6 | ✅ Rendered |
| Lists | ✅ Ordered/Unordered | ✅ Rendered |

### Security Configuration
- **Hardcoded Whitelist**: Cannot be modified
- **External Domains**: Empty array, not configurable
- **Allowed Protocols**: http, https, mailto, tel only
- **JavaScript**: Completely blocked
- **Event Handlers**: All stripped
- **Custom Attributes**: Removed

### Accessibility Status
**⚠️ NOT WCAG COMPLIANT**:
- No ARIA attributes implemented
- No role definitions
- No alternative text mechanism
- No RTL text support (Arabic/Hebrew display incorrectly)
- Screen readers receive raw HTML only
- No semantic structure beyond markdown headings

## Best Practices

### Content Guidelines
- **Length**: Keep individual fields under 100 words
- **Total**: Limit to 1000 words across all RichText fields
- **Structure**: Use markdown headings for screen reader navigation
- **Images**: Embed only essential images, <100KB each
- **Tables**: Avoid (will be stripped) - use lists instead

### Performance Optimization
- **Field Count**: Maximum 10-15 RichText fields per form
- **Conditional Display**: Avoid frequent visibility toggles
- **Content Distribution**: Split large content across multiple forms
- **Mobile Testing**: Always test on target devices with real content

### Memory Management
- **Mobile Deployment**: Warn users about memory accumulation
- **App Restart**: Recommend periodic restart for long sessions
- **Content Audit**: Review and minimize RichText usage
- **Alternative Approaches**: Consider PDF attachments for lengthy instructions

### Authoring Workflow
1. Write content in Designer's visual mode
2. Toggle to source mode to verify markdown
3. Test in notebook preview (catches runtime filtering)
4. Check for "Error" display in console
5. Verify on mobile devices for memory impact

### Common Anti-Patterns to Avoid
- ❌ Using RichText for dynamic content
- ❌ Creating tables (they won't display)
- ❌ Embedding large images (>100KB)
- ❌ Writing documentation essays
- ❌ Conditional visibility on text input fields
- ❌ Assuming external images will work
- ❌ Ignoring memory accumulation on mobile

## See Also

- **[TextField](./TextField.md)** - For capturing user text input
- **[MultilineText](./MultilineText.md)** - For paragraph text capture
- **[TemplatedString](./TemplatedString.md)** - For dynamic content generation
- **[Conditional Logic Guide](../guides/ConditionalLogic.md)** - Visibility patterns
- **[Form Design Best Practices](../guides/FormDesign.md)** - Optimizing form performance
- **[Memory Management Guide](../guides/MemoryManagement.md)** - Mobile optimization strategies
- **[Accessibility Compliance](../guides/Accessibility.md)** - WCAG requirements and workarounds