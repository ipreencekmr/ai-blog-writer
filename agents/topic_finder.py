from crewai import Agent
from crewai_tools import SerperDevTool
import os

class TopicFinderAgent:
    def __init__(self):
        self.agent = Agent(
            role='Topic Finder',
            goal='Identify trending and relevant topics in the tech industry for blog writing.',
            backstory='You are an expert in tech trends, constantly monitoring industry news, social media, and emerging technologies to find compelling topics that resonate with readers.',
            verbose=True,
            allow_delegation=False,
            tools=[SerperDevTool(api_key=os.getenv('SERPER_API_KEY'))]
        )

    def get_agent(self):
        return self.agent