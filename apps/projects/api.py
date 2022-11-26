from rest_framework import viewsets, permissions

from . import models
from . import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Project class"""

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class DonantViewSet(viewsets.ModelViewSet):
    """ViewSet for the Donant class"""

    queryset = models.Donant.objects.all()
    serializer_class = serializers.DonantSerializer
    permission_classes = [permissions.IsAuthenticated]
