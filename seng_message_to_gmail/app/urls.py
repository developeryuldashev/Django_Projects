from django.urls import path
from .views import contactsendemail

urlpatterns=[
          path('',contactsendemail, name='index')
]