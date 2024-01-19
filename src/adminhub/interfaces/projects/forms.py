from django import forms
from adminhub.data import models


class ProjectForm(forms.Form):
    project_fields = forms.fields_for_model(models.Project)

    name = project_fields['name']
    description = project_fields['description']
