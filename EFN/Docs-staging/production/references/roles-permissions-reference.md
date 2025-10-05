<!-- concat:boundary:start section="roles-permissions" -->
<!-- concat:metadata
document_id: roles-permissions
category: reference
type: permission-model
last_updated: 2025-01-08
-->

<!-- discovery:metadata
provides: [role-definitions, permission-matrix, inheritance-model, administration-guide]
requires: [dashboard-access, user-management]
see-also: [users-interface, teams-interface, notebooks-interface, glossary, llm-navigation-manifest]
-->

<!-- structured:metadata
meta:purpose: permission-reference
meta:audience: [administrators, notebook-creators, documentation]
meta:priority: essential
meta:complexity: comprehensive
meta:version: 1.0.0
meta:document: roles_permissions_reference
meta:depth-tags: [essential, important, comprehensive]
-->

# Roles and Permissions Reference

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Glossary](./glossary.md) | **Roles & Permissions** | [Navigation Manifest →](./llm-navigation-manifest.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Glossary](#glossary) | [Navigation Manifest ↓](#llm-navigation-manifest) -->

## Overview {essential}

Fieldmark implements a three-tier permission model with role inheritance and virtual role mapping. Understanding this system is essential for project administration and user management.

### Permission Hierarchy {essential}
```
Global Roles (System-wide)
    ↓
Team Roles (Per team)
    ↓
Notebook Roles (Per notebook/project)
```

### Key Concepts {essential}

| Concept | Description | Example |
|---------|-------------|---------|
| **Direct Assignment** | Roles explicitly granted to users | User gets PROJECT_ADMIN on Notebook A |
| **Role Inheritance** | Higher roles include lower role permissions | PROJECT_ADMIN inherits PROJECT_MANAGER |
| **Virtual Roles** | Automatic roles from team membership | TEAM_MEMBER gets PROJECT_CONTRIBUTOR on team notebooks |
| **Permission Override** | More specific roles override general ones | PROJECT_ADMIN overrides TEAM_MEMBER |

### Terminology Alignment

| UI Term | Code Term | Description |
|---------|-----------|-------------|
| **Notebook** | Project | Data collection instance |
| **Template** | Template | Reusable notebook design |
| **Editor/Designer** | UI Specification | Notebook structure definition |
| **Records** | Project Records | Collected data entries |
| **Create Notebook** | CREATE_PROJECT | Action to make new notebook |
| **Edit Notebook** | UPDATE_PROJECT_UISPEC | Action to modify structure |

---

## 1. Global Roles (System-wide) {essential}

Global roles apply across the entire Fieldmark system and are managed through the Dashboard Users interface.

### 📍 Dashboard Administration Location
**Navigate to**: Dashboard → Users → [Select User] → System Roles  
**Who can modify**: GENERAL_ADMIN only  
**Interface**: Checkbox or dropdown selection per role

### GENERAL_USER (Default Role) {essential}

**Automatic for**: All registered users  
**Purpose**: Basic system access  
**Dashboard indicator**: No special badge (default)

#### Permissions
- View lists of accessible notebooks and templates
- Create and manage own API tokens (long-lived tokens)
- Verify email address
- View own user profile

#### Cannot
- Create new notebooks or templates
- Access system administration
- Modify other users

#### Common Use Case
Every user has this role automatically. Field data collectors typically have GENERAL_USER + notebook-specific roles.

### GENERAL_CREATOR (Content Creator) {essential}

**Purpose**: Create notebooks and templates  
**Dashboard indicator**: "{{CREATOR_BADGE_TEXT}}" badge  
**Assignment**: Manual by administrator

#### Additional Permissions
- ✅ **CREATE new notebooks** anywhere in system
- ✅ **CREATE new templates** anywhere in system  
- List all templates in system
- Convert notebooks to templates

#### Inherits From
- GENERAL_USER (all basic permissions)

#### Common Use Case
```
{{RESEARCHER_NAME}} needs to design data collection forms.
Grant: GENERAL_CREATOR
Result: Can create notebooks and templates globally
```

#### Dashboard Creation Paths
- **Create Notebook**: Home → Create Notebook button
- **Create Template**: Templates → Create Template button

### GENERAL_ADMIN (System Administrator) {essential}

**Purpose**: Complete system control  
**Dashboard indicator**: "{{ADMIN_BADGE_TEXT}}" badge (often {{ADMIN_BADGE_COLOR}})  
**Assignment**: Manual by existing GENERAL_ADMIN only

#### Exclusive Permissions
- **User Management**
  - View all users in system
  - Add/remove any global role
  - Reset any user password  
  - Delete users permanently
  - View user activity logs

- **System Operations**
  - Initialize system API
  - Restore from backups
  - Validate databases
  - Send test emails
  - View system logs

- **Team Administration**
  - Create teams without restrictions
  - Add/remove team administrators (exclusive)
  - Delete any team

- **Override Permissions**
  - ✅ **EDIT any notebook** structure or content
  - ✅ **DELETE any notebook** regardless of ownership
  - ✅ **ACCESS all notebooks** without invitation
  - Manage any user's API tokens

#### Inherits From
- GENERAL_CREATOR (creation permissions)
- All PROJECT_ADMIN permissions (on every notebook)
- All TEAM_ADMIN permissions (on every team)
- All TEMPLATE_ADMIN permissions (on every template)

#### Dashboard Administration Paths
- **User Management**: Dashboard → Users
- **System Settings**: Dashboard → Settings (if available)
- **All Notebooks**: Dashboard → Notebooks (sees all)

#### Security Note
⚠️ This role has unrestricted access. Limit to {{MAX_ADMINS}} users maximum.

---

## 2. Team Roles (Team-specific) {important}

Team roles simplify permission management by automatically granting notebook access to team members.

### 📍 Dashboard Administration Location
**Navigate to**: Dashboard → Teams → [Select Team] → Users tab  
**Who can modify**: TEAM_ADMIN, TEAM_MANAGER (limited), GENERAL_ADMIN  
**Interface**: Add User button → Role dropdown

### How Team Roles Work {essential}

```
User joins team with role
    ↓
Automatically receives "virtual roles"
    ↓
Gets permissions on all team resources
```

### TEAM_MEMBER (Team Contributor) {important}

**Purpose**: Contribute data to team notebooks  
**Dashboard indicator**: "Member" in team user list  
**Assignment**: Via team invitation or direct add

#### Direct Permissions
- View team details and description
- View team member list
- Access team templates

#### Virtual Roles Granted
| Resource Type | Virtual Role | Result |
|--------------|--------------|--------|
| Team Notebooks | PROJECT_CONTRIBUTOR | Can view/edit all records |
| Team Templates | TEMPLATE_GUEST | Can view/use templates |

#### Common Use Case
```
{{FIELD_WORKER}} joins {{TEAM_NAME}}
Role: TEAM_MEMBER
Result: Automatically can contribute to all team notebooks
```

### TEAM_MEMBER_CREATOR (Creative Team Member) {important}

**Purpose**: Create new notebooks within team  
**Dashboard indicator**: "Member (Creator)" in team list  
**Assignment**: Special variant of team member

#### Additional Permissions
- ✅ **CREATE notebooks** within the team
- Does NOT automatically access all team notebooks

#### Use Case
Team member who creates project-specific notebooks but doesn't need access to all team data.

### TEAM_MANAGER (Team Manager) {important}

**Purpose**: Manage team resources and membership  
**Dashboard indicator**: "{{MANAGER_BADGE_TEXT}}" badge in team list  
**Assignment**: By TEAM_ADMIN or GENERAL_ADMIN

#### Direct Permissions
- Update team details (name, description)
- ✅ **CREATE notebooks** in team
- ✅ **CREATE templates** in team
- Add/remove team members
- Manage member and manager invitations
- View all team invitations

#### Virtual Roles Granted
| Resource Type | Virtual Role | Result |
|--------------|--------------|--------|
| Team Notebooks | PROJECT_MANAGER | Can edit notebook structure |
| Team Templates | TEMPLATE_GUEST | Can view/use templates |

#### Cannot
- Delete team
- Add/remove team administrators

#### Dashboard Management Paths
- **Add Members**: Team → Users tab → Add User
- **Create Notebook**: Team → Notebooks tab → Create Notebook
- **Manage Invites**: Team → Invites tab

### TEAM_ADMIN (Team Administrator) {important}

**Purpose**: Full team control  
**Dashboard indicator**: "{{TEAM_ADMIN_BADGE_TEXT}}" badge in team list  
**Assignment**: By GENERAL_ADMIN only

#### Additional Permissions
- ✅ **DELETE team** (if no resources)
- Add/remove team managers
- Full control over team settings

#### Virtual Roles Granted
| Resource Type | Virtual Role | Result |
|--------------|--------------|--------|
| Team Notebooks | PROJECT_ADMIN | Full notebook control |
| Team Templates | TEMPLATE_ADMIN | Full template control |

#### Inherits From
- TEAM_MANAGER (all management permissions)

---

## 3. Notebook (Project) Roles {important}

Notebook roles provide granular permissions for specific data collection instances.

### 📍 Dashboard Administration Location
**Navigate to**: Dashboard → Notebooks → [Select Notebook] → Users tab  
**Who can modify**: PROJECT_ADMIN, PROJECT_MANAGER (limited), GENERAL_ADMIN  
**Interface**: Invite User button → Role selection

### PROJECT_GUEST (Notebook Guest) {important}

**Purpose**: Limited data contribution  
**Dashboard indicator**: "Guest" in notebook user list  
**Use case**: External collaborators with restricted access

#### Permissions
- View notebook metadata
- Create own records
- View/edit/delete ONLY own records
- Cannot see other users' data

### PROJECT_CONTRIBUTOR (Data Collector) {essential}

**Purpose**: Standard field data collection  
**Dashboard indicator**: "Contributor" in notebook user list  
**Most common role**: For field workers

#### Additional Permissions
- View ALL records in notebook
- Edit ALL records (including others')
- Delete ALL records
- Export own data
- Bulk operations on records

#### Inherits From
- PROJECT_GUEST (own record management)

### PROJECT_MANAGER (Notebook Manager) {important}

**Purpose**: Manage notebook configuration  
**Dashboard indicator**: "Manager" in notebook user list

#### Additional Permissions
- ✅ **EDIT notebook details** (name, description)
- ✅ **EDIT notebook structure** (UPDATE_PROJECT_UISPEC)
- Change notebook status (open/closed)
- Export all notebook data
- Manage all invitations (except admin)
- Add/remove users (except admins)

#### Dashboard Management Paths
- **Edit Structure**: Notebook → Edit/Designer button
- **Manage Users**: Notebook → Users tab
- **Export Data**: Notebook → Records → Export

#### Inherits From
- PROJECT_CONTRIBUTOR (all data permissions)

### PROJECT_ADMIN (Notebook Administrator) {essential}

**Purpose**: Full notebook control  
**Dashboard indicator**: "Administrator" in notebook user list

#### Additional Permissions
- ✅ **DELETE entire notebook**
- Add/remove notebook administrators
- Generate test/debug records
- Change notebook team ownership
- Access audit logs

#### Inherits From
- PROJECT_MANAGER (all management permissions)

---

## 4. Permission Quick Reference {essential}

### Who Can Create Notebooks?

| Role | Create Anywhere | Create in Team | Dashboard Location |
|------|----------------|----------------|-------------------|
| GENERAL_ADMIN | ✅ | ✅ | Home → Create Notebook |
| GENERAL_CREATOR | ✅ | ✅* | Home → Create Notebook |
| TEAM_MANAGER | ❌ | ✅ | Team → Notebooks → Create |
| TEAM_MEMBER_CREATOR | ❌ | ✅ | Team → Notebooks → Create |
| TEAM_MEMBER | ❌ | ❌ | No create button visible |
| GENERAL_USER | ❌ | ❌ | No create button visible |

*If also has team role

### Who Can Edit Notebook Structure?

| Role | Edit Any | Edit Team Notebooks | Edit Assigned | Dashboard Location |
|------|----------|---------------------|---------------|-------------------|
| GENERAL_ADMIN | ✅ | ✅ | ✅ | Notebook → Edit |
| PROJECT_MANAGER | ❌ | ❌ | ✅ | Notebook → Edit |
| PROJECT_ADMIN | ❌ | ❌ | ✅ | Notebook → Edit |
| TEAM_MANAGER | ❌ | ✅ (virtual) | ❌ | Notebook → Edit |
| TEAM_ADMIN | ❌ | ✅ (virtual) | ❌ | Notebook → Edit |

### Who Can Delete Notebooks?

| Role | Delete Any | Delete Team | Delete Assigned | Dashboard Location |
|------|------------|-------------|-----------------|-------------------|
| GENERAL_ADMIN | ✅ | ✅ | ✅ | Notebook → Settings → Delete |
| PROJECT_ADMIN | ❌ | ❌ | ✅ | Notebook → Settings → Delete |
| TEAM_ADMIN | ❌ | ✅ | ❌ | Notebook → Settings → Delete |

---

## 5. Common Permission Scenarios {important}

### Scenario: Research Team Setup
```
Team: {{RESEARCH_TEAM}}
Team Leader: {{TEAM_LEADER}}
Researchers: {{NUM_RESEARCHERS}}
Field Workers: {{NUM_FIELD_WORKERS}}

Roles:
- Team Leader: GENERAL_CREATOR + TEAM_ADMIN
  → Can create notebooks and fully manage team

- Researchers: GENERAL_CREATOR + TEAM_MANAGER  
  → Can create/edit notebooks within team

- Field Workers: GENERAL_USER + TEAM_MEMBER
  → Can contribute data to all team notebooks
```

### Scenario: External Collaboration
```
External Partner: {{PARTNER_ORG}}
Shared Notebook: {{NOTEBOOK_NAME}}

Roles:
- Partner Users: GENERAL_USER + PROJECT_GUEST on specific notebook
  → Can only see and edit their own records

- Partner Supervisor: GENERAL_USER + PROJECT_CONTRIBUTOR
  → Can see all data but not change structure
```

### Scenario: Template Designer
```
Designer: {{DESIGNER_NAME}}
Purpose: Create reusable templates for organisation

Roles:
- GENERAL_CREATOR (global)
- TEMPLATE_ADMIN on created templates
  → Can create and modify template library
```

---

## 6. Template Permissions {comprehensive}

### Template Roles

| Role | Permissions | Dashboard Location |
|------|-------------|-------------------|
| TEMPLATE_ADMIN | Full control, edit, delete | Templates → [Template] → Settings |
| TEMPLATE_GUEST | View and use only | Templates list |

### Who Can Create Templates?

| Role | Create Anywhere | Create in Team |
|------|----------------|----------------|
| GENERAL_ADMIN | ✅ | ✅ |
| GENERAL_CREATOR | ✅ | ✅* |
| TEAM_MANAGER | ❌ | ✅ |

*If has appropriate team role

---

## 7. Troubleshooting Permissions {important}

### Common Issues and Solutions

| Problem | Likely Cause | Solution | Check Location |
|---------|--------------|----------|----------------|
| "Can't create notebook" | Missing GENERAL_CREATOR | Grant GENERAL_CREATOR role | Users → [User] → Roles |
| "Can't edit notebook structure" | Missing PROJECT_MANAGER | Add as notebook manager | Notebook → Users |
| "Can't see team notebooks" | Not team member | Add to team | Team → Users → Add |
| "Can't delete notebook" | Need PROJECT_ADMIN | Upgrade notebook role | Notebook → Users |
| "Can't add team admin" | Need GENERAL_ADMIN | Only system admin can do this | Contact system admin |

### Permission Debugging Checklist

1. Check global roles: Dashboard → Users → [User]
2. Check team membership: Teams → [Team] → Users
3. Check notebook roles: Notebooks → [Notebook] → Users
4. Check virtual roles from teams
5. Verify email is confirmed (some features restricted)

---

## 8. API Token Permissions {comprehensive}

Long-lived tokens inherit the permissions of the user who created them:

| Token Creator Role | Token Permissions |
|-------------------|-------------------|
| GENERAL_USER | Basic read access only |
| GENERAL_CREATOR | Can create resources via API |
| GENERAL_ADMIN | Full API access |

### Token Management

- Users: Can create/revoke own tokens
- GENERAL_ADMIN: Can manage any user's tokens
- Dashboard: Users → [User] → API Tokens

---

## 9. Special Cases and Edge Conditions {comprehensive}

### Orphaned Notebooks
- Notebooks without team ownership
- Only PROJECT roles apply (no team virtual roles)
- GENERAL_ADMIN can reassign to team

### Permission Conflicts
Resolution order (highest priority first):
1. Direct notebook role (PROJECT_*)
2. Team virtual role (from TEAM_*)
3. Global permissions (GENERAL_*)

### Cross-Team Scenarios
- Users can belong to multiple teams
- Each team's virtual roles apply independently
- No permission inheritance between teams

---

## Cross-References {important}

For UI details:
→ [Users Interface](../dashboard/users-interface.md) - System role management
→ [Teams Interface](../dashboard/teams-interface.md) - Team role management  
→ [Notebooks Interface](../dashboard/notebooks-interface.md) - Notebook role management

For concepts:
→ [Glossary](./glossary.md) - Role and permission definitions
→ [Dashboard Patterns](../dashboard/dashboard-patterns.md) - Permission management workflows

For operations requiring permissions:
→ {{cross-ref:editor-form-settings}} - Editor access requires PROJECT_CONTRIBUTOR
→ {{cross-ref:editor-notebook-info}} - Metadata editing requires PROJECT_MANAGER
→ [Operations Reference](./operations-reference.md) - Import/export requires PROJECT_MANAGER
→ {{cross-ref:notebook-templates}} - Template creation requires GENERAL_CREATOR or TEMPLATE_CREATOR

---

## Complete Action Reference {comprehensive}

### Project (Notebook) Actions

| Action | Required Role | Description | UI/API |
|--------|---------------|-------------|--------|
| CREATE_PROJECT | GENERAL_CREATOR or TEAM_MANAGER | Create new notebook | Both |
| UPDATE_PROJECT_UISPEC | PROJECT_MANAGER | Edit notebook structure | Both |
| DELETE_PROJECT | PROJECT_ADMIN | Delete entire notebook | Both |
| READ_ALL_PROJECT_RECORDS | PROJECT_CONTRIBUTOR | View all data | Both |
| EXPORT_PROJECT_DATA | PROJECT_MANAGER | Export all records | Both |
| VIEW_PROJECT_INVITES | PROJECT_MANAGER | View pending invites | Both |
| CREATE_PROJECT_INVITES | PROJECT_MANAGER | Send notebook invitations | Both |
| REVOKE_PROJECT_INVITES | PROJECT_MANAGER | Cancel pending invites | Both |
| CHANGE_PROJECT_STATUS | PROJECT_ADMIN | Close/reopen notebook | API |
| REASSIGN_PROJECT_TEAM | PROJECT_ADMIN | Change notebook team ownership | API |
| GENERATE_RANDOM_PROJECT_RECORDS | PROJECT_ADMIN + DEVELOPER_MODE | Generate test data | API |

### Team Actions

| Action | Required Role | Description | UI/API |
|--------|---------------|-------------|--------|
| CREATE_TEAM | GENERAL_ADMIN | Create new team | Both |
| DELETE_TEAM | TEAM_ADMIN | Delete team (soft delete) | Both |
| ADD_ADMIN_TO_TEAM | GENERAL_ADMIN only | Appoint team admin | Both |
| CREATE_PROJECT_IN_TEAM | TEAM_MANAGER | Create team notebook | Both |
| VIEW_TEAM_DETAILS | TEAM_MEMBER | View team information | Both |
| VIEW_TEAM_INVITES | TEAM_MANAGER | View pending team invites | Both |
| CREATE_TEAM_INVITES | TEAM_MANAGER | Send team invitations | Both |
| REVOKE_TEAM_INVITES | TEAM_MANAGER | Cancel team invites | Both |
| MANAGE_TEAM_MEMBERS | TEAM_MANAGER | Add/remove team members | Both |

### User & Authentication Actions

| Action | Required Role | Description | UI/API |
|--------|---------------|-------------|--------|
| ADD_OR_REMOVE_GLOBAL_USER_ROLE | GENERAL_ADMIN | Manage system roles | Both |
| DELETE_USER | GENERAL_ADMIN | Remove user permanently | Both |
| VIEW_USER_LIST | GENERAL_ADMIN | View all system users | Both |
| RESET_USER_PASSWORD | GENERAL_ADMIN | Force password reset | Both |
| VERIFY_EMAIL | GENERAL_USER (self) | Verify email address | Both |
| RESEND_VERIFICATION | GENERAL_USER (self) | Request new verification | Both |

### API Token Actions

| Action | Required Role | Description | UI/API |
|--------|---------------|-------------|--------|
| CREATE_LONG_LIVED_TOKEN | GENERAL_USER | Create API tokens | UI |
| READ_MY_LONG_LIVED_TOKENS | GENERAL_USER | View own tokens | UI |
| EDIT_MY_LONG_LIVED_TOKEN | GENERAL_USER | Update own token details | UI |
| REVOKE_MY_LONG_LIVED_TOKEN | GENERAL_USER | Disable own tokens | UI |
| READ_ANY_LONG_LIVED_TOKENS | GENERAL_ADMIN | View all users' tokens | API |
| EDIT_ANY_LONG_LIVED_TOKEN | GENERAL_ADMIN | Edit any user's tokens | API |
| REVOKE_ANY_LONG_LIVED_TOKEN | GENERAL_ADMIN | Revoke any user's tokens | API |

### System Administration Actions

| Action | Required Role | Description | UI/API |
|--------|---------------|-------------|--------|
| RESTORE_FROM_BACKUP | GENERAL_ADMIN | System restore | API |
| INITIALIZE_ADMIN | First user only | Create initial admin | API |
| VIEW_SYSTEM_LOGS | GENERAL_ADMIN | Access system logs | Both |
| SEND_TEST_EMAIL | GENERAL_ADMIN | Test email configuration | API |
| VALIDATE_DATABASE | GENERAL_ADMIN | Check database integrity | API |

## Virtual Roles & Permission Inheritance {comprehensive}

### Virtual Role Mapping

Virtual roles are automatically assigned based on team membership and provide default permissions on team resources:

| Team Role | Virtual Notebook Role | Automatic Permissions |
|-----------|----------------------|----------------------|
| TEAM_MEMBER | PROJECT_CONTRIBUTOR | Create/edit records in team notebooks |
| TEAM_MANAGER | PROJECT_MANAGER | Manage structure of team notebooks |
| TEAM_ADMIN | PROJECT_ADMIN | Full control of team notebooks |

### Permission Inheritance Hierarchy

```
GENERAL_ADMIN
    ├── Inherits all PROJECT_ADMIN permissions (every notebook)
    ├── Inherits all TEAM_ADMIN permissions (every team)
    └── Inherits all TEMPLATE_ADMIN permissions (every template)

PROJECT_ADMIN
    └── Inherits PROJECT_MANAGER
        └── Inherits PROJECT_CONTRIBUTOR

TEAM_ADMIN
    └── Inherits TEAM_MANAGER
        └── Inherits TEAM_MEMBER
```

### Permission Resolution Order

When a user has multiple roles, permissions are resolved in this order:

1. **Direct notebook role** (highest priority)
   - Explicitly assigned PROJECT_* role
2. **Virtual role from team**
   - Automatic role from team membership
3. **Global system role**
   - GENERAL_* permissions
4. **Inherited permissions**
   - From higher roles in same hierarchy

### Example Permission Scenarios

| Scenario | User Roles | Effective Permission | Reason |
|----------|------------|---------------------|--------|
| User in team + direct role | TEAM_MEMBER + PROJECT_ADMIN | PROJECT_ADMIN | Direct role overrides virtual |
| Admin accessing any notebook | GENERAL_ADMIN | PROJECT_ADMIN | Global admin has full access |
| Team manager creating notebook | TEAM_MANAGER | Can create in team | Team role grants creation |
| Multiple team memberships | TEAM_MEMBER in A, TEAM_ADMIN in B | Different per team | Team roles independent |

---

*Last updated: 2025-01-09 | Based on FAIMS3 codebase analysis*

<!-- concat:boundary:end section="roles-permissions" -->