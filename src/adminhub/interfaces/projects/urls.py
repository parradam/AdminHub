from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.Projects.as_view(), name='project-list'),
    path('projects/new',
         views.CreateProject.as_view(), name='create-project'),
    path('projects/<int:pk>',
         views.Project.as_view(), name='project-detail'),
]