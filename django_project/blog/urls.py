from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='blog-home'),
    path('personalweb/', views.personalweb, name ='blog-personalweb')
]
