from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from polls.models import Question, Choice

def index(request):
    return HttpResponse('Hello, this is polls index')

def question(request, question_id):
    try:
        q = Question.objects.get(id=int(question_id))
        # c_list = q.choice_set.all()
    except Exception as e:
        return HttpResponse('Question[%s] Error! ...%s' %(question_id, str(e)))
    else:
        return HttpResponse(q)

def question_detail(request, question_id):
    try:
        q = Question.objects.get(id=int(question_id))
        c_list = q.choice_set.all()
        s= str(q)
        for c in c_list:
            s =  s+ '<br>%s</br>' %(c)
    except Exception as e:
        return HttpResponse('Question[%s] Error! ...%s' %(question_id, str(e)))
    else:
        return HttpResponse(s)

def all_question(request):
    q_list = Question.objects.all()
    return HttpResponse(q_list)


def all_choice(request):
    c_list = Choice.objects.all()
    return HttpResponse(c_list)




