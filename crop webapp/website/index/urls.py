from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('products',views.products, name='products'),
    path('recommend',views.recommend, name='recommend'),
    path('contact',views.contact, name='contact'),
    path('about',views.about,name='about'),
    path('redirect_form_data',views.redirect_form_data,name='redirect_form_data')
]