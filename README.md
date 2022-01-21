# News Authenticity

News filter Check the authenticity of the same news what we receive & response to someone's request
to confirm authenticity.

# Prerequisites

- Python >= 3.6
- Celery >= 5.1
- Redis server must be installed
- Postgres database

# Run on local

- Create virtualenv : ```foo@bar:~$ virtualenv env```
- Install all requirements : ```pip install -r requirements.txt```
- Create .env file in same directory where manage.py is placed. Please add all enviorements variables in it which is listed below.
- Create Database of postgres.
- Run : ```Python manage.py migrate```
- Create superuser and other users to execute the code. Also add the preference of user to get notification.
- Please load the fixtures. You can also add more category from admin panel. : ```python manage.py loaddata newsfeed/fixtures/category.json```
- Runserver : ```Python manage.py runserver```
- Run celery to execute task periodically. - ```celery -A newsfilter.celery_config.celery_app worker --beat -l info```

# Features

- Fetch news from news api.
- Display news list on Website.
- User will receive the notification over the email for their preference category.
- User can set postive and negative vote to specific news.

# Future features

- Add authentication for users.
- Display news list based on the user preference.

# Project Work Flow

- There are 2 celery task.
    - news_api_org_task : This is periodical task which will execute in every 30 mins. It will fetch latest news from the news API and store into database.  
    - send_notification_email : This will send the email to user once system fetch new news. It will only send the notification to the user if system find new news in their preference.
- User can see list of news on home page and they can up vote and down vote the specific news.

# Environment Variables

- SECRET_KEY
- EMAIL_HOST
- EMAIL_PORT
- EMAIL_BACKEND
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- DB_ENGINE
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- REDIS_URL
- BROKER_URL
- SERVER
- CELERY_RESULT_BACKEND
- NEWS_API_ORG_API_KEY