import pytest
from adminhub.data import models
from adminhub.domain.projects import operations as project_operations
from adminhub.domain.tasks import operations as task_operations


@pytest.mark.django_db
def test_task_is_created():
    project = project_operations.create_project(
        "Project name", "Project description")
    assert models.task.Task.objects.all().count() == 0
    task = task_operations.create_task('Name', 'Description', project)
    assert models.task.Task.objects.all().count() == 1
    assert task.name == 'Name'
    assert task.description == 'Description'
    assert task.status == 'T'


@pytest.mark.django_db
def test_task_is_updated():
    project = project_operations.create_project(
        "Project name", "Project description")
    task = task_operations.create_task('Name', 'Description', project)
    assert task.name == 'Name'
    assert task.description == 'Description'
    assert task.status == 'T'

    updated_task = task_operations.update_task(
        task, 'Updated task name', 'Updated task description', 'C')
    assert updated_task.name == 'Updated task name'
    assert updated_task.description == 'Updated task description'
    assert updated_task.status == 'C'
