from rest_framework import generics

from course_topic_app import serializers, models


class CourseTopicListView(generics.ListAPIView):
    """
    Use this endpoint to GET all courses.
    """
    serializer_class = serializers.CourseTopicSerializer
    queryset = models.CourseTopicModel.objects.all()
