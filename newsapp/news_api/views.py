from django.shortcuts import render
# requests module to fetch the particular news 
# from the news api 
import requests
import os

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