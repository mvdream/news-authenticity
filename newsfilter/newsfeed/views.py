import json
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import JsonResponse
from newsfeed.models import NewsData


class HomePageView(TemplateView):
    template_name = 'newsfeed/base.html'


class NewsFeedListing(ListView):
    template_name = "newsfeed/news_list.html"
    model = NewsData
    paginate_by = 10
    context_object_name = 'news_list'
    ordering = '-positive_votes'


class ChangeVoteCount(View):

    def put(self, request):
        try:
            data = json.loads(request.body)
            vote_type = str(data.get('voteType'))
            news_id = data.get('newsId')
            if vote_type and news_id:
                news_obj = NewsData.objects.filter(pk=news_id).first()
                if int(vote_type) == 0:
                    news_obj.negative_votes += 1
                elif int(vote_type) == 1:
                    news_obj.positive_votes += 1
                news_obj.save()
                resp = {'success': 'vote done.'}
            return JsonResponse(resp, status=200)
        except Exception as e:
            print('Exception in add comment view', str(e))
