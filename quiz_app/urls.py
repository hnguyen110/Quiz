from rest_framework_nested import routers

from quiz_app.views.question.base_question_view_set import BaseQuestionViewSet
from quiz_app.views.quiz.base_quiz_view_set import BaseQuizViewSet

router = routers.DefaultRouter()
router.register('quizzes', BaseQuizViewSet, basename='quizzes')

quiz_router = routers.NestedDefaultRouter(router, 'quizzes', lookup='quiz')
quiz_router.register('questions', BaseQuestionViewSet, basename='quiz-questions')

urlpatterns = router.urls + quiz_router.urls
