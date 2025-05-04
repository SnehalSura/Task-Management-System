from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET', 'POST'])
def task_list(request):

    """
    task_list function handles fetching all tasks and adding a new task.
    GET: Returns a list of tasks, with optional filtering and sorting.
    POST: Creates a new task with the provided data.

    """

    if request.method == 'GET':
        tasks = Task.objects.all()

        # Optional query params for filtering and sorting
        sort_by_date = request.query_params.get('sort_by_date', None)
        search_date = request.query_params.get('search_date', None)
        search_title = request.query_params.get('search', None)

        if sort_by_date:             # Sort tasks by date
            tasks = tasks.order_by('date')
        if search_date:              # Filter tasks by date
            tasks = tasks.filter(date=search_date)
        if search_title:             # Search tasks by title
            tasks = tasks.filter(title__icontains=search_title)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        # Validate and save a new task
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
def task_detail(request, id):
    """
    task_detail function handles updating or deleting a specific task by ID.
    PATCH: Updates the task with the provided fields.
    DELETE: Deletes the task.
    
    """
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        # Return an error response if the task is not found
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        # Validate and update the task
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        # Delete the task and return a success message
        task.delete()
        return Response({'msg': 'Task deleted'}, status=status.HTTP_204_NO_CONTENT)
