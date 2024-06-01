from crewai import Task
from blog_tools import search_tool
from blog_agents import blog_researcher, blog_writer

research_task = Task(
    description=(
        "Develop a compelling narrative that captures the essence of the {topic}"
        "considering its potential to disrupt or reshape the {topic} ecosystem."
        "Your final report should clearly articulate the key points,"
        "its market opportunities and potential risks"
    ),
    expected_output="A comprehensive report on the latest {topic} trends.",
    tools=[search_tool],
    agent=blog_researcher
)

write_task = Task(
    description=(
        """Weave a captivating narrative that explores the essence of {topic}.
        Based on the Senior Researcher's research, consider its origins, key developments, 
        and the human element that drives its evolution.
        Then proof read your work properly."""
    ),
    expected_output=(
        "Write an article about {topic} trends."
        "Formatted as markdown"
    ),
    tools=[search_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog.md"
)
