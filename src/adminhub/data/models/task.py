from django.db import models
from . import Project


class Task(models.Model):
    """
    An action to be completed as part of a project.
    """

    class Statuses(models.TextChoices):
        TO_DO = 'T', 'To do'
        IN_PROGRESS = 'I', 'In progress'
        COMPLETE = 'C', 'Complete'

    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    status = models.CharField(
        max_length=1,
        choices=Statuses.choices,
        default=Statuses.TO_DO,
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, related_name='tasks')
