from django.db import models

from quiz_app.models.quiz import Quiz


class Question(models.Model):
    type = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
