from django.db import models
# Create your models here.
class Addgoal(models.Model):
    gname = models.CharField(max_length=50)
    desc = models.TextField()

