from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from manager.models import Project, ProjectUpload, Task

# Create your views here.
@never_cache
@login_required
def manager_home(request):
    if request.user.is_staff:
        return render(request, 'manager/index.html', {})
    return redirect("employee_home")


@never_cache
@login_required
def add_employee(request):
    if request.user.is_superuser:
        return redirect('/admin')

    if request.user.is_staff:
        return render(request, 'manager/add_employee.html', {})
    return redirect("employee_home")


@never_cache
@login_required
def validate_add_employee(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        is_staff = False

        if User.objects.filter(username=username).exists():
            return redirect("add_employee")
        
        if User.objects.filter(email=email).exists():
            return redirect("add_employee")

        User.objects.create_user(username=username, email=email, password=password, is_staff=is_staff)

        return redirect("view_employees")
    return redirect("add_employee")


@never_cache
@login_required
def view_employees(request):
    if request.user.is_superuser:
        return redirect('/admin')

    if request.user.is_staff:
        return render(request, 'manager/view_employees.html', {"employees": User.objects.filter(is_staff=False)})
    return redirect("employee_home")


@never_cache
@login_required
def add_project(request):
    if request.user.is_superuser:
        return redirect('/admin')

    if request.user.is_staff:
        return render(request, 'manager/add_project.html', {})
    return redirect("employee_home")


@never_cache
@login_required
def validate_add_project(request):
    if request.method == "POST":
        project_title = request.POST.get("project_title")
        description = request.POST.get("description")
        manager = request.user

        project = Project()
        project.project_title = project_title
        project.description = description
        project.manager = manager
        project.save()

        return redirect("employee_home")
    return redirect("add_project")


@never_cache
@login_required
def view_projects(request):
    if request.user.is_superuser:
        return redirect('/admin')

    if request.user.is_staff:
        return render(request, 'manager/view_projects.html', {"projects": Project.objects.filter(manager=request.user)})
    return redirect("employee_home")



@never_cache
@login_required
def view_project(request, id):
    if request.user.is_superuser:
        return redirect('/admin')

    if request.user.is_staff:
        tasks = Task.objects.filter(project=Project.objects.get(pk=id))
        return render(request, 'manager/view_project.html', {"project": Project.objects.get(pk=id), 
                                                             "employees": User.objects.filter(is_staff=False),
                                                             "tasks": tasks})
    return redirect("employee_home")


@never_cache
@login_required
def add_task(request, id):
    if request.method == "POST":
        task_name = request.POST.get("title")
        project = Project.objects.get(pk=id)
        assigned_to = User.objects.get(pk=int(request.POST.get('assigned_to')))
        Task.objects.create(task_name=task_name, project=project, assigned_to=assigned_to)
        return redirect("view_projects")
    return redirect("employee_home") 


@never_cache
@login_required
def complete_project(request, id):
    if request.method == "POST":
        project = Project.objects.get(pk=id)
        project.status = True
        project.save()
        return redirect("view_projects")
    return redirect("employee_home") 
    

@never_cache
@login_required
def show_upload_projects(request):
    if request.user.is_superuser:
        return redirect('/admin')

    if request.user.is_staff:
        projects = []
        try:
            projects = Project.objects.filter(status=True, manager=request.user).exclude(
            Q(projectupload__isnull=False) | Q(projectupload__id__isnull=False)
            )
        except Exception as e:
            pass
        return render(request, 'manager/upload_project.html', {"projects": projects})
    
    return redirect("employee_home")


@never_cache
@login_required
def upload_project(request, id):
    upload = ProjectUpload()
    upload.project = Project.objects.get(pk=id)
    print("OK")
    upload.save()
    return redirect("show_upload_projects")