# todo/api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include
from .views import (
    TaskListApiView, TaskFilterApiView
)

urlpatterns = [
    path('', TaskListApiView.as_view()),
    path('<int:task_id>/', TaskFilterApiView.as_view()),
]