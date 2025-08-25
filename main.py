#from app.scheduler import start_scheduler
from app.content_generator import generate_post
from app.linkedin_client import post_to_linkedin

if __name__ == "__main__":
    #start_scheduler() For local scheduling

    # For production
    content = generate_post()
    post_to_linkedin(content)