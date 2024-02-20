from .views import *
from django.urls import path

urlpatterns = [
    path('login/', login, name='login'),
    path('logout_reply/', logout_reply, name='logout_reply'),
    path('register/', register, name='register'),


    
]
