import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from dotenv import load_dotenv
from crewai import Crew
from agents.topic_finder import TopicFinderAgent
from agents.research_analyst import ResearchAnalystAgent
from agents.evaluator import EvaluatorAgent
from agents.formatter import FormatterAgent
from agents.email_agent import EmailAgent
from src.tasks import create_tasks
import schedule
import time

load_dotenv()

def run_blog_creation():
    # Initialize agents
    topic_agent = TopicFinderAgent().get_agent()
    research_agent = ResearchAnalystAgent().get_agent()
    evaluator_agent = EvaluatorAgent().get_agent()
    formatter_agent = FormatterAgent().get_agent()
    email_agent = EmailAgent().get_agent()

    # Create tasks
    tasks = create_tasks(topic_agent, research_agent, evaluator_agent, formatter_agent, email_agent)

    # Create and run crew
    crew = Crew(
        agents=[topic_agent, research_agent, evaluator_agent, formatter_agent, email_agent],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("Blog creation completed:", result)

if __name__ == "__main__":
    # For testing, run once
    run_blog_creation()

    # For daily scheduling (uncomment to enable)
    # schedule.every().day.at("09:00").do(run_blog_creation)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)  # Check every minute