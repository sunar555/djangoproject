from django.db import models

# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    verify_password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Blog(models.Model):
    subject = models.CharField(max_length=50)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.subject
