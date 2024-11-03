from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditProfileForm
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('login')
    

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('transpo')
            # Redirect to a success page.
                
        else:
            messages.success(request, ("There Was an Error Logging In, Try Again..."))
            # Return an 'invalid login' error message.
            return redirect('login')
    return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('transpo')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('transpo')

    def get_object(self):
        return self.request.user