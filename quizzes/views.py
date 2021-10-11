from pprint import pprint

from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import QuizSerializer, UserAnswerSerializer
from .models import Question


class ListCreateApiQuiz(APIView):
    permission_classes: tuple = IsAuthenticated,

    def get(self, request: Request) -> JsonResponse:
        serializer: QuizSerializer = QuizSerializer(Question.objects.all(), many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request: Request) -> JsonResponse:
        serializer: QuizSerializer = QuizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(data=serializer.data, status=201, safe=False)


class RetrieveUpdateDeleteApiQuiz(APIView):
    permission_classes: tuple = IsAuthenticated,

    def put(self, request: Request, question_id: int):
        question: Question = Question.objects.get(pk=question_id)
        serializer: QuizSerializer = QuizSerializer(question, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(data=serializer.data, status=202, safe=False)

    def get(self, request: Request, question_id: int) -> JsonResponse:
        question: Question = Question.objects.get(pk=question_id)
        serializer: QuizSerializer = QuizSerializer(question)

        return JsonResponse(serializer.data, safe=False)

    def delete(self, request: Request, question_id: int) -> JsonResponse:
        Question.objects.get(pk=question_id).delete()

        return JsonResponse(True, safe=False, status=204)


class CreateUserAnswer(APIView):
    permission_classes: tuple = IsAuthenticated,

    def post(self, request: Request) -> JsonResponse:
        request.data['user'] = request.user.id
        serializer: UserAnswerSerializer = UserAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(serializer.data)
