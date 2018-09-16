from django.db import  models
from django.forms import ModelForm
from news.models import news_model
from django.core.exceptions import NON_FIELD_ERRORS


class add_news_form(ModelForm):
    class Meta:
        model = news_model
        fields = ['name', 'content', 'date']