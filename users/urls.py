from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('logout', login_view, name='logout'),
]