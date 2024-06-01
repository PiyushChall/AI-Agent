from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from blog_tools import search_tool
import os

google_api_key = os.environ['GOOGLE_API_KEY']
llm = ChatGoogleGenerativeAI(
  model="gemini-1.5-pro",
  verbose=True,
  temperature=0.5,
  google_api_key=google_api_key,
)


blog_researcher = Agent(
    role="Senior Researcher",
    goal=(
        """Explore the bleeding edge of {topic} and identify promising new techs."""
    ),
    verbose=True,
    memory=True,
    backstory=(
        """Curiosity burns bright, guiding you to the frontiers of innovation.
        Unearthing knowledge isn't enough; you're passionate about sharing it,
        empowering others to change the world with you."""
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=True
)

blog_writer = Agent(
    role="Writer",
    goal=(
        """Craft enthralling narratives that ignite curiosity about {topic} tech
        Also proof read your work properly.
        Check for any grammatical errors and spelling mistakes, and correct them 
        if necessary. Also make sure to check the key points of your article."""
    ),
    verbose=True,
    memory=True,
    backstory=(
        """A master storyteller with a knack for untangling complexity,
        you weave engaging narratives that captivate and educate.
        You illuminate groundbreaking discoveries, making them accessible to all."""
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=True
)
