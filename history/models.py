from django.db import models
from products.models import product_model

# Create your models here.


class histoy_model(models.Model):
    product = models.ForeignKey(product_model, on_delete=models.CASCADE)
    number = models.IntegerField()
    time = models.DateTimeField()
    current_number_in_stock = models.IntegerField()
