from django.shortcuts import render
from django.http import  HttpResponse
from .models import Question
# Create your views here.

def index(request):
    last_question_list=Question.objects.order_by('-pub_date')[:5]
    output=','.join([q.question_text for  q in last_question_list])
    return HttpResponse(output)



def detail(request,question_id):
    return HttpResponse("You looking at question %s" % question_id)

def results(request,question_id):
    response="You looking at results of %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You voting on question %s " % question_id)



