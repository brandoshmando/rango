import unittest
from django.test import TestCase
from rangoapp.models import Category
from rangoapp.tests.factories import CategoryFactory

class CategoryTests(TestCase):

  def test_views_default_zero(self):
    category = CategoryFactory.create()

    self.assertEqual(category.views, 0)
