from crewai import Task

def create_tasks(topic_agent, research_agent, evaluator_agent, formatter_agent, email_agent):
    find_topic_task = Task(
        description="Identify a trending and engaging topic in the tech industry suitable for a blog post.",
        agent=topic_agent,
        expected_output="A concise topic title for the blog post."
    )

    research_task = Task(
        description="Conduct thorough research on the selected topic, gathering facts, examples, and relevant information from reliable sources.",
        agent=research_agent,
        expected_output="A detailed research summary with facts, examples, and citations.",
        context=[find_topic_task]
    )

    evaluate_task = Task(
        description="Evaluate the researched content for accuracy, reliability, and completeness by cross-checking with multiple sources.",
        agent=evaluator_agent,
        expected_output="Validated content with confirmed facts and any corrections or additions.",
        context=[research_task]
    )

    format_task = Task(
        description="Format the validated content into a Medium-style blog post, including an introduction, body with examples and code snippets, and citations.",
        agent=formatter_agent,
        expected_output="A fully formatted blog post in Markdown format, ready for publication.",
        context=[evaluate_task]
    )

    email_task = Task(
        description="Send the formatted blog post as an email attachment to the specified recipient.",
        agent=email_agent,
        expected_output="Confirmation that the email has been sent successfully.",
        context=[format_task]
    )

    return [find_topic_task, research_task, evaluate_task, format_task, email_task]