from django.urls import path
from .views import employee_home, employee_view_project, employee_view_projects, task_done, tasks_completed, tasks_incompleted

urlpatterns = [
    path('home', employee_home, name="employee_home"),
    path('tasks_completed', tasks_completed, name="tasks_completed"),
    path('tasks_incompleted', tasks_incompleted, name="tasks_incompleted"), 
    path('task_done/<int:id>', task_done, name="task_done"),  
    path('employee_view_projects', employee_view_projects, name="employee_view_projects"),  
    path('employee_view_project/<int:id>', employee_view_project, name="employee_view_project"), 
]