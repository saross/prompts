# Fieldmark Glossary: Key Terms and Concepts

**Purpose**: Define critical terminology for consistent understanding  
**Created**: 2025-01-07  
**Usage**: Reference for all Fieldmark-specific terms and concepts

<!-- structured:metadata
meta:purpose: technical-reference
meta:summary: Comprehensive glossary defining all Fieldmark-specific terminology and concepts.
meta:generates: term-definitions
meta:requires: [fieldmark-knowledge]
meta:version: 3.0.0
meta:document: glossary
meta:depth-tags: [essential]
-->

<!-- discovery:metadata
provides: [term-definitions, concept-clarification, ontology]
see-also: [notebook-format-guide, component-reference, field-type-index]
-->

## Core Architecture Terms

### fields
**Definition**: The lowest level of the three-tier hierarchy containing individual field definitions.  
**Context**: Each field has a unique identifier and contains component configuration.  
**Example**: `"site-name": { "component-name": "TextField", ... }`  
**See**: [Form Structure Guide](#form-structure-guide)

### fviews
**Definition**: Form views - the middle tier that groups fields into logical sections.  
**Critical**: REQUIRED layer between fields and viewsets. 50% of import failures are due to missing fviews.  
**Example**: `"basic-info": { "fields": ["field1", "field2"], "label": "Basic Information" }`  
**See**: [Notebook Structure](#notebook-structure-errors)

### viewsets
**Definition**: The top tier that groups fviews into complete forms or pages.  
**Context**: What users see as distinct screens or tabs in the application.  
**Example**: `"main-form": { "views": ["section1", "section2"], "label": "Survey Form" }`  
**See**: [Form Structure Guide](#form-structure-guide)

### visible_types
**Definition**: Array listing which viewsets are accessible to users.  
**Critical**: Must reference existing viewsets or forms won't appear.  
**Example**: `"visible_types": ["main-form", "review-form"]`  
**See**: [Notebook Format Guide](#notebook-format-guide)

### ui-specification
**Definition**: The container object holding all form structure (fields, fviews, viewsets).  
**Context**: Required wrapper for all notebook configuration.  
**Example**: `"ui-specification": { "fields": {...}, "fviews": {...}, "viewsets": {...} }`

## Field Configuration Terms

### component-namespace
**Definition**: Package/library providing the component implementation.  
**Values**: `faims-custom`, `formik-material-ui`, `mapping-plugin`, `qrcode`  
**Example**: `"component-namespace": "faims-custom"`  
**See**: [Component Reference](#component-reference)

### component-name
**Definition**: The specific component class within the namespace.  
**Example**: `"component-name": "FAIMSTextField"`  
**Note**: Designer UI names often differ from actual component names.  
**See**: [Designer Component Mapping](#designer-component-mapping)

### component-parameters
**Definition**: Configuration object containing all field-specific settings.  
**Critical**: Must include `"name"` parameter matching the field identifier.  
**Example**: `"component-parameters": { "name": "field-id", "label": "Field Label" }`

### type-returned
**Definition**: Data type the field returns when saved.  
**Values**: `faims-core::String`, `faims-core::Number`, `faims-core::Array`, `faims-attachment::Files`  
**Example**: `"type-returned": "faims-core::String"`

### validationSchema
**Definition**: Yup-based validation rules array.  
**Format**: Array of arrays, type validation must come first.  
**Example**: `[["yup.string"], ["yup.required", "This field is required"]]`  
**See**: [Validation Errors](#validation-errors)

## Special Field Types

### HRID
**Definition**: Human-Readable Identifier - user-friendly record IDs instead of UUIDs.  
**Implementation**: Uses TemplatedStringField with template patterns.  
**Example**: `"PROJECT-2024-001"` instead of `"rec-a7f3b2c1-d4e5..."`  
**Critical**: Should be included in every notebook for usability.  
**See**: [TemplatedStringField](#templatedstringfield)

### TemplatedStringField
**Definition**: Auto-generates strings from templates with variables.  
**Variables**: `{{PROJECT}}`, `{{_CREATED_DATE}}`, `{{_INCREMENT}}`  
**Security**: ⚠️ XSS vulnerability if used with user input - use only for system-generated values.  
**See**: [Text Fields](#text-input-fields)

### RelationshipField
**Definition**: Links records within or between notebooks.  
**Limits**: Performance degrades beyond 50 relationships per record.  
**Example**: Links artifact to context, sample to site.  
**See**: [Relationship Field](#relationship-fields)

## Conditional Logic Terms

### is-logic
**Definition**: Object defining conditional visibility rules for fields.  
**Format**: `{ "if": "controller-field", "==": "trigger-value" }`  
**Complex**: Supports `and`, `or`, `in`, `!=`, `>`, `<` operators.  
**See**: [Dynamic Forms Guide](#dynamic-forms-guide)

### logic_select
**Definition**: Boolean flag marking a field as a conditional logic controller.  
**Critical**: Must be `true` on controller field for is-logic to work.  
**Example**: `"logic_select": true` on RadioGroup controlling dependent fields.

## Platform-Specific Terms

### Mobile-only Components
**Definition**: Components that only function on iOS/Android apps.  
**List**: `QRCodeFormField` (scanning), `TakePoint` (GPS), `TakePhoto` (camera)  
**Best Practice**: Always provide web fallbacks.  
**See**: [Platform Reference](#platform-reference)

### Offline Mode
**Definition**: Ability to work without internet connection.  
**Context**: Mobile apps cache data; web requires initial connection.  
**Limitation**: MapFormField needs internet for first tile load.

## Data Types

### faims-core::String
**Definition**: Basic text data type.  
**Used by**: TextField, Select, DateTimeNow, most fields.

### faims-core::Number
**Definition**: Numeric data type.  
**Used by**: TextField with type="number", BasicAutoIncrementer.

### faims-core::Array
**Definition**: Multiple value data type.  
**Used by**: MultiSelect, Checkbox groups.

### faims-attachment::Files
**Definition**: File attachment data type.  
**Used by**: TakePhoto, AudioFormField.

### faims-core::JSON
**Definition**: Complex object data type.  
**Used by**: TakePoint (GPS coordinates), MapFormField.

## Validation Terms

### yup
**Definition**: JavaScript schema validation library used by Fieldmark.  
**Usage**: All validation rules start with `yup.` prefix.  
**Order**: Type validation (yup.string) must come before constraints (yup.required).  
**See**: [Validation Error Decoder](#validation-error-decoder)

### Cross-field Validation
**Definition**: Validation rules referencing other fields.  
**Example**: `["yup.min", ["yup.ref", "start-date"], "Must be after start date"]`  
**See**: [Cookbook Recipe #1](#recipe-1-date-range-picker)

## Template System Terms

### Template Markers
**Definition**: Placeholder variables in parametric templates.  
**Format**: `{{VARIABLE_NAME}}`  
**Example**: `{{FIELD_ID}}`, `{{FIELD_LABEL}}`, `{{VALIDATION_MESSAGE}}`  
**Count**: 1,290 markers added to documentation.  
**See**: [Cookbook](#fieldmark-cookbook)

### Parametric Generation
**Definition**: Creating notebooks by replacing template variables rather than editing JSON.  
**Benefit**: Ensures all references update consistently.  
**See**: [Generation-Ready Patterns](#generation-ready-patterns)

## Common Issues Terms

### Missing fviews
**Definition**: Most common import failure - missing middle tier.  
**Impact**: 50% of notebook import failures.  
**Fix**: Add fviews layer between fields and viewsets.  
**See**: [Troubleshooting Index](#notebook-structure-errors)

### Circular Reference
**Definition**: Field relationships creating infinite loops.  
**Symptom**: "Maximum call stack exceeded" error.  
**Fix**: Check relationship field configurations.

### Race Condition
**Definition**: Timing issue where operations complete out of order.  
**Example**: Address field geocoding vs user typing.  
**Fix**: Implement debounce configuration.

## Designer vs JSON Terms

### Designer UI Name
**Definition**: Field name shown in Fieldmark Designer interface.  
**Issue**: Often differs from actual JSON component name.  
**Example**: "Text Field" in Designer = "FAIMSTextField" in JSON.  
**See**: [Designer Component Mapping](#designer-component-mapping)

### Component Mapping
**Definition**: Translation table between Designer names and JSON components.  
**Critical**: Required for converting Designer notebooks to JSON.  
**Location**: designer-component-mapping.md

## Metadata Terms

### metadata
**Definition**: Notebook-level configuration section.  
**Contains**: Project name, version, hridField designation.  
**Example**: `"metadata": { "name": "Project 2024", "hridField": "record-id" }`

### discovery:metadata
**Definition**: Documentation metadata for content discovery.  
**Format**: HTML comments with provides/see-also tags.  
**Purpose**: Helps LLMs understand document relationships.

### structured:metadata
**Definition**: Enhanced metadata with purpose, summary, requirements.  
**Format**: HTML comments with meta: prefixed tags.  
**Purpose**: Semantic understanding of document content.

## Security Terms

### XSS (Cross-Site Scripting)
**Definition**: Security vulnerability allowing malicious script injection.  
**Risk**: TemplatedStringField with user input.  
**Mitigation**: Never use user input in templates.  
**See**: [Security Considerations](#security-considerations)

## Performance Terms

### Relationship Limit
**Definition**: ~50 relationships per record before performance degrades.  
**Impact**: Slow form loading and saving.  
**Solution**: Split into multiple related forms.

### Notebook Size Limit
**Definition**: Practical limit of ~100 fields per notebook.  
**Impact**: Slow import/export, UI lag.  
**Solution**: Split into multiple viewsets.

## API & Automation Terms

### Long-Lived Token
**Definition**: API authentication token with extended validity period.
**Duration**: Maximum 90 days.
**Usage**: Automation scripts and integrations.
**Location**: User Profile → Manage Long-Lived Tokens.
**Security**: Shown only once at creation.

### Bearer Token
**Definition**: Short-lived access token for API calls.
**Duration**: 5 minutes default.
**Obtained**: Exchange long-lived token via API.
**Format**: `Authorization: Bearer <token>`

### Token Rotation
**Definition**: Security practice of regularly replacing API tokens.
**Frequency**: Monthly recommended.
**Purpose**: Limit exposure if token compromised.

## Permission Terms

### Virtual Role
**Definition**: Automatic permission grant based on team membership.
**Example**: TEAM_MEMBER gets PROJECT_CONTRIBUTOR on all team notebooks.
**Purpose**: Simplify permission management.
**Cascade**: Applied to all current and future team resources.

### Close Status
**Definition**: Notebook state preventing new data collection.
**Effect**: Read-only access, exports still available.
**Reversible**: Can reopen anytime.
**Note**: No separate "archive" state exists.

### Invitation
**Types**: Team invites (broad access) or Notebook invites (specific).
**Duration**: 7 days validity.
**Permissions**: Determined by role offered.
**Templates**: Only accessible via team membership.

## Dashboard Terms

### Dashboard
**Definition**: Web-based administrative interface for managing Fieldmark projects.
**URL**: Usually `https://dashboard.fieldmark.app` (or organisation-specific URL).
**Contains**: Templates, Notebooks, Users, Teams sections.
**Access**: Browser-based, requires authentication. Desktop/laptop recommended for Notebook Editor use.
**Notebook Editor**: Opens as modal overlay within Dashboard, not a separate page.
**See**: [Dashboard Overview](../dashboard/dashboard-overview.md)

### Team
**Definition**: Organisational unit that owns and manages shared resources.  
**Purpose**: Centralised permission management and resource sharing.  
**Hierarchy**: Teams → Notebooks/Templates → Users.  
**See**: [Teams Interface](../dashboard/teams-interface.md)

### Notebook
**Definition**: Deployed instance of a template where data collection occurs.  
**Context**: Each notebook has its own users, permissions, and records.  
**Creation**: From template or JSON definition.  
**See**: [Notebooks Interface](../dashboard/notebooks-interface.md)

### Template
**Definition**: Reusable design defining notebook structure and validation.  
**Components**: Fields, validation rules, UI configuration.  
**Creation**: Via Designer interface or JSON import.  
**See**: [Templates Interface](../dashboard/templates-interface.md)

### Designer
**Definition**: Alternate name for Notebook Editor - visual interface for creating and editing templates.
**Architecture**: Modal overlay within Dashboard.
**Panels**: DESIGN tab (form builder with "ADD A FIELD" button), INFO tab (metadata).
**Interaction Pattern**: Uses modal dialogs for field selection and inline editing for configuration - NOT drag-and-drop.
**Save Behaviour**: Does NOT auto-save. Clicking SAVE closes Editor and returns to Dashboard.
**Note**: No built-in preview - test in separate browser tab.
**See**: [Designer Component Mapping](./designer-component-mapping.md), [UI Interaction Patterns](./ui-interaction-patterns.md)

### Global Role
**Definition**: System-wide permission level.  
**Types**: GENERAL_USER (default), GENERAL_CREATOR, GENERAL_ADMIN.  
**Scope**: Applies across entire Fieldmark system.  
**Inheritance**: Higher roles inherit lower role permissions.  
**See**: [Roles & Permissions Reference](./roles-permissions-reference.md)

### GENERAL_USER
**Definition**: Default role for all registered users.  
**Permissions**: Basic access, view lists, manage own tokens.  
**Automatic**: Every user has this role.  
**See**: [Global Roles](./roles-permissions-reference.md#1-global-roles-system-wide-essential)

### GENERAL_CREATOR  
**Definition**: Role for users who can create notebooks and templates.  
**Permissions**: CREATE_PROJECT, CREATE_TEMPLATE actions.  
**Key Role**: Required for notebook designers.  
**See**: [Global Roles](./roles-permissions-reference.md#general-creator-content-creator-essential)

### GENERAL_ADMIN
**Definition**: System administrator with full control.  
**Permissions**: All system operations, user management, override access.  
**God Mode**: Inherits all other admin roles automatically.  
**See**: [Global Roles](./roles-permissions-reference.md#general-admin-system-administrator-essential)

### Project Role
**Definition**: Permissions within a specific notebook (project).  
**Types**: PROJECT_GUEST, PROJECT_CONTRIBUTOR, PROJECT_MANAGER, PROJECT_ADMIN.  
**Scope**: Single notebook only.  
**See**: [Notebook Roles](./roles-permissions-reference.md#3-notebook-project-roles-important)

### Team Role
**Definition**: Permissions within a team context.  
**Types**: TEAM_MEMBER, TEAM_MEMBER_CREATOR, TEAM_MANAGER, TEAM_ADMIN.  
**Virtual Roles**: Automatically grants notebook permissions.  
**See**: [Team Roles](./roles-permissions-reference.md#2-team-roles-team-specific-important)

### Virtual Role
**Definition**: Automatic permissions granted through team membership.  
**Example**: TEAM_MEMBER gets PROJECT_CONTRIBUTOR on all team notebooks.  
**Benefit**: Simplifies permission management.  
**See**: [How Team Roles Work](./roles-permissions-reference.md#how-team-roles-work-essential)

### Role Inheritance
**Definition**: Higher roles automatically include lower role permissions.  
**Example**: PROJECT_ADMIN inherits PROJECT_MANAGER permissions.  
**Direction**: Flows from specific to general.  
**See**: [Permission Hierarchy](./roles-permissions-reference.md#permission-hierarchy-essential)

### Invitation
**Definition**: Email-based process for granting access to notebooks or teams.  
**Workflow**: Send → Pending → Accept/Decline → Active.  
**Expiry**: 7 days by default.  
**See**: [Invitation Process](../dashboard/notebooks-interface.md#invitation-process)

### Record Status
**Definition**: Workflow state of collected data.  
**States**: Draft → Submitted → Reviewed → Archived.  
**Transitions**: Role-dependent permissions.  
**See**: [Record Status Workflow](../dashboard/notebooks-interface.md#record-status-workflow)

### Export Formats
**Definition**: Available data output formats from notebooks.  
**Types**: CSV (structured data), Photo Archive (ZIP with HRID-renamed images).  
**Fallback**: Original filenames if no HRID present.  
**See**: [Export Options](../dashboard/notebooks-interface.md#export-options)

### Email Verification
**Definition**: Required confirmation of user email address.  
**Banner**: Persistent reminder until verified.  
**Impact**: Limits certain features until complete.  
**See**: [Email Verification](../dashboard/users-interface.md#email-verification)

### Parametric Workflow
**Definition**: Template-based UI instructions with customisable variables.  
**Format**: Steps with {{VARIABLE}} markers for context-specific values.  
**Purpose**: Enable LLMs to generate customised guidance.  
**See**: [Dashboard Patterns](../dashboard/dashboard-patterns.md)

## Editor Terms

### Data Collection App
**Definition**: Mobile and web application for entering data into activated notebooks.
**URL**: Usually `https://app.fieldmark.app` (separate from Dashboard).
**Platform**: Works on both mobile devices and web browsers.
**Mobile-Only Features**: Barcode/QR code scanning (not available in web browser).
**Offline**: Full offline support for data entry and sync when connection restored.
**See**: [Platform Reference](./platform-reference.md), [UI Interaction Patterns](./ui-interaction-patterns.md)

### Notebook Editor
**Definition**: Modal overlay interface for creating and modifying notebooks and templates, spawned from Dashboard.
**Architecture**: Opens as a modal overlay within Dashboard (same URL), not a separate page or application.
**Usage**: Same editor used for both templates and notebooks.
**Interface**: Form builder using modal dialogs (field type selection) and inline editing (form names, field configuration).
**Save Behaviour**: Does NOT auto-save. Clicking SAVE closes the Editor and returns to Dashboard.
**Access**: Available to team members based on their team role.
**Note**: Sometimes referred to as just "Editor" or "Designer" in the interface.
**See**: [UI Interaction Patterns](./ui-interaction-patterns.md)

### Notebook Info
**Definition**: Notebook Editor page for configuring notebook-level metadata.  
**Location**: Notebook Editor → Info tab.  
**Contains**: Project name, lead, institution, description, custom fields.  
**Purpose**: FAIR data compliance and metadata standards support.  
**See**: [Editor Notebook Info](./editor-notebook-info.md)

### Custom Metadata Fields
**Definition**: User-defined key-value pairs for project-specific metadata.  
**Creation**: Via Info page "Create New Field" interface.  
**Use Cases**: Grant tracking, ethics approval, repository compliance.  
**Format**: All values stored as strings in metadata object.  
**See**: [Editor Notebook Info](./editor-notebook-info.md#custom-metadata-fields)

### Three-tier Metadata System
**Definition**: Fieldmark's hierarchical metadata architecture.  
**Levels**: Notebook (Info) → Record (fields) → Field (annotation/uncertainty).  
**Purpose**: Comprehensive data documentation for FAIR compliance.  
**Implementation**: Info page, form fields, field-level metadata toggles.  
**See**: [Editor Notebook Info](./editor-notebook-info.md#metadata-hierarchy)

### RAiD (Research Activity Identifier)
**Definition**: Persistent identifier system for research projects.  
**Format**: `https://raid.org/10.25917/{{SUFFIX}}`.  
**Integration**: Custom metadata fields in Info page.  
**Purpose**: Project tracking and citation.  
**See**: [Editor Notebook Info](./editor-notebook-info.md#research-activity-identifier-raid)

### FAIR Data Principles
**Definition**: Findable, Accessible, Interoperable, Reusable data standards.  
**Implementation**: Through notebook metadata, permissions, standards compliance.  
**Location**: Configured via Info page metadata.  
**Components**: Identifiers, descriptions, standards, licenses.  
**See**: [Editor Notebook Info](./editor-notebook-info.md#fair-data-implementation)

### Form Settings
**Definition**: Configuration panel in Notebook Editor controlling per-viewset behaviour.  
**Location**: Notebook Editor → Design tab → Form Settings (expandable).  
**Configures**: Finish button logic, layout style, summary fields, HRID.  
**Scope**: Per-form, not global.  
**See**: [Editor Form Settings](./editor-form-settings.md)

### Record List Table  
**Definition**: Primary interface displaying all notebook records in tabular format.  
**Location**: Notebook → Records tab.  
**Customisation**: Via Form Settings → Summary Fields.  
**Default columns**: HRID or UUID if not configured.  
**See**: [Editor Form Settings](./editor-form-settings.md#summary_fields)

### Summary Fields
**Definition**: Fields displayed as columns in record list table.  
**Configuration**: Form Settings → Summary Fields (multi-select).  
**Best Practice**: Select 2-4 most identifying fields.  
**Fallback**: Shows HRID only if none selected.  
**See**: [Editor Form Settings](./editor-form-settings.md#summary_fields)

### publishButtonBehaviour
**Definition**: Validation strategy controlling when forms can be completed.  
**Options**: `always`, `visited`, `noErrors`.  
**UI Label**: "Finish Button Behaviour" in Form Settings.  
**Default**: `"always"` (no restrictions).  
**See**: [Editor Form Settings](./editor-form-settings.md#publishbuttonbehaviour)

### Layout Style
**Definition**: How form sections are displayed to users.
**Options**: `tabs` (horizontal), `inline` (vertical scroll).
**Configuration**: Form Settings → Layout Style.
**Platform**: Mobile often better with inline, desktop with tabs.
**See**: [Editor Form Settings](./editor-form-settings.md#layout)

### Modal Dialog Pattern
**Definition**: UI interaction pattern using pop-up dialogs for complex selections in Notebook Editor.
**Used For**: Field type selection (6-tab categorised modal), conditional logic configuration, templated strings.
**Behaviour**: Opens overlay, user makes selection, modal closes and returns to editor.
**Field Categories**: TEXT, CHOICE, DATE & TIME, MEDIA, LOCATION, STRUCTURED (6 tabs with 1-6 cards each).
**See**: [UI Interaction Patterns](./ui-interaction-patterns.md#1-configuration-patterns-modal-dialogs-and-inline-editing)

### Inline Editing Pattern
**Definition**: UI interaction pattern for direct text and configuration editing in Notebook Editor.
**Used For**: Form names, section names, field configuration settings, Form Settings panel.
**Behaviour**: Click element → edit in place → confirm with checkmark or cancel with X.
**Collapsible Panels**: Form Settings, individual field configuration, Hidden Fields (click grey bar to expand/collapse).
**See**: [UI Interaction Patterns](./ui-interaction-patterns.md#1-configuration-patterns-modal-dialogs-and-inline-editing)

## Acronyms

| Acronym | Full Term | Context |
|---------|-----------|---------|
| HRID | Human-Readable Identifier | User-friendly record IDs |
| XSS | Cross-Site Scripting | Security vulnerability |
| GPS | Global Positioning System | Location capture |
| JSON | JavaScript Object Notation | Data format |
| UI | User Interface | Designer or app interface |
| UUID | Universally Unique Identifier | System-generated IDs |
| CRUD | Create, Read, Update, Delete | Database operations |
| CSV | Comma-Separated Values | Export format |
| ZIP | ZIP Archive | Compressed file format |

---

## Usage Notes

This glossary provides:
1. **Consistent terminology** across all documentation
2. **Clear definitions** for Fieldmark-specific concepts
3. **Cross-references** to detailed documentation
4. **Context** for when and how terms are used

For implementation details, see the referenced documentation sections.

---

*This glossary defines ~60 critical terms for Fieldmark notebook development.*