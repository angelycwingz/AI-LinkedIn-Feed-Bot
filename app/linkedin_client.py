import requests
import json
from config.settings import LINKEDIN_ACCESS_TOKEN,LINKEDIN_USER_ID

def post_to_linkedin(content: str):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    payload = {
        "author": f"urn:li:person:{LINKEDIN_USER_ID}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code in (200, 201):
        print("✅ Posted successfully on LinkedIn!", response.json().get("id"))
    else:
        print(f"❌ Failed: {response.status_code} {response.text}")