import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_create_project_template(client: Client):

    url = reverse('create-project')

    response = client.get(url)

    assert response.status_code == 200
    assert 'create-project.html' in [
        template.name for template in response.templates]

    response_content = response.content.decode('utf-8')

    assert 'New project' in response_content
    assert '<h1>New project</h1>' in response_content
    assert '<form method="post" action="">' in response_content
    assert '<input type="text" name="name" maxlength="50" required id="id_name">' in response_content
    assert '<input type="text" name="description" maxlength="120" required id="id_description">' in response_content
    assert '<button type="submit">Create project</button>' in response_content


@pytest.mark.django_db
def test_create_project_template_post(client: Client):

    url = reverse('create-project')

    data = {
        'name': 'pname',
        'description': 'pdesc',
    }

    response = client.post(url, data=data, follow=True)

    assert response.status_code == 200
    assert 'project-detail.html' in [
        template.name for template in response.templates]
    assert 'project' in response.context
    project = response.context['project']
    assert project.name == 'pname'
    assert project.description == 'pdesc'
