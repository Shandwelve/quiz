from django.db import models


class Question(models.Model):
    text: models.CharField = models.CharField(max_length=200, null=False)


class Answer(models.Model):
    text: models.CharField = models.CharField(max_length=200, null=False)
    question: models.ForeignKey = models.ForeignKey(Question, models.CASCADE, related_name="answers")
    is_correct: models.BooleanField = models.BooleanField(null=False)


class UserQuestion(models.Model):
    question: models.BooleanField = models.ForeignKey(Question, models.CASCADE)
    answer: models.BooleanField = models.ForeignKey(Answer, models.CASCADE)
