from django.db import models

from quiz_app.models.question import Question


class QuestionSolution(models.Model):
    description = models.TextField(null=False)
    isCorrect = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='solutions')
