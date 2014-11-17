from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("<a href='/rangoapp/about'>About</a>")

def about(request):
  return HttpResponse("<a href='/rangoapp'>Index</a>")
