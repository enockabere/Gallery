from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name='welcome'),
    path('all/', views.all_images,name='allImages'),
    path('single/', views.single_image,name='singleImage'),
    path('search/', views.search_results,name='search_results')
]