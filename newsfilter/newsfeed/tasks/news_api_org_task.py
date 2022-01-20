from newsfilter import celery_app
from newsfeed.services.new_api_org import NewApiOrgData
from celery import Task
from datetime import timedelta
from celery.schedules import crontab


celery_app.conf.beat_schedule.update(
    {
        "run-every-30mins": {
            "task": "news_api_org_task",
            "schedule": crontab(minute='*/1'),
        }
    }
)


class NewsApiOrgTask(Task):

    name = "news_api_org_task"

    def run(self):
        try:
            obj = NewApiOrgData()
            obj.fetch_api_data()
            obj.save_data_to_database()
        except Exception as e:
            print("Exception in shcedule reminder send mail task", str(e))


news_api_org_task = celery_app.register_task(NewsApiOrgTask())
