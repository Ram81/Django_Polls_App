from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404

from .models import Question
from django.template import loader

# Create your views here.
def index(request):
	list_question=Question.objects.order_by('-pub_date')[:5]
#	template=loader.get_template('polls/index.html')
	context={
		'list_question':list_question,
	}
#	return HttpResponse(template.render(context,request))
	return render(request,'polls/index.html',context)

def detail(request,question_id):
#	try:
#		q=Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question You are looking for doesn't exists!")

	q=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{ 'question':q })

def results(request,question_id):
	message="You are Looking for %s."
	return HttpResponse(message % question_id)

def vote(request,question_id):
	return HttpResponse("<h2> Votes for Question %s. </h2>"% question_id)
