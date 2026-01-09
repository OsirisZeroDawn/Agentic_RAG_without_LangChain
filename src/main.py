from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import GalaxonOrchestrator

app = FastAPI()
orchestrator = GalaxonOrchestrator()


class IdeaInput(BaseModel):
    idea: str


@app.post("/analyze")
def analyze (input: IdeaInput):
        return orchestrator.run(input.idea)

"""
Sub-Tasks Definition

1- User Interface Development
Design and implement a simple web-based user interface using streamlit or Gradio.

2- Prompt Engineering
Create a refine structured prompt for each AI agetn to ensure clear reasoning, role seperation.

3- Structure Output Definition
Define the expected AI outputs according to business requirements, specifying dimensions such as industry, competitors, oppurtunities, and bling spots.

4- Dashboard
Build a simple dashboard that transforms the structured AI outputs into clear tables and charts

"""
