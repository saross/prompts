# Task: Form Navigation and Data Flow Documentation

## Context
Create third-draft LLM-first documentation for Form Navigation and Data Flow in Fieldmark/FAIMS3.

## Reference Documents
- "Notebook Structure Documentation - Status Update.md"
- "Conditional Logic System - Third Draft Documentation"
- "Documentation State & Decisions Record"

## STRICT WORKFLOW - FOLLOW EXACTLY

### Step 1: Ask Questions (DO NOT SKIP)
Create TWO separate lists:
1. **5-6 Design Questions for me** (user experience, workflow, patterns)
2. **4-6 Technical Questions for Claude Code** (in markdown code block)

### Step 2: STOP AND WAIT
- Wait for my answers to design questions
- Wait for Claude Code responses
- Ask follow-up clarifications if needed
- DO NOT PROCEED WITHOUT ANSWERS

### Step 3: Repeat
- Create next batch of 4-6 questions
- Continue until you have enough information
- Typically need 3-4 batches total

### Step 4: Create Documentation
- ONLY after collecting all answers
- Use tags: {essential} {important} {comprehensive}

## EXAMPLE FORMAT REQUIRED

```
Design Questions (for you):
1. What navigation patterns are most common?
2. How do users save and resume?
[3-4 more]

Technical Questions (for Claude Code):
```markdown
# Navigation Batch 1: Core Mechanics

1. **Navigation State**
   - How is current section tracked?
   - What data structure stores navigation state?

2. **Draft Saving**
   - When are drafts created?
   - Auto-save frequency?

[2-4 more questions maximum]
```
```

## CRITICAL RULES
✅ Maximum 6 questions per batch
✅ Separate design from technical
✅ Use markdown blocks for Claude Code
✅ WAIT for answers before next batch
✅ NO documentation until Step 4

❌ NO 60-question lists
❌ NO immediate documentation generation
❌ NO proceeding without answers

## Areas to Investigate
- Navigation patterns (linear/non-linear)
- Draft save/resume
- Parent-child data flow
- Progress tracking
- Required field navigation
- Export/submission process

Remember: Ask → Wait → Clarify → Repeat → Document