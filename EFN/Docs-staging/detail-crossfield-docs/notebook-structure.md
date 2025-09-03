# Notebook Structure: Forms, Sections, and Fields - Third Draft Documentation

## Overview

Fieldmark notebooks employ a three-tier hierarchical architecture organizing data collection into Forms (viewsets), Sections (views), and Fields. This structure scales from simple single-form checklists to sophisticated multi-entity recording systems with dozens of interconnected forms supporting complex parent-child relationships. The architecture operates without virtualization, rendering all fields simultaneously, which creates performance boundaries at approximately 50-100 fields per section. Critical architectural decisions—such as field ID uniqueness being global across the entire notebook—cascade through the system and cannot be modified after data collection begins without risk of data loss.

The system's distributed nature introduces unique behaviors: child records orphaned by soft-deleted parents remain accessible, circular parent-child relationships are possible without prevention, and malformed conditional logic can crash entire forms. Understanding these architectural realities alongside the flexible configuration options enables notebook designers to create robust data collection instruments whilst avoiding documented performance cliffs and structural pitfalls.

## Common Use Cases

### Archaeological Recording Hierarchies
• **Context → Feature → Sample**: Excavation units containing features with associated samples
• **Site → Trench → Context → Find**: Multi-level spatial organisation with artefact recording  
• **Survey → Transect → Observation → Photo**: Systematic survey with structured observations
• **Building → Room → Element → Condition**: Architectural recording with condition assessments
• **Area → Structure → Deposit → Artefact Group → Artefact**: Deep hierarchical excavation recording

### Heritage Management Workflows
• **Property → Building → Element → Issue → Intervention**: Asset management with remediation tracking
• **Site → Monument → Component → Material → Treatment**: Conservation planning hierarchies
• **Landscape → Character Area → Feature → Attribute**: Landscape characterisation studies
• **Collection → Box → Object → Component → Analysis**: Museum cataloguing with conservation

### Ecological Survey Patterns  
• **Site → Plot → Quadrat → Species → Individual**: Vegetation surveys with specimen tracking
• **Transect → Point → Observation → Measurement → Photo**: Wildlife monitoring protocols
• **Station → Visit → Sample → Subsample → Analysis**: Water quality monitoring
• **Grid → Cell → Trap → Capture → Biometric**: Mark-recapture studies

### Geological Documentation
• **Formation → Member → Bed → Sample → Analysis**: Stratigraphic recording
• **Site → Outcrop → Unit → Structure → Measurement**: Structural geology mapping
• **Core → Section → Interval → Sample**: Drilling documentation

## Core Configuration

### Required Root Properties
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
**Critical**: Forms omitted from `visible_types` remain accessible via relationships but hidden from navigation menu. Empty or undefined `visible_types` shows all forms.

### Form (Viewset) Configuration

#### Required Properties
| Property | Type | Description | Default if Missing |
|----------|------|-------------|-------------------|
| `label` | string | Display name in navigation | Form ID used |
| `views` | array | Section IDs in display order | Empty array (blank form) |
| `publishButtonBehaviour` | string | Save button logic | `"always"` |

**Note**: Contrary to some documentation, missing `publishButtonBehaviour` does NOT cause failure—defaults to `"always"`.

#### Optional Properties  
| Property | Type | Default | Description | Constraints |
|----------|------|---------|-------------|-------------|
| `hridField` | string | Falls back to "hrid" prefix | Field providing human-readable ID | Must reference existing field |
| `layout` | string | `"inline"` | Section presentation mode | `"inline"` or `"tabs"` only |
| `summary_fields` | array | `[]` | Fields shown in record lists | Gracefully handles missing fields |

**Removed Properties**: Documentation may reference `parent_link` or `is_root`—these properties do not exist. Parent-child relationships are configured at field level using RelationshipField.

### Section (View) Configuration

#### Required Properties
| Property | Type | Description | Constraints |
|----------|------|-------------|-------------|
| `label` | string | Section heading displayed | Any string |
| `fields` | array | Field IDs in display order | Must reference existing fields; IDs globally unique |

**Critical**: Section IDs must be globally unique across ALL forms, not just within their form. Designer auto-generates IDs as `viewSetId-slugified-label`.

#### Optional Properties
| Property | Type | Default | Description | Behavior |
|----------|------|---------|-------------|----------|
| `condition` | object | null | Visibility condition | Malformed conditions crash form |
| `description` | string | null | Help text (not widely supported) | May not display |

### Field ID Requirements
**Critical Architecture Decision**: Field IDs must be globally unique across the ENTIRE notebook, not per section or form. The system maintains a single global namespace for all fields. Duplicate field IDs cause configuration overwrites without warning.

## Validation Rules

### Form-Level Validation

| Validation Type | Trigger | Behavior | Error Display | Recovery |
|-----------------|---------|----------|---------------|----------|
| Required fields | Save attempt | Blocks submission | Red badge on section, field error | Fill required fields |
| Field validation | Field blur | Non-blocking | Below field, section indicator | Correct field value |
| Schema compliance | JSON import | May fail silently | Console warnings only | Check browser console |
| Missing sections | Form render | Ignored | Console warning | Section omitted from display |
| Missing fields | Section render | Ignored | Console warning: "undefined field" | Field omitted from display |
| Malformed conditions | Form load | **CRASHES FORM** | White screen | Fix JSON, reimport |

### Section-Level Validation Aggregation

| Platform | Error Display | Visited Tracking | Required Indicator | Completion Status |
|----------|---------------|------------------|-------------------|-------------------|
| Desktop (inline) | Red text below section header | N/A | Asterisk in header | N/A |
| Desktop (tabs) | Red dot with count on tab | Checkmark when visited | Asterisk on tab | All tabs show status |
| iOS | Red badge on step | Green when visited | Red asterisk | Step counter (3/5) |
| Android | Red indicator | Tick mark | Bold asterisk | Fraction (3/5) |

### Configuration Validation Examples

```json
{
  "viewset-validation": {
    "views": ["section-1", "nonexistent-section"],  // Silently ignores missing
    "hridField": "missing-field",                    // Falls back to "hrid" prefix
    "publishButtonBehaviour": null                   // Defaults to "always"
  },
  "section-validation": {
    "fields": ["field-1", "undefined-field"],        // Logs warning, continues
    "condition": {
      "field": "nonexistent",                        // May crash at runtime
      "operator": "invalid"                          // WILL crash form
    }
  }
}
```

## Display Behaviour

### Desktop Rendering

#### Inline Layout Mode (Default)
- All sections render vertically without virtualization
- Performance degrades beyond 50-100 fields per section
- Smooth scroll anchors to section starts
- Section headers NOT sticky (browser limitation)
- Fields render in exact array order
- No lazy loading—entire form in DOM

#### Tabs Layout Mode
- Horizontal stepper with full section names
- Previous/Next buttons flank stepper
- Current section scales 1.2x for emphasis
- All sections still rendered (no lazy loading)
- Keyboard: Tab/Shift-Tab navigates sections
- Visited sections show checkmark indicator
- Error sections show red badge with count

### Mobile Rendering

#### iOS Behaviour
- Tabs compact to numbered stepper (1/5 format)
- Swipe gestures conflict with system gestures
- Momentum scrolling in inline mode
- Form header remains fixed
- Software keyboard pushes content up
- No viewport optimization for large forms

#### Android Behaviour  
- Material Design stepper in tabs mode
- Hardware back button behavior inconsistent
- FAB for save action (when implemented)
- Predictive back gesture may show previous section
- Pull-to-refresh not implemented
- Same performance limits as iOS

### Responsive Breakpoints
```javascript
// From useScreenSize.tsx
xs: < 576px     // Phone portrait
sm: 576-768px    // Phone landscape/small tablet
md: 768-992px    // Tablet
lg: 992-1200px   // Desktop
xl: > 1200px     // Large desktop
```

### Performance Characteristics
- **50-100 fields/section**: Noticeable input lag begins
- **100+ fields/section**: Significant degradation
- **200+ fields/section**: Near unusable
- **20-30 conditional fields**: Evaluation lag noticeable
- **No virtualization**: All fields always in DOM
- **No pagination**: Complete form always rendered

## Interaction Patterns

### Navigation Flows

#### Linear Progression (Tabs Mode)
1. User enters form at first section
2. Completes fields in current section  
3. Clicks "Next" or section tab
4. Validation occurs if `publishButtonBehaviour: "noErrors"`
5. Section marked as visited in `visitedSteps` Set
6. Hidden conditional sections do NOT count as visited
7. Save enabled based on publishButtonBehaviour logic

#### Non-Linear Access (Inline Mode)
1. All sections immediately visible (performance impact)
2. User scrolls to any section (no tracking)
3. Can fill sections in any order
4. No visited tracking in inline mode
5. Save button follows publishButtonBehaviour rules

#### Parent-Child Navigation
1. Parent form provides RelationshipField with `relation_type: "Child"`
2. "Add New [Type]" button navigates to child form
3. Parent context preserved in location state (not configuration)
4. Child automatically linked to parent
5. "Save & Return" navigates back to parent
6. "Save & Add Another" creates sibling
7. Parent can have multiple different child types via multiple RelationshipFields

### State Persistence
- Form state preserved during child creation
- Unsaved changes trigger browser beforeunload warning
- No auto-save implementation (documentation incorrect)
- Offline changes stored in PouchDB
- Navigation history maintained in browser

### publishButtonBehaviour Logic
```javascript
// Actual implementation
"always"    // Save always enabled (default)
"visited"   // Enabled when all visible sections visited
"noErrors"  // Enabled when no validation errors exist
```
**Note**: Conditional hidden sections don't block "visited" requirement.

## Conditional Logic Support

### Section-Level Conditions

```json
{
  "archaeological-section": {
    "label": "Archaeological Details",
    "fields": ["period", "phase", "finds"],
    "condition": {
      "operator": "equal",
      "field": "site-type",        // Must exist in same form
      "value": "archaeological"
    }
  }
}
```

### Complex Multi-Condition Logic

```json
{
  "specialist-section": {
    "label": "Specialist Recording",
    "fields": ["analysis-type", "specialist-notes"],
    "condition": {
      "operator": "and",
      "conditions": [
        {"operator": "equal", "field": "requires-specialist", "value": true},
        {"operator": "not-equal", "field": "status", "value": "preliminary"},
        {"operator": "or", "conditions": [
          {"operator": "equal", "field": "material", "value": "ceramic"},
          {"operator": "equal", "field": "material", "value": "lithic"}
        ]}
      ]
    }
  }
}
```

### Conditional Logic Limitations
- **Cannot reference other forms**: Only fields in same form accessible
- **Cannot reference parent fields**: No `$parent.field` syntax
- **Cannot check array properties**: No `.length` or indexed access
- **Malformed conditions crash form**: No error recovery
- **Performance degradation**: 20-30 conditional fields cause lag

### Performance Optimization
- Conditions compile to JavaScript functions once
- Re-evaluation ONLY when controller fields change
- Controller fields identified by presence in conditions
- Initial load evaluates all conditions
- Smart optimization skips non-controller field changes

## Data Storage and Export

### Database Structure (PouchDB/CouchDB)

```json
{
  "_id": "ctx_001_abc123",
  "type": "context",              // Form type from viewset ID
  "created": "2024-03-15T10:30:00Z",
  "created_by": "user@example.com",
  "updated": "2024-03-15T14:20:00Z",
  "updated_by": "user@example.com",
  "deleted": false,               // Soft delete flag
  "data": {
    "context-id": "CTX-001",
    "description": "Occupation layer",
    "finds": [                    // Child relationships
      {
        "record_id": "fnd_001_def456",
        "relation_type_vocabPair": ["is child of", "is parent of"]
      }
    ]
  }
}
```

### Parent-Child Data Structure
- **Parent → Child**: One-to-many via RelationshipField
- **Child → Parent**: Reference stored in child's relationship field
- **Orphaned children**: Remain when parent soft-deleted
- **Multiple child types**: Single parent can have different child forms
- **Circular relationships**: Possible, not prevented
- **No cascade delete**: Children must be manually managed

### CSV Export Format

#### File Structure
- Each form type exports as separate CSV file
- Filename: `formtype_export_timestamp.csv`
- Relationships flattened to string format

#### Relationship Encoding
```csv
_id,identifier,description,stratigraphic_relationships,finds
ctx001,CTX-001,Occupation layer,"cuts/ctx002;fills/ctx003","is parent of/fnd001;is parent of/fnd002"
```

#### Export Characteristics
- **Format**: `{vocabulary}/{record_id}` semicolon-delimited
- **Hierarchy lost**: Parent-child structure flattened
- **No re-import**: Relationships cannot be restored from CSV
- **Metadata preserved**: Timestamps and user info included
- **Empty fields**: Exported as empty strings, not null

### JSON Export Structure
```json
{
  "notebook_version": "1.0.0",
  "export_date": "2024-03-15T16:00:00Z",
  "records": {
    "context": [ /* array of context records */ ],
    "find": [ /* array of find records */ ]
  },
  "relationships": {
    "hierarchical": [ /* parent-child mappings */ ],
    "linked": [ /* peer relationships */ ]
  }
}
```

## Common Patterns

### Example 1: Simple Two-Level Hierarchy (Site → Feature)
```json
{
  "ui-specification": {
    "visible_types": ["site-form", "feature-form"],
    "viewsets": {
      "site-form": {
        "label": "Site Record",
        "views": ["site-basic", "site-location"],
        "hridField": "site-id",
        "publishButtonBehaviour": "always",
        "layout": "inline"
      },
      "feature-form": {
        "label": "Feature Record", 
        "views": ["feature-details", "feature-measurements"],
        "hridField": "feature-number",
        "publishButtonBehaviour": "noErrors",
        "layout": "tabs"
      }
    },
    "fviews": {
      "site-basic": {
        "label": "Basic Information",
        "fields": ["site-id", "site-name", "recorder", "date"]
      },
      "site-location": {
        "label": "Location Details",
        "fields": ["grid-ref", "map-widget", "access-notes"]
      },
      "feature-details": {
        "label": "Feature Information",
        "fields": ["feature-number", "feature-type", "description", "parent-site"]
      },
      "feature-measurements": {
        "label": "Dimensions",
        "fields": ["length", "width", "depth", "volume"],
        "condition": {
          "operator": "not-equal",
          "field": "feature-type",
          "value": "surface-scatter"
        }
      }
    },
    "fields": {
      "parent-site": {
        "component-namespace": "faims-custom",
        "component-name": "RelatedRecordSelector",
        "type-returned": "faims-core::Relationship",
        "component-parameters": {
          "label": "Parent Site",
          "name": "parent-site",
          "related_type": "site-form",
          "relation_type": "Child",
          "multiple": false,
          "allowLinkToExisting": true
        }
      }
      // ... other field definitions
    }
  }
}
```
**Behavior**: Features link to sites via RelationshipField. Measurements section hidden for surface scatters. Forms outside `visible_types` still accessible via relationships.

### Example 2: Complex Multi-Branch Hierarchy
```json
{
  "ui-specification": {
    "visible_types": ["trench", "context", "find", "sample", "photo"],
    "viewsets": {
      "trench": {
        "label": "Trench",
        "views": ["trench-info", "trench-team"],
        "hridField": "trench-code",
        "publishButtonBehaviour": "visited",
        "layout": "tabs"
      },
      "context": {
        "label": "Context", 
        "views": ["context-basic", "context-matrix", "context-interpretation"],
        "hridField": "context-number",
        "publishButtonBehaviour": "noErrors",
        "layout": "tabs"
      },
      "find": {
        "label": "Find",
        "views": ["find-basic", "find-details"],
        "hridField": "find-number",
        "publishButtonBehaviour": "always"
      },
      "sample": {
        "label": "Sample",
        "views": ["sample-info", "sample-processing"],
        "hridField": "sample-number", 
        "publishButtonBehaviour": "always"
      },
      "photo": {
        "label": "Photograph",
        "views": ["photo-metadata", "photo-subjects"],
        "hridField": "photo-id",
        "publishButtonBehaviour": "always"
      }
    },
    "fviews": {
      "context-basic": {
        "label": "Basic Context Info",
        "fields": ["context-number", "context-type", "parent-trench", "description"]
      },
      "context-matrix": {
        "label": "Stratigraphic Matrix",
        "fields": ["stratigraphic-relationships", "physical-relationships"]
      },
      "context-interpretation": {
        "label": "Interpretation",
        "fields": ["interpretation", "period", "phase", "context-finds", "context-samples"],
        "condition": {
          "operator": "not-equal",
          "field": "context-type",
          "value": "unstratified"
        }
      }
      // ... additional view definitions
    },
    "fields": {
      "parent-trench": {
        "component-name": "RelatedRecordSelector",
        "component-parameters": {
          "label": "Parent Trench",
          "related_type": "trench",
          "relation_type": "Child",
          "multiple": false
        }
      },
      "context-finds": {
        "component-name": "RelatedRecordSelector",
        "component-parameters": {
          "label": "Finds from this Context",
          "related_type": "find",
          "relation_type": "Child",
          "multiple": true,
          "allowLinkToExisting": false
        }
      },
      "context-samples": {
        "component-name": "RelatedRecordSelector",
        "component-parameters": {
          "label": "Samples from this Context",
          "related_type": "sample",
          "relation_type": "Child",
          "multiple": true
        }
      },
      "stratigraphic-relationships": {
        "component-name": "RelatedRecordSelector",
        "component-parameters": {
          "label": "Stratigraphic Relationships",
          "related_type": "context",
          "relation_type": "is-related-to",
          "relation_linked_vocabPair": [
            ["cuts", "is cut by"],
            ["fills", "is filled by"],
            ["above", "below"]
          ]
        }
      }
      // ... additional field definitions
    }
  }
}
```
**Behavior**: Single parent (Context) has multiple child types (Find, Sample). Circular relationships possible between contexts. Interpretation section conditional on stratified contexts.

### Example 3: Performance-Optimized Structure
```json
{
  "ui-specification": {
    "visible_types": ["survey-point", "observations", "photos"],
    "viewsets": {
      "survey-point": {
        "label": "Survey Point",
        "views": ["point-location", "point-environment"],
        "layout": "inline",  // Better for mobile with few fields
        "publishButtonBehaviour": "always"
      },
      "observations": {
        "label": "Species Observations",
        "views": ["species-1", "species-2", "species-3", "species-4"],
        "layout": "tabs",  // Split large form across tabs
        "publishButtonBehaviour": "visited"
      },
      "photos": {
        "label": "Photo Record",
        "views": ["photo-capture"],  // Separate form for media
        "publishButtonBehaviour": "always"
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
      },
      "species-3": {
        "label": "Rare Species",
        "fields": [/* 20 fields */],
        "condition": {
          "operator": "equal",
          "field": "rare-species-present",
          "value": true
        }
      }
    }
  }
}
```
**Behavior**: Limits fields per section to maintain performance. Conditional sections reduce initial load. Media separated to dedicated form.

### Example 4: Conditional Section Cascade
```json
{
  "fviews": {
    "screening": {
      "label": "Initial Screening",
      "fields": ["material-type", "requires-detailed", "requires-specialist"]
    },
    "detailed-recording": {
      "label": "Detailed Recording",
      "fields": ["measurements", "surface-treatment", "manufacture"],
      "condition": {
        "operator": "equal",
        "field": "requires-detailed",
        "value": true
      }
    },
    "ceramic-analysis": {
      "label": "Ceramic Specialist Recording",
      "fields": ["fabric", "form", "decoration"],
      "condition": {
        "operator": "and",
        "conditions": [
          {"operator": "equal", "field": "material-type", "value": "ceramic"},
          {"operator": "equal", "field": "requires-specialist", "value": true}
        ]
      }
    },
    "lithic-analysis": {
      "label": "Lithic Specialist Recording", 
      "fields": ["raw-material", "technology", "use-wear"],
      "condition": {
        "operator": "and",
        "conditions": [
          {"operator": "equal", "field": "material-type", "value": "lithic"},
          {"operator": "equal", "field": "requires-specialist", "value": true}
        ]
      }
    }
  }
}
```
**Behavior**: Progressive disclosure based on screening decisions. Only evaluates conditions when controller fields change. Maximum 3-4 conditional sections recommended before performance impact.

## Troubleshooting Guide

### Common Issues and Solutions

| Issue | Symptoms | Diagnosis | Solution |
|-------|----------|-----------|----------|
| Form won't load | White screen, no content | Check console for condition compilation errors | Fix malformed conditions in JSON |
| Sections missing | Expected sections not visible | Condition evaluating false or section ID wrong | Verify controller field values and section IDs |
| Save button disabled | Cannot save despite filling fields | publishButtonBehaviour requirement not met | Check setting: "always", "visited", or "noErrors" |
| Fields not appearing | Blank sections | Field IDs don't exist or duplicated globally | Ensure globally unique field IDs |
| Slow form response | Lag when typing | Too many fields (>100) or conditionals (>30) | Split into multiple sections/forms |
| Lost form state | Data disappears on navigation | Browser storage disabled | Enable cookies/localStorage |
| Orphaned records | Children without parents | Parent deleted (soft delete) | Manually manage orphaned records |
| Duplicate IDs | HRID conflicts | Auto-increment not coordinated | Use device-specific prefixes |
| Export missing relationships | CSV lacks connections | Relationships flattened | Parse relationship strings manually |
| Import fails silently | JSON accepted but broken | Invalid field references | Check console for warnings |

### Debug Checklist

#### Configuration Validation
- [ ] All field IDs globally unique across entire notebook
- [ ] All section IDs globally unique across all forms  
- [ ] All referenced field IDs actually exist in fields object
- [ ] All referenced section IDs exist in fviews object
- [ ] No circular section references
- [ ] Conditions reference existing fields only

#### Performance Optimization
- [ ] < 50 fields per section (100 absolute max)
- [ ] < 20 conditional fields per form (30 absolute max)
- [ ] < 10 sections per form for tabs mode
- [ ] Media fields in separate forms where possible
- [ ] Complex calculations avoided in conditions

#### Data Integrity
- [ ] HRID fields configured for all forms
- [ ] HRID includes device/user prefix for uniqueness
- [ ] Parent-child relationships properly configured
- [ ] Soft-delete implications understood
- [ ] Export format meets analysis needs

#### Platform Testing
- [ ] Tested on target mobile devices
- [ ] Touch targets adequate size (44px minimum)
- [ ] Offline functionality verified
- [ ] Sync behavior understood

### Error Messages and Meanings

| Error Message | Location | Cause | Resolution |
|---------------|----------|-------|------------|
| "UI Spec had an undefined field with name: [field_name]" | Console | Field ID doesn't exist | Remove from section or create field |
| "Section ID already exists" | Designer | Duplicate section ID | Rename section |
| "Cannot read property 'operator' of undefined" | Console/Crash | Malformed condition | Fix condition syntax |
| "Maximum call stack exceeded" | Console/Crash | Circular condition reference | Remove circular dependency |
| "publishButtonBehaviour is undefined" | Not shown (defaults) | Missing property | Optional, defaults to "always" |
| "Cannot find viewset" | Console | Form ID mismatch | Check visible_types and viewset IDs |
| White screen (no error) | Form view | Condition compilation failed | Check all conditions in JSON |

### Common Configuration Mistakes

```json
// WRONG: Field IDs not globally unique
{
  "fviews": {
    "section-1": {"fields": ["description"]},
    "section-2": {"fields": ["description"]}  // ERROR: Duplicate field ID
  }
}

// WRONG: Malformed condition
{
  "condition": {
    "field": "my-field",  // ERROR: Missing operator
    "value": true
  }
}

// WRONG: Reference to non-existent field
{
  "condition": {
    "operator": "equal",
    "field": "nonexistent-field",  // ERROR: Field doesn't exist
    "value": "something"
  }
}

// CORRECT: Proper structure
{
  "fviews": {
    "section-1": {"fields": ["description-1"]},
    "section-2": {"fields": ["description-2"]}
  },
  "condition": {
    "operator": "equal",
    "field": "existing-field",
    "value": "expected-value"
  }
}
```

## Implementation Notes

### Technical Constraints
- **No virtualization**: All fields render simultaneously (React without windowing)
- **No lazy loading**: All sections in DOM even in tabs mode
- **Global namespace**: Field IDs must be unique across entire notebook
- **Section IDs global**: Must be unique across all forms, not just within form
- **No pagination**: Forms render completely regardless of size
- **Memory limits**: Device-dependent, typically issues beyond 200 fields total
- **Sync limitations**: Reciprocal relationships delayed until online
- **No conflict resolution**: Last-write-wins for concurrent edits

### Platform-Specific Limitations

#### Web Browser
- Sticky headers not supported consistently
- Performance varies significantly by browser
- Memory limits around 500-1000 fields total
- Local storage required for state persistence

#### iOS Application
- Tab gestures may conflict with system gestures
- Hardware keyboard support inconsistent
- Memory pressure earlier than desktop
- GPS/Camera features available

#### Android Application  
- Hardware back button behavior inconsistent
- Material Design compliance partial
- Performance similar to iOS
- Variable device capabilities

### Known Critical Issues
- **Malformed conditions crash forms**: No graceful error handling
- **Circular relationships possible**: No prevention mechanism
- **Orphaned children on delete**: Soft delete doesn't cascade
- **No schema migration**: Structure changes risk data loss
- **Silent failures common**: Missing fields/sections ignored
- **Performance cliffs undocumented**: No warnings before degradation
- **Designer GUI limitations**: Many features require JSON editing

### Designer Limitations Requiring JSON Editing
- Section reordering within forms
- Field reordering within sections  
- Complex conditional logic
- Vocabulary pairs for relationships
- Performance optimizations
- Some validation rules
- Export configurations

### Architecture Decisions and Rationale
- **Global field IDs**: Simplifies field reference resolution
- **No virtualization**: Simpler implementation, acceptable for intended scale
- **Soft delete only**: Preserves data integrity and audit trail
- **Client-side validation**: Enables offline functionality
- **Flat export format**: Maximum compatibility with analysis tools
- **Last-write-wins**: Simplest conflict resolution for distributed system

## Best Practices

### Structural Design
1. **Plan before building**: Structure cannot be safely modified after data collection
2. **Globally unique IDs**: Prefix field IDs with section/form identifier
3. **Shallow hierarchies**: Maximum 3-4 levels for usability
4. **Logical grouping**: 5-10 related fields per section
5. **Separate media forms**: Isolate photos/files for performance

### Performance Optimization
1. **Field limits**: Maximum 50 fields per section, 100 total per form
2. **Conditional restraint**: Maximum 20 conditional fields per form
3. **Tab mode for large forms**: Reduces visible field count
4. **Avoid deep nesting**: Each level adds complexity
5. **Test on target devices**: Mobile performance varies significantly

### User Experience
1. **Progressive disclosure**: Use conditions to show advanced fields
2. **Consistent navigation**: Maintain patterns across forms
3. **Clear labeling**: Section and form names describe content
4. **Logical flow**: Order sections by workflow
5. **Required field minimization**: Only mandate essential data

### Data Management  
1. **HRID configuration**: Include device/user prefix for uniqueness
2. **Relationship planning**: Document parent-child structures
3. **Export consideration**: Design with CSV limitations in mind
4. **Orphan management**: Plan for soft-delete scenarios
5. **Backup strategy**: Regular JSON exports for recovery

### Development Workflow
1. **Incremental building**: Test each form before adding next
2. **JSON validation**: Validate structure before import
3. **Performance testing**: Load test with realistic data volumes
4. **Platform testing**: Verify on all target devices
5. **Documentation**: Record structural decisions and rationale

### Team Coordination
1. **ID naming conventions**: Establish and document standards
2. **Section templates**: Create reusable section patterns
3. **Vocabulary standardization**: Agree on relationship terms
4. **Testing protocols**: Define acceptance criteria
5. **Change management**: Version control notebook definitions

## See Also

### Essential Prerequisites
- [Field Type Reference](./field-types.md) - Individual field configuration
- [RelationshipField Documentation](./relationship-field.md) - Parent-child and linked relationships
- [TemplatedStringField](./templated-string.md) - HRID generation

### Related Configuration Guides
- [Conditional Logic Guide](./conditional-logic.md) - Advanced condition syntax
- [Validation Framework](./validation.md) - Field validation rules
- [Designer Interface Guide](./designer.md) - GUI capabilities and limitations

### System Architecture
- [State Management](./state-management.md) - Redux store structure
- [Synchronization Architecture](./sync.md) - Multi-device coordination
- [Database Schema](./database.md) - PouchDB/CouchDB structure
- [Export Formats](./export.md) - CSV and JSON specifications

### Performance and Optimization
- [Performance Tuning Guide](./performance.md) - Optimization strategies
- [Mobile Deployment](./mobile.md) - Platform-specific considerations
- [Offline Capabilities](./offline.md) - Disconnected operation

### Troubleshooting Resources
- [Common Errors](./errors.md) - Error message reference
- [Migration Guide](./migration.md) - Schema change strategies
- [Debug Tools](./debug.md) - Browser developer tools usage

---

**Document Version**: 3.0  
**Last Updated**: August 2025  
**Validation**: Technical answers verified through 40-question investigation
**Status**: Production Ready

*Critical Warning: This documentation reflects actual system behavior as of August 2025, including known issues and limitations. Some behaviors differ from original design intentions. Test thoroughly in your deployment environment before production use.*