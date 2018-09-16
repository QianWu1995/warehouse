from django.db import models

# Create your models here.


class product_model(models.Model):
    ##kitid = models.CharField(max_length = 100)
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    size = models.CharField(max_length = 100)
    style = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)
    number_in_stock = models.IntegerField(default= 1)

    def __str__(self):
        return self.name
##class kit(models.Model):
