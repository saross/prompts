<!-- concat:boundary:start section="dashboard-patterns" -->
<!-- concat:metadata
document_id: dashboard-patterns
category: workflow_recipes
type: parametric_ui_instructions
customisable: true
last_updated: 2025-09-08
-->

<!-- discovery:metadata
provides: [workflow-recipes, parametric-instructions, best-practices, project-setup]
see-also: [dashboard-overview, teams-interface, notebooks-interface, dashboard-troubleshooting]
-->

# Dashboard Workflow Patterns

<!-- structured:metadata
meta:purpose: workflow-guidance
meta:summary: Parametric UI workflow recipes for common dashboard operations that LLMs can customise for specific contexts.
meta:generates: step-by-step-instructions
meta:requires: [ui-access, appropriate-roles]
meta:version: 3.0.0
meta:document: dashboard_patterns
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Teams Interface](./teams-interface.md) | **Dashboard Patterns** | [Dashboard Troubleshooting →](./dashboard-troubleshooting.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Teams Interface](#teams-interface) | [Dashboard Troubleshooting ↓](#dashboard-troubleshooting) -->

## Overview {essential}

This document provides parametric workflow recipes for common Dashboard operations. Each recipe:
- Contains template markers ({{VARIABLE}}) for customisation
- Provides step-by-step UI instructions
- Includes validation checklists
- Offers troubleshooting guidance

### How to Use These Recipes {essential}

1. Select appropriate recipe for task
2. Replace template markers with actual values
3. Follow steps sequentially
4. Use checklists to verify completion
5. Refer to troubleshooting if issues arise

### Template Marker Reference {essential}

| Marker | Description | Example Value |
|--------|-------------|---------------|
| {{PROJECT_NAME}} | Project identifier | "Pilbara Survey 2025" |
| {{TEAM_NAME}} | Team identifier | "CSIRO Minerals" |
| {{TEAM_SIZE}} | Number of members | "12" |
| {{USER_EMAIL}} | User email address | "researcher@csiro.au" |
| {{NOTEBOOK_NAME}} | Notebook identifier | "Site-A-Records" |
| {{TEMPLATE_NAME}} | Template identifier | "Archaeological-Survey-v2" |
| {{ROLE_NAME}} | Permission role | "Data Collector" |
| {{NUM_SITES}} | Number of locations | "5" |
| {{DATE_RANGE}} | Project timeline | "March-June 2025" |

---

## Recipe 1: Complete Project Setup {essential}

**Purpose**: Set up a new field research project from scratch

### Parameters
- {{PROJECT_TYPE}}: Type of research (e.g., "Archaeological", "Geological", "Ecological")
- {{PROJECT_NAME}}: Full project name
- {{PROJECT_ABBREV}}: Short code (e.g., "PS2025")
- {{TEAM_SIZE}}: Number of team members
- {{NUM_SITES}}: Number of collection sites
- {{START_DATE}}: Project start date

### Prerequisites
- [ ] Organisation Administrator or System Administrator role
- [ ] List of team member emails
- [ ] Template design completed or selected
- [ ] Site list prepared

### Steps

#### Phase 1: Team Creation
1. Navigate to **Teams** section
2. Click **Create Team** button
3. Enter details:
   - Name: "{{PROJECT_NAME}} Team"
   - Description: "{{PROJECT_TYPE}} research project running {{DATE_RANGE}}"
4. Click **Create**
5. ✓ Team created and visible in list

#### Phase 2: Add Team Members
6. Open team: Click **{{TEAM_NAME}}** from Teams list
7. Go to **Users** tab
8. For each of {{TEAM_SIZE}} members:
   - Click **Add User**
   - Enter email: {{USER_EMAIL}}
   - Select role:
     - Project leads → Team Administrator
     - Others → Team Member
   - Click **Add User**
9. ✓ All members added to team

#### Phase 3: Create or Select Template
10. Go to **Templates** tab
11. Either:
    - **Option A**: Click existing "{{TEMPLATE_NAME}}"
    - **Option B**: Click **Create Template** → Design new
12. If creating new:
    - Name: "{{PROJECT_ABBREV}}-Template"
    - Build in Designer
    - Include HRID field: "{{PROJECT_ABBREV}}-{{_YYYY}}-{{auto_increment}}"
    - Save template
13. ✓ Template ready for deployment

#### Phase 4: Deploy Notebooks
14. Go to **Notebooks** tab
15. For each of {{NUM_SITES}} sites:
    - Click **Create Notebook**
    - Name: "{{PROJECT_ABBREV}}-Site-{{SITE_ID}}"
    - Select template: {{TEMPLATE_NAME}}
    - Team ownership: Auto-assigned
    - Click **Create**
16. ✓ All notebooks deployed

#### Phase 5: Configure Permissions
17. For each notebook:
    - Open notebook
    - Go to **Users** tab
    - Verify team members have access
    - Adjust roles if needed:
      - Site supervisors → Notebook Administrator
      - Field workers → Data Collector
      - QA staff → Data Reviewer
18. ✓ Permissions configured

### Validation Checklist
- [ ] Team visible in Teams list
- [ ] All {{TEAM_SIZE}} members added
- [ ] Template includes HRID field
- [ ] {{NUM_SITES}} notebooks created
- [ ] All notebooks show team ownership
- [ ] Export test successful
- [ ] Sample record creation works

### Troubleshooting
- **Can't create team**: Need Organisation Administrator role
- **Members not receiving invites**: Check spam folders
- **Template won't save**: Check for required HRID field
- **Notebooks not visible**: Refresh page or check filters

---

## Recipe 2: Bulk User Onboarding {important}

**Purpose**: Add multiple users to existing project infrastructure

### Parameters
- {{NUM_USERS}}: Number of new users
- {{DEFAULT_ROLE}}: Standard role assignment
- {{NOTEBOOK_LIST}}: Notebooks requiring access
- {{TRAINING_NOTEBOOK}}: Practice notebook name

### Prerequisites
- [ ] Notebook Administrator role for target notebooks
- [ ] User email list prepared
- [ ] Roles determined for each user
- [ ] Training materials ready

### Steps

#### Phase 1: Prepare User List
1. Create spreadsheet with:
   - Column A: Email addresses
   - Column B: Display names
   - Column C: Intended role
   - Column D: Notebook assignments
2. ✓ User data organised

#### Phase 2: Send Invitations
3. For each notebook in {{NOTEBOOK_LIST}}:
   - Navigate to notebook
   - Go to **Invites** tab
   - For each of {{NUM_USERS}} users:
     - Click **Invite User**
     - Enter email from list
     - Select role: {{DEFAULT_ROLE}}
     - Add message: "Welcome to {{PROJECT_NAME}}. Training notebook: {{TRAINING_NOTEBOOK}}"
     - Click **Send Invitation**
4. ✓ All invitations sent

#### Phase 3: Monitor Acceptance
5. Daily for next 7 days:
   - Check **Invites** tab
   - Note accepted invitations
   - Resend expired invitations
   - Follow up via email if needed
6. ✓ All users accepted invitations

#### Phase 4: Verify Access
7. For each notebook:
   - Go to **Users** tab
   - Confirm all {{NUM_USERS}} appear
   - Verify correct roles assigned
8. ✓ Access verified

### Validation Checklist
- [ ] All {{NUM_USERS}} invited
- [ ] Acceptance rate >90%
- [ ] Users appear in Users tab
- [ ] Roles correctly assigned
- [ ] Users can access notebooks
- [ ] Training notebook accessible

---

## Recipe 3: Template Version Migration {important}

**Purpose**: Migrate notebooks to updated template version

### Parameters
- {{OLD_VERSION}}: Current template version
- {{NEW_VERSION}}: Target template version
- {{NUM_NOTEBOOKS}}: Notebooks to migrate
- {{BREAKING_CHANGES}}: List of incompatible changes
- {{MIGRATION_DATE}}: Planned migration date

### Prerequisites
- [ ] New template version tested
- [ ] Breaking changes documented
- [ ] User communication sent
- [ ] Backup exports completed

### Steps

#### Phase 1: Preparation
1. Export all data from current notebooks:
   - Open each notebook
   - Go to **Records** tab
   - Click **Export** → CSV
   - Click **Export** → Photo Archive
2. Document current template:
   - Go to **Templates**
   - Open {{OLD_VERSION}}
   - Click **Export** → Download JSON
3. ✓ Backups complete

#### Phase 2: Create New Template
4. Go to **Templates**
5. Click **Create Template**
6. Either:
   - Upload modified JSON
   - Clone and modify existing
7. Name: "{{TEMPLATE_NAME}}-{{NEW_VERSION}}"
8. Test thoroughly in separate notebook
9. ✓ New template validated

#### Phase 3: Deploy New Notebooks
10. For each of {{NUM_NOTEBOOKS}}:
    - Create new notebook with {{NEW_VERSION}}
    - Name: "{{ORIGINAL_NAME}}-v{{NEW_VERSION}}"
    - Configure same permissions
11. ✓ New notebooks ready

#### Phase 4: Data Migration
12. If compatible structure:
    - Import CSV data to new notebooks
    - Verify data integrity
13. If breaking changes:
    - Manual data transfer required
    - Document transformation rules
14. ✓ Data migrated

#### Phase 5: Cutover
15. On {{MIGRATION_DATE}}:
    - Archive old notebooks
    - Redirect users to new versions
    - Monitor for issues
16. ✓ Migration complete

### Validation Checklist
- [ ] All data exported from old notebooks
- [ ] New template thoroughly tested
- [ ] {{NUM_NOTEBOOKS}} new notebooks created
- [ ] Data successfully migrated
- [ ] Users can access new notebooks
- [ ] Old notebooks archived

---

## Recipe 4: Multi-Site Coordination {comprehensive}

**Purpose**: Manage distributed data collection across multiple locations

### Parameters
- {{NUM_SITES}}: Number of sites
- {{SITE_TEAMS}}: Teams per site
- {{CENTRAL_TEAM}}: Coordinating team
- {{SYNC_FREQUENCY}}: Data sync schedule
- {{REPORTING_SCHEDULE}}: Progress report timing

### Prerequisites
- [ ] Site list with team assignments
- [ ] Network connectivity plan
- [ ] Data standards documented
- [ ] Communication channels established

### Steps

#### Phase 1: Structure Setup
1. Create central team:
   - Name: "{{PROJECT_NAME}}-Central"
   - Add coordination staff
2. For each of {{NUM_SITES}}:
   - Create site team: "{{PROJECT_NAME}}-{{SITE_ID}}"
   - Add site personnel
3. ✓ Team structure created

#### Phase 2: Template Standardisation
4. Create master template in central team
5. Share with all site teams:
   - Each team clones template
   - No modifications allowed
6. ✓ Consistent templates deployed

#### Phase 3: Notebook Deployment
7. Each site team creates notebooks:
   - "{{SITE_ID}}-Daily-Records"
   - "{{SITE_ID}}-Samples"
   - "{{SITE_ID}}-Photos"
8. ✓ All notebooks operational

#### Phase 4: Cross-Site Access
9. Grant central team members viewer access:
   - Add to each site notebook
   - Role: Data Viewer
10. Create summary notebook for aggregation
11. ✓ Central oversight enabled

#### Phase 5: Synchronisation Protocol
12. Establish {{SYNC_FREQUENCY}} sync:
    - Sites export data
    - Upload to central repository
    - Central team validates
    - Feedback provided
13. ✓ Sync protocol active

### Validation Checklist
- [ ] {{NUM_SITES}} site teams created
- [ ] All using identical template
- [ ] Central team has viewer access
- [ ] Sync tested successfully
- [ ] Communication channels work
- [ ] First report generated

---

## Recipe 5: Permission Audit {comprehensive}

**Purpose**: Review and update all user permissions across project

### Parameters
- {{AUDIT_SCOPE}}: Teams, notebooks, or both
- {{USER_COUNT}}: Total users to review
- {{INACTIVE_THRESHOLD}}: Days before marking inactive
- {{REVIEW_FREQUENCY}}: How often to audit

### Steps

#### Phase 1: Generate Reports
1. For each team in {{AUDIT_SCOPE}}:
   - Go to **Users** tab
   - Screenshot or export member list
2. For each notebook:
   - Go to **Users** tab
   - Document all users and roles
3. ✓ Current state documented

#### Phase 2: Review Activity
4. For each user:
   - Check last activity date
   - Mark if >{{INACTIVE_THRESHOLD}} days
   - Note unusual permission levels
5. ✓ Activity reviewed

#### Phase 3: Update Permissions
6. Remove inactive users:
   - Select user
   - Click remove/trash icon
   - Confirm removal
7. Adjust incorrect roles:
   - Click current role
   - Select correct role
   - Save changes
8. ✓ Permissions updated

#### Phase 4: Documentation
9. Create audit report:
   - Users removed: count and names
   - Roles changed: before/after
   - Recommendations for future
10. Schedule next audit: {{REVIEW_FREQUENCY}}
11. ✓ Audit complete

### Validation Checklist
- [ ] All teams reviewed
- [ ] All notebooks reviewed
- [ ] Inactive users removed
- [ ] Roles match responsibilities
- [ ] Report generated
- [ ] Next audit scheduled

---

## Recipe 6: Emergency Data Recovery {comprehensive}

**Purpose**: Recover from data loss or corruption

### Parameters
- {{AFFECTED_NOTEBOOK}}: Corrupted notebook
- {{LAST_BACKUP}}: Most recent export
- {{RECOVERY_METHOD}}: Restore or rebuild
- {{DATA_LOSS_WINDOW}}: Time since backup

### Prerequisites
- [ ] Regular backups exist
- [ ] System Administrator access
- [ ] Users notified of issue
- [ ] Recovery window scheduled

### Steps

#### Phase 1: Assessment
1. Document the issue:
   - What data is affected
   - When corruption noticed
   - Last known good state
2. Check available backups:
   - CSV exports
   - Photo archives
   - JSON templates
3. ✓ Damage assessed

#### Phase 2: Preparation
4. Create recovery notebook:
   - Name: "{{AFFECTED_NOTEBOOK}}-Recovery"
   - Same template version
   - Do not delete original yet
5. ✓ Recovery environment ready

#### Phase 3: Data Restoration
6. Import from {{LAST_BACKUP}}:
   - Upload CSV data
   - Restore photo archive
   - Verify record counts
7. Identify gap: {{DATA_LOSS_WINDOW}}
8. ✓ Bulk data restored

#### Phase 4: Gap Recovery
9. For missing records:
   - Check user local storage
   - Review email notifications
   - Contact recent users
   - Manually recreate if possible
10. ✓ Gap minimised

#### Phase 5: Validation
11. Compare restored vs original:
    - Record counts
    - User access
    - Data integrity
12. When satisfied:
    - Archive corrupted notebook
    - Rename recovery to original
13. ✓ Recovery complete

### Validation Checklist
- [ ] All backup data imported
- [ ] Gap period addressed
- [ ] Users can access notebook
- [ ] Data integrity verified
- [ ] Original archived safely
- [ ] Incident documented

---

## Recipe 7: Project Handover {important}

**Purpose**: Transfer project ownership and knowledge

### Parameters
- {{OUTGOING_ADMIN}}: Departing administrator
- {{INCOMING_ADMIN}}: New administrator
- {{HANDOVER_PERIOD}}: Transition timeline
- {{PROJECT_RESOURCES}}: List of owned resources

### Steps

#### Phase 1: Access Grant
1. Add {{INCOMING_ADMIN}} to all teams:
   - Grant Team Administrator role
2. Add to all notebooks:
   - Grant Notebook Administrator role
3. ✓ Full access provided

#### Phase 2: Knowledge Transfer
4. Document:
   - Project workflows
   - Template modifications
   - Known issues
   - User contacts
5. Schedule training sessions
6. ✓ Knowledge documented

#### Phase 3: Transition Period
7. For {{HANDOVER_PERIOD}}:
   - Both admins active
   - Incoming shadows outgoing
   - Questions addressed
8. ✓ Transition complete

#### Phase 4: Access Removal
9. Downgrade {{OUTGOING_ADMIN}}:
   - To Team Member or remove
   - To Data Viewer or remove
10. Update documentation
11. ✓ Handover finalised

### Validation Checklist
- [ ] New admin has all access
- [ ] Documentation complete
- [ ] Training provided
- [ ] Old admin removed/downgraded
- [ ] Team notified
- [ ] No access gaps

---

## Best Practices Summary {important}

### Planning
- Document all workflows before starting
- Test with small group first
- Have rollback plan ready
- Communicate changes clearly

### Execution
- Follow steps sequentially
- Verify each phase before proceeding
- Document deviations
- Keep audit trail

### Validation
- Use checklists consistently
- Test with real users
- Verify data integrity
- Confirm permissions work

### Maintenance
- Regular audits (monthly/quarterly)
- Keep documentation updated
- Archive old resources
- Monitor system health

## Cross-References {important}

For interface details:
→ [Dashboard Overview](./dashboard-overview.md)

For specific components:
→ [Templates Interface](./templates-interface.md)
→ [Notebooks Interface](./notebooks-interface.md)
→ [Users Interface](./users-interface.md)
→ [Teams Interface](./teams-interface.md)

For troubleshooting:
→ [Dashboard Troubleshooting](./dashboard-troubleshooting.md)

<!-- concat:boundary:end section="dashboard-patterns" -->