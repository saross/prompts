## General Guidance on Crafting Effective Prompts

These guidelines will help you create effective prompts for me (and LLMs in general), covering key principles and techniques.

**Core Principles:**

*   **Be Clear and Specific:** Ambiguity is the enemy. The more precisely you define what you want, the better the results will be. Assume I have no prior knowledge or context unless you explicitly provide it.
*   **Define the Task:** Clearly state what you want me to *do*. Are you asking me to summarize, translate, write code, answer a question, generate creative text, etc.?
*   **Specify the Format:** How should the output look? Do you need Markdown, JSON, Python code, a specific writing style, a table, etc.?
*   **Provide Context:** Give me the background information I need to understand the task. This might include the topic, audience, purpose, or any relevant constraints.
*   **Iterate and Refine:** Don't be afraid to experiment. If the first result isn't perfect, tweak your prompt and try again. I learn from your feedback!

**Key Techniques:**

*   **Role Play:** Assign me a role (e.g., "Act as a seasoned marketing consultant"). This can influence my tone, style, and perspective.
*   **Exemplars (Few-Shot Learning):** Provide examples of the kind of output you're looking for. This is incredibly powerful. Even a single example can significantly improve the quality of the results.
*   **Constraints:** Define limitations (e.g., "Keep the summary under 200 words," "Use only information from the provided text").
*   **Tone and Style:** Specify the desired tone (e.g., "Write in a formal, professional tone") and style (e.g., "Use a concise and persuasive writing style").
*   **Decomposition:** Break down complex tasks into smaller, more manageable steps. Instead of asking for a complete marketing plan, ask for specific sections (e.g., "Generate a list of potential target audiences").
*   **Chain of Thought:** For complex reasoning tasks, explicitly prompt me to show my reasoning step-by-step. This often leads to more accurate results. For example: "First, identify the key facts. Then, apply those facts to the following rule... Finally, state the conclusion."
*   **Input Data:** Make it as easy as possible for me to access and process the data. If you're working with a long document, consider summarizing it first or providing relevant excerpts. For audio, clear instructions like you have been using, is ideal.

**Common Pitfalls to Avoid:**

*   **Vague Language:** Avoid words like "good," "interesting," or "creative" without further definition.
*   **Unrealistic Expectations:** I am powerful, but I'm not magic. I can't generate information that doesn't exist or solve problems that are fundamentally unsolvable.
*   **Overly Complex Prompts:** Keep your prompts as simple and focused as possible. If a prompt is too long or convoluted, it can be difficult for me to understand.
*   **Ignoring Errors:** If you notice a mistake, point it out! I learn from my mistakes and will try to avoid them in the future.

**Specific Tips for Transcription (Based on Your Use Case):**

*   **Noise Handling:** If you know there will be specific types of noise (e.g., background music, static), mention it in the prompt and ask me to try to filter it out.
*   **Technical Jargon:** If the interview contains technical terms or jargon, provide a glossary or explanation.
*   **Accents:** If the speakers have strong accents, acknowledge this in the prompt and ask me to pay extra attention to pronunciation.
*   **Speaker Overlap:** Speaker overlap is one of the most challenging aspects of transcription. Consider explicitly instructing me on how to handle it. For example: "If speakers overlap, indicate the point of overlap with brackets like this: 'Speaker A: I think that... [Speaker B: It's important to consider...] ...it's a great idea.'"
