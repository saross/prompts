<!-- concat:boundary:start section="dashboard-troubleshooting" -->
<!-- concat:metadata
document_id: dashboard-troubleshooting
category: problem_resolution
type: diagnostic_guide
solution_count: 45
last_updated: 2025-09-08
-->

<!-- discovery:metadata
provides: [error-solutions, diagnostic-flowcharts, common-issues, quick-fixes]
see-also: [dashboard-overview, dashboard-patterns, troubleshooting-index]
-->

# Dashboard Troubleshooting Guide

<!-- structured:metadata
meta:purpose: problem-resolution
meta:summary: Comprehensive troubleshooting guide for Dashboard UI issues with error-to-solution mappings and diagnostic flowcharts.
meta:generates: solutions
meta:requires: [error-identification, symptom-matching]
meta:version: 3.0.0
meta:document: dashboard_troubleshooting
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Dashboard Patterns](./dashboard-patterns.md) | **Dashboard Troubleshooting** | [Production Docs →](../README.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Dashboard Patterns](#dashboard-patterns) | [Field Documentation ↓](#text-input-fields) -->

## Quick Diagnosis Table {essential}

| Symptom | Likely Cause | Solution | Section |
|---------|--------------|----------|---------|
| Can't login | Wrong credentials/suspended | Reset password | [Authentication](#authentication-issues) |
| Can't see notebook | No permission | Request access | [Access](#access-permission-issues) |
| Can't create team | Wrong role | Need Org Admin | [Teams](#team-management-issues) |
| Template won't save | Missing HRID | Add HRID field | [Templates](#template-designer-issues) |
| Invite not received | Email issues | Check spam | [Invitations](#invitation-email-issues) |
| Export fails | Large dataset | Batch export | [Data](#data-export-issues) |
| Can't edit record | Wrong status | Check workflow | [Records](#record-management-issues) |
| Sync not working | Network issue | Check connection | [Sync](#synchronisation-issues) |

---

## Authentication Issues {essential}

### Cannot Login

#### Symptoms
- "Invalid credentials" error
- Page refreshes without login
- "Account suspended" message

#### Diagnostic Steps
1. Verify email address spelling
2. Check caps lock
3. Try password reset
4. Check with administrator

#### Solutions

| Cause | Solution | Prevention |
|-------|----------|------------|
| **Wrong password** | Click "Forgot Password" → Reset via email | Use password manager |
| **Account suspended** | Contact administrator for reactivation | Regular activity |
| **Email not verified** | Check email for verification link | Verify immediately |
| **Account doesn't exist** | Request account creation | Maintain user list |
| **Browser issues** | Clear cookies/cache, try different browser | Keep browser updated |

### Session Timeout

#### Symptoms
- Suddenly logged out
- "Session expired" message
- Work lost warning

#### Solutions
```
Immediate: Login again
Long-term: Settings > Preferences > Extend session timeout
Best practice: Save work frequently
```

---

## Access & Permission Issues {important}

### Cannot See Resources

#### Diagnostic Flowchart
```
Can't see notebook/template?
├─ Are you logged in?
│  └─ No → Login first
├─ Check "All Notebooks" filter
│  └─ Still missing → You lack permission
├─ Check team membership
│  └─ Not member → Request team invitation
└─ Contact notebook admin for access
```

#### Permission Resolution Matrix

| Resource Type | Who to Contact | Required Info |
|--------------|---------------|---------------|
| **Notebook** | Notebook Administrator | Notebook name, purpose |
| **Template** | Template owner or Team Admin | Template name, use case |
| **Team** | Team Administrator | Team name, role needed |
| **System Feature** | System Administrator | Feature, business need |

### Wrong Permissions

#### Symptoms
- Can view but not edit
- Missing action buttons
- "Permission denied" errors

#### Solutions by Role

| Current Role | Need To | Solution |
|-------------|---------|----------|
| **Data Viewer** | Edit records | Request Data Collector role |
| **Data Collector** | Review records | Request Data Reviewer role |
| **Team Member** | Manage team | Request Team Administrator |
| **Standard User** | Create templates | Request Template Designer role |

---

## Template & Designer Issues {important}

### Template Won't Save

#### Common Causes & Fixes

| Error | Cause | Solution |
|-------|-------|----------|
| **"Invalid template"** | Missing HRID field | Add TemplatedStringField |
| **"Duplicate field ID"** | Same ID used twice | Rename one field |
| **"Missing fviews"** | No form structure | Add fviews layer in JSON |
| **Silent failure** | Browser timeout | Check console, try again |

#### HRID Field Template
```json
"record_hrid": {
  "component-namespace": "faims-custom",
  "component-name": "TemplatedStringField",
  "component-parameters": {
    "template": "{{PROJECT}}-{{_YYYY}}-{{auto_increment}}"
  }
}
```

### Designer Not Loading

#### Symptoms
- Blank screen
- Spinning loader
- Fields not draggable

#### Solutions
1. **Refresh page** (Ctrl+F5)
2. **Clear browser cache**
3. **Try different browser**
4. **Check browser console** for errors
5. **Disable browser extensions**

### Field Configuration Lost

#### Symptoms
- Settings reset to default
- Validation rules missing
- Help text disappeared

#### Prevention & Recovery
- **Save frequently** (every 5-10 changes)
- **Export JSON backup** before major changes
- **Test in separate notebook** first
- **Document complex configurations**

---

## Notebook Deployment Issues {important}

### Notebook Creation Fails

#### Error Messages & Solutions

| Error | Meaning | Fix |
|-------|---------|-----|
| **"Name already exists"** | Duplicate notebook | Choose unique name |
| **"Template not found"** | Template deleted | Use JSON backup |
| **"Invalid JSON"** | Syntax error | Validate with linter |
| **"Permission denied"** | Insufficient role | Need admin rights |

### Notebook Not Accessible

#### Diagnostic Steps
```
1. Verify notebook exists:
   Notebooks > All Notebooks (admin only)
   
2. Check your access:
   Notebook > Users tab > Find your email
   
3. Check invitation status:
   Notebook > Invites tab
   
4. Request access:
   Contact notebook admin with:
   - Notebook name
   - Required role
   - Business justification
```

---

## Team Management Issues {comprehensive}

### Cannot Create Team

| Issue | Requirement | Solution |
|-------|------------|----------|
| **No create button** | Need Org Admin role | Request role elevation |
| **"Name exists"** | Unique name required | Modify team name |
| **Creation fails** | System issue | Contact support |

### Cannot Add Team Members

#### Troubleshooting Checklist
- [ ] Verify Team Administrator role
- [ ] Check email address format
- [ ] Ensure user not already member
- [ ] Try resending invitation
- [ ] Check spam filters
- [ ] Verify email exists

### Team Resources Not Visible

| Resource | Location | Common Issue |
|----------|----------|--------------|
| **Notebooks** | Team > Notebooks tab | Not created from team context |
| **Templates** | Team > Templates tab | Created individually |
| **Members** | Team > Users tab | Invitations pending |

---

## Invitation & Email Issues {important}

### Invitations Not Received

#### Step-by-Step Resolution

1. **Check spam/junk folder**
2. **Verify email address**
   - No typos
   - Correct domain
3. **Check email filters**
   - Whitelist fieldmark domain
4. **Resend invitation**
   - Cancel original
   - Send new invitation
5. **Alternative method**
   - Direct account creation
   - Manual addition by admin

### Invitation Expired

| Action | Who Can Do | Process |
|--------|-----------|---------|
| **Resend** | Notebook/Team Admin | Invites tab > Resend |
| **Cancel & Recreate** | Admin | Cancel > New invitation |
| **Direct Add** | Admin | Users tab > Add directly |

### Email Verification Issues

#### Banner: "Your email is not verified!"

Solutions:
1. Click "Click here" in banner
2. Check email for verification
3. Check spam folder
4. Request new verification
5. Contact admin if persistent

---

## Data & Export Issues {comprehensive}

### Export Fails or Empty

#### Diagnostic Matrix

| Symptom | Cause | Solution |
|---------|-------|----------|
| **CSV empty** | No records exist | Create records first |
| **Photos missing** | No media fields | Check template design |
| **Export hangs** | Large dataset | Export in batches |
| **Format error** | Special characters | Clean data first |
| **Permission denied** | Insufficient role | Request Viewer role minimum |

### Data Not Saving

#### Immediate Actions
1. **Check network connection**
2. **Look for error messages**
3. **Try saving again**
4. **Copy data to clipboard**
5. **Screenshot as backup**

#### Root Causes
- Network interruption
- Session timeout
- Validation failures
- Server issues
- Browser crashes

### Import Failures

| Error | Meaning | Fix |
|-------|---------|-----|
| **"Invalid format"** | Wrong structure | Match template fields |
| **"Type mismatch"** | Wrong data type | Convert data types |
| **"Required field missing"** | Empty required | Fill required fields |
| **"Duplicate HRID"** | ID exists | Use unique identifiers |

---

## Record Management Issues {important}

### Cannot Edit Records

#### Permission Hierarchy
```
Can edit if:
├─ You created record (in draft)
├─ You have Notebook Admin role
├─ You have Data Collector role (own records)
└─ Record not in "reviewed" status
```

### Record Status Workflow Issues

| From Status | To Status | Who Can Change | Common Issue |
|------------|-----------|---------------|--------------|
| **Draft** | Submitted | Author/Collector | Validation errors |
| **Submitted** | Reviewed | Reviewer only | Wrong role |
| **Reviewed** | Draft | Admin only | Locked status |
| **Any** | Deleted | Owner/Admin | Permission denied |

### Records Not Visible

1. Check filters (may be hiding records)
2. Verify notebook access
3. Check record status
4. Confirm sync completed
5. Look in correct notebook

---

## Synchronisation Issues {comprehensive}

### Offline Sync Problems

#### Mobile App Sync Failures

| Issue | Check | Fix |
|-------|-------|-----|
| **No sync button** | Internet connection | Connect to network |
| **Sync fails** | Server accessibility | Wait and retry |
| **Partial sync** | Storage space | Clear device space |
| **Conflicts** | Multiple edits | Choose version |
| **Data loss** | Sync interrupted | Check local cache |

#### Sync Conflict Resolution

When conflicts occur:
1. **Both versions shown**
2. **Compare differences**
3. **Choose version:**
   - Keep local
   - Keep server
   - Merge manually
4. **Confirm choice**
5. **Document decision**

---

## Performance Issues {comprehensive}

### Slow Loading

#### Performance Optimisation Checklist

- [ ] Clear browser cache
- [ ] Reduce records per page (10 instead of 50)
- [ ] Use filters to limit data
- [ ] Close unnecessary tabs
- [ ] Check network speed
- [ ] Try different browser
- [ ] Disable browser extensions
- [ ] Close unused notebooks

### Browser-Specific Issues

| Browser | Common Issue | Solution |
|---------|-------------|----------|
| **Chrome** | Memory usage | Clear cache regularly |
| **Firefox** | Slow scripts | Update browser |
| **Safari** | Compatibility | Use Chrome/Firefox |
| **Edge** | Extension conflicts | Disable extensions |

---

## Common Error Messages {comprehensive}

### Error Message Decoder

| Error | Meaning | Action |
|-------|---------|--------|
| **"400 Bad Request"** | Invalid data sent | Check form data |
| **"401 Unauthorized"** | Not logged in | Login again |
| **"403 Forbidden"** | No permission | Request access |
| **"404 Not Found"** | Resource deleted | Verify existence |
| **"500 Server Error"** | System issue | Wait and retry |
| **"Network Error"** | Connection lost | Check internet |

---

## Emergency Procedures {important}

### Data Recovery

If data appears lost:
1. **Don't panic** - Data often recoverable
2. **Check filters** - May be hiding data
3. **Check other notebooks** - May be wrong location
4. **Check local storage** - Browser may have cache
5. **Check exports** - Recent backups
6. **Contact admin** - Server backups available

### System Outage

During outage:
1. **Save work locally** (copy to document)
2. **Screenshot important data**
3. **Note time and issues**
4. **Check status page**
5. **Use offline mode** (mobile)
6. **Wait for restoration**

---

## Preventive Measures {important}

### Best Practices Checklist

#### Daily
- [ ] Save work frequently
- [ ] Verify sync status
- [ ] Check email for invitations

#### Weekly
- [ ] Export important data
- [ ] Review permissions
- [ ] Clear browser cache
- [ ] Check for updates

#### Monthly
- [ ] Full data backup
- [ ] Permission audit
- [ ] Remove inactive users
- [ ] Archive completed work

---

## Getting Help {essential}

### Information to Provide

When requesting help, include:

1. **Error message** (exact text or screenshot)
2. **Steps to reproduce** (what you did)
3. **Expected result** (what should happen)
4. **Actual result** (what happened)
5. **Browser/device** (Chrome on Windows, etc.)
6. **Notebook/Team name** (affected resources)
7. **Time of issue** (when it occurred)
8. **Your role** (permissions you have)

### Support Channels

| Channel | Use For | Response Time |
|---------|---------|---------------|
| **System Admin** | Permission issues | Same day |
| **Team Admin** | Team resources | Hours |
| **Help Docs** | How-to questions | Immediate |
| **Community Forum** | Best practices | 1-2 days |

## Cross-References {important}

For general troubleshooting:
→ [Troubleshooting Index](../references/troubleshooting-index.md) - Comprehensive error solutions
→ [Operations Reference](../references/operations-reference.md) - Migration and recovery

For workflow guidance:
→ [Dashboard Patterns](./dashboard-patterns.md) - Parametric workflow recipes
→ [Implementation Patterns](../patterns/implementation-patterns-guide.md) - Best practices

For interface details:
→ [Dashboard Overview](./dashboard-overview.md) - System architecture
→ [Designer Component Mapping](../references/designer-component-mapping.md) - Field name issues

For field-specific issues:
→ [Text Fields](../field-categories/text-fields-v05.md#troubleshooting) - HRID and text issues
→ [Media Fields](../field-categories/media-fields-v05.md#common-issues) - Upload problems
→ [Location Fields](../field-categories/location-fields-v05.md#troubleshooting) - GPS issues
→ [Constraints Reference](../references/constraints-reference.md) - Platform limitations

<!-- concat:boundary:end section="dashboard-troubleshooting" -->