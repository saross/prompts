# Your First Notebook in 15 Minutes 🚀

*Welcome to Fieldmark! In the next 15 minutes, you'll create your first data collection notebook and enter your first record. No experience needed - just follow along!*

## What You'll Achieve

By the end of this guide, you'll have:
- ✅ Created a working notebook from scratch
- ✅ Added fields for data collection
- ✅ Entered and saved your first record
- ✅ Learned how to invite team members
- ✅ Gained confidence to explore further

## Before You Start

**You'll need**: A Fieldmark account with at least Standard User permissions. If you don't have an account yet, ask your project administrator or team admin to invite you.

**Browser**: Works best with Chrome, Firefox, or Safari. Make sure you're using a recent version.

### 📖 Quick Terms to Know

Before we dive in, here are five terms you'll see:

- **Dashboard**: Your home screen after logging in - think of it as mission control
- **Notebook**: A data collection form you create and customise
- **Notebook Editor**: The visual tool where you build and modify notebooks and templates (sometimes just called "Editor")
- **Records**: The actual data entries people create using your notebook
- **Fields**: Individual input elements (like text boxes or photo buttons) in your form

---

## Step 1: Access Your Dashboard (2 minutes)

Let's begin by logging into Fieldmark and finding our way around.

### Login to Fieldmark

1. Open your browser and go to your Fieldmark URL (usually something like `https://api.fieldmark.app`)
2. Enter your email and password (or select the appropriate SSO provider, e.g., Google)
3. Click **Sign In**

[SCREENSHOT: Login page with email and password fields]

### Welcome to Your Dashboard!

After logging in, you'll see the Dashboard Overview. This is your command centre where you can:
- Create new notebooks (from scratch or from templates)
- Access and edit existing notebooks
- Create and edit templates
- Manage teams and users

[SCREENSHOT: Dashboard Overview showing the main navigation and Create buttons]

> ✨ **Pro Tip**: Bookmark this page! You'll be coming back here often. In most browsers, press `Ctrl+D` (Windows/Linux) or `Cmd+D` (Mac) to bookmark.

### ✓ You'll Know It Worked When...
- You see your name or email in the bottom-left user menu
- The dashboard (right pane) shows navigation options like Notebooks, Templates, Users, Teams
- You see a list of notebooks in the main window
- No error messages or login prompts appear

Great! You're in. Now let's create something amazing.

---

## Step 2: Create Your First Notebook (3 minutes)

Creating a notebook is easy. Let's do it!

### Create a New Notebook

From the Dashboard:

1. Click **Notebooks** in the left navigation
2. Click **+ Create Notebook**

[SCREENSHOT: Templates interface showing Create Template button]

### Name Your Creation

In the creation dialog:
1. **Template/Notebook Name**: Type "My First Survey" (or any name you like!)
2. **Select team**: Use the dropdown to select the team the notebook belongs to (usually there will only be one option) 
3. Ignore the 'optional' fields
4. Click **Create Notebook**

### Navigating to your new, blank notebook

After you click 'Create Notebook', you will return to the list of notebooks, where you should:
1. Go to the end of the list, clicking through to later pages if needed
3. Click on the name of the notebook you just created (last in the list)
4. Click on the **Actions** tab
5. Click **Open in Editor**

### Hello, Notebook Editor!

Fantastic! You're now in the Notebook Editor. This is where the magic happens.

[SCREENSHOT: Notebook Editor interface showing the form builder layout]

You'll see the main areas:
- Top navigation: DESIGN and INFO tabs, with CANCEL and SAVE buttons
- Main canvas: Your form building area with a "+" button to add sections
- Form controls: "ADD NEW FORM" button to create new forms
- Top right: UNDO and REDO buttons for quick correction

> ⚠️ **Common Mistake**: Don't worry if it looks empty - that's normal! We're about to fill it with useful fields. The Notebook Editor saves automatically as you work.

### ✓ You'll Know It Worked When...
- The Notebook Editor opens with "Form 1" ready for editing
- You see the helpful instruction text about adding forms and sections
- The "+" button is visible for adding new elements
- The DESIGN tab is selected and active
- No error messages appear

> 📱 **Mobile Users**: The Notebook Editor works best on tablets or computers. If you're on a phone, you might want to switch devices for this setup phase. Once created, your notebook will work perfectly on mobile for data collection!

---

## Step 3: Add Your Fields (5-7 minutes)

Now for the fun part - let's add fields to collect data! We'll add five essential fields, taking our time with each one.

### Part A: Your First Two Fields (2 minutes)

Let's start with the basics - a text field and a dropdown. These are the bread and butter of data collection.

#### Field 1: Site Name (Text Field)

1. **Find the field**: In the left panel, look for **FAIMSTextField** (or just **TextField**)
2. **Add it**: Drag it onto the centre canvas
3. **Configure it** by clicking on the field:
   - **Field Label**: Type "Site Name"
   - **Field Name**: Auto-generates as "site_name" (perfect!)
   - **Required**: Toggle this on ✓
   - **Helper Text**: Add "Enter the official site designation"

[SCREENSHOT: Adding a TextField with configuration panel open]

> ✓ **Check Your Progress**: You should see "Site Name" appear in the centre panel with a red asterisk (*) indicating it's required.

#### Field 2: Site Type (Dropdown)

Now let's add a dropdown for selecting options.

1. **Find it**: Look for **Select** in the left panel
2. **Drag it** below your Site Name field
3. **Configure it**:
   - **Field Label**: Type "Site Type"
   - **Options**: Click "Add Option" and add these one by one:
     - Archaeological
     - Geological  
     - Ecological
     - Other
   - **Required**: Toggle on ✓

> 💡 **Platform Note**: On mobile devices, Select fields automatically adapt to native pickers for better usability.

**Quick Save**: The Notebook Editor auto-saves, but you can manually save by clicking **Save** in the top toolbar.

### Part B: Date and Long Text (2 minutes)

Now let's add fields for capturing when and what happened.

#### Field 3: Visit Date (Date Picker)

Every record needs a date!

1. **Find it**: Look for **DateTime with Now button** (captures current date/time automatically)
2. **Drag it** below Site Type
3. **Configure it**:
   - **Field Label**: Type "Visit Date"
   - **Required**: Toggle on ✓
   - **Hide Time**: Toggle on if you only need the date

> ✓ **Check Your Progress**: You now have three fields in your form. The date field shows it will auto-populate with "now".

#### Field 4: Observations (Text Area)

For longer descriptions, we need a multiline text field.

1. **Find it**: Use **MultipleTextField** (designed for longer text)
2. **Drag it** below Visit Date
3. **Configure it**:
   - **Field Label**: Type "Observations"
   - **Number of Rows**: Set to 4
   - **Helper Text**: "Describe site conditions and notable features"

> 📱 **Mobile Tip**: MultipleTextField automatically expands on mobile devices as users type more content.

### Part C: Adding Photo Capability (1 minute)

Let's add the ability to capture photos - essential for field documentation!

#### Field 5: Site Photo (Camera)

1. **Find it**: Look for **TakePhoto** in the palette
2. **Drag it** to the bottom of your form
3. **Configure it**:
   - **Field Label**: Type "Site Photo"
   - **Required**: Leave off (photos optional)
   - **Multiple Photos**: Leave off for now

[SCREENSHOT: Completed form showing all five fields in the Notebook Editor]

### Adding Form Completion Settings

One crucial step - let's ensure records can be properly saved:

1. Click on **Form Settings** (gear icon or settings button)
2. Find **Form Completion**:
   - **Submit Button Label**: Set to "Save Record"
   - **Show Summary**: Toggle on
3. Find **Record Identification**:
   - Enable **Auto-generate HRID** (Human Readable ID)
   - Pattern: Leave as default or set to "SITE-{{YYYY}}-{{autoincrement}}"

### ✓ Final Check: You'll Know It Worked When...

Before moving on, verify:
- You can see 5 fields in the centre panel
- They appear in order: Site Name, Site Type, Visit Date, Observations, Site Photo
- Required fields show red asterisks (*)
- Form settings show "Save Record" button configured

> ✨ **Pro Tip**: Start simple like we just did. You can always come back to add more fields, validation rules, or conditional logic. Most successful notebooks begin with 5-10 fields and evolve based on actual use.

---

## Step 4: Deploy and Test Your Notebook (3 minutes)

Time to see your creation in action! Let's deploy your template as a notebook and enter test data.

### Deploy Your Template

1. **Save the Template**: Click **Save** one more time to ensure everything is saved
2. **Create Notebook from Template**:
   - Look for **Deploy** or **Create Notebook** button
   - Or go to the **Actions** menu and select "Create Notebook"
3. **Name Your Notebook**: 
   - Keep "My First Survey" or rename it
   - Click **Create**

### Access Your Notebook

After deployment, you'll either:
- Be redirected to the notebook automatically, OR
- Need to navigate to **Notebooks** and find "My First Survey"

Click on your notebook to open it.

[SCREENSHOT: Notebook interface showing the data entry form]

### ✓ You'll Know You're Ready When...
- You see your form without the Notebook Editor interface
- The fields are ready for data entry
- There's a "New Record" or "+" button visible

### Create Your First Record

Let's fill in some test data:

1. Click **New Record** or the **+** button
2. Fill in your fields:
   - **Site Name**: Enter "Test Location Alpha"
   - **Site Type**: Select "Archaeological" from the dropdown
   - **Visit Date**: Will auto-fill with today's date/time
   - **Observations**: Type "This is my first Fieldmark record! The site shows interesting features worth documenting."
   - **Site Photo**: 
     - Click the camera/photo button
     - Allow camera permissions if asked
     - Take any photo (even of your desk - this is just practice!)

[SCREENSHOT: Filled form with sample data]

### Save Your Record

Look for the **Save Record** button (as we configured):
- It should be at the bottom of the form
- Click it!

Congratulations! 🎉 You've just created your first record!

### ✓ You'll Know It Saved When...
- You see a success message
- The form shows your record summary
- You're given options to create another record or view all records

### View Your Success

1. Navigate to the **Records** section (might be a tab or menu option)
2. You should see your record listed:
   - Shows "Test Location Alpha"
   - Shows today's date
   - Has a unique ID like "SITE-2025-0001"
3. Click on the record to view full details

[SCREENSHOT: Records list showing the saved record]

> ⚠️ **Can't See Records?** Make sure you're in the notebook view, not the template. Templates are for design; notebooks are for data collection.

---

## Step 5: Collaborate and Refine (2 minutes)

Your notebook works! Now let's share it with others and learn about permissions.

### Understanding Permissions

Fieldmark uses a role-based permission system. As the notebook creator, you're automatically the **Notebook Administrator**. Here's what each role can do:

| Role | Can Do |
|------|--------|
| **Data Collector** | Add and edit their own records |
| **Data Reviewer** | Review and approve records |
| **Data Viewer** | View records only (read-only) |
| **Notebook Admin** | Everything, including inviting users |

### Invite a Team Member

1. In your notebook, find the **Users** or **Invites** tab
2. Click **Invite User**
3. Enter their details:
   - **Email**: Their email address
   - **Role**: Choose "Data Collector" to start
   - **Message**: Optional welcome message
4. Click **Send Invitation**

[SCREENSHOT: Invite users dialog]

They'll receive an email invitation to join your notebook!

> 💡 **Team Tip**: If you're part of a team, team members automatically get access through virtual roles - no individual invitations needed!

### Make an Improvement

Let's add one enhancement based on what we learned:

1. Return to **Templates** section
2. Find your "My First Survey" template
3. Click **Edit** to reopen the Notebook Editor
4. Select the "Observations" field
5. Add **Validation**:
   - Minimum length: 10 characters
   - Validation message: "Please provide at least 10 characters"
6. **Save** the template

> ✨ **Pro Tip**: Changes to templates don't affect existing notebooks. You'll need to create a new notebook from the updated template or manually update the existing one.

---

## 🎯 Success Checklist

Let's confirm you've accomplished everything:

- ✅ Logged into Fieldmark successfully
- ✅ Created a template with 5 fields
- ✅ Configured form completion settings
- ✅ Deployed template as a notebook
- ✅ Entered and saved a test record
- ✅ Viewed your record with its HRID
- ✅ Understood permission roles
- ✅ Invited a user (optional)

**If you checked all these boxes - you did it!** 🎉

---

## Quick Troubleshooting

Running into issues? Here are solutions to common problems:

### "I can't find the Notebook Editor"
**Solution**: Check that you're a member of a team with appropriate permissions. Team members can access the Notebook Editor based on their team role.

### "My Save button isn't appearing"
**Solution**: Check Form Settings → Form Completion → Publish Button Behaviour. Make sure it's configured properly.

### "The person I invited hasn't received an email"
**Solution**: 
1. Check their spam/junk folder
2. Verify the email address is correct
3. Check the Invites tab for status
4. Resend if needed

### "I can't take a photo"
**Solution**: 
- **Mobile**: Check app permissions in device settings
- **Desktop**: Ensure browser has camera access
- **All platforms**: HTTPS connection required for camera access

### "My record ID looks weird (like rec_xxxxx)"
**Solution**: You need to configure an HRID field. Go to Form Settings and set up the human-readable ID pattern.

### "Changes to my template aren't showing in the notebook"
**Solution**: Templates and notebooks are separate. Create a new notebook from the updated template, or manually update the existing notebook's configuration.

---

## 🚀 Power User Tips

Now that you've mastered the basics, here are some advanced features to explore:

### Virtual Roles Through Teams
If your organisation uses teams:
- Team members automatically get notebook access
- No need for individual invitations
- Permissions cascade from team roles

### API Automation
Once comfortable with the interface:
- Generate API tokens from your User Profile
- Automate data exports
- Integrate with Excel or Google Sheets
- See the automation guide for examples

### Conditional Logic
Make smart forms that adapt:
- Show/hide fields based on answers
- Skip irrelevant sections
- Validate related fields together

### Template Library
Build once, deploy many:
- Save successful notebooks as templates
- Share templates with your team
- Create template variants for different scenarios

---

## What's Next?

You've completed your first notebook - fantastic work! Here are your next adventures:

### Immediate Next Steps
- **Experiment**: Try different field types (RadioGroup, AdvancedSelect, MapField)
- **Explore**: Check out existing templates in your system
- **Practice**: Create a notebook for a real use case

### Recommended Learning Path
1. 📱 **Mobile Data Collection** - Test your notebook on a phone/tablet
2. 🔄 **Data Export** - Learn to export records as CSV/JSON
3. ⚙️ **Advanced Fields** - Explore RelatedRecordSelector, BasicAutoIncrementer
4. 📊 **Automation Basics** - Simple scripts for daily exports

### Get Help
- **In-app**: Look for the help icon (?)
- **Documentation**: Check the comprehensive reference guide
- **Team Support**: Ask your team administrator
- **Virtual Roles**: If in a team, you already have access to team resources!

---

## You Did It! 🎊

In just 15 minutes, you've mastered the fundamental Fieldmark workflow:

1. **Design** in the Notebook Editor
2. **Deploy** as a notebook
3. **Collect** data with proper structure
4. **Collaborate** with role-based permissions
5. **Iterate** based on real needs

This template-first approach means you can start simple and grow as you learn. Your notebooks will evolve with your project needs.

**Welcome to the Fieldmark community!** We can't wait to see what you'll create.

---

*Remember: Every expert was once a beginner. You've taken your first steps, and that's the hardest part. Keep experimenting, keep learning, and most importantly - keep collecting great data!*

*P.S. - Did you know? Fieldmark was formerly known as FAIMS3. If you see old documentation mentioning FAIMS, that's us!*