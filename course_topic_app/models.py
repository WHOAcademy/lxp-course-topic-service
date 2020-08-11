from django.db import models


class CourseTopicModel(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    synonyms = models.CharField(max_length=100)
    parent = models.ForeignKey(to='self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
