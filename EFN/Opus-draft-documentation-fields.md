Hi Opus, I'd like to pick up here where I left off in another chat. We're extending the 'Field Selection Best Practices' guide (see project knowledge) for FAIMS3 / Fieldmark, an electronic field notebook platform, by producing detailed guides about when and how to use each field type.   For background, please see 'field-types-user-guide', 'field-design-insights-for-opus' (from Claude Code, who analysed the codebase to produce technical specs for the field creation), 'field-types-user-guide', and especially 'development summary and next steps'.   # Overall goal  Our goal is to produce a comprehensive guide that can improve Claude Code's decisions when it is creating JSON definition files for notebooks from user input of various kinds (direct instructions, fieldwork protocols or guides, data specifications, etc.). We will later make derivative, human-focused documentation; this document is CC-first.  

# Current status and next task  

Let's resume with the to-do list. We are proceeding category-by-category (text field, number fields, date & time fields, etc.; see summary table in project knowledge for categories), producing detailed guides for each.  

We have finished drafts of: 
* Text fields
* Number fields 
* Date and Time fields 
* Media fields
* Location fields

These markdown documents can be found in project knowledge, use them as models. 

We are now ready to begin 'Choice' fields.

# Steps

1. For each category, please review available information in:
   - The summary table
   - the 'best practice guide' specific to the individual fields
   - 'Notebook JSON', 'Overview of Related Records', 'user guide' and 'insights for Opus' documents, so long as they are not contradicted or superceded by the 'summary table' or 'best practice guide'

2. Silent scan: privately consider the information you have and list additional information you still need.

3. Clarify loop: ask me clarigying questions *one question at a time* until you estimate with >95% confidence that you understand how each field works, when it should be chosen, and how it should be used, such that you could (a) deciding when field use is appropriate and (b) deploying that field (this confidence level will be a good benchmark for ensuring CC will also understand when and how to use each field). 

4. Blueprint: when you reach 95% confidence, produce a brief, crisp outline of the detailed category guide (max 1/10th length of actual category) in chat *not* as an artefact. Your model is 'Text Field - Detailed Documentation.md' in project knowledge. Request feedback or approval from me before proceeding.

5. Build and self-test: 
    - Once you get approval to generate the complete guide, do so.
    - For each field type, write your description, and be sure to always include sections on:
      - Technical Characteristics
      - Best Practice Recommendations
      - See also (cross references to related fields)
      - Known Issues
      - Limitations 
    - Do a final accuracy check and style alignment check ('academic eloquence' style)
    - Fix anything you find and deliver the final category guide as a markdown artefact modeled on 'Text Field - Detailed Documentation.md' in project knowledge.