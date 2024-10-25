from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('riderhub/', views.RiderHub.as_view(), name='riderhub'),
]
