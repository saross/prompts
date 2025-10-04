# Dashboard Documentation Enhancement TODO

**Created**: 2025-01-09  
**Source**: Codebase analysis of FAIMS3  
**Purpose**: Document features discovered in code but missing/incomplete in dashboard documentation

## Important Terminology Clarifications

### 🔄 Close vs Archive
**Finding**: The codebase only supports two notebook states: `OPEN` and `CLOSED`
- **No separate archive state exists**
- "Close" and "Archive" both mean setting status to `CLOSED`
- UI may show "Close" button on Actions tab
- Documentation should standardise on "Close/Closed" terminology
- API endpoint: `PUT /api/notebooks/:id/status` with body `{"status": "CLOSED"}`

### 🛠️ Developer Mode
**Finding**: Developer Mode is a server-side configuration, not a user preference
- Enabled by setting `DEVELOPER_MODE=true` environment variable
- Affects entire API server instance, not individual users
- Enables test data generation and debug logging
- Still requires appropriate user permissions to access features
- Typically used in development/training environments only

## Features Discovered from Codebase Analysis

### 1. **Long-Lived API Tokens System** 📌
**Location**: User Profile (lower-left user button) → Manage API Tokens  
**Documentation Needed**:
- Full CRUD operations for API tokens at `/api/tokens/`
- Create tokens with title, description, expiry dates
- Token value only shown once at creation (security)
- Enable/disable tokens without deletion
- Track last used timestamps
- Permission required: `CREATE_LONG_LIVED_TOKEN`

### 2. **Invite Management System** 🎫
**Documentation Needed**:
- Separate invite endpoints for notebooks and teams
- Create invites with specific role assignments
- View all pending invites (notebook/team)
- Revoke invites before acceptance
- Check invite validity

### 3. **Developer Mode Features** 🛠️
**When DEVELOPER_MODE environment variable enabled**:
- Random record generation endpoint
- POST `/api/notebooks/:id/generate`
- Configurable record count for testing
- Requires `GENERATE_RANDOM_PROJECT_RECORDS` permission
- **NOTE**: Server-side configuration, not a UI toggle
- Enabled via `DEVELOPER_MODE=true` environment variable

### 4. **Advanced Export Features** 📤
**Documentation Needed**:
- Multiple export formats beyond CSV
- Download token system for async exports
- View-specific exports: `/api/notebooks/:id/records/:viewID.:format`
- Sync status checking

### 5. **User Management Extensions** 👥
**Documentation Needed**:
- DELETE user endpoint - Complete user removal
- Bulk role assignment/removal
- Email verification challenge system

### 6. **Notebook Status Management** 📊
**Documentation Needed**:
- Status change endpoint: PUT `/api/notebooks/:id/status`
- Close/reopen notebooks (only two states: OPEN/CLOSED)
- Team reassignment: PUT `/api/notebooks/:id/team`
- **CLARIFICATION**: "Close" and "Archive" refer to the same operation (status → CLOSED)

### 7. **Advanced Permissions Actions** 🔐
**Missing from documentation**:
- `VIEW_TEAM_DETAILS`
- `VIEW_PROJECT_INVITES`
- `VIEW_TEAM_INVITES`
- `CREATE_LONG_LIVED_TOKEN`
- `GENERATE_RANDOM_PROJECT_RECORDS`
- `ADD_OR_REMOVE_GLOBAL_USER_ROLE`

### 8. **Team Member Management** 👥
- POST `/api/teams/:id/delete` - Soft delete teams
- Detailed member role management
- Virtual roles from team membership

### 9. **Granular Record Operations** 📝
- Individual record sync status checking
- Bulk sync status validation

### 10. **System Administration Features** ⚙️
- Initial admin user creation on first setup
- Global role management

### 11. **Email System Integration** 📧
- Email reset functionality
- Verification email system
- Invite email dispatch

### 12. **Template Versioning Hints** 📋
- Template derivation tracking
- Template update cascading

## Documentation Status - Session 2 (2025-01-09)

### ✅ COMPLETED THIS SESSION
1. **API Token Management** - Full documentation added to users-interface.md
2. **User Profile Navigation** - Added to dashboard-overview.md
3. **Notebook Close/Open** - Actions tab documented in notebooks-interface.md
4. **Permissions Matrix** - 40+ actions added to roles-permissions-reference.md
5. **Teams Edit Tab** - Added missing 6th tab documentation
6. **Templates Actions Tab** - Corrected to show 6 operations
7. **Team Invites Enhancement** - Virtual roles and best practices added
8. **Tab Verification** - Fixed Records tab (removed), Export tab (added), all interfaces verified

### ⚠️ INTEGRATION TASKS NEEDED
1. **Cross-Reference Updates**
   - Add {{cross-ref:}} markers for new API token section
   - Link virtual roles to permission matrix
   - Connect close/open to workflow docs

2. **Consistency Checks**
   - Verify "Close" terminology (not "Archive") throughout
   - Ensure virtual role descriptions consistent
   - Check permission names match codebase

3. **Deduplication Review**
   - Actions tab content vs other operation descriptions
   - Team vs notebook invite guidance
   - Permission requirements across docs

## Required Documentation Updates

### Priority 1: User-Visible Features
1. **Add API Token Management section** to users-interface.md ✅ DONE
   - Navigation: User button → User Profile → Manage API Tokens
   - Creating, disabling, deleting tokens
   - Security best practices

2. **Document Invite System** in notebooks-interface.md and teams-interface.md
   - Creating and managing invites (partially documented)
   - Role assignment during invite
   - Revocation process

3. **Add Notebook Close/Open functionality** to notebooks-interface.md ✅ DONE
   - ✅ Verified "Close Notebook" button exists on Actions tab
   - ✅ Documented close/reopen functionality (status: OPEN↔CLOSED)
   - ✅ Documented effects: read-only, no data collection when closed
   - ✅ Clarified there's no separate "archive" state

### Priority 2: Advanced Features
4. **Create api-automation-guide.md**
   - Using long-lived tokens
   - API endpoints reference
   - Authentication patterns

5. **Document Developer Mode** (if applicable)
   - Enabling developer mode
   - Test data generation
   - Training environment setup

### Priority 3: Permission System
6. **Update roles-permissions-reference.md**
   - Add all missing actions
   - Document virtual roles
   - Permission inheritance model

### Files to Update
- [✅] `dashboard/users-interface.md` - API tokens section ADDED
- [✅] `dashboard/notebooks-interface.md` - Actions tab & close/open status ADDED
- [ ] `dashboard/teams-interface.md` - Enhance invite system docs, soft delete
- [✅] `dashboard/dashboard-overview.md` - User Profile navigation ADDED
- [✅] `references/roles-permissions-reference.md` - Complete permission matrix ADDED
- [ ] Create new: `api-automation-guide.md`
- [ ] Create new: `developer-features-guide.md` (server config only - not user-facing)

## Validation Required
- Check which features are UI-accessible vs API-only
- Verify permission requirements for each feature
- Test workflows with different user roles
- Confirm current UI matches discovered features

## Feature Accessibility Analysis

### UI-Accessible Features (Confirmed)
| Feature | Location | Status |
|---------|----------|--------|
| API Token Management | User Profile → Manage Long-Lived Tokens | ✅ Documented |
| Password Change | User Profile → Change Password | ✅ Documented |
| Notebook Invites | Notebook → Users Tab → Add User | ✓ Partially documented |
| Team Invites | Team → Invites Tab | ✓ Partially documented |
| User Management | Dashboard → Users | ✓ Documented |
| Team Management | Dashboard → Teams | ✓ Documented |
| Basic Export | Notebook → Export (CSV, Photos) | ✓ Documented |

### API-Only Features (No UI Currently)
| Feature | Endpoint | Use Case |
|---------|----------|----------|
| Notebook Status Change | PUT /api/notebooks/:id/status | Close/reopen notebooks (OPEN↔CLOSED) |
| Team Reassignment | PUT /api/notebooks/:id/team | Bulk team transfers |
| Random Data Generation | POST /api/notebooks/:id/generate | Testing (Developer Mode) |
| Advanced Export Formats | /api/notebooks/:id/records/:viewID.:format | Custom exports |
| Bulk Role Assignment | Various endpoints | Automation scripts |
| Email Verification API | /api/users/:id/verify | Custom verification flows |
| Download Tokens | /api/export/token | Async large exports |
| Sync Status Checking | /api/notebooks/:id/sync-status | Monitoring tools |

### Features Requiring Further Investigation
| Feature | Expected Location | Investigation Needed |
|---------|------------------|---------------------|
| Template Versioning | Templates interface | Check if derivation tracking visible |
| Virtual Roles Display | Users/Teams interface | Verify if inheritance shown |
| Activity Logs | User profiles | Check if last-used timestamps visible |
| Soft Delete Teams | Teams interface | Confirm delete vs archive behaviour |

## Permission Requirements Matrix

### Feature-Permission Mapping

| Feature | Required Permission | Role(s) That Have It | Notes |
|---------|-------------------|---------------------|--------|
| **API Token Management** ||||
| - Create tokens | CREATE_LONG_LIVED_TOKEN | All users (GENERAL_USER) | Default permission |
| - View own tokens | READ_MY_LONG_LIVED_TOKENS | All users | Self-management |
| - Edit own tokens | EDIT_MY_LONG_LIVED_TOKEN | All users | Self-management |
| - Revoke own tokens | REVOKE_MY_LONG_LIVED_TOKEN | All users | Self-management |
| - Manage all tokens | *_ANY_LONG_LIVED_TOKEN actions | GENERAL_ADMIN only | System administration |
| **Invite Management** ||||
| - View notebook invites | VIEW_PROJECT_INVITES | PROJECT_MANAGER+ | Notebook management |
| - Create notebook invites | Role-based (see matrix) | PROJECT_MANAGER+ | Depends on invite role |
| - View team invites | VIEW_TEAM_INVITES | TEAM_MANAGER+ | Team management |
| - Create team invites | Role-based (see matrix) | TEAM_MANAGER+ | Depends on invite role |
| **Status Management** ||||
| - Close notebook | CHANGE_PROJECT_STATUS | PROJECT_ADMIN | Check if UI has Close button |
| - Reassign team | REASSIGN_PROJECT_TEAM | PROJECT_ADMIN | API only currently |
| **Developer Features** ||||
| - Generate test data | GENERATE_RANDOM_PROJECT_RECORDS | PROJECT_ADMIN + DEV_MODE | Requires flag |
| **User Management** ||||
| - Delete users | DELETE_USER | GENERAL_ADMIN | Permanent action |
| - Manage global roles | ADD_OR_REMOVE_GLOBAL_USER_ROLE | GENERAL_ADMIN | System-wide |
| **Team Management** ||||
| - View team details | VIEW_TEAM_DETAILS | TEAM_MEMBER+ | Basic access |
| - Soft delete teams | DELETE_TEAM | TEAM_ADMIN | Recoverable |

### Permission Inheritance Rules

1. **Notebook Permissions**
   - PROJECT_ADMIN → PROJECT_MANAGER → PROJECT_CONTRIBUTOR
   - Higher roles inherit all lower permissions

2. **Team Permissions**
   - TEAM_ADMIN → TEAM_MANAGER → TEAM_MEMBER
   - Team roles grant virtual notebook roles

3. **System Permissions**
   - GENERAL_ADMIN has all permissions everywhere
   - GENERAL_CREATOR can create notebooks/templates
   - GENERAL_USER has basic self-management

### Critical Permission Notes

⚠️ **Security Considerations**:
- Long-lived tokens inherit creator's permissions
- Tokens cannot exceed creator's permission level
- Maximum token duration: 90 days (security policy)
- Invite permissions depend on role being granted

ℹ️ **Virtual Role Behaviour**:
- Team membership automatically grants notebook access
- Direct notebook roles override team virtual roles
- Multiple team memberships = multiple virtual roles

---

*Based on FAIMS3 codebase analysis - 12 significant features need documentation*
*Permission requirements verified against api/src/api/*.ts files*