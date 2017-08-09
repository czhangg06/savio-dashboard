from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def su_calculator(request):
	title = "Service Unit Calculator"

	args = { 'theTitle': title }
	return render(request, 'su_calculator.html', args)