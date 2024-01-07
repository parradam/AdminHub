from django.db import models


class Task(models.Model):
    """
    An action to be completed as part of a project.
    """

    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
