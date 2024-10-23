from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.Homepage.as_view(), name='home'),
    path('ridestatus/', views.RideStatus.as_view(), name='ridestatus')
]
