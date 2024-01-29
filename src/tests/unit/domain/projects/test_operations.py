import pytest
from adminhub.data import models
from adminhub.domain.projects import operations as project_operations


@pytest.mark.django_db
def test_project_is_created():
    assert models.project.Project.objects.all().count() == 0
    project = project_operations.create_project(
        'Project name', 'Project description')
    assert models.project.Project.objects.all().count() == 1
    assert project.name == 'Project name'
    assert project.description == 'Project description'


@pytest.mark.django_db
def test_project_is_updated():
    project = project_operations.create_project(
        "Project name", "Project description")
    assert project.name == 'Project name'
    assert project.description == 'Project description'

    updated_project = project_operations.update_project(
        project, 'Updated project name', 'Updated project description')
    assert updated_project.name == 'Updated project name'
    assert updated_project.description == 'Updated project description'
