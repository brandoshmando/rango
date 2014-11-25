import unittest
from django.test import TestCase
from rangoapp.tests.factories import CategoryFactory, PageFactory
from django.core.urlresolvers import reverse

class ViewTests(TestCase):
  pass
  def test_index_view(self):
    category = CategoryFactory.create()
    category.save()

    page = PageFactory.build(category=category)
    page.save()

    url = reverse("rangoapp.views.index")
    response = self.client.get(url)

    self.assertEqual(response.status_code, 200)
    self.assertIn(category.name, response.content)
    self.assertIn(page.title, response.content)
