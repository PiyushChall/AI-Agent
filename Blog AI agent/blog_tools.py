from crewai_tools import SerperDevTool
import os

serper_api_key = os.environ['SERPER_API_KEY']

search_tool = SerperDevTool()
