from langchain_openai import AzureChatOpenAI
from constants import AZURE_API_VERSION

llms = {
    "azure-gpt-4o-mini": AzureChatOpenAI(
        azure_deployment="gpt-4o-mini", api_version=AZURE_API_VERSION, temperature=0.7
    ),
    "azure-gpt-4o": AzureChatOpenAI(
        azure_deployment="gpt-4o", api_version=AZURE_API_VERSION, temperature=0.7
    ),
}

topic = input("Give me a topic and I'll write a HAIKU for you: ")

messages = [
    ("system", "You are a haiku poet. Write a haiku on the topic given by user."),
    ("human", topic),
]

model_name = "azure-gpt-4o-mini"
poet = llms[model_name]
poem = poet.invoke(messages).content
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(poem)
