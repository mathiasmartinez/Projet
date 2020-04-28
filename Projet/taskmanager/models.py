from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    priority = models.IntegerField()
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.name





