import json
from urllib.request import urlopen

from django.conf import settings
from opentracing_instrumentation.request_context import span_in_context
from rest_framework import generics, response

from course_topic_app import serializers, models
from lxp_course_topic_service.settings.base import tracer

tracing = settings.OPENTRACING_TRACING


class CourseTopicListView(generics.ListAPIView):
    """
    Use this endpoint to GET all courses.
    """
    serializer_class = serializers.CourseTopicSerializer
    queryset = models.CourseTopicModel.objects.all()


def get_skills(request):
    url = "http://localhost:8000/api/skills"
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    return data


class GetSkillsForCourseTopicsView(generics.ListAPIView):
    queryset = models.CourseTopicModel.objects.all()

    def get(self, request, *args, **kwargs):
        with tracer.start_span('get_skills') as span:
            span.set_tag('Get Skills', 'Bla bla bla')
            with span_in_context(span):
                data = get_skills(request)
        return response.Response(data)
