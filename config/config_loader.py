import yaml
import os
from pathlib import Path

class ConfigLoader:
    def __init__(self, config_dir=None):
        if config_dir is None:
            config_dir = os.path.join(os.path.dirname(__file__))
        self.config_dir = config_dir
        self.agents_config = None
        self.tasks_config = None
        self._load_configs()
    
    def _load_configs(self):
        """Load YAML configuration files."""
        agents_path = os.path.join(self.config_dir, 'agents.yml')
        tasks_path = os.path.join(self.config_dir, 'tasks.yml')
        
        with open(agents_path, 'r') as f:
            self.agents_config = yaml.safe_load(f)
        
        with open(tasks_path, 'r') as f:
            self.tasks_config = yaml.safe_load(f)
    
    def get_agent_config(self, agent_name):
        """Get configuration for a specific agent."""
        if not self.agents_config:
            self._load_configs()
        return self.agents_config.get('agents', {}).get(agent_name)
    
    def get_all_agents_config(self):
        """Get all agents configuration."""
        if not self.agents_config:
            self._load_configs()
        return self.agents_config.get('agents', {})
    
    def get_task_config(self, task_name):
        """Get configuration for a specific task."""
        if not self.tasks_config:
            self._load_configs()
        return self.tasks_config.get('tasks', {}).get(task_name)
    
    def get_all_tasks_config(self):
        """Get all tasks configuration."""
        if not self.tasks_config:
            self._load_configs()
        return self.tasks_config.get('tasks', {})
    
    def get_task_sequence(self, sequence_name):
        """Get a predefined task sequence."""
        if not self.tasks_config:
            self._load_configs()
        return self.tasks_config.get('task_sequences', {}).get(sequence_name, {}).get('tasks', [])
