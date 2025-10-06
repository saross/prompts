# Notebook Activation Workflow {essential}

## Architecture Overview

Notebook **activation** occurs in the **mobile/data collection app** (app.fieldmark.app),
NOT in the Editor or Dashboard.

**Critical**: There is NO "Active" or "Active (1)" toggle in the Notebook Editor's Info tab.
This is a common documentation error.

## Activation Process

1. Navigate to data collection app: `https://app.fieldmark.app`
2. Log in with same credentials as Dashboard
3. Click **NOT ACTIVE** tab (shows notebooks available for activation)
4. Find your notebook in the list
5. Click green **ACTIVATE** button
6. Confirm in modal dialogue
7. Notebook moves to **ACTIVE** tab

## What Activation Does

- Downloads notebook structure to device for offline use
- Downloads existing records (if any) to local database
- Enables offline data collection
- Starts background sync when online

## Troubleshooting

- **Notebook doesn't appear**: Check permissions, verify same login credentials
- **Activation fails**: Ensure stable internet connection
- **Can't deactivate**: Feature coming soon (current limitation)

## See Also

- [Offline-First Architecture](../references/platform-reference.md#offline-first)
- [Sync Behaviour](./notebooks-interface.md#sync-settings)
