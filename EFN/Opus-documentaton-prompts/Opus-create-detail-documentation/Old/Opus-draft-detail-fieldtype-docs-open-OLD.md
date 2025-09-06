Hi Opus,

Continuing Phase 1 field documentation (third-draft production), 'upstream' LLM-first documentation enabling construction of 'downstream' artefacts including (a) human-facing user/creator documentation at various depth levels; (b) guidance for Claude Code when constructing JSON files to define notebooks. Execute the following startup sequence:

## 1. Previous Session Handover
### Technical Questions from Prior Analysis
[Questions identified during previous field documentation]
- Decimal precision handling and rounding behaviour?
- Negative number support and range constraints?
- Scientific notation acceptance and display?
- Increment/decrement buttons on mobile platforms?
- Locale-specific formatting (thousands separators)?

### Discovered Constraints & Patterns
[Technical limitations and successful patterns from recent work]
- Platform detection unavailable (_PLATFORM variable absent)
- Required validation can break cross-platform compatibility
- Validation tables must specify platform impact column
- Always document workarounds for missing functionality

### Related Field Insights
[Relevant discoveries from similar components]
- NumberField may share validation patterns with TextField
- Mobile keyboard configuration critical for user experience
- Consider pairing strategies similar to QRCodeFormField/TextField

## 2. Load Critical Resources
Search project knowledge for and confirm loading of:
- Second-draft documenation related to the field [specify most relevant, named using the pattern: 'XXX Fields - Detailed Documentation.md', e.g., 'Text Fields - Detailed Documehntation.md']
- Field Documentation Progress Matrix (for status & checklist)
- Phase 1 Focus document (for standards)
- Completed field examples [most relevant completed fields]

## 3. Session Context
**Date/Time**: [YYYY-MM-DD HH:MM]
**Target Field**: [FieldName]
**Package**: [A/B/C/D/E/F] - [Package Description]

## 4. Automated Status Retrieval
From the loaded Progress Matrix, extract and confirm:
- Current completion: [N]/25 fields ([X]%)
- Package status: [X of Y fields in package complete]
- Previous session end time and handover notes
- Documented questions for this field

## 5. Field Intelligence Brief
Review second-draft documentation and identify:
- Template compliance gaps (sections missing or incomplete)
- Technical ambiguities requiring clarification
- Platform-specific behaviours needing investigation
- Validation and error handling uncertainties

## 6. Execution Protocol
### Phase 1: Gap Analysis (10 minutes)
- Compare second draft against 13-section template
- Generate prioritised question list
- Estimate information sufficiency percentage

### Phase 2: Clarification Loop (20-30 minutes)
- Ask technical questions **one-by-one** for comprehension
- No arbitrary limit on the number of questions
- Target >95% confidence threshold

### Phase 3: Blueprint Generation (5 minutes)
- Produce structured outline (max 200 words)
- Await approval before proceeding
 
### Phase 4: Documentation Production (30-40 minutes)
- Generate complete third-draft documentation
- Apply style consistency from completed examples
- Ensure heritage context integration

### Phase 5: Quality Assurance (10 minutes)
- Verify all 13 template sections
- Confirm 3-4 JSON examples with behaviours
- Check cross-references and troubleshooting guide
- Document technical discoveries

## 7. Success Criteria
- [ ] All template sections complete
- [ ] Validation table populated
- [ ] Platform behaviours documented
- [ ] 3-4 JSON examples included
- [ ] Troubleshooting guide with debug checklist
- [ ] Technical discoveries logged
- [ ] Heritage examples integrated
- [ ] Documentation optimised for LLM-first workflows
- [ ] Documentation can be used to generate human-readable guides and references
- [ ] Documentation can be used to generate instructions and guidelines for Claude Code when creating notebook JSON

## 8. Context Management
- Monitor response length and complexity
- If approaching limits, complete current section and create handover
- Prioritise completeness over starting new sections

Confirm resource loading complete and ready to proceed with [FieldName] analysis.