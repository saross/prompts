# Alignment Plan for Text, Number, and DateTime Fields Documentation
## To Match Choice Fields v05 and LLM-Optimal Structure

## Current State Analysis

### Document Comparison
| Document | H2 Sections | Lines | Designer Guide Position | Individual Field Ref | Quick Reference Enhanced |
|----------|------------|-------|------------------------|---------------------|-------------------------|
| **text-fields-v05.md** | 24 | 3,442 | #11 (line 183) ❌ | H2 ✅ | No ❌ |
| **number-fields-v05.md** | 22 | 2,747 | #2 (line 33) ✅ | H2 ✅ | No ❌ |
| **datetime-fields-v05.md** | 22 | 2,619 | #2 (line 26) ✅ | H2 ✅ | No ❌ |
| **select-choice-fields-v05.md** | 23 | ~3,430 | #2 (line 38) ✅ | H2 ✅ | Yes ✅ |

### Key Structural Issues

#### 1. Text Fields (Most Work Needed)
- **Designer Usage Guide at position #11** - needs to move to #2
- Missing Field Selection Guide at position #3
- Has 24 sections (1 extra - needs consolidation)
- No enhanced Quick Reference boxes
- No Validation Timing Behavior subsection
- Anti-patterns already distributed ✅

#### 2. Number Fields (Moderate Work)
- Designer Usage Guide correctly at #2 ✅
- Missing standard H2 section (has 22, needs 23)
- No enhanced Quick Reference boxes
- No Validation Timing Behavior subsection
- Anti-patterns already distributed ✅

#### 3. DateTime Fields (Moderate Work)
- Designer Usage Guide correctly at #2 ✅
- Missing standard H2 section (has 22, needs 23)
- No enhanced Quick Reference boxes
- No Validation Timing Behavior subsection
- Anti-patterns already distributed ✅

## Required Changes for All Three Documents

### A. STRUCTURAL CHANGES (High Priority)

#### 1. Section Reordering
**Text Fields Only:**
- Move Designer Usage Guide from position #11 to position #2
- Move Field Selection Guide to position #3
- Reorder remaining sections to match LLM-optimal structure

#### 2. Missing Sections
**All Three Documents Need:**
- Ensure all 23 standard H2 sections are present
- Add missing sections with {importance} tags
- Verify section names match exactly

### B. CONTENT ENHANCEMENTS (High Priority)

#### 1. Quick Reference Box Enhancement
**Add to EVERY field in ALL documents:**
```markdown
| Touch Targets | [specific pixel measurements] |
| Performance | [thresholds: optimal, degraded, unusable] |
| Storage | [data format, null handling] |
```

#### 2. Validation Timing Behavior
**Add to Common Characteristics in ALL documents:**
```markdown
#### Validation Timing Behavior [affects: All fields] {important}
- **On mount**: Validation runs but errors hidden until touched
- **On change**: Immediate validation, field marked as touched
- **On blur**: Re-validates and displays any errors
- **On submit**: All fields validated, all errors shown
- **Platform differences**: Mobile may delay blur event
```

#### 3. Anti-pattern Distribution
✅ **ALREADY COMPLETE** - All three documents already have anti-patterns distributed per field

### C. TECHNICAL CORRECTIONS (Critical)

#### 1. Type-returned Values
**Verify and correct in all documents:**
- Boolean fields: `faims-core::Bool` (NOT Boolean)
- Number fields: `faims-core::Number`
- String fields: `faims-core::String`
- Integer fields: `faims-core::Integer`

#### 2. Validation Schemas
**Verify and correct:**
- `["yup.bool"]` NOT `["yup.boolean"]`
- `["yup.number"]` for numeric fields
- `["yup.string"]` for text fields
- `["yup.date"]` for date fields

### D. CONTENT TO OFFLOAD (Medium Priority)

#### Move to Standalone Documents:
1. **performance-thresholds-matrix.md**
   - Extract detailed performance tables
   - Keep only essential thresholds inline

2. **platform-specifications-reference.md**
   - Extract platform-specific implementation details
   - Keep only critical differences inline

3. **field-technical-architecture.md**
   - Extract deep technical implementation
   - Keep only essential architecture notes

4. **validation-timing-reference.md**
   - Extract detailed validation sequences
   - Keep only standard timing behavior

5. **debug-procedures-guide.md**
   - Extract detailed debugging steps
   - Keep only common troubleshooting

## Implementation Plan

### Phase 1: Text Fields (Most Complex)
**Estimated Time: 2 hours**
1. ✏️ Restructure sections (move Designer Guide to #2)
2. ✏️ Add Field Selection Guide at #3
3. ✏️ Enhance all Quick Reference boxes
4. ✏️ Add Validation Timing Behavior
5. ✏️ Fix type-returned values
6. ✏️ Verify against codebase

### Phase 2: Number Fields
**Estimated Time: 1 hour**
1. ✏️ Add missing H2 section
2. ✏️ Enhance all Quick Reference boxes
3. ✏️ Add Validation Timing Behavior
4. ✏️ Verify type-returned values
5. ✏️ Verify against codebase

### Phase 3: DateTime Fields
**Estimated Time: 1 hour**
1. ✏️ Add missing H2 section
2. ✏️ Enhance all Quick Reference boxes
3. ✏️ Add Validation Timing Behavior
4. ✏️ Verify type-returned values
5. ✏️ Verify against codebase

### Phase 4: Create Standalone Documents
**Estimated Time: 2 hours**
1. 📄 Create performance-thresholds-matrix.md
2. 📄 Create platform-specifications-reference.md
3. 📄 Create validation-timing-reference.md
4. 📄 Extract content from all field documents
5. 📄 Add cross-references

## Success Criteria

### All Documents Must Have:
- [ ] Exactly 23 H2 sections in correct order
- [ ] Designer Usage Guide at position #2
- [ ] Field Selection Guide at position #3
- [ ] Individual Field Reference as H2 (not H1)
- [ ] All fields as H3 under Individual Field Reference
- [ ] Enhanced Quick Reference boxes (8+ rows)
- [ ] Validation Timing Behavior subsection
- [ ] Distributed anti-patterns per field
- [ ] Correct type-returned values
- [ ] {importance} tags on all H2 sections
- [ ] 2,200-2,700 lines (after offloading)

## Order of Operations

### Recommended Sequence:
1. **Start with Number or DateTime** (easier, already have Designer Guide at #2)
2. **Then tackle Text Fields** (most complex restructuring)
3. **Create standalone documents** as content is extracted
4. **Final verification** against codebase

## Special Considerations

### Text Fields Unique Issues:
- Has Component Selection Decision Tree section (may need to merge with Field Selection Guide)
- Longest document (3,442 lines) - needs most offloading
- Most fields to update (13 text field types)

### Number Fields Unique Issues:
- Has CRITICAL PRECISION risks (not SECURITY)
- Controlled number fields with complex validation
- Scientific notation handling

### DateTime Fields Unique Issues:
- Has CRITICAL DATA INTEGRITY risks
- Timezone complexity
- Multiple format standards

## Next Steps

1. **Decide implementation order** based on priority
2. **Create backup copies** before major changes
3. **Use automated tools** where possible (search/replace for type-returned)
4. **Test JSON examples** after corrections
5. **Verify against codebase** using accuracy check process

## Estimated Total Time: 6-8 hours

This plan ensures all field documentation reaches the same high standard as the choice fields documentation, with consistent LLM-optimal structure and verified technical accuracy.