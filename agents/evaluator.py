from crewai import Agent
from crewai_tools import SerperDevTool
import os

class EvaluatorAgent:
    def __init__(self):
        self.agent = Agent(
            role='Evaluator',
            goal='Validate the accuracy and reliability of the researched content and facts from multiple sources.',
            backstory='You are a fact-checker extraordinaire, cross-referencing information across various sources to ensure the content is truthful, up-to-date, and well-substantiated.',
            verbose=True,
            allow_delegation=False,
            llm="gpt-4o",
            tools=[SerperDevTool(api_key=os.getenv('SERPER_API_KEY'))]
        )

    def get_agent(self):
        return self.agent