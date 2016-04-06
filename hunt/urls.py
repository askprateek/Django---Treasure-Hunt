from django.conf.urls import url
from .views import *

urlpatterns= [
    url(r'^$', hunt_main_page),
    #url(r'^check$', check, name='hunt/check.html'),
]
