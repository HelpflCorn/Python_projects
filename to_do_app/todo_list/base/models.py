from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    task_title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_title
    
    class Meta:
        ordering = ["complete"]
    