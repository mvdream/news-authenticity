from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import reverse
from django.contrib.sites.models import Site


class SendEmailService:

    @classmethod
    def send_email(self, receiver_email, username, category):
        domain = Site.objects.get_current().domain
        newsfeed_url = f"{domain}{reverse('news:news-list')}"
        context = {'category': category,
                   "username": username, 'url': newsfeed_url}
        subject = 'NewsFeed'
        email_body = get_template('newsfeed/email_template.html').render(context)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver_email]
        mail = EmailMessage(subject, email_body, email_from, recipient_list)
        mail.content_subtype = "html"  # Main content is now text/html
        mail.send()
