from rest_framework.permissions import BasePermission

from quiz_app.models.course_participant import CourseParticipant


class IsCourseParticipant(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        elif request.user.is_staff:
            return True
        participant = CourseParticipant \
            .objects \
            .filter(course_id=view.kwargs['course_pk'] if 'course_pk' in view.kwargs else view.kwargs['pk']) \
            .first()
        return participant is not None and participant.user == request.user
