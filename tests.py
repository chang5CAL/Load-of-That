from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
import unittest

# Create your tests here.
class APIResponseTest(unittest.TestCase):
	def test_NOT(self):
		self.assertFalse(False)
	def test(self):
		self.assertTrue(True)
	def testagain(self):
		self.assertTrue(True)
	def testNew(self):
		self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()