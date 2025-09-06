# Shareable Content Candidates
## Content That Should Be Extracted to Standalone Documents

### 1. ✅ Validation Timing (DONE)
**Created**: `validation-timing-reference.md`
- Universal across all fields
- Platform-specific variations documented
- State management details

### 2. Component Namespace Information
**Proposed file**: `component-namespace-reference.md`

**Universal content**:
- All custom fields use `"component-namespace": "faims-custom"`
- Standard fields use `"component-namespace": "formik-material-ui"`
- Namespace errors and troubleshooting identical across all types
- Case sensitivity rules

**What to include**:
- Complete namespace list
- Component name mapping table
- Common errors and fixes
- Migration from old namespaces

### 3. Designer Limitations
**Proposed file**: `designer-limitations-reference.md`

**Universal limitations**:
- Cannot edit validation messages
- Cannot configure error display
- Cannot set complex validation rules
- Cannot create conditional validation
- Cannot customize component styling
- Preview limitations

**Varies by field**: Specific field configurations available in Designer

### 4. Security Vulnerabilities
**Proposed file**: `security-vulnerabilities-reference.md`

**Common across all fields**:
- XSS risks in labels (HTML injection)
- SQL injection (not applicable - NoSQL)
- File upload risks (media fields)
- Data validation bypass methods
- Client-side validation limitations

**Field-specific**: Each type has unique risks that should stay in main docs

### 5. Export Behavior
**Proposed file**: `data-export-reference.md`

**Universal patterns**:
- CSV export formatting
- JSON export structure
- Null vs empty string handling
- Array serialization (MultiSelect)
- Date formatting standards
- Special character escaping

### 6. Performance Thresholds Matrix
**Proposed file**: `performance-thresholds-matrix.md`

**Shareable metrics**:
- Form rendering times by field count
- Validation performance impacts
- Mobile vs desktop thresholds
- Memory usage patterns
- Network sync impacts

**Field-specific**: Exact numbers vary by field type

### 7. Platform Behaviors
**Proposed file**: `platform-specifications-reference.md`

**Universal behaviors**:
- iOS specific issues (touch targets, blur events)
- Android specific issues (keyboard behavior)
- PWA limitations
- Browser differences (Safari, Chrome, Firefox)
- Native picker availability

### 8. Common Anti-patterns
**Proposed file**: `anti-patterns-master-list.md`

**Universal anti-patterns**:
- Wrong namespace usage
- Incorrect type-returned values
- Validation schema order errors
- Missing required properties
- Case sensitivity mistakes

**Keep distributed**: Field-specific anti-patterns stay with fields

### 9. Meta Properties
**Proposed file**: `meta-properties-reference.md`

**Universal for all fields**:
```json
"meta": {
  "annotation": {"include": true, "label": "Notes"},
  "uncertainty": {"include": true, "label": "Uncertain"}
}
```
- Same structure across all fields
- Same behavior and storage
- Same Designer configuration

### 10. Formik Integration Details
**Proposed file**: `formik-integration-reference.md`

**Universal details**:
- Field state management
- Touched/pristine/dirty states
- Error handling pipeline
- Value transformation
- Submit handling

## Recommended Extraction Priority

### Phase 1: High Value, Easy Extraction (1 hour)
1. ✅ Validation Timing (DONE)
2. Component Namespace Information
3. Meta Properties
4. Export Behavior

### Phase 2: Medium Complexity (2 hours)
5. Designer Limitations
6. Platform Behaviors
7. Performance Thresholds

### Phase 3: Requires Careful Consolidation (2 hours)
8. Security Vulnerabilities
9. Common Anti-patterns
10. Formik Integration

## Benefits of Extraction

### For Documentation:
- Reduces each field doc by ~200-300 lines
- Eliminates redundancy across 5 category docs
- Single source of truth for universal behaviors
- Easier to maintain and update

### For Users:
- Can bookmark reference docs for quick access
- Don't need to hunt through field docs for common info
- Clear separation of universal vs specific
- Better understanding of system-wide patterns

### For LLMs:
- Cleaner, more focused field documentation
- Can reference shared docs when needed
- Reduces token usage for field-specific queries
- Better context management

## Implementation Strategy

### Step 1: Create reference doc
### Step 2: Add cross-references in field docs
```markdown
### Validation Timing
See [Validation Timing Reference](validation-timing-reference.md) for complete details.

**Field-specific notes:**
- Text fields validate on every keystroke
- [Any unique behaviors for this field type]
```

### Step 3: Remove redundant content from field docs
### Step 4: Update table of contents/README

## Estimated Impact

**Current state**: 5 category docs × ~3000 lines = ~15,000 lines
**After extraction**: 5 category docs × ~2200 lines + 10 reference docs × ~200 lines = ~13,000 lines
**Net reduction**: ~2,000 lines
**Redundancy eliminated**: ~8,000 lines (counting duplicates)