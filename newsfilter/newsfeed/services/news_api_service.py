from abc import ABC, abstractmethod
from newsfeed.models import NewsData, Category


class ApiUtility(ABC):

    news_data = []

    def __init__(self):
        self.categories = list(
            Category.objects.all().values_list('name', flat=True))

    @abstractmethod
    def fetch_api_data(self):
        pass

    def save_data_to_database(self):
        try:
            for data in self.news_data:
                news_list = list(data.values())[0]
                newsfeeds = [
                    NewsData(title=news.get('title'),
                             url=news.get('url'),
                             content=news.get('content'),
                             category=news.get('category'))
                    for news in news_list if NewsData.objects.filter(url=news.get('url')).count() == 0
                ]
                NewsData.objects.bulk_create(newsfeeds)
        except Exception as e:
            print("Exception to save_data_to_database : ", str(e))
