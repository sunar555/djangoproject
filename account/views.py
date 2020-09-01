from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Signup, Login
from . import forms



# Create your views here.
def index(request):
    return HttpResponse('Hello')

def temp_demo(request):
    dist_var ={'any_key': "hello, this is a value for the key from view.py that can be used in index.html",
               'Name': (2+4) #just for testing
               }
    return render(request,'account/template.html', context=dist_var)

def sign_up_view(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['password'] 
            b = form.cleaned_data['verify_password']
            if a == b:
                post = form.save(commit=False)
                post.save()
            else:
                form = forms.SignupForm()
                messages.error(request, "Password didn't match try again")
            return redirect ('/',pk=post.pk)
    return render(request,'account/signup.html',{'signup':form})

def login_view(request):
    form = forms.LoginForm()
    if request.method =="POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["username"]
            b = form.cleaned_data["password"]
            try:
                bb = Signup.objects.values_list('password', flat=True).get(username=a)
            except Signup.DoesNotExist:
                bb = "kjdasjhgjggjdsadbejkhsndsadasdsad"
            if b == bb:
                return HttpResponse("Congratulation! You're signed in " + a)
                #return redirect('/', pk=post.pk)
            else:
                messages.error(request, "Username or Password is not correct.")
        else:
             form = forms.LoginForm()
          #      return HttpResponse("Password not matched, try again")
    else:
        form = forms.LoginForm()



    return render(request,'account/login.html',{'login':form})




