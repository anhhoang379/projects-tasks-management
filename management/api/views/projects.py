from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from management.api.permissions import ProjectPermissions
from management.api.serializers import ProjectSerializer
from management.models import Project


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, ProjectPermissions)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, ProjectPermissions)
