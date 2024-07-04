import os
import openai
from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool, ScrapeWebsiteTool
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv, find_dotenv
import pypandoc
import tempfile

FileReadTool = FileReadTool()
OpencriticSearchTool = ScrapeWebsiteTool(website_url='https://opencritic.com/')
search_tool = DuckDuckGoSearchRun()

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]


writer = Agent(
    role='Senior Game Journalist',
    goal='Summarised the best 5 games that were released in 2022 and why they were successful.',
    backstory="""You are a Senior Game Journalist at a leading game review website.
    To understand the latest trends in the gaming industry, you need to analyze the most successful games of last year. 
    You have a knack for dissecting complex game play ideas , deep understanding in video games, good experience in game understanding and presenting
    the game through good writing skills.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, OpencriticSearchTool]
)

task1 = Task(
    description="""Conduct a comprehensive analysis of the best games released in 2022.
    Identify key trends, breakthrough game play elements, and potential industry impacts from these games.
    Compile your findings in a detailed report regarding the best 5 games that were released in 2022 and why they were successful.
    OUTPUT IN A MARKDOWN FORMAT""",
    agent=writer,
    expected_output='''
    Title: [Title of the report]
    Content: [Summarised the best 5 games that were released in 2022 and why they were successful.]
    '''
)

save_output_task = Task(
    description='Save the summarized games news to markdown file',
    expected_output='File saved successfully',
    agent=writer,
    tools=[FileReadTool],
    output_file='outputs/output2.md',
    create_directory=True
)

crew = Crew(
  agents=[writer],
  tasks=[task1,save_output_task],
  verbose=2,
  process=Process.sequential
)

result = crew.kickoff()

print("#### USAGE ####")
print (crew.usage_metrics) 


def generate_report(md_text, output_file):
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as temp_md:
        temp_md.write(md_text.encode("utf-8"))
        temp_md_path = temp_md.name
        
    try:
        output = pypandoc.convert_file(temp_md_path, "pdf", outputfile=output_file)
        return "Success"
    
    finally:
        os.remove(temp_md_path)

print("######################")
print(result)
