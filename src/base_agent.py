from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

class BaseAgent:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def run(self,task: str, context:dict)
        messages = [
            {"role":"system","content":self.system_prompt},
            {
                "role":"user"
                "content":f"""Task:{task}
                 Context:{context}
            """
            }
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return response.choices[0].message.content
