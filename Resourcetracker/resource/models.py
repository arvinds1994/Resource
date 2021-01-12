from django.db import models

# Create your models here.

class Resource(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=10)
    email_id = models.EmailField()
    project_name = models.CharField(max_length=30)
    team_name = models.CharField(max_length=30)
    added_on = models.DateField(auto_now=True)
    assigned_work = models.TextField(default='', null=True)

    def __str__(self):
        return self.employee_id