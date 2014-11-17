from django.shortcuts import render

def index(request):
  return HttpResponse("Rango says hey there world...")
