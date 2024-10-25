from django.urls import path
from .views import PendingList, DetailTask, CreateTask, EditTask, DeleteTask


urlpatterns = [path('', PendingList.as_view(), name='pending'),
               path('task/<int:pk>', DetailTask.as_view(), name='task'),
               path('create-task/', CreateTask.as_view(), name='create-task'),
               path('edit-task/<int:pk>', EditTask.as_view(), name='edit-task'),
               path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task')]
