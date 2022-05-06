from .models import *
from rest_framework import serializers

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class LessonMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'