from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404 , HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.views import generic

from .models import Question, Choice



def index(request):
     latest_question_list= Question.objects.order_by('-pub_date')[:2]
     for q in latest_question_list:
          print(q)
     context = {
          'latest_question_list': latest_question_list,
     }
     return render(request,'index.html',context)


def detail(request,question_id):
     question = get_object_or_404(Question, pk=question_id)
     return render(request,'detail.html',{"question":question})


def results(request,question_id):
     question = get_object_or_404(Question,pk = question_id)
     return render(request, 'result.html',{'question': question})


def vote(request,question_id):
     # return HttpResponse(f"you're voting on question {question_id}")
     question = get_object_or_404(Question, pk= question_id)
     try:
          selectes_choice =question.choice_set.get(pk= request.POST['choice'])
     except (KeyError, Choice.DoesNotExist):
          return render(request, ('detail.html'),{
               'question': question,
               'error_message': "your ar did selected choice"
          })
     else:
          selectes_choice.vote +=1
          selectes_choice.save()
          return HttpResponseRedirect(reverse('firstdjango:results',args=(question.id,)))

