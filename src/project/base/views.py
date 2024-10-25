from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class PendingList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task_list.html'

class DetailTask(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/detail_task.html'


class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('pending')
    # When we get a successful event it goes to the URL named "pending" check in urls.py


class EditTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('pending')


class DeleteTask(DeleteView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_deleted.html'
    success_url = reverse_lazy('pending')