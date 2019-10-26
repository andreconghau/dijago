from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_name = models.CharField(max_length=200)
    published_at = models.DateTimeField(default=timezone.now())
    author = models.CharField(max_length=200, default='')
    ordering = models.IntegerField(default=0)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_tex = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

