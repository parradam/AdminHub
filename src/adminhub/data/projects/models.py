from django.db import models


class Project(models.Model):
    """
    A collection of tasks.
    """

    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
