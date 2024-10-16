from django.shortcuts import render
from django.views import View
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from. import forms

# Create your views here.

class GetAllStudents(View):

    def get(self, request):
        students = models.Student.objects.all()  #get, filter can be used as well

        return render(request, 'all_students.html', {"students": students})

class GetStudents(APIView):

    def get(self, request):
        students = models.Student.objects.all()

        things = {
            "thing1": 1,
            "thing2": 2
        }

        return Response(things, status=status.HTTP_200_OK)
    

class CreateStudent(View):

    def get(self, request):
        form = forms.CreateStudentForm()

        return render(request, 'create_student_form.html', {'form':form})
    
    def post(self, request):

        form = forms.CreateStudentForm(request.POST)
        if form.is_valid():
            student = models.Student(
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],
                email = form.cleaned_data["email"]

            )

            student.save()
            return render(request, "sucess.html")
        
        return render(request, "error.html")
    
class NewStudent(APIView):

     def post(self, request):
        first_name = request.data.get("fisrt_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        student = models.Student(
                first_name = first_name,
                last_name = last_name,
                email = email
    
            )
        

from django.shortcuts import render, redirect

class Homepage(View):
    def get(self, request):
        return render(request, 'home.html')  # Create a template called new_template.html
    
    def post(self, request):
        if request.method == "POST":
        # Redirect to another URL
            return redirect('login')  # Change '/new-url/' to your desired 
        
        
class SigninPage(View):
    def get(self, request):
        form = forms.SigninForm()
        return render(request, 'login.html', {'form': form})  # Create a template called new_template.html
    
    def post(self, request):

        form = forms.SigninForm(request.POST)

        if form.is_valid():
            cwid = form.cleaned_data['CWID']
            try:
                rider = models.Rider.objects.get(CWID = cwid)
                return render(request, "sucess.html")
            except models.Rider.DoesNotExist:
                return render(request, "error.html")
            

class BookaRide(View):
    def get (self, request):
        form = forms.BookaRideForm
        return render(request, 'bookride.html', {'form':form})
    
    def post(self, request):
        form = forms.BookaRideForm(request.POST)
        if form.is_valid():
            RideRequest = models.RideRequest(
               dropoff_location = form.cleaned_data['Location']
            )
            try:
                Drivername = form.cleaned_data['Driver']
                Driver = models.Driver.objects.get(first_name=Drivername)
                Driver.status = 'Unavailable'
                Driver.save()
                RideRequest.save()
                return render(request, 'sucess.html')
            except Driver.DoesNotExist:
                return render(request, 'error.html')
        
    

class GetAllDrivers(View):
    def get(self, request):
        drivers = models.Driver.objects.all()  # Fetch all drivers
        return render(request, 'all_drivers.html', {"drivers": drivers})

            