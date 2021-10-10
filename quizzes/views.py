from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.views import APIView

from .serializers import QuizSerializer
from .models import Question


class ListCreateApiQuiz(APIView):
    parser_classes: tuple = JSONParser,

    def get(self, request: Request) -> JsonResponse:
        serializer: QuizSerializer = QuizSerializer(Question.objects.all(), many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request: Request) -> JsonResponse:
        serializer: QuizSerializer = QuizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(data=serializer.data, status=201, safe=False)


class RetrieveUpdateDeleteApiQuiz(APIView):
    parser_classes: tuple = JSONParser,

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
