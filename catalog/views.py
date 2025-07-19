from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from catalog.models import Tag, Task


class IndexView(View):
    template_name = "catalog/index.html"

    def get(self, request):
        return render(request, self.template_name)

### > TagsViews < ###
class TagsCreateView(CreateView):
    model = Tag
    template_name = "catalog/tags_date.html"
    context_object_name = "tags"
    fields = "__all__"
    success_url = reverse_lazy("catalog:tags")


class TagsListView(ListView):
    model = Tag
    template_name = "catalog/tags_list.html"
    context_object_name = "tags"


class TagsUpdateView(UpdateView):
    model = Tag
    template_name = "catalog/tags_date.html"
    context_object_name = "tags"
    fields = "__all__"
    success_url = reverse_lazy("catalog:tags")


class TagsDeleteView(DeleteView):
    model = Tag
    template_name = "catalog/tags_date.html"
    context_object_name = "tags"
    success_url = reverse_lazy("catalog:tags")

### > TasksViews < ###
class TasksCreateView(CreateView):
    model = Task
    template_name = "catalog/tasks_date.html"
    context_object_name = "tasks"
    fields = "__all__"
    success_url = reverse_lazy("catalog:tasks")


class TasksListView(ListView):
    model = Task
    template_name = "catalog/tasks_list.html"
    context_object_name = "tasks"


class TasksUpdateView(UpdateView):
    model = Task
    template_name = "catalog/tasks_date.html"
    context_object_name = "tasks"
    fields = "__all__"
    success_url = reverse_lazy("catalog:tasks")

class TasksDeleteView(DeleteView):
    model = Task
    template_name = "catalog/tasks_delete.html"
    context_object_name = "tasks"
    success_url = reverse_lazy("catalog:tasks")