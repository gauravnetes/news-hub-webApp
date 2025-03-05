from django.shortcuts import render
# requests module to fetch the particular news 
# from the news api 
import requests
import os

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth import login

API_KEY = os.getenv("NEWS_API_KEY")
# Create your views here.
def home(request): 
    url = f'https://newsapi.org/v2/top-headlines?category=technology&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {
        'articles':  articles
    }
    return render(request, 'news_api/home.html', context)
def signup_page(request): 
    return render(request, 'news_api/signup.html')
def signup(request):  
    if request.user.is_authenticated:  # Redirect if user is already logged in
        return redirect('home')

    if request.method == "POST":  
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            return render(request, 'news_api/signup.html', {'error': 'Email already exists'})

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        # login(request, user)  # Automatically log in the user
        return redirect('login_page')  

    return render(request, 'news_api/signup.html')

# Login 
def login_page(request):
    return render(request, 'news_api/login.html')
def login_user(request): 
    if request.user.is_authenticated:  # type: ignore
        return redirect('home')
    
    if request.method == "POST": 
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.filter(email=email).first()
        if user: 
            user = authenticate(request, username = user.username, password=password)    
            if user: 
                login(request, user)
                return redirect('home')
            else: 
                return render(request, 'news_api/login.html', {'error': 'Invalid Credentials'})
        else: 
            return render(request, 'news_api/login.html', {'error': 'User does not exist'})
    return redirect('login_page')