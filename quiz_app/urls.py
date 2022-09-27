from rest_framework_nested import routers

from quiz_app.views.question.base_question_view_set import BaseQuestionViewSet
from quiz_app.views.question_solution.base_question_solution_view_set import BaseQuestionSolutionViewSet
from quiz_app.views.quiz.base_quiz_view_set import BaseQuizViewSet
from quiz_app.views.quiz_participant.base_quiz_participant_view_set import BaseQuizParticipantViewSet

router = routers.DefaultRouter()
router.register('quizzes', BaseQuizViewSet, basename='quizzes')

quiz_router = routers.NestedDefaultRouter(router, 'quizzes', lookup='quiz')
quiz_router.register('questions', BaseQuestionViewSet, basename='quiz-questions')
quiz_router.register('participants', BaseQuizParticipantViewSet, 'quiz-participants')

question_router = routers.NestedDefaultRouter(quiz_router, 'questions', lookup='question')
question_router.register('solutions', BaseQuestionSolutionViewSet, basename='question-solutions')

urlpatterns = router.urls + quiz_router.urls + question_router.urls
