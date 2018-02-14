from django.shortcuts import render
from django.http import HttpResponse

from time import strftime

def index(request):
	return HttpResponse("<h1>Hello, Django World!</h1><p>Right now it is " + strftime('%c') + "</p>")
