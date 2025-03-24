from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model, handling user data.
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model, handling task data.
    Includes assigned_users as a list of user IDs.
    """
    assigned_users = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 
                  'completed_at', 'status', 'assigned_users']