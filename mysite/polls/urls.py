from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),

# modifying urls for index.html links to detail page to some other using {% url 'detail' l.id %}
#	url(r'^specifics/(?P<question_id>[0-9]+)/$',views.detail,name='detail'),

	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]

