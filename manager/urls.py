from django.urls import path

from .views import add_employee, add_project, add_task, complete_project, manager_home, show_upload_projects, upload_project, validate_add_employee, validate_add_project, view_employees, view_project, view_projects

urlpatterns = [
    path('home', manager_home, name="manager_home"),
    path('add_employee', add_employee, name="add_employee"),
    path('validate_add_employee', validate_add_employee, name="validate_add_employee"),
    path('view_employees', view_employees, name="view_employees"),
    path('add_project', add_project, name="add_project"), 
    path('validate_add_project', validate_add_project, name="validate_add_project"), 
    path('view_projects', view_projects, name="view_projects"), 
    path('view_project/<int:id>', view_project, name="view_project"), 
    path('add_task/<int:id>', add_task, name="add_task"),  
    path('complete_project/<int:id>', complete_project, name="complete_project"),   
    path('upload_project/<int:id>', upload_project, name="upload_project"),   
    path('show_upload_projects', show_upload_projects, name="show_upload_projects"),    
]