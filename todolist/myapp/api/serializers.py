# myapp/api/serializers.py
from rest_framework import serializers
from myapp.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["name", "priority", "creation_date", "end_date", "status", "description"]

