from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from catalog.models import Tag


class IndexView(View):
    template_name = "catalog/index.html"

    def get(self, request):
        return render(request, self.template_name)


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
