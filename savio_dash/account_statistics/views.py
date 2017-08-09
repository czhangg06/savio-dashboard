from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def account_statistics(request):
	title = "Account Statistics"

	args = { 'theTitle': title }
	return render(request, 'account_statistics.html', args)