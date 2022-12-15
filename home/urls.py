from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("forgot", views.forgot, name = 'forgot'),
    path("signup", views.signup, name = 'signup'),
    path("signin", views.signin, name = 'signin'),
    path("signout", views.signout, name = 'signout')
    # path("forgot", views.forgot, name = 'forgot'),
    # path("folder", views.folder, name = 'folder')
]