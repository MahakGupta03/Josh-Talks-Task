from django.urls import path
from .views import create_user, create_task, assign_task, get_user_tasks

urlpatterns = [
    path('api/users/', create_user, name='create_user'),
    path('api/tasks/', create_task, name='create_task'),
    path('api/tasks/<int:task_id>/assign/', assign_task, name='assign_task'),
    path('api/users/<int:user_id>/tasks/', get_user_tasks, name='get_user_tasks'),
]