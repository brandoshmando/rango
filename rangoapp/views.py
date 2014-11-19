from django.shortcuts import render
from django.http import HttpResponse
from rangoapp.models import Category, Page
from rangoapp.forms import CategoryForm, PageForm
from IPython import embed

def index(request):
  top_data = {}

  categories = Category.objects.order_by('-likes')[:5]
  top_data['categories'] = categories

  pages = Page.objects.order_by('-views')[:5]
  top_data['pages'] = pages

  return render(request, 'rangoapp/index.html', top_data )

def about(request):
  about_vars = {'boldmessage': 'AHHHHHH'}
  return render(request, 'rangoapp/about.html', about_vars)

def category(request, category_name_slug):
  category_data = {}

  try:
    category = Category.objects.get(slug=category_name_slug)
    category_data['category_name'] = category.name

    pages = Page.objects.filter(category=category)
    category_data['pages'] = pages

    category_data['category'] = category

  except Category.DoesNotExist:
    pass

  return render(request, 'rangoapp/category.html', category_data)

def add_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return index(request)

    else:
      print form.errors
  else:
    form = CategoryForm()

  return render(request, 'rangoapp/add_category.html', {'form':form})

def add_page(request):
  if request.method == 'POST':
    form = PageForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else:
      print form.errors
    else:
      form = PageForm()

  return render(request, 'rangoapp/add_page.html', {'form':form})





