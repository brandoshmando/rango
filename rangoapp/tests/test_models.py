import unittest
from django.test import TestCase
from rangoapp.models import Category
from rangoapp.tests.factories import CategoryFactory

class CategoryTests(TestCase):

  def test_views_default_zero(self):
    category = CategoryFactory.create()

    self.assertEqual(category.views, 0)

  def test_likes_default_zero(self):
    category = CategoryFactory.create()

    self.assertEqual(category.likes, 0)

  def test_create_category(self):
    category = CategoryFactory.create()

    self.assertTrue(isinstance(category, Category))