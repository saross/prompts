# Prompt Restructuring Analysis
## For Media Fields and Reference Documents
Date: 2025-09-03

## Current Situation

We have:
1. **9 reference documents** with shared content extracted
2. **4 field category documents** following LLM-optimal structure
3. **Existing v5 prompt** for media fields that predates the reference extraction

## Key Question: How Should We Structure Prompts?

### Option 1: Single Unified Prompt
**One prompt that generates both category doc AND updates reference docs**

PROS:
- Single source of truth
- Ensures consistency
- Handles cross-cutting concerns naturally

CONS:
- Very complex prompt
- Difficult to maintain
- May confuse LLM with dual objectives

### Option 2: Two Specialized Prompts
**One for field category, one for reference updates**

PROS:
- Clear separation of concerns
- Easier to maintain and debug
- Can run independently

CONS:
- Risk of inconsistency
- Need coordination between prompts
- Potential duplication

### Option 3: Modular Prompt with Flags
**Base prompt with toggles for what to generate**

PROS:
- Flexible approach
- Reusable components
- Can generate either or both

CONS:
- More complex to implement
- Requires careful parameter management

## Recommended Approach: Modified Option 2

### A. Primary Field Category Prompt (media-fields-v05)
Focus on field-specific content with AWARENESS of reference docs:

```markdown
## REFERENCE DOCUMENT AWARENESS
The following content has been extracted to reference documents.
DO NOT duplicate this content, instead link to:

1. **Validation Timing** → Link to validation-timing-reference.md
   - Mount/change/blur/submit behavior (universal)
   
2. **Component Namespaces** → Link to component-namespace-reference.md
   - Namespace troubleshooting (universal)
   
3. **Data Export** → Link to data-export-reference.md
   - CSV/JSON formats (mostly universal)
   - Note field-specific issues only
   
4. **Security** → Link to security-considerations-reference.md
   - General XSS, injection patterns
   - Note field-specific vulnerabilities only
   
5. **Performance** → Link to performance-thresholds-reference.md
   - General thresholds
   - Note field-specific limits only

[etc.]

## WHAT TO INCLUDE IN FIELD CATEGORY DOC
Focus on what's UNIQUE to media fields:
- File size limits specific to FileUploader
- Camera permissions specific to TakePhoto
- Platform-specific media behaviors
- Media processing pipelines
- Storage strategies for media
```

### B. Reference Update Prompt
Separate prompt to ADD media-specific content to references:

```markdown
## UPDATE REFERENCE DOCUMENTS
Add media field information to existing references:

### validation-timing-reference.md
ADD:
- FileUploader validation on file selection
- TakePhoto validation after capture
- Async validation for file size/type

### data-export-reference.md  
ADD:
- Binary data export challenges
- Base64 encoding in JSON
- File path references in CSV
- Media sync strategies

### security-considerations-reference.md
ADD:
- File upload vulnerabilities
- EXIF data privacy concerns  
- Path traversal risks
- Malicious file detection

[etc.]
```

## Implementation Strategy for Media Fields

### Step 1: Modify Existing Media Prompt
Update the v5 media prompt to:
1. Remove sections that now belong in reference docs
2. Add "See [Reference]" links where appropriate
3. Focus on media-specific content

### Step 2: Create Reference Update Checklist
Document what needs adding to each reference:
- Which references need media content
- What specific content to add
- How to maintain consistency

### Step 3: Execute in Sequence
1. Generate media-fields-v05.md with modified prompt
2. Update reference docs with media-specific additions
3. Verify no duplication or gaps

## Structural Changes Needed to Current Prompt

### REMOVE from media-fields-v05 prompt:
- Generic validation timing section
- Universal component namespace errors
- General export behavior
- Common security patterns
- Universal performance thresholds

### ADD to media-fields-v05 prompt:
```markdown
## Reference Document Links
When encountering universal patterns, link to:
- [Validation Timing Reference](../reference-docs/validation-timing-reference.md)
- [Component Namespace Reference](../reference-docs/component-namespace-reference.md)
- [Data Export Reference](../reference-docs/data-export-reference.md)
[etc.]

## Field-Specific Focus
Include ONLY content unique to media fields:
- File type restrictions
- Upload size limits
- Camera API details
- Image processing
- Offline storage
- Binary data handling
```

### KEEP in media-fields-v05 prompt:
- All media-specific configurations
- Platform-specific camera/file behaviors
- Media processing pipelines
- Storage strategies
- Media-specific examples

## Reference Documents Needing Media Updates

1. **accessibility-reference.md**
   - Camera interface accessibility
   - File upload keyboard navigation
   - Touch targets for capture button

2. **data-export-reference.md**
   - Binary file handling
   - Base64 encoding issues
   - File path strategies

3. **performance-thresholds-reference.md**
   - File size limits
   - Upload timeout thresholds
   - Image processing limits

4. **security-considerations-reference.md**
   - File upload vulnerabilities
   - EXIF stripping requirements
   - Malicious file detection

5. **formik-integration-reference.md**
   - File array handling
   - Async upload validation
   - Binary data in form state

6. **designer-limitations-reference.md**
   - Media field configuration limits
   - File type configuration

## Recommended Next Steps

1. **Create revised media-fields-v05 prompt** that acknowledges reference docs
2. **Create media-reference-updates checklist** documenting what to add
3. **Generate media-fields-v05.md** with new prompt
4. **Update reference docs** with media-specific content
5. **Verify consistency** across all documents

This approach maintains separation of concerns while ensuring completeness and avoiding duplication.