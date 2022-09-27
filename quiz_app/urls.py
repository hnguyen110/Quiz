from rest_framework_nested import routers

from quiz_app.views.base_quiz_view_set import BaseQuizViewSet

router = routers.DefaultRouter()
router.register('quizzes', BaseQuizViewSet, basename='quizzes')

urlpatterns = router.urls
