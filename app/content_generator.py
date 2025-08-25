import random
import requests
from config.settings import PERPLEXITY_API_KEY

# # Load env vars
# load_dotenv()
# PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "YOUR_OPENAI_API_KEY")

topics = [
    "Latest AI tools",
    "AI thought leadership",
    "AI in healthcare",
    "AI in productivity",
    "AI ethics & future",
    "AI news update",
    "AI technology for developers",
]

def generate_post():
    topic = random.choice(topics)
    prompt = f"""Write a short, creative LinkedIn post on {topic}.
                keep it under 130 words.
                Add 3-5 relevant trending hashtags.
                Title should be 'AI thought of the day!'.
            """
    
    # Set up the API endpoint and headers
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    # Define the request payload
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "user", "content":prompt}
        ]
    }

    # Make the API call
    response = requests.post(url, headers=headers, json=payload)

    return response.json()["choices"][0]['message']['content'].strip()