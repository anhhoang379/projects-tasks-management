from django.urls import path

from management.api.views import (
    LoginView,
    ProjectDetailView,
    ProjectListCreateView,
    SignUpView,
    TaskDetailView,
    TaskListCreateView,
)

urlpatterns = [
    path("users/signup/", SignUpView.as_view(), name="user-sisnup"),
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
