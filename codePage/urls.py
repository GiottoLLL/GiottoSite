from django.urls import path
from codePage import views


urlpatterns = [
    path('', views.index, name='index')
]