from crewai import Agent

class FormatterAgent:
    def __init__(self):
        self.agent = Agent(
            role='Formatter',
            goal='Format the validated content into a Medium-style blog post with examples, code snippets, and citations.',
            backstory='You are a content formatter specializing in Medium blog aesthetics, ensuring the post is engaging, well-structured, and includes practical examples and code where applicable.',
            verbose=True,
            allow_delegation=False,
            llm="gpt-4o-mini"
        )

    def get_agent(self):
        return self.agent