from django.test import SimpleTestCase
from course_topic_app.models import CourseTopicModel


class TestCourseTopics(SimpleTestCase):
    def setUp(self):
        self.course_topic = CourseTopicModel(name="Title", description="text", synonyms="Lorem Ipsum")

    def test_title(self):
        self.assertEqual(self.course_topic.name, "Title")
