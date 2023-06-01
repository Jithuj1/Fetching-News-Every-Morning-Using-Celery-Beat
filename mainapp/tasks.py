from celery import shared_task
import requests
from .models import News


@shared_task
def SaveDailyNews():
    print('reached here')
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-05-18&sortBy=publishedAt&apiKey=d69ca4ccf3ed44859bc650c7e80a96f9' 
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data ['articles']
        articles = articles [0:2]
        print(len(articles))
        for i in articles:
            obj = News()
            obj.author = i ['author']
            obj.title = i ['title']
            obj.dis = i ['description']
            obj.content = i ['content']
            obj.image_url = i ['urlToImage']
            obj.save()


@shared_task
def printEvery():
    print('hello this is from celery beat')