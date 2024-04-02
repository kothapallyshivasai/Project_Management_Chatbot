from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=50, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.project_title} - {self.manager.username}' 
    

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class ProjectUpload(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)