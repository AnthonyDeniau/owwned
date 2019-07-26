from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello documentation!")

def show(request):
    return HttpResponse("Not implemented!")

def create(request):
    return HttpResponse("Not implemented!")

def edit(request):
    return HttpResponse("Not implemented!")

def delete():
    return HttpResponse("Not implemented!")
