from crewai import Agent
import api
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = api.GOOGLE_API_KEY
llm = ChatGoogleGenerativeAI(model="",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=api_key
                             )

news_researcher = Agent(
    role="Senior Researcher",
    goel='Discover new technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at hte forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[],
    llm=llm,
    allow_delegation=True
)

news_writer = Agent(
    role="Writer",
    goel='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With creative skill of simplifying complex topic, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)