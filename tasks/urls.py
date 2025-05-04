from django.urls import path
from .views import task_list, task_detail

urlpatterns = [
    path('tasks/', task_list, name='task-list'),  # List and create tasks
    path('tasks/<int:id>/', task_detail, name='task-detail'),  # Retrieve, update, or delete a specific task
]

# For Testing the API:
# - Use "/tasks/" for listing all tasks (GET) or creating a new task (POST).
# - Use "/tasks/<id>/" for updating (PATCH), or deleting (DELETE) a specific task.

