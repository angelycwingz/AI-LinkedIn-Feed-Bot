import requests
import json
from config.settings import LINKEDIN_ACCESS_TOKEN,LINKEDIN_USER_ID

API_BASE_URL = "https://api.linkedin.com/v2"

def get_person_urn_from_sub():
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}", "LinkedIn-Version": "202505"}
    resp = requests.get(f"{API_BASE_URL}/userinfo", headers=headers)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch userinfo: {resp.status_code} {resp.text}")
    sub = resp.json().get("sub")
    if not sub:
        raise Exception("No 'sub' in userinfo response")
    return f"urn:li:person:{sub}"


def post_to_linkedin(content: str):

    """Post content to LinkedIn using dynamic numeric URN"""
    member_urn = get_person_urn_from_sub()

    """Post generated content to LinkedIn feed"""
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }

    payload = {
        "author": member_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code in (200, 201):
        print("✅ Posted successfully on LinkedIn!", response.json().get("id"))
    else:
        print(f"❌ Failed: {response.status_code} {response.text}")