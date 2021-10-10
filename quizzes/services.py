from quizzes.models import Question, Answer


def create_answers(answers: list, question: Question) -> None:
    for answer in answers:
        Answer.objects.create(question=question, **answer)


def update_answers(answers: list, question: Question) -> None:
    question.answers.all().delete()
    create_answers(answers, question)
