"""
Deprecated: This agent is now loaded from config/agents.yml
Use AgentFactory from config.agent_factory instead.
"""
from config.agent_factory import AgentFactory

class TopicFinderAgent:
    def __init__(self):
        factory = AgentFactory()
        self.agent = factory.create_agent('topic_finder')

    def get_agent(self):
        return self.agent