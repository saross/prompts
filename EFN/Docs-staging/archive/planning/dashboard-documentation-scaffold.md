# Dashboard Operations Guide (SCAFFOLD)

**Created**: 2025-01-07  
**Status**: Scaffold - to be filled with actual Dashboard capabilities  
**Purpose**: Document the Dashboard interface for user management and notebook operations

---

## ⚠️ NOTE TO TOMORROW

This is a scaffold based on typical functionality. Tomorrow we will:
1. Walk through actual Dashboard capabilities
2. Correct any misalignments with reality
3. Fill in all [NEEDS DOCUMENTATION] sections
4. Add [SCREENSHOT] placeholders where appropriate

---

## Overview

The Dashboard is your control center for managing projects, users, and notebooks in Fieldmark. It provides the administrative interface between creating notebooks in the Designer and deploying them to field users.

**Key Functions**:
- User and team management
- Notebook deployment
- Data export
- Project administration

## 1. Access & Authentication

### Getting to the Dashboard
[NEEDS DOCUMENTATION]
- URL/access point
- Browser requirements
- Mobile access availability?

### Authentication Methods
[NEEDS DOCUMENTATION]
- Standard login (email/password)
- Single Sign-On (SSO)?
- Two-factor authentication (2FA)?
- Social login options?

### Account Creation
[NEEDS DOCUMENTATION]
- Self-registration process
- Invitation-only access
- Account approval workflow
- Initial setup steps

### Password Management
[NEEDS DOCUMENTATION]
- Password requirements
- Password reset process
- Password change procedure
- Security timeout settings

## 2. Dashboard Layout & Navigation

### Main Interface Elements
[NEEDS DOCUMENTATION]
[SCREENSHOT: Dashboard main view]
- Navigation menu structure
- Key sections/tabs
- User profile area
- Notifications area

### Dashboard Home/Landing
[NEEDS DOCUMENTATION]
- Default view contents
- Quick stats/metrics shown
- Recent activity feed?
- Quick actions available

## 3. Project Management

### Creating a New Project
[NEEDS DOCUMENTATION]
- Project creation process
- Required information
- Project settings/configuration
- Project templates available?

### Project Settings
[NEEDS DOCUMENTATION]
- Project name/description
- Project visibility (public/private?)
- Data retention settings
- Project archiving/deletion

### Project Roles & Permissions
[NEEDS DOCUMENTATION]
- Available roles (admin, creator, user, viewer?)
- Permission matrix
- Default permissions
- Custom role creation?

## 4. User Management

### Inviting Users
[NEEDS DOCUMENTATION]
- How to send invitations
- Bulk invitation process
- Invitation email customization
- Invitation expiry period
- Resending invitations
[SCREENSHOT: Invite users interface]

### User List/Directory
[NEEDS DOCUMENTATION]
- Viewing all users
- User search/filter options
- User status indicators
- Bulk user actions

### Managing Individual Users
[NEEDS DOCUMENTATION]
- View user profile
- Change user role
- Reset user password
- Suspend/activate user
- Remove user from project

### Team Management
[NEEDS DOCUMENTATION]
- Creating teams
- Adding users to teams
- Team permissions
- Team leaders/hierarchy?

## 5. Notebook Operations

### Notebook List View
[NEEDS DOCUMENTATION]
- How notebooks are displayed
- Notebook status indicators
- Sort/filter options
- Bulk operations

### Actions Menu
[NEEDS DOCUMENTATION - Critical Section]

The Actions menu appears for each notebook and provides key operations:

#### "Edit Notebook in Designer"
[NEEDS DOCUMENTATION]
- Opens Designer interface
- Version control/history?
- Save/publish workflow
- Collaborative editing?

#### "Assign Notebook to Team"
[NEEDS DOCUMENTATION]
- Team selection interface
- Assignment permissions
- Notification to team members
- Removing assignments

#### "Download Notebook JSON"
[NEEDS DOCUMENTATION]
- Export format options
- Include data or structure only?
- Version information included?

#### "Replace Notebook JSON"
[NEEDS DOCUMENTATION]
- Upload interface
- Validation process
- Version conflict handling
- Rollback options

### Notebook Deployment
[NEEDS DOCUMENTATION]
- Publishing notebooks to users
- Staging/production environments?
- Deployment notifications
- Version management

## 6. Data Management

### Data Export
[NEEDS DOCUMENTATION]
[SCREENSHOT: Export interface]

#### Export Formats
[NEEDS DOCUMENTATION]
- Available formats (CSV, JSON, Excel, etc.)
- Format-specific options
- Data transformation options

#### Export Filters
[NEEDS DOCUMENTATION]
- Date range selection
- User filtering
- Record status filtering
- Field selection

#### Export Process
[NEEDS DOCUMENTATION]
- Synchronous vs asynchronous export
- Large dataset handling
- Export notifications
- Download management

### Data Import
[NEEDS DOCUMENTATION - if available]
- Import capabilities
- Supported formats
- Validation process
- Error handling

### Data Viewing
[NEEDS DOCUMENTATION]
- In-Dashboard data viewing?
- Record browsing interface
- Search capabilities
- Edit capabilities?

## 7. Analytics & Reporting

### Dashboard Metrics
[NEEDS DOCUMENTATION - if available]
- User activity metrics
- Data collection statistics
- Notebook usage analytics
- Performance metrics

### Reports
[NEEDS DOCUMENTATION - if available]
- Available report types
- Custom report creation
- Report scheduling
- Report export/sharing

## 8. System Administration

### Global Settings
[NEEDS DOCUMENTATION - if available]
- System-wide configuration
- Default settings
- Feature toggles
- Integration settings

### Audit Logs
[NEEDS DOCUMENTATION - if available]
- User action logging
- Data access logs
- System event logs
- Log export capabilities

### Backup & Recovery
[NEEDS DOCUMENTATION - if available]
- Backup scheduling
- Manual backup process
- Recovery procedures
- Data retention policies

## 9. Integrations

### API Access
[NEEDS DOCUMENTATION - if available]
- API key management
- API documentation link
- Rate limiting
- Webhook configuration

### Third-Party Integrations
[NEEDS DOCUMENTATION - if available]
- Available integrations
- Configuration process
- Data sync settings
- Integration monitoring

## 10. Help & Support

### In-Dashboard Help
[NEEDS DOCUMENTATION]
- Help menu location
- Contextual help availability
- Tutorial/walkthrough features
- Tooltip system

### Support Access
[NEEDS DOCUMENTATION]
- Support ticket creation
- Documentation links
- Community forum access
- Contact information

## Common Workflows

### Workflow 1: Setting Up a New Project
[NEEDS DOCUMENTATION]
1. Create project
2. Configure settings
3. Invite team members
4. Create first notebook
5. Deploy to users

### Workflow 2: Daily Operations
[NEEDS DOCUMENTATION]
1. Check dashboard metrics
2. Review new data
3. Export for analysis
4. Manage user requests

### Workflow 3: Notebook Updates
[NEEDS DOCUMENTATION]
1. Edit in Designer
2. Test changes
3. Version management
4. Deploy update
5. Notify users

## Troubleshooting

### Common Dashboard Issues
[NEEDS DOCUMENTATION]
- Login problems
- Permission errors
- Export failures
- Performance issues

### Error Messages
[NEEDS DOCUMENTATION]
- Common error codes
- Error explanations
- Resolution steps

---

## TODO for Tomorrow's Session

### Information to Gather:
1. **Actual menu structure** - What are the main navigation items?
2. **Invite system details** - How exactly does user invitation work?
3. **Export capabilities** - What formats and filters are actually available?
4. **Actions menu** - Precise names and functions of each action
5. **Team structure** - How teams relate to notebooks and permissions
6. **Data viewing** - Can you view/edit data in Dashboard or export only?
7. **Version control** - How are notebook versions managed?
8. **Deployment process** - How do notebooks get from Designer to users?

### Screenshots Needed:
1. Dashboard login page
2. Main Dashboard view
3. User invitation interface
4. Notebook list with Actions menu
5. Export configuration screen
6. Team assignment interface
7. Designer launch from Dashboard

### Key Questions:
1. Is there a distinction between projects and deployments?
2. Can multiple notebooks be assigned to one team?
3. Is there staging/production environment separation?
4. What role types exist and what can each do?
5. Is there audit logging visible to users?
6. Can data be edited within the Dashboard?
7. Are there analytics/reporting features?
8. What integrations are available?

---

## Notes

This scaffold represents common functionality expected in a system like Fieldmark. The actual Dashboard may have:
- **More features** than listed here
- **Different terminology** for similar concepts
- **Unique workflows** specific to archaeological/research needs
- **Simpler or more complex** permission models

Tomorrow's session will align this scaffold with reality and fill in all gaps.

---

*End of scaffold - Ready for tomorrow's documentation session*