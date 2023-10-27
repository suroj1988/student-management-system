from .views import *
from django.urls import path
from .import HodViews,staffViews,studentViews

urlpatterns = [
    path('', home, name='home'),
    path('base', base, name='base')

]