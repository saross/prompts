<!-- concat:boundary:start section="templates-interface" -->
<!-- concat:metadata
document_id: templates-interface
category: ui_management
designer_integration: true
json_generation: true
last_updated: 2025-09-08
-->

<!-- discovery:metadata
provides: [template-management, designer-usage, field-configuration, version-control]
see-also: [designer-component-mapping, field-selection-guide, notebooks-interface, dashboard-patterns]
-->

# Templates Interface

<!-- structured:metadata
meta:purpose: template-management
meta:summary: Template creation, editing, and management through Designer interface with JSON schema generation.
meta:generates: template-json
meta:requires: [template-designer-role, designer-access]
meta:version: 3.0.0
meta:document: templates_interface
meta:depth-tags: [essential, important, comprehensive]
-->

## Document Navigation {essential}
<!-- concat:nav-mode:individual -->
[← Dashboard Overview](./dashboard-overview.md) | **Templates Interface** | [Notebooks Interface →](./notebooks-interface.md)
<!-- concat:nav-mode:concatenated -->
<!-- When viewing in reference.md: [↑ Dashboard Overview](#dashboard-overview) | [Notebooks Interface ↓](#notebooks-interface) -->

## Overview {essential}

Templates define the structure and behaviour of data collection notebooks. They contain:
- Field definitions and types
- Validation rules and constraints
- UI configurations and layouts
- Conditional logic and relationships
- Human-readable identifier patterns

**Template Editor Context**: Templates are created and edited using the Notebook Editor, which opens as a modal overlay within the Dashboard. The Editor does NOT auto-save - clicking SAVE closes the Editor and returns to the Dashboard template list.

### Access Requirements {essential}

- **Team Role**: Team members can create/edit templates based on their team role
- **Team Context**: Team Administrator (for team templates)
- **Permissions**: Create, edit, clone templates

## Main Templates List {essential}

The templates interface displays all available templates:

### List View Components

| Element | Description | Actions |
|---------|-------------|---------|
| **Filter Bar** | Search by name/metadata | Type to filter |
| **Create Template** | Initiates new template | Opens creation dialog |
| **Template Cards** | Individual template entries | Click to view details |

### Template Entry Information

Each template shows:
- Template name
- Description (truncated)
- Owner (user or team)
- Creation date
- Last modified date
- Notebook count (using this template)

## Template Creation Pathways {essential}

### Method 1: From Scratch
```
Templates > Create Template > Start from scratch
→ Creates empty template → Returns to templates list
→ Navigate to new template > Actions tab > Open in Editor
```

**Post-Creation Navigation**: After creating a template, you return to the templates list. New templates appear at the END of the list, not the top.

**To Access Your New Template**:
1. **Option A - Search**: Use the search/filter bar at the top of the list to search by template name
2. **Option B - Scroll**: Navigate to the end of the list
3. **Option C - Pagination**: If applicable, navigate to the last page

**Once Located**:
1. Click on the template name
2. Click the **Actions** tab
3. Click **"Open in Editor"** button
4. Notebook Editor opens as a modal overlay within Dashboard
5. Build your template (add forms, fields, configure validation)
6. Click green **SAVE** button (top-right) to save and close Editor
7. You return to Dashboard template list

**Critical**: The Notebook Editor does NOT auto-save. Clicking SAVE closes the Editor and returns you to the Dashboard. This is the intended behaviour. To resume editing, repeat steps 1-4 above.

### Method 2: From JSON File
```
Templates > Create Template > Upload JSON file
→ Imports existing definition
```

### Method 3: From Existing Template
```
Templates > View Template > Clone
→ Creates copy for modification
```

### Creation Dialog Fields

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| **Template Name** | Yes | Unique identifier | {{TEMPLATE_NAME}} |
| **Description** | No | Purpose and usage notes | {{TEMPLATE_DESC}} |
| **JSON File** | No | For import method | {{JSON_FILE_PATH}} |
| **Team Assignment** | No | If created from team context | {{TEAM_NAME}} |

## Designer/Editor Interface {important}

The Notebook Editor (also called "Designer") is a modal overlay interface for building templates. It opens within the Dashboard when you click "Open in Editor" from a template's Actions tab.

**Architecture**: Modal overlay within Dashboard (same URL), not a separate page or application.

**Save Behaviour**: Does NOT auto-save. Clicking SAVE closes the Editor and returns to Dashboard.

**See**: [UI Interaction Patterns](../references/ui-interaction-patterns.md#14-save-behaviour-in-notebook-editor) for complete workflow details.

### Interface Structure

#### Left Panel: Template Metadata (Info Page)
- **Notebook Name**: Display name for notebooks
- **Description**: Detailed template purpose
- **Version**: Manual version number (e.g., "1.0.0")
- **Author**: Creator identification
- **Project**: Associated project name

⚠️ **Version Control Note**: Version numbers are manually maintained metadata, not automated versioning.

#### Centre Panel: Form Builder
- **Forms**: Add using "ADD NEW FORM" button
- **Sections**: Logical groupings of fields within forms
- **Fields**: Add using "ADD A FIELD" button (opens modal dialog with 6 categorised tabs)
- **Field Order**: Use interface controls to reorder
- **Field Actions**: Click grey bar to expand/collapse, configure, duplicate, delete

📝 **Preview Note**: No built-in preview. Keep Fieldmark web app open in separate tab for testing. Updates reflect quickly after saving.

**Field Addition Workflow**:
1. Click "ADD A FIELD" button
2. Modal dialog opens with 6 tabs: TEXT, CHOICE, DATE & TIME, MEDIA, LOCATION, STRUCTURED
3. Select tab category, then click component card (hover for helper text)
4. Modal closes, field appears in collapsed state in "Visible Fields" list
5. Click grey bar to expand field and configure settings inline

**See**: [UI Interaction Patterns](../references/ui-interaction-patterns.md#1-configuration-patterns-modal-dialogs-and-inline-editing) for complete interaction details.

#### Right Panel: Field Properties (Inline Editing)
When a field is expanded, configure properties inline:
- **Field Identifier**: Unique field name (JSON key)
- **Display Label**: User-visible text
- **Field Type**: Component selection (from modal)
- **Validation**: Rules and constraints
- **Help Text**: User guidance
- **Conditional Logic**: Show/hide rules (configured via modal dialog)

### Designer Field Selection {important}

**Critical Naming Clarification**:

| Designer Name | Component Created | Use Case |
|---------------|------------------|----------|
| **FAIMS Text Field** | FAIMSTextField | Single-line text |
| **Text Field** | MultipleTextField | Multi-line text |
| **Email** | TextField (configured) | Email validation |

⚠️ This naming inconsistency causes significant confusion. Always verify component-name in JSON.

### Available Field Categories {essential}

For complete field documentation, see:
- [Text Fields](../field-categories/text-fields-v05.md) - Including HRID configuration
- [Selection Fields](../field-categories/select-choice-fields-v05.md) - RadioGroup, Select, MultiSelect
- [Date/Time Fields](../field-categories/datetime-fields-v05.md) - Date pickers and timestamps
- [Number Fields](../field-categories/number-fields-v05.md) - Auto-increment and validation
- [Location Fields](../field-categories/location-fields-v05.md) - GPS capture and mapping
- [Media Fields](../field-categories/media-fields-v05.md) - Photo and file uploads
- [Relationship Field](../field-categories/relationship-field-v05.md) - Record linking
- [Display Field](../field-categories/display-field-v05.md) - RichText markdown

For Designer-specific mappings:
→ [Designer Component Mapping](../references/designer-component-mapping.md) - **Critical reference**
→ [Component Reference](../references/component-reference.md) - Namespaces and types
→ [Constraints Reference](../references/constraints-reference.md) - Designer limitations

## Template Configuration {important}

### Required Components

Every template MUST include:

1. **HRID Field** (TemplatedString)
   ```json
   "{{HRID_FIELD_ID}}": {
     "component-namespace": "faims-custom",
     "component-name": "TemplatedStringField",
     "component-parameters": {
       "template": "{{PROJECT_ABBREV}}-{{_YYYY}}-{{auto_increment}}"
     }
   }
   ```
   Without HRID, records display as UUIDs (e.g., `a7f3b2c1-d4e5-6789-0abc`)

2. **Form Structure** (fviews layer)
   ```json
   "fviews": {
     "{{FORM_ID}}": {
       "fields": ["{{FIELD_ID_1}}", "{{FIELD_ID_2}}"],
       "views": ["{{SECTION_ID_1}}", "{{SECTION_ID_2}}"]
     }
   }
   ```

3. **Field Name Parameters**
   ```json
   "component-parameters": {
     "name": "{{FIELD_ID}}"  // Must match field key
   }
   ```

### Validation Configuration {comprehensive}

Templates support Yup validation schema:

```json
"validationSchema": [
  ["yup.string"],
  ["yup.required", "{{VALIDATION_MESSAGE}}"],
  ["yup.min", 10, "Minimum 10 characters"],
  ["yup.matches", "^[A-Z]", "Must start with capital"]
]
```

Common validation patterns:
- Required fields: `["yup.required", "Field is required"]`
- String length: `["yup.min", 5]`, `["yup.max", 100]`
- Number ranges: `["yup.min", 0]`, `["yup.max", 100]`
- Date ranges: `["yup.min", ["yup.ref", "start_date"]]`
- Pattern matching: `["yup.matches", "regex", "message"]`

For parametric validation recipes:
→ [Cookbook](../patterns/cookbook.md) - Date range validation, cascading selects
→ [Dynamic Forms Guide](../patterns/dynamic-forms-guide.md) - Cross-field validation

### Conditional Logic {comprehensive}

Templates support field visibility conditions:

```json
"is_visible_when": [
  {
    "field": "{{TRIGGER_FIELD_ID}}",
    "operator": "equals",
    "value": "{{TRIGGER_VALUE}}"
  }
]
```

Supported operators:
- `equals`: Exact match
- `not_equals`: Not matching
- `contains`: Substring present
- `not_contains`: Substring absent
- `greater_than`: Numeric comparison
- `less_than`: Numeric comparison

## Template Management {important}

### Template Details View

Accessed by clicking a template from the list:

#### Available Tabs

| Tab | Content | Actions |
|-----|---------|---------|
| **Details** | Metadata and info | View template properties |
| **Notebooks** | Using this template | View deployed notebooks |
| **Actions** | Management operations | Edit, Clone, Export, Delete |

#### Details Tab Content
- Template name and identifier
- Description of purpose
- Version number (manually maintained)
- Author information
- Creation and modification timestamps
- Associated team (if applicable)

#### Notebooks Tab Content
- List of all notebooks using this template
- Notebook names (clickable links)
- Status indicators (Open/Closed)
- Record counts
- Team ownership
- Deployment dates

#### Actions Tab Operations

1. **Edit Template**
   - Opens template in the Notebook Editor
   - Requires TEMPLATE_ADMIN or GENERAL_CREATOR permission
   - Button label: "Open in Editor"

2. **Assign Template to Team**
   - Associates template with a team for management
   - Requires appropriate team permissions
   - Button label: "Assign Template to Team"

3. **Download JSON**
   - Exports the complete template definition
   - Available to all authenticated users
   - Downloads as .json file

4. **Replace Template JSON File**
   - Upload new JSON to update template structure
   - Requires TEMPLATE_ADMIN permission
   - Validates JSON before replacement

5. **Create Notebook**
   - Deploy new notebook from this template
   - Requires GENERAL_CREATOR or team permissions
   - Button label: "Create Notebook"

6. **Archive Template**
   - Mark template as archived/inactive
   - Requires TEMPLATE_ADMIN permission
   - Archived templates remain accessible but not in active lists

**Note**: Clone operation may be available through Edit or as separate action depending on permissions.

### Template Testing {important}

**Recommended Testing Workflow**:

1. Save template in Designer
2. Switch to Fieldmark web app tab
3. Create test notebook from template
4. Enter sample data
5. Identify issues
6. Return to Designer and modify
7. Repeat until satisfied

## JSON Export/Import {comprehensive}

### Export Process
```
Template Details > Export > Download JSON
```

Exported JSON includes:
- Complete field definitions
- Validation schemas
- UI configurations
- Metadata

### Import Process
```
Create Template > Choose File > Select JSON
```

Import requirements:
- Valid JSON syntax
- Unique field identifiers
- Required fviews structure
- Compatible component names

### JSON Enhancement Requirements {comprehensive}

You must edit JSON directly for:

**Advanced Validation**:
- Complex regex patterns
- Cross-field validation
- Custom error messages
- Dynamic validation rules

**Performance Optimisation**:
- Large text field limits
- Async validation
- Debounced inputs
- Lazy loading

**Security Configurations**:
- XSS prevention in templates
- Input sanitisation
- File upload restrictions
- API endpoint security

## Team-Owned Templates {important}

When created from team context:

### Ownership Benefits
- Centralised management
- Shared access for team members
- Consistent project standards
- Simplified permissions

### Creation from Team
```
Teams > {{TEAM_NAME}} > Templates > Create Template
```

Automatically:
- Assigns team ownership
- Grants team admin edit rights
- Makes visible to team members

## Template Best Practices {important}

### Naming Conventions
```
{{PROJECT}}-{{TYPE}}-{{VERSION}}
Example: CSIRO-Survey-v2.1
```

### Version Management
- Use semantic versioning (1.0.0)
- Document changes in description
- Never modify templates with active notebooks
- Clone for major changes

### Field Organisation
- Group related fields in sections
- Order by data collection flow
- Provide clear help text
- Use consistent naming patterns

### Performance Considerations
- Limit fields per section (<20)
- Avoid deep nesting
- Optimise conditional logic
- Test on mobile devices

## Common Issues {comprehensive}

### Template Won't Import

| Issue | Solution |
|-------|----------|
| Invalid JSON | Validate with JSON linter |
| Missing fviews | Add form structure layer |
| Duplicate IDs | Ensure unique field names |
| Unknown components | Check component-name spelling |

### Designer Limitations

| Limitation | Workaround |
|-----------|------------|
| No preview | Use separate browser tab |
| Can't set all properties | Edit JSON after export |
| Complex logic not supported | Use JSON for advanced features |
| No undo/redo | Save versions frequently |

### Field Configuration Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Field not appearing | Not in fviews.fields | Add to form structure |
| Validation not working | Missing name parameter | Ensure name matches ID |
| Label not showing | Missing label parameter | Add to component-parameters |

## Cross-References {important}

For detailed field configuration:
→ [Designer Component Mapping](../references/designer-component-mapping.md)

For field selection guidance:
→ [Field Selection Guide](../patterns/field-selection-guide.md)

For JSON structure details:
→ [Notebook Format Guide](../references/notebook-format-guide.md)

For deployment:
→ [Notebooks Interface](./notebooks-interface.md)

<!-- concat:boundary:end section="templates-interface" -->