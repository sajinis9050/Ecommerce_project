from django.urls import path
from . import views


urlpatterns = [
     path('', views.index2),
     path('new', views.new)
]