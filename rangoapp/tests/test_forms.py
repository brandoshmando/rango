import unittest
from django.test import TestCase
from rangoapp.forms import CategoryForm, PageForm
from faker import Factory as FakerFactory
from rangoapp.tests.factories import CategoryFactory, PageFactory
from IPython import embed

faker = FakerFactory.create()

class CategoryFormTests(TestCase):
  def test_valid_form(self):
    category = CategoryFactory.create()
    data = {'name': category.name, 'likes':category.likes, 'views':category.views}
    form = CategoryForm(data=data)
    self.assertTrue(form.is_valid())