from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name="index"),
      path('signup', views.register_request, name="signup"),
      path('signin', views.login_request, name="signin"),
      path('subject', views.upload_subject, name="upload_subject"),
      path('course', views.course_upload, name="course_upload"),
]