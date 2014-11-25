import factory
import random
from faker import Factory as FakerFactory
from rangoapp.models import Category, Page, UserProfile

faker = FakerFactory.create()

class CategoryFactory(factory.Factory):
  FACTORY_FOR = Category

  name = faker.company()

class PageFactory(factory.Factory):
  FACTORY_FOR = Page

  category = CategoryFactory.create()
  title = fake.company()
  url = "http://www.example.com"






