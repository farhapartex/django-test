from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass
