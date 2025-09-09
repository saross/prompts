# Screenshot Integration Workflow - Complete Implementation Guide

**Created**: 2025-01-08  
**Purpose**: Practical guide for integrating screenshots into documentation using vision models  
**Status**: Ready for implementation

## Quick Start Checklist

- [ ] llama3.2-vision:11b installed locally (`ollama pull llama3.2-vision:11b`)
- [ ] Screenshots captured and organized
- [ ] Documentation with placeholders ready
- [ ] Scripts from this guide saved to `/scripts/` folder

---

## Part 1: Placeholder System Reference

### Standard Placeholders We Use

#### Basic Screenshot
```markdown
[SCREENSHOT: Description of what should be shown]
```

#### Screenshot with Annotations
```markdown
[SCREENSHOT: Login page
 HIGHLIGHT: Email field (red box)
 HIGHLIGHT: Password field (red box)
 CIRCLE: Sign In button (green circle)
 ARROW: Points to "Forgot Password" link
 CALLOUT: "Enter your credentials here"]
```

#### Platform-Specific
```markdown
[SCREENSHOT-DESKTOP: Dashboard main view]
[SCREENSHOT-MOBILE: Dashboard main view with menu collapsed]
```

#### Navigation & Validation
```markdown
[LOCATION: Save button - specify exact position]
[VISUAL CHECK: 5 fields should be visible]
[NAVIGATE: Settings > Notebooks > Create]
[SUCCESS STATE: Green checkmark appears]
[ERROR STATE: Red error message below field]
```

---

## Part 2: Screenshot Capture Strategy

### Naming Convention
```bash
# Pattern: context-component-state-number.png
dashboard-home-empty-01.png
dashboard-create-notebook-dialog-02.png
editor-fields-configured-03.png
notebook-record-saved-success-04.png
```

### Organized Folder Structure
```
/screenshots/
  /quickstart/          # For quickstart guide
  /field-guide/         # For field user guide
  /dashboard/           # For dashboard docs
  /workflows/           # Multi-step processes
  /errors/              # Error states
  /mobile/              # Mobile-specific
```

---

## Part 3: Vision Model Processing Scripts

### Script 1: Single Screenshot Analyzer
```bash
#!/bin/bash
# analyze-screenshot.sh
# Usage: ./analyze-screenshot.sh image.png "Creating a notebook"

IMAGE="$1"
CONTEXT="$2"
OUTPUT="${IMAGE%.png}_analysis.md"

# Comprehensive analysis prompt
cat << 'EOF' | ollama run llama3.2-vision:11b --image "$IMAGE" > "$OUTPUT"
Analyze this Fieldmark UI screenshot for documentation.
Context: $CONTEXT

Provide in this exact format:

## Description
[2-3 sentences describing what screen/interface is shown and its purpose]

## UI Elements
- Buttons: [list with positions like "top-right", "bottom center"]
- Input fields: [list with labels and states]
- Navigation: [menus, tabs, breadcrumbs with locations]
- Status indicators: [any badges, counts, states]

## Annotation Instructions
HIGHLIGHT: [elements needing red boxes]
CIRCLE: [buttons needing green circles]
ARROW: [elements needing arrows pointing to them]
CALLOUT: [text explanations needed]

## Success Indicators
- [What shows the task succeeded]
- [Visual confirmations visible]
- [State changes apparent]

## Platform Notes
- Screen type: [Desktop/Tablet/Mobile]
- Responsive elements: [what would change on mobile]

## Potential Confusion Points
- [Elements that might confuse users]
- [Missing or unclear labels]
EOF

echo "Analysis saved to $OUTPUT"
```

### Script 2: Batch Processor for Documentation
```bash
#!/bin/bash
# process-doc-screenshots.sh
# Usage: ./process-doc-screenshots.sh quickstart-notebook-creators.md

DOC_FILE="$1"
DOC_NAME="${DOC_FILE%.md}"
SCREENSHOT_DIR="screenshots/${DOC_NAME}/"

# Extract all placeholders from document
grep -o '\[SCREENSHOT[^]]*\]' "$DOC_FILE" | nl -nrz -w3 > placeholders.txt

# Process each placeholder
while IFS=$'\t' read -r NUM PLACEHOLDER; do
    echo "Processing placeholder $NUM: $PLACEHOLDER"
    
    # Extract context from placeholder
    CONTEXT=$(echo "$PLACEHOLDER" | sed 's/\[SCREENSHOT: \(.*\)\]/\1/')
    
    # Expected screenshot filename
    SCREENSHOT="${SCREENSHOT_DIR}screenshot-${NUM}.png"
    
    if [ -f "$SCREENSHOT" ]; then
        echo "  Analyzing $SCREENSHOT..."
        ./analyze-screenshot.sh "$SCREENSHOT" "$CONTEXT"
    else
        echo "  WARNING: Missing $SCREENSHOT"
        echo "  Expected for: $CONTEXT"
    fi
done < placeholders.txt
```

### Script 3: Placeholder Resolution
```python
#!/usr/bin/env python3
# resolve-placeholders.py
# Usage: python resolve-placeholders.py document.md

import re
import sys
import subprocess
import json
from pathlib import Path

class PlaceholderResolver:
    def __init__(self, doc_path):
        self.doc_path = Path(doc_path)
        self.doc_name = self.doc_path.stem
        self.screenshot_dir = Path(f"screenshots/{self.doc_name}")
        self.analysis_dir = Path(f"analysis/{self.doc_name}")
        
    def extract_placeholders(self):
        """Extract all placeholders from document"""
        with open(self.doc_path, 'r') as f:
            content = f.read()
            
        # Find all placeholder types
        patterns = {
            'screenshot': r'\[SCREENSHOT(?:-\w+)?: ([^\]]+)\]',
            'location': r'\[LOCATION: ([^\]]+)\]',
            'visual_check': r'\[VISUAL CHECK: ([^\]]+)\]',
            'navigate': r'\[NAVIGATE: ([^\]]+)\]',
        }
        
        placeholders = []
        for ptype, pattern in patterns.items():
            for match in re.finditer(pattern, content):
                placeholders.append({
                    'type': ptype,
                    'full_text': match.group(0),
                    'content': match.group(1),
                    'position': match.start()
                })
                
        return sorted(placeholders, key=lambda x: x['position'])
    
    def process_screenshot(self, placeholder, index):
        """Process screenshot through vision model"""
        screenshot_path = self.screenshot_dir / f"screenshot-{index:03d}.png"
        
        if not screenshot_path.exists():
            return {
                'status': 'missing',
                'expected_path': str(screenshot_path),
                'placeholder': placeholder['content']
            }
            
        # Parse annotation instructions if present
        lines = placeholder['content'].split('\n')
        context = lines[0]
        annotations = {}
        
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('HIGHLIGHT:'):
                annotations.setdefault('highlights', []).append(line[10:].strip())
            elif line.startswith('CIRCLE:'):
                annotations.setdefault('circles', []).append(line[7:].strip())
            elif line.startswith('ARROW:'):
                annotations.setdefault('arrows', []).append(line[6:].strip())
                
        # Run vision model analysis
        result = subprocess.run(
            ['./analyze-screenshot.sh', str(screenshot_path), context],
            capture_output=True,
            text=True
        )
        
        # Parse analysis results
        analysis_path = screenshot_path.with_suffix('.md')
        if analysis_path.exists():
            with open(analysis_path, 'r') as f:
                analysis = f.read()
        else:
            analysis = result.stdout
            
        return {
            'status': 'processed',
            'screenshot': str(screenshot_path),
            'context': context,
            'annotations': annotations,
            'analysis': analysis
        }
    
    def generate_report(self, results):
        """Generate implementation report"""
        report = [
            f"# Screenshot Integration Report",
            f"## Document: {self.doc_path.name}",
            f"",
            f"### Summary",
            f"- Total placeholders: {len(results)}",
            f"- Screenshots found: {sum(1 for r in results if r.get('status') == 'processed')}",
            f"- Missing screenshots: {sum(1 for r in results if r.get('status') == 'missing')}",
            f"",
            f"### Placeholder Details",
            f""
        ]
        
        for i, result in enumerate(results, 1):
            report.append(f"#### {i}. {result['type'].upper()}")
            report.append(f"**Original**: `{result['full_text']}`")
            
            if result['type'] == 'screenshot':
                if result.get('status') == 'missing':
                    report.append(f"⚠️ **Missing**: Expected at `{result['expected_path']}`")
                else:
                    report.append(f"✅ **Found**: `{result['screenshot']}`")
                    if result.get('annotations'):
                        report.append(f"**Annotations needed**:")
                        for atype, items in result['annotations'].items():
                            report.append(f"  - {atype}: {', '.join(items)}")
            else:
                report.append(f"**Action needed**: {result['content']}")
                
            report.append("")
            
        return '\n'.join(report)
    
    def process_document(self):
        """Main processing pipeline"""
        print(f"Processing {self.doc_path}...")
        
        # Extract placeholders
        placeholders = self.extract_placeholders()
        print(f"Found {len(placeholders)} placeholders")
        
        # Process each one
        results = []
        screenshot_index = 1
        
        for placeholder in placeholders:
            print(f"  Processing: {placeholder['type']} at position {placeholder['position']}")
            
            if placeholder['type'] == 'screenshot':
                result = self.process_screenshot(placeholder, screenshot_index)
                screenshot_index += 1
            else:
                result = {'status': 'manual_action_needed'}
                
            result.update(placeholder)
            results.append(result)
            
        # Generate report
        report = self.generate_report(results)
        report_path = Path(f"reports/{self.doc_name}_screenshot_report.md")
        report_path.parent.mkdir(exist_ok=True)
        
        with open(report_path, 'w') as f:
            f.write(report)
            
        print(f"Report saved to {report_path}")
        return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resolve-placeholders.py document.md")
        sys.exit(1)
        
    resolver = PlaceholderResolver(sys.argv[1])
    resolver.process_document()
```

---

## Part 4: Complete Workflow Process

### Step 1: Prepare Documentation
1. Write documentation with placeholders
2. Count placeholders: `grep -c '\[SCREENSHOT' document.md`
3. Create screenshot list

### Step 2: Capture Screenshots
1. Use consistent browser window size (1280x800 recommended)
2. Follow naming convention
3. Capture all states (empty, filled, success, error)
4. Save to organized folders

### Step 3: Run Vision Model Analysis
```bash
# Single document
python resolve-placeholders.py quickstart-notebook-creators.md

# Batch processing
for doc in production/human-facing/*.md; do
    python resolve-placeholders.py "$doc"
done
```

### Step 4: Review Analysis Reports
Check `reports/` folder for:
- Missing screenshots list
- Annotation requirements
- Platform-specific notes
- Confusion points identified

### Step 5: Create Annotated Versions
Using the annotation instructions from analysis:
```bash
# Example using ImageMagick
convert screenshot.png \
  -stroke red -strokewidth 3 -fill none \
  -draw "rectangle 100,50 300,100" \
  -stroke green -strokewidth 3 \
  -draw "circle 400,200 430,200" \
  screenshot-annotated.png
```

### Step 6: Update Documentation
Replace placeholders with:
```markdown
<!-- Was: [SCREENSHOT: Login page] -->
![Login page](screenshots/quickstart/login-page-01.png)
*Enter your email and password, then click Sign In*
```

---

## Part 5: Quality Checklist

### Before Processing
- [ ] All placeholders follow standard format
- [ ] Screenshots captured at consistent resolution
- [ ] File naming convention followed
- [ ] Folder structure organized

### During Processing
- [ ] Vision model installed and working
- [ ] Scripts have execute permissions
- [ ] Output directories exist
- [ ] Error handling in place

### After Processing
- [ ] All placeholders resolved
- [ ] Annotations match requirements
- [ ] Alt text added for accessibility
- [ ] Mobile/desktop variations noted
- [ ] Documentation builds correctly

---

## Part 6: Maintenance Workflow

### When UI Changes
1. Identify affected screenshots: `grep -l "affected-component" *.md`
2. Recapture screenshots
3. Re-run vision analysis
4. Compare with previous analysis
5. Update documentation if needed

### Regular Audits
```bash
#!/bin/bash
# audit-screenshots.sh
# Monthly screenshot audit

echo "Screenshot Audit Report"
echo "======================"
echo ""
echo "Missing screenshots:"
find production -name "*.md" -exec grep -l '\[SCREENSHOT' {} \; | while read doc; do
    echo "Checking $doc..."
    grep '\[SCREENSHOT' "$doc" | nl
done

echo ""
echo "Orphaned screenshots:"
find screenshots -name "*.png" | while read img; do
    name=$(basename "$img")
    if ! grep -r "$name" production/; then
        echo "  Orphaned: $img"
    fi
done
```

---

## Part 7: Advanced Integration

### Automated Pipeline with GitHub Actions
```yaml
name: Screenshot Documentation
on:
  pull_request:
    paths:
      - 'production/**/*.md'
      - 'screenshots/**/*.png'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Check placeholders
        run: |
          ./scripts/validate-placeholders.sh
          
      - name: Verify screenshots exist
        run: |
          python scripts/resolve-placeholders.py --check-only
          
      - name: Generate report
        run: |
          python scripts/generate-screenshot-report.py > screenshot-status.md
          
      - name: Comment on PR
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('screenshot-status.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });
```

### Integration with Documentation Build
```python
# build-with-screenshots.py
# Integrate into docs build process

def process_markdown_with_screenshots(content):
    """Replace placeholders with actual screenshots during build"""
    
    def replace_screenshot(match):
        placeholder = match.group(1)
        # Look up corresponding screenshot
        screenshot = find_screenshot_for_placeholder(placeholder)
        if screenshot:
            return f"![{placeholder}]({screenshot})"
        else:
            return f"<!-- MISSING: {placeholder} -->"
    
    return re.sub(r'\[SCREENSHOT: ([^\]]+)\]', replace_screenshot, content)
```

---

## Appendix: ROI Tracking

### Time Metrics to Track
```python
# track-metrics.py
metrics = {
    'manual_description_time': 2,  # minutes per screenshot
    'manual_annotation_time': 3,   # minutes per screenshot
    'vision_processing_time': 0.5, # minutes per screenshot
    'review_time': 0.5,            # minutes per screenshot
    
    'total_screenshots': 200,
    'manual_total': 200 * 5,        # 1000 minutes
    'automated_total': 200 * 1,     # 200 minutes
    'time_saved': 800,              # minutes
    'percentage_saved': 80          # percent
}
```

---

## Ready-to-Use Commands

```bash
# Setup
mkdir -p screenshots scripts reports analysis
chmod +x scripts/*.sh

# Process single document
./scripts/analyze-screenshot.sh dashboard-home.png "Dashboard home page"

# Batch process folder
for img in screenshots/quickstart/*.png; do
    ./scripts/analyze-screenshot.sh "$img" "Quickstart guide"
done

# Generate full report
python scripts/resolve-placeholders.py production/human-facing/quickstart-notebook-creators.md

# Audit all documentation
find production -name "*.md" | while read doc; do
    echo "Checking $doc..."
    python scripts/resolve-placeholders.py "$doc" --report-only
done
```

---

*This workflow document contains everything needed to implement the screenshot pipeline. Save scripts to `/scripts/` folder and begin with small test before full implementation.*