from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class punch_model(models.Model):
    id = models.AutoField(primary_key = True)
    time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)