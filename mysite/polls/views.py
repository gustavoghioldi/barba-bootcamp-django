from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render

from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    #return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {
        "question": question
    }
    return render(request, "polls/details.html", context)


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")