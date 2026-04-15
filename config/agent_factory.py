import os
from crewai import Agent
from crewai_tools import SerperDevTool
from config.config_loader import ConfigLoader

class AgentFactory:
    def __init__(self):
        self.config_loader = ConfigLoader(os.path.join(os.path.dirname(__file__)))
        self.agents = {}
    
    def _load_tool(self, tool_config):
        """Load a tool based on configuration."""
        tool_type = tool_config.get('type')
        
        if tool_type == 'SerperDevTool':
            api_key_env = tool_config.get('config', {}).get('api_key_env')
            api_key = os.getenv(api_key_env)
            return SerperDevTool(api_key=api_key)
        elif tool_type == 'EmailTool':
            # Import dynamically to avoid circular imports
            from tools.email_tool import send_email_tool
            return send_email_tool
        
        return None
    
    def create_agent(self, agent_name):
        """Create an agent from YAML configuration."""
        if agent_name in self.agents:
            return self.agents[agent_name]
        
        agent_config = self.config_loader.get_agent_config(agent_name)
        if not agent_config:
            raise ValueError(f"Agent configuration not found: {agent_name}")
        
        # Load tools
        tools = []
        for tool_config in agent_config.get('tools', []):
            tool = self._load_tool(tool_config)
            if tool:
                tools.append(tool)
        
        # Create agent
        agent = Agent(
            role=agent_config.get('role'),
            goal=agent_config.get('goal'),
            backstory=agent_config.get('backstory'),
            verbose=agent_config.get('verbose', True),
            allow_delegation=agent_config.get('allow_delegation', False),
            llm=agent_config.get('llm', 'gpt-4o-mini'),
            tools=tools
        )
        
        self.agents[agent_name] = agent
        return agent
    
    def create_all_agents(self):
        """Create all agents from configuration."""
        agents_config = self.config_loader.get_all_agents_config()
        agents_dict = {}
        
        for agent_name in agents_config.keys():
            agents_dict[agent_name] = self.create_agent(agent_name)
        
        return agents_dict
