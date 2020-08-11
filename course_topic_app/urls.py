from django.urls import path

from course_topic_app import views


urlpatterns = [
    path('course-topics', views.CourseTopicListView.as_view(), name='list-course-topics')
]
