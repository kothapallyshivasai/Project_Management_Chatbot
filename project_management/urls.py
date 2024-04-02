from django.contrib import admin
from django.urls import path, include
from .views import custom_logout, employee_login, home, manager_login, validate_employee_login, validate_manager_login, register
from django.contrib.auth import views

urlpatterns = [
    path('admin', admin.site.urls, name="admin"),
    path('', home, name="home"),
    path('logout', custom_logout, name="logout"),
    path('employee/login', employee_login, name="employee_login"),
    path('employee/validate_employee_login', validate_employee_login, name="validate_employee_login"),
    path('manager/login', manager_login, name="manager_login"),
    path('manager/validate_manager_login', validate_manager_login, name="validate_manager_login"),
    path('register', register, name="register"),
    path('employee/', include("employee.urls")),
    path('manager/', include("manager.urls")),
]
