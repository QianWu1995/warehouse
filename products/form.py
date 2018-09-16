from django.db import  models
from django.forms import ModelForm
from products.models import product_model
from history.models import histoy_model
from django.core.exceptions import NON_FIELD_ERRORS

class add_product_form(ModelForm):
    class Meta:
        model = product_model
        fields = ['name', 'size', 'style','color','number_in_stock']


class import_export_form(ModelForm):
    class Meta:
        model = histoy_model
        fields = ['product', 'number']