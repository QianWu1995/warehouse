from django.shortcuts import render

from django.apps import apps
# Create your views here.

news_model = apps.get_model('news', 'news_model')


def home(request):
    all_news = news_model.objects.all()
    return render(request, 'home.html', {'all_news': all_news})