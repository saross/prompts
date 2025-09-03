# Conditional Logic System - Third Draft Documentation
## Fieldmark/FAIMS3 Notebook Designer Reference

### Document Classification
- **Component Type**: System Behavior
- **Audience Tags**: {designer} {developer} {claude-code}
- **Depth Levels**: {essential} {important} {comprehensive}
- **Version**: 1.0.0
- **Last Technical Verification**: August 2025

---

## 1. Quick Start {essential} {designer}

### What Are Conditions?
Conditions control when fields and sections appear in your notebook, similar to skip patterns in survey tools like Survey Monkey or Qualtrics. They create dynamic forms that adapt based on user input, streamlining data entry especially on mobile devices.

### Basic Example: "Other" Field Pattern
```json
{
  "category": {
    "component-name": "Select",
    "component-parameters": {
      "label": "Category",
      "ElementProps": {
        "options": [
          {"value": "site", "label": "Archaeological Site"},
          {"value": "artifact", "label": "Artifact"},
          {"value": "other", "label": "Other"}
        ]
      }
    }
  },
  "category_other": {
    "component-name": "TextField",
    "component-parameters": {
      "label": "Please specify other",
      "required": true
    },
    "condition": {
      "operator": "equal",
      "field": "category",
      "value": "other"
    }
  }
}
```

### Testing Workflow {essential} {designer}
Conditions must be tested in deployed notebooks (not Designer preview):
1. Open Designer in one browser tab
2. Open deployed notebook in another tab  
3. Make changes in Designer and save
4. Refresh notebook tab (changes apply in seconds)
5. Test conditions with real data entry

**Note**: Designer preview does NOT evaluate conditions. Always test in deployed notebook.

---

## 2. Critical Warnings {essential} {designer} {claude-code}

### ⚠️ Type Matching Required
Number fields require number values in conditions - string numbers will NOT match:
- ✅ **CORRECT**: `{"operator": "equal", "field": "count", "value": 5}`
- ❌ **WRONG**: `{"operator": "equal", "field": "count", "value": "5"}`

This is the #1 source of "why isn't my condition working?" issues.

### ⚠️ Hidden Required Fields Still Validate
Required fields that are hidden by conditions STILL block form submission:
- **Solution 1**: Never hide required fields
- **Solution 2**: Make fields non-required if they can be hidden
- **Solution 3**: Use duplicate fields pattern (one required, one optional)

### ⚠️ No Cross-Form References
Conditions can only reference fields within the same form (viewset):
- Parent forms cannot reference child form fields
- Child forms cannot reference parent form fields
- No mechanism exists for cross-form field access

### ⚠️ BasicAutoIncrementer String Comparison
Auto-incrementers return padded strings ("0001", "0002"), not numbers.
String comparison means "0150" < "0099" is TRUE (alphabetical order).
- **Solution**: Design compound HRIDs that sort properly regardless

### ⚠️ No Field ID Migration
When field IDs change, conditions referencing them fail silently:
- No error messages
- Condition returns false
- Manual update required

---

## 3. How Conditions Work {important} {developer}

### Condition Lifecycle
1. **Compilation**: Conditions compiled to JavaScript functions on form load
2. **Caching**: Stored as `conditionFn` property on fields/sections
3. **Evaluation**: Only when "controller fields" change
4. **Application**: Hide/show fields before render (no flicker)

### Controller Fields
Any field referenced in a condition automatically becomes a "controller field":
- Detection is automatic - no configuration needed
- Only changes to controller fields trigger re-evaluation
- Optimizes performance by avoiding unnecessary checks

### Values Object
All fields are initialized in the values object on form load:
- Fields start with their `initialValue` (or `""` if not specified)
- Fields are never removed from values, only updated
- Hidden field values persist and remain accessible

---

## 4. Configuration and JSON Structure {important} {claude-code}

### Basic Condition Structure
```json
{
  "field-name": {
    "component-name": "TextField",
    "component-parameters": {...},
    "condition": {
      "operator": "equal",
      "field": "trigger-field",
      "value": "expected-value"
    }
  }
}
```

### Section-Level Conditions
Entire sections can be conditional. When hidden:
- Section removed from navigation breadcrumb
- Progress indicators update (e.g., "2/2" becomes "2/3" when section appears)
- No placeholder or gap in navigation

```json
{
  "OptionalSection": {
    "label": "Additional Details",
    "fields": ["field1", "field2", "field3"],
    "condition": {
      "operator": "equal",
      "field": "collect-details",
      "value": "yes"
    }
  }
}
```

### Property Names
- **Modern**: `condition` (recommended)
- **Legacy**: `is_logic` (deprecated but supported)

---

## 5. Operators Reference {important} {claude-code}

### Comparison Operators

| Operator | Description | Type Handling | Example Value |
|----------|-------------|---------------|---------------|
| `equal` | Exact match | Strict (===) | `"yes"`, `5`, `true` |
| `not-equal` | Not equal | Strict (!==) | `"no"`, `10`, `false` |
| `greater` | Greater than | Coercion | `10` |
| `greater-equal` | Greater or equal | Coercion | `0` |
| `less` | Less than | Coercion | `100` |
| `less-equal` | Less or equal | Coercion | `999` |
| `regex` | Pattern match | String | `"\\d+"`, `"^[A-Z]"` |

### Array Operators
For fields returning arrays (multi-select, checkboxes):

| Operator | Description | Example Value |
|----------|-------------|---------------|
| `contains` | Array includes value | `"option1"` |
| `does-not-contain` | Array excludes value | `"option2"` |
| `contains-one-of` | Has at least one | `["A", "B", "C"]` |
| `does-not-contain-any-of` | Has none of these | `["X", "Y"]` |
| `contains-all-of` | Has all values | `["A", "B"]` |
| `does-not-contain-all-of` | Missing at least one | `["A", "B", "C"]` |
| `contains-regex` | Any element matches | `"test.*"` |
| `does-not-contain-regex` | No element matches | `"^temp"` |

### Logical Operators

| Operator | Description | Short-Circuit | Performance Tip |
|----------|-------------|---------------|-----------------|
| `and` | All conditions true | Yes (first false) | Put likely-false first |
| `or` | Any condition true | Yes (first true) | Put likely-true first |

---

## 6. Complex Logic Patterns {important} {claude-code}

### AND Logic Example
Show field only if multiple conditions are met:
```json
{
  "condition": {
    "operator": "and",
    "conditions": [
      {"operator": "equal", "field": "sample-collected", "value": "yes"},
      {"operator": "greater", "field": "sample-count", "value": 0}
    ]
  }
}
```

### OR Logic Example
Show field if any condition is met:
```json
{
  "condition": {
    "operator": "or",
    "conditions": [
      {"operator": "equal", "field": "contact-method", "value": "email"},
      {"operator": "equal", "field": "contact-method", "value": "online"}
    ]
  }
}
```

### Nested Complex Logic
Combine AND and OR for sophisticated patterns:
```json
{
  "condition": {
    "operator": "or",
    "conditions": [
      {
        "operator": "and",
        "conditions": [
          {"operator": "equal", "field": "survey-type", "value": "detailed"},
          {"operator": "greater", "field": "team-size", "value": 2}
        ]
      },
      {"operator": "equal", "field": "override-details", "value": true}
    ]
  }
}
```
This reads as: `(survey-type='detailed' AND team-size>2) OR override-details=true`

---

## 7. Field Type Interactions {important} {developer}

### Standard Field Types

| Field Type | Value Type | Condition Value | Notes |
|------------|------------|-----------------|-------|
| TextField | string | `"text"` | Exact string match |
| NumberField | number | `42` | Use numbers, not strings |
| NumberInput | number | `3.14` | Decimal support |
| Checkbox | boolean | `true` or `false` | Not "true" string |
| RadioGroup | string | `"option1"` | Returns value, not label |
| Select (single) | string | `"selected"` | Returns value property |
| Select (multiple) | array | Use array operators | Empty = `[]` |
| DatePicker | string | `"2024-01-01"` | ISO format, string comparison works |
| DateTimeField | string | `"2024-01-01T10:30"` | Local time, no timezone |
| BasicAutoIncrementer | string | `"0001"` | Padded string, alphabetical sort |

### Complex Fields - Cannot Use Directly
These fields return complex objects that cannot be used in conditions:

| Field Type | Returns | Workaround |
|------------|---------|------------|
| TakePhoto | Blob array | Use TemplatedStringField pattern |
| TakePoint | GeoJSON object | Extract to hidden field |
| MapFormField | GeoJSON object | Manual indicator field |
| RelationshipField | Relationship objects | Hidden status field |
| AnnotationAttachment | Attachment array | Manual checkbox |

---

## 8. Complex Field Workarounds {important} {designer} {claude-code}

### The Hidden Template Pattern
For complex fields that can't be used directly in conditions, create a hidden TemplatedStringField that automatically tracks their status:

```json
{
  "site-photos": {
    "component-name": "TakePhoto",
    "component-parameters": {
      "label": "Site Photographs"
    }
  },
  "_has_photos": {
    "component-name": "TemplatedStringField",
    "component-parameters": {
      "template": "{{#site-photos}}yes{{/site-photos}}{{^site-photos}}no{{/site-photos}}",
      "hidden": true
    }
  },
  "photo-description": {
    "component-name": "MultilineTextField",
    "component-parameters": {
      "label": "Describe the photographs",
      "helperText": "Include details about what each photo shows",
      "required": true
    },
    "condition": {
      "operator": "equal",
      "field": "_has_photos",
      "value": "yes"
    }
  }
}
```

### Pattern Conventions
- **Naming**: Prefix with underscore (`_has_photos`, `_has_location`)
- **Values**: Use simple `yes/no` or `true/false`
- **Visibility**: Always set `hidden: true`
- **Updates**: Automatic when source field changes

### Common Templates

```javascript
// Boolean existence check (most common for conditions)
"{{#fieldname}}yes{{/fieldname}}{{^fieldname}}no{{/fieldname}}"

// Alternative boolean format
"{{#fieldname}}true{{/fieldname}}{{^fieldname}}false{{/fieldname}}"

// Default value pattern
"{{fieldname}}{{^fieldname}}none{{/fieldname}}"
```

### Mustache Template Limitations for Conditions
- Cannot access array `.length` property
- Limited nested property access
- Cannot perform calculations
- Boolean existence checks most reliable

**Note**: For complete Mustache template capabilities including string concatenation, date formatting, and advanced patterns, see the TemplatedStringField documentation. This section focuses only on patterns useful for conditional logic.

---

## 9. Value Handling and Type Coercion {comprehensive} {developer}

### Field State Scenarios

| Scenario | In values? | equal to `null` | equal to `""` | not-equal to `""` |
|----------|------------|-----------------|---------------|-------------------|
| Never touched | Yes (initialized) | false | true (usually) | false |
| User typed then cleared | Yes | false | true | false |
| Has null value | Yes | true | false | true |
| Has empty string | Yes | false | true | false |
| Field doesn't exist in form | No | false | false | true |

### Type Coercion Rules
- **equal/not-equal**: Strict comparison (`===`, `!==`)
  - `"5"` will NOT equal `5`
  - `true` will NOT equal `"true"`
- **Comparison operators**: JavaScript coercion applies
  - `"20" > 10` returns `true` (string coerced to number)
  - `"10" < 5` returns `false`

### Hidden Field Value Behavior
- Values persist when hidden
- Included in form submission
- Can be referenced by other conditions
- Validation still enforced (including required)

---

## 10. Performance Optimization {important} {developer}

### Performance Boundaries

| Complexity | Safe Limit | Notes |
|------------|------------|-------|
| Simple conditions (equal) | 100-200 per form | Minimal impact |
| Complex nested conditions | 20-30 per form | Noticeable at higher counts |
| Controller fields | ~50 | Each triggers re-evaluation |
| Nesting depth | ~10 levels | Tested to 20+ but degrades |
| AND/OR array size | 10-20 conditions | Similar to nesting |

### Optimization Strategies

#### 1. Condition Ordering (50-90% improvement)
Leverage short-circuiting by ordering conditions strategically:

```json
// OPTIMIZED - Likely true first in OR
{
  "operator": "or",
  "conditions": [
    {"operator": "equal", "field": "common-field", "value": true},
    {"operator": "regex", "field": "description", "value": "complex.*pattern"}
  ]
}

// OPTIMIZED - Likely false first in AND
{
  "operator": "and",
  "conditions": [
    {"operator": "equal", "field": "rare-condition", "value": true},
    {"operator": "greater", "field": "count", "value": 100}
  ]
}
```

#### 2. Minimize Controller Fields
Each controller field triggers re-evaluation. Group related conditions under single triggers where possible.

#### 3. Avoid Regex When Possible
Regex operations are more expensive than simple comparisons.

### Warning Signs of Performance Issues
- Lag when typing in controller fields
- Delayed field show/hide animations
- Form freezing during navigation
- Browser "script running slowly" warnings

---

## 11. Common Patterns {important} {designer}

### Pattern: Other → Specify
```json
{
  "category": {
    "component-name": "RadioGroup",
    "component-parameters": {
      "label": "Site Type",
      "options": [
        {"value": "historic", "label": "Historic"},
        {"value": "prehistoric", "label": "Prehistoric"},
        {"value": "other", "label": "Other"}
      ]
    }
  },
  "category_other_specify": {
    "component-name": "TextField",
    "component-parameters": {
      "label": "Please specify other site type",
      "required": true,
      "helperText": "Provide a brief description"
    },
    "condition": {
      "operator": "equal",
      "field": "category",
      "value": "other"
    }
  }
}
```

### Pattern: Progressive Disclosure
```json
{
  "basic_survey": {
    "component-name": "RadioGroup",
    "component-parameters": {
      "label": "Conduct detailed survey?",
      "options": [
        {"value": "yes", "label": "Yes - Full Survey"},
        {"value": "no", "label": "No - Basic Only"}
      ]
    }
  },
  "DetailedSection": {
    "label": "Detailed Survey Information",
    "condition": {
      "operator": "equal",
      "field": "basic_survey",
      "value": "yes"
    },
    "fields": [
      "measurement-method",
      "measurement-precision",
      "environmental-conditions",
      "team-members"
    ]
  }
}
```

### Pattern: Conditional Required Fields (Workaround)
Since conditional validation isn't supported, use duplicate fields:
```json
{
  "contact_method": {
    "component-name": "RadioGroup",
    "component-parameters": {
      "label": "Preferred Contact Method",
      "options": [
        {"value": "email", "label": "Email"},
        {"value": "phone", "label": "Phone"},
        {"value": "none", "label": "No Contact"}
      ]
    }
  },
  "email_optional": {
    "component-name": "TextField",
    "component-parameters": {
      "label": "Email Address",
      "type": "email",
      "required": false
    },
    "condition": {
      "operator": "not-equal",
      "field": "contact_method",
      "value": "email"
    }
  },
  "email_required": {
    "component-name": "TextField",
    "component-parameters": {
      "label": "Email Address",
      "type": "email",
      "required": true,
      "helperText": "Required for email contact"
    },
    "condition": {
      "operator": "equal",
      "field": "contact_method",
      "value": "email"
    }
  }
}
```

### Pattern: Manual vs Automated Indicators

#### Use Manual Indicators When:
- Human confirmation required
- Audit trail needed
- Complex judgment involved
- No technical derivation possible

#### Use Automated Templates When:
- Value computable from other fields
- Consistency crucial
- Reducing cognitive load
- System tracking fields

---

## 12. Troubleshooting Guide {important} {designer}

### Debugging Checklist
When a condition isn't working, check in order:

1. **Type Mismatch** (Most Common)
   - Number field with string value?
   - Boolean field with string "true"?
   - Check exact types in browser console

2. **Field ID Spelling**
   - Exact match required
   - Case-sensitive
   - No typos in field reference

3. **Deployment Status**
   - Conditions don't work in Designer preview
   - Must test in deployed notebook
   - Changes require save and refresh

4. **Field Initialization**
   - Check if field exists in values object
   - May need initialValue set
   - Hidden fields still need initialization

5. **Operator Choice**
   - Using `equal` when you need `contains`?
   - Array field needs array operators
   - Regex format correct?

### Debug Techniques

#### Enable Debug Logging
```javascript
// In browser console
localStorage.setItem('debug', 'faims:*');
// Refresh page to see detailed logs
```

#### Monitor Condition Performance
```javascript
// Add to console before testing
const originalFn = window.compileExpression;
window.compileExpression = function(expr) {
  console.time('condition-compile');
  const result = originalFn(expr);
  console.timeEnd('condition-compile');
  return result;
}
```

#### Inspect Values Object
```javascript
// In browser console while form is open
console.log(window.Formik.values);
// Or for specific field
console.log(window.Formik.values['field-name']);
```

### Common Issues and Solutions

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| Field never appears | Type mismatch in condition | Verify number vs string types |
| Field always visible | Condition syntax error | Check operator spelling |
| Required hidden field blocks save | Validation on hidden fields | Make non-required or keep visible |
| Condition works intermittently | Race condition or missing field | Ensure field initialized first |
| Performance degradation | Too many complex conditions | Simplify logic or reduce count |
| Changes don't take effect | Not refreshing deployed notebook | Save in Designer, refresh notebook |

### Error Messages

| Error | Meaning | Fix |
|-------|---------|-----|
| "Unknown operator X" | Invalid operator name | Check spelling (e.g., `equal` not `equals`) |
| Form won't load | Malformed condition JSON | Validate JSON syntax |
| Silent failure | Field reference doesn't exist | Verify field ID exists in form |

---

## 13. Validation Rules and Display Behavior {comprehensive} {developer}

### Validation Interaction with Conditions

| Validation Rule | When Hidden | When Visible | Notes |
|-----------------|-------------|--------------|-------|
| required: true | Still enforced | Enforced | Hidden required fields block submission |
| min/max | Still enforced | Enforced | Numeric bounds always checked |
| pattern | Still enforced | Enforced | Regex patterns always validated |
| Custom validation | Still runs | Runs | All validation runs regardless |

### Display Behavior

| Aspect | Behavior | Notes |
|--------|----------|-------|
| Initial render | Hidden if condition false | No flicker - evaluated before display |
| Show animation | Immediate | No transition effects |
| Hide animation | Immediate | Values preserved |
| Layout shift | Minimal | Space collapses when hidden |
| Tab order | Skips hidden fields | Keyboard navigation adjusts |
| Section navigation | Hidden sections removed | Progress indicators update dynamically |
| Breadcrumbs | Hidden sections omitted | Navigation updates in real-time |

### Error Message Display
- Hidden fields with validation errors don't show messages
- Errors appear when field becomes visible
- Form submission shows all errors (including hidden)

---

## 14. Migration and Compatibility {comprehensive} {developer}

### Field ID Changes
**Warning**: No automatic migration for renamed fields
- Conditions fail silently (return false)
- No error messages or warnings
- Manual update required in all conditions
- Search and replace recommended

### Legacy Format Support

#### Old is_logic Format
Still supported but deprecated:
```json
{
  "field-name": {
    "is_logic": {
      "trigger-field": ["value1", "value2"]
    }
  }
}
```

#### Modern Equivalent
```json
{
  "field-name": {
    "condition": {
      "operator": "or",
      "conditions": [
        {"operator": "equal", "field": "trigger-field", "value": "value1"},
        {"operator": "equal", "field": "trigger-field", "value": "value2"}
      ]
    }
  }
}
```

### Version Compatibility
- Conditions work identically across platforms
- No mobile-specific behavior
- Offline mode fully supported
- All browsers supporting ES6

---

## 15. Known Limitations and Roadmap {important} {designer} {developer}

### Current Limitations

#### Cannot Do (Technical Limitations)
- **Cross-form references** - No access to parent/child form fields
- **Array length checks** - Cannot count items in arrays
- **Nested property access** - Limited support for object.property
- **Conditional validation** - Cannot make fields required only when visible
- **Complex calculations** - No sum, average, or arithmetic operations
- **Complex field conditions** - TakePhoto, TakePoint, RelationshipField need workarounds

#### Cannot Do (Implementation Gaps)
- **Designer preview evaluation** - Must deploy to test conditions
- **Field ID migration** - Renamed fields break conditions silently
- **Debug visibility** - No visual indicators of condition evaluation
- **Circular dependency detection** - System allows but doesn't warn

### Roadmap Features (Planned Improvements)

#### High Priority
- **Designer preview with conditions** - Test without deployment
- **Conditional validation** - Required only when visible
- **Additional operators** (User requested):
  - `between` - Range checks (e.g., `5 < x < 10`)
  - `count` - Array length (e.g., number of photos)
  - `sum` - Total of numeric fields
  - `average` - Mean of numeric fields
  - `product` - Multiplication of field values
  - Basic arithmetic (`+`, `-`, `*`, `/`)

#### Future Considerations
- **Calculated fields** - Auto-compute values from other fields
- **Cross-form references** - Access parent/child form fields
- **Migration tools** - Update conditions when field IDs change
- **Visual debugging** - Show condition evaluation in Designer
- **Performance monitoring** - Built-in condition profiling
- **Dependency visualization** - Graph of field relationships

### Workarounds for Current Limitations

| Limitation | Current Workaround |
|------------|-------------------|
| No Designer preview | Two-tab testing workflow |
| No conditional validation | Duplicate fields (required/optional) |
| No array counts | Manual indicator fields |
| Complex field conditions | TemplatedStringField pattern |
| No calculations | Server-side processing or manual entry |

---

## 16. Design Patterns and Best Practices {important} {designer}

### Effective Condition Design

#### 1. Use Required Fields as Triggers
Required fields guarantee user interaction, making them ideal condition controllers:
```json
{
  "survey-type": {
    "component-name": "RadioGroup",
    "component-parameters": {
      "required": true,
      "label": "Survey Type"
    }
  },
  "grid-details": {
    "condition": {
      "operator": "equal",
      "field": "survey-type",
      "value": "grid"
    }
  }
}
```

#### 2. Group Related Conditions
Minimize cognitive load by grouping related conditional fields:
```json
{
  "PhotoSection": {
    "label": "Photographic Documentation",
    "condition": {
      "operator": "equal",
      "field": "include-photos",
      "value": "yes"
    },
    "fields": [
      "photo-capture",
      "photo-description",
      "photographer-name",
      "photo-conditions"
    ]
  }
}
```

#### 3. Clear Visual Hierarchy
Use section headers or display fields to explain conditional content:
```json
{
  "detailed-header": {
    "component-name": "RichText",
    "component-parameters": {
      "content": "<h3>Additional Details Required</h3><p>Please complete all fields below</p>"
    },
    "condition": {
      "operator": "equal",
      "field": "needs-details",
      "value": true
    }
  }
}
```

### When to Use Conditions

**Good Use Cases:**
- Skip patterns for irrelevant fields
- Progressive disclosure of complexity
- Role-based field visibility
- Dynamic form adaptation
- Mobile screen optimization

**Avoid Conditions When:**
- All users need the field
- Complexity exceeds benefit
- Cross-form logic required
- Performance is critical

---

## 16. Platform Behavior Matrix {comprehensive} {developer}

### Platform Comparison

| Feature | Web | iOS | Android | Notes |
|---------|-----|-----|---------|-------|
| Condition evaluation | ✅ Identical | ✅ Identical | ✅ Identical | Client-side JavaScript |
| Performance | Fastest | Good | Good | Desktop typically faster |
| Offline support | ✅ Full | ✅ Full | ✅ Full | No server dependency |
| Debug tools | Best | Limited | Limited | Browser DevTools advantage |
| Touch events | Mouse | Native | Native | No impact on conditions |

### Browser Compatibility

| Browser | Support | Notes |
|---------|---------|-------|
| Chrome 90+ | ✅ Full | Recommended for Designer |
| Firefox 88+ | ✅ Full | Full support |
| Safari 14+ | ✅ Full | macOS and iOS |
| Edge 90+ | ✅ Full | Chromium-based |

---

## 17. Implementation Notes {comprehensive} {developer}

### Technical Architecture

#### Compilation Process
```javascript
// Simplified compilation flow
compileUiSpecConditionals(spec) {
  for (field in spec.fields) {
    if (field.condition) {
      field.conditionFn = compileExpression(field.condition);
      addToControllerFields(extractFieldRefs(field.condition));
    }
  }
}
```

#### Evaluation Cycle
1. Controller field changes
2. Formik triggers update
3. branchingLogic.tsx checks conditions
4. getFieldsMatchingCondition filters fields
5. React re-renders with filtered fields

#### Memory Model
- All conditions compiled once on load
- Functions cached in memory
- Values object holds all field states
- Hidden values persist in Formik state

### File Locations (Internal Reference)
- Core logic: `/app/src/conditionals.ts`
- Compilation: `/app/src/uiSpecification.ts`
- Runtime evaluation: `/app/src/gui/components/record/branchingLogic.tsx`
- Legacy support: `/app/src/uiSpecification.ts:compileIsLogic()`

---

## 18. Decision Trees {claude-code}

### Condition Necessity Decision
```
Is this field always needed?
├─ Yes → No condition required
└─ No → Does visibility depend on user input?
    ├─ No → Consider permission/role system
    └─ Yes → Implement condition
        ├─ Single trigger → Simple condition
        ├─ Multiple triggers → OR logic
        └─ Multiple requirements → AND logic
```

### Operator Selection Guide
```
What comparison do you need?
├─ Exact match → equal / not-equal
├─ Numeric comparison → greater / less operators
├─ Text pattern → regex
├─ Multiple options → contains operators
├─ Complex logic → Nested AND/OR
└─ Field existence → Check against null/empty
```

### Complex Field Handling
```
Is the field type complex (Photo/Location/Relationship)?
├─ No → Use direct condition
└─ Yes → Can the state be derived?
    ├─ No → Use manual indicator field
    └─ Yes → Use TemplatedStringField pattern
        ├─ Boolean check → {{#field}}yes{{/field}}
        └─ Value extraction → Limited support
```

---

## 19. Anti-Patterns to Avoid {important} {designer}

### ❌ Hidden Required Fields
```json
// AVOID - Blocks form submission when hidden
{
  "critical-field": {
    "component-parameters": {"required": true},
    "condition": {"operator": "equal", "field": "optional", "value": "yes"}
  }
}
```

### ❌ Cross-Form Dependencies
```json
// WON'T WORK - Cannot reference parent form
{
  "child-field": {
    "condition": {"operator": "equal", "field": "parent.field", "value": "yes"}
  }
}
```

### ❌ Type Mismatches
```json
// BROKEN - Number field won't match string
{
  "condition": {
    "operator": "equal",
    "field": "number-field",
    "value": "5"  // Should be 5 (number)
  }
}
```

### ❌ Over-Complex Nesting
Avoid deeply nested conditions that are hard to debug and maintain.

---

## 20. Relationship to Other Systems {important} {designer}

### Related Field Types

#### TemplatedStringField
Essential for condition workarounds with complex fields:
- Creates derived values for conditions
- Enables boolean checks on arrays
- Provides computed fields

#### BasicAutoIncrementer
Special consideration needed:
- Returns padded strings
- Alphabetical sorting issues
- Best used in compound IDs

#### Select vs MultiSelect
Different operators required:
- Select: Use standard operators
- MultiSelect: Use array operators

### Integration with Other Features

| Feature | Interaction with Conditions |
|---------|----------------------------|
| Validation | Runs regardless of visibility |
| Draft Saving | Hidden values preserved |
| Export | All values included |
| Relationships | Cannot be used in conditions |
| Annotations | Cannot be used in conditions |

---

## Appendix A: Complete JSON Examples {comprehensive} {claude-code}

### Example 1: Heritage Site Survey with Progressive Disclosure
```json
{
  "fields": {
    "site-type": {
      "component-name": "RadioGroup",
      "component-parameters": {
        "label": "Heritage Site Type",
        "required": true,
        "options": [
          {"value": "aboriginal", "label": "Aboriginal Site"},
          {"value": "historical", "label": "Historical Site"},
          {"value": "maritime", "label": "Maritime Heritage"},
          {"value": "other", "label": "Other"}
        ]
      }
    },
    "site-type-other": {
      "component-name": "TextField",
      "component-parameters": {
        "label": "Specify Other Site Type",
        "required": true
      },
      "condition": {
        "operator": "equal",
        "field": "site-type",
        "value": "other"
      }
    },
    "aboriginal-details": {
      "component-name": "Select",
      "component-parameters": {
        "label": "Aboriginal Site Category",
        "ElementProps": {
          "options": [
            {"value": "midden", "label": "Shell Midden"},
            {"value": "art", "label": "Rock Art"},
            {"value": "tool", "label": "Tool Making Site"},
            {"value": "ceremonial", "label": "Ceremonial Site"}
          ]
        }
      },
      "condition": {
        "operator": "equal",
        "field": "site-type",
        "value": "aboriginal"
      }
    },
    "requires-protection": {
      "component-name": "Checkbox",
      "component-parameters": {
        "label": "Site requires immediate protection"
      }
    },
    "protection-details": {
      "component-name": "MultilineTextField",
      "component-parameters": {
        "label": "Protection Measures Required",
        "required": true,
        "rows": 4
      },
      "condition": {
        "operator": "equal",
        "field": "requires-protection",
        "value": true
      }
    }
  }
}
```

### Example 2: Complex Multi-Condition Form
```json
{
  "fields": {
    "survey-method": {
      "component-name": "Select",
      "component-parameters": {
        "label": "Survey Method",
        "ElementProps": {
          "options": [
            {"value": "pedestrian", "label": "Pedestrian Survey"},
            {"value": "vehicular", "label": "Vehicular Survey"},
            {"value": "aerial", "label": "Aerial Survey"},
            {"value": "marine", "label": "Marine Survey"}
          ]
        }
      }
    },
    "team-size": {
      "component-name": "NumberInput",
      "component-parameters": {
        "label": "Team Size"
      }
    },
    "detailed-recording": {
      "component-name": "RadioGroup",
      "component-parameters": {
        "label": "Detailed Recording Required?",
        "options": [
          {"value": "yes", "label": "Yes"},
          {"value": "no", "label": "No"}
        ]
      },
      "condition": {
        "operator": "or",
        "conditions": [
          {
            "operator": "and",
            "conditions": [
              {"operator": "equal", "field": "survey-method", "value": "pedestrian"},
              {"operator": "greater", "field": "team-size", "value": 2}
            ]
          },
          {"operator": "equal", "field": "survey-method", "value": "aerial"}
        ]
      }
    }
  }
}
```

### Example 3: Photo Documentation with Automated Detection
```json
{
  "fields": {
    "site-photos": {
      "component-name": "TakePhoto",
      "component-parameters": {
        "label": "Site Photographs",
        "helperText": "Capture overall site images"
      }
    },
    "_has_photos": {
      "component-name": "TemplatedStringField",
      "component-parameters": {
        "template": "{{#site-photos}}yes{{/site-photos}}{{^site-photos}}no{{/site-photos}}",
        "hidden": true
      }
    },
    "photo-metadata": {
      "component-name": "Select",
      "component-parameters": {
        "label": "Photography Conditions",
        "ElementProps": {
          "options": [
            {"value": "sunny", "label": "Sunny"},
            {"value": "overcast", "label": "Overcast"},
            {"value": "rain", "label": "Rain"},
            {"value": "artificial", "label": "Artificial Light"}
          ]
        }
      },
      "condition": {
        "operator": "equal",
        "field": "_has_photos",
        "value": "yes"
      }
    },
    "photo-description": {
      "component-name": "MultilineTextField",
      "component-parameters": {
        "label": "Describe Photographs",
        "required": true,
        "rows": 3
      },
      "condition": {
        "operator": "equal",
        "field": "_has_photos",
        "value": "yes"
      }
    }
  }
}
```

### Example 4: Dynamic Section Navigation
This example shows how conditional sections affect navigation and progress indicators:
```json
{
  "sections": {
    "Main": {
      "label": "Main",
      "fields": ["artifact-length", "artifact-width", "artifact-height", "add-additional"]
    },
    "ArtefactMeasurements": {
      "label": "Artefact Measurements",
      "fields": ["weight", "material", "condition"]
    },
    "ExtraArtefactMeasurements": {
      "label": "Extra Artefact Measurements",
      "fields": ["volume", "density", "magnetic-susceptibility"],
      "condition": {
        "operator": "equal",
        "field": "add-additional",
        "value": true
      }
    }
  },
  "fields": {
    "artifact-length": {
      "component-name": "NumberInput",
      "component-parameters": {
        "label": "Artefact Length (mm)",
        "helperText": "Length of the artefact in mm"
      }
    },
    "add-additional": {
      "component-name": "Checkbox",
      "component-parameters": {
        "label": "Add Additional Artefact Measurements?",
        "helperText": "Check to add additional dimensions"
      }
    }
  }
}
```
**Navigation behavior:**
- When unchecked: Progress shows "2/2", two sections visible
- When checked: Progress shows "2/3", "Extra Artefact Measurements" appears
- Navigation breadcrumbs update dynamically
- No page reload required

---

## Appendix B: Quick Reference Card {essential} {designer}

### Most Common Patterns
```json
// Show if equals
{"operator": "equal", "field": "trigger", "value": "yes"}

// Show if NOT equals
{"operator": "not-equal", "field": "trigger", "value": "no"}

// Show if greater than
{"operator": "greater", "field": "count", "value": 10}

// Show if any of multiple values (OR)
{
  "operator": "or",
  "conditions": [
    {"operator": "equal", "field": "type", "value": "A"},
    {"operator": "equal", "field": "type", "value": "B"}
  ]
}

// Show if multiple conditions met (AND)
{
  "operator": "and",
  "conditions": [
    {"operator": "equal", "field": "required", "value": true},
    {"operator": "greater", "field": "count", "value": 0}
  ]
}

// Check if multi-select contains value
{"operator": "contains", "field": "multi-select", "value": "option1"}

// Pattern match with regex
{"operator": "regex", "field": "code", "value": "^[A-Z]{3}\\d{3}$"}
```

### Testing Checklist
- [ ] Open notebook in separate tab (not Designer preview)
- [ ] Check field types match condition values
- [ ] Verify field IDs spelled correctly
- [ ] Test all condition paths
- [ ] Check required field behavior

---

**Document Status**: Complete Third Draft - Production Ready  
**Technical Verification**: Full code analysis completed  
**Production Testing**: Patterns verified in deployed notebooks  
**Cross-References**: Field type documentation, TemplatedStringField, BasicAutoIncrementer  
**Known Issues**: Designer preview, conditional validation, cross-form references  
**Roadmap Items**: Preview conditions, calculated fields, additional operators  
**Next Review**: After Designer preview conditions implemented

---

*End of Conditional Logic System Documentation - Ready for Project Knowledge*