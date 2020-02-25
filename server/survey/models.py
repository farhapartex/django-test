from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    survey = models.ForeignKey(Survey, verbose_name=_("Survey"),related_name="questions", on_delete=models.CASCADE)
    text = models.TextField()