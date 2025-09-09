# Basic Automation with API Tokens {comprehensive}

**Purpose**: Enable power users to automate common Fieldmark tasks without programming knowledge  
**Audience**: Research support staff, data managers, IT support  
**Prerequisites**: API token created via User Profile

## Overview {comprehensive}

Fieldmark's API tokens enable automated data operations without manual dashboard interaction. This guide covers practical automation scenarios using simple tools.

## Creating Your API Token {comprehensive}

Before automation, create a long-lived token:

1. Navigate to User Profile (click username, lower-left)
2. Click "Manage Long-Lived Tokens"
3. Click "Create Long Lived Token"
4. Set duration (max 90 days)
5. **Copy token immediately** (shown only once)
6. Store securely (password manager recommended)

## Common Automation Scenarios {comprehensive}

### 1. Daily Data Export to CSV

Export all notebook records automatically:

```bash
# Using curl (Linux/Mac)
TOKEN="your-token-here"
NOTEBOOK_ID="notebook-id-here"
SERVER="https://your-fieldmark-server.edu.au"

# Exchange token for access token
ACCESS_TOKEN=$(curl -s -X POST "$SERVER/api/auth/exchange-long-lived-token" \
  -H "Content-Type: application/json" \
  -d "{\"token\": \"$TOKEN\"}" | jq -r '.access_token')

# Export data
curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  "$SERVER/api/notebooks/$NOTEBOOK_ID/records.csv" \
  -o "export-$(date +%Y%m%d).csv"
```

### 2. Excel Power Query Integration

Connect Excel directly to Fieldmark data:

1. Open Excel → Data → Get Data → From Web
2. Enter API URL: `https://your-server/api/notebooks/NOTEBOOK_ID/records.csv`
3. Choose "Advanced" and add header:
   - Key: `Authorization`
   - Value: `Bearer YOUR_ACCESS_TOKEN`
4. Data refreshes automatically when opened

### 3. Scheduled Backup Script

Windows batch file for weekly backups:

```batch
@echo off
set TOKEN=your-token-here
set SERVER=https://your-fieldmark-server.edu.au
set NOTEBOOK=notebook-id-here

REM Get current date
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "date=%dt:~0,8%"

REM Download backup
curl -H "Authorization: Bearer %TOKEN%" ^
  "%SERVER%/api/notebooks/%NOTEBOOK%/export" ^
  -o "backup-%date%.json"
```

### 4. Google Sheets Integration

Import Fieldmark data into Google Sheets:

```javascript
function importFieldmarkData() {
  var token = 'your-token-here';
  var notebookId = 'notebook-id-here';
  var server = 'https://your-fieldmark-server.edu.au';
  
  var response = UrlFetchApp.fetch(
    server + '/api/notebooks/' + notebookId + '/records.csv',
    {
      headers: {
        'Authorization': 'Bearer ' + token
      }
    }
  );
  
  var csvData = Utilities.parseCsv(response.getContentText());
  var sheet = SpreadsheetApp.getActiveSheet();
  sheet.getRange(1, 1, csvData.length, csvData[0].length).setValues(csvData);
}
```

### 5. Photo Archive Download

Download all photos from a notebook:

```bash
# Linux/Mac script
TOKEN="your-token-here"
NOTEBOOK_ID="notebook-id-here"
SERVER="https://your-fieldmark-server.edu.au"

# Download photo archive
curl -H "Authorization: Bearer $TOKEN" \
  "$SERVER/api/notebooks/$NOTEBOOK_ID/photos.zip" \
  -o "photos-$(date +%Y%m%d).zip"

# Extract to dated folder
unzip -d "photos-$(date +%Y%m%d)" "photos-$(date +%Y%m%d).zip"
```

## Security Best Practices {comprehensive}

### Token Storage
- **Never** commit tokens to version control
- **Never** share tokens via email or chat
- Use environment variables or secure vaults
- Rotate tokens monthly

### Access Control
- Create separate tokens for different tasks
- Use descriptive names (e.g., "Daily Export Script")
- Delete unused tokens immediately
- Monitor "Last Used" timestamps

### Error Handling
- Check for HTTP 401 (unauthorised) - token may be expired
- HTTP 429 (rate limited) - add delays between requests
- Log errors for troubleshooting

## Troubleshooting {comprehensive}

| Issue | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorised | Token expired or disabled | Create new token |
| 403 Forbidden | Insufficient permissions | Check notebook access rights |
| 404 Not Found | Wrong notebook ID | Verify ID in dashboard URL |
| 500 Server Error | Server issue | Contact administrator |
| Empty response | No data in notebook | Verify records exist |

## Limitations {comprehensive}

- Tokens expire after maximum 90 days
- Rate limits apply (100 requests/minute)
- Large exports may timeout (>1000 records)
- Binary attachments require separate download

## Next Steps

For more complex integrations:
- Contact IT support for assistance
- Consider dedicated integration development
- See future developer documentation (planned)

---

**Note**: This guide covers basic automation only. Complex integrations requiring data modification or real-time sync should be developed with IT support.