import datetime

from django.test import TestCase
from django.utils import timezone

from django.urls import reverse
from .models import Question

# Create your tests here.

class QuestionMethodTest(TestCase):
	
	def test_was_published_recently_with_old_question(self):
		t=timezone.now()+datetime.timedelta(days=30)
		future_date=Question(pub_date=t)
		self.assertIs(future_date.was_published_recently(),False)

	def test_was_published_with_recent_question(self):
		t=timezone.now()-datetime.timedelta(hours=1)
		recent_date=Question(pub_date=t)
		self.assertIs(recent_date.was_published_recently(),True)
