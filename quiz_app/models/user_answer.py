from django.db import models

from quiz_app.models.question import Question
from quiz_app.models.question_solution import QuestionSolution
from quiz_app.models.quiz_participant import QuizParticipant


class UserAnswer(models.Model):
    class Meta:
        unique_together = ('question', 'selected_solution', 'participant')

    result = models.FloatField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_solution = models.ForeignKey(QuestionSolution, on_delete=models.CASCADE)
    participant = models.ForeignKey(QuizParticipant, on_delete=models.CASCADE, related_name='answers')
