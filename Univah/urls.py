from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('riderhub/', views.RiderHub.as_view(), name='riderhub'),
    path('driverhub/', views.DriverHub.as_view(), name='driverhub'),
    path('transpo/', views.Transpo.as_view(), name = 'transpo'),
    path('maptest', views.Maptest.as_view(), name = 'maptest'),
]


