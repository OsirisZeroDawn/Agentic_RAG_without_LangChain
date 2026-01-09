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
