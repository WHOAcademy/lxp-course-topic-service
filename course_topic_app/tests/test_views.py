from django.urls import reverse
from rest_framework.test import APITestCase

from course_topic_app.models import CourseTopicModel


class TestSkillView(APITestCase):

    def test_get_all(self):

        topic_1 = CourseTopicModel.objects.create(name='Topic name', description='Topic description', synonyms='python')
        topic_2 = CourseTopicModel.objects.create(name='Topic name', description='Topic description', synonyms='python',
                                                  parent=topic_1)

        url = reverse("list-course-topics")
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        self.assertEquals(topic_1.name, response.data[0]["name"])
        self.assertEquals(topic_1.description, response.data[0]["description"])
        self.assertEquals(topic_1.synonyms, response.data[0]["synonyms"])
        self.assertTrue(response.data[0].get("parent") is None)

        self.assertEquals(topic_2.name, response.data[1]["name"])
        self.assertEquals(topic_2.description, response.data[1]["description"])
        self.assertEquals(topic_2.synonyms, response.data[1]["synonyms"])
        self.assertTrue(response.data[1].get("parent") is not None)
