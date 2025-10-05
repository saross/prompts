<!-- concat:boundary:start section="form-structure-guide" -->
<!-- concat:metadata
document_id: form-structure-guide
category: patterns
version: 1.0
last_updated: 2025-01-06
purpose: Comprehensive guide to form architecture, sections, and navigation patterns
source_documents:
  - notebook-structure.md (34KB)
  - navigation.md (19KB)
  - quick-start.md (12KB) - structure examples only
-->

<!-- discovery:metadata
provides: [viewsets, fviews, multi-section-forms, navigation-patterns]
see-also: [notebook-format-guide, relationship-field-v05]
-->


# Form Structure Guide


<!-- structured:metadata
meta:purpose: implementation-patterns
meta:summary: Three-tier architecture (fields→fviews→viewsets) requirements and structural patterns.
meta:generates: notebook-structures
meta:requires: [field-definitions, form-hierarchy]
meta:version: 3.0.0
meta:document: form_structure_guide
meta:depth-tags: [essential, important]
-->

## Overview {essential}

This guide consolidates all knowledge about Fieldmark's hierarchical form architecture, navigation patterns, and structural best practices. It covers the three-tier system of Forms (viewsets), Sections (views), and Fields, along with navigation strategies for different use cases and platforms.

## Core Architecture Principles {essential}

### Three-Tier Hierarchical System {essential}

Fieldmark notebooks organize data collection through three levels:

1. **Forms (Viewsets)**: Top-level record types (e.g., Site, Context, Find)
2. **Sections (Views)**: Logical groupings within forms (e.g., Basic Info, Measurements, Photos)
3. **Fields**: Individual data entry components

This architecture scales from simple single-form checklists to sophisticated multi-entity recording systems with dozens of interconnected forms supporting complex parent-child relationships.

### Critical Architecture Decisions

- **No virtualization**: All fields render simultaneously without windowing
- **Performance considerations**: Estimated ~50-100 fields per section may cause degradation (approximate guideline)
- **Global namespace**: Field IDs must be globally unique across entire notebook
- **No navigation blocking**: Users can navigate freely regardless of validation errors
- **Automatic persistence**: Draft saves every 10 seconds
- **Decoupled sync**: Background synchronization never blocks navigation

## Navigation Strategies {important}

### Navigation Mode Selection {#navigation-modes}

#### Vertical Organisation (Inline Mode)
Best for linear data collection workflows with <5 sections:

```json
{
  "viewsets": {
    "survey-form": {
      "label": "Survey Record",
      "layout": "inline",  // All sections visible on single page
      "views": ["basic", "observations", "notes"]
    }
  }
}
```

**Advantages**:
- All sections immediately visible
- Natural scrolling between sections
- No clicking required for navigation
- Best for forms with <50 total fields

**Limitations**:
- Performance degrades with many fields
- No lazy loading - entire form in DOM
- Section headers NOT sticky

#### Horizontal Organisation (Tabs Mode)
Best for complex multi-step workflows or forms with many sections:

```json
{
  "viewsets": {
    "excavation-form": {
      "label": "Excavation Record",
      "layout": "tabs",  // One section visible at a time
      "views": ["context", "matrix", "finds", "samples", "photos", "interpretation"]
    }
  }
}
```

**Advantages**:
- Better performance with many sections
- Clear progress indication
- Reduced cognitive load
- Visited sections tracked

**Limitations**:
- Requires clicking to navigate
- Still renders all sections (no lazy loading)
- More complex navigation on mobile

### Platform-Specific Navigation {#platform-navigation}

#### Desktop Behaviour
- **Inline mode**: Smooth scroll anchors to section starts
- **Tabs mode**: Horizontal stepper with full section names
  - Previous/Next buttons flank stepper
  - Current section scales 1.2x for emphasis
  - Keyboard: Tab/Shift-Tab navigates sections
  - Visited sections show checkmark indicator
  - Error sections show red badge with count

#### Mobile Behaviour
- **iOS**: 
  - Tabs compact to numbered stepper (1/5 format)
  - Swipe gestures may conflict with system gestures
  - Momentum scrolling in inline mode
- **Android**:
  - Material Design stepper in tabs mode
  - Hardware back button behaviour inconsistent
  - FAB for save action (when implemented)

### Responsive Breakpoints
```javascript
xs: < 576px     // Phone portrait
sm: 576-768px   // Phone landscape/small tablet
md: 768-992px   // Tablet
lg: 992-1200px  // Desktop
xl: > 1200px    // Large desktop
```

## Form Configuration {important}

### Required Root Properties {#form-configuration}

```json
{
  "ui-specification": {
    "visible_types": ["form-1", "form-2"],  // REQUIRED: Controls navigation menu
    "viewsets": {                           // REQUIRED: Form definitions
      "form-1": { /* config */ }
    },
    "fviews": {                             // REQUIRED: Section definitions  
      "section-1": { /* config */ }
    },
    "fields": {                             // REQUIRED: Field specifications
      "field-1": { /* config */ }
    }
  }
}
```

**Critical**: Forms omitted from `visible_types` remain accessible via relationships but hidden from navigation menu.

### Form (Viewset) Properties

#### Required Properties
| Property | Type | Description | Default if Missing |
|----------|------|-------------|-------------------|
| `label` | string | Display name in navigation | Form ID used |
| `views` | array | Section IDs in display order | Empty array (blank form) |
| `publishButtonBehaviour` | string | Save button logic | `"always"` |

#### Optional Properties
| Property | Type | Default | Description | Constraints |
|----------|------|---------|-------------|-------------|
| `hridField` | string | Falls back to "hrid" prefix | Field providing human-readable ID | Must reference existing field |
| `layout` | string | `"inline"` | Section presentation mode | `"inline"` or `"tabs"` only |
| `summary_fields` | array | `[]` | Fields shown in record lists | Gracefully handles missing fields |

### Section (View) Configuration

#### Required Properties
| Property | Type | Description | Constraints |
|----------|------|-------------|-------------|
| `label` | string | Section heading displayed | Any string |
| `fields` | array | Field IDs in display order | Must reference existing fields; IDs globally unique |

**Critical**: Section IDs must be globally unique across ALL forms, not just within their form.

#### Optional Properties
| Property | Type | Default | Description | Behaviour |
|----------|------|---------|-------------|----------|
| `condition` | object | null | Visibility condition | Malformed conditions crash form |
| `description` | string | null | Help text (not widely supported) | May not display |

## Field-Specific Structure Considerations {comprehensive}

### Text Fields {#text-fields}

**Structure patterns**:
- Group related text fields in same section
- Place single-line before multi-line
- Consider separate section for long narrative fields
- Maximum 10-15 text fields per section for performance

### Number Fields {#number-fields}

**Structure patterns**:
- Group measurements in dedicated section
- Place units adjacent to number fields
- Consider tabs mode for many numeric fields
- Use conditional sections for optional measurements

### Date/Time Fields {#datetime-fields}

**Structure patterns**:
- Place timestamps early in form
- Group temporal fields together
- Consider sticky fields for dates across children
- Use DateTime Now for automatic capture

### Selection Fields {#select-fields}

**Structure patterns**:
- Radio buttons best for 2-5 options inline
- Dropdowns for >5 options or limited space
- Checkboxes in separate section if many
- Consider conditional logic for hierarchical choices

### Location Fields {#location-fields}

**Structure patterns**:
- Dedicated location section recommended
- Place map widget prominently
- Group coordinate fields together
- Consider mobile-first for GPS capture

### Media Fields {#media-fields}

**Structure patterns**:
- Separate media section or form
- Last section to avoid performance impact
- Consider dedicated photo form for many images
- Limit to 5-10 photos per section

### Display Fields {#display-fields}

**Structure patterns**:
- Use for section introductions
- Place at beginning of sections
- Consider for conditional instructions
- Avoid excessive display fields (performance)

### Relationship Fields {#relationship-field}

**Structure patterns**:
- Place parent link first in child forms
- Group related relationships
- Consider dedicated relationships section
- Use tabs mode for complex hierarchies

## Parent-Child Hierarchies {important}

### Common Archaeological Patterns {#archaeological-hierarchies}

- **Context → Feature → Sample**: Excavation units containing features with samples
- **Site → Trench → Context → Find**: Multi-level spatial organisation
- **Survey → Transect → Observation → Photo**: Systematic survey structure
- **Building → Room → Element → Condition**: Architectural recording

### Heritage Management Workflows {#heritage-hierarchies}

- **Property → Building → Element → Issue → Intervention**: Asset management
- **Site → Monument → Component → Material → Treatment**: Conservation planning
- **Landscape → Character Area → Feature → Attribute**: Landscape characterisation
- **Collection → Box → Object → Component → Analysis**: Museum cataloguing

### Ecological Survey Patterns {#ecological-hierarchies}

- **Site → Plot → Quadrat → Species → Individual**: Vegetation surveys
- **Transect → Point → Observation → Measurement → Photo**: Wildlife monitoring
- **Station → Visit → Sample → Subsample → Analysis**: Water quality monitoring
- **Grid → Cell → Trap → Capture → Biometric**: Mark-recapture studies

### Hierarchy Design Principles

1. **Limit depth**: Maximum 3-4 levels for usability
2. **Create parent first**: Always save parent before children
3. **Use sticky fields**: Carry context between children
4. **Plan relationships**: Document parent-child structures
5. **Consider orphan handling**: Plan for soft-delete scenarios

## Data Flow and Persistence {important}

### Save and Navigation Flow {#data-flow}

**Current System**:
```
User Input → Field onChange → Formik State → 10 Second Timer → Draft DB
User Navigates → Force Save → Draft DB
User Clicks "Finish and..." → Production DB → Delete from Draft
```

Note: A future roadmap item includes eliminating the draft database to simplify the data flow.

### Navigation State Management

```javascript
// Component state (not Redux)
state = {
  activeStep: 2,              // Current section index
  view_cached: "details",     // Current section ID
  visitedSteps: Set(["basic", "details"]) // Visited sections
}
```

**Important**: Navigation position is NOT persisted - users return to first section on reload.

### publishButtonBehaviour Logic

```javascript
"always"    // Save always enabled (default)
"visited"   // Enabled when all visible sections visited
"noErrors"  // Enabled when no validation errors exist
```

**Note**: Conditional hidden sections don't block "visited" requirement.

## Performance Optimization {comprehensive}

### Performance Characteristics by Structure {#performance}

**Note**: These are approximate guidelines based on code analysis. Actual performance varies by device, browser, and specific field types. Test with your specific use case.

| Structure Pattern | Estimated Field Threshold | Expected Performance | Use Case |
|------------------|---------------------------|---------------------|-----------|
| Single section inline | ~50 fields | Good | Quick surveys |
| Multi-section inline | ~100 total | Acceptable | Linear workflows |
| Tabs with 3-5 sections | ~30/section | Good | Standard forms |
| Tabs with 6-10 sections | ~20/section | Acceptable | Complex recording |
| Deep hierarchies (4+ levels) | Fewer fields recommended | Variable | Detailed documentation |

### Optimization Strategies

1. **Split large forms**: Break into multiple smaller forms
2. **Use conditional sections**: Hide irrelevant fields
3. **Separate media**: Isolate photos/files in dedicated forms
4. **Limit fields per section**: Maximum 50, ideally <30
5. **Avoid deep nesting**: Each level adds complexity
6. **Test on target devices**: Mobile performance varies

### Common Performance Issues

| Issue | Impact | Mitigation |
|-------|--------|------------|
| >100 fields/section | Severe lag | Split into multiple sections |
| >30 conditional fields | Evaluation lag | Reduce conditions or split forms |
| All sections inline with many fields | Memory spike | Use tabs mode |
| Deep hierarchies (>4 levels) | Navigation complexity | Flatten structure |

## Conditional Section Patterns {comprehensive}

### Progressive Disclosure {#conditional-sections}

```json
{
  "fviews": {
    "screening": {
      "label": "Initial Screening",
      "fields": ["material-type", "requires-detailed"]
    },
    "detailed-recording": {
      "label": "Detailed Recording",
      "fields": ["measurements", "surface-treatment"],
      "condition": {
        "operator": "equal",
        "field": "requires-detailed",
        "value": true
      }
    }
  }
}
```

### Role-Based Sections

```json
{
  "specialist-section": {
    "label": "Specialist Recording",
    "fields": ["analysis-type", "specialist-notes"],
    "condition": {
      "operator": "and",
      "conditions": [
        {"operator": "equal", "field": "requires-specialist", "value": true},
        {"operator": "not-equal", "field": "status", "value": "preliminary"}
      ]
    }
  }
}
```

### Conditional Logic Limitations

- Cannot reference other forms
- Cannot reference parent fields
- Cannot check array properties
- Malformed conditions crash form
- Performance degradation with 20-30 conditional fields

## Validation and Navigation {important}

### Non-Blocking Validation Pattern {#validation}

Navigation is never blocked by validation errors:

1. User can navigate freely between sections
2. Errors shown but don't prevent movement
3. Save button behaviour controlled by `publishButtonBehaviour`
4. Submit attempt jumps to first error

### Visual Error Indicators

| Platform | Section with Errors | Required Fields | Completed Section |
|----------|-------------------|-----------------|-------------------|
| Desktop Tabs | Red dot with count | Asterisk (*) | Checkmark (✓) |
| Desktop Inline | Red text below header | Asterisk (*) | Green border |
| Mobile | Red badge on step | Red asterisk | Green checkmark |

## Structure Pattern Examples {comprehensive}

### Example 1: Simple Two-Level Hierarchy

```json
{
  "ui-specification": {
    "visible_types": ["site-form", "feature-form"],
    "viewsets": {
      "site-form": {
        "label": "Site Record",
        "views": ["site-basic", "site-location"],
        "layout": "inline"  // Few sections, simple structure
      },
      "feature-form": {
        "label": "Feature Record",
        "views": ["feature-details", "feature-measurements"],
        "layout": "tabs",  // More complex, benefits from tabs
        "publishButtonBehaviour": "noErrors"
      }
    }
  }
}
```

### Example 2: Performance-Optimized Structure

```json
{
  "viewsets": {
    "observations": {
      "label": "Species Observations",
      "views": ["species-1", "species-2", "species-3"],
      "layout": "tabs"  // Split large form across tabs
    }
  },
  "fviews": {
    "species-1": {
      "label": "Common Species (1-25)",
      "fields": [/* 25 fields max for performance */]
    },
    "species-2": {
      "label": "Common Species (26-50)",
      "fields": [/* 25 fields max */],
      "condition": {
        "operator": "equal",
        "field": "record-all-species",
        "value": true
      }
    }
  }
}
```

### Example 3: Complex Multi-Branch Hierarchy

```json
{
  "visible_types": ["trench", "context", "find", "sample", "photo"],
  "viewsets": {
    "context": {
      "label": "Context",
      "views": ["context-basic", "context-matrix", "context-interpretation"],
      "layout": "tabs",  // Complex form benefits from tabs
      "publishButtonBehaviour": "noErrors"
    }
  }
}
```

## Mobile vs Desktop Considerations {important}

### Mobile-Specific Features {#mobile-considerations}
- GPS functionality for coordinates
- Camera integration for photos
- QR/barcode scanning
- Touch optimized interface
- Offline capability priority

### Desktop-Specific Features
- Larger screen for complex forms
- Keyboard navigation
- Multiple windows for reference
- Better for data review
- Notebook design using Designer

### Choosing Your Platform
- **Tablets**: Optimal middle ground for field work
- **Phones**: Quick data capture, simple forms
- **Desktop**: Complex forms, data review, notebook design
- Design acknowledging most field collection on mobile

## Troubleshooting Structure Issues {comprehensive}

### Common Issues and Solutions

| Issue | Symptoms | Solution |
|-------|----------|----------|
| Form won't load | White screen | Check conditions in JSON |
| Sections missing | Not visible | Verify section IDs and conditions |
| Slow form response | Typing lag | Reduce fields per section |
| Lost form state | Data disappears | Enable cookies/localStorage |
| Navigation confused | Wrong section shown | Check for duplicate section IDs |

### Debug Checklist

- [ ] All field IDs globally unique
- [ ] All section IDs globally unique
- [ ] < 50 fields per section
- [ ] < 20 conditional fields per form
- [ ] < 10 sections per form for tabs
- [ ] Conditions reference existing fields only

## Best Practices Summary {comprehensive}

### DO:
✅ Plan structure before building  
✅ Use tabs mode for complex forms  
✅ Limit fields per section (<50)  
✅ Group related fields together  
✅ Test on target mobile devices  
✅ Use conditional sections for optional data  
✅ Configure human-readable IDs  

### DON'T:
❌ Exceed 100 fields per section  
❌ Create hierarchies >4 levels deep  
❌ Mix unrelated fields in sections  
❌ Forget global uniqueness of IDs  
❌ Ignore mobile performance  
❌ Use complex conditions (>20 fields)  

## Migration Notes {comprehensive}

### Current System Considerations
- Draft database requires "Finish and..." to save to production
- Two-database architecture
- Navigation state not persisted across sessions
- No deep linking to specific sections

### Potential Future Improvements
Various improvements are being considered for the roadmap, including navigation persistence, deep linking support, and architecture simplifications.

## Related Documentation {important}

- [Field Selection Guide](./field-selection-guide.md) - Choosing appropriate field types
- [Dynamic Forms Guide](./dynamic-forms-guide.md) - Validation and conditional logic
- [Implementation Patterns Guide](./implementation-patterns-guide.md) - Common patterns
- [Component Reference](../references/component-reference.md) - Technical details
- [Platform Reference](../references/platform-reference.md) - Device-specific behaviour

<!-- concat:boundary:end section="form-structure-guide" -->