from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from manager.models import Project, Task
from django.contrib.auth.models import User

# Create your views here.
@never_cache
@login_required
def employee_home(request):
    if not request.user.is_staff:
        return render(request, "employee/index.html", {})
    return redirect("manager_home")


@never_cache
@login_required
def tasks_completed(request):
    if not request.user.is_staff:
        tasks = Task.objects.filter(assigned_to=request.user, status=True)
        return render(request, "employee/tasks_completed.html", {"tasks": tasks})
    return redirect("manager_home")


@never_cache
@login_required
def tasks_incompleted(request):
    if not request.user.is_staff:
        tasks = Task.objects.filter(assigned_to=request.user, status=False)
        return render(request, "employee/tasks_incompleted.html", {"tasks": tasks})
    return redirect("manager_home")


@never_cache
@login_required
def task_done(request, id):
    if not request.user.is_staff:
        if request.method == "POST":
            task = Task.objects.get(pk=id)
            task.status = True
            task.save()
            return redirect("tasks_completed")
    return redirect("manager_home")


@never_cache
@login_required
def employee_view_projects(request):
    if not request.user.is_staff:
        projects = Project.objects.filter(
            status=True,
            projectupload__isnull=False
        )
        return render(request, "employee/view_projects.html", {"projects": projects})
    return redirect("manager_home")


@never_cache
@login_required
def employee_view_project(request, id):
    if request.user.is_superuser:
        return redirect('/admin')

    if not request.user.is_staff:
        tasks = Task.objects.filter(project=Project.objects.get(pk=id))
        return render(request, 'employee/view_project.html', {"project": Project.objects.get(pk=id), 
                                                             "employees": User.objects.filter(is_staff=False),
                                                             "tasks": tasks})
    return redirect("employee_home")