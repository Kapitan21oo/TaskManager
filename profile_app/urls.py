from .views import *
from django.urls import path

urlpatterns = [
    path('', main_page, name='main_page'),
    path('register', register_user, name='registers'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),


]