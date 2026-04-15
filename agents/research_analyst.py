"""
Deprecated: This agent is now loaded from config/agents.yml
Use AgentFactory from config.agent_factory instead.
"""
from config.agent_factory import AgentFactory

class ResearchAnalystAgent:
    def __init__(self):
        factory = AgentFactory()
        self.agent = factory.create_agent('research_analyst')

    def get_agent(self):
        return self.agent