import pytest
from django.urls import reverse
from django.test import Client
from adminhub.domain.projects import operations as project_operations
from adminhub.domain.tasks import operations as task_operations


@pytest.mark.django_db
def test_project_view(client: Client):
    project1 = project_operations.create_project(
        'Project 1', 'Description 1')
    task1 = task_operations.create_task(
        'Task 1', 'Task description 1', project1)

    url = reverse('project-detail', kwargs={'pk': project1.pk})

    response = client.get(url)

    assert response.status_code == 200
    assert 'project-detail.html' in [
        template.name for template in response.templates]
    assert 'project' in response.context
    assert 'tasks_in_progress' in response.context
    assert 'tasks_to_do' in response.context
    assert 'tasks_complete' in response.context

    project = response.context['project']
    assert project1 == project

    tasks_to_do = response.context['tasks_to_do']
    assert len(tasks_to_do) == 1
    assert task1 in tasks_to_do
