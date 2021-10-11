from rest_framework import serializers
from .models import Answer, Question, UserQuestion
from .services import create_answers, update_answers


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model: UserQuestion = UserQuestion
        fields: tuple = 'question', 'answer', 'user'


class AnswerSerializer(serializers.ModelSerializer):
    id: serializers.IntegerField = serializers.IntegerField(read_only=True)
    text: serializers.CharField = serializers.CharField(max_length=200)
    is_correct: serializers.BooleanField = serializers.BooleanField()

    class Meta:
        model: Answer = Answer
        fields: tuple = 'id', 'text', 'is_correct'


class QuizSerializer(serializers.ModelSerializer):
    id: serializers.IntegerField = serializers.IntegerField(read_only=True)
    answers: AnswerSerializer = AnswerSerializer(many=True)
    text: serializers.CharField = serializers.CharField(max_length=200)

    def create(self, validated_data: dict):
        answers: list = validated_data.pop('answers')
        question: Question = Question.objects.create(**validated_data)
        create_answers(answers, question)

        return question

    def update(self, instance: Question, validated_data: dict) -> Question:
        instance.text = validated_data.get('text')
        answers: list = validated_data.pop('answers')
        instance.save()
        update_answers(answers, instance)

        return instance

    class Meta:
        model: Question = Question
        fields: tuple = 'id', 'text', 'answers'
