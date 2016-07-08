from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from api import views
import unittest

# Create your tests here.
class APIResponseTest(unittest.TestCase):
	def test_Facebook(self):
		if(views.index("city=seattle&type=coding&state=WA&country=US") != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			self.assertTrue(False)
	def test_Meetup(self):
		if(views.Meetup("city=seattle&type=coding&state=WA&country=US") != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			self.assertTrue(False)
	def test_EventBrite(self):
		if(views.EventBrite_Call("city=seattle&type=coding&state=WA&country=US") != HttpResponse(status=404)):
			self.assertTrue(True)
		else:
			self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()