from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITests(TestCase):
    def setUp(self):
        """
        Creating an API client and some sample tasks for testing.
        """
        self.client = APIClient()
        self.task1 = Task.objects.create(title="Task 1", description="Description 1", completed=False)
        self.task2 = Task.objects.create(title="Task 2", description="Description 2", completed=True)
        self.task_list_url = "/tasks/"
        self.task_detail_url = f"/tasks/{self.task1.id}/"

    def test_get_task_list(self):
        """
        Test fetching the list of tasks.
        """
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], "Task 1")

    def test_create_task(self):
        """
        Test creating a new task via POST.
        """
        data = {"title": "New Task", "description": "New Description", "completed": False}
        response = self.client.post(self.task_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.last().title, "New Task")

    def test_update_task(self):
        """
        Test updating an existing task using PATCH.
        """
        data = {"title": "Updated Task"}
        response = self.client.patch(self.task_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, "Updated Task")

    def test_delete_task(self):
        """
        Test deleting a task using DELETE.
        """
        response = self.client.delete(self.task_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)
