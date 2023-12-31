from django.db import models
from django.contrib.auth.models import AbstractUser, User

# class User(AbstractUser):
#       id_admin = models.BooleanField(default=False)
#       id_student = models.BooleanField(default=False)

class Subject(models.Model):
      title = models.CharField(max_length=200)
      slug = models.TextField()
      image = models.FileField(upload_to='images/')

      def __str__(self):
            return self.title
class Course(models.Model):
      title = models.CharField(max_length=200)
      instructor = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
      subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
      slug = models.TextField(max_length=300)
      overview = models.CharField(max_length=200)

      def __str__(self):
            return self.title
class Module(models.Model):
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
      title = models.CharField(max_length=200)
      description = models.TextField(max_length=400)
      order = models.CharField(max_length = 250)

      def __str__(self):
            return self.title