# flake8: noqa
from .login import LoginView
from .projects import ProjectListCreateView
from .tasks import TaskDetailView, TaskListCreateView

__all__ = [
    "LoginView",
    "ProjectListCreateView",
    "TaskListCreateView",
    "TaskDetailView",
]
