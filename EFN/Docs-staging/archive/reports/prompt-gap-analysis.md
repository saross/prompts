# Prompt Gap Analysis: Media Fields Documentation
## Comparing Approaches and Expected Outcomes
Date: 2025-09-03

## Current State of Field Category Documents

### What We've Achieved (text, number, datetime, choice):
1. **~2,700-3,400 lines** of focused, field-specific content
2. **LLM-optimal structure** with Designer Guide at #2, Selection Guide at #3
3. **Complete extraction** from source documents
4. **Reference links** to 9 shared documents
5. **Standardized sections** including:
   - Decision trees with return types
   - Decision matrices
   - Selection strategies with platform/accessibility notes
   - Field quirks index
   - Performance thresholds
   - JSON patterns cookbook
   - Anti-patterns index
   - Error message reference
   - Field interaction matrix

### Quality Markers:
- Field-specific examples with complete JSON
- Platform behaviors documented per field
- Migration procedures for deprecated components
- Troubleshooting guides with solutions
- Cross-references to other field categories

## What the V6 Media Prompt Will Produce

### Strengths:
1. ✅ **Reference awareness** - Won't duplicate shared content
2. ✅ **LLM-optimal structure** - Maintains proven template
3. ✅ **Media-specific focus** - Concentrates on unique aspects
4. ✅ **Proper sectioning** - All standard sections included

### Potential Gaps:
1. ⚠️ **Source material quality** - Depends on completeness of FileUploader.md, TakePhoto.md
2. ⚠️ **Field coverage** - Do we have docs for MapForm, TakePoint?
3. ⚠️ **Depth of content** - Will we reach 2,700+ lines?
4. ⚠️ **Pattern extraction** - Need rich examples from source

## Gap Analysis: Opus Prompts vs V6 Approach

### Opus Sequential Approach (from your selection):
**PROS:**
- Systematic field-by-field extraction
- Explicit deduplication markers
- Preserves every detail
- Clear variant handling

**CONS:**
- Not reference-aware (predates extraction)
- Would duplicate reference content
- More complex multi-step process
- Not optimized for our new structure

### V6 Reference-Aware Approach:
**PROS:**
- Single-pass generation
- Reference-aware from start
- Follows proven structure
- Cleaner output

**CONS:**
- Depends on source completeness
- Less systematic extraction
- May miss nuanced variants

## Critical Question: Will V6 Get Us There?

### YES, if source documents contain:
1. **Complete technical specifications** for each field
2. **Platform-specific behaviors** documented
3. **Rich JSON examples** with variations
4. **Error scenarios** and solutions
5. **Performance limits** with numbers
6. **Security considerations** specific to media

### NO, if source documents lack:
1. **Quirks and edge cases** (often discovered through use)
2. **Cross-field interactions** (media + text combinations)
3. **Migration patterns** from older versions
4. **Real-world usage examples**
5. **Platform-specific gotchas**

## Recommended Hybrid Approach

### Phase 1: Use V6 Prompt
Generate initial media-fields-v05.md to establish:
- Core structure
- Basic field documentation
- Initial examples
- Reference links

### Phase 2: Enhancement Pass
Use targeted prompts to add missing content:

#### A. Field Quirks Extraction
```markdown
Review source docs and codebase for:
- Undocumented behaviors
- Platform inconsistencies
- Edge cases
- Workarounds
```

#### B. Pattern Development
```markdown
Generate comprehensive patterns for:
- Offline photo queue
- Multi-file upload with progress
- GPS accuracy thresholds
- File size optimization
```

#### C. Cross-Field Integration
```markdown
Document interactions between:
- TakePhoto + TextField (captions)
- FileUploader + Select (categorization)
- MapForm + Number (coordinates)
```

#### D. Performance Testing Results
```markdown
Add specific thresholds discovered through testing:
- Upload timeout limits
- Concurrent upload max
- Image processing boundaries
- Memory constraints
```

## Specific Gaps to Address Post-Generation

### 1. Location Fields Documentation
Check if we have:
- MapForm.md
- TakePoint.md
- GPS/coordinate handling

If missing, need separate extraction effort.

### 2. Media Processing Pipeline
Likely not in source docs:
- Thumbnail generation
- EXIF stripping
- Compression algorithms
- Format conversions

### 3. Offline Sync Strategies
Complex topic that may need:
- Queue management
- Conflict resolution
- Retry mechanisms
- Priority handling

### 4. Platform-Specific Camera APIs
Often underdocumented:
- iOS 17+ changes
- Android 14+ restrictions
- PWA limitations
- Browser differences

## Success Metrics

### Minimum Viable Documentation:
- [x] All media/location fields documented
- [x] Core configuration examples
- [x] Basic troubleshooting
- [x] Reference links working
- [x] ~1,500+ lines

### Target State (matching other categories):
- [ ] 2,700+ lines of rich content
- [ ] Complete quirks index
- [ ] Comprehensive patterns cookbook
- [ ] Full error reference
- [ ] Platform matrix complete
- [ ] Migration procedures
- [ ] Performance thresholds with numbers

## Recommendation

### Use Three-Phase Approach:

**Phase 1: V6 Generation** (Immediate)
- Run consolidation-prompt-media-fields-v6-reference-aware.md
- Get baseline documentation
- Identify gaps

**Phase 2: Gap Analysis** (After Generation)
- Compare output to text/number/datetime/choice docs
- List missing sections
- Note thin content areas

**Phase 3: Targeted Enhancement** (Follow-up)
Create specific prompts for:
1. Quirks and edge cases extraction
2. Pattern cookbook development
3. Performance threshold documentation
4. Platform-specific behavior matrix
5. Error message compilation

### Expected Outcome:
- Phase 1: 60-70% complete (~1,800 lines)
- Phase 2: Gap identification
- Phase 3: 95% complete (~2,700+ lines)

## Alternative: Opus + V6 Hybrid

If source docs are very rich, could:
1. Use Opus prompts for systematic extraction
2. Post-process to remove reference duplicates
3. Restructure to match LLM-optimal template

More work but guarantees completeness.

## Conclusion

The V6 prompt will get us **most of the way there** (60-70%), but will likely need follow-up enhancement to match the depth and quality of existing field category documents. This is acceptable and manageable:

1. **V6 provides the skeleton** - Right structure, reference awareness
2. **Follow-up adds the meat** - Quirks, patterns, real-world details
3. **Total effort reasonable** - Less than starting from scratch

The key advantage is maintaining consistency with our new reference-aware architecture while building on proven patterns.