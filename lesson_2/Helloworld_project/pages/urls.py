from django.urls import path
from .views import home_page_view, Home_Page_View
urlpatterns=[
    path('home1',home_page_view, name='home1'),
    path('home2',Home_Page_View.as_view(), name='home2')
]
