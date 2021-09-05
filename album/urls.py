from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.welcome,name='welcome'),
    path('all/', views.all_images,name='allImages'),
    path('single/<int:pk>', views.single_image,name='singleImage'),
    path('search/', views.search_results,name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)