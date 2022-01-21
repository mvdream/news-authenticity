import logging
from newsfilter import celery_app
from newsfeed.services.new_api_org import NewApiOrgData
from celery import Task
from celery.schedules import crontab


celery_app.conf.beat_schedule.update(
    {
        "run-every-30mins": {
            "task": "news_api_org_task",
            "schedule": crontab(minute='*/1'),
        }
    }
)
logger = logging.getLogger("newsfilter")


class NewsApiOrgTask(Task):

    name = "news_api_org_task"

    def run(self):
        try:
            obj = NewApiOrgData()
            obj.fetch_api_data()
            obj.save_data_to_database()
        except Exception as e:
            logger.error(
                dict(
                    message="Exception in shcedule reminder send mail task",
                    class_name="NewsApiOrgTask",
                    errors=e,
                )
            )


news_api_org_task = celery_app.register_task(NewsApiOrgTask())
