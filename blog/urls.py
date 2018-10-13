""" The Blogs url Conf """

from django.urls import path   
from blog import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
