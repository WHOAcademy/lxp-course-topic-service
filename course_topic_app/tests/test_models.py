from django.db import DataError
from django.test import TestCase

from course_topic_app.models import CourseTopicModel


class TestCourseTopicModel(TestCase):

    @staticmethod
    def _create_course_topic():
        return CourseTopicModel.objects.create(name="Title", description="description", synonyms='example')

    def test_create_course_topic(self):
        topic_1 = self._create_course_topic()
        CourseTopicModel.objects.create(name="Title", description="description", synonyms='example', parent=topic_1)

    def test_get_all(self):
        self._create_course_topic()
        self._create_course_topic()
        self._create_course_topic()

        roles = CourseTopicModel.objects.all()
        self.assertEqual(len(roles), 3)

    def test_role_obj(self):
        topic_1 = self._create_course_topic()
        CourseTopicModel.objects.create(name="Title", description="description", synonyms='example', parent=topic_1)

        topic = CourseTopicModel.objects.all()[1]
        self.assertTrue(isinstance(topic, CourseTopicModel))
        self.assertEqual(topic.name, "Title")
        self.assertEqual(topic.description, "description")
        self.assertEqual(topic.synonyms, "example")
        self.assertTrue(topic.parent)

    def test_name_max_length(self):
        with self.assertRaises(DataError):
            title = "This is a test This is a test This is a test This is a test "
            CourseTopicModel.objects.create(name=title, description="description", synonyms='example')

    def test_slug_max_length(self):
        with self.assertRaises(DataError):
            synonyms = "This is a test This is a test This is a test This is a test This is a test This is a test " \
                       "This is a test This is a test This is a test This is a test This is a test This is a test " \
                       "This is a test This is a test This is a test "
            CourseTopicModel.objects.create(name='title', description="description", synonyms=synonyms)
