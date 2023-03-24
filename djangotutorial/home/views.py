from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def recommend(request):
    return HttpResponse("Recommendation")

def login(request):
    return HttpResponse("login")

def signup(response):
    return HttpResponse("SignUp")
