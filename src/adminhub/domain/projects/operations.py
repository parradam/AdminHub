from adminhub.data import models


def create_project(name, description):
    project = models.Project.objects.create(name=name, description=description)
    return project


def update_project(project: models.Project, name: str, description: str) -> models.Project:
    project.name = name
    project.description = description
    project.save()

    return project
