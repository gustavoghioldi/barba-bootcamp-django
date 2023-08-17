from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from polls.models import Question, Choice
from polls.forms import VoteForm
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

def detail_form(request):
    form = VoteForm(request.POST)
    context = {}
    context['form']= form
    return render(request, "polls/details_form.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # <-- es parecido Question.objects.get(pk=question_id) 
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {
                "question": question,
                "error_message": "You didn't select a choice.",
            }
        return render(request, "polls/details.html", context)

    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))