from django.conf import settings
from django.db import models

from quiz_app.models.quiz import Quiz


class QuizParticipant(models.Model):
    class Meta:
        unique_together = ('user', 'quiz')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='participants')
    isComplete = models.BooleanField(default=False)
