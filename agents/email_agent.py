from crewai import Agent
from tools.email_tool import send_email_tool

class EmailAgent:
    def __init__(self):
        self.agent = Agent(
            role='Email Sender',
            goal='Send the formatted blog post as a document attachment via email.',
            backstory='You are responsible for delivering the final blog post to the user via email, ensuring it reaches the intended recipient securely.',
            verbose=True,
            allow_delegation=False,
            tools=[send_email_tool]
        )

    def get_agent(self):
        return self.agent