from django.shortcuts import render
from django.http import HttpResponse

def swipe(request):
	return render(request,'menu/swipe.html')

def home (request):
	return render(request,'menu/home.html')
# Create your views here.
