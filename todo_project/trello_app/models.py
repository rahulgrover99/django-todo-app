from django.db import models
from django.utils import timezone
# Create your models here.

# Requirements
    # - Tasks 
    #     - content
    #     - creation_date
    #     - deadline
    #     - task_list 
        
    #     - Status 
    #     - completed_on

    #  - Task List
        # - name 
        # - created_at



# Task Table

# id | content | creation_date | deadline | task_list_id | status | completed_on | status


# Task_list
# id | name | created_at


class TaskList(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
   

class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)


    STATUS_CHOICES = (
        ('P', 'PENDING'),
        ('C', 'COMPLETED'),
        ('IP', 'IN_PROGRESS'),
        ('D', 'DROPPED')
    )
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0], max_length=2)

    def __str__(self):
        return f"{self.content}-{self.task_list}"
    

