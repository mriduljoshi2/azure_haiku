import os
import time
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, Tool, create_openai_tools_agent
from langchain_openai import AzureChatOpenAI
from langchain_core.tools import tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from constants import AZURE_API_VERSION

load_dotenv(".env")


@tool
def get_current_date():
    """Simple tool that returns the current date as a string."""
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d")


@tool
def reverse_string(text: str):
    """Simple tool that reverses a string."""
    return text[::-1]


# Set up the prompt template (basic example)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Initialize the AzureChatOpenAI model
model = AzureChatOpenAI(
    azure_deployment="gpt-4o", api_version=AZURE_API_VERSION, temperature=0
)

# Define the tools
tools = [
    get_current_date,
    reverse_string,
]

# Initialize the agent with the Azure model and tools
agent = create_openai_tools_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Test the agent by executing a simple query
queries = [
    "What is today's date?",
    "Reverse the string 'hello'",
    "Why did the chicken cross the road?",
]

for query in queries:
    start_time = time.time()
    response = agent_executor.invoke(
        {
            "input": f"""Use only the tools at your disposal to answer the query.
    If tools are insufficient to give an answer, respond with 'Insufficient info!'
    The query is - {query}"""
        }
    )
    time_taken = time.time() - start_time
    print(f"Query: {query}\nResponse: {response['output']}")
    print(f"Time taken: {time_taken} seconds")
