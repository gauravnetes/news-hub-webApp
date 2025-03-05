# here we're gonna hit request to the news api
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home')
]