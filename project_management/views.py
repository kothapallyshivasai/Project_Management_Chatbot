from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login as auth_login
from django.views.decorators.cache import never_cache

@never_cache
def home(request):
    if request.user.is_staff:
        return redirect("manager_home")
    if request.user.is_authenticated:
        return redirect("employee_home")
    return render(request, "default/index.html", {})

@never_cache
def employee_login(request):
    if request.user.is_staff:
        return redirect("manager_home")
    if request.user.is_authenticated:
        return redirect("employee_home")
    return render(request, "default/employee_login.html", {})

@never_cache
def validate_employee_login(request):
    if request.user.is_staff:
        return redirect("manager_home")
    if request.user.is_authenticated:
        return redirect("employee_home")
    
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))

        if user is not None:
            if not user.is_staff:
                auth_login(request, user)  
                return redirect("employee_home")
            return redirect("home")
            
        else:
            return redirect("employee_login")
        
    return redirect("home")
    

@never_cache
def manager_login(request):
    if request.user.is_staff:
        return redirect("manager_home")
    if request.user.is_authenticated:
        return redirect("employee_home")
    return render(request, "default/manager_login.html", {})

@never_cache
def validate_manager_login(request):
    if request.user.is_staff:
        return redirect("manager_home")
    if request.user.is_authenticated:
        return redirect("employee_home")
    
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))

        if user is not None:
            if user.is_staff:
                auth_login(request, user)  
                return redirect("manager_home")
            return redirect("home")
            
        else:
            return redirect("manager_login")
    return redirect("home")
    
@never_cache
def register(request):
    if request.user.is_staff:
        return redirect("manager_home")
    if request.user.is_authenticated:
        return redirect("employee_home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        is_staff = True

        if password != password2:
            return redirect("register")

        if User.objects.filter(username=username).exists():
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            return redirect("register")

        User.objects.create_user(username=username, email=email, password=password, is_staff=is_staff)
        authenticated_user = authenticate(request, username=username, password=password)
        
        auth_login(request, authenticated_user)  
        return redirect("manager_home")
    
    return render(request, "default/register.html", {})

@never_cache
def custom_logout(request):
    logout(request)
    return redirect("home")