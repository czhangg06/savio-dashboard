from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def menu(request):
	return render(request, 'menu.html')


