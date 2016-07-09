from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from api import views
import unittest
import json
from django.http import HttpRequest

# Create your tests here.
class APIResponseTest(unittest.TestCase):
	def test_Facebook(self):
		req = HttpRequest("city=seattle&type=coding&state=WA&country=US")
		if(views.index(req) != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			print("Test")
			self.assertTrue(False)
	def test_Meetup(self):
		req = HttpResponse("city" : "seattle", "type" : "coding", "state" : "WA", "country":"US")
		if(views.meetup(jsreqonObj) != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			self.assertTrue(False)
	def test_EventBrite(self):
		req = HttpRequest("city=seattle&type=coding&state=WA&country=US")
		if(views.eventbrite_call(req) != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()