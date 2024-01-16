from adminhub.data.projects import models


def get_all_projects():
    projects = models.Project.objects.all()
    return projects
