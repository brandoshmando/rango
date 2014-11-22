from django import template
from rangoapp.models import Category

register = template.Library()

@register.inclusion_tag('rangoapp/cats.html')
def get_category_list():
  return { 'cats' : Category.objects.all() }