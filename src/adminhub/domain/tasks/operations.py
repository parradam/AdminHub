from adminhub.data import models


def create_task(name: str, description: str, project: models.Project):
    task = models.Task.objects.create(
        name=name, description=description, project=project)
    return task
