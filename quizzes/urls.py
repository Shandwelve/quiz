from . import views
from django.urls import path

from .views import ListCreateApiQuiz, RetrieveUpdateDeleteApiQuiz, CreateUserAnswer

urlpatterns = [
    path('', ListCreateApiQuiz.as_view()),
    path('<int:question_id>', RetrieveUpdateDeleteApiQuiz.as_view()),
    path('add_answer', CreateUserAnswer.as_view())
]
