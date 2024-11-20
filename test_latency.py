import time
from langchain_openai import AzureChatOpenAI
from constants import AZURE_API_VERSION


# Initialize the model
model = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini", api_version=AZURE_API_VERSION, temperature=0
)


def test_azure_api_latency():
    """Test direct API latency without LangChain agent overhead"""

    test_messages = [
        "What is 2+2?",
        "Tell me a short joke",
        "What's the capital of France?",
    ]

    print("Testing direct Azure API latency...\n")

    for message in test_messages:
        print(f"Query: {message}")

        # Time the API call
        start_time = time.time()
        try:
            response = model.invoke(message)
            api_time = time.time() - start_time
            print(f"Response: {response.content}")
            print(f"API Response Time: {api_time:.2f} seconds")
        except Exception as e:
            print(f"Error: {str(e)}")
        print("-" * 50)


if __name__ == "__main__":
    test_azure_api_latency()
