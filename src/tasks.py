from crewai import Task

def create_tasks(topic_agent, research_agent, evaluator_agent, formatter_agent, email_agent, topic_provided=False, topic=None):
    if not topic_provided:
        find_topic_task = Task(
            description="Identify a trending and engaging topic in the tech industry suitable for a blog post.",
            agent=topic_agent,
            expected_output="A concise topic title for the blog post."
        )
        research_context = [find_topic_task]
        research_description = "Conduct thorough research on the selected topic, gathering facts, examples, and relevant information from reliable sources."
    else:
        find_topic_task = None
        research_context = []
        research_description = f"Conduct thorough research on the topic: {topic}, gathering facts, examples, and relevant information from reliable sources."

    research_task = Task(
        description=research_description,
        agent=research_agent,
        expected_output="A detailed research summary with updated facts, examples, and citations.",
        context=research_context
    )

    evaluate_task = Task(
        description="Evaluate the researched content for accuracy, reliability, and completeness by cross-checking with multiple sources.",
        agent=evaluator_agent,
        expected_output="Validated content with confirmed facts and any corrections or additions.",
        context=[research_task]
    )

    format_task = Task(
        description="Format the validated content into a comprehensive Medium-style blog post. Structure the post with the following sections: Introduction (hook and overview), Background (historical context and evolution), Why It Is Needed (problem it solves and benefits), Analogy (simple explanation using a relatable analogy), Examples (basic code snippets and configurations), Real-World Use Cases (industry applications with examples), Pros and Cons (balanced analysis), Alternatives (comparison with other tools/solutions), Best Practices (from basic to advanced usage guidelines), and Conclusion (summary, final thoughts, closing statement, and future outlook). Include citations throughout and ensure the content covers basic to advanced usage. Make it engaging, informative, and suitable for a technical audience.",
        agent=formatter_agent,
        expected_output="A fully formatted blog post in Markdown format, ready for publication, with all specified sections and examples.",
        context=[evaluate_task]
    )

    email_task = Task(
        description="Send the formatted blog post as an email attachment to the specified recipient.",
        agent=email_agent,
        expected_output="Confirmation that the email has been sent successfully.",
        context=[format_task]
    )

    if topic_provided:
        return [research_task, evaluate_task, format_task, email_task]
    else:
        return [find_topic_task, research_task, evaluate_task, format_task, email_task]