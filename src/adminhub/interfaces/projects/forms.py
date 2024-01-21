from django import forms
from adminhub.data import models


class CreateProject(forms.Form):
    project_fields = forms.fields_for_model(models.Project)

    name = project_fields['name']
    description = project_fields['description']


class UpdateProject(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(max_length=120)

    def __init__(self, project, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if project:
            self.fields['name'].initial = project.name
            self.fields['description'].initial = project.description
