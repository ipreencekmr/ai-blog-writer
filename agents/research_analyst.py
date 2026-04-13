from crewai import Agent
from crewai_tools import SerperDevTool
import os

class ResearchAnalystAgent:
    def __init__(self):
        self.agent = Agent(
            role='Research Analyst',
            goal='Gather detailed, factual information on the selected topic from reliable sources.',
            backstory='You are a meticulous researcher with access to web search tools, skilled in compiling comprehensive data, examples, and insights on tech topics.',
            verbose=True,
            allow_delegation=False,
            tools=[SerperDevTool(api_key=os.getenv('SERPER_API_KEY'))]
        )

    def get_agent(self):
        return self.agent