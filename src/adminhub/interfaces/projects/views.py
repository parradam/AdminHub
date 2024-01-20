from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views import generic
from django import shortcuts
from adminhub.domain.projects import queries
from adminhub.domain.projects import operations
from . import forms
from django.urls import reverse


class Projects(generic.ListView):
    template_name = 'project-list.html'
    context_object_name = 'projects_list'

    def get_queryset(self) -> Any:
        return queries.get_all_projects()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class Project(generic.DetailView):
    template_name = 'project-detail.html'
    context_object_name = 'project_detail'

    def get_object(self) -> Any:
        project = queries.get_project(pk=self.kwargs['pk'])
        return project

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class CreateProject(generic.FormView):
    form_class = forms.ProjectForm
    template_name = 'create-project.html'

    def form_valid(self, form: Any) -> HttpResponse:
        project = operations.create_project(
            name=form.cleaned_data['name'], description=form.cleaned_data['description'])

        return shortcuts.redirect('project-detail', pk=project.pk)


class UpdateProject(generic.FormView):
    form_class = forms.ProjectForm
    template_name = 'update-project.html'
    context_object_name = 'project_detail'

    def get_object(self) -> Any:
        project = queries.get_project(pk=self.kwargs['pk'])
        return project

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = self.get_object()
        return context

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        project = self.get_object()
        initial['name'] = project.name
        initial['description'] = project.description
        return initial

    def form_valid(self, form: Any) -> HttpResponse:
        project = operations.update_project(pk=self.kwargs['pk'],
                                            name=form.cleaned_data['name'], description=form.cleaned_data['description'])

        return shortcuts.redirect(reverse('project-detail', kwargs={'pk': project.pk}))
