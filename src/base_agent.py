from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

class BaseAgent:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def run(self,task: str, context:dict)
        messages = [
            {"role":"system","content":self.system_prompt}
        ]
