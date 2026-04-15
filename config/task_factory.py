from crewai import Task
from config.config_loader import ConfigLoader

class TaskFactory:
    def __init__(self, agents_dict):
        """
        Initialize TaskFactory with a dictionary of agents.
        
        Args:
            agents_dict: Dictionary with agent names as keys and Agent objects as values
        """
        self.config_loader = ConfigLoader()
        self.agents_dict = agents_dict
        self.tasks = {}
    
    def create_task(self, task_name):
        """Create a task from YAML configuration."""
        if task_name in self.tasks:
            return self.tasks[task_name]
        
        task_config = self.config_loader.get_task_config(task_name)
        if not task_config:
            raise ValueError(f"Task configuration not found: {task_name}")
        
        # Get the agent
        agent_name = task_config.get('agent')
        agent = self.agents_dict.get(agent_name)
        if not agent:
            raise ValueError(f"Agent not found for task: {task_name}")
        
        # Build context from dependencies
        context_task_names = task_config.get('context', [])
        context = []
        for context_task_name in context_task_names:
            context.append(self.create_task(context_task_name))
        
        # Create task
        task = Task(
            description=task_config.get('description'),
            agent=agent,
            expected_output=task_config.get('expected_output'),
            context=context
        )
        
        self.tasks[task_name] = task
        return task
    
    def create_tasks_for_sequence(self, sequence_name):
        """
        Create all tasks for a given sequence.
        
        Args:
            sequence_name: Name of the task sequence (e.g., 'with_topic_generation', 'with_topic_provided')
        
        Returns:
            List of Task objects in the correct order
        """
        task_names = self.config_loader.get_task_sequence(sequence_name)
        if not task_names:
            raise ValueError(f"Task sequence not found: {sequence_name}")
        
        tasks = []
        for task_name in task_names:
            tasks.append(self.create_task(task_name))
        
        return tasks
