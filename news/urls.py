
from django.urls import path, re_path
from news.views import news_home,add_news



urlpatterns = [
    path('', news_home),

    path('add', add_news)
]