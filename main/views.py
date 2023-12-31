from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, SubjectForm, CourseForm
from .models import Course, Subject
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

def index(request):
      return render(request, 'navbar.html', {})

def register_request(request):
      
      if request.method =='POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                  user = form.save()
                  print(user)
            messages.success(request, "Fill the fields to register!!!!!!!!")
            return redirect('subject')
      if request.method == 'GET':
            form = RegisterForm()
            return render(request, 'register.html', {'form': form})
      
def login_request(request):
      
      if request.method =='POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  username = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
                  user = authenticate(username = username, password = password)
                  if user is not None:
                        login(request, user)
                        messages.success(request, "user is logged in")
                  else:
                        messages.error(request, "invalid username or password try again")
            else:
                  messages.error(request, "Invalid username or password")
      return render(request = request, template_name= 'login.html')

def upload_subject(request):
      if request.method == 'POST':
            form = SubjectForm(request.POST, request.FILES)
            if form.is_valid():
                  subject = form.save()
                  print(subject)
                  messages.success(request, "new subject is uploaded") 
            messages.error(request, "Invalid input")
      return render(request=request, template_name='subject.html')

@csrf_exempt
def course_upload(request):
      course = Course.objects.all()
      subject = Subject.objects.all()
      instructor = User.objects.all()
      context = {'course': course, 'subject':subject, 'instructor': instructor}
      if request.method == 'POST':
            form = CourseForm(request.POST)
            if form.is_valid():
                  form.instance.instructor = User.objects.get(username = request.POST.get('instructor'))
                  form.instance.subject = Subject.objects.get(title = request.POST.get('subject'))
                  form.save()
                  messages.success(request, "course is uploaded successfully!! thanks")
            messages.error(request, "Invalid Input form")
            return render(request=request, template_name='course.html', context=context )
      else:
            return render(request=request, template_name='course.html', context=context )