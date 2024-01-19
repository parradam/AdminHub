from adminhub.data import models


def create_project(name, description):
    project = models.Project.objects.create(name=name, description=description)
    return project
