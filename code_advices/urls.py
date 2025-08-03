from django.urls import path
from .views import ChangeLogListCreateView, ChangeLogCreateView

urlpatterns = [
    path("changelogs/", ChangeLogListCreateView.as_view(), name="changelog-list-create"),
    path("changelogs/create/", ChangeLogCreateView.as_view(), name="changelog-create"),
]
