from django.urls import path
from . import views


urlpatterns = [
     path('', views.index3),
     path('new', views.new)
]