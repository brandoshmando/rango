from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  template_var = {'boldmessage':'AHHHHHHHH'}
  return render(request, 'rangoapp/index.html', template_var)
def about(request):
  return HttpResponse("<a href='/rangoapp'>Index</a>")
