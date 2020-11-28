from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', views.task_main, name='main'),
]
