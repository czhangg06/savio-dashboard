from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def settings(request):
	title = "Your Settings"

	args = { 'theTitle': title }
	return render(request, 'settings.html', args)