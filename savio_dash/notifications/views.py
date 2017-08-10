from django.shortcuts import render, HttpResponse
from django.contrib import messages
import os, os.path, json

# Create your views here.
def notifications(request):
	title = "Notification Center"

	args = { 'theTitle': title }

	if 6 == 6:
		messages.info(request, "You've used up 75 percent of your quota")
	return render(request, 'notifications.html', args)
