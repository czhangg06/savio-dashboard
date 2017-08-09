from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def job_history(request):
	title = "Job History"

	args = { 'theTitle': title }
	return render(request, 'job_history.html', args)