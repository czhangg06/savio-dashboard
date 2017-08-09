from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def faqs(request):
	title = "Frequently Asked Questions"

	args = { 'theTitle': title }
	return render(request, 'faqs.html', args)