# Permission Patterns

**Purpose**: Common permission and access control patterns in Fieldmark  
**Audience**: Administrators, notebook managers  
**Category**: Security and access management

## Virtual Role Pattern {important}

### Context
When users join teams, they need appropriate access to all team resources without individual configuration.

### Solution
Virtual roles automatically grant permissions on team resources:

```
Team Membership → Virtual Roles → Resource Access

TEAM_MEMBER → PROJECT_CONTRIBUTOR (all team notebooks)
           → TEMPLATE_GUEST (all team templates)

TEAM_MANAGER → PROJECT_MANAGER (all team notebooks)
            → TEMPLATE_GUEST (all team templates)

TEAM_ADMIN → PROJECT_ADMIN (all team notebooks)
          → TEMPLATE_ADMIN (all team templates)
```

### Implementation
1. Add user to team with appropriate role
2. Virtual roles apply immediately
3. No manual notebook permissions needed
4. Future notebooks inherit permissions

### When to Use
- Managing research groups
- Consistent permissions across resources
- Template access requirements
- Long-term collaborations

### When NOT to Use
- Single notebook access
- External reviewers
- Temporary access
- Different permissions per notebook

## Least Privilege Pattern {essential}

### Context
Users should have minimum permissions necessary for their work.

### Solution
Start with lowest role and escalate only when needed:

1. **Default to Team Member** for new collaborators
2. **Document reasons** for elevated roles
3. **Regular audits** to remove unnecessary permissions
4. **Time-bound elevation** for temporary needs

### Example Workflow
```
New User Request
    ↓
Start as TEAM_MEMBER
    ↓
Monitor for 2 weeks
    ↓
Elevate if justified
    ↓
Document decision
    ↓
Schedule review
```

## Token Rotation Pattern {comprehensive}

### Context
Long-lived API tokens pose security risks if compromised.

### Solution
Implement regular token rotation:

1. **Monthly Rotation Schedule**
   - Create new token before old expires
   - Update automation scripts
   - Delete old token after verification

2. **Separate Tokens per Task**
   ```
   Daily Export → "export-token" (30 days)
   Backup Script → "backup-token" (60 days)
   Integration → "integration-token" (90 days)
   ```

3. **Monitoring**
   - Check "Last Used" timestamps weekly
   - Investigate dormant tokens
   - Disable suspicious activity immediately

## Invitation Strategy Pattern {important}

### Context
Choosing between team and notebook invitations affects access scope.

### Decision Matrix

| Scenario | Use Team Invite | Use Notebook Invite |
|----------|-----------------|---------------------|
| Need template access | ✅ | ❌ |
| Multiple notebooks | ✅ | ❌ |
| Single notebook only | ❌ | ✅ |
| External collaborator | ❌ | ✅ |
| Research group member | ✅ | ❌ |
| Temporary access | ❌ | ✅ |
| Consistent permissions | ✅ | ❌ |
| Granular control | ❌ | ✅ |

### Implementation Guidelines

**Team Invites**:
1. Review all team resources first
2. Choose appropriate team role
3. Send invite with clear expectations
4. Monitor resource usage

**Notebook Invites**:
1. Confirm single notebook suffices
2. Set specific notebook role
3. Include access duration
4. Plan removal process

## Close/Reopen Pattern {essential}

### Context
Notebooks complete data collection but need preservation.

### Solution
Use Close status instead of deletion:

1. **Closing Process**
   ```
   Active Collection → Review Data → Close Notebook
                                   ↓
                            Status: CLOSED
                            Data: Read-only
                            Export: Available
   ```

2. **Benefits**
   - Data preserved
   - Exports still work
   - Can reopen if needed
   - Clear completion status

3. **Reopening Process**
   ```
   Closed Notebook → New Requirements → Reopen
                                      ↓
                                Status: OPEN
                                Collection: Enabled
   ```

### When to Close
- Data collection complete
- Project ended
- Archival required
- Prevent accidental changes

### When NOT to Close
- Temporary pause
- Seasonal collection
- Ongoing project
- Active analysis

## Related Documentation

- [Roles & Permissions Reference](../references/roles-permissions-reference.md)
- [Teams Interface](../dashboard/teams-interface.md)
- [API Token Management](../dashboard/users-interface.md#api-token-management)
- [Automation Basics](../advanced/automation-basics.md)