from base_agent import BaseAgent

clarifier_agent = BaseAgent(
    "You clarify and structure vague business ideas"
)

industry_agent = BaseAgent(
    "You indentify the industry and environment of a business idea."
)

competitor_agent = BaseAgent(
    "You identify competitors and group them into archetypes."
)

oppurtunity_agent = BaseAgent(
    "You identify market gaps and oppurtunities."
)

blindspot_agent = BaseAgent(
    "You critically detect missing or unclear elements."
)
