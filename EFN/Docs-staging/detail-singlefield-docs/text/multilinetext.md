Multiline Text Field - Complete Third-Draft Documentation.md
14.16 KB •333 lines
•
Formatting may be inconsistent from source

# MultilineText Field

## Overview

The MultilineText field – implemented through the MultipleTextField component – provides extended text entry capabilities within the Fieldmark ecosystem, accommodating narrative content, detailed observations, and interpretative discourse that exceeds the constraints of single-line input paradigms. This field type maintains a fixed-height presentation with internal scrolling mechanisms, eschewing auto-expansion behaviours in favour of consistent spatial allocation within form layouts. Whilst the underlying FormikTextField component permits configuration through either the dedicated MultipleTextField registration or manual TextField parametrisation, we observe universal adoption of the former approach across production deployments, establishing it as the de facto standard for multi-line text capture.

## Common Use Cases

- **Field observations and interpretations**: Recording detailed contextual observations, preliminary interpretations, and analytical narratives during data collection
- **Methodological documentation**: Capturing procedural variations, sampling strategies, and site-specific adaptations to standard protocols
- **Descriptive cataloguing**: Comprehensive artefact descriptions, stratigraphic narratives, and morphological characterisations requiring extended exposition
- **Qualitative data collection**: Interview transcriptions, ethnographic observations, and participant responses in mixed-methods research
- **Administrative annotations**: Detailed provenance information, conservation assessments, and curatorial notes exceeding brief notation
- **Interdisciplinary synthesis**: Integrative observations bridging archaeological, ecological, and geological phenomena within landscape studies

## Core Configuration

### Required Properties
```json
{
  "component-namespace": "formik-material-ui",
  "component-name": "MultipleTextField",
  "type-returned": "faims-core::String",
  "component-parameters": {
    "name": "field-identifier",
    "label": "Field Label",
    "multiline": true
  }
}
```

### Optional Properties
```json
{
  "component-parameters": {
    "helperText": "Detailed guidance for extended text entry",
    "placeholder": "Enter comprehensive observations...",
    "required": false,
    "fullWidth": true,
    "variant": "outlined",
    "disabled": false,
    "InputProps": {
      "type": "text",
      "rows": 4
    }
  },
  "validationSchema": [
    ["yup.string"],
    ["yup.max", 10000, "Maximum 10,000 characters recommended"]
  ],
  "initialValue": "",
  "meta": {
    "annotation": {"include": false, "label": "annotation"},
    "uncertainty": {"include": true, "label": "interpretation confidence"}
  }
}
```

### Property Specifications

#### Required Properties
- **component-namespace** (`string`): Invariably "formik-material-ui" for production deployments
- **component-name** (`string`): "MultipleTextField" – the standardised designation superseding manual configuration
- **type-returned** (`string`): "faims-core::String" maintaining type consistency with single-line variants
- **multiline** (`boolean`): Intrinsically true for MultipleTextField, enabling multi-line behaviour
- **name** (`string`): Unique identifier within the notebook's namespace
- **label** (`string`): Human-readable field designation

#### Optional Properties
- **helperText** (`string`): Contextual guidance supporting comprehensive data entry
- **placeholder** (`string`): Ghosted prompt text indicating expected content depth
- **rows** (`number`): Display height in text rows (default: 4), maintaining fixed dimensions
- **fullWidth** (`boolean`): Horizontal expansion to container boundaries
- **variant** (`string`): Visual presentation – "outlined", "filled", or "standard"

## Validation Rules

### Built-in Validation
- **Type enforcement**: String data type validation through Yup schema
- **No automatic length limits**: Unrestricted by default, constrained only by system resources
- **Whitespace handling**: Preserves formatting with singular exception for whitespace-only input
- **Touched-first paradigm**: Error manifestation contingent upon user interaction

### Configurable Validation
| Rule | Schema | Purpose | Error Message |
|------|--------|---------|---------------|
| required | `["yup.required", "Field is required"]` | Mandates content provision | "Field is required" |
| max length | `["yup.max", 10000, "Exceeds recommended length"]` | Performance optimisation | "Exceeds recommended length" |
| min length | `["yup.min", 50, "Insufficient detail"]` | Ensures substantive content | "Insufficient detail" |
| matches | `["yup.matches", /pattern/, "Format invalid"]` | Structure enforcement | "Format invalid" |

### Validation Examples
```json
{
  "validationSchema": [
    ["yup.string"],
    ["yup.required", "Interpretation required"],
    ["yup.min", 100, "Minimum 100 characters for detailed observation"],
    ["yup.max", 10000, "Consider document attachment for extensive text"]
  ]
}
```

### Error Messages
| Validation State | Visual Presentation | Message Position | Remediation |
|-----------------|---------------------|------------------|-------------|
| Required empty | Red border, red text | Below field | Provide content |
| Length violation | Red border, red text | Below field | Adjust length |
| Pattern mismatch | Red border, red text | Below field | Restructure content |
| Valid state | Standard appearance | None | Proceed |

## Display Behaviour

### Desktop Rendering
- **Element type**: HTML textarea with Material-UI enhancement
- **Height behaviour**: Fixed rows maintaining spatial consistency (default: 4)
- **Overflow handling**: Vertical scrollbar materialises upon content excess
- **Resize capability**: Disabled – users cannot manually adjust field dimensions
- **Width behaviour**: Respects fullWidth parameter, typically spanning container

### Mobile Rendering
#### iOS Behaviour
- **Keyboard presentation**: Standard text keyboard with return key functionality
- **Scrolling mechanism**: Touch-based scrolling within fixed field boundaries
- **Auto-capitalisation**: Sentence capitalisation by default
- **Text selection**: Long-press invokes selection handles
- **Viewport behaviour**: Keyboard emergence may necessitate page scroll

#### Android Behaviour
- **Keyboard type**: Multiline text input with return key
- **Voice input**: Supports extended dictation with paragraph breaks
- **Gesture typing**: Available where keyboard provides
- **Copy/paste**: Full formatting preservation during clipboard operations
- **Scrolling**: Smooth touch scrolling within field confines

### Responsive Considerations
- Field maintains fixed height across viewport transitions
- Internal scrolling accommodates content overflow consistently
- Touch targets preserve accessibility minimums (44×44px)
- Font size maintains 16px minimum, preventing iOS zoom behaviour

## Interaction Patterns

### User Input Methods
- **Direct typing**: Primary mechanism supporting extended composition
- **Voice dictation**: Platform-dependent availability for narrative capture
- **Paste operations**: Complete formatting preservation from external sources
- **Touch scrolling**: Vertical navigation within field boundaries
- **Keyboard navigation**: Tab traversal, arrow keys for cursor positioning

### Content Management
- **Line break handling**: Enter key creates new lines within field
- **Whitespace preservation**: Maintains tabs, indentation, multiple spaces
- **Formatting retention**: Copy-paste operations preserve source formatting
- **Scroll behaviour**: Automatic scroll to cursor during active editing

### State Transitions
- **Pristine**: Untouched field, no validation display
- **Focused**: Active editing state, cursor visible
- **Touched**: Post-interaction, enabling validation display
- **Scrollable**: Scrollbar appears when content exceeds visible area

## Conditional Logic Support

MultilineText fields participate fully in conditional logic systems:

```json
{
  "condition": {
    "operator": "is_not_empty",
    "field": "initial-observation"
  }
}
```

We observe effective deployment as controller fields despite content length:
```json
{
  "condition": {
    "operator": "contains",
    "field": "site-description",
    "value": "disturbed"
  }
}
```

## Data Storage and Export

### Internal Storage
- **Encoding**: UTF-8 string preservation
- **Whitespace fidelity**: Complete preservation except whitespace-only → empty string
- **Character limits**: No explicit constraints; CouchDB document limits apply (~1MB practical)
- **Line ending handling**: Preserves platform-specific line endings without normalisation

### Export Formats
- **CSV**: Escaped with quotes, line breaks preserved within cells
- **JSON**: String with escaped special characters
- **Plain text**: Direct content export with formatting intact
- **Database**: TEXT or LONGTEXT fields accommodate extensive content

### Performance Considerations
- **Recommended maximum**: 10,000 characters for optimal performance
- **No chunking**: Entire content loads simultaneously
- **Memory implications**: Large texts may impact mobile device performance
- **Sync considerations**: Extensive text increases synchronisation payload

## Common Patterns

### Pattern: Detailed Site Interpretation
```json
{
  "site-interpretation": {
    "component-namespace": "formik-material-ui",
    "component-name": "MultipleTextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Site Interpretation",
      "name": "site-interpretation",
      "helperText": "Provide comprehensive interpretative narrative",
      "required": true,
      "multiline": true,
      "fullWidth": true,
      "InputProps": {
        "rows": 6
      }
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.required", "Interpretation required"],
      ["yup.min", 200, "Minimum 200 characters for substantive interpretation"]
    ],
    "initialValue": ""
  }
}
```

### Pattern: Optional Field Notes
```json
{
  "field-notes": {
    "component-namespace": "formik-material-ui",
    "component-name": "MultipleTextField",
    "type-returned": "faims-core::String",
    "component-parameters": {
      "label": "Field Notes (Optional)",
      "name": "field-notes",
      "placeholder": "Additional observations, methodological notes, or contextual information...",
      "multiline": true,
      "InputProps": {
        "rows": 4
      }
    },
    "validationSchema": [
      ["yup.string"],
      ["yup.max", 5000, "Consider attachment for extensive notes"]
    ],
    "initialValue": ""
  }
}
```

## Troubleshooting Guide

### Common Issues

#### Cannot see all text
**Cause**: Fixed height with internal scrolling not immediately apparent  
**Solution**: Scroll within field boundaries; scrollbar appears on hover/focus

#### Whitespace-only input disappears
**Cause**: Intentional conversion of whitespace-only to empty string  
**Solution**: This prevents inadvertent "invisible" content; include actual text

#### Performance degradation with large text
**Cause**: No text chunking or lazy loading implemented  
**Solution**: Maintain content below 10,000 characters; use attachments for extensive documents

#### Line breaks not visible in exports
**Cause**: Export format may not preserve formatting  
**Solution**: Verify CSV reader respects quoted line breaks; use appropriate export format

### Platform-Specific Issues

#### iOS: Keyboard covers field
Ensure viewport meta tags permit appropriate scrolling behaviour

#### Android: Voice input creates run-on text
Platform limitation; manual paragraph breaks may be necessary

#### Desktop: Cannot resize field
By design; fixed dimensions maintain form consistency

### Debug Checklist
- [ ] Component-name is "MultipleTextField" not "TextField"
- [ ] multiline parameter set to true
- [ ] Rows parameter appropriate for content
- [ ] No maxLength preventing input
- [ ] Validation schema permits expected content length
- [ ] InitialValue is empty string, not null

## Implementation Notes

### Technical Architecture
The MultipleTextField represents a specialised registration of the FormikTextField component, pre-configured for multi-line behaviour. This architectural decision – favouring configuration-specific registrations over parameter-based differentiation – enhances Designer integration whilst maintaining implementation consistency. We observe complete adoption of this pattern across production deployments, validating the design philosophy.

### Performance Implications
The absence of dynamic sizing or content chunking reflects a deliberate prioritisation of implementation simplicity over performance optimisation for edge cases. Our empirical observations suggest the 10,000-character recommendation adequately accommodates typical field research narratives whilst maintaining acceptable performance across device categories.

### Whitespace Philosophy
The singular exception for whitespace-only conversion – transforming pure whitespace to empty strings – prevents data quality issues arising from inadvertent space entry whilst preserving all meaningful formatting. This design decision reflects careful consideration of field research realities where formatting conveys semantic information.

## Best Practices

- Configure row count commensurate with expected content volume
- Provide clear helper text indicating expected detail level
- Consider uncertainty metadata for interpretative content
- Implement length validation aligned with performance thresholds
- Document formatting expectations where structure matters
- Test scrolling behaviour on target devices
- Consider attachment fields for genuinely extensive documentation
- Preserve formatting for methodological transparency

## See Also

- **TextField**: Single-line variant for brief content
- **RichText**: Display-only formatted text presentation
- **FileUpload**: Alternative for extensive documentation
- **Select**: Where responses permit standardisation
- **TemplatedStringField**: For structured text generation

---

*The MultilineText field, instantiated through the MultipleTextField component, provides the primary mechanism for capturing extended narrative content within Fieldmark, balancing unlimited expression with pragmatic performance constraints whilst maintaining complete fidelity to researcher intent through comprehensive whitespace preservation.*