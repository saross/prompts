# LLM Documentation Assessment Prompt Template

## Purpose
This prompt template enables systematic assessment of the Fieldmark documentation's LLM optimization quality, coverage, and effectiveness. Use this with Claude or other LLMs to generate consistent assessment reports after major documentation updates.

---

## Assessment Prompt

Please perform a comprehensive LLM optimization assessment of the Fieldmark documentation located at `/production/reference.md`. Generate a detailed report following the structure and criteria below.

### 1. Document Statistics Analysis
Analyze and report on:
```
- Total line count of reference.md
- File size in MB
- Number of documents included
- Number of sections/categories
- Growth/change from previous assessment (if applicable)
```

Use these commands:
- `wc -l reference.md` for line count
- `du -h reference.md` for file size
- Count documents in each category directory

### 2. LLM Optimization Scoring (100-point scale)

Evaluate each category and provide a score with justification:

| Category | Weight | Assessment Criteria |
|----------|--------|-------------------|
| **Navigation** (15%) | Document discoverability, manifest quality, index completeness |
| **Templates** (15%) | Parametric generation capability, template markers, cookbook recipes |
| **Troubleshooting** (15%) | Error coverage percentage, solution quality, diagnostic tools |
| **Metadata** (10%) | Structured metadata presence, summary tags, discovery tags |
| **Glossary** (10%) | Term coverage, consistency, cross-references |
| **Examples** (10%) | JSON examples, code snippets, practical demonstrations |
| **Cross-references** (10%) | Link integrity, bidirectional references, navigation paths |
| **Size Optimization** (5%) | Within target limits, appropriate verbosity |
| **Coverage** (10%) | Completeness of documentation, gap analysis |

Calculate overall score: Sum of (Category Score × Weight)

### 3. Content Coverage Audit

Verify presence and quality of:

#### Core Documentation
- [ ] Field category documents (8 expected)
- [ ] Dashboard interface documents (7 expected)
- [ ] Pattern guides (6 expected)
- [ ] Technical references (14+ expected)
- [ ] Advanced features (1+ expected)

#### Supporting Materials
- [ ] Working notebook templates
- [ ] Automation examples
- [ ] Troubleshooting index
- [ ] Navigation manifest
- [ ] Glossary

### 4. Key Metrics Comparison

Create comparison table if previous assessment exists:

| Metric | Previous | Current | Change | Status |
|--------|----------|---------|--------|--------|
| Total Lines | X | Y | +/-% | ✅/⚠️ |
| File Size | X MB | Y MB | +/-% | ✅/⚠️ |
| Documents | X | Y | +/- | ✅/⚠️ |
| Template Markers | X | Y | +/- | ✅/⚠️ |
| Glossary Terms | X | Y | +/- | ✅/⚠️ |
| Error Coverage | X% | Y% | +/-% | ✅/⚠️ |

### 5. Quality Validation Checks

Perform these validation tests:

#### Cross-Reference Integrity
```bash
# Check for broken XREF placeholders
grep -n "XREF" reference.md

# Check for broken links
grep -o "\[.*\]([^)]*)" reference.md | grep -v "http"
```

#### Metadata Completeness
```bash
# Check for structured metadata
grep -c "structured:metadata" reference.md

# Check for discovery metadata
grep -c "discovery:metadata" reference.md
```

#### Template Marker Coverage
```bash
# Count template markers
grep -c "{{.*}}" reference.md
```

### 6. Gap Analysis

Identify and list:
- Missing documentation areas
- Incomplete sections
- Outdated information
- Integration gaps
- User journey gaps

### 7. LLM Usability Assessment

Evaluate from an LLM's perspective:
- **Information Density**: Is information appropriately chunked?
- **Context Windows**: Will it fit in typical LLM context limits?
- **Semantic Structure**: Can meaning be extracted efficiently?
- **Generation Readiness**: Can parametric generation occur smoothly?
- **Query Answerability**: Can common questions be answered directly?

### 8. Human Usability Assessment

Evaluate from a human developer's perspective:
- **Navigation Ease**: Can users find information quickly?
- **Learning Path**: Is there a clear progression?
- **Practical Examples**: Are there enough real-world examples?
- **Troubleshooting**: Can errors be resolved independently?

### 9. Recommendations

Provide prioritized recommendations:

#### Immediate Actions (Priority 1)
- Critical fixes needed
- Broken elements to repair
- Missing essential content

#### Short-term Improvements (Priority 2)
- Enhancement opportunities
- Coverage gaps to fill
- Quality improvements

#### Long-term Enhancements (Priority 3)
- Nice-to-have additions
- Future feature documentation
- Advanced integrations

### 10. Executive Summary

Synthesize findings into:
- **Overall Score**: X/100
- **Key Strengths**: Top 3-5 strengths
- **Critical Gaps**: Top 3-5 gaps
- **Impact Assessment**: Value delivered by documentation
- **Comparison**: Better/worse than previous assessment and why

---

## Report Format

Generate the report as a markdown document with:
- Clear heading structure
- Data tables for metrics
- Checkboxes for validation items
- Color coding (✅ good, ⚠️ warning, ❌ problem)
- Specific line numbers and file references
- Actionable recommendations

Save the report as: `LLM-OPTIMIZATION-ASSESSMENT-[DATE].md`

---

## Usage Instructions

1. **Preparation**
   - Ensure reference.md is freshly built
   - Have previous assessment reports available
   - Note any recent major changes

2. **Execution**
   ```bash
   # First, rebuild reference.md
   ./scripts/build-reference.sh
   
   # Then run this assessment prompt with Claude
   ```

3. **Follow-up**
   - Compare with previous assessments
   - Create action items from recommendations
   - Update FUTURE-TASKS.md with findings
   - Schedule next assessment

---

## Assessment Frequency

Perform assessments:
- After major documentation additions (>10% growth)
- Before major releases
- Quarterly for maintenance
- After structural reorganization
- When LLM usage patterns change

---

*This prompt template version: 1.0*  
*Created: 2025-01-10*  
*For use with: Claude 3.5+ or equivalent LLM*