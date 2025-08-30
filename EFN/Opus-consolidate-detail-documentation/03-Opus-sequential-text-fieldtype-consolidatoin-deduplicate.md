# Prompt 3: Deduplicate the [7]-Field Document

Take the merged document with [SHARED]/[VARIANT] tags and reorganize to remove redundancy while preserving ALL information.

## CORE DIRECTIVE
Deduplication = MOVING content to shared sections, never DELETING. Every piece of information must remain accessible.

## Instructions

### Step 1: Process Shared Content Markers

Review all [SHARED-START] and [SHARED-END] pairs:
- Content between SHARED-START markers goes to Common Characteristics
- Content at SHARED-END locations becomes a reference
- Preserve field-specific details within moved content

Review all [VARIANT] markers:
- Move to Common Characteristics with clear field attribution
- Create comparison table if multiple variants exist
- Note implementation differences explicitly

### Step 2: Organize Common Sections

**Common Characteristics** subsections:
- Shared Limitations (note which fields affected)
- Common Validation Patterns (preserve field variations)
- Platform Behaviors (maintain field-specific columns)
- Performance Boundaries (list per field)
- Security Considerations (note field-specific risks)

Format shared content as:
```
**Topic Name** [affects: Field1, Field2, Field3]
Common behavior description...
- Field1: specific detail
- Field2: specific detail
- Field3: uses default
```

### Step 3: Create References

Replace moved content with precise references:
- At SHARED-END locations: `See [Common Characteristics > Topic Name]`
- For variants: `See [Common Characteristics > Topic Name > Field Variant]`
- Include differentiator if needed: `(this field: 50 char limit)`

### Step 4: Handle Complex Cases

**Similar but Different Content**:
- Threshold test: >70% identical = move to common
- <70% identical = keep separate
- Edge cases = keep both, cross-reference

**Variant Handling**:
- 2 variants: Show side-by-side comparison
- 3+ variants: Create comparison table
- Implementation differences: Preserve all details

## Verification Checklist

**Marker Resolution**:
- [ ] All [SHARED-START/END] pairs processed
- [ ] All [VARIANT] tags addressed
- [ ] References created for all moved content

**Content Preservation** (counts must match):
- Total warnings: ___ before = ___ after
- Total JSON examples: ___ before = ___ after  
- Total validation rules: ___ before = ___ after
- Total troubleshooting items: ___ before = ___ after

**Structure Validation**:
- [ ] Common Characteristics expanded with subsections
- [ ] Individual sections contain unique content only
- [ ] All references use [Section > Subsection] format
- [ ] Variant differences explicitly documented

## Example Transformation

**BEFORE**:
```
[NumberInput section]
[SHARED-START: validation-timing]
Validation only displays after field is "touched" (focused then blurred)
[SHARED-END: validation-timing]

[ControlledNumber section]  
[SHARED-END: validation-timing - see above]
```

**AFTER Common Characteristics**:
```
### Validation Behavior [affects: NumberInput, ControlledNumber]
Validation only displays after field is "touched" (focused then blurred)
```

**AFTER Individual Sections**:
```
[NumberInput section]
Validation: See [Common Characteristics > Validation Behavior]

[ControlledNumber section]
Validation: See [Common Characteristics > Validation Behavior]
```

## Variant Example

**BEFORE**:
```
[VARIANT-NumberInput]: Accepts any numeric value
[VARIANT-ControlledNumber]: Requires min/max constraints
```

**AFTER Common Characteristics**:
```
### Numeric Constraints
| Field | Constraint Requirement | Default Behavior |
|-------|----------------------|------------------|
| NumberInput | Optional | Accepts any numeric value |
| ControlledNumber | Required | Must define min/max range |
```

## DO NOT
- ❌ Delete any information
- ❌ Merge truly different behaviors
- ❌ Create ambiguous references
- ❌ Lose field-specific details
- ❌ Combine different error messages

## Final Validation
Can you trace every piece of information from the original documents to its location in the deduplicated version?

Output the deduplicated document with ALL information preserved in optimized organization.