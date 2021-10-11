from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text: models.CharField = models.CharField(max_length=200, null=False)


class Answer(models.Model):
    text: models.CharField = models.CharField(max_length=200, null=False)
    question: models.ForeignKey = models.ForeignKey(Question, models.CASCADE, related_name="answers")
    is_correct: models.BooleanField = models.BooleanField(null=False)


class UserQuestion(models.Model):
    question: models.ForeignKey = models.ForeignKey(Question, models.CASCADE)
    answer: models.ForeignKey = models.ForeignKey(Answer, models.CASCADE)
    user: models.ForeignKey = models.ForeignKey(User, models.RESTRICT)

    class Meta:
        unique_together: tuple = 'user', 'question', 'answer'
