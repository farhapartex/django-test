from django.shortcuts import render
from rest_framework import generics, viewsets,mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import *
# Create your views here.


class QuestionViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnly,
    ]

class ExamViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Exam.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)