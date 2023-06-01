from django.urls import path
from .views import SaveNews, AllNews, CeleryWork

urlpatterns = [
    path('news', SaveNews),
    path('all', AllNews),
    path('celery', CeleryWork)
]
