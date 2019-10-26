from django.db import models


# Create your models here.

class Question(models.Model):
    question_name = models.CharField(max_length=200)
    published_at = models.DateTimeField


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_tex = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

