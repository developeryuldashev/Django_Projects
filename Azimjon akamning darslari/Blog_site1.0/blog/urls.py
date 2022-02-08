from django.urls import path
from .views import *


urlpatterns=[
    path('', articles, name='articles'),
    path('article/<int:id>/', article_detail, name='article_detail'),
    path('reaction/<int:id>/<str:react>/',reaction, name='reaction'),
    path('persons/', persons_view, name='persons_list'),
]