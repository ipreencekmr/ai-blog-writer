import os
import sys
import argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from dotenv import load_dotenv
from crewai import Crew
from config.agent_factory import AgentFactory
from config.task_factory import TaskFactory
from utils.utils import write_blog
import schedule
import time

load_dotenv()

def run_blog_creation(topic=None, topic_provided=False):
    # Initialize agent factory and create all agents
    agent_factory = AgentFactory()
    agents_dict = agent_factory.create_all_agents()
    
    # Determine which task sequence to use
    sequence_name = 'with_topic_provided' if topic_provided else 'with_topic_generation'
    
    # Initialize task factory and create tasks
    task_factory = TaskFactory(agents_dict)
    tasks = task_factory.create_tasks_for_sequence(sequence_name)
    
    # Get agents list for crew
    agent_order = ['topic_finder', 'research_analyst', 'evaluator', 'formatter', 'email_sender']
    if topic_provided:
        agent_order = agent_order[1:]  # Remove topic_finder if topic is provided
    
    agents = [agents_dict[agent_name] for agent_name in agent_order]
    
    # Create and run crew
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("Blog creation completed:", result)
    
    # ✅ Save blog from formatter task
    write_blog(tasks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Blog Writer")
    parser.add_argument('--topic', default=os.getenv('TOPIC'), help='Topic for the blog post')
    parser.add_argument('--to_email', default=os.getenv('TO_EMAIL'), help='Email to send the blog to')
    args = parser.parse_args()

    topic_provided = args.topic is not None
    topic = args.topic

    if args.to_email:
        os.environ['EMAIL_TO'] = args.to_email

    # For testing, run once
    run_blog_creation(topic=topic, topic_provided=topic_provided)

    # For daily scheduling (uncomment to enable)
    # schedule.every().day.at("09:00").do(run_blog_creation)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)  # Check every minute