from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rangoapp.models import Category, Page, UserProfile
from rangoapp.forms import CategoryForm, PageForm, UserForm, UserProfileForm
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

def add_page(request, category_name_slug):
  try:
    cat = Category.objects.get(slug=category_name_slug)
  except Category.DoesNotExist:
    cat = None

  if request.method == 'POST':
    form = PageForm(request.POST)

    if form.is_valid():
      if cat:
        page = form.save(commit=False)
        page.category = cat
        page.views = 0
        page.save()
        return category(request, category_name_slug)
    else:
      print form.errors
  else:
    form = PageForm()

  data = {'form': form, 'category': cat}
  return render(request, 'rangoapp/add_page.html', data)

def register(request):
  registered = False

  if request.method == 'POST':
    user_form = UserForm(request.POST)
    profile_form = UserProfileForm(request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save(commit=False)

      user.set_password(user.password)
      user.save()

      profile = profile_form.save(commit=False)
      profile.user = user

      if 'picture' in request.FILES:
        profile.picture = request.FILES['picture']

      profile.save()
      registered = True
    else:
      print user_form.errors, profile_form.errors
  else:
    user_form = UserForm()
    profile_form = UserProfileForm()
  return render(request, 'rangoapp/register.html', {'user_form': user_form, 'profile_form': UserProfileForm, 'registered': registered})







