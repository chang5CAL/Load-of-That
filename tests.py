from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from api import views
import unittest
import json
import requests
from django.http import HttpRequest
from django.http import HttpResponse

# Create your tests here.
class APIResponseTest(unittest.TestCase):
	def test_Facebook(self):
		if(requests.get('http://localhost:8000/api/?city=seattle&type=coding&state=WA&country=US') != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			print("Test")
			self.assertTrue(False)
	def test_Meetup(self):
		if(requests.get('http://localhost:8000/api/meetup/?city=seattle&type=coding&state=WA&country=US') != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			self.assertTrue(False)
	def test_EventBrite(self):
		if(requests.get('http://localhost:8000/api/eventbrite_call/?city=seattle&type=event&state=WA&country=US') != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()