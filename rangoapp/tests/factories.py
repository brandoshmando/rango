import factory
import random
from faker import Factory as FakerFactory
from rangoapp.models import Category, Page, UserProfile

faker = FakerFactory

class CategoryFactory(factory.Factory):
  FACTORY_FOR = Category

  name = faker.company()
  likes = random.randrange(10,50)
  views = random.randrange(10,50)
