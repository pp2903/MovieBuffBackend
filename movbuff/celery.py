import os
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movbuff.settings")

app = Celery("movbuff")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    
    "send-favorites-in-mail": {
        "task": "baseapp.tasks.generate_and_send_pdf",
        "schedule": 10,
        # 'schedule':crontab(hour=20,minute=30,day_of_week=5),
    },
}
