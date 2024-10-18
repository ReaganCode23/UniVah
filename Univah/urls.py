from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.Homepage.as_view(), name='home'),
    path('login/', views.SigninPage.as_view(), name='login'),  # New URL
    path('bookride/',views.BookaRide.as_view(), name='bookride'),
    path("all_drivers/", views.GetAllDrivers.as_view(), name="all_drivers"),
    path("hometemplate/", views.HomeTemplate.as_view(), name="hometemplate")      
]
