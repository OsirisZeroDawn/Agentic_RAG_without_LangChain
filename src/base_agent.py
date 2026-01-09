from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

class BaseAgent:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def run(self,task: str, context:dict):
        messages = [
            {"role":"system","content":self.system_prompt},
            {
                "role":"user",
                "content":f"""Task:{task}
                 Context:{context}
            """
            }
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
#possible error with deprecated Open AI API call here
        return response.choices[0].message.content


# there is a possible issue in the structuring of the openai api call, particularly with the SDK formatting not being correct, it has been suggested this is a better way (see below)
# from openai import OpenAI
# from openai.types.chat import ChatCompletionMessageParam

# client = OpenAI()

# class BaseAgent:
#     def __init__(self, system_prompt: str):
#         self.system_prompt = system_prompt

#     def run(self, task: str, context: dict):
#         messages: list[ChatCompletionMessageParam] = [
#             {"role": "system", "content": self.system_prompt},
#             {"role": "user", "content": f"Task: {task}\nContext: {context}"},
#         ]

#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=messages
#         )

#         return response.choices[0].message.content
