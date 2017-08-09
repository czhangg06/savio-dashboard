from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def quota_manager(request):
	title = "Quota Manager"

	args = { 'theTitle': title }
	return render(request, 'quota_manager.html', args)