from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.add, name='add'),
    url(r'^choice/(?P<id>[0-9]+)/$', views.choice, name='choice'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
]