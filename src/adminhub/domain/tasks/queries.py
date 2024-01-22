from adminhub.data import models


def get_tasks_for_project(project: models.Project):
    tasks = models.Task.objects.filter(project__id=project.pk)
    return tasks
