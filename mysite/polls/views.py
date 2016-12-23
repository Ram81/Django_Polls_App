from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect

from .models import Question,choice
from django.template import loader
from django.urls import reverse

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
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{ 'question' :question})


def vote(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		select_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,choice.DoesNotExists):
		return render(request,'polls/detail.html',{
			'question':question,
			'error_message':"You Didn't Select a Choice",
		})

	else:
		select_choice.votes+=1;
		select_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))























