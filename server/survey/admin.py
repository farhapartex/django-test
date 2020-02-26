from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey','text',)

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass
