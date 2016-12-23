from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
from django.template import loader

# Create your views here.
def index(request):
	list_question=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={
		'list_question':list_question,
	}
	return HttpResponse(template.render(context,request))

def detail(request,question_id):
	return HttpResponse("<h2> You are Looking at Question %s.</h2>"% question_id)

def results(request,question_id):
	message="You are Looking for %s."
	return HttpResponse(message % question_id)

def vote(request,question_id):
	return HttpResponse("<h2> Votes for Question %s. </h2>"% question_id)
