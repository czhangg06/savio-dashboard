from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def personal_statistics(request):
	title = "Personal Statistics"

	args = { 'theTitle': title }
	return render(request, 'personal_statistics.html', args)