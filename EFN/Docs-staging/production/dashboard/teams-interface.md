<!-- concat:boundary:start section="teams-interface" -->
<!-- concat:metadata
document_id: teams-interface
category: collaboration
ownership_model: team_based
resource_sharing: true
last_updated: 2025-09-08
-->

<!-- discovery:metadata
provides: [team-management, resource-ownership, member-roles, collaborative-workflows]
see-also: [notebooks-interface, templates-interface, users-interface, dashboard-patterns]
-->

# Teams Interface

<!-- structured:metadata
meta:purpose: collaboration-management
meta:summary: Organisational units for managing shared resources, team members, and collaborative field research projects.
meta:generates: team-structures
meta:requires: [org-admin-role, team-creation]
meta:version: 3.0.0
meta:document: teams_interface
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Users Interface](./users-interface.md) | **Teams Interface** | [Dashboard Patterns →](./dashboard-patterns.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Users Interface](#users-interface) | [Dashboard Patterns ↓](#dashboard-patterns) -->

## Overview {essential}

Teams provide organisational structure for collaborative field research projects. They:
- Own and manage notebooks and templates
- Control member access and permissions
- Facilitate resource sharing
- Streamline project management
- Simplify user onboarding

### Key Benefits {essential}

| Benefit | Description |
|---------|-------------|
| **Centralised Management** | Single point for resource control |
| **Simplified Permissions** | Team-based rather than individual |
| **Resource Sharing** | Templates and notebooks shared automatically |
| **Collaborative Workflows** | Built-in team coordination |
| **Scalable Structure** | Grows with project needs |

## Main Teams List {essential}

### List View Components

| Element | Description | Actions |
|---------|-------------|---------|
| **Filter Bar** | Search teams | Type to filter |
| **Create Team** | New team button | Opens dialog |
| **Team Entries** | Individual teams | Click for details |
| **Pagination** | Navigate list | 10/25/50 per page |

### Team Entry Information

Each team displays:
- Team name
- Description
- Owner (creator)
- Member count
- Creation date
- Last activity

### Example Teams {important}

Common team structures in Fieldmark:

| Team Name | Purpose | Typical Size |
|-----------|---------|--------------|
| CSIRO Mineral Resources | Geological surveys | 10-20 members |
| Fieldmark Demo Team | Training and demos | 5-10 members |
| The Artefact Post | Archaeological recording | 15-25 members |
| Heritage Forum Team | Cultural heritage | 20-30 members |

## Team Creation {essential}

### Creation Requirements

| Requirement | Description |
|-------------|-------------|
| **System Role** | Organisation Admin or higher |
| **Unique Name** | Not used by existing team |
| **Description** | Recommended for clarity |

### Creation Dialog

Simple two-field form:

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| **Team Name** | Yes | Unique identifier | {{TEAM_NAME}} |
| **Description** | No | Purpose and scope | {{TEAM_DESC}} |

```
Teams > Create Team > Enter Details > Create
```

Initial setup:
- Creator becomes Team Administrator
- Team appears in list immediately
- Ready for member additions
- Can own resources immediately

## Individual Team View {important}

Team management interface with five tabs:

### Details Tab {essential}

Static team information:

| Field | Description | Editable |
|-------|-------------|----------|
| **Name** | Team identifier | No |
| **Description** | Team purpose | Yes (Admin) |
| **Created By** | Original creator | No |
| **Created At** | Timestamp | No |
| **Updated At** | Last modification | No |

Edit button available for Team Administrators.

### Invites Tab {important}

Manages team membership invitations:

#### Invitation Process

1. **Send Invitation**
   ```
   Invites > Invite User > Enter Email > Select Role > Send
   ```

2. **Pending State**
   - Shows in invites list
   - Can resend or cancel
   - 7-day expiration

3. **Acceptance**
   - User clicks email link
   - Joins team automatically
   - Appears in Users tab

#### Invite Management

| Status | Description | Actions |
|--------|-------------|---------|
| **Pending** | Awaiting response | Resend, Cancel |
| **Accepted** | User joined | View in Users |
| **Expired** | Time limit passed | Resend |

#### Understanding Team vs Notebook Invites {essential}

**When to use Team Invites:**
- Grant access to ALL team resources (notebooks, templates)
- Provide template access (only available through teams)
- Establish organisational hierarchy
- Manage groups of related notebooks

**When to use Notebook Invites:**
- Grant access to specific notebooks only
- Temporary or limited collaboration
- External users who shouldn't see other team resources
- Fine-grained permission control

**Critical**: Templates can ONLY be accessed through team membership.

#### Virtual Roles - Automatic Access {essential}

Team membership automatically grants virtual roles on ALL team resources:

| Team Role | Virtual Notebook Role | Virtual Template Role | Effect |
|-----------|----------------------|----------------------|--------|
| **Team Member** | PROJECT_CONTRIBUTOR | TEMPLATE_GUEST | Create/edit records in all team notebooks |
| **Team Manager** | PROJECT_MANAGER | TEMPLATE_GUEST | Manage all team notebook structures |
| **Team Admin** | PROJECT_ADMIN | TEMPLATE_ADMIN | Full control of all team resources |

**Example**: Adding someone as Team Member to a team with 5 notebooks automatically grants PROJECT_CONTRIBUTOR on all 5, plus any future notebooks.

#### Permission Requirements for Invites

| Inviting Role | Who Can Send | Notes |
|---------------|--------------|--------|
| Team Member | Team Manager+ | Standard collaboration |
| Team Manager | Team Manager+ | Delegation allowed |
| Team Admin | GENERAL_ADMIN only | Elevation restricted |

#### Best Practices

- **Default to Team Member** role (least privilege)
- **Review team resources** before inviting (user gets access to all)
- **Use team invites** for template access and consistent permissions
- **Use notebook invites** for granular, temporary access
- **Document** admin/manager role assignments

### Notebooks Tab {important}

Team-owned notebooks management:

#### Notebook List Features

| Column | Description | Actions |
|--------|-------------|---------|
| **Name** | Notebook identifier | Click to open |
| **Description** | Purpose | View only |
| **Users** | Member count | View list |
| **Records** | Data count | View records |
| **Created** | Deployment date | Sort by date |

#### Create Notebook from Team

```
Notebooks Tab > Create Notebook
```

Benefits of team creation:
- Automatic team ownership
- Members get immediate access
- Inherits team permissions
- Appears in team notebook list

#### Notebook Creation Dialog

| Field | Required | Auto-filled |
|-------|----------|-------------|
| **Name** | Yes | No |
| **Template** | No* | No |
| **JSON File** | No* | No |
| **Team Owner** | Yes | {{TEAM_NAME}} |

*Select template OR upload JSON OR proceed to Designer

### Templates Tab {important}

Team-owned templates:

#### Template Management

| Action | Permission | Description |
|--------|-----------|-------------|
| **View** | Team Member | See all team templates |
| **Create** | Team Admin | New template for team |
| **Edit** | Team Admin | Modify existing |
| **Clone** | Team Member | Copy for modification |
| **Delete** | Team Admin | Remove if unused |

#### Create Template from Team

```
Templates Tab > Create Template
```

Process:
1. Opens creation dialog
2. Enter template name
3. Optional: Upload JSON
4. Creates with team ownership
5. Available to all members

#### Template Dialog

| Field | Required | Description |
|-------|----------|-------------|
| **Template Name** | Yes | Display name |
| **JSON File** | No | Pre-populate |

Leave JSON blank to start from scratch in Designer.

### Users Tab {important}

Team member management:

#### Member List Display

| Column | Description | Sortable |
|--------|-------------|----------|
| **Name** | Member name | Yes |
| **Email** | Contact | Yes |
| **Roles** | Team permissions | No |
| **Remove** | Delete button | No |

#### Add User Process

```
Users Tab > Add User
```

Add User Dialog:

| Field | Required | Options |
|-------|----------|---------|
| **User Email** | Yes | Valid email |
| **Role** | Yes | Dropdown selection |

#### Team Roles {essential}

Only two team-specific roles:

| Role | Permissions | Use Case |
|------|------------|----------|
| **Team Administrator** | Full team control | Team leaders |
| **Team Member** | Access resources | Researchers |

#### Role Capabilities {comprehensive}

**Team Administrator can:**
- Add/remove members
- Change member roles
- Create team resources
- Edit team details
- Delete team (if empty)

**Team Member can:**
- Access team notebooks
- Use team templates
- View member list
- Clone templates
- Create records

### Edit Tab {important}

Allows team administrators to modify team properties:

#### Editable Fields

| Field | Description | Validation |
|-------|-------------|------------|
| **Team Name** | Display name | Must be unique |
| **Description** | Team purpose and details | Optional, markdown supported |
| **Team Settings** | Configuration options | Based on permissions |

#### Edit Permissions

- Only Team Administrators can access Edit tab
- Changes take effect immediately
- Name changes update all references
- Activity logged for audit trail

#### Edit Process

1. Navigate to team → Edit tab
2. Modify desired fields
3. Click "Save Changes"
4. Confirmation message appears
5. Changes reflected across system

**Note**: Team name changes affect all associated notebooks and templates.

#### Member Management Actions

| Action | Who Can | Process |
|--------|---------|---------|
| **Add Member** | Team Admin | Email invitation |
| **Change Role** | Team Admin | Click role > Select |
| **Remove Member** | Team Admin | Click trash icon |

## Resource Ownership {important}

### Ownership Benefits

Team ownership provides:
- Centralised control
- Persistent access
- Simplified permissions
- Clear accountability
- Easy handover

### Owned Resources

Teams can own:
- **Notebooks**: Data collection instances
- **Templates**: Reusable designs

### Ownership Rules {comprehensive}

1. **Creation Context**
   - Resources created from team inherit ownership
   - Can't transfer existing resources to team
   - Team deletion requires empty resources

2. **Access Control**
   - All team members access team resources
   - Team admins manage all team resources
   - Individual permissions still apply within notebooks

3. **Persistence**
   - Resources remain with team despite member changes
   - Team admin role can be transferred
   - Ownership survives creator departure

## Team Workflows {important}

### Standard Team Setup

1. **Create Team**
   ```
   Teams > Create Team > {{TEAM_NAME}}
   ```

2. **Add Members**
   ```
   Team > Users > Add User > {{EMAIL}} > {{ROLE}}
   ```

3. **Create Template**
   ```
   Team > Templates > Create > Design
   ```

4. **Deploy Notebook**
   ```
   Team > Notebooks > Create > Select Template
   ```

5. **Begin Collection**
   - Members access notebook
   - Create records
   - Collaborate on data

### Team Handover Process {comprehensive}

When team leadership changes:

1. **Add New Administrator**
   - Invite new leader
   - Grant Team Administrator role

2. **Knowledge Transfer**
   - Document team practices
   - Share resource passwords
   - Explain workflows

3. **Transition Period**
   - Both admins active
   - Gradual handover
   - Verify access

4. **Remove Old Administrator**
   - Downgrade to member
   - Or remove entirely

## Best Practices {important}

### Team Structure

```
{{ORGANISATION}}-{{PROJECT}}-{{YEAR}}
Example: CSIRO-Minerals-2025
```

### Team Sizing

| Team Size | Management Overhead | Recommended For |
|-----------|-------------------|-----------------|
| 2-5 members | Minimal | Small surveys |
| 5-15 members | Moderate | Standard projects |
| 15-30 members | Significant | Large expeditions |
| 30+ members | High | Multi-site programs |

### Permission Strategy

1. **Minimal Administrators**
   - 1-2 admins per team
   - Clear succession plan
   - Document decisions

2. **Regular Reviews**
   - Monthly member audit
   - Remove inactive users
   - Update roles as needed

3. **Clear Documentation**
   - Team purpose in description
   - Role responsibilities documented
   - Workflow guides maintained

## Common Issues {comprehensive}

### Team Management Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Can't create team | Wrong system role | Need Org Admin |
| Can't add members | Not team admin | Request elevation |
| Can't see team | Not a member | Request invitation |
| Can't delete team | Has resources | Delete notebooks first |

### Member Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Invitation not received | Email issues | Check spam, resend |
| Wrong role assigned | Selection error | Team admin can change |
| Can't access resources | Permissions | Check notebook roles |
| Removed by mistake | Admin error | Re-invite |

### Resource Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Notebook not visible | Not deployed | Create from team |
| Template locked | Being edited | Wait or contact admin |
| Can't create resources | Member role only | Need admin role |

## Integration with Other Components {important}

### Teams → Notebooks
- Team ownership simplifies permissions
- Members automatically get access
- Centralised notebook management

### Teams → Templates
- Shared template library
- Consistent project standards
- Version control at team level

### Teams → Users
- Role-based team membership
- Simplified onboarding
- Clear permission hierarchy

## Cross-References {important}

For notebook deployment:
→ [Notebooks Interface](./notebooks-interface.md)

For template creation:
→ [Templates Interface](./templates-interface.md)

For user roles:
→ [Users Interface](./users-interface.md)

For team workflows:
→ [Dashboard Patterns](./dashboard-patterns.md)

<!-- concat:boundary:end section="teams-interface" -->