# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Interview(models.Model):
	interviewer_email = models.EmailField(max_length=200)
	candidate_email = models.EmailField(max_length=200)
	start_time = models.TimeField('Interview start time')
	end_time = models.TimeField('Interview end time')
	date = models.DateField('Interview Date')

	def __str__(self):
		return self.interviewer_email

	def get_start_time(self):
		return self.start_time.strftime('%H:%M:%S')

	def get_end_time(self):
		return self.end_time.strftime('%H:%M:%S')
