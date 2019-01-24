from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says the about page is <a href=/rango/about/>here </a>")

def about(request):
	return HttpResponse("Rango says here is the about page, and the main page is <a href=/rango/> here </a>")
