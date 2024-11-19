import os

from dotenv import load_dotenv

load_dotenv(".env")

AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "")
