from typing import Any
from django.db.models.query import QuerySet
from django import http
from django.views import generic
from django import shortcuts
from adminhub.domain.projects import queries
from adminhub.domain.projects import operations
from . import forms
from django.urls import reverse
from adminhub.data import models


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
    form_class = forms.CreateProject
    template_name = 'create-project.html'

    def form_valid(self, form: Any) -> http.HttpResponse:
        project = operations.create_project(
            name=form.cleaned_data['name'], description=form.cleaned_data['description'])

        return shortcuts.redirect('project-detail', pk=project.pk)


class UpdateProject(generic.FormView):
    form_class = forms.UpdateProject
    template_name = 'update-project.html'
    context_object_name = 'project_detail'

    def setup(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> None:
        try:
            self.project = shortcuts.get_object_or_404(
                models.Project, pk=kwargs.get('pk'))
        except models.Project.DoesNotExist:
            return http.HttpResponseNotFound('Project not found')
        return super().setup(request, *args, **kwargs)

    def form_valid(self, form: Any) -> http.HttpResponse:
        project = operations.update_project(self.project,
                                            name=form.cleaned_data['name'], description=form.cleaned_data['description'])

        success_url = self.get_success_url(project)
        return shortcuts.redirect(success_url)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['project'] = self.project
        return kwargs

    def get_success_url(self, project: models.Project) -> str:
        return reverse('project-detail', kwargs={'pk': project.pk})
