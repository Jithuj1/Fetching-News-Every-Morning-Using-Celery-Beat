import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryBeat.settings')

app = Celery('CeleryBeat')

app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery Beat
app.conf.beat_schedule ={
    'print-hello':{
        'task':'mainapp.tasks.SaveDailyNews',
        'schedule':crontab(hour=3)
    }
}

app.autodiscover_tasks()

app.conf.timezone = 'UTC'