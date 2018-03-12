# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import collections
from .forms import CreateInterview, EditInterview
from .models import Interview
from datetime import datetime
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    interviews = Interview.objects.order_by('-date', '-start_time')
    template = loader.get_template('dashboard/index.html')
    datewise = {}
    temp = []
    if (len(interviews)):
        cur = interviews[0]
        for i in interviews:
            if i.date == cur.date:
                temp.append(i)
            else:
                datewise[cur.date] = temp
                cur = i
                temp = []
                temp.append(i)
        datewise[cur.date] = temp
        datewise = collections.OrderedDict(sorted(datewise.items(), reverse=True))
    if (not('status' in request.session)):
    	request.session['status'] = 'Dashboard Online'
    context = {
        'interviews': datewise,
        'status': request.session['status'],
    }
    return HttpResponse(template.render(context, request))


def add(request):
    if (request.method == 'POST'):
        form = CreateInterview(request.POST)
        if (form.is_valid()):
            interviewer_email = form.cleaned_data['interviewer_email']
            for i in interviewer_email:
                print(i)
            candidate_email = form.fields['candidate_email']
            print('user')
            for i in candidate_email.choices:
                print(i[0],i[1])
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            date_ = form.cleaned_data['date']
            I = Interview(interviewer_email=interviewer_email, candidate_email=candidate_email, start_time=start_time, end_time=end_time, date=date_)
            I.save()
            request.session['status'] = "Interview Created Successfully"
            return redirect(reverse('dashboard:index'))
    else:
        form = CreateInterview()
    return render(request, 'dashboard/add.html', {'form': form})


def edit(request, id):
    if (request.method == 'POST'):
        form = EditInterview(request.POST)
        if (form.is_valid()):
            I = Interview.objects.get(id=id)
            I.interviewer_email = form.cleaned_data['interviewer_email']
            I.candidate_email = form.cleaned_data['candidate_email']
            I.start_time = form.cleaned_data['start_time']
            I.end_time = form.cleaned_data['end_time']
            I.date = form.cleaned_data['date']
            I.save()
            request.session['status'] = "Interview Edited Successfully"
            return redirect(reverse('dashboard:index'))
    return render(request, 'dashboard/add.html', {'form': form})


def choice(request, id):
    if (request.method == 'POST'):
        if ('Delete' in request.POST):
            I = Interview.objects.get(id=id)
            I.delete()
            request.session['status'] = "Interview Deleted Successfully"
            return redirect(reverse('dashboard:index'))
        else:
            I = Interview.objects.get(id=id)
            form = EditInterview(initial={'interviewer_email': I.interviewer_email, 'candidate_email':I.candidate_email, 'start_time': I.start_time, 'end_time': I.end_time, 'date': I.date})
    return render(request, 'dashboard/edit.html', {'form': form, 'Interview_Object': I})
