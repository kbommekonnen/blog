from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Subject, Course


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):

    username = forms.CharField(max_length=200)
    class Meta:
        model=User
        fields = ['username','email','password1']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'slug', 'image']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields =['title', 'instructor', 'subject', 'slug', 'overview']