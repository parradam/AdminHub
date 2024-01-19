from adminhub.data import models


def get_all_projects():
    projects = models.Project.objects.all()
    return projects


def get_project(pk):
    project = models.Project.objects.get(pk=pk)
    return project
