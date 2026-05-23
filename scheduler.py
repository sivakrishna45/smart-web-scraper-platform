import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from datetime import datetime
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import main as run_scraper

# Create logs directory
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("logs/scheduler.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Scheduler")

def scheduled_job():
    start_time = time.time()

    print(f"\n{'═' * 80}")
    print(f"🕒 Scheduled Scrape Started - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'═' * 80}\n")

    try:
        run_scraper()

        duration = round(time.time() - start_time, 2)

        logger.info(f"✅ Scheduled job completed successfully")
        logger.info(f"⏱ Duration: {duration} seconds")

    except Exception as e:
        logger.error(f"❌ Scheduled job failed: {e}", exc_info=True)

def job_listener(event):
    if event.exception:
        logger.error("❌ Job crashed")
    else:
        logger.info("✅ Job executed successfully")

if __name__ == "__main__":

    jobstores = {
        'default': SQLAlchemyJobStore(
            url='sqlite:///data/jobs.db'
        )
    }

    executors = {
        'default': ThreadPoolExecutor(5)
    }

    job_defaults = {
        'coalesce': False,
        'max_instances': 1,
        'misfire_grace_time': 300
    }

    scheduler = BlockingScheduler(
        jobstores=jobstores,
        executors=executors,
        job_defaults=job_defaults,
        timezone="US/Central"
    )

    scheduler.add_listener(
        job_listener,
        EVENT_JOB_EXECUTED | EVENT_JOB_ERROR
    )

    scheduler.add_job(
        scheduled_job,
        trigger='cron',
        hour=8,
        minute=0,
        id='daily_web_scrape',
        name='Daily Smart Scraper Job',
        replace_existing=True
    )

    print("🚀 Smart Web Scraper Scheduler Started")
    print("⏰ Runs daily at 8:00 AM CST")
    print("📁 Logs: logs/scheduler.log")
    print("🗄 Persistent Jobs DB: data/jobs.db")
    print("Press Ctrl + C to stop\n")

    # Optional immediate first run
    scheduled_job()

    scheduler.start()