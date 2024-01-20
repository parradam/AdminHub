from collections.abc import Mapping
from django import forms
from django.forms.utils import ErrorList
from adminhub.data import models


class CreateProjectForm(forms.Form):
    project_fields = forms.fields_for_model(models.Project)

    name = project_fields['name']
    description = project_fields['description']


class ProjectForm(forms.Form):
    def __init__(self, project: models.Project, *args, **kwargs) -> None:
        self.project = project
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = project.name
        self.fields['description'].initial = project.description

    project_fields = forms.fields_for_model(models.Project)

    name = project_fields['name']
    description = project_fields['description']
