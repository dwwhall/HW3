from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Blog Home</h1>')

def personalweb(request):
	return HttpResponse("<title>Dwight's website</title><br></br><br></br><center><h1>This is Dwight's Page</h1></center>")

