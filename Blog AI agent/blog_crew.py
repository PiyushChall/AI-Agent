from crewai import Crew, Process
from blog_agents import blog_researcher, blog_writer, llm
from blog_tasks import research_task, write_task

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.hierarchical,
    manager_llm=llm
)

topic = input("Feed me the topic: ")
result = crew.kickoff(inputs={"topic": topic})
print(result)
