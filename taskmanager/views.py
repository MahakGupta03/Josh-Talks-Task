from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer

@api_view(['POST'])
def create_user(request):
    """
    API endpoint to create a new user.
    Expects name, email, and mobile in the request body.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_task(request):
    """
    API endpoint to create a new task.
    Expects name and description; other fields are optional or auto-set.
    """
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def assign_task(request, task_id):
    """
    API endpoint to assign a task to one or multiple users.
    Expects a list of user_ids in the request body.
    """
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    user_ids = request.data.get('user_ids', [])
    users = User.objects.filter(id__in=user_ids)
    if len(users) != len(user_ids):
        return Response({"error": "One or more users not found"}, 
                        status=status.HTTP_400_BAD_REQUEST)

    task.assigned_users.add(*users)
    return Response({"message": "Users assigned to task"}, 
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_tasks(request, user_id):
    """
    API endpoint to retrieve all tasks assigned to a specific user.
    """
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    tasks = Task.objects.filter(assigned_users=user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)