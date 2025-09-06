# Field Documentation Production Protocol

## Primary Objective
Generate third-draft upstream LLM-first documentation enabling:
- **Downstream Output A**: Human-facing user/creator documentation at various depth levels
- **Downstream Output B**: Precise guidance for Claude Code when constructing JSON notebook definitions

## Prerequisites
Confirm completion of Discovery Phase:
- [ ] Second-draft documentation reviewed (confirmed via title containing keywords)
- [ ] 13-section template loaded from Progress Matrix
- [ ] Gap analysis complete
- [ ] All clarification questions answered
- [ ] Meeting ALL concrete criteria:
  - All validation rules understood
  - All platform behaviours documented
  - All error messages specified
  - All default values defined
  - All inter-field dependencies mapped

## Answer Collection Protocol
**CRITICAL**: Request answers in THEMATIC CLUSTERS to maintain conceptual coherence whilst optimising investigation efficiency.

Format for each exchange:
1. State: "Please investigate Cluster [A/B/C/D]: [cluster theme]" followed by the constituent questions
2. Wait for consolidated response addressing interrelated concerns
3. Acknowledge receipt: "Understood. [Synthesis of key findings]"
4. Proceed to next cluster

**Cluster A**: Configuration and Parameters (Designer interface, parameter support)  
**Cluster B**: Platform Behaviours and Permissions (Camera access, platform variations)  
**Cluster C**: Technical Implementation (EXIF, storage, validation, processing)  
**Cluster D**: Operational Boundaries (Offline behaviour, export, performance, architecture)

Continue until all questions answered, then state: "All clarifications collected. Preparing blueprint."

## Blueprint Generation
Create structured documentation outline (max 200 words):

### Structure
- List all 13 sections with 1-line description of planned content
- Highlight sections requiring most expansion from second draft
- Note any sections where information remains uncertain

### Key Enhancements
- Technical clarifications to be added
- Platform-specific details to document
- Validation rules to specify
- Error scenarios to cover

**STOP**: Present blueprint and await explicit approval before proceeding.

## Documentation Production
Upon receiving approval (e.g., "approved", "proceed", "yes"):

### Apply Template Structure
Generate all 13 sections as specified in Progress Matrix, ensuring:
- Technical precision for LLM consumption
- Sufficient detail for downstream generation
- Clear behavioural specifications

### Required Elements
1. **JSON Examples** (3-4 minimum):
   - Basic usage
   - Advanced configuration
   - Edge case handling
   - Platform-specific variant (if applicable)

2. **Validation Table**:
   - Rule | Condition | Error Message | Platform Impact
   - Include all discovered constraints

3. **Troubleshooting Guide**:
   - Common issues with solutions
   - Debug checklist
   - Platform-specific gotchas

4. **Heritage Examples**:
   - Historical usage patterns (if found in project knowledge)
   - Migration notes from older versions

5. **Cross-References & Dependencies**:
   - **Required companions**: Fields that must be present
   - **Common pairings**: Fields typically used together
   - **Mutual exclusions**: Fields that conflict
   - **Validation cascades**: How this field's validation affects others
   - **Dependent fields**: Fields that rely on this field's value
   - Include specific field names and explain the relationship nature

### Style Requirements
- Match tone and structure of completed third-draft examples
- Prioritise technical accuracy over readability
- Include explicit null/undefined handling
- Document all default values

## Quality Assurance Checklist
Self-verify before submission:
- [ ] All 13 template sections present and complete
- [ ] Minimum 3 JSON examples with inline behaviour notes
- [ ] Validation table populated with all rules
- [ ] Platform differences explicitly documented
- [ ] Error messages specified for all validation failures
- [ ] Troubleshooting guide includes debug steps
- [ ] Cross-references to related fields included
- [ ] Technical discoveries from Q&A integrated
- [ ] Suitable for automated downstream generation

## Final Output Format
Present as single markdown artifact titled:
"[FieldName] Field - Third Draft Documentation"

---
*End of Production Phase. Documentation ready for downstream processing.*