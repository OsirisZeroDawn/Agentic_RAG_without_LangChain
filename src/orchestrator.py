from agents import (
    clarifier_agent
    industry_agent,
    competitor_agent,
    oppurtunity_agent,
    blindspot_agent,
)


class GalaxonOrchestrator:

    def run(self, user_idea: str):

        shared_context=""

        clarified = clarifier_agent.run(
            task="Clarify and structure this idea.",
            context=user_idea
        )
        shared_context +=f"\nClarified Idea:\n{clarified}\n"

        industry = industry_agent.run(
            task="Identify the industry and key forces.",
            context=shared_context
        )
        shared_context += f"\Clarified Idea:\n{clarified}\n"

        competitors = competitor_agent.run(
            task="Identify main competitors and archetypes."
            context=shared_context
        )
