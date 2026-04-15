import os

def write_blog(tasks, output_path="output/blog.md"):
    """
    Extracts formatter task output from task list and writes to a markdown file.
    """

    # 🔍 Step 1: Find formatter task
    format_task = None

    for task in tasks:
        # Match by agent role (most reliable)
        if hasattr(task, "agent") and task.agent:
            role = getattr(task.agent, "role", "").lower()
            if "formatter" in role:
                format_task = task
                break

        # Fallback: match by description
        if "format" in task.description.lower():
            format_task = task

    if not format_task:
        raise ValueError("❌ Formatter task not found in task list")

    # 🔍 Step 2: Extract output safely
    formatted_blog = None

    if format_task.output:
        formatted_blog = (
            getattr(format_task.output, "raw", None)
            or getattr(format_task.output, "result", None)
            or str(format_task.output)
        )

    if not formatted_blog or not formatted_blog.strip():
        raise ValueError("❌ Formatter task did not produce any content")

    # 📁 Step 3: Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 💾 Step 4: Write file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted_blog)

    print(f"✅ Blog saved at {output_path}")