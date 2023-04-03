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

rainfall = {
     'trivandrum' : '146',
     'kollam' :'108',
     'pathanamthitta':'217',
     'alappuzha':'230',
     'kottayam':'260',
     'idukki':'272',
     'ernakulam':'258',
     'thrissur' :'208',
     'palakkad' :'242',
     'malappuram':'255',
     'calicut' : '238',
     'wayanad' : '117',
     'kannur' : '200',
     'kasargod' : '279',
}