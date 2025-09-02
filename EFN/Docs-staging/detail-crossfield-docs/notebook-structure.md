# Fieldmark Forms and Sections: Comprehensive Documentation

## Hierarchical Architecture Overview

Fieldmark employs a three-tier hierarchical structure for organising data collection instruments:

1. **Fields** (`ui-specification.fields`): Individual input elements, each possessing a unique identifier
2. **Sections/Views** (`ui-specification.fviews`): Logical groupings of related fields
3. **Forms/Viewsets** (`ui-specification.viewsets`): Collections of sections representing complete data entry forms

This architecture supports complex parent – child entity relationships, wherein data collected in one form establishes hierarchical relationships with data in subsequent forms.

## Forms (Viewsets) Specification

### Conceptual Purpose

Forms represent discrete entities within the data model. A typical archaeological deployment might comprise:
- **Context Form**: Primary entity recording excavation contexts
- **Feature Form**: Child entity of Context, recording archaeological features
- **Artefact Group Form**: Child entity of Context, recording assemblages
- **Artefact Form**: Child entity of Artefact Group, recording individual objects

### Technical Configuration

Each viewset requires the following properties:

```json
{
  "viewset-id": {
    "label": "Human-readable form name",
    "views": ["section-id-1", "section-id-2"],
    "hridField": "field-id-for-human-readable-identifier",
    "publishButtonBehaviour": "always|visited|noErrors",
    "layout": "inline|tabs",
    "summary_fields": ["field-id-1", "field-id-2"]
  }
}
```

#### Property Specifications

- **label**: The form name displayed to users in navigation and headers
- **views**: Ordered array of section identifiers belonging to this form
- **hridField**: Designates which field provides the human-readable identifier for records (critical for record lists and relationships)
- **publishButtonBehaviour**: Controls save button enablement
  - `"always"`: Button remains enabled regardless of form state
  - `"visited"`: Enabled only after user visits all sections
  - `"noErrors"`: Enabled only when no validation errors exist
- **layout**: Determines section presentation mode
  - `"inline"` (default): Vertical scrolling through all sections
  - `"tabs"`: Horizontal navigation with section indicators
- **summary_fields** (optional): Fields displayed in record list views

### Required Root Properties

The UI specification must include:
- **visible_types**: Array listing which forms to display in the interface
- Forms lacking `publishButtonBehaviour` will fail to load

## Sections (Views) Specification

### Conceptual Purpose

Sections provide logical organisation within forms, grouping related fields for improved user comprehension and workflow efficiency. Sections serve purely organisational purposes without functional properties beyond display control.

### Technical Configuration

```json
{
  "section-id": {
    "label": "Section Heading",
    "fields": ["field-id-1", "field-id-2"],
    "condition": {
      "operator": "equal",
      "field": "controller-field-id",
      "value": "trigger-value"
    }
  }
}
```

#### Display Modes

**Inline Mode** (default):
- All sections rendered vertically within a continuous scrollable page
- Optimal for shorter forms or mobile interfaces
- Provides immediate visibility of all available sections

**Tab Mode** (`layout: "tabs"`):
- Sections presented as navigable tabs or stepper components
- Desktop: Horizontal stepper with named sections
- Mobile: Compact stepper with previous/next navigation
- Visual indicators convey:
  - Current section (scaled emphasis)
  - Visited sections (visual marking)
  - Sections containing errors (red badge indicators)

## Navigation Patterns and Workflows

### Standard Navigation Flow

1. User enters a form from the record list or through parent – child creation
2. Progresses through sections (vertically in inline mode, horizontally in tab mode)
3. Creates child entities via dedicated UI elements, which:
   - Navigates to the appropriate child form
   - Preserves parent context
   - Allows recursive child creation
4. Completes child entity with "Save and Close" (returning to parent) or "Save and New" (creating sibling)
5. Finalises parent form with "Save and Close" (returning to record list) or "Save and New" (creating sibling)

### Navigation Flexibility

Whilst the above represents typical workflow, the system permits considerable flexibility:
- Users may navigate between sections non-linearly
- Forms may be saved in incomplete states (though required fields generate warnings)
- Navigation state persists during child entity creation
- Back navigation maintains form state and entered data

## Conditional Logic Framework

### Implementation Architecture

Conditional display logic applies at three levels:
- **Field Level**: Individual fields appear/disappear based on conditions
- **Section Level**: Entire sections show/hide dynamically
- **Form Level**: Forms can be conditionally available based on parent data

### Condition Specification

Simple conditions:
```json
{
  "operator": "equal|not-equal|greater-than|less-than",
  "field": "controller-field-id",
  "value": "comparison-value"
}
```

Complex conditions:
```json
{
  "operator": "and|or",
  "conditions": [
    {"operator": "equal", "field": "type", "value": "detailed"},
    {"operator": "not-equal", "field": "status", "value": "draft"}
  ]
}
```

### Performance Optimisation

The conditional logic system employs sophisticated optimisation:
- Conditions compile to JavaScript functions (`conditionFn`) for efficient evaluation
- Re-evaluation occurs only when "controller fields" change
- Controller fields identified through:
  - Presence of `logic_select` property (legacy mechanism)
  - Inclusion in `conditional_sources` set
- This targeted re-evaluation prevents unnecessary computation

## State Management

### Form State Tracking

The system maintains several state dimensions:
- **Active Step**: Current section in tab mode
- **Visited Steps**: Set of section identifiers user has accessed
- **Field Errors**: Validation errors propagated to section indicators
- **Form Completeness**: Aggregate of required field satisfaction

### Validation Cascade

Validation operates hierarchically:
1. Field-level validation executes on value change
2. Section-level indicators aggregate field validation states
3. Form-level controls respond to aggregate validation state
4. Parent forms may validate child entity requirements

## Platform-Specific Considerations

### Mobile Adaptations
- Tab mode utilises mobile-optimised stepper component
- Inline mode provides better single-handed navigation
- Touch targets sized appropriately for mobile interaction
- Reduced information density in mobile layouts

### Desktop Optimisations
- Tab mode displays full section names
- Keyboard navigation fully supported
- Multiple sections potentially visible simultaneously
- Higher information density permitted

## Creation Workflows in Designer

### Form Creation Patterns

Users exhibit varied approaches to form construction:

**Top-Down Approach**:
1. Create all forms first
2. Add sections to each form
3. Populate sections with fields

**Incremental Approach**:
1. Create first form
2. Add all sections and fields
3. Proceed to next form

**Hybrid Approaches**:
- Any combination of the above patterns is supported
- Designer permits non-linear construction workflows
- JSON editing can supplement GUI-based design at any stage

### Control Centre – Designer Integration

The system implements a sophisticated seamless integration between administrative and design interfaces:

**Workflow Initiation**:
1. User navigates to notebook in Control Centre
2. Selects "Open in Editor" from Actions tab
3. Designer launches as modal overlay (95vw × 95vh) within same browser tab
4. Control Centre remains accessible beneath the modal layer

**Technical Implementation**:
- Redux store instantiation for state management
- Automatic JSON migration for schema compatibility
- Unique designer identifiers injected for internal tracking
- In-memory router creation for Designer navigation
- Browser-level beforeunload event listener prevents accidental data loss

**Save and Synchronisation**:
- "Done" action extracts current Redux state
- Designer identifiers stripped from exported JSON
- File object generated with formatted JSON
- PUT request updates notebook in Control Centre
- React Query cache invalidation ensures UI synchronisation
- Modal closes with smooth animation, returning to Control Centre

This architecture ensures data integrity whilst providing a fluid editorial experience, eliminating the friction traditionally associated with JSON import/export workflows.

### Template System

- Any notebook can be saved as a template
- Templates create editable copies through "Create New from Template"
- Template library development ongoing
- JSON-based template sharing currently required (GUI tools in development)

## JSON Interoperability

The system maintains complete bidirectional compatibility between Designer GUI and JSON representation:
- Notebooks created in Designer can be exported as JSON
- JSON can be manually edited and reimported
- Claude Code can generate JSON for Designer refinement
- Invalid JSON triggers validation errors rather than system failures
- Hybrid workflows (GUI + manual editing + AI generation) fully supported

## Performance Characteristics

### Rendering Optimisation
- Lazy loading of sections in tab mode
- Virtual scrolling for long inline forms
- Conditional elements excluded from DOM when hidden

### Validation Performance
- Per-section validation reduces computation
- Controller field mechanism prevents validation cascades
- Asynchronous validation supported for external checks

### Memory Management
- Unsaved data persisted in local state
- Large media fields utilise reference storage
- Automatic cleanup of orphaned child entities