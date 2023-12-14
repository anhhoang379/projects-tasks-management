from django.urls import path

from management.api.views import (
    LoginView,
    ProjectDetailView,
    ProjectListCreateView,
    TaskDetailView,
    TaskListCreateView,
)

urlpatterns = [
    # path('users/register/', UserCreateView.as_view(), name='user-register'),
    path("users/login/", LoginView.as_view(), name="user-login"),
    path(
        "projects/",
        ProjectListCreateView.as_view(),
        name="project-list-create",
    ),
    path(
        "projects/<int:pk>/",
        ProjectDetailView.as_view(),
        name="project-detail",
    ),
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
