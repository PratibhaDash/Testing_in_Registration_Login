from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from .forms import *
from user.models import RegistrationPage
# Create your views here.

def Registrationpage(request):
    regpage=RegistrationPage.objects.all()
    context={
        'regpage':regpage
    }
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile_no=request.POST.get('mobile_no')
        address=request.POST.get('address')
        password=request.POST.get('password')
        
        rp=RegistrationPage(
            name=name,
            email=email,
            mobile_no=mobile_no,
            address=address,
            password=password
        )
        rp.save()
        return redirect('login')
    return render(request,'registration.html')


def Loginpage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        return redirect('logout')
    return render(request,'login.html')


def Logoutpage(request):
    return render(request,'logout.html')
    
