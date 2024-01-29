from django.test import TestCase
from adminhub.data import models
from adminhub.domain.projects import operations as project_operations
from adminhub.domain.tasks import operations as task_operations


class TestTaskOperations(TestCase):
    def test_task_is_created(self):
        project = project_operations.create_project(
            "Project name", "Project description")
        task = task_operations.create_task(
            "Task name", "Task description", project)

        self.assertIsInstance(project, models.Project)
        self.assertIsInstance(task, models.Task)
        self.assertEqual(task.name, 'Task name')
        self.assertEqual(task.description, 'Task description')
        self.assertEqual(task.project, project)
        self.assertEqual(task.status, 'T')
        self.assertTrue(hasattr(task, 'pk'))

    def test_task_is_updated(self):
        project = project_operations.create_project(
            'Project name', 'Project description')
        task = task_operations.create_task(
            'Task name', 'Task description', project)

        updated_task = task_operations.update_task(
            task, 'Updated task name', 'Updated task description', 'C')

        self.assertIsInstance(project, models.Project)
        self.assertIsInstance(updated_task, models.Task)
        self.assertEqual(updated_task.name, 'Updated task name')
        self.assertEqual(updated_task.description, 'Updated task description')
        self.assertEqual(updated_task.status, 'C')
        self.assertEqual(updated_task.project, project)
        self.assertTrue(hasattr(updated_task, 'pk'))
