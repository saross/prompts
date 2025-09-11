# Documentation Generation Prompts

This folder contains reusable prompt templates for generating and maintaining Fieldmark documentation with Claude or other LLMs.

## Available Prompts

### 1. LLM Assessment Prompt (`llm-assessment-prompt.md`)
**Purpose**: Systematically assess the LLM optimization quality of the documentation  
**Use When**: After major documentation updates (>10% growth) or quarterly reviews  
**Output**: Detailed assessment report with scoring and recommendations

### 2. Quickstart Generation Prompt (`quickstart-generation-prompt.md`)
**Purpose**: Generate or update the "Your First Notebook in 15 Minutes" guide  
**Use When**: UI changes, field updates, or major feature additions  
**Output**: Complete quickstart guide maintaining consistent structure and tone

## How to Use These Prompts

### General Usage Pattern

1. **Load the reference documentation**
   ```
   "Please load /production/reference.md for context"
   ```

2. **Load the specific prompt template**
   ```
   "Using the prompt at /production/prompts/[prompt-name].md, please [generate/assess]..."
   ```

3. **Specify the output location**
   ```
   "Save the output to /production/[appropriate-location]"
   ```

### Specific Examples

#### Running an LLM Assessment

```
"Please perform an LLM optimization assessment of the current documentation 
using the prompt template at /production/prompts/llm-assessment-prompt.md. 
Compare with the previous assessment in llm-optimization-session2-report.md 
and save the new report as llm-optimization-assessment-[DATE].md"
```

Expected output:
- Comprehensive scoring report (100-point scale)
- Metrics comparison with previous assessment
- Gap analysis and recommendations
- Typically 400-500 lines

#### Regenerating the Quickstart Guide

```
"Please regenerate the quickstart guide using the prompt template at 
/production/prompts/quickstart-generation-prompt.md. Pull current field 
information from reference.md and save to 
/production/human-facing/quickstart-notebook-creators.md"
```

Expected output:
- 400-450 line quickstart guide
- 15-minute completion timeline
- Consistent friendly tone
- Current technical accuracy

#### Updating Part of a Document

```
"Using the structure defined in /production/prompts/quickstart-generation-prompt.md, 
please update only Step 3 (Add Your Fields) in the existing quickstart guide 
to reflect the new field types"
```

## When to Use Prompts vs Direct Editing

### Use Prompt Templates When:
- **Major changes**: >5 UI elements changed
- **Systematic updates**: Field naming conventions change
- **Complete regeneration**: Starting fresh for new version
- **Consistency critical**: Multiple documents need same updates
- **Assessment needed**: Quarterly quality reviews

### Use Direct Editing When:
- **Minor fixes**: 1-2 typos or terms
- **Small additions**: Single troubleshooting item
- **Quick corrections**: One field name update
- **Wording tweaks**: Improving clarity without structural change

## Creating New Prompt Templates

When creating a new prompt template, include:

1. **Purpose Statement**: Clear description of what the prompt generates
2. **Structure Requirements**: Detailed outline of required sections
3. **Technical Specifications**: Where to pull accurate information
4. **Style Guidelines**: Tone, voice, and formatting rules
5. **Quality Checks**: Validation criteria for output
6. **Usage Instructions**: How and when to use the prompt

### Template Structure

```markdown
# [Document Type] Generation Prompt

## Purpose
[What this prompt generates and why]

## Generation Prompt
[The actual prompt to give to the LLM]

### Document Structure Requirements
[Detailed requirements]

### Technical Accuracy Requirements
[Where to get correct information]

### Style Guidelines
[Tone, voice, formatting]

## Usage Instructions
[How to use this prompt]

## Example Output
[Sample of expected output]
```

## Maintenance

### Updating Prompt Templates

When Fieldmark UI or features change:

1. **Update the prompt template** to reflect new requirements
2. **Document the changes** in the prompt's version notes
3. **Test the prompt** by generating sample output
4. **Commit with clear message** about what changed

### Version Control

Each prompt template should include:
- Version number
- Creation date
- Last updated date
- What changed in updates

## Benefits of Using These Prompts

1. **Consistency**: Same structure and quality across regenerations
2. **Completeness**: All required elements included automatically
3. **Efficiency**: Faster than manual rewriting
4. **Accuracy**: Pulls from authoritative sources
5. **Maintainability**: Easy to update templates when requirements change
6. **Documentation**: Templates themselves document requirements

## Tips for Best Results

1. **Always load reference.md first** - This ensures technical accuracy
2. **Specify the output format** - Markdown with specific heading levels
3. **Request validation** - Ask the LLM to verify against requirements
4. **Review output** - Always human-review generated content
5. **Test procedures** - Verify that generated guides actually work

## Future Prompt Templates

Consider creating templates for:
- API documentation generation
- Troubleshooting guide updates
- Field documentation updates
- Dashboard documentation updates
- Migration guide generation

---

*Last Updated: 2025-01-10*  
*Prompts Folder Version: 1.0*