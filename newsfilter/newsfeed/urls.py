from django.urls import path
from newsfeed.views import (HomePageView, NewsFeedListing, ChangeVoteCount)

app_name = "news"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news', NewsFeedListing.as_view(), name='news-list'),
    path('change_vote_count', ChangeVoteCount.as_view(), name='change-vote-count'),
]
