import os
from dotenv import load_dotenv

load_dotenv()      # reads .env into environment

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "YOUR_PERPLEXITY_API_KEY")
LINKEDIN_USER_ID = os.getenv("LINKEDIN_USER_ID", "YOUR_LINKEDIN_USER_ID")
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN", "YOUR_LINKEDIN_ACCESS_TOKEN")