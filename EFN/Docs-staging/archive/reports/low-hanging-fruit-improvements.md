# Low-Hanging Fruit for Document Improvements
## Quick Wins with Maximum Impact

## 1. 🍎 Add Validation Timing Behavior (15 minutes total)
**Impact: HIGH** - Critical missing information
**Effort: LOW** - Same text for all 3 documents

### Add to Common Characteristics section in all three docs:
```markdown
#### Validation Timing Behavior [affects: All fields] {important}
- **On mount**: Validation runs but errors hidden until touched
- **On change**: Immediate validation, field marked as touched
- **On blur**: Re-validates and displays any errors
- **On submit**: All fields validated, all errors shown
- **Platform differences**: Mobile may delay blur event
```

**Implementation:**
- Simple copy-paste into 3 documents
- Location: Common Characteristics section (already exists)
- No structural changes needed

---

## 2. 🍎 Fix Type-returned Values (30 minutes total)
**Impact: CRITICAL** - Prevents broken notebooks
**Effort: LOW** - Simple find/replace

### Global corrections needed:
```bash
# For all three documents:
Replace: "faims-core::Boolean" → "faims-core::Bool"
Replace: ["yup.boolean"] → ["yup.bool"]

# Verify these are correct:
- "faims-core::String" 
- "faims-core::Number"
- "faims-core::Integer"
- "faims-core::Date"
```

**Implementation:**
- Use global find/replace
- Quick verification against codebase
- Test one JSON example to confirm

---

## 3. 🍎 Add Missing H2 Section Tags (10 minutes)
**Impact: MEDIUM** - Improves LLM parsing
**Effort: MINIMAL** - Just adding tags

### Number & DateTime need one more section each:
- They have 22 sections (need 23)
- Likely missing {importance} tags on some H2s
- Quick scan and add missing tags

**Implementation:**
- Compare against choice fields H2 list
- Add any missing {essential}, {important}, or {comprehensive} tags
- No content changes needed

---

## 4. 🍎 Quick Reference Enhancement Template (45 minutes)
**Impact: HIGH** - Major usability improvement
**Effort: MEDIUM** - But can be semi-automated

### Create a template and bulk apply:
```markdown
| Touch Targets | Standard HTML input (44×22px minimum) |
| Performance | <100 fields optimal, 200+ degraded |
| Storage | String/Number/Date, null as empty |
```

**For text fields (default for all):**
- Touch Targets: "Standard HTML input (44×22px minimum)"
- Performance: "Single field instant, 100+ fields noticeable lag"
- Storage: "String, empty string for null"

**For number fields (default for all):**
- Touch Targets: "Standard HTML input (44×22px minimum)"
- Performance: "Validation on each keystroke, 50+ fields noticeable"
- Storage: "Number, null for empty"

**For datetime fields (default for all):**
- Touch Targets: "Native picker on mobile, calendar on desktop"
- Performance: "Date parsing on each change, 50+ fields degraded"
- Storage: "ISO 8601 string, null for empty"

**Implementation:**
- Create defaults, then customize only where needed
- Can use regex to insert after "| Default |" line in Quick Reference

---

## 5. 🍎 Verify Component Names (20 minutes)
**Impact: CRITICAL** - Prevents "component not found" errors
**Effort: LOW** - Quick check

### Quick verification checklist:
- All use `"component-namespace": "faims-custom"`
- Component names are EXACT (case-sensitive)
- Common mistakes: "DatetimeNow" vs "DateTimeNow"

**Implementation:**
- Grep for component-name patterns
- Compare against working notebooks
- Fix any case mismatches

---

## Total Time: ~2 hours for ALL improvements

## Order of Implementation (Fastest First):

1. **Add Validation Timing (15 min)** - Highest value, lowest effort
2. **Fix type-returned (30 min)** - Critical fixes
3. **Add H2 tags (10 min)** - Quick improvement
4. **Verify components (20 min)** - Prevent errors
5. **Quick Reference rows (45 min)** - Biggest task but high value

---

## What We're NOT Doing (Yet):

### These are important but NOT low-hanging fruit:

❌ **Moving Designer Usage Guide in text-fields**
- Requires major restructuring
- Risk of breaking references
- Save for dedicated session

❌ **Creating standalone documents**
- Requires content extraction and reorganization
- New document creation
- Save for Phase 2

❌ **Adding Field Selection Guide to text-fields**
- Requires new content creation
- Structural changes
- Save for comprehensive update

❌ **Trimming documents to 2,500 lines**
- Requires careful content evaluation
- Risk of losing information
- Save for when standalone docs exist

---

## Quick Test After Changes:

### Validation Test (5 minutes):
1. Extract one JSON example from each document
2. Test in a notebook
3. Verify field renders correctly
4. Check validation works

### This gets us 80% of the value with 20% of the effort!