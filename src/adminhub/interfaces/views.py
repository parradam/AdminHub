from typing import Any
from django.views import generic
from adminhub.controllers.projects.get_projects import get_all_projects


class Projects(generic.ListView):
    template_name = 'project-list.html'
    context_object_name = 'projects_list'

    def get_queryset(self) -> Any:
        return get_all_projects()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
