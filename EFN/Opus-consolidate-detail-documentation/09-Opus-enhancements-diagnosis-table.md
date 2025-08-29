## Prompt C1: Create Quick Diagnosis Tables

You are enhancing a Fieldmark field documentation file for LLM-first consumption, particularly for Claude Code notebook generation.

TASK: Create Quick Diagnosis Tables that map symptoms to causes and solutions.

INPUT: The consolidated text field documentation is available in project knowledge as "Email and Address Fields - Merged Documentation.md" - this document contains all 7 field types. Please search for and load this document to analyze, focusing on troubleshooting and common issues sections.

CRITICAL INSTRUCTION: Generate ONLY the new section to be appended. Do NOT reproduce the original document. Output ONLY the enhancement section with clear integration markers.

REQUIREMENTS:
1. Create a new section "Enhanced Quick Diagnosis Tables (2025-08)" at document end, just before the Metadata section
2. Generate ONLY this new section, not the full document
3. Use markdown tables
4. Include field-specific issues and solutions
5. Apply rich column structure: Symptom | Field Type | Cause | Solution | Prereq | Speed | Freq | Admin | Prevention | Version
6. Organize by problem categories with clear severity indicators
7. Include legend, escalation triggers, prevention checklist, and common procedures sections
8. Use symbols for quick scanning: 🟢 Quick Win | 🟡 Standard | 🔴 Complex | 🔥 Daily | ⚡ Weekly | 💧 Rare | 👤 User | 🔧 Admin
9. Make solutions actionable with prerequisites and prevention strategies
10. Include version marker for time-sensitive issues

OUTPUT FORMAT:

[START OF GENERATED SECTION - Add before Metadata]
---
## Enhanced Quick Diagnosis Tables (2025-08) {important}

### Legend
- **Speed**: 🟢 <1min | 🟡 1-5min | 🔴 >5min or needs help
- **Frequency**: 🔥 Daily | ⚡ Weekly | 💧 Rare
- **Admin**: 👤 User fix | 🔧 Admin/Developer needed
- **Prereq**: What you need before attempting the fix
- **Prevention**: How to avoid this issue in future

### When Generation Fails

| Symptom | Field Type | Likely Cause | Quick Fix | Prereq | Speed | Freq | Admin | Prevention | Version |
|---------|------------|--------------|-----------|--------|-------|------|-------|------------|---------|
| Empty HRID displayed | TemplatedString | Missing referenced field | Check field names (case-sensitive) | Designer access | 🟢 | 🔥 | 👤 | Test templates with sample data | 2025-08 |
| Shows [object Object] | TemplatedString | Using complex field | Use only for conditionals {{#field}} | Mustache knowledge | 🟡 | ⚡ | 👤 | Document field return types | 2025-08 |
| Scanner won't complete | QRCodeFormField | Multiple barcodes | Isolate single barcode | Physical access | 🟢 | 🔥 | 👤 | Train: one barcode at a time | 2025-08 |
| Scanner disabled | QRCodeFormField | Web platform | Pair with TextField | Notebook edit | 🔴 | 🔥 | 🔧 | Design with platform detection | 2025-08 |

### When Validation Fails

| Symptom | Field Type | Likely Cause | Quick Fix | Prereq | Speed | Freq | Admin | Prevention | Version |
|---------|------------|--------------|-----------|--------|-------|------|-------|------------|---------|
| Required not showing error | All text inputs | Field not touched | Focus then blur field | None | 🟢 | 🔥 | 👤 | Train on validation timing | 2025-08 |
| Email rejecting valid | Email | Spaces in input | Remove all spaces | None | 🟢 | ⚡ | 👤 | Add "no spaces" to helper | 2025-08 |
| Pattern never matches | TextField | Regex not escaped | Double-escape: "\\\\d" | Regex knowledge | 🟡 | 💧 | 🔧 | Provide pattern examples | 2025-08 |
| Form won't submit | QRCodeFormField | Required on web | Remove required | Designer access | 🟡 | 🔥 | 🔧 | Never require mobile-only fields | 2025-08 |

[Continue with other categories using same enhanced structure...]

### When Display Issues Occur
| Tables disappear | RichText | DOMPurify strips | Use image instead | None | 🟢 | 🔥 | 👤 | Know runtime limits | 2025-08 |

### When Export Issues Occur  
| JSON in single column | Address | Complex object | Post-process script | Python knowledge | 🟡 | ⚡ | 👤 | Document process | 2025-08 |

### When Performance Issues Occur
| Form lag on input | Text fields | >30 per section | Paginate form | Designer access | 🟡 | ⚡ | 🔧 | Count fields first | 2025-08 |

### Escalation Triggers

| Condition | Action | Contact | Urgency |
|-----------|--------|---------|---------|
| Same issue after 3 attempts | Document steps taken | Team lead | Medium |
| Data loss suspected | Stop immediately | IT support | HIGH |
| Multiple users affected | Check system status | Admin | HIGH |
| Fix requires missing access | Request access | Notebook owner | Low |
| Security issue suspected | Do not attempt fix | Security team | CRITICAL |

### Prevention Checklist

#### Before Deployment
- [ ] Test all templates with sample data
- [ ] Count total fields (<50 recommended)
- [ ] Check platform compatibility
- [ ] Verify validation with invalid data
- [ ] Document known limitations
- [ ] Test on target devices

#### During Training
- [ ] Explain validation timing (touch then blur)
- [ ] Demonstrate scanner technique (steady, isolated)
- [ ] Show export format examples
- [ ] Practice error recovery procedures
- [ ] Provide platform-specific guides

#### Ongoing Monitoring
- [ ] Track recurring issues weekly
- [ ] Monitor performance metrics
- [ ] Review error logs regularly
- [ ] Update documentation
- [ ] Gather user feedback

### Common Fix Procedures

#### Procedure A: Clear and Retry
1. Save any entered data (screenshot if needed)
2. Refresh browser/app
3. Clear browser cache if persists
4. Retry operation
5. If fails, escalate using triggers above

#### Procedure B: Permission Reset (Mobile)
1. Go to device Settings
2. Find Apps > Fieldmark
3. Tap Permissions
4. Enable all required permissions
5. Force stop app
6. Restart and retry

#### Procedure C: Export Data Recovery (Address JSON)
```python
import pandas as pd
import json
```

df = pd.read_csv('export.csv')
if 'site_address' in df.columns:
    df['address_data'] = df['site_address'].apply(
        lambda x: json.loads(x) if x else {}
    )
    df['postcode'] = df['address_data'].apply(
        lambda x: x.get('address', {}).get('postcode', '')
    )

### Quick Reference Matrix

| If you see... | First try... | Then try... | Last resort... |
|---------------|--------------|-------------|----------------|
| Empty field after entry | Tab away and back | Save form | Refresh page |
| Red field, no message | Check field type docs | Look for hidden requirements | Contact support |
| Scanner running forever | Check for multiple barcodes | Clean barcode | Use manual entry |
| Form won't save | Check required fields | Look for hidden fields | Export and recreate |
| Slow performance | Close other apps | Restart device | Reduce form complexity |

### Category Completion Requirements
- Generation Fails: Include all template and scanner issues
- Validation Fails: Cover touched state, schema order, type mismatches  
- Display Issues: Address rendering, visibility, platform differences
- Export Issues: Include format-specific problems and solutions
- Performance Issues: Document all thresholds and degradation points

[END OF GENERATED SECTION]

INTEGRATION CHECKLIST:
[ ] Enhanced structure with 9 columns per table
[ ] Legend clearly explains all symbols
[ ] Escalation triggers defined
[ ] Prevention strategies included
[ ] Common procedures documented
[ ] Quick reference matrix provided
[ ] All critical issues covered

VALIDATION:
Ensure 60%+ of issues are quick wins (🟢)
Cover all severity levels
Provide alternative approaches for complex issues
Include specific prerequisites for each fix

This version maintains all the structural enhancements that make the tables more useful (both for humans and LLMs) but defers the embedded metadata implementation for a later comprehensive pass across the entire documentation.


