# Field Documentation Discovery Protocol

## Primary Objective
Prepare for third-draft production of upstream LLM-first documentation that enables:
- **Downstream Output A**: Human-facing user/creator documentation at various depth levels
- **Downstream Output B**: Precise guidance for Claude Code when constructing JSON notebook definitions

Success requires meeting ALL concrete criteria:
- All validation rules identified and understood
- All platform behaviours documented or confirmed absent
- All error messages and feedback mechanisms specified
- All default values and data constraints defined (JSON)
- All default values and configuration constraints identified (Designer web app GUI)
- All inter-field dependencies and related fields mapped

## Session Context
**Target Field**: [FieldName]  
**Package**: [A/B/C/D/E/F] - [Package Description]

## Resource Loading Instructions
Search project knowledge for the following resources:

1. **Second-draft documentation**: 
   - Primary search: Documents containing "Detailed Documentation" AND "[FieldName]"
   - Expected pattern: "[FieldName] Fields - Detailed Documentation.md"
   - **Fallback**: If not found, list ALL documents containing "[FieldName]" and select most relevant
   
2. **Template specification**: Load "Field Documentation Progress Matrix" 
   - Extract the 13-section template structure from this document
   - Note completion status for [FieldName]
   
3. **Standards reference**: Load "Phase 1 Focus" document
   - Identify LLM-first documentation requirements
   
4. **Completed examples**: 
   - Primary search: Documents containing "third draft" OR "third-draft"
   - **Fallback**: Search for "[FieldName]" AND ("final" OR "complete" OR "v3")
   - Prioritise fields from same package or field type category or with similar validation patterns

**CRITICAL**: For each resource category, either:
- Confirm exact document loaded with full title, OR
- List available candidates and justify selection, OR
- Explicitly state "No matching documents found"

Do not proceed without the 13-section template from the Progress Matrix.

## Resource Loading Confirmation
Present loaded resources in this format:

### Loaded Documents Manifest
```
1. SECOND DRAFT: [Exact filename as loaded]
   - Status: ✓ Confirmed / ⚠ Alternative selected / ✗ Not found
   - Rationale: [If alternative selected, explain why]

2. TEMPLATE: [Exact filename]
   - Status: ✓ Confirmed
   - Sections found: [List if successfully extracted]

3. STANDARDS: [Exact filename]
   - Status: ✓ Confirmed / ✗ Not found

4. EXAMPLES: 
   - [Filename 1] (Package X, Field Type)
   - [Filename 2] (Package Y, Field Type)
   - Status: ✓ Loaded N examples / ⚠ Limited examples / ✗ None found
```

### Validation Checkpoint
Before proceeding to gap analysis:
- Confirm: "All critical resources loaded. Ready to analyse."
- OR state: "Missing [resource type]. Proceeding with limitations: [specify impact]"

**STOP**: Await confirmation that correct documents have been loaded before analysis.

## Related Field Analysis
Claude Code or prior documentation indicates functional relationships with other fields including: [Fieldname(s)]

[PLACEHOLDER: Insert pre-filled related field analysis from end-of-field checklist here]

## Gap Analysis & Intelligence Gathering
Once resources loaded, analyse the second-draft documentation:

### Section Completeness Audit
Against the 13-section template, identify:
- Missing sections (not present at all)
- Skeletal sections (<50 words where more detail expected)
- Sections lacking technical specificity

### Technical Ambiguity Assessment
Document uncertainties regarding:
- Validation rules and edge cases
- Platform-specific behaviours (web/iOS/Android)
- Error handling and user feedback mechanisms
- Functional relationships with other fields or components
- Data type constraints and transformations

### Information Sufficiency Rating
Estimate current documentation completeness: [X]%
List specific information gaps preventing 100% rating.

## Documented Knowledge Inventory
Before generating questions, explicitly catalogue information already present in second-draft:

### Already Documented
- **Validation rules specified**: [List actual rules found]
- **Platform behaviours described**: [Quote relevant sections]
- **Error messages defined**: [List messages documented]
- **Configuration options detailed**: [Enumerate parameters]
- **Integration points identified**: [List relationships mentioned]

### Confirmed Gaps
Only generate questions for information explicitly absent from the above inventory.

## Strategic Question Synthesis
Generate 10–20 consolidated questions targeting **ONLY** information gaps not addressed in second-draft documentation. Before formulating each question, verify it cannot be answered from the loaded documentation.

**Critical filter**: If the second draft contains even partial information about a topic, incorporate that knowledge into the question rather than asking from scratch. Example: Instead of "What validation rules apply?" ask "The documentation mentions min/max validation—are there other validation types?"

Prioritise questions that:
- Resolve ambiguities blocking documentation production
- Clarify behavioural variations affecting user experience  
- Identify undocumented constraints or dependencies
- Expose platform-specific implementation divergences

Structure questions within these domains (2–5 questions per category):
### Core Functionality & Configuration
### Validation & Error Handling  
### Platform-Specific Behaviours
### Architectural Relationships

Consolidation example: "How does validation cascade when (a) initial vs runtime, (b) with dependent fields present, and (c) across platform implementations?"

**Constraint**: Limit to maximum 20 questions. Quality and precision supersede quantity.

**Output format**: Number all questions sequentially. 

## Handover Package
Conclude with:
- Total question count
- Estimated completeness without answers: [X]%
- Estimated completeness with all answers: [Y]%
- Ready for answer collection phase: YES/NO

---
*End of Discovery Phase. Copy question list to Production Prompt after collecting answers.*