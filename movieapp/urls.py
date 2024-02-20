from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name='index'),
    path('movie-video/<int:id>', movie_detail, name='movie_detail'),
    path('channel-video/<int:id>', channel_detail, name='channel_detail'),
    path('live_channel/', live_channel, name='live_channel'),
    path('about/', about, name='about'),

    path('search/', QidirishView.as_view(), name='search'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    