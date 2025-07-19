from django.contrib import admin
from django.urls import path

from .views import (
    IndexView, TagsCreateView, TagsListView,
    TagsUpdateView, TagsDeleteView, TasksListView,
    TasksCreateView, TasksUpdateView, TasksDeleteView
)

app_name = "catalog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    path("create_tag/", TagsCreateView.as_view(), name="create_tag"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("update_tag/<int:pk>/", TagsUpdateView.as_view(), name="update_tag"),
    path("delete_tag/<int:pk>/", TagsDeleteView.as_view(), name="delete_tag"),

    path("create_task/", TasksCreateView.as_view(), name="create_task"),
    path("tasks/", TasksListView.as_view(), name="tasks"),
    path("update_task/<int:pk>/", TasksUpdateView.as_view(), name="update_task"),
    path("delete_task/<int:pk>/", TasksDeleteView.as_view(), name="delete_task"),
]
