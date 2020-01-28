
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    # ex: /polls/
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # ex: /polls/5/
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    # ex: /polls/5/results/
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    # ex: /polls/5/vote/
    return HttpResponse(f"You're voting on question {question_id}.")