# Field Selection Optimization Guide

## Purpose
This document outlines the additional information needed in field documentation to enable intelligent, automated field type selection when converting field protocols, data requirements, or fieldwork manuals into optimized Fieldmark notebooks.

---

## Export & Analysis Considerations {essential}

### TextField vs MultilineText
- **TextField**: Easy CSV analysis, sortable, filterable, suitable for pivot tables
- **MultilineText**: Requires text processing, harder to analyze, may need NLP tools
- **Impact**: Choose TextField when data needs categorization or statistical analysis

### Select vs TextField  
- **Select**: Guaranteed clean data, easy aggregation, consistent vocabulary
- **TextField**: Requires normalization, prone to variants ("site 1" vs "Site 1" vs "Site One")
- **Impact**: Use Select when <20 options, TextField when truly open-ended or list changes frequently

### NumberField vs TextField for Numeric Data
- **NumberField**: Enables calculations, enforces numeric type, prevents data entry errors
- **TextField**: Allows ranges ("5-10"), approximations ("~100"), qualitative additions ("5 (broken)")
- **Impact**: Use NumberField for measurements, TextField for estimates or annotated counts

---

## UX Decision Matrix {essential}

| Scenario | Better Choice | Why |
|----------|--------------|-----|
| "Species name" with known list | Select with 200 options | Prevents typos, ensures consistency |
| "Species name" with evolving list | TextField with autocomplete | List changes frequently, new species likely |
| "Count" of items | NumberField | Enforces numeric, enables calculations |
| "Count" with uncertainty | TextField | Allows ranges ("5-10"), approximations |
| "Color" selection | RadioGroup (<7 options) | All options visible, faster selection |
| "Color" selection | Select (>7 options) | Saves screen space |
| Quick yes/no decisions | Checkbox | Single tap/click |
| Multiple related yes/no | RadioGroup | Shows relationship between options |

---

## Field Selection by Workflow {essential}

### Rapid Data Entry (mobile, standing, field conditions)
- **Prefer**: Radio, Select, Checkbox, TakePhoto, TakePoint
- **Avoid**: MultilineText, lengthy TextField entries
- **Why**: Touch targets easier, minimal typing, works with gloves

### Detailed Documentation (desktop, seated, lab conditions)
- **Prefer**: MultilineText, RichText sections, complex conditionals
- **Acceptable**: Complex validation patterns, multi-field dependencies
- **Why**: Comfortable environment, full keyboard, larger screen

### Batch Processing (repeated similar records)
- **Prefer**: Fields with defaults, TemplatedString for IDs, Select/Radio
- **Avoid**: Required free text without patterns
- **Why**: Reduces repetitive typing, maintains consistency

### Collaborative Entry (multiple users, different expertise)
- **Prefer**: Select with "Other" option, clear helperText
- **Include**: RichText instructions, validation messages
- **Why**: Ensures consistency across users, self-documenting

---

## Data Quality Impact {essential}

### Controlling Data Quality

#### HIGH QUALITY (Controlled vocabulary)
- **RadioGroup**: 2-5 options, always visible, impossible to enter invalid data
- **Select**: 6-20 options, dropdown, controlled but can be lengthy
- **MultiSelect**: Multiple selections from fixed list, no free text
- **Checkbox**: Boolean data, clear yes/no

#### MEDIUM QUALITY (Guided entry)
- **TextField with pattern validation**: Enforces format (e.g., site codes)
- **NumberField with min/max**: Keeps values in reasonable range
- **TemplatedString**: Auto-generated IDs, consistent format
- **Email field**: Format validation built-in

#### LOW QUALITY (Free text, user-dependent)
- **TextField without validation**: Any text allowed
- **MultilineText**: Long-form text, impossible to standardize
- **Address**: Complex JSON, requires post-processing

---

## Common Specification Patterns {essential}

| Specification Says | Consider These Options | Choose Based On |
|-------------------|------------------------|-----------------|
| "Enter [noun]" | TextField, Select | Size of vocabulary, need for consistency |
| "Describe [noun]" | MultilineText, Select + Other field | Expected length, analysis needs |
| "Record [noun]" | TextField, Select, RelatedRecordSelector | Whether it references other data |
| "Count/Number of" | NumberField, Counter, TextField | Precision needs, whether ranges occur |
| "Measure [dimension]" | NumberField | Always, unless units vary |
| "Select all that apply" | MultiSelect, Checkbox group | Number of options (<5 use Checkbox) |
| "Date/Time when" | DateTime, DateField, TextField | Precision needed, relative dates |
| "Location of" | TakePoint, MapField, TextField | GPS availability, precision needs |
| "Photo of" | TakePhoto, FileUpload | Mobile vs desktop, immediate vs later |
| "Identify [object]" | Select, TextField with validation | Vocabulary size, expertise level |
| "Classification" | Hierarchical Select, Radio | Complexity of taxonomy |
| "Notes" or "Comments" | MultilineText | Always, unless character limit needed |
| "ID" or "Identifier" | TemplatedString | Always for auto-generation |
| "Contact" | Email, TextField | Validation importance |

---

## Optimization Rules {essential}

### Core Decision Rules

1. **IF** will_be_analyzed AND <20_options → Select/Radio
2. **IF** mobile_primary AND requires_typing → Minimize text fields
3. **IF** data_consistency_critical → Never use free text
4. **IF** options_change_frequently → TextField with validation
5. **IF** users_are_domain_experts → TextField acceptable
6. **IF** field_protocol_says_"approximately" → TextField not NumberField
7. **IF** comparison_needed_across_records → Use controlled vocabulary
8. **IF** field_used_for_sorting → Avoid MultilineText
9. **IF** GPS_available → TakePoint over TextField for coordinates
10. **IF** offline_operation → Avoid fields requiring external validation

### Performance Optimization Rules

1. **IF** >50 fields → Split into multiple views
2. **IF** >10 conditional fields → Consider separate record types
3. **IF** repetitive_data_entry → Add defaults and templates
4. **IF** slow_network → Minimize photo fields
5. **IF** batch_import_planned → Ensure fields match import format

---

## Real-World Heuristics {comprehensive}

### Rules from Field Experience

- "If >30% of users will enter 'Other', use TextField not Select"
- "If field protocol says 'description', use MultilineText unless it's a classification"
- "If counting things, use NumberField unless ranges/approximations are common"
- "If field will be used for grouping/filtering, never use MultilineText"
- "If users are in a hurry, never require MultilineText"
- "If data entry is in rain/cold, minimize typing"
- "If validation is critical, validate at entry not export"
- "If field is for searching later, use Select not TextField"

### Common Mistakes to Avoid

1. **Using TextField for categories** → Makes analysis difficult
2. **Using MultilineText for structured data** → Parse errors later
3. **Using NumberField for codes** → Leading zeros get lost
4. **Not including "Unknown" option** → Forces false data
5. **Making all fields required** → Blocks partial saves
6. **Using QRCodeFormField on mixed devices** → Desktop users stuck
7. **Over-validating TextField** → Users can't enter edge cases
8. **Under-validating critical IDs** → Duplicates and errors

---

## Domain-Specific Patterns {comprehensive}

### Archaeological Fieldwork
- **"Context number"** → TemplatedString (always, for consistency)
- **"Soil color"** → Select from Munsell chart (standardized)
- **"Coordinates"** → TakePoint (mobile) or two NumberFields (desktop)
- **"Interpretation"** → MultilineText (always, narrative needed)
- **"Finds"** → RelatedRecordSelector (links to finds records)
- **"Phase"** → Select (controlled vocabulary essential)
- **"Dimensions"** → NumberField (calculations needed)

### Ecological Surveys
- **"Species"** → Hierarchical Select (taxonomic structure)
- **"Abundance"** → Select with ranges ("1-10", "11-50", etc.)
- **"GPS location"** → TakePoint (precision critical)
- **"Habitat type"** → RadioGroup (limited options)
- **"Evidence of"** → MultiSelect (multiple indicators)
- **"Transect ID"** → TemplatedString (auto-generated)

### Cultural Heritage
- **"Significance"** → RadioGroup (fixed scale)
- **"Condition"** → Select (standardized terms)
- **"Recommendations"** → MultilineText (narrative)
- **"Photo documentation"** → TakePhoto with required annotation
- **"Owner contact"** → Email field (validation important)

### Laboratory Records
- **"Sample ID"** → TemplatedString with barcode
- **"Weight"** → NumberField with 3 decimal places
- **"Procedure followed"** → Select (SOP list)
- **"Observations"** → MultilineText
- **"Result"** → Depends on test type
- **"QC check"** → Checkbox with conditional fields

---

## Decision Flow for Field Selection {essential}

```
1. What does the specification ask for?
   ↓
2. What is the data type? (text/number/choice/location/media)
   ↓
3. How will it be analyzed? (statistical/categorical/narrative)
   ↓
4. What is the entry context? (field/lab/office)
   ↓
5. Who are the users? (expert/trained/public)
   ↓
6. What is the vocabulary size? (<5/5-20/20-100/>100)
   ↓
7. How important is consistency? (critical/important/nice-to-have)
   ↓
8. Will it change over time? (never/rarely/frequently)
   ↓
9. DECISION → Optimal field type
```

---

## Examples of Optimization Decisions {comprehensive}

### Example 1: "Artifact Material"
- **Specification**: "Record the material of the artifact"
- **Analysis**: Grouping and filtering needed
- **Vocabulary**: ~15 common materials
- **Users**: Trained archaeologists
- **Decision**: **Select field** with standard options + "Other"
- **Why**: Controlled vocabulary ensures consistency, manageable list size

### Example 2: "Site Description"  
- **Specification**: "Describe the site"
- **Analysis**: Qualitative, not structured
- **Expected length**: 2-3 paragraphs
- **Users**: Various expertise levels
- **Decision**: **MultilineText** with 6 rows
- **Why**: Narrative needed, no structure to enforce

### Example 3: "Number of Sherds"
- **Specification**: "Count pottery sherds"
- **Analysis**: Statistical analysis planned
- **Data nature**: Exact counts when <50, estimates when more
- **Decision**: **NumberField** for small counts, **TextField** for large estimates
- **Why**: Enables calculation for precise counts, allows "~200" for estimates

### Example 4: "Find Location"
- **Specification**: "Record where the find was located"
- **Context**: Active excavation
- **Device**: iPad with GPS
- **Precision needed**: Sub-meter
- **Decision**: **TakePoint** with annotation field
- **Why**: GPS available, precision important, annotation adds context

---

## Implementation Priority {essential}

### Must Have for Optimization
1. Vocabulary size guidance
2. Analysis impact documentation  
3. Platform-specific limitations
4. Validation pattern library

### Should Have
1. Domain-specific patterns
2. Performance thresholds
3. UX workflow templates
4. Data quality metrics

### Nice to Have
1. A/B testing results
2. User preference studies
3. Export format examples
4. Integration patterns

---

## Testing the Optimization {comprehensive}

To verify if field selection is optimized, check:

1. **Data Quality Test**: Will this field type prevent common errors?
2. **Analysis Test**: Can I easily analyze/aggregate this data?
3. **User Test**: Is this the fastest/easiest for users to complete?
4. **Platform Test**: Does this work on all target devices?
5. **Scale Test**: Does this work with expected data volume?
6. **Integration Test**: Does this match upstream/downstream systems?
7. **Maintenance Test**: Can non-technical users modify if needed?

---

## Conclusion

With this additional information integrated into field documentation, automated systems can make intelligent decisions that balance:
- Data quality requirements
- User experience optimization
- Analysis and export needs
- Platform constraints
- Domain-specific conventions
- Performance considerations

The key is providing not just "what" each field does, but "when" and "why" to choose it over alternatives.