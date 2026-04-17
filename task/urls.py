from django.urls import path,include
from .views import index, task_list, create, delete_task, edit_task

urlpatterns = [
    path('', task_list, name='index'),
    path('create', create, name="create"),
    path('edit/<int:id>', edit_task, name='edit'),
    path('delete/<int:id>/', delete_task, name="delete"),
    path('accounts/',include('django.contrib.auth.urls') )
]
