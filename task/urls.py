from django.urls import path
from .views import index, task_list, create, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', task_list, name='tasks'),
    path('create', create, name="create"),
    path('delete/<int:id>/', delete_task, name="delete"),
]
