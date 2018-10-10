from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

from .models import Question, Choice

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:2]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request,'polls/index.html',context)


def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    # return HttpResponse(f'Your Looking at question {question_id}')


def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html', {'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':'You didnt select a choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
