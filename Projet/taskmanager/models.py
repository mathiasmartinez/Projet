from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class Project(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey('Project',on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    assignee = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    priority = models.IntegerField() # Degré de priorité avec 1 une tâche prioritaire
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Journal(models.Model):
    date = models.DateTimeField(default=timezone.now)
    entry = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey('Task',on_delete=models.CASCADE)





