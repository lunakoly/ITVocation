from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    """
    Task serializer
    """
    published = serializers.DateTimeField()
    header = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=2000)
    exp = serializers.IntegerField()
    status = serializers.IntegerField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.header = validated_data.get('header', instance.header)
        instance.save()
        return instance
