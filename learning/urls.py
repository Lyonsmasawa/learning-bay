from django.urls import path
from . import views

urlpatterns = [
    path('login-page/', views.loginPage, name="login-page"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('profile/<str:pk>', views.userProfile, name="profile"),
    path('', views.home, name="home"),
    path('group/<str:pk>/', views.group, name="group"),
    path('create-group/', views.createGroup, name="create-group"),
    path('update-group/<str:pk>/', views.updateGroup, name="update-group"),
    path('delete-group/<str:pk>/', views.deleteGroup, name="delete-group"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
]
