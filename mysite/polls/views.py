from django.http import HttpResponse
from django.template import loader

from polls.models import Question, Choice

def index(request):

    template = loader.get_template("polls/index.html")
    context = {"nombres": ["juan", "pedro", "arturo"],
               "choices": Choice.objects.all()
               }
    return HttpResponse(template.render(context, request))

def choices(request):
    choices = Choice.objects.all()
    choices_list = []
    for choice in choices:
        choices_list.append({
            "question": choice.question.question_text,
            "choice_text":choice.choice_text,
            "votes": choice.votes
        })

    return HttpResponse(choices_list)


def questions(request):
    questions = Question.objects.all()
    questions_list = []
    for question in questions:
        questions_list.append({
            "question": question.question_text,
            "pub_date":str(question.pub_date)
        })

    return HttpResponse(questions_list)