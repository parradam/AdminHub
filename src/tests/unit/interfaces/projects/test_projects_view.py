import pytest
from django.urls import reverse
from django.test import Client
from adminhub.domain.projects import operations as project_operations


@pytest.mark.django_db
def test_projects_view(client: Client):
    project1 = project_operations.create_project(
        'Project 1', 'Description 1')
    project2 = project_operations.create_project(
        'Project 2', 'Description 2')

    url = reverse('project-list')

    response = client.get(url)

    assert response.status_code == 200
    assert 'project-list.html' in [
        template.name for template in response.templates]
    assert 'projects_list' in response.context

    projects_list = response.context['projects_list']
    assert len(projects_list) == 2
    assert project1 in projects_list
    assert project2 in projects_list
