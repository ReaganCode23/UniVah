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