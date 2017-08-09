from django.shortcuts import render, HttpResponse
import os, os.path, json

# Create your views here.
def notifications(request):
	title = "Notification Center"

	args = { 'theTitle': title }
	return render(request, 'notifications.html', args)