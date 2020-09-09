from django.urls import path
from . import views

urlpatterns = [
    path('', views.search,name='index_page'),
    path('multiple/', views.multiple_weather,name='add_page'),

]
