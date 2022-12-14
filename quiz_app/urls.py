from rest_framework_nested import routers

from quiz_app.views.course.base_course_view_set import BaseCourseViewSet
from quiz_app.views.course_participant.base_course_participant_view_set import BaseCourseParticipantViewSet
from quiz_app.views.course_section.base_course_section_view_set import BaseCourseSectionViewSet
from quiz_app.views.course_section_item.base_course_section_item_view_set import BaseCourseSectionItemViewSet
from quiz_app.views.question.base_question_view_set import BaseQuestionViewSet
from quiz_app.views.question_solution.base_question_solution_view_set import BaseQuestionSolutionViewSet
from quiz_app.views.quiz.base_quiz_view_set import BaseQuizViewSet
from quiz_app.views.quiz_participant.base_quiz_participant_view_set import BaseQuizParticipantViewSet
from quiz_app.views.quiz_participant.create_quiz_participants_view_set import CreateQuizParticipantsViewSet
from quiz_app.views.user_answer.base_user_answer_view_set import BaseUserAnswerViewSet

router = routers.DefaultRouter()
router.register('quizzes', BaseQuizViewSet, basename='quizzes')
router.register('courses', BaseCourseViewSet, basename='courses')

quiz_router = routers.NestedDefaultRouter(router, 'quizzes', lookup='quiz')
quiz_router.register('questions', BaseQuestionViewSet, basename='quiz-questions')
quiz_router.register('participants', BaseQuizParticipantViewSet, basename='quiz-participants')
quiz_router.register('assign-participants', CreateQuizParticipantsViewSet, basename='assign-participants')

question_router = routers.NestedDefaultRouter(quiz_router, 'questions', lookup='question')
question_router.register('solutions', BaseQuestionSolutionViewSet, basename='question-solutions')

participant_router = routers.NestedDefaultRouter(quiz_router, 'participants', lookup='participant')
participant_router.register('answers', BaseUserAnswerViewSet, basename='participant-answers')
# participant_router.register('results', BaseQuizResultViewSet, basename='participant-quiz-results')

course_router = routers.NestedDefaultRouter(router, 'courses', lookup='course')
course_router.register('sections', BaseCourseSectionViewSet, basename='course-sections')
course_router.register('participants', BaseCourseParticipantViewSet, basename='course-participants')

section_router = routers.NestedDefaultRouter(course_router, 'sections', lookup='section')
section_router.register('items', BaseCourseSectionItemViewSet, basename='section-items')

urlpatterns = router.urls \
              + quiz_router.urls \
              + question_router.urls \
              + participant_router.urls \
              + course_router.urls \
              + section_router.urls
