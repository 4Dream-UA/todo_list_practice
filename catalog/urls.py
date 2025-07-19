from django.contrib import admin
from django.urls import path

from .views import IndexView, TagsCreateView, TagsListView, TagsUpdateView, TagsDeleteView

app_name = "catalog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create_tag/", TagsCreateView.as_view(), name="create_tag"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("update_tag/<int:pk>/", TagsUpdateView.as_view(), name="update_tag"),
    path("delete_tag/<int:pk>/", TagsDeleteView.as_view(), name="delete_tag"),
]
