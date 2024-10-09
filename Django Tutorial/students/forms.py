from django import forms


class CreateStudentForm(forms.Form):
    first_name = forms.CharField(max_length=255, label="First Name")
    last_name = forms.CharField(max_length=255, label="Last Name")
    email = forms.EmailField(label="Email")


