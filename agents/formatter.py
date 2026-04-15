"""
Deprecated: This agent is now loaded from config/agents.yml
Use AgentFactory from config.agent_factory instead.
"""
from config.agent_factory import AgentFactory

class FormatterAgent:
    def __init__(self):
        factory = AgentFactory()
        self.agent = factory.create_agent('formatter')

    def get_agent(self):
        return self.agent