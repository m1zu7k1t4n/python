from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. you're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question {0}".format(question_id))


def results(request, question_id):
    response = "you're looking at the results of question {0}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("you're voting on question {0}".format(question_id))
