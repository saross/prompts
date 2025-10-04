#!/bin/bash
# rename-screenshots.sh
# Rename screenshots to final convention based on mapping

RAW_DIR="/home/shawn/Code/prompts/EFN/Docs-staging/production/screenshots/quickstart/raw"
FINAL_DIR="/home/shawn/Code/prompts/EFN/Docs-staging/production/screenshots/quickstart/final"

# Create final directory if it doesn't exist
mkdir -p "$FINAL_DIR"

echo "Renaming screenshots to final convention..."
echo ""

# Getting Started Section
cp "$RAW_DIR/Screenshot from 2025-10-04 14-51-20.png" "$FINAL_DIR/quickstart-001-login.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-40-51.png" "$FINAL_DIR/quickstart-002-dashboard-overview.png"
cp "$RAW_DIR/Screenshot from 2025-10-04 14-52-25.png" "$FINAL_DIR/quickstart-003-notebooks-pagination.png"

# Notebook Editor Interface
cp "$RAW_DIR/Screenshot from 2025-10-02 23-16-05.png" "$FINAL_DIR/quickstart-004-editor-interface.png"

# Form Creation
cp "$RAW_DIR/Screenshot from 2025-10-04 15-20-36.png" "$FINAL_DIR/quickstart-005-form-name-editing.png"
cp "$RAW_DIR/Screenshot from 2025-10-01 22-06-00.png" "$FINAL_DIR/quickstart-006-form-created.png"
cp "$RAW_DIR/Screenshot from 2025-10-04 14-35-41.png" "$FINAL_DIR/quickstart-007-section-name-editing.png"
cp "$RAW_DIR/Screenshot from 2025-10-01 22-14-51.png" "$FINAL_DIR/quickstart-008-section-created.png"

# Field 1: Site Name
cp "$RAW_DIR/Screenshot from 2025-10-04 14-36-50.png" "$FINAL_DIR/quickstart-009-add-field-site-name.png"
cp "$RAW_DIR/Screenshot from 2025-10-04 14-38-42.png" "$FINAL_DIR/quickstart-010-site-name-expanded.png"

# Field 2: Site Type
cp "$RAW_DIR/Screenshot from 2025-10-02 15-38-57.png" "$FINAL_DIR/quickstart-011-add-field-choice.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 15-53-41.png" "$FINAL_DIR/quickstart-012-edit-option-habitation.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 15-58-56.png" "$FINAL_DIR/quickstart-013-site-type-expanded.png"

# Field 3: Survey Date
cp "$RAW_DIR/Screenshot from 2025-10-02 16-08-37.png" "$FINAL_DIR/quickstart-014-add-field-datetime.png"
cp "$RAW_DIR/Screenshot from 2025-10-04 14-40-53.png" "$FINAL_DIR/quickstart-015-survey-date-expanded.png"

# Field 4: Observations
cp "$RAW_DIR/Screenshot from 2025-10-02 17-15-31.png" "$FINAL_DIR/quickstart-016-add-field-text.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 17-18-22.png" "$FINAL_DIR/quickstart-017-observations-expanded.png"

# Field 5: Site Photo
cp "$RAW_DIR/Screenshot from 2025-10-04 14-42-53.png" "$FINAL_DIR/quickstart-018-add-field-media.png"
cp "$RAW_DIR/Screenshot from 2025-10-04 14-44-10.png" "$FINAL_DIR/quickstart-019-site-photo-expanded.png"

# Form Settings
cp "$RAW_DIR/Screenshot from 2025-10-02 17-36-14.png" "$FINAL_DIR/quickstart-020-all-fields-visible.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 17-29-25.png" "$FINAL_DIR/quickstart-021-form-settings-panel.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 17-37-35.png" "$FINAL_DIR/quickstart-022-form-settings-configured.png"

# Activation Workflow
cp "$RAW_DIR/Screenshot from 2025-10-04 14-50-33.png" "$FINAL_DIR/quickstart-023-active-zero.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 17-53-59.png" "$FINAL_DIR/quickstart-024-not-active-tab.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-01-18.png" "$FINAL_DIR/quickstart-025-activating-modal.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-02-37.png" "$FINAL_DIR/quickstart-026-active-one.png"

# Data Collection
cp "$RAW_DIR/Screenshot from 2025-10-02 18-14-40.png" "$FINAL_DIR/quickstart-027-empty-notebook.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-17-28.png" "$FINAL_DIR/quickstart-028-form-33-percent.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-29-16.png" "$FINAL_DIR/quickstart-029-annotation-interface.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-22-20.png" "$FINAL_DIR/quickstart-030-form-100-percent.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-25-25.png" "$FINAL_DIR/quickstart-031-datetime-picker.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-33-31.png" "$FINAL_DIR/quickstart-032-record-not-synced.png"
cp "$RAW_DIR/Screenshot from 2025-10-02 18-38-31.png" "$FINAL_DIR/quickstart-033-record-synced.png"
cp "$RAW_DIR/Screenshot from 2025-10-04 14-53-55.png" "$FINAL_DIR/quickstart-034-settings-tab.png"

echo "✓ Renamed 34 screenshots"
echo ""
echo "Final screenshots saved to:"
echo "$FINAL_DIR"
