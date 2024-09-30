from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDataBaseTool,
)
from langchain_community.utilities.sql_database import SQLDatabase

from textwrap import dedent

from langchain_openai import ChatOpenAI

from crewai import Agent, Crew, Process, Task
from crewai_tools import tool
from crewai.crews.crew_output import CrewOutput

from dotenv import load_dotenv
import os
import re

# Change the default LLM
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"
llm = ChatOpenAI(model="gpt-4o-mini")

data_visualiser  = Agent(
    role="Data Visualization Specialist",
    goal="You receive data from the database developer and visualize it",
    backstory=dedent(
        """
        You have deep experience with visualizing data using Python and create
        graphs using Plotly.
        Your work is always based on the provided data and is clear,
        easy-to-understand and to the point. You have attention
        to detail and always produce very detailed work (as long as you need).
        """
    ),
    llm=llm,
    allow_delegation=False
)