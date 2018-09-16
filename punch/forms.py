from django.forms import ModelForm
from punch.models import punch_model


class punch_in_form(ModelForm):
    class Meta:
        model = punch_model
        fields = []