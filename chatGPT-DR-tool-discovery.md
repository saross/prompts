Hi ChatGPT.

Today we're going to be doing a deep and systematic literature **search**. This is one component of a much longer process, so you're going to need to be specific, focused, meticulous, and detail-oriented.

We need to read through JOAD, issue by issue https://openarchaeologydata.metajnl.com/issue/archive article by article, and make a list of EVERY SINGLE ARTICLE. 

Our objective is, within each article to identify mentions of software tools which meet our criteria:
<criteria>
# Tool definition
For our project, a software tool is any discrete piece of software—be it a program, script, or web application—that is developed or substantially modified by researchers to perform specific, research-oriented computational tasks. These tasks must involve active data processing, such as analysis, simulation, visualization, modeling, or automation, where input data is dynamically created, documented, transformed, or interpreted to generate meaningful results. In contrast, products whose primary function is to simply display, store, or promote static datasets—without offering mechanisms for active computational engagement—are excluded. 

In essence, a valid software tool for our purposes is one that not only **supports research in archaeology or historical sciences** but does so by actively collecting and/or processing data rather than merely serving as a generic data repository or static interface.
</criteria>


**Data to Extract for Each Article:**  
- **Title:** The title of the article, enclosed in quotes.  
- **Authors:** The article’s authors, listed in a dedicated column.  
- **URL:** A direct link to the article.  
- **Issue Number:** Volume and Issue as referenced in https://joss.theoj.org/toc
- **Year:** The publication year of the article.  
- **Tools Mentioned:** Explicitly named research software tools used for the relevant research tasks (multiple entries allowed, separated by semicolons).

**Output Format:**  
The final dataset should be output as a CSV file inside a code block. The columns must appear in this exact order:

"Title"	"Authors"	"URL"	"Issue Number"	"Year"	"Tools Mentioned"

**Additional Instructions:**  
- **No inline citations:** Avoid any extra markers or citation references within the data cells to prevent data corruption.  
- **Meticulous research:** Take as much time as needed to carefully review each article and verify the accuracy of tool mentions.  
- **Error Reporting:** If any errors or issues arise during the process, provide a separate error log outlining the encountered problems.  
- **Iterative Process:** This is a long-term, iterative project, so precision is prioritized over speed.  

Please begin with issues 1-8. 