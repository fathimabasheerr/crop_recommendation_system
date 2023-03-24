from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path("recommend", views.recommend),
    path('login',views.login),
    path('signup',views.signup)
    
]