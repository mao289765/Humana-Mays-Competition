from django.shortcuts import render

from django.http import HttpResponse

home = "\
<img src=\"http://178.128.68.14/logo.png\" alt=\"logo\">\
<br>Please select a patient to view opioid reccomendations: <br><br>\
<a href=\"http://127.0.0.1:8000/patient1/\">Patient 1</a><br><br>\
<a href=\"http://127.0.0.1:8000/patient2/\">Patient 2</a><br><br>\
<a href=\"http://127.0.0.1:8000/patient3/\">Patient 3</a><br>\
"

def index(request):
    return HttpResponse(home)
	
def patient1(request):
	return HttpResponse("PATIENT 1")
	
def patient2(request):
	return HttpResponse("PATIENT 2")
	
def patient3(request):
	return HttpResponse("PATIENT 3")
