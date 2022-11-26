from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [
            "name",
            "description",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = [
            "name",
            "description",
            "price",
            "image",
        ]


class DonantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Donant
        fields = [
            "name",
            "amount",
            "visible",
        ]
