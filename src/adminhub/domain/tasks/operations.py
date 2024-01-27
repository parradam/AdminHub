from adminhub.data import models


def create_task(name: str, description: str, project: models.Project):
    task = models.Task.objects.create(
        name=name, description=description, project=project)
    return task


def update_task(task: models.Task, name: str, description: str, status: str) -> models.Project:
    task.name = name
    task.description = description
    task.status = status
    task.save()

    return task


def delete_task(pk: int) -> None:
    models.Task.objects.filter(pk=pk).delete()
