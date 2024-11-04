from django.urls import path
from .import views

urlpatterns = [
    path('riderhub/', views.RiderHub.as_view(), name='riderhub'),
    path('driverhub/', views.DriverHub.as_view(), name='driverhub'),
    path('', views.Transpo.as_view(), name = 'transpo'),
]


