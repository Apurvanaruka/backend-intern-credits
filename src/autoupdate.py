from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from datetime import datetime
from models import Credit
from utils import get_db

def add_daily_credits():
    print(f"Running daily Credit update: {datetime.utcnow()} UTC")

    db: Session = next(get_db())
    try:
        credits = db.query(Credit).all()
        for credit in credits:
            credit.credits += 5
            credit.last_updated = datetime.utcnow()
        db.commit()
        print("Daily credits added to all User")
    except Exception as e:
        db.rollback()
        print("Failed to update Credits:", e)
    finally:
        db.close()


def start_scheduler():
    scheduler = BackgroundScheduler(timezone="UTC")
    scheduler.add_job(add_daily_credits, trigger="cron", hour=0, minute=0)
    scheduler.start()
    print("Scheduler started: Adds 5 Credits daily at 00:00 UTC Mid night")
