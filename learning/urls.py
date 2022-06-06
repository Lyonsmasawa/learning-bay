from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('group/<str:pk>', views.group, name="group"),
    path('create-group/', views.createGroup, name="create-group")
]
