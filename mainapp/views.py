from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import News
from .serializer import NewsSerializer
from .tasks import SaveDailyNews


@api_view(['GET'])
def SaveNews(request):
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
    return Response({"dat":"response successfully saved"})


@api_view(['GET'])
def AllNews(request):
    all = News.objects.all()
    serializer = NewsSerializer(all, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def CeleryWork(request):
    SaveDailyNews.delay()
    return Response(status=status.HTTP_200_OK)
