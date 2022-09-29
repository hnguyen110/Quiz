from rest_framework.permissions import BasePermission

from quiz_app.models.quiz_participant import QuizParticipant


class IsQuizParticipant(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        participant = QuizParticipant \
            .objects \
            .filter(pk=view.kwargs['participant_pk']) \
            .first()
        return participant is not None and participant.user == request.user

    # def has_object_permission(self, request, view, obj):
    #     return obj.participant.user == request.user
