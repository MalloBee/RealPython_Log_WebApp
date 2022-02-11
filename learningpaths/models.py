from django.db import models


# Create your models here.
class LearningPath(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)


class Course(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField()
    learning_path = models.ForeignKey(LearningPath, on_delete=models.CASCADE)
