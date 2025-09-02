# Remaining Additions to select-choice-fields-v05.md

## Total Scope: ~200-250 lines

## 1. Quick Reference Enhancements (25 lines total)
Add 3 rows to each of 5 fields' Quick Reference boxes:

### ✅ Checkbox (line ~1022)
```markdown
| Touch Targets | 24×24px icon, 48×48px target |
| Performance | 20-30 optimal, 50+ degraded, 100+ unusable |
| Storage | Boolean (true/false, null→false) |
```

### ✅ MultiSelect (line ~1264)
```markdown
| Touch Targets | Full row clickable (48px height) |
| Performance | ≤15 expanded optimal, 20+ dropdown, 50+ degraded |
| Storage | Array of strings, empty array valid |
```

### ✅ RadioGroup (line ~1559)
```markdown
| Touch Targets | 42px radio buttons (below iOS 44px standard) |
| Performance | 3-7 optimal, 10+ degraded, 20+ unusable |
| Storage | String, no null state after selection |
```

### ✅ Select (line ~1818)
```markdown
| Touch Targets | Native picker on mobile, dropdown on desktop |
| Performance | 50 options acceptable, 100+ degraded, 200+ unusable |
| Storage | String, empty string for no selection |
```

### ✅ AdvancedSelect (line ~2102)
```markdown
| Touch Targets | Fixed 500px width causes mobile scrolling |
| Performance | 50 nodes optimal, 100+ degraded, 500+ unusable |
| Storage | String path with " > " delimiter |
```

## 2. Missing Named Examples (150 lines total)

### 📝 Checkbox - Add 2 examples (30 lines)
After existing examples (~line 1145):
- **"Data Quality Indicator with Persistence"** - Shows meta.persistent usage
- **"Migration from RadioGroup Pattern"** - Shows conversion from Yes/No radio

### 📝 MultiSelect - Add 3 examples (45 lines)
After existing example (~line 1440):
- **"Basic Multi-Selection with Validation"** - artefact-materials with yup.min
- **"Dropdown for Long Lists"** - permits-required with 10+ options
- **"Migration from Multiple Checkboxes"** - recording-methods consolidation

### 📝 RadioGroup - Add 2 examples (30 lines)
After existing example (~line 1750):
- **"Heritage Condition Assessment"** - Excellent/Good/Fair/Poor/Not assessed
- **"Binary Choice Alternative"** - Why to use Select instead

### 📝 Select - Add 2 examples (30 lines)
After existing example (~line 2040):
- **"Site Classification"** - Heritage site types with empty option
- **"Condition Assessment with Null Option"** - Proper null handling

### 📝 AdvancedSelect - Add 2 examples (30 lines)
After existing example (~line 2380):
- **"Biological Taxonomy"** - Kingdom > Phylum > Class hierarchy
- **"Archaeological Context Hierarchy"** - Site > Area > Context > Find

## 3. Inline Enhancements (50-75 lines total)

### 🔧 Key Features Sections (5 fields × 3-4 lines = 15-20 lines)
Add inline to existing bullet points:
- Specific pixel measurements where relevant
- Performance thresholds inline
- State transition notes

Example for Checkbox:
```markdown
- ⚠️ Label not clickable - only 24×24px checkbox icon responds (iOS requires 44×44px minimum)
- ⚠️ Performance degrades with 50+ checkboxes, unusable at 100+ (use MultiSelect instead)
```

### 🔧 Validation Sections (5 fields × 2-3 lines = 10-15 lines)
Add timing notes:
```markdown
- Validates on change (immediate feedback)
- Errors display on blur (after user leaves field)
- All validation runs on submit attempt
```

### 🔧 Issues Sections (5 fields × 4-5 lines = 20-25 lines)
Add platform-specific notes:
```markdown
**Platform-specific behaviors:**
- **iOS**: Touch target below 44×44px Apple HIG standard
- **Android**: Material Design 48×48px touch target respected
- **Desktop**: Hover states work, click target matches visual size
```

### 🔧 Common Characteristics Section (10-15 lines)
Add missing subsection after line ~656:
```markdown
#### Validation Timing Behavior [affects: All fields] {important}
- **On mount**: Validation runs but errors hidden until touched
- **On change**: Immediate validation, field marked as touched
- **On blur**: Re-validates and displays any errors
- **On submit**: All fields validated, all errors shown
- **Platform differences**: Mobile may delay blur event
```

## 4. Summary of Content NOT Being Added
These go to standalone docs instead:
- ❌ Technical Architecture (Material-UI wrapping, Formik details)
- ❌ Separate Platform-Specific Rendering sections
- ❌ State Transition diagrams
- ❌ Debug Checklists per field
- ❌ Cross-References sections per field
- ❌ Storage format tables
- ❌ Migration code scripts

## Implementation Order

### Phase 1: Quick Reference (25 lines) - 10 minutes
1. Add 3 rows to each Quick Reference box
2. Include exact measurements from source docs

### Phase 2: Common Characteristics (15 lines) - 5 minutes
1. Add Validation Timing Behavior subsection

### Phase 3: Inline Enhancements (50 lines) - 20 minutes
1. Enhance Key Features with measurements
2. Add timing to Validation sections
3. Add platform notes to Issues sections

### Phase 4: Missing Examples (150 lines) - 30 minutes
1. Add 11 named examples total
2. Include complete JSON configurations
3. Add use case explanations

## Total Time Estimate: ~1 hour
## Total Lines: ~240 lines

## Verification Checklist
- [ ] All 5 Quick Reference boxes enhanced
- [ ] Validation Timing added to Common Characteristics
- [ ] All 11 named examples added
- [ ] Inline measurements in Key Features
- [ ] Platform notes in Issues sections
- [ ] Document remains under 2,700 lines total