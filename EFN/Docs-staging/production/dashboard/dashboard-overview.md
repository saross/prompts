<!-- concat:boundary:start section="dashboard-overview" -->
<!-- concat:metadata
document_id: dashboard-overview
category: system_navigation
component_count: 5
ui_driven: true
last_updated: 2025-09-08
-->

<!-- discovery:metadata
provides: [system-architecture, navigation-structure, component-overview, role-hierarchy]
see-also: [templates-interface, notebooks-interface, users-interface, teams-interface, dashboard-patterns]
-->

# Fieldmark Dashboard Overview

<!-- structured:metadata
meta:purpose: system-navigation
meta:summary: Centralised web interface for managing field data collection projects, templates, notebooks, teams, and users.
meta:generates: ui-navigation
meta:requires: [authenticated-user, browser-access, network-connection]
meta:version: 3.0.0
meta:document: dashboard_overview
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Production Docs](../README.md) | **Dashboard Overview** | [Templates Interface →](./templates-interface.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Top](#fieldmark-v3-documentation-structure) | [Templates Interface ↓](#templates-interface) -->

## System Architecture {essential}

Fieldmark implements a hierarchical organisational structure for field data collection:

```
Teams (Organisational Units)
  ├── Notebooks (Data Collection Instances)
  │     ├── Users (with specific roles)
  │     ├── Records (collected data)
  │     └── Invitations (pending access)
  └── Templates (Notebook Designs)
        ├── Versions (manual tracking)
        └── Field definitions (JSON schema)
```

### Key Concepts {essential}

**Teams**: Organisational containers that own resources and manage collaborative access.

**Templates**: Reusable notebook designs containing field definitions, validation rules, and UI configurations.

**Notebooks**: Deployed instances of templates where actual data collection occurs.

**Users**: System participants with role-based permissions at both system and notebook levels.

## Navigation Structure {essential}

The Dashboard provides five main navigation sections:

| Section | Purpose | Primary Actions |
|---------|---------|-----------------|
| **Home** | Dashboard landing and overview | View recent activity |
| **Templates** | Template management | Create, edit, clone templates |
| **Notebooks** | Data collection management | Deploy, manage, export data |
| **Users** | User administration | Manage roles and permissions |
| **Teams** | Collaboration units | Organise resources and members |

### UI Consistency Patterns {important}

All main interfaces follow consistent patterns:

1. **List Views**
   - Filter/search bar at top
   - Create button (+ icon or text)
   - Sortable columns
   - Pagination controls

2. **Detail Views**
   - Tabbed interface for different aspects
   - Edit button for modifications
   - Action buttons contextually displayed

3. **Creation Dialogs**
   - Modal overlays
   - Required fields marked with asterisks
   - Cancel/confirm buttons
   - Validation feedback inline

## Role-Based Access Control {important}

### System-Wide Roles

Fieldmark implements four hierarchical system roles:

| Role | Permissions | Typical User |
|------|------------|--------------|
| **System Administrator** | Full system control, all operations | IT administrators |
| **Organisation Administrator** | Manage teams and users | Project managers |
| **Template Designer** | Create and modify templates | Field researchers |
| **Standard User** | Access assigned notebooks | Data collectors |

### Notebook-Specific Roles

Within individual notebooks, users have additional roles:

| Role | Permissions | Scope |
|------|------------|-------|
| **Notebook Administrator** | Full notebook control | Single notebook |
| **Data Collector** | Create/edit own records | Single notebook |
| **Data Reviewer** | Review/approve records | Single notebook |
| **Data Viewer** | Read-only access | Single notebook |

### Team Roles

Teams have their own role hierarchy:

| Role | Permissions | Scope |
|------|------------|-------|
| **Team Administrator** | Manage team resources | Single team |
| **Team Member** | Access team resources | Single team |

## Permission Inheritance {important}

Permission precedence follows this hierarchy:

1. System Administrator (overrides all)
2. Notebook-specific roles (within notebook context)
3. Team roles (for team-owned resources)
4. System roles (baseline permissions)

### Critical Permission Rules {comprehensive}

- System Administrators have implicit access to all resources
- Notebook Administrator role supersedes team membership for that notebook
- Team Administrators can manage all team-owned resources
- Users can have different roles in different notebooks
- Role changes take effect immediately (no logout required)

## Dashboard Components {essential}

### Authentication State

All dashboard screens display authentication status:

```
Your email is not verified!
Check your emails for a verification request. Click here to send another request to {{USER_EMAIL}}.
```

This banner persists until email verification is complete.

### Global Navigation

Breadcrumb navigation shows current location:
```
Home > Teams > {{TEAM_NAME}} > Notebooks
```

### User Menu {essential}

The user menu provides account management and personalisation options:

#### Location
- **Position**: Lower-left corner of dashboard
- **Display**: Shows username and email
- **Access**: Click username to open menu

#### Menu Options

| Option | Description | Navigation Path |
|--------|-------------|----------------|
| **Profile** | Access user profile and settings | Username → Profile |
| **Log out** | End current session | Username → Log out |

#### User Profile Page

Accessing the Profile option opens the User Profile management page with:

1. **Account Information Section**
   - Email address (read-only)
   - Display name
   - Email verification status
   - Warning banner if email unverified

2. **Password Management Section**
   - "Change Password" button
   - Secure password update form
   - Password requirements displayed

3. **API Token Management Section**
   - "Manage Long-Lived Tokens" button
   - Access to API token creation and management
   - View existing tokens and their status

**Navigation Example**:
```
Click Username (lower-left) → Select "Profile" → View User Profile page
                                             → Click "Manage Long-Lived Tokens"
                                             → Create/manage API tokens
```

### Action Patterns

Primary actions consistently positioned:
- Create/Add: Top right of lists
- Edit: Top right of detail views
- Delete: In dropdown menus (requires confirmation)
- Export: Context-specific placement

## Data Flow {important}

### Template to Notebook Flow

1. **Template Creation**
   - Design in Designer/Editor
   - Save as template
   - Optional: Assign to team

2. **Notebook Deployment**
   - Select template (or JSON file)
   - Configure notebook metadata
   - Set initial permissions
   - Deploy for data collection

3. **Data Collection**
   - Users create records
   - Data validated against template
   - Records saved with metadata

4. **Data Export**
   - CSV format for structured data
   - Photo archive with HRID renaming
   - JSON for full fidelity

### User Invitation Flow

1. **Invitation Sent**
   - Email address entered
   - Role selected
   - Optional message added

2. **Pending State**
   - Shows in Invites tab
   - Can be resent or cancelled
   - Expires after set period

3. **Acceptance**
   - User clicks email link
   - Creates/links account
   - Appears in Users list

## Platform Considerations {comprehensive}

### Browser Requirements

- Modern browsers (Chrome, Firefox, Safari, Edge)
- JavaScript enabled
- Cookies enabled for session management
- Minimum 1024x768 resolution

### Network Requirements

- Stable internet connection for sync
- HTTPS for all communications
- WebSocket support for real-time updates

### Performance Characteristics

- List views paginated (default 10 items)
- Lazy loading for large datasets
- Client-side filtering where possible
- Server-side sorting for consistency

## Security Model {comprehensive}

### Authentication

- Email/password authentication
- Session-based with timeout
- Optional multi-factor authentication
- Password reset via email

### Authorisation

- Role-based access control (RBAC)
- Resource-level permissions
- API key support for programmatic access
- Audit logging of all actions

### Data Protection

- HTTPS encryption in transit
- Database encryption at rest
- Regular automated backups
- GDPR compliance features

## Integration Points {comprehensive}

### External Systems

- Email service for notifications
- Cloud storage for media files
- Geographic services for mapping
- Export to analysis tools

### API Access

- RESTful API endpoints
- Authentication via API keys
- Rate limiting applied
- Webhook support for events

## Common Terminology {essential}

| Term | Definition |
|------|------------|
| **HRID** | Human-Readable Identifier for records |
| **Designer** | Visual interface for creating templates |
| **Deployment** | Making a notebook available for data collection |
| **Sync** | Synchronising local and server data |
| **Role** | Set of permissions assigned to a user |
| **Team** | Organisational unit for collaboration |

## Quick Start Checklist {important}

For new projects:

- [ ] Create team (if using team structure)
- [ ] Design template (or select existing)
- [ ] Deploy notebook from template
- [ ] Configure user roles
- [ ] Send invitations to team members
- [ ] Test data collection workflow
- [ ] Verify export functionality
- [ ] Document project-specific conventions

## Next Steps

- For template creation, see [Templates Interface](./templates-interface.md)
- For notebook deployment, see [Notebooks Interface](./notebooks-interface.md)
- For user management, see [Users Interface](./users-interface.md)
- For team setup, see [Teams Interface](./teams-interface.md)
- For common workflows, see [Dashboard Patterns](./dashboard-patterns.md)

<!-- concat:boundary:end section="dashboard-overview" -->