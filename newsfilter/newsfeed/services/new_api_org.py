import requests
from datetime import datetime
from newsfeed.services.news_api_service import ApiUtility
from newsfeed.constants import NewsApiConstants
from newsfeed.models import Category
from newsfeed.tasks.send_notification_task import send_notification_email


class NewApiOrgData(ApiUtility):

    def fetch_api_data(self):
        try:
            categories = self.categories
            url = NewsApiConstants.NEWS_API_ORG_URL
            today = datetime.today().date().strftime("%Y-%m-%d")
            params = {"from": today,
                      "sort_by": "popularity",
                      "apikey": NewsApiConstants.NEWS_API_ORG_API_KEY}

            for category in categories:
                category_obj = Category.objects.filter(name=category).first()
                param = params.copy()
                param.update({"q": category})
                resp = requests.get(url, param)
                json_resp = resp.json()
                if json_resp.get('status').lower() == "ok":
                    articles = json_resp.get('articles')
                    article_data = [{"category": category_obj, "title": article.get('title', ''), "content": article.get(
                        'content', ''), "url": article.get('url', '')} for article in articles]
                    self.news_data.append({category_obj.name: article_data})
                    if articles:
                        send_notification_email.delay(category)
                else:
                    print("Error response for url : {}, category : {}, response : {}".format(
                        url, category, json_resp))

        except Exception as e:
            print("Exception in NewsAPIOrgData method", str(e))
