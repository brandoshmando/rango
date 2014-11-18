from django.shortcuts import render
from django.http import HttpResponse
from rangoapp.models import Category
def index(request):
  top_categories = Category.objects.order_by('-likes')[:5]
  return render(request, 'rangoapp/index.html', { 'categories': top_categories} )
def about(request):
  about_vars = {'boldmessage': 'AHHHHHH'}
  return render(request, 'rangoapp/about.html', about_vars)
