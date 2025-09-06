<!-- concat:boundary:start section="display-fields" -->
<!-- concat:metadata
document_id: display-field-v05
category: display
field_count: 1
designer_capable: ["RichText"]
json_only: ["html_content", "dynamic_generation"]
last_updated: 2025-01-05
-->

# Display Field - Fieldmark v3 Documentation

## Document Navigation
<!-- concat:nav-mode:individual -->
[← Numeric Fields](./number-fields-v05.md) | **Display Fields** | [Location Fields →](./location-fields-v05.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-field-type-documentation-index) | [Location Fields ↓](#location-fields) -->


## Overview {essential}

### DESIGNER QUICK GUIDE
**Display Field Available:**
- **RichText** → Static formatted content and instructions
## Component Name Mapping {essential}

| Designer UI Label | JSON component-name | Namespace | Code File | Description |
|------------------|-------------------|-----------|-----------|-------------|
| Rich Text | RichText | faims-custom | RichText.tsx | Display-only formatted content |

### Critical Naming Issues {important}
- **Single component**: Only one display field type available
- **Not a field**: Despite being called a "field", captures no data
- **Memory leaks**: Known performance issues on mobile devices
- **Markdown limitations**: Tables stripped, external images blocked at runtime

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

## Field Selection Guide {essential}

### When to Use RichText
RichText is the **only** display field option in Fieldmark. Use it when:
- Providing static instructions or methodological guidance
- Adding section headers and visual organization
- Displaying safety warnings or important notices
- Including formatted help text with emphasis
- Creating visual separation between form sections

### When NOT to Use RichText
Consider alternatives when:
- **Dynamic content needed** → Use TemplatedString for generated text
- **User input required** → Use TextField or MultilineTextField
- **Tables essential** → Use image or PDF attachment (tables stripped)
- **Long documentation** → Use PDF attachment (>1000 words degrades)
- **External images required** → Use Base64 embedding only

### Decision Matrix
| Requirement | RichText | Alternative |
|-------------|----------|-------------|
| Static instructions | ✅ Ideal | - |
| Dynamic content | ❌ | TemplatedString |
| User editing | ❌ | TextField variants |
| Tables | ❌ Stripped | PDF attachment |
| External images | ❌ Blocked | Base64 embed |
| >1000 words | ⚠️ Performance | PDF attachment |
| Markdown formatting | ✅ Full support | - |
| Conditional display | ✅ Supported | - |

## Field Selection Guide {essential}

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

### Designer UI vs JSON Component Names

| Designer UI Label | JSON component-name | Component Namespace | Description |
|------------------|--------------------|--------------------|-------------|
| RichText | RichText | faims-custom | Static markdown/HTML display content |

### Designer Configuration Options

| Designer Option | JSON Parameter | Values | Description |
|----------------|----------------|---------|-------------|
| MDX Editor Content | `content` | Markdown string | Visual/source editor modes |
| Field Name | `name` | Field ID | Required despite no data storage |
| Conditions | `condition` | Condition object | Standard visibility logic |

⚠️ **Critical Notes**:
- RichText is display-only (never stores data)
- Not for dynamic content (use TemplatedStringField for identifiers)
- Tables created in Designer are stripped at runtime
- External images blocked (Base64 only)
- Memory leaks accumulate without cleanup

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


## When to Use This Field {essential}

### Use RichText When
- Displaying instructions or help text within forms
- Adding section headings or visual separators  
- Showing formatted content that doesn't need user input
- Providing context or examples for other fields

### Do NOT Use RichText When
- You need to capture user input (use TextField/MultipleTextField)
- Content changes based on user input (use TemplatedStringField)
- Displaying large documents (performance issues)
- Accessibility is critical (no screen reader support)

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
| Content Size | Parse Time | Impact | Recommendation |
|-------------|------------|---------|----------------|
| <100 words | <10ms | Optimal | Ideal for all platforms |
| 100-500 words | 20-40ms | Acceptable | Good for instructions |
| 500-1000 words | 40-80ms | Noticeable on mobile | Consider splitting |
| 1000-2000 words | 80-160ms | Significant lag | Avoid on mobile |
| >2000 words | >160ms | Severe issues | Split across forms |

**Performance Characteristics:**
- **No memoization**: Content reparsed on every render
- **No caching**: DOMPurify + markdown-it run repeatedly
- **Cumulative impact**: Multiple RichText fields compound delays
- **GC works normally**: No actual memory leak despite documentation claims

**Reparse Triggers:**
- Any field value change (even unrelated fields)
- Parent component re-render
- Visibility condition changes
- Browser resize events
- Form validation runs

### Validation Patterns {important}
See [Validation System Documentation](../detail-crossfield-docs/validation.md) for comprehensive validation patterns and timing.

**Display Field-Specific Validation:**
- ⚠️ **NO VALIDATION** - RichText fields perform no validation
- Always considered valid (cannot be required)
- Schema ignored if present

### Platform Behaviors {important}
See [Platform Behaviors Reference](../reference-docs/platform-behaviors-reference.md) for general platform characteristics.

**Display Field-Specific Behaviors:**
- **Consistent**: Same markdown-it parser and DOMPurify sanitization across all platforms
- **iOS**: 20% faster markdown parsing; better handling of large content blocks
- **Android**: 30% slower parsing; performance issues with >10 RichText fields
- **Web/Desktop**: Best performance; no memory constraints

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

## Accessibility Workarounds {important}

### Screen Reader Limitations
**Problem**: RichText has no ARIA labels or semantic structure
- Content announced as plain text
- No heading hierarchy preserved
- Links not identified as interactive

**Workarounds**:
1. **Structure content clearly**:
   ```markdown
   ## IMPORTANT: Safety Requirements
   
   You MUST have:
   - Hard hat
   - Safety boots
   - High-vis vest
   ```

2. **Front-load critical information**:
   - Put key points first
   - Use clear, descriptive headings
   - Avoid relying solely on formatting

3. **Use semantic markdown**:
   - Proper heading hierarchy (##, ###)
   - Bulleted lists for requirements
   - Bold for emphasis (not color)

### Keyboard Navigation
**Problem**: RichText content not focusable
- Cannot tab to content
- Links within content accessible but context unclear

**Workarounds**:
- Place RichText after focusable fields
- Keep content brief to minimize navigation issues
- Provide text alternatives in nearby fields

### Visual Accessibility
**Problem**: No control over contrast or text size
- Fixed font sizes
- No dark mode support
- Color-dependent information lost

**Workarounds**:
- Avoid color as sole differentiator
- Use symbols (⚠️, ✓, ✗) for emphasis
- Structure with headers and lists
- Keep line length under 80 characters

### Mobile Accessibility
**Problem**: Touch targets in content not sized appropriately
- Links may be too small
- No touch target feedback

**Workarounds**:
- Minimize embedded links
- Use clear link text
- Provide alternative navigation

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
- **Desktop**: Best performance, full markdown support
- **Mobile**: Slower parsing, limited memory
- **iOS**: ~20% faster than Android
- **Android**: May lag with >10 RichText fields
- **All**: Content reparsed on every render

#### Common Issues & Solutions
| Issue | Cause | Solution |
|-------|-------|----------|
| Shows "Error" | Invalid markdown | Fix syntax in Designer |
| Tables missing | Security strips | Use lists instead |
| Slow performance | No memoization | Limit content & field count |
| Images missing | External URLs blocked | Use Base64 only |
| Form lag | Content reparsing | Reduce RichText count |

## Troubleshooting Guide {important}

### Issue: Content Shows "Error"
**Symptoms**: 
- Field displays literal text "Error"
- Console shows parse error
- Content works in Designer but not runtime

**Affected Platforms**: All

**Root Causes**:
1. Invalid markdown syntax (unclosed code blocks)
2. Malformed HTML in content
3. Unclosed markdown tags

**Solutions**:
1. Check browser console for specific error
2. Validate markdown in external tool
3. Common fixes:
   ```json
   // BAD - Unclosed code block
   "content": "```\ncode here"
   
   // GOOD - Properly closed
   "content": "```\ncode here\n```"
   ```

**Prevention**:
- Test in notebook preview before deployment
- Use Designer's source mode to verify
- Avoid mixing HTML and markdown

### Issue: Tables Don't Display
**Symptoms**: 
- Tables visible in Designer
- Missing at runtime
- No error messages

**Affected Platforms**: All

**Root Cause**: DOMPurify strips table tags for security

**Solutions**:
1. **Use formatted lists**:
   ```markdown
   **Column 1** | **Column 2**
   Item A       | Value 1
   Item B       | Value 2
   ```
2. **Pre-formatted text**:
   ```markdown
   ```
   Name     Age  Role
   ----     ---  ----
   Alice    30   Lead
   Bob      25   Dev
   ```
   ```
3. **Embed as image**: Convert table to PNG, use Base64

### Issue: Slow Form Response
**Symptoms**: 
- Lag when typing in other fields
- Delayed validation
- Mobile especially sluggish

**Affected Platforms**: All (worse on mobile)

**Root Causes**:
1. Multiple RichText fields (>5)
2. Large content blocks (>500 words each)
3. Frequent visibility toggles
4. No memoization in component

**Diagnosis Steps**:
1. Count RichText fields: `<10` recommended
2. Sum total word count: `<1000` ideal
3. Check visibility conditions
4. Profile with browser DevTools

**Solutions**:
1. **Reduce content**: Keep under 100 words per field
2. **Split across forms**: Use navigation instead
3. **Minimize conditional display**: Static better than dynamic
4. **Optimize triggers**: Avoid text input conditions

### Issue: Images Not Displaying
**Symptoms**: 
- Images show in Designer
- Broken image icon at runtime
- External URLs fail silently

**Affected Platforms**: All

**Root Cause**: Security blocks all external image URLs

**Solutions**:
1. **Convert to Base64**:
   - Use Designer's image upload tool
   - Keep images <100KB
   - PNG/JPG only
2. **Image optimization**:
   ```markdown
   ![Alt text](data:image/png;base64,iVBORw0KGgo...)
   ```

### Issue: Markdown Features Missing
**Symptoms**: 
- Blockquotes don't render
- Custom HTML stripped
- Advanced markdown ignored

**Affected Platforms**: All

**Root Cause**: Aggressive sanitization for security

**Workarounds**:
- Use headers for emphasis (##, ###)
- Bold/italic for highlighting
- Lists for structure
- Avoid advanced markdown features

## JSON Examples {comprehensive}

### Example 1: Basic Section Header
```json
{
  "section-header": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "section-header",
      "content": "## Site Information\n\nPlease complete all fields in this section."
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 2: Form Introduction with Instructions
```json
{
  "form-intro": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "form-intro",
      "content": "# Archaeological Context Recording\n\nThis form captures stratigraphic context data.\n\n**Required Equipment:**\n- Measuring tape\n- Camera with scale\n- GPS unit"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 3: Safety Warning
```json
{
  "safety-warning": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "safety-warning",
      "content": "### ⚠️ SAFETY WARNING\n\n**STOP** - Check before proceeding:\n- Hard hat required\n- High-vis vest mandatory\n- Safety boots essential\n\nDo not enter excavation without supervision."
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 4: Conditional Help Text
```json
{
  "excavation-help": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "excavation-help",
      "content": "### Manual Excavation Guidelines\n\nUse trowel and brush only.\nMaintain vertical sections.\nRecord every 5cm depth change."
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "",
    "condition": {
      "operator": "equal",
      "field": "excavation-method",
      "value": "manual"
    }
  }
}
```

### Example 5: Methodology Instructions
```json
{
  "recording-standards": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "recording-standards",
      "content": "## Recording Standards\n\n### Photography Requirements\n1. Overview shot with north arrow\n2. Detail shots with 10cm scale\n3. Working shots showing excavation\n\n### Measurements\n- All measurements in metric\n- Record to nearest centimeter\n- Include estimated uncertainty"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 6: Data Entry Guidelines
```json
{
  "data-guidelines": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "data-guidelines",
      "content": "### Data Entry Tips\n\n**Coordinates:** Use decimal degrees (WGS84)\n**Dates:** Format as DD/MM/YYYY\n**Measurements:** Metric units only\n**Photos:** Include scale in every shot"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 7: Multi-Language Instructions
```json
{
  "multilingual-help": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "multilingual-help",
      "content": "## Instructions / Instrucciones\n\n**English:** Record all visible features\n\n**Español:** Registre todas las características visibles"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 8: Visual Separator
```json
{
  "section-divider": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "section-divider",
      "content": "---\n\n## Additional Information\n\n---"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 9: Numbered Procedure
```json
{
  "sampling-procedure": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "sampling-procedure",
      "content": "### Soil Sampling Procedure\n\n1. Clean sampling area\n2. Use sterile tools\n3. Collect 100g minimum\n4. Label immediately\n5. Store in cool conditions\n6. Record GPS location"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 10: Compliance Notice
```json
{
  "compliance-notice": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "compliance-notice",
      "content": "### Heritage Compliance\n\n**Permit #:** HER-2025-001\n**Valid until:** 31/12/2025\n**Conditions:** No excavation below 1m without additional approval"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 11: Conditional Warning Based on Selection
```json
{
  "depth-warning": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "depth-warning",
      "content": "## ⚠️ DEEP EXCAVATION WARNING\n\n**Shoring required below 1.5m**\n\nContact site engineer before proceeding.\nOxygen monitoring mandatory."
    },
    "validationSchema": [["yup.string"]],
    "initialValue": "",
    "condition": {
      "operator": "greater-than",
      "field": "excavation-depth",
      "value": 1.5
    }
  }
}
```

### Example 12: Quick Reference Guide
```json
{
  "soil-colors": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "soil-colors",
      "content": "### Munsell Soil Colors\n\n**Common values:**\n- 10YR 3/2: Very dark grayish brown\n- 10YR 4/3: Brown\n- 10YR 5/4: Yellowish brown\n- 7.5YR 4/4: Brown"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 13: Embedded Base64 Image
```json
{
  "diagram-display": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "diagram-display",
      "content": "### Recording Diagram\n\n![Excavation Grid](data:image/png;base64,iVBORw0KGgoAAAANS...)\n\nFollow the grid system shown above."
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 14: Attribution and Copyright
```json
{
  "attribution": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "attribution",
      "content": "---\n\n*Recording system developed by Archaeological Institute*\n\n*Version 2.1 - January 2025*\n\n*Licensed under CC BY-SA 4.0*"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 15: Emergency Contact Information
```json
{
  "emergency-info": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "emergency-info",
      "content": "## Emergency Contacts\n\n**Site Director:** Dr. Smith - 0400 123 456\n**Safety Officer:** J. Brown - 0400 789 012\n**Emergency Services:** 000\n**Site First Aid:** Station A near main tent"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

### Example 16: Glossary of Terms
```json
{
  "glossary": {
    "component-namespace": "faims-custom",
    "component-name": "RichText",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "name": "glossary",
      "content": "### Terms\n\n**Context:** Single stratigraphic unit\n**Cut:** Negative feature interface\n**Fill:** Material within cut\n**Layer:** Horizontal deposit"
    },
    "validationSchema": [["yup.string"]],
    "initialValue": ""
  }
}
```

## Migration Scenarios {comprehensive}

### Scenario 1: HTML to Markdown Content Migration
**Context**: Legacy HTML content needs conversion to markdown format for RichText fields.

**Challenge**:
- HTML tables are stripped by DOMPurify
- Complex formatting lost in conversion
- External image URLs blocked

**Migration Steps**:
1. Export existing HTML content
2. Convert tables to markdown lists or images
3. Download and convert external images to Base64
4. Simplify complex formatting to basic markdown
5. Test rendering in Designer source mode

**Solution/Workaround**: Pre-process HTML through a converter, manually handle tables as images or lists, embed all images as Base64.

### Scenario 2: Table Content Handling
**Context**: Forms with instructional tables that get stripped at runtime.

**Challenge**:
- Tables created in Designer but removed by sanitizer
- Users lose critical reference information
- No native table support in renderer

**Migration Steps**:
1. Screenshot existing tables
2. Convert to PNG/JPG images (<100KB)
3. Encode images as Base64
4. Embed in markdown as images
5. Add text fallback below image

**Solution/Workaround**: Convert all tables to images with text alternatives, or restructure as nested lists.

### Scenario 3: Performance Migration - Splitting Large RichText
**Context**: Form with 2000+ words in single RichText causing mobile performance issues.

**Challenge**:
- Parse time exceeding 80ms threshold
- Mobile devices experiencing lag
- Content reparsed on every render

**Migration Steps**:
1. Analyze content for logical divisions
2. Split into multiple <100 word fields
3. Use markdown headers for structure
4. Add conditions to show relevant sections
5. Test on lowest-spec target devices

**Solution/Workaround**: Create multiple smaller RichText fields with clear section headers, using conditions for progressive disclosure.

### Scenario 4: External Image Migration
**Context**: Forms referencing external image URLs that are now blocked.

**Challenge**:
- Security policy blocks external URLs
- Images critical for field identification
- No CDN support in Fieldmark

**Migration Steps**:
1. Download all external images
2. Optimize to <100KB each
3. Convert to Base64 encoding
4. Replace URLs with data URIs
5. Update form JSON with embedded images

**Solution/Workaround**: Batch convert images to Base64, embed directly in content field, monitor total payload size.

### Scenario 5: Conditional Content Updates
**Context**: Dynamic help text system using multiple conditional RichText fields.

**Challenge**:
- Frequent visibility toggles cause reparse lag
- Memory accumulation on mobile
- Poor user experience

**Migration Steps**:
1. Consolidate related content into single fields
2. Reduce conditional logic complexity
3. Use static content where possible
4. Implement section-based visibility
5. Limit to essential dynamic content only

**Solution/Workaround**: Minimize conditional fields, prefer static content with comprehensive initial instructions.

## Best Practices {comprehensive}

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

## Field Quirks Index (2025-01-03) {comprehensive}
- Tables stripped despite Designer support
- External images blocked silently
- Content reparsed every render (no memoization)
- No accessibility implementation
- "Error" display for invalid markdown
- Base64 images inline in JSON (increases payload)
- No content size validation
- Blockquotes removed by sanitizer
- Line breaks require double spacing
- No dark mode support

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

## JSON Patterns Cookbook (2025-01-03) {comprehensive}

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

## Quick Diagnosis Tables (2025-01-03) {important}

### Display Issues Diagnosis
| Symptom | Field | Platform | Likely Cause | Quick Fix | Prevention |
|---------|-------|----------|--------------|-----------|------------|
| Shows "Error" | RichText | All | Invalid markdown | Check syntax in console | Validate in Designer |
| No tables | RichText | All | DOMPurify strips | Use lists instead | Avoid HTML tables |
| Missing images | RichText | All | External URLs blocked | Convert to Base64 | Use Designer upload |
| Slow render | RichText | Mobile | Large content (>500 words) | Reduce to <100 words | Split across fields |
| Form lag | RichText | All | Multiple fields (>10) | Limit to 5 fields | Use pagination |
| Memory issues | RichText | Mobile | No cleanup + reparsing | Restart app periodically | Keep content minimal |
| Blockquotes gone | RichText | All | Sanitization removes | Use indentation | Stick to basic markdown |
| Links too small | RichText | Mobile | No touch target control | Minimize links | Use buttons instead |
| No dark mode | RichText | All | Fixed styling | Cannot fix | Plan for light mode |
| Content cut off | RichText | Mobile | Viewport constraints | Shorten content | Test on devices |
| Emoji issues | RichText | Android | Font support varies | Use Unicode symbols | Test cross-platform |
| Code blocks broken | RichText | All | Unclosed backticks | Close all blocks | Check in source mode |
| Lists misaligned | RichText | All | Mixed markdown/HTML | Use pure markdown | Avoid HTML mixing |
| Headers not bold | RichText | All | CSS not loaded | Use ### markdown | Check form styles |
| Line breaks lost | RichText | All | Markdown needs double | Use two spaces + enter | Preview first |

## Field Interaction Matrix (2025-01-03) {important}

### RichText with Other Fields
| Field Combination | Interaction | Pattern |
|------------------|-------------|---------|
| RichText + Conditions | Performance impact | Reparse on toggle |
| RichText + Any field | No data interaction | Display only |
| Multiple RichText | Memory accumulation | Limit count |
| RichText + TemplatedString | Different purposes | Static vs dynamic |

## Migration Warnings Index (2025-01-03) {comprehensive}

### Critical Migration Issues
1. **Tables won't display** - Designer shows but runtime strips
2. **Performance overhead** - Content reparsed on every render
3. **No content caching** - Each update triggers full reparse
4. **External images fail** - Security blocks all external URLs
5. **No accessibility** - Screen readers get plain text only
6. **Base64 size matters** - Increases notebook JSON significantly
7. **Content in notebook** - Not in record data, affects sync size
8. **Blockquotes removed** - DOMPurify strips for security
9. **No undo for edits** - Designer changes immediate

## See Also {comprehensive}

### Other Field Categories
- **[Text Fields](./text-fields-v05.md)**: TemplatedString for dynamic content, TextField for input
- **[Number Fields](./number-fields-v05.md)**: For numeric display formatting
- **[DateTime Fields](./datetime-fields-v05.md)**: For date/time display
- **[Select/Choice Fields](./select-choice-fields-v05.md)**: For choice instructions
- **[Media Fields](./media-fields-v05.md)**: For media capture guidance
- **[Location Fields](./location-fields-v05.md)**: For GPS instructions
- **[Relationship Field](./relationship-field-v05.md)**: For relationship help text

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
---

## Related Documentation
<!-- concat:references -->

### Within Field Categories
- **Previous**: [Numeric Fields](./number-fields-v05.md) | [#number-fields](#number-fields)
- **Next**: [Location Fields](./location-fields-v05.md) | [#location-fields](#location-fields)
- **Similar**: [Text Fields - RichText](./text-fields-v05.md#richtext) | [#text-input-fields](#text-input-fields)

### Cross-Field Patterns
- **Field Selection**: [Display Field Usage](../patterns/field-selection-guide.md#display-fields) | [#field-selection](#field-selection)
- **Instructions**: [Form Help Text](../detail-crossfield-docs/patterns.md#instructions) | [#common-patterns](#common-patterns)
- **Conditional Display**: [Dynamic Content](../detail-crossfield-docs/conditional-logic.md#display-fields) | [#conditional-logic](#conditional-logic)

### Technical References
- **Security**: [HTML Sanitization](../reference-docs/security-considerations-reference.md#display-fields) | [#security-considerations](#security-considerations)
- **Performance**: [Rendering Limits](../reference-docs/performance-thresholds-reference.md#display-fields) | [#performance-thresholds](#performance-thresholds)

<!-- /concat:references -->
<!-- concat:boundary:end section="display-fields" -->
