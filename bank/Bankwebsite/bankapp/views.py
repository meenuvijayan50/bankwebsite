from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from bankapp.forms import UserForm
from bankapp.models import District,Branches


# Create your views here.
def demo(request):
    return render(request,"base.html")
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    return render(request,"register.html")

def userform(request):
    District_id =request.POST.get('District')
    branche= Branches.objects.filter(District_id=District_id).order_by('name')
    return render(request,"forms.html" , {'branche' : branche})


def add_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # form.save()
            messages.info(request, " submitted successfully.")
            # return redirect('register')
    return render(request, 'branches.html', {'form': form})

def load_branches(request):
    District_id = request.GET.get('District_id')
    branches= User.objects.filter(District_id=District_id).all()
    return render(request, 'forms.html', {'branches': branches})
# def submit(request):
#     return HttpResponse("Application accepted")