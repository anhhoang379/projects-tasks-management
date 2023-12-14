from rest_framework import viewsets
from rest_framework.response import Response

from management.api.serializers import SignUpSerializer


class SignUpViewSet(viewsets.ViewSet):
    serializer_class = SignUpSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "success"})
