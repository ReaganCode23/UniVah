from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.Homepage.as_view(), name='home'),
    path('login/', views.SigninPage.as_view(), name='login'),     
]
