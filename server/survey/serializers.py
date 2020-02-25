import logging
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    survey = SurveySerializer(read_only=True)
    survey_id = serializers.PrimaryKeyRelatedField(
        source="survey",
        queryset=Survey.objects.all(),
        write_only=True,
    )
    class Meta:
        model = Question
        fields = ("id","survey","survey_id","text")


class ExamSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    question_id = serializers.PrimaryKeyRelatedField(
        source="question",
        queryset=Question.objects.all(),
        write_only=True,
    )

    def get_question(self, model):
        return model.question.text

    class Meta:
        model = Exam
        fields = ("id","question","question_id","answer","user")
        extra_kwargs = {
            'user': {'read_only': True},
        }