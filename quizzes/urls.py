from . import views
from django.urls import path

from .views import ListCreateApiQuiz, RetrieveUpdateDeleteApiQuiz

urlpatterns = [
    path('z', ListCreateApiQuiz.as_view()),
    path('<int:question_id>', RetrieveUpdateDeleteApiQuiz.as_view())
]
