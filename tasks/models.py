from django.db import models
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=date.today)  # Allows updates if needed using patch method
    completed = models.BooleanField(default=False, blank=True, null=True)
    
    # date = models.DateField(auto_now_add=True)   # Automatically set to the current date when a new task is created, but
    # prevents it from being updated in the future. So, used default=date.today property

    def __str__(self):
        return self.title
