<!-- concat:boundary:start section="users-interface" -->
<!-- concat:metadata
document_id: users-interface  
category: user_management
permissions: role_based
authentication: email_password
last_updated: 2025-09-08
-->

<!-- discovery:metadata
provides: [user-management, system-roles, permissions-matrix, activity-tracking]
see-also: [notebooks-interface, teams-interface, dashboard-overview, dashboard-patterns]
-->

# Users Interface

<!-- structured:metadata
meta:purpose: user-administration
meta:summary: System-wide user management, role assignment, activity tracking, and permission control.
meta:generates: user-permissions
meta:requires: [admin-role, user-database]
meta:version: 3.0.0
meta:document: users_interface
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Notebooks Interface](./notebooks-interface.md) | **Users Interface** | [Teams Interface →](./teams-interface.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Notebooks Interface](#notebooks-interface) | [Teams Interface ↓](#teams-interface) -->

## Overview {essential}

The Users interface provides system-wide user management capabilities:
- User account administration
- System role assignment
- Activity monitoring
- Permission management
- Account lifecycle control

### Access Requirements {essential}

| Operation | Required Role |
|-----------|--------------|
| View user list | Any authenticated user |
| View user details | Any authenticated user |
| Modify roles | System/Organisation Admin |
| Delete users | System Administrator |
| View activity logs | System/Organisation Admin |

## Main Users List {essential}

### List View Components

| Element | Description | Functionality |
|---------|-------------|--------------|
| **Search/Filter** | Find users | By name, email, role |
| **User Entries** | Individual users | Click for details |
| **Pagination** | Navigate list | 10/25/50 per page |
| **Sort Controls** | Order results | By name, date, activity |

### User Entry Display

Each user entry shows:
- Display name
- Email address
- System roles (abbreviated)
- Account status (active/suspended)
- Last login timestamp
- Registration date

## System Roles {essential}

### Role Hierarchy

Fieldmark implements four hierarchical system-wide roles:

| Role | Abbreviation | Permissions | Typical User |
|------|--------------|-------------|--------------|
| **System Administrator** | SysAdmin | Full system control | IT administrators |
| **Organisation Administrator** | OrgAdmin | Manage teams and users | Project managers |
| **Template Designer** | Designer | Create/modify templates | Field researchers |
| **Standard User** | User | Basic access | Data collectors |

### Permission Matrix {important}

| Action | SysAdmin | OrgAdmin | Designer | User |
|--------|----------|----------|----------|------|
| Create users | ✓ | ✓ | ✗ | ✗ |
| Assign system roles | ✓ | ✓* | ✗ | ✗ |
| Create teams | ✓ | ✓ | ✗ | ✗ |
| Create templates | ✓ | ✓ | ✓ | ✗ |
| Deploy notebooks | ✓ | ✓ | ✓ | ✗ |
| Access all notebooks | ✓ | ✗ | ✗ | ✗ |
| View system logs | ✓ | ✓ | ✗ | ✗ |
| System configuration | ✓ | ✗ | ✗ | ✗ |

*Organisation Admins cannot assign System Administrator role

### Role Assignment Rules {comprehensive}

1. **Elevation Restrictions**
   - Users cannot elevate above their own role
   - Only SysAdmin can create other SysAdmins
   - Role changes take effect immediately

2. **Downgrade Protection**
   - Cannot remove last SysAdmin
   - Warning when removing admin roles
   - Confirmation required for downgrades

3. **Inheritance Behaviour**
   - System roles provide baseline permissions
   - Notebook roles can extend permissions
   - Team roles apply to team resources only

## Individual User View {important}

### User Profile Display

| Section | Information | Editable By |
|---------|------------|-------------|
| **Account Info** | Name, email, created date | User or Admin |
| **System Roles** | Assigned system permissions | Admin only |
| **Activity Summary** | Login history, actions | View only |
| **Team Memberships** | Associated teams | Team/Org Admin |
| **Notebook Access** | Participated notebooks | View only |
| **Created Resources** | Templates, notebooks | View only |

### User Actions Menu {important}

Available actions depend on viewer's role:

| Action | Who Can Perform | Description |
|--------|-----------------|-------------|
| **Edit Profile** | User or Admin | Modify name, contact |
| **Change Roles** | Admin | Adjust system permissions |
| **Reset Password** | User or Admin | Force password change |
| **Suspend Account** | Admin | Temporary disable |
| **Delete User** | SysAdmin | Permanent removal |
| **View Activity** | Admin | Detailed action log |
| **Export Data** | User or Admin | User's collected data |

## User Management Operations {important}

### Creating Users

Users can be created through:

1. **Direct Creation** (Admin)
   ```
   Users > Create User > Fill Form > Save
   ```

2. **Invitation Accept** (Self-service)
   ```
   Email Invitation > Accept > Create Account
   ```

3. **SSO Integration** (If configured)
   ```
   Login with SSO > Auto-create profile
   ```

### User Creation Form

| Field | Required | Validation | Example |
|-------|----------|------------|---------|
| **Email** | Yes | Valid email format | {{USER_EMAIL}} |
| **Display Name** | Yes | 2-50 characters | {{USER_NAME}} |
| **Password** | Yes | Minimum 8 characters | {{TEMP_PASSWORD}} |
| **System Role** | Yes | From available roles | {{SYSTEM_ROLE}} |
| **Send Welcome Email** | No | Checkbox | {{SEND_WELCOME}} |

### Modifying Users {comprehensive}

#### Profile Updates
- Display name changes
- Contact information
- Timezone preferences
- Language settings
- Notification preferences

#### Role Modifications
```
User Profile > Roles > Edit > Select New Role > Save
```

Considerations:
- Logged-in users see changes immediately
- May affect access to current resources
- Audit log entry created
- Email notification sent

#### Password Management

| Method | Initiated By | Process |
|--------|--------------|---------|
| **User Reset** | User | Email link → New password |
| **Admin Reset** | Admin | Force change on next login |
| **Expired Password** | System | Prompt at login |
| **Security Reset** | System | After suspicious activity |

### Suspending Users {comprehensive}

Suspension temporarily disables account:

Effects:
- Cannot login
- Active sessions terminated
- Retains all data and permissions
- Can be reversed

Process:
```
User Profile > Actions > Suspend Account > Confirm
```

Reasons for suspension:
- Security investigation
- Extended leave
- Policy violation pending review
- Account compromise

### Deleting Users {comprehensive}

⚠️ **Critical Operation** - Requires System Administrator

#### Pre-Deletion Checklist

- [ ] Export user's data
- [ ] Transfer resource ownership
- [ ] Document deletion reason
- [ ] Notify affected teams
- [ ] Archive activity logs

#### Deletion Options

| Option | Effect | Use Case |
|--------|--------|----------|
| **Soft Delete** | Mark as deleted, retain data | Compliance requirements |
| **Hard Delete** | Remove all traces | GDPR request |
| **Anonymise** | Replace PII with placeholders | Research continuity |

#### Data Handling

| Data Type | Soft Delete | Hard Delete | Anonymise |
|-----------|-------------|-------------|-----------|
| Profile | Hidden | Removed | Randomised |
| Records | Retained | Removed | Author anonymised |
| Activity Logs | Retained | Removed | User ID replaced |
| Team Membership | Removed | Removed | Removed |

## Activity Tracking {comprehensive}

### Activity Log Contents

Each log entry contains:
- Timestamp (UTC)
- User identifier
- Action performed
- Resource affected
- IP address
- Session ID
- Result (success/failure)

### Tracked Actions

| Category | Examples |
|----------|----------|
| **Authentication** | Login, logout, password change |
| **Data Operations** | Create, read, update, delete records |
| **Permission Changes** | Role assignments, access grants |
| **System Actions** | Template creation, notebook deployment |
| **Administrative** | User management, system configuration |

### Log Retention

| Log Type | Retention Period | Purpose |
|----------|-----------------|---------|
| Authentication | 90 days | Security monitoring |
| Data changes | 1 year | Audit trail |
| Admin actions | 3 years | Compliance |
| System errors | 30 days | Debugging |

## Email Verification {important}

### Verification Banner

Unverified users see:
```
Your email is not verified!
Check your emails for a verification request. Click here to send another request to {{USER_EMAIL}}.
```

### Verification Process

1. **Initial Email** sent on account creation
2. **Reminder Banner** appears on all pages
3. **Resend Option** available via banner
4. **Verification Link** valid for 24 hours
5. **Confirmation** on successful verification

### Restrictions for Unverified Users

| Feature | Available | Restricted |
|---------|-----------|------------|
| View notebooks | ✓ | |
| Create records | ✓ | |
| Export data | | ✓ |
| Create notebooks | | ✓ |
| Invite users | | ✓ |
| API access | | ✓ |

## User Profile Access {essential}

### Accessing Your Profile

Users can access their profile through the user menu:

1. **Click your username** in the lower-left corner of any dashboard page
2. **Select "Profile"** from the dropdown menu
3. **View User Profile page** with account management options

### User Profile Sections

The User Profile page contains three main sections:

| Section | Description | Actions Available |
|---------|-------------|------------------|
| **Account Information** | Email, name, verification status | View only |
| **Password Management** | Password change functionality | Change Password button |
| **API Token Management** | Long-lived tokens for automation | Manage Long-Lived Tokens button |

### Password Management {important}

Users can change their password directly from the profile:

1. **Navigate to User Profile** (username → Profile)
2. **Click "Change Password"** button
3. **Enter current password** for verification
4. **Enter new password** (must meet security requirements)
5. **Confirm new password** and save

Password requirements:
- Minimum 8 characters
- Mix of upper and lowercase letters
- At least one number
- At least one special character

## API Token Management {essential}
<!-- concat:reference:api-token-management -->

### Overview

Long-lived API tokens enable programmatic access to Fieldmark's APIs for automation, data integration, and external tool connectivity. These tokens are managed through the User Profile interface.

### Accessing Token Management

```
User Menu (lower-left) → Profile → Manage Long-Lived Tokens
```

### Token Management Interface {important}

The token management page displays:

| Column | Description | Details |
|--------|-------------|----------|
| **Title** | Token name | User-defined identifier |
| **Description** | Token purpose | What the token is used for |
| **Status** | Enabled/Disabled | Active state of token |
| **Created** | Creation timestamp | When token was generated |
| **Last Used** | Usage timestamp | Most recent API call |
| **Expires** | Expiry date | When token becomes invalid |
| **Owner** | Token creator | User who created token |
| **Actions** | Management options | Edit, Disable, Delete |

### Creating API Tokens {important}

#### Token Creation Process

1. **Navigate to Token Management**
   ```
   User Profile → Manage Long-Lived Tokens → Create Long Lived Token
   ```

2. **Configure Token Settings**
   
   | Field | Required | Description | Example |
   |-------|----------|-------------|----------|
   | **Title** | Yes | Descriptive name | "Data Export Automation" |
   | **Description** | Yes | Purpose and usage | "Daily export to analytics platform" |
   | **Token Duration** | Yes | Expiry setting | 30 days, 60 days, 90 days, or custom |

3. **Set Expiry Date**
   - **Quick Select**: Predefined durations (30/60/90 days)
   - **Custom Date**: Specific expiry date (max 90 days)
   - **No Expiry**: Not available for security reasons

4. **Generate Token**
   - Click "Create Long-Lived Token"
   - **CRITICAL**: Copy token immediately
   - Token shown only once for security

#### Token Display Screen {important}

⚠️ **Important - Save Your Token**

The token creation screen displays:
- Red warning banner about one-time display
- Token value with copy button
- Usage instructions with code examples
- API endpoint information

Example usage shown:
```bash
POST /api/auth/exchange-long-lived-token
Content-Type: application/json

{"token": "hAeW0aTdbdHB0GMC83IGEop8Vx2ReYMx6lrapmCm..."}
```

Response format:
```json
{
  "access_token": "Bearer token for API calls"
}
```

### Managing Existing Tokens {comprehensive}

#### Token Operations

| Operation | Description | Process | Notes |
|-----------|-------------|---------|--------|
| **View Details** | See token information | Click token row | Shows metadata only |
| **Edit Token** | Update title/description | Actions → Edit | Cannot change expiry |
| **Disable Token** | Temporarily deactivate | Actions → Disable | Reversible action |
| **Enable Token** | Reactivate disabled token | Actions → Enable | Restores access |
| **Delete Token** | Permanently remove | Actions → Delete | Irreversible, requires confirmation |

#### Token Security Features

1. **One-Time Display**
   - Token value shown only at creation
   - Cannot be retrieved later
   - Must be stored securely by user

2. **Expiry Enforcement**
   - Maximum duration: 90 days
   - Automatic invalidation at expiry
   - Cannot extend existing tokens

3. **Activity Tracking**
   - Last used timestamp updated
   - Usage patterns monitored
   - Suspicious activity flagged

4. **Permission Requirements**
   - Requires `CREATE_LONG_LIVED_TOKEN` permission
   - Standard users may need admin approval
   - Organisation policies apply

### Token Usage Best Practices {comprehensive}

#### Security Guidelines

1. **Storage**
   - Never commit tokens to version control
   - Use environment variables or secure vaults
   - Encrypt tokens at rest

2. **Rotation**
   - Regular token rotation (monthly recommended)
   - Replace before expiry
   - Delete unused tokens

3. **Scope**
   - Create separate tokens for different purposes
   - Use descriptive names
   - Document token usage

4. **Monitoring**
   - Review token activity regularly
   - Investigate unusual patterns
   - Disable suspicious tokens immediately

#### Integration Patterns

| Use Case | Token Strategy | Rotation Frequency |
|----------|---------------|--------------------|
| **CI/CD Pipeline** | Per-environment tokens | Monthly |
| **Data Export** | Task-specific tokens | Quarterly |
| **External Integration** | Per-service tokens | Monthly |
| **Development Testing** | Short-lived tokens | Weekly |
| **Production Automation** | Monitored tokens | Monthly |

### Troubleshooting API Tokens {comprehensive}

| Issue | Cause | Solution |
|-------|-------|----------|
| Token not working | Expired or disabled | Check status, create new if needed |
| Cannot create token | Missing permission | Request `CREATE_LONG_LIVED_TOKEN` role |
| Token limit reached | Maximum tokens exceeded | Delete unused tokens |
| Authentication fails | Incorrect usage | Review API documentation |
| Token compromised | Security breach | Delete immediately, audit usage |

### API Token Permissions {important}

Tokens inherit the permissions of the creating user:

| User Role | Token Capabilities |
|-----------|-------------------|
| **System Admin** | Full API access |
| **Organisation Admin** | Organisation-wide operations |
| **Template Designer** | Template and notebook operations |
| **Standard User** | Limited to user's permissions |

**Note**: Tokens cannot exceed the creator's permission level.

### Automation Guide

For practical automation examples using API tokens:
→ [Basic Automation Guide](../advanced/automation-basics.md) - Common tasks without programming
→ {{cross-ref:automation-basics}} - Practical examples for power users

## Best Practices {important}

### Role Assignment Strategy

1. **Principle of Least Privilege**
   - Grant minimum necessary permissions
   - Escalate only when required
   - Regular permission reviews

2. **Role Distribution**
   ```
   Recommended ratios:
   - System Admins: 2-3 per organisation
   - Org Admins: 1 per 10-20 users
   - Designers: Based on template needs
   - Standard Users: Majority
   ```

3. **Documentation**
   - Document role assignment reasons
   - Maintain role responsibility matrix
   - Regular audit of permissions

### User Onboarding {comprehensive}

#### Standard Process

1. **Account Creation**
   - Admin creates or user self-registers
   - Email verification sent
   - Initial role assigned

2. **Team Assignment**
   - Add to relevant teams
   - Configure team roles

3. **Notebook Access**
   - Send notebook invitations
   - Assign notebook-specific roles

4. **Training**
   - Provide role-specific guides
   - Share documentation links
   - Assign mentor if needed

5. **Verification**
   - Confirm email verified
   - Test access to resources
   - Check permission levels

### Security Considerations {comprehensive}

#### Password Policy

Enforce strong passwords:
- Minimum 8 characters
- Mixed case letters
- Numbers and symbols
- No common patterns
- No recent reuse

#### Account Monitoring

Watch for:
- Failed login attempts
- Unusual access patterns
- Permission escalation attempts
- Dormant account reactivation
- Geographic anomalies

#### Regular Audits

Monthly:
- Review admin accounts
- Check suspended users
- Verify email addresses

Quarterly:
- Full permission audit
- Remove inactive users
- Update role assignments

## Common Issues {comprehensive}

### Access Problems

| Issue | Cause | Solution |
|-------|-------|----------|
| Can't login | Suspended/deleted account | Check with admin |
| Wrong permissions | Role not assigned | Request role update |
| Missing notebooks | No invitation sent | Request notebook access |
| Can't create resources | Insufficient system role | Need Designer role |

### Email Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| No verification email | Spam filter | Check spam, resend |
| Link expired | >24 hours old | Request new link |
| Wrong email | Typo in address | Admin correction |
| Email bouncing | Invalid address | Update email |

### Role Conflicts

| Situation | Resolution |
|-----------|------------|
| System vs Notebook role | Higher permission wins |
| Team vs Notebook role | Notebook role takes precedence |
| Multiple team roles | Most permissive applies |

## Cross-References {important}

For notebook-specific roles:
→ [Notebooks Interface](./notebooks-interface.md)

For team roles:
→ [Teams Interface](./teams-interface.md)

For permission workflows:
→ [Dashboard Patterns](./dashboard-patterns.md)

For troubleshooting:
→ [Dashboard Troubleshooting](./dashboard-troubleshooting.md)

<!-- concat:boundary:end section="users-interface" -->