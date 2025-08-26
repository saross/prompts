Please complete the following end-of-field checklist, executing all specified actions:

## Required Actions

### 1. Generate Session Completion Report
Produce a structured session summary following the template below, calculating all metrics:

**Date/Time**: [Current timestamp]
**Field Completed**: [Field name] - third draft

#### Session Status
- [✅] Documentation saved to artifact
- [✅] No truncation or context issues
- [✅] All Q&A incorporated
- [✅] Ready for production use

### 2. Quality Assurance Verification
Confirm all template sections (minimum 13) are present and complete:
- [ ] All required template sections included with [N] sections present
- [ ] Validation table with [N] types documented
- [ ] Platform behaviours (Desktop/iOS/Android) specified
- [ ] JSON examples ([N] provided, target: 3-4)
- [ ] Troubleshooting guide ([N] issues, target: 5-8)
- [ ] Cross-references ([N] added, target: 5+)
- [ ] Heritage context examples included

### 3. Document Technical Discoveries
Summarise critical findings in structured categories:
- **Architectural Behaviours**: [Key operational patterns]
- **Implementation Constraints**: [Technical limitations]
- **Platform-Specific Issues**: [Cross-platform considerations]
- **Performance Implications**: [Efficiency concerns]
- **Unresolved Ambiguities**: [Questions requiring future investigation]

### 4. Create Bug Reports and Feature Requests Artifact
For bugs or missing features, generate a markdown artifact titled "BugReports_FeatureRequests_[FieldName]" containing:
- Bug reports with severity ratings (Critical/High/Medium/Low)
- Feature requests with priority levels
- Each item numbered with prefix (BUG-[FIELD]-NNN or FEAT-[FIELD]-NNN)
- [✅] Bug report and feature requests created (confirm to user)

### 5. Update Field Documentation Progress Matrix
Load the Field Documentation Progress Matrix from project knowledge and update it with:
- Mark field as COMPLETE in Third Draft column
- Recalculate completion percentage
- Add technical discoveries to log section
- Update session handover box with next field details
- Modify package status if applicable
- [✅] Field Documentation Progress Matrix updated (confirm to user)

## Related Field Handover Preparation
**If one or more functionally related fields identified**, list them: '[Nextfield(s)] identified as functionally related to [CurrentField]' and complete this section.
**If no functionally related fields identified**, state 'No related fields requiring handover preparation' and skip this section. 

### Architectural Findings
**Component relationship**: [Shared component | Distinct components | Unknown]  
**If shared**: Configuration parameters that differ  
**If distinct**: Behavioural overlap despite separation

### Reusability Map
**Sections to inherit verbatim**: [List section names only]  
**Sections requiring complete rewrite**: [List with one-line rationale]  
Example: "Validation Rules – different error message framework"

### Critical Warnings
**False similarities**: [Specific behaviours that appear identical but aren't]  
**Hidden dependencies**: [Discovered requirements not obvious from interface]  
Example: "Camera permission cascade differs from file selection despite identical UI"

### Documentation Strategy Recommendation
Based on the completed analysis of [CurrentField], recommend approach for [NextField]:
- **Independent documentation with aggressive cross-referencing** (default for moderate overlap)
- **Differential documentation** (document only divergences, reference [CurrentField] for shared behaviours)
- **Unified revision required** (overlap suggests both fields need consolidated documentation)
- **Architectural investigation required** (relationship remains ambiguous despite documentation effort)
  
## Output Requirements (Sequential)
*In case of failures, document failure reason and pause for instructions.*
1. Present session completion report (including handover if applicable)
2. Create bug/feature artifact 
3. Update matrix document with single write operation
4. Confirm: "All [N] actions completed successfully"

## Automation Instructions
- Calculate all percentages automatically
- Extract technical discoveries from Q&A exchanges
- Generate sequential bug/feature numbering starting from BUG-[CurrentField]-001