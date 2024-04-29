# serializers.py
from rest_framework import serializers
from .models import AndroidApp, Task, TaskCompletion

class AndroidAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCompletion
        fields = '__all__'
