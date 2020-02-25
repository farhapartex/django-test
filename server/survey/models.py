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

    def __str__(self):
        return self.text


ANSWER_CHOICE = (('yes','Yes'),('no','No'))
class Exam(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), related_name="exams", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name=_("Question"), related_name="qexams", on_delete=models.CASCADE)
    answer = models.CharField(_("Answer"),choices=ANSWER_CHOICE, max_length=10)