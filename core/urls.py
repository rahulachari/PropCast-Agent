from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('predict/', views.predict, name='predict'),
    path('download-report/', views.download_report, name='download_report'),
    path('properties/', views.properties_list, name='properties_list'),
    path('compare/', views.compare_properties, name='compare_properties'),
]