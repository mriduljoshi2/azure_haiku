import os

from dotenv import load_dotenv

load_dotenv(".env")

AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "")
api_key = os.getenv("AZURE_OPENAI_API_KEY", "")
deployment_name = "your-deployment-name"
openai_api_base = os.getenv("AZURE_OPENAI_ENDPOINT", "")
