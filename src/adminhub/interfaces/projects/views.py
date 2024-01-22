from typing import Any
from django import http
from django.views import generic
from django import shortcuts
from adminhub.domain.projects import queries
from adminhub.domain.projects import operations
from adminhub.domain.tasks import queries as task_queries
from adminhub.domain.tasks import operations as task_operations
from . import forms
from . import forms as project_forms
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


class Project(generic.FormView):
    template_name = 'project-detail.html'
    form_class = project_forms.CreateProjectTask

    def setup(self, request: http.HttpRequest, *args, **kwargs) -> None:
        super().setup(request, *args, **kwargs)

        self.project: models.Project = shortcuts.get_object_or_404(
            models.Project, pk=self.kwargs['pk'])
        self.tasks = task_queries.get_tasks_for_project(self.project)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        create_project_task_form = project_forms.CreateProjectTask()

        context['project'] = self.project
        context['tasks'] = self.tasks
        context['create_project_task_form'] = create_project_task_form

        return context

    def form_valid(self, form) -> http.HttpResponse:
        task = task_operations.create_task(
            name=form.cleaned_data['name'], description=form.cleaned_data['description'], project=self.project)

        success_url = self.get_success_url()
        return shortcuts.redirect(success_url)

    def get_success_url(self) -> str:
        return reverse('project-detail', kwargs={'pk': self.project.pk})


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
