import logging
from celery import Task
from newsfilter import celery_app
from newsfeed.models import (
    User
)
from newsfeed.services import SendEmailService

logger = logging.getLogger("newsfilter")


class SendNotificationEmail(Task):

    name = "send_notification_email"

    def run(self, category):
        try:
            user_profiles = User.objects.filter(preferences__isnull=False)
            users = user_profiles.filter(preferences__name=category)
            for user in users:
                if user.email:
                    SendEmailService.send_email(user.email, user.username, category)
        except Exception as e:
            logger.error(
                dict(
                    message="error while send notification email ",
                    class_name="SendNotificationEmail",
                    errors=e,
                )
            )


send_notification_email = celery_app.register_task(SendNotificationEmail())
