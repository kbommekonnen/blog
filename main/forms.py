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

    widgets = {
        'title': forms.TextInput(attrs={"class":"form-control"}),
        'instructor': forms.Select(attrs={"class":"form-control"}),
        'subject': forms.Select(attrs={"class":"form-control"}),
        'slug': forms.Textarea(attrs={"class":"form-control"}),
        'overview': forms.TextInput(attrs={"class":"form-control"}),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instructor'].queryset = User.objects.all()
        self.fields['subject'].queryset = Subject.objects.all()
        