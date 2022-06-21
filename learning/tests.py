from django.test import TestCase
from django.contrib.auth.models import User
from .models import Language, Group, Message

# Create your tests here.
class LanguageTestClass(TestCase):
    def setUp(self):
        self.new_language = Language(name="Lyons")
        self.new_language.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_language, Language))

class GroupTestCase(TestCase):
    pass