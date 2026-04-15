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
        self.topic = None
        self.current_date = None
        self.current_year = None
    
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
        
        # Inject topic into description if provided
        description = task_config.get('description')
        if task_name == 'find_topic':
            year_context = f" for {self.current_year}" if self.current_year else ""
            description = f"Identify a trending and engaging topic in the tech industry suitable for a blog post{year_context}. Focus on current trends. Avoid outdated topics from previous years. Make sure the topic is fresh, relevant, and timely for this year."
        elif self.topic and task_name == 'research':
            date_context = f" Today's date is {self.current_date}." if self.current_date else ""
            description = f"Conduct thorough up-to-date research on the following topic: '{self.topic}'. Find the most recent information and latest developments.{date_context} Gather facts, examples, and relevant information from reliable sources. Ensure all information is current and not outdated."
        elif self.topic and task_name == 'evaluate':
            description = f"Evaluate the researched content about '{self.topic}' for accuracy, reliability, and completeness by cross-checking with multiple sources."
        elif self.topic and task_name == 'format':
            description = f"Format the validated content about '{self.topic}' into a comprehensive Medium-style blog post. Structure the post with the following sections: Introduction (hook and overview), Background (historical context and evolution), Why It Is Needed (problem it solves and benefits), Analogy (simple explanation using a relatable analogy), Examples (practical descriptions and explanations), Real-World Use Cases (industry applications with examples), Pros and Cons (balanced analysis), Alternatives (comparison with other tools/solutions), Best Practices (from basic to advanced usage guidelines), and Conclusion (summary, final thoughts, closing statement, and future outlook). Include citations throughout and ensure the content covers basic to advanced usage. Use Medium blog formatting including bold, italics, headers, and proper section breaks for readability and engagement. DO NOT use markdown code blocks (triple backticks). Instead, describe code concepts and examples in natural language with proper emphasis and formatting. Make it engaging, informative, and suitable for a technical audience."
        
        # Create task
        task = Task(
            description=description,
            agent=agent,
            expected_output=task_config.get('expected_output'),
            context=context
        )
        
        self.tasks[task_name] = task
        return task
    
    def create_tasks_for_sequence(self, sequence_name, topic=None, current_date=None, current_year=None):
        """
        Create all tasks for a given sequence.
        
        Args:
            sequence_name: Name of the task sequence (e.g., 'with_topic_generation', 'with_topic_provided')
            topic: The topic to research (optional, for sequences with_topic_provided)
            current_date: Current date string for context (e.g., 'April 15, 2026')
            current_year: Current year (e.g., 2026)
        
        Returns:
            List of Task objects in the correct order
        """
        # Store topic, date, and year for use in create_task
        self.topic = topic
        self.current_date = current_date
        self.current_year = current_year
        
        task_names = self.config_loader.get_task_sequence(sequence_name)
        if not task_names:
            raise ValueError(f"Task sequence not found: {sequence_name}")
        
        tasks = []
        for task_name in task_names:
            tasks.append(self.create_task(task_name))
        
        return tasks
