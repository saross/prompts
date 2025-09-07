# Navigation Index for Bidirectional Links

**Purpose**: Registry of all cross-references and bidirectional links in documentation  
**Created**: 2025-01-07  
**Usage**: Reference for maintaining link integrity across documentation updates

<!-- discovery:metadata

<!-- structured:metadata
meta:purpose: technical-reference
meta:summary: Bidirectional link registry and cross-reference validation checklist.
meta:generates: lookup-tables
meta:requires: [fieldmark-knowledge]
meta:version: 3.0.0
meta:document: navigation_index
meta:depth-tags: [essential]
-->

provides: [bidirectional-links, cross-reference-registry, anchor-inventory]
see-also: [llm-navigation-manifest, field-type-index]
-->

## Bidirectional Link Registry

### Field Type Cross-References

#### Text Fields ← → Related Topics
- **text-fields-v05.md**
  - → field-selection-guide.md (field selection)
  - → platform-reference.md (mobile keyboards)
  - → constraints-reference.md (XSS vulnerabilities)
  - ← designer-component-mapping.md (component names)
  - ← form-structure-guide.md (form examples)

#### Number Fields ← → Related Topics
- **number-fields-v05.md**
  - → platform-reference.md (platform behaviors)
  - → constraints-reference.md (precision limits)
  - → operations-reference.md (migration from deprecated)
  - ← designer-component-mapping.md (component names)
  - ← field-selection-guide.md (numeric decisions)

#### DateTime Fields ← → Related Topics
- **datetime-fields-v05.md**
  - → platform-reference.md (timezone issues)
  - → operations-reference.md (migration guide)
  - → field-selection-guide.md (temporal decisions)
  - ← designer-component-mapping.md (component names)
  - ← dynamic-forms-guide.md (date validation)

#### Selection Fields ← → Related Topics
- **select-choice-fields-v05.md**
  - → field-selection-guide.md (choice matrices)
  - → dynamic-forms-guide.md (conditional logic)
  - → platform-reference.md (touch interfaces)
  - ← designer-component-mapping.md (component names)
  - ← form-structure-guide.md (form examples)

#### Location Fields ← → Related Topics
- **location-fields-v05.md**
  - → platform-reference.md (GPS accuracy)
  - → constraints-reference.md (privacy concerns)
  - → media-fields-v05.md (geotagging)
  - ← designer-component-mapping.md (component names)
  - ← implementation-patterns-guide.md (spatial patterns)

#### Media Fields ← → Related Topics
- **media-fields-v05.md**
  - → platform-reference.md (mobile cameras)
  - → constraints-reference.md (file size limits)
  - → location-fields-v05.md (geotagging)
  - ← designer-component-mapping.md (component names)
  - ← implementation-patterns-guide.md (photo workflows)

#### Relationship Field ← → Related Topics
- **relationship-field-v05.md**
  - → form-structure-guide.md (parent-child forms)
  - → dynamic-forms-guide.md (conditional relationships)
  - → constraints-reference.md (performance limits)
  - ← designer-component-mapping.md (component names)
  - ← field-selection-guide.md (relationship patterns)

#### Display Field ← → Related Topics
- **display-field-v05.md**
  - → text-fields-v05.md (comparison with text)
  - → constraints-reference.md (markdown limitations)
  - ← designer-component-mapping.md (component names)

### Pattern Guide Cross-References

#### Field Selection Guide ← → Related Topics
- **field-selection-guide.md**
  - → All field-categories/*.md (field details)
  - → platform-reference.md (platform constraints)
  - → implementation-patterns-guide.md (patterns)
  - ← form-structure-guide.md (selection context)
  - ← dynamic-forms-guide.md (conditional selection)

#### Form Structure Guide ← → Related Topics
- **form-structure-guide.md**
  - → notebook-format-guide.md (JSON structure)
  - → relationship-field-v05.md (parent-child)
  - → field-selection-guide.md (field choices)
  - ← implementation-patterns-guide.md (structure patterns)
  - ← dynamic-forms-guide.md (multi-section logic)

#### Dynamic Forms Guide ← → Related Topics
- **dynamic-forms-guide.md**
  - → select-choice-fields-v05.md (conditional triggers)
  - → form-structure-guide.md (form sections)
  - → implementation-patterns-guide.md (logic patterns)
  - ← field-selection-guide.md (dynamic selection)
  - ← All field docs (validation examples)

#### Implementation Patterns ← → Related Topics
- **implementation-patterns-guide.md**
  - → field-selection-guide.md (selection patterns)
  - → form-structure-guide.md (structure patterns)
  - → dynamic-forms-guide.md (logic patterns)
  - ← All field docs (implementation examples)
  - ← constraints-reference.md (workarounds)

### Reference Document Cross-References

#### Designer Component Mapping ← → Related Topics
- **designer-component-mapping.md**
  - → All field-categories/*.md (provides mappings for)
  - → component-reference.md (technical details)
  - → notebook-format-guide.md (JSON usage)
  - ← All documents (primary reference)

#### Component Reference ← → Related Topics
- **component-reference.md**
  - → designer-component-mapping.md (mapping context)
  - → All field-categories/*.md (component details)
  - ← notebook-format-guide.md (component usage)
  - ← constraints-reference.md (component limits)

#### Constraints Reference ← → Related Topics
- **constraints-reference.md**
  - → platform-reference.md (platform limits)
  - → operations-reference.md (migration issues)
  - → All field docs (field constraints)
  - ← implementation-patterns-guide.md (workarounds)

#### Operations Reference ← → Related Topics
- **operations-reference.md**
  - → constraints-reference.md (limitation context)
  - → platform-reference.md (platform ops)
  - → All field docs (migration paths)
  - ← troubleshooting-index.md (when created)

#### Platform Reference ← → Related Topics
- **platform-reference.md**
  - → location-fields-v05.md (GPS issues)
  - → media-fields-v05.md (camera issues)
  - → All field docs (platform behaviors)
  - ← constraints-reference.md (platform limits)

#### Notebook Format Guide ← → Related Topics
- **notebook-format-guide.md**
  - → designer-component-mapping.md (component usage)
  - → form-structure-guide.md (structure patterns)
  - ← notebook-templates.md (when created)
  - ← All field docs (JSON examples)

## Anchor Inventory

### Primary Section Anchors

#### Field Documentation Anchors
- `#text-input-fields` - Text field documentation
- `#selection-fields` - Selection field documentation
- `#datetime-fields` - DateTime field documentation
- `#number-fields` - Number field documentation
- `#display-fields` - Display field documentation
- `#location-fields` - Location field documentation
- `#media-fields` - Media field documentation
- `#relationship-fields` - Relationship field documentation

#### Pattern Guide Anchors
- `#field-selection-guide` - Selection guidance
- `#form-structure-guide` - Form structure
- `#dynamic-forms-guide` - Dynamic forms
- `#implementation-patterns-guide` - Implementation patterns

#### Reference Document Anchors
- `#designer-component-mapping` - Component mappings
- `#component-reference` - Component details
- `#constraints-reference` - Constraints
- `#operations-reference` - Operations
- `#platform-reference` - Platform specifics
- `#notebook-format-guide` - Notebook format

### Common Sub-Section Anchors

#### Standard Field Sections
- `#overview` - Field overview
- `#designer-quick-guide` - Designer usage
- `#configuration` - Configuration details
- `#validation` - Validation rules
- `#json-examples` - JSON examples
- `#common-issues` - Common problems
- `#platform-notes` - Platform specifics

#### Pattern Guide Sections
- `#core-principles` - Design principles
- `#decision-matrix` - Decision matrices
- `#use-cases` - Use case examples
- `#anti-patterns` - What to avoid
- `#best-practices` - Recommended approaches

## Link Validation Checklist

### Pre-Build Validation
- [ ] All XREF placeholders replaced
- [ ] All relative paths updated
- [ ] All anchors unique
- [ ] All cross-references bidirectional

### Post-Build Validation
- [ ] All internal links resolve
- [ ] No broken anchors
- [ ] Navigation flows both ways
- [ ] Discovery metadata present

## Maintenance Notes

### When Adding New Documents
1. Add to this navigation index
2. Update llm-navigation-manifest.md
3. Add discovery metadata to new file
4. Update all related bidirectional links
5. Add to build-reference.sh if needed

### When Removing Documents
1. Remove from this index
2. Update llm-navigation-manifest.md
3. Fix all broken links in related docs
4. Update build-reference.sh

### When Renaming Sections
1. Update anchor in source document
2. Update all references in this index
3. Search and replace old anchor globally
4. Test navigation after rebuild

---

*This index maintains the integrity of cross-references throughout the documentation system.*