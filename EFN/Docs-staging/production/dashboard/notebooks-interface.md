<!-- concat:boundary:start section="notebooks-interface" -->
<!-- concat:metadata
document_id: notebooks-interface
category: data_collection
deployment: true
export_formats: ["CSV", "photo_archive"]
last_updated: 2025-09-08
-->

<!-- discovery:metadata
provides: [notebook-deployment, record-management, user-permissions, data-export, invitation-flow]
see-also: [templates-interface, users-interface, teams-interface, dashboard-patterns]
-->

# Notebooks Interface

<!-- structured:metadata
meta:purpose: data-collection-management
meta:summary: Deploy templates as notebooks, manage users and permissions, collect records, and export data.
meta:generates: notebook-instances
meta:requires: [template-selection, user-assignment]
meta:version: 3.0.0
meta:document: notebooks_interface
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Templates Interface](./templates-interface.md) | **Notebooks Interface** | [Users Interface →](./users-interface.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Templates Interface](#templates-interface) | [Users Interface ↓](#users-interface) -->

## Overview {essential}

Notebooks are deployed instances of templates where actual data collection occurs. Each notebook:
- Maintains its own user base
- Enforces template-defined validation
- Stores collected records
- Tracks data provenance
- Supports offline collection (mobile)

## Main Notebooks List {essential}

### Quick Filters

The interface provides three filter views:

| Filter | Description | Visibility |
|--------|-------------|------------|
| **Activated Notebooks** | Notebooks you're participating in | All users |
| **Notebooks with roles** | Where you have specific permissions | All users |
| **All Notebooks** | System-wide view | Admin only |

### List Components

| Element | Description | User Action |
|---------|-------------|-------------|
| **Search Bar** | Filter by name/metadata | Type to search |
| **Create Notebook** | Deploy new instance | Opens creation dialog |
| **Notebook Entries** | Individual notebooks | Click for details |

### Notebook Entry Information

Each entry displays:
- Notebook name
- Description
- Status indicators (active/archived)
- User count
- Record count
- Last activity timestamp
- Team ownership (if applicable)

## Notebook Creation {essential}

### Creation Dialog

The notebook creation process requires:

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| **Notebook Name** | Yes | Unique identifier | {{NOTEBOOK_NAME}} |
| **Template Selection** | No* | Choose existing template | {{TEMPLATE_NAME}} |
| **JSON Upload** | No* | Alternative to template | {{JSON_FILE_PATH}} |
| **Team Assignment** | Auto | If created from team context | {{TEAM_NAME}} |

*One method required: template OR JSON OR proceed to Designer

### Creation Pathways

**Required Role**: `GENERAL_CREATOR` or team member with notebook creation rights ({{cross-ref:roles-permissions-reference}})

#### Path 1: From Template
```
Notebooks > Create Notebook > Select Template > {{TEMPLATE_NAME}}
→ Configure settings → Deploy
```

#### Path 2: From JSON
```
Notebooks > Create Notebook > Upload JSON > Choose File
→ Validate structure → Deploy
```

#### Path 3: From Team Context
```
Teams > {{TEAM_NAME}} > Notebooks > Create Notebook
→ Automatic team ownership → Deploy
```

#### Path 4: Direct to Designer
```
Notebooks > Create Notebook > Leave blank
→ Opens Designer → Build template → Deploy
```

## Individual Notebook View {important}

Each notebook has a comprehensive management interface with tabs:

### Details Tab {essential}

Displays notebook metadata:

| Field | Description | Editable |
|-------|-------------|----------|
| **Name** | Notebook identifier | Yes (Admin) |
| **Description** | Purpose and notes | Yes (Admin) |
| **Template** | Source template name | No |
| **Created** | Deployment timestamp | No |
| **Modified** | Last update time | No |
| **Status** | Active/Archived | Yes (Admin) |
| **Team** | Owning team | No |
| **Statistics** | Users, records, activity | No |

### Records Tab {important}

The primary data collection interface:

#### Record List Features

| Feature | Description | Permissions |
|---------|-------------|-------------|
| **Filter** | Search records | All users |
| **Sort** | By date, author, status | All users |
| **View** | Open record details | Based on role |
| **Edit** | Modify record | Owner or Admin |
| **Delete** | Remove record | Owner or Admin |
| **Export** | Download data | Based on role |

#### Record Information

Each record shows:
- HRID (Human-Readable Identifier)
- Creation timestamp
- Author (username)
- Status (draft/submitted/reviewed)
- Last modified
- Revision count

#### Record Status Workflow

| Status | Description | Who Can Transition |
|--------|-------------|-------------------|
| **Draft** | Work in progress | Author |
| **Submitted** | Ready for review | Author → Reviewer |
| **Reviewed** | Approved | Reviewer |
| **Archived** | Historical | Administrator |

#### Export Options {essential}

Current export formats:

1. **CSV Export**
   - Structured tabular data
   - All fields as columns
   - UTF-8 encoding
   - Includes metadata fields

2. **Photo Archive**
   - ZIP file containing images
   - Photos renamed using HRIDs
   - Fallback: Original filename if no HRID
   - Maintains folder structure

### Users Tab {important}

Manages notebook participants:

#### User List Display

| Column | Description | Sortable |
|--------|-------------|----------|
| **Name** | Display name | Yes |
| **Email** | Contact address | Yes |
| **Roles** | Assigned permissions | No |
| **Status** | Active/Invited | Yes |
| **Last Activity** | Recent action | Yes |

#### User Actions

| Action | Permission Required | Description |
|--------|-------------------|-------------|
| **Add User** | Notebook Admin | Opens invitation dialog |
| **Edit Role** | Notebook Admin | Modify permissions |
| **Remove User** | Notebook Admin | Revoke access |
| **View Activity** | Notebook Admin | See user actions |

#### Notebook Roles {essential}

| Role | Permissions | Use Case |
|------|------------|----------|
| **Notebook Administrator** | Full control | Project manager |
| **Data Collector** | Create/edit own records | Field worker |
| **Data Reviewer** | Review all records | Quality control |
| **Data Viewer** | Read-only access | Stakeholder |

### Invites Tab {important}

Handles pending invitations:

#### Invitation Management

| Status | Description | Actions Available |
|--------|-------------|------------------|
| **Pending** | Awaiting response | Resend, Cancel |
| **Accepted** | User joined | View in Users tab |
| **Expired** | Time limit exceeded | Resend |
| **Declined** | User rejected | Remove, Resend |

#### Invitation Process

1. **Create Invitation**
   ```
   Users Tab > Add User > Enter Email
   → Select Role → Add Message (optional) → Send
   ```

2. **Email Sent**
   - Contains acceptance link
   - Shows notebook name
   - Includes personal message
   - Valid for 7 days

3. **User Accepts**
   - Clicks email link
   - Creates/links account
   - Gains immediate access

4. **Invitation Complete**
   - User appears in Users list
   - Invitation removed from pending
   - Activity logged

## Data Collection Workflow {important}

### Record Creation

1. User navigates to notebook
2. Clicks "Create Record" button
3. Fills form fields per template
4. Saves as draft or submits
5. Record assigned HRID

### Record Editing

- Draft status: Full editing allowed
- Submitted: Limited by role
- Reviewed: Admin only
- All edits create revisions

### Data Validation

Templates enforce:
- Required fields
- Format validation
- Range constraints
- Cross-field rules
- Conditional requirements

For validation implementation:
→ [Dynamic Forms Guide](../patterns/dynamic-forms-guide.md) - Validation patterns
→ [Field Selection Guide](../patterns/field-selection-guide.md) - Choosing validators
→ [Implementation Patterns](../patterns/implementation-patterns-guide.md) - Best practices

## Offline Capabilities {comprehensive}

### Mobile App Features

- Download notebook for offline use
- Collect data without connection
- Queue changes locally
- Sync when connected
- Conflict resolution

### Sync Process

1. **Download Phase**
   - Template definition
   - Existing records
   - User permissions

2. **Offline Work**
   - Create new records
   - Edit existing (if permitted)
   - Queue all changes

3. **Upload Phase**
   - Send queued changes
   - Receive updates
   - Resolve conflicts
   - Update local cache

## Team-Owned Notebooks {important}

### Benefits of Team Ownership

- Centralised permission management
- Automatic member access
- Consistent project standards
- Simplified onboarding

### Team Context Creation

When created from team:
```
Teams > {{TEAM_NAME}} > Notebooks > Create
```

Automatically:
- Assigns team ownership
- Grants team members access
- Inherits team permissions
- Appears in team's notebook list

## Performance Considerations {comprehensive}

### Large Datasets

| Records | Performance Impact | Recommendations |
|---------|-------------------|-----------------|
| <1,000 | None | Standard usage |
| 1,000-10,000 | Minor | Use filtering |
| 10,000-50,000 | Noticeable | Pagination essential |
| >50,000 | Significant | Consider archiving |

### Optimisation Strategies

- Regular data exports
- Archive completed projects
- Remove inactive users
- Clean up draft records
- Optimise photo storage

## Common Issues and Solutions {comprehensive}

### Notebook Creation Failures

| Issue | Cause | Solution |
|-------|-------|----------|
| "Invalid template" | JSON syntax error | Validate JSON |
| "Name already exists" | Duplicate notebook | Choose unique name |
| "Permission denied" | Insufficient role | Request elevation |
| "Template not found" | Deleted template | Use JSON backup |

### Import/Export Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| CSV empty | No records | Create records first |
| Photos missing | No media fields | Check template |
| Export fails | Large dataset | Export in batches |
| Import rejected | Wrong format | Check JSON structure |

### Permission Problems

| Issue | Required Role | Solution |
|-------|--------------|----------|
| Can't edit records | `PROJECT_CONTRIBUTOR` | Request role from notebook admin ({{cross-ref:roles-permissions-reference}}) |
| Can't invite users | `PROJECT_ADMIN` | Contact notebook admin ({{cross-ref:roles-permissions-reference}}) |
| Can't see notebook | Any notebook role | Request invitation from admin |
| Can't delete notebook | `PROJECT_ADMIN` | Contact notebook administrator |
| Can't export data | `PROJECT_MANAGER` | Request manager role ({{cross-ref:roles-permissions-reference}}) |

## Best Practices {important}

### Notebook Naming
```
{{PROJECT}}-{{LOCATION}}-{{YEAR}}-{{TYPE}}
Example: CSIRO-Pilbara-2025-Survey
```

### User Management
- Assign roles based on actual needs
- Regular permission audits
- Remove inactive users
- Document role decisions

### Data Management
- Regular exports for backup
- Test export formats early
- Plan data retention
- Archive completed projects

### Quality Control
- Implement review workflows
- Use Data Reviewer role
- Regular data validation
- Document data standards

## Cross-References {important}

For template design:
→ [Templates Interface](./templates-interface.md)

For user roles:
→ [Users Interface](./users-interface.md)

For team management:
→ [Teams Interface](./teams-interface.md)

For workflows:
→ [Dashboard Patterns](./dashboard-patterns.md)

<!-- concat:boundary:end section="notebooks-interface" -->