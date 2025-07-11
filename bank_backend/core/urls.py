from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register),
    #path('welcome/',welcome),
    path('login/', login_view, name='login'),
    path('dashboard/',Dashboard,name='dashboard'),
    path('',index, name='index' )
]