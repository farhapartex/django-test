from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
# Create your models here.


ANSWER_CHOICE = ((True,'Yes'),(False,'No')) 
class Question(models.Model):
    name = models.CharField(_("Name"), max_length=250)

    def __str__(self):
        return self.name

class Survey(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"),related_name="survies", on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, verbose_name=_("Questions"))

    def __str__(self):
        return self.user.username