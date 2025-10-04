#!/usr/bin/env python3
"""
update-screenshots.py
Replace screenshot placeholders with actual image references and alt text
"""

import re

# Define all screenshot replacements with descriptive alt text
replacements = [
    # Line 25 - URLs (skipped, text-only by agreement)
    (
        r'\[SCREENSHOT: Two browser windows side by side showing Dashboard \(api\.fieldmark\.app\) and Data Collection App \(app\.fieldmark\.app\) URLs with labels\]',
        '<!-- URLs comparison explained in text above - no screenshot needed -->'
    ),
    # Line 49 - Login
    (
        r'\[SCREENSHOT: Login page with email and password fields\]',
        '![Fieldmark login page with Email Address and Password fields, along with Sign in button and Continue with Google option](../screenshots/quickstart/final/quickstart-001-login.png)'
    ),
    # Line 59 - Dashboard Overview
    (
        r'\[SCREENSHOT: Dashboard Overview showing the main navigation and Create buttons\]',
        '![Fieldmark Dashboard showing left sidebar with Notebooks, Templates navigation and main content area with notebook list and Create Notebook button](../screenshots/quickstart/final/quickstart-002-dashboard-overview.png)'
    ),
    # Line 84 - Notebooks interface
    (
        r'\[SCREENSHOT: Notebooks interface showing Create Notebook button\]',
        '![Dashboard Notebooks view showing the notebook list table and Create Notebook button in the upper right](../screenshots/quickstart/final/quickstart-002-dashboard-overview.png)'
    ),
    # Line 105 - Pagination
    (
        r'\[SCREENSHOT: Notebook list showing pagination controls at bottom \("< 1 2 3 >"\) and search bar at top, with arrow pointing to "My First Survey" at end of list\]',
        '![Dashboard notebook list showing pagination controls at bottom (Page 1 of 6) and Filter results search bar at top of the table](../screenshots/quickstart/final/quickstart-003-notebooks-pagination.png)'
    ),
    # Line 115 - Editor interface
    (
        r'\[SCREENSHOT: Notebook Editor interface showing the form builder layout\]',
        '![Notebook Editor showing DESIGN and INFO tabs, UNDO/REDO buttons, Form Name field with "Form 1", ADD NEW FORM button, and blue info box explaining the form building process](../screenshots/quickstart/final/quickstart-004-editor-interface.png)'
    ),
    # Line 128 - UNDO/REDO
    (
        r'\[SCREENSHOT: Close-up of Editor showing UNDO and REDO buttons below top bar, above tabs\]',
        '![Close-up view of Notebook Editor showing UNDO and REDO buttons positioned below the top bar (with CANCEL and SAVE) and above the DESIGN/INFO tabs](../screenshots/quickstart/final/quickstart-004-editor-interface.png)'
    ),
    # Line 163 - Form name editing
    (
        r'\[SCREENSHOT: Form Name field being edited to "Site Details", ADD NEW FORM button highlighted\]',
        '![Notebook Editor with EDIT FORM NAME active, showing inline editor with "Site Details" entered and checkmark/X buttons for confirming or canceling the edit](../screenshots/quickstart/final/quickstart-005-form-name-editing.png)'
    ),
    # Line 174 - Form created
    (
        r'\[SCREENSHOT: Created form showing "Site Details" with success message and Section Name field\]',
        '![Form successfully created showing "FORM: SITE DETAILS" badge, green success message "Form has been created. Add a section to get started", DELETE FORM and EDIT FORM NAME options, Form Settings panel, and Section Name input field](../screenshots/quickstart/final/quickstart-006-form-created.png)'
    ),
    # Line 186 - Section name editing
    (
        r'\[SCREENSHOT: Section Name field being edited to "Basic Information", "\+" button highlighted\]',
        '![Section Name field with "Basic Information" entered and green "+" button next to it for creating the section](../screenshots/quickstart/final/quickstart-007-section-name-editing.png)'
    ),
    # Line 197 - Section created
    (
        r'\[SCREENSHOT: Created section showing "Basic Information" with editing controls and "ADD A FIELD" button visible\]',
        '![Section successfully created showing numbered badge "1", section title "Basic Information", section editing controls (DELETE SECTION, DUPLICATE SECTION, MOVE SECTION, EDIT SECTION NAME, ADD NEW SECTION), ADD CONDITION button, green ADD A FIELD button, and Visible Fields/Hidden Fields areas](../screenshots/quickstart/final/quickstart-008-section-created.png)'
    ),
    # Line 219 - Add field Site Name
    (
        r'\[SCREENSHOT: "Add a field" dialog showing field name changed to "Site Name" and "FAIMS Text Field" selected\]',
        '![Add a field modal dialog with "Site Name" entered in the Field name box, TEXT tab active, and "FAIMS Text Field" option highlighted with green border](../screenshots/quickstart/final/quickstart-009-add-field-site-name.png)'
    ),
    # Line 228 - Site Name expanded
    (
        r'\[SCREENSHOT: Expanded "Site Name" field showing configuration options with Required toggled on\]',
        '![Expanded Site Name field showing Label "Site Name", Field ID "Site-Name", Helper Text "Enter the official site designation or name", Required checkbox checked with green checkmark, and additional options like Annotation, Uncertainty, Copy value to new records](../screenshots/quickstart/final/quickstart-010-site-name-expanded.png)'
    ),
    # Line 250 - Add field choice
    (
        r'\[SCREENSHOT: "Add a field" dialog showing CHOICE category with "Select one option" highlighted\]',
        '![Add a field modal dialog showing CHOICE tab active with field types including Checkbox, Select Multiple, and "Select one option" (radio buttons) highlighted with green border](../screenshots/quickstart/final/quickstart-011-add-field-choice.png)'
    ),
    # Line 262 - Edit option
    (
        r'\[SCREENSHOT: Edit Option dialog showing changing "1" to "Habitation"\]',
        '![Edit Option modal dialog with Option Text field showing "1" being changed to "Habitation", and CANCEL/SAVE buttons at bottom](../screenshots/quickstart/final/quickstart-012-edit-option-habitation.png)'
    ),
    # Line 272 - Site Type expanded
    (
        r'\[SCREENSHOT: Expanded "Site Type" field showing options list and Required/Annotation/Uncertainty enabled\]',
        '![Expanded Site Type field showing complete options list (Habitation, Mortuary, Ceremonial, Workshop/Industrial, Defensive, Agricultural, Other) with drag handles, Required checkbox checked, Annotation checkbox checked with label "annotation", and Uncertainty checkbox checked with label "uncertainty"](../screenshots/quickstart/final/quickstart-013-site-type-expanded.png)'
    ),
    # Line 305 - Add field datetime
    (
        r'\[SCREENSHOT: "Add a field" dialog showing DATE & TIME tab with "Date and Time with Now button" highlighted\]',
        '![Add a field modal dialog with DATE & TIME tab active showing field types including Date time picker, Date picker, Month picker, and "Date and Time with Now button" highlighted with green border](../screenshots/quickstart/final/quickstart-014-add-field-datetime.png)'
    ),
    # Line 315 - Survey Date expanded
    (
        r'\[SCREENSHOT: Expanded "Survey Date" field showing configuration with Time pre-populated and Required enabled\]',
        '![Expanded Survey Date field showing Label "Survey Date", Field ID "Survey-Date", Helper Text "Date and time when this site was surveyed" with green highlight, Time pre-populated checkbox checked with green checkmark and explanation text, Required checkbox checked, and other configuration options](../screenshots/quickstart/final/quickstart-015-survey-date-expanded.png)'
    ),
    # Line 335 - Add field text
    (
        r'\[SCREENSHOT: "Add a field" dialog showing TEXT tab with "Text Field" highlighted\]',
        '![Add a field modal dialog with "Observations" entered as field name, TEXT tab active, showing field types including FAIMS Text Field, Email, "Text Field" highlighted, and other text-based options](../screenshots/quickstart/final/quickstart-016-add-field-text.png)'
    ),
    # Line 344 - Observations expanded
    (
        r'\[SCREENSHOT: Expanded "Observations" field showing configuration\]',
        '![Expanded Observations field showing Label "Observations", Field ID "Observations", Helper Text "Describe site conditions, features, and any notable characteristics", Rows to display set to 4, and configuration checkboxes for Required, Annotation, Uncertainty](../screenshots/quickstart/final/quickstart-017-observations-expanded.png)'
    ),
    # Line 367 - Add field media
    (
        r'\[SCREENSHOT: "Add a field" dialog showing MEDIA tab with "Take Photo" highlighted\]',
        '![Add a field modal dialog with "Site Photo" entered as field name, MEDIA tab active, showing "Upload a File" and "Take Photo" options with Take Photo highlighted with green border](../screenshots/quickstart/final/quickstart-018-add-field-media.png)'
    ),
    # Line 378 - Site Photo expanded
    (
        r'\[SCREENSHOT: Expanded "Site Photo" field showing configuration\]',
        '![Expanded Site Photo field in collapsed list view and detailed configuration view showing Label "Site Photo", Field ID "Site-Photo", Helper Text "Photograph the site for documentation", Annotation checkbox checked with custom label "Photo notes", and other configuration options](../screenshots/quickstart/final/quickstart-019-site-photo-expanded.png)'
    ),
    # Line 387 - All fields visible
    (
        r'\[SCREENSHOT: All five fields visible in Visible Fields list\]',
        '![Visible Fields section showing all five collapsed fields in order: Site Name (FAIMSTextField, Required badge), Site Type (RadioGroup, Required badge), Survey Date (DateTimeNow, Required badge), Observations (MultipleTextField), Site Photo (TakePhoto)](../screenshots/quickstart/final/quickstart-020-all-fields-visible.png)'
    ),
    # Line 393 - Form Settings panel
    (
        r'\[SCREENSHOT: Form Settings panel at the top showing configuration options\]',
        '![Form Settings panel showing configuration options including Finish Button Behavior, Layout Style, Summary Fields, and Human-Readable ID Field dropdowns](../screenshots/quickstart/final/quickstart-021-form-settings-panel.png)'
    ),
    # Line 403 - Form Settings configured
    (
        r'\[SCREENSHOT: Form Settings panel showing configured selections - Always Show, Tabs, Site Name \+ Site Type selected, Site Name as HRID\]',
        '![Form Settings panel fully configured showing Finish Button Behavior set to "Always Show", Layout Style set to "Tabs", Summary Fields showing "Site Name ×" and "Site Type ×" tags, and Human-Readable ID Field set to "Site Name"](../screenshots/quickstart/final/quickstart-022-form-settings-configured.png)'
    ),
    # Line 441 - Active 0
    (
        r'\[SCREENSHOT: Fieldmark app "My Notebooks" home screen showing ACTIVE \(0\) and NOT ACTIVE tabs\]',
        '![Fieldmark mobile app My Notebooks screen showing ACTIVE (0) tab selected with empty state message explaining notebooks need to be activated, and NOT ACTIVE (90) tab visible, plus REFRESH NOTEBOOKS button](../screenshots/quickstart/final/quickstart-023-active-zero.png)'
    ),
    # Line 447 - NOT ACTIVE tab
    (
        r'\[SCREENSHOT: NOT ACTIVE tab showing list of notebooks with ACTIVATE buttons\]',
        '![NOT ACTIVE tab showing list of available notebooks with green ACTIVATE buttons next to each, including notebooks like "Map Tester May", "Groundwater", "NIMY Nathan", and others, with horizontal scroll for pagination](../screenshots/quickstart/final/quickstart-024-not-active-tab.png)'
    ),
    # Line 455 - Activating modal
    (
        r'\[SCREENSHOT: "Activating Notebooks" modal dialog with warning and ACTIVATE/CANCEL buttons\]',
        '![Activating Notebooks modal dialog with blue information icon, explanation text about offline functionality and data downloading, warning about stable internet connection, note about de-activation not being available yet, and green ACTIVATE and CANCEL buttons at bottom](../screenshots/quickstart/final/quickstart-025-activating-modal.png)'
    ),
    # Line 464 - Active 1
    (
        r'\[SCREENSHOT: ACTIVE \(1\) tab showing "Quickstart-test" notebook in the list\]',
        '![ACTIVE (1) tab showing Quickstart-test notebook in the list with Name column header and pagination showing 1-1 of 1](../screenshots/quickstart/final/quickstart-026-active-one.png)'
    ),
    # Line 497 - Empty notebook
    (
        r'\[SCREENSHOT: Empty notebook view showing interface elements and empty table with column headers\]',
        '![Empty Quickstart-test notebook showing ADD NEW SITE DETAILS button (orange), REFRESH RECORDS button (green), MY SITE DETAILSS (0) tab, DETAILS, SETTINGS, and MAP tabs, empty table with column headers (Sync, Site Name, Site Type, Created, Created By, Last Updated, Last Updated By), "No rows" message, search bar, Filters button, and pagination showing 0-0 of 0](../screenshots/quickstart/final/quickstart-027-empty-notebook.png)'
    ),
    # Line 505 - Form 33%
    (
        r'\[SCREENSHOT: Data entry form showing Site Name and Site Type fields with progress bar at 33%\]',
        '![Data entry form for Site Details showing 33% Completed progress bar at top, Site Name field (required, marked with red asterisk) with helper text, Site Type radio button field (required) showing options Habitation through Other with blue dog ear annotation icon, checkmark and save icons in top right](../screenshots/quickstart/final/quickstart-028-form-33-percent.png)'
    ),
    # Line 517 - Annotation interface
    (
        r'\[SCREENSHOT: Site Type with annotation interface expanded showing "annotation" text area with "This site is likely a dwelling but may be a workshop\." and "uncertainty" checkbox checked\]',
        '![Site Type field with annotation interface expanded below, showing annotation text area containing "This site is likely a dwelling but may be a workshop." and uncertainty checkbox checked below it](../screenshots/quickstart/final/quickstart-029-annotation-interface.png)'
    ),
    # Line 545 - Form 100%
    (
        r'\[SCREENSHOT: Complete filled form showing all fields populated, 100% completion bar, with "TAKE FIRST PHOTO" button visible\]',
        '![Complete data entry form showing 100% Completed progress bar, all fields filled including Site Name "Test Location Alpha", Site Type "Habitation" selected with annotation, Survey Date populated "02/10/2025, 18:17:14", Observations text entered, Site Photo section showing "No Photos Yet" with green TAKE FIRST PHOTO button](../screenshots/quickstart/final/quickstart-030-form-100-percent.png)'
    ),
    # Line 557 - Datetime picker
    (
        r'\[SCREENSHOT: Bottom of form showing date/time picker open and three action buttons\]',
        '![Bottom of form showing Survey Date field with calendar picker open displaying October 2025 month view with time selectors (18, 24, 55), Clear and Today links, and form action buttons below: FINISH AND CLOSE SITE-DETAILS (green), FINISH AND NEW SITE-DETAILS (orange text), and CANCEL (orange)](../screenshots/quickstart/final/quickstart-031-datetime-picker.png)'
    ),
    # Line 565 - Record not synced
    (
        r'\[SCREENSHOT: Record list showing "MY SITE DETAILSS \(1\)" tab with table displaying one row: orange sync icon, "Test Location Alpha", "Habitation", creation timestamp, username\]',
        '![Record list showing MY SITE DETAILSS (1) tab with table containing one record: orange three-dot sync icon in Sync column, "Test Location Alpha" in Site Name, "Habitation" in Site Type, "2025-10-02 18:32:49" in Created, "shawn@fieldnote.com.au" in Created By and Last Updated By columns, pagination showing 1-1 of 1](../screenshots/quickstart/final/quickstart-032-record-not-synced.png)'
    ),
    # Line 582 - Record synced
    (
        r'\[SCREENSHOT: Record list showing green cloud with checkmark icon in Sync column, indicating successful sync\]',
        '![Record list showing same record with green cloud and checkmark icon in Sync column indicating successful synchronization to server](../screenshots/quickstart/final/quickstart-033-record-synced.png)'
    ),
    # Line 590 - Settings tab
    (
        r'\[SCREENSHOT: SETTINGS tab showing "Sync Notebook" toggle ON, "Get attachments from other devices" toggle Off, and "Deactivate Notebook" section\]',
        '![SETTINGS tab showing Sync Notebook section with toggle switch ON and explanation text, Get attachments from other devices section with toggle Off and detailed explanation about trade-offs, and Deactivate Notebook section with warning text and red DEACTIVATE NOTEBOOK button](../screenshots/quickstart/final/quickstart-034-settings-tab.png)'
    ),
]

def update_screenshots(input_file, output_file):
    """Replace all screenshot placeholders with actual references"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply all replacements
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    # Write updated content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Updated {len(replacements)} screenshot references")
    print(f"✓ Output written to: {output_file}")

if __name__ == "__main__":
    input_file = "/home/shawn/Code/prompts/EFN/Docs-staging/production/human-facing/quickstart-creation-and-collection.md"
    output_file = input_file  # Overwrite original

    update_screenshots(input_file, output_file)
