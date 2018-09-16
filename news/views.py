from django.shortcuts import render
from .models import news_model
from news.forms import add_news_form


def news_home(request):
    all_news = news_model.objects.all()
    return render(request, 'news.html',{'all_news':all_news})


def add_news(request):
    if request.method == "POST":
        form = add_news_form(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.name = form.cleaned_data['name']
            news.size = form.cleaned_data['content']
            news.date = form.cleaned_data['date']

            news.save()

            return render(request, 'add_news.html', {'form': form})
    else:
        form = add_news_form()
    return render(request, 'add_news.html', {'form': form})