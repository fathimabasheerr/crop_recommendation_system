from django.shortcuts import render
from django.http import HttpResponse



def index(request):
     return render(request,'home.html')

def products(request):
     return render(request,'products.html')

def recommend(request):
     return render(request,"recommend.html")

def contact(request):
     return render(request,'contact.html')

def about(request):
     return render(request,'about.html')


