# Mapping Consistency Report - Production Documentation

## Date: 2025-01-06
## Purpose: Check for contradictions/duplications between new designer-component-mapping.md and existing docs

## FINDINGS

### 1. CONTRADICTIONS FOUND ⚠️

#### number-fields-v05.md
The file has TWO different mapping tables that contradict each other:

**Table 1 (Line ~27):** ✅ CORRECT
```
| Controlled Number | TextField | formik-material-ui | TextField with type="number" and validation |
```

**Table 2 (Line ~319):** ❌ WRONG
```
| Controlled Number | ControlledNumber | faims-custom | Bounded numeric with slider |
```

This is a problem - the second table still shows ControlledNumber as a component name, which we know is incorrect.

#### relationship-field-v05.md
Has conflicting information:

**Table 1 (Line ~35):**
```
| Related Record Selector | RelationshipField | faims-custom | Record linking |
```

**Table 2 (Line ~95):**
```
| RelatedRecordSelector | RelatedRecordSelector | faims-custom | Bidirectional record relationships |
```

The new mapping document says:
```
| Related Record | RelatedRecordSelector | faims-custom |
```

So there's confusion about whether the component is "RelationshipField" or "RelatedRecordSelector".

#### select-choice-fields-v05.md
Shows incorrect namespaces:
```
| Checkbox | Checkbox | formik-material-ui |
| Select Field | Select | formik-material-ui |
| Select Multiple | MultiSelect | formik-material-ui |
| Select one option | RadioGroup | formik-material-ui |
```

But the new mapping (and reality) shows these are in `faims-custom` namespace.

#### location-fields-v05.md
Shows wrong namespace:
```
| Take GPS Point | TakePoint | mapping-plugin |
| Map Form Field | MapFormField | mapping-plugin |
```

TakePoint is actually in `faims-custom`, only MapFormField is in `mapping-plugin`.

### 2. DUPLICATIONS FOUND 📋

Every field category document has its own "Component Name Mapping" section that partially duplicates the new comprehensive mapping. This creates:
- Multiple sources of truth
- Maintenance burden (need to update multiple places)
- Risk of inconsistency (as we've seen)

### 3. CONSISTENCY ISSUES 🔍

#### Naming Inconsistencies:
- "Take GPS Point" vs "Take Point"
- "Related Record Selector" vs "RelatedRecordSelector" vs "RelationshipField"
- "Select Field" vs "Select"
- "Select Multiple" vs "MultiSelect"
- "Select one option" vs "RadioGroup"

#### Missing Information:
Individual field docs don't mention:
- ActionButton
- RandomStyle  
- Core-material-ui components
- The fact that many Designer fields are TextField configurations

### RECOMMENDATIONS

## IMMEDIATE FIXES NEEDED (Contradictions):

1. **number-fields-v05.md**: 
   - Remove or fix the second table showing "ControlledNumber" as a component

2. **relationship-field-v05.md**:
   - Clarify whether component is "RelationshipField" or "RelatedRecordSelector"
   - Need to check actual codebase

3. **select-choice-fields-v05.md**:
   - Fix namespaces (most are faims-custom, not formik-material-ui)

4. **location-fields-v05.md**:
   - Fix TakePoint namespace (should be faims-custom)

## STRUCTURAL RECOMMENDATIONS:

### Option 1: Centralize (Recommended)
- Keep comprehensive mapping ONLY in designer-component-mapping.md
- Remove "Component Name Mapping" sections from individual field docs
- Have field docs reference the central mapping

### Option 2: Specialize
- Keep only field-specific mappings in each doc
- Reference central doc for complete list
- Add clear note about which is authoritative

### Option 3: Synchronize
- Keep both but ensure they're identical
- Add automation to check consistency
- Higher maintenance burden

## CURRENT DUPLICATION STATS:

- 8 field category docs with mapping sections
- 1 comprehensive mapping document
- Total of 9 different places defining the same mappings
- ~40% have contradictions or errors

## PRIORITY:

**HIGH**: Fix the contradictions in number-fields-v05.md (ControlledNumber issue)
**MEDIUM**: Clarify RelatedRecordSelector vs RelationshipField  
**MEDIUM**: Fix namespace errors in select-choice and location docs
**LOW**: Decide on centralization strategy

---

*Report generated: 2025-01-06*
*Action required: Fix contradictions before next build*