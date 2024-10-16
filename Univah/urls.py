from django.urls import path
from .import views

urlpatterns = [

    path("all/", views.GetAllStudents.as_view(), name="all"),
    path("all-again/", views.GetStudents.as_view(), name="all-again"),
    path("new/", views.CreateStudent.as_view(), name = "new"),
    path("new/", views.NewStudent.as_view(), name = "new"),
    path('home/', views.Homepage.as_view(), name='home'),
    path('login/', views.SigninPage.as_view(), name='login'),  # New URL
    path('bookride/',views.BookaRide.as_view(), name='bookride'),
    path("all_drivers/", views.GetAllDrivers.as_view(), name="all_drivers"),
    path("hometemplate/", views.HomeTemplate.as_view(), name="hometemplate")
           
]
