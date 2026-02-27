import openai


class PromptAgent:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)
        self.system_prompt = """
        Act as a Senior Prompt Engineer. Your goal is to transform the user's raw input into a high-quality, structured prompt.
        Apply the following framework:
        1. Assign a specific Expert Persona.
        2. Define clear Context and Task.
        3. Specify Output Format and Style.
        4. Include Constraints and Step-by-Step reasoning instructions (Chain of Thought).

        Structure your response as follows:
        ---
        ###  IMPROVED PROMPT
        [The optimized prompt ready to copy-paste]

        ###  IMPROVEMENTS MADE
        [Brief bullet points explaining the engineering techniques used]
        ---
        """

    def improve(self, user_input):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Improve this prompt: {user_input}"}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
