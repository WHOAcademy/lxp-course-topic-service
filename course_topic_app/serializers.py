from rest_framework import serializers
from .models import CourseTopicModel


class CourseTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTopicModel
        fields = '__all__'
        depth = 1
