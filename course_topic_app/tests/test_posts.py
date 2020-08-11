from django.test import SimpleTestCase
from course_topic_app.models import CourseTopicModel


class TestCourse(SimpleTestCase):
    def setUp(self):
        #TODO: fix this
        self.course = CourseTopicModel(title="Title", description="text")

    def test_title(self):
        self.assertEqual(self.course.title, "Title")
