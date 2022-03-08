from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Welcome!')

def signin(request):
    return HttpResponse('Sign in')

def signup(request):
    return HttpResponse('Sign up')