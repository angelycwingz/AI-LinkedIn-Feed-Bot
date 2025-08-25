from apscheduler.schedulers.blocking import BlockingScheduler
from app.content_generator import generate_post
from app.linkedin_client import post_to_linkedin
import datetime

def job():
    print(f"Running job at {datetime.datetime.now()}")
    content = generate_post()
    post_to_linkedin(content)

def start_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(func=job, trigger='cron', hour=20, minute=38) # Runs daily at 11:00 AM
    print("Scheduler started... waiting for 11 AM.")
    scheduler.start()