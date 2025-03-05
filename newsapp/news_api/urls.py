# here we're gonna hit request to the news api
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'), 
    path('signup/', views.signup_page, name='signup_page'), 
    path('register/', views.signup, name= 'signup'), 
    path('login/', views.login_page, name='login_page'), 
    path('authenticate/', views.login_user, name='login')
]