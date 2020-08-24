from django.urls import path

from course_topic_app import views


urlpatterns = [
    path('course-topics', views.CourseTopicListView.as_view(), name='list-course-topics'),
    path('get-skills-for-course-topics', views.GetSkillsForCourseTopicsView.as_view(),
         name='get-skills-for-course-topics')
]
