from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.Projects.as_view(), name='project-list'),
    path('projects/new',
         views.CreateProject.as_view(), name='create-project'),
    path('projects/change/<int:pk>/',
         views.UpdateProject.as_view(), name='update-project'),
    path('projects/<int:pk>',
         views.Project.as_view(), name='project-detail'),
    path('projects/confirm-delete/<int:pk>', views.ConfirmDeleteProject.as_view(),
         name='confirm-delete-project'),
    path('projects/delete/<int:pk>', views.DeleteProject.as_view(),
         name='delete-project'),
    path('tasks/change/<int:pk>/',
         views.UpdateProjectTask.as_view(), name='update-project-task'),
    path('tasks/delete/<int:pk>', views.DeleteProjectTask.as_view(),
         name='delete-project-task'),
]
