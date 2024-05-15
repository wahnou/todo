from rest_framework import serializers
from todo import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'completed',
        )
        model = models.Task