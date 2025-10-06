# Your First Notebook in 15 Minutes 🚀

*Welcome to Fieldmark! In the next 15 minutes, you'll create your first data collection notebook and enter your first record. No experience needed - just follow along!*

## What You'll Achieve

By the end of this guide, you'll have:

- ✅ Created a working notebook from scratch
- ✅ Added five different field types for data collection
- ✅ Configured your notebook so records display properly
- ✅ Entered and saved your first record
- ✅ Gained confidence to explore further

## Before You Start

### What You Need

- A Fieldmark account (if you don't have one, ask your project administrator)
- A desktop or laptop computer (the Notebook Editor doesn't work well on mobile)
- Chrome, Firefox, Safari, or Edge browser

### Quick Terms to Know

- **Dashboard**: Your central hub where you manage notebooks and view records
- **Notebook**: A template that defines what data you'll collect (like a customisable form)
- **Notebook Editor**: The design tool where you build and modify notebooks
- **Records**: The actual data entries people create using your notebook
- **Fields**: Individual questions or data points in your notebook (like "Site Name" or "Date")

> 💡 **Pro tip**: Think of it like this - a notebook is like a blank form template, and records are the filled-in copies of that form.

---

## Step 1: Access Your Dashboard (2 minutes)

First, let's get you logged in and oriented.

### Log In to Fieldmark

1. Go to your Fieldmark instance URL (your administrator will have provided this)
2. Enter your email address and password
3. Click "Sign in"

[SCREENSHOT: Login page showing email and password fields with green Sign in button]

> If you're using Google authentication, click "Continue with Google" instead.

### Explore Your Dashboard

Once logged in, you'll see your Dashboard. This is your home base in Fieldmark. Take a moment to notice:

- The **Fieldmark logo** in the top-left corner
- Your **user menu** in the bottom-left (shows your initials)
- The main area where notebooks will appear

[SCREENSHOT: Dashboard overview showing empty notebook list with navigation elements]

> 💡 **Bookmark this page!** You'll come back here often, so save it to your browser's bookmarks bar.

### ✓ You'll Know It Worked When...

- [ ] You see your Dashboard with "Notebooks" or similar navigation
- [ ] Your user icon appears (usually in the bottom-left corner)
- [ ] The page title says "Fieldmark" or shows your instance name

#### Common Issue: Can't Find the User Menu?

**Look in the bottom-left corner** of the screen. It's a circular icon with your initials. If you still can't find it, try refreshing the page or logging out and back in.

---

## Step 2: Create Your First Notebook (3 minutes)

Now let's create a simple notebook for recording site visits.

### Start a New Notebook

You can create notebooks in two ways, but we'll use the direct approach:

1. From your Dashboard, click **"Templates"** in the navigation
2. Click the **"Create Template"** button (usually green or prominent)
3. You'll see the **Notebook Editor** open - this is where the magic happens!

[SCREENSHOT: Notebook Editor interface showing the Design tab with Form Settings panel]

### Understanding the Notebook Editor

The Notebook Editor has three key areas:

1. **Top tabs**: Switch between "Design" (where you build) and "Info" (metadata)
2. **Left panel**: Shows your forms and sections
3. **Main area**: Where you add and configure fields

You'll see a default form already created (often called "Form 1" or similar). Let's rename it:

4. Click **"Edit Form Name"** next to the form name
5. Type **"Site Details"** and press Enter
6. You'll see a section called "Basic Information" - that's perfect, leave it as is

> ⚠️ **Mobile Warning**: The Notebook Editor requires a desktop computer. Don't try this on your phone or tablet - it won't work properly!

### ✓ You'll Know It Worked When...

- [ ] You see "Notebook Editor" at the top of the page
- [ ] The "Design" tab is active (underlined or highlighted)
- [ ] You see "Form Settings" and "Add a Field" buttons
- [ ] Your form is named "Site Details"

#### Common Issue: Buttons Not Responding?

If the interface seems frozen, try these steps:
1. Click "Save" in the top-right corner first
2. Refresh the page
3. If problems persist, try a different browser (Chrome or Firefox work best)

---

## Step 3: Add Your Fields (5-7 minutes)

Now for the fun part - adding fields to collect data! We'll add five fields to create a practical site survey form.

### Part A: First Two Fields (2 minutes)

#### Add a Text Field for Site Name

1. Click the green **"Add a Field"** button
2. You'll see field categories at the top - make sure **"TEXT"** is selected
3. In the field name box, type **"Site Name"**
4. Click the **"FAIMS Text Field"** card (single-line text input)
5. Click **"Add Field"** at the bottom

[SCREENSHOT: Add field dialogue showing TEXT category with FAIMS Text Field selected]

Great! Your first field is added. Now let's add a dropdown.

#### Add a Select Field for Site Type

1. Click **"Add a Field"** again
2. Click the **"CHOICE"** category at the top
3. In the field name box, type **"Site Type"**
4. Click **"Select Field"** (the dropdown option)
5. Click **"Add Field"**
6. Now you'll see the field appear - click the **arrow** next to "Site Type" to expand it
7. Under "Options", you'll see "Option 1" - click it and change it to **"Habitation"**
8. Click **"Add Option"** and add these choices:
   - Mortuary
   - Ceremonial
   - Workshop/Industrial
   - Agricultural

[SCREENSHOT: Select Field configuration showing multiple options like Habitation, Mortuary, Ceremonial]

> ✓ **Progress check**: You should now see two fields - "Site Name" and "Site Type" - in your visible fields list.

### Part B: Date and Long Text (2 minutes)

#### Add a Date Field with Now Button

1. Click **"Add a Field"**
2. Click **"DATE & TIME"** category
3. Type **"Survey Date"** for the field name
4. Click **"Date and Time with Now button"** (this lets users quickly set current date/time)
5. Click **"Add Field"**

[SCREENSHOT: DATE & TIME category showing Date and Time with Now button option selected]

Perfect! Now let's add a field for longer notes.

#### Add a Multiline Text Field

1. Click **"Add a Field"**
2. Click **"TEXT"** category
3. Type **"Observations"** for the field name
4. Click **"Text Field"** (the multi-line option - despite the confusing name!)
5. Click **"Add Field"**

[SCREENSHOT: TEXT category showing Text Field option for multiline text]

> The naming is confusing - "FAIMS Text Field" is for single lines, "Text Field" is for multiple lines!

> ✓ **Progress check**: You should now have four fields total. Take a breath - you're doing great!

### Part C: Photo Capability (1 minute)

Let's add the ability to capture photos.

#### Add a Photo Field

1. Click **"Add a Field"**
2. Click **"MEDIA"** category
3. Type **"Site Photo"** for the field name
4. Click **"Take Photo"** (this enables camera capture)
5. Click **"Add Field"**

[SCREENSHOT: MEDIA category showing Take Photo option selected]

Excellent! You've now got five fields. But there's one crucial step remaining...

### Configure Form Completion Settings

This is **critical** - without this configuration, your records will display as confusing codes like "rec_a7f3b2c1" instead of readable names.

1. Scroll up and click **"Form Settings"** (the gear icon near the top)
2. The panel will expand - scroll down to find **"Human-Readable ID Field"**
3. Click the dropdown and select **"Site Name"**

[SCREENSHOT: Form Settings panel showing Human-Readable ID Field dropdown with Site Name selected]

> This tells Fieldmark to display your site name in the records list instead of cryptic IDs. It's essential!

4. While you're here, find **"Summary Fields"** and select **"Site Type"**
   - This shows the site type in your records list for quick reference

### ✓ You'll Know It Worked When...

- [ ] You see five fields listed under "Visible Fields"
- [ ] Each field shows its type badge (FAIMSTextField, Select Field, DateTimeNow, MultipleTextField, TakePhoto)
- [ ] Form Settings shows "Site Name" as the Human-Readable ID Field
- [ ] The form looks complete and organised

[SCREENSHOT: Completed form showing all five fields visible in the editor]

#### Troubleshooting: Field Not Appearing?

- **Check you clicked "Add Field"** at the bottom of the dialogue
- **Scroll down** - new fields appear at the bottom of the visible fields list
- **Look for the arrow** - you might need to expand collapsed fields
- **Save your work** - click the green "Save" button in the top-right

#### Troubleshooting: Can't Find Form Settings?

- **Look for the gear icon** near your form name
- **It might be collapsed** - click it to expand the panel
- **Scroll down within the panel** to find Human-Readable ID Field

---

## Step 4: Deploy and Test Your Notebook (3 minutes)

Your notebook is designed - now let's make it active and test it!

### Save and Activate Your Notebook

1. Click the green **"Save"** button in the top-right corner
2. Switch to the **"Info"** tab (next to Design)
3. Give your notebook a name: **"My First Site Survey"**
4. Scroll down to the **"Active"** section
5. You'll see "Not Active (0)" - click **"Activate"**
6. A confirmation dialogue appears - click **"Activate"** again

[SCREENSHOT: Activation modal showing confirmation dialogue]

7. Wait a moment - the status will change to **"Active (1)"**

[SCREENSHOT: Active status showing "Active (1)"]

> The number shows how many active versions of this notebook exist. Don't worry about versions for now!

### Navigate to Your Notebook

1. Click the **"Back"** button or arrow to return to your Dashboard
2. Find your notebook **"My First Site Survey"** in the list
3. Click on it to open it
4. You'll see an empty records list with the button **"Add New Site Details"**

[SCREENSHOT: Empty notebook showing "No rows" with Add New Site Details button]

### Enter Your First Record

Time to test your creation!

1. Click **"Add New Site Details"** (the orange button)
2. You'll see your form with all five fields - let's fill it in:
   - **Site Name**: Type "Test Location Alpha"
   - **Site Type**: Select "Habitation" from the dropdown
   - **Survey Date**: Click the **"Now"** button (it fills in current date/time automatically)
   - **Observations**: Type something like "I looked at the site and it's a dwelling"
   - **Site Photo**: Click "Take First Photo" if you want (or skip it for now)

[SCREENSHOT: Form filled to 100% showing all fields completed]

3. Notice the **green progress bar** at the top showing "100% Completed"
4. Click the **"Submit"** or **"Finish"** button (you'll find it at the bottom or in a "three dots" menu)

### View Your Record

After submitting, you'll return to the records list. Now you should see:

- Your record showing **"Test Location Alpha"** (not "rec_something"!)
- The site type "Habitation" displayed
- A green sync indicator showing it's saved

[SCREENSHOT: Records list showing one synced record with Site Name and Site Type visible]

### ✓ You'll Know It Worked When...

- [ ] Your notebook shows "Active (1)" status
- [ ] You can click "Add New Site Details" to create records
- [ ] Your form displays all five fields correctly
- [ ] After submitting, your record appears in the list
- [ ] The record shows "Test Location Alpha" (not a cryptic code)
- [ ] The sync indicator shows green (synced to server)

#### Troubleshooting: Form Shows "rec_xxxxx" Instead of Site Name?

**This means the Human-Readable ID Field wasn't configured.** Here's how to fix it:

1. Go back to Templates
2. Edit your notebook
3. Open Form Settings
4. Set "Human-Readable ID Field" to "Site Name"
5. Save
6. Create a new version (you may need to deactivate the old one first)

#### Troubleshooting: Can't Find the Finish Button?

- **Look for three dots** (⋮) in the top-right corner - the menu might be there
- **Check the bottom of the form** after scrolling all the way down
- **Make sure all required fields are filled** - the button stays hidden until the form is valid

---

## Step 5: Collaborate and Refine (2 minutes)

You've created a working notebook! Now let's talk about sharing it with your team.

### Understanding Permissions

Fieldmark uses a role-based system for collaboration:

| Role | What They Can Do |
|------|------------------|
| **Team Member** | View and use notebooks shared with their team |
| **Template Creator** | Create and edit notebooks for their team |
| **Project Manager** | Manage teams, users, and all notebooks |
| **System Administrator** | Full system access and configuration |

### Sharing Your Notebook

To share your notebook with colleagues:

1. Your notebook is automatically available to your team members
2. If you need to invite someone to your team, ask your Project Manager or System Administrator
3. Team members will see the notebook in their Dashboard once they log in

> **Note**: Individual notebook permissions don't exist - access is managed through team membership. This keeps things simple!

[SCREENSHOT: Settings tab showing team and permission controls]

### Virtual Roles for Advanced Setups

For larger teams, Fieldmark supports "virtual roles" that let you:

- Give different people different access to notebooks
- Create specialist roles (like "Data Validator" or "Field Supervisor")
- Manage complex permission schemes

Ask your administrator about virtual roles if your project needs this level of control.

### Making Improvements

Want to change your notebook? Here's how:

1. Go back to **Templates**
2. Click on **"My First Site Survey"**
3. Click **"Edit"** or the pencil icon
4. Make your changes in the Notebook Editor
5. **Save** your changes
6. You may need to **create a new version** (the system will guide you)

> 💡 **Tip**: Fieldmark keeps previous versions, so you can't accidentally destroy your work. Experiment freely!

### ✓ You'll Know It Worked When...

- [ ] You understand the four main user roles
- [ ] You know how to share notebooks (through teams)
- [ ] You can find the Edit button to modify your notebook
- [ ] You feel confident making changes

---

## Success Checklist

Congratulations! 🎊 Let's review everything you've accomplished:

- [ ] Logged in to Fieldmark and found your Dashboard
- [ ] Created a new notebook using the Notebook Editor
- [ ] Added five fields: text, select, date/time, multiline text, and photo
- [ ] Configured the Human-Readable ID Field (critical step!)
- [ ] Activated your notebook
- [ ] Created and saved your first record
- [ ] Saw your record display properly in the records list
- [ ] Understood basic sharing through teams
- [ ] Know how to edit and improve your notebook

**If you've ticked all these boxes, you're officially a Fieldmark notebook creator!** 🎯

---

## Quick Troubleshooting

Here are the most common issues and their solutions:

### Can't Find the Notebook Editor

**Solution**: Look for "Templates" in your navigation, then click "Create Template". If you don't see this option, check with your administrator - you may need the "Template Creator" role.

### Fields Not Showing in the Form

**Solution**: Make sure you clicked "Add Field" at the bottom of the dialogue. Also check that fields are in "Visible Fields" not "Hidden Fields" in the editor.

### Save Button Missing or Disabled

**Solution**: The Save button is always in the top-right corner. If it's greyed out, you may not have made any changes yet. If you don't see it at all, try refreshing the page.

### Can't Invite Team Members

**Solution**: Only Project Managers and System Administrators can invite users to teams. Ask your administrator to add colleagues to your team.

### Photos Won't Upload

**Solution**: On mobile, check camera permissions in your device settings. On desktop, the Take Photo field works best on mobile devices - consider using "Upload a File" instead for desktop testing.

### Records Show "rec_xxxxx" Instead of Readable Names

**Solution**: This is the most common issue! Go to Form Settings and set the "Human-Readable ID Field" to a text field like "Site Name". You may need to create a new active version of your notebook.

---

## Power User Tips

Ready to go further? Here are some advanced capabilities to explore:

### Virtual Roles Through Teams

For complex projects, you can create multiple teams with different access levels. Team membership automatically grants "virtual roles" that control who can see and edit which notebooks.

### API Automation

Fieldmark has a REST API that lets you programmatically create records, export data, and manage notebooks. Perfect for integrating with other systems.

### Conditional Logic

You can make fields appear or disappear based on other field values. For example, only show "Excavation Details" if Site Type is "Archaeological". This requires JSON editing but creates powerful dynamic forms.

### Template Library

As you create more notebooks, you'll build a library of reusable templates. Copy and modify existing notebooks rather than starting from scratch each time.

---

## What's Next?

Now that you've mastered the basics, here are your next steps:

### Immediate Next Steps

1. **Create a real notebook** for your actual project needs
2. **Add more field types** - try numbers, GPS locations, or dropdown hierarchies
3. **Enter several test records** to ensure your notebook works smoothly

### Learning Path

1. **Explore field types** - Fieldmark has text, numbers, dates, selections, GPS, photos, and more
2. **Learn form structure** - create multi-section forms with tabs and navigation
3. **Master validation** - make fields required, set number ranges, create patterns
4. **Try conditional logic** - show/hide fields based on user input

### Help Resources

- **Documentation**: Your administrator can provide links to full documentation
- **Community**: Ask questions in your organisation's Fieldmark community
- **Support**: Contact your system administrator for technical assistance
- **Training**: Request hands-on training sessions for your team

---

## Closing

You've just built your first data collection notebook in Fieldmark! This is a significant achievement - you've gone from zero to creating a working data collection system in just 15 minutes.

Remember, every expert was once a beginner. Don't be afraid to experiment, make mistakes, and learn. The Fieldmark system is designed to be forgiving - you can always edit, improve, and refine your notebooks.

Your journey in field data collection has just begun. Welcome to the community of researchers, archaeologists, ecologists, and field workers using Fieldmark to capture better data in the field.

Happy field working!

---

*Note: Fieldmark was formerly known as FAIMS3 (Field Acquired Information Management Systems). You may see references to FAIMS3 in older documentation or community discussions - it's the same platform with a new name.*
