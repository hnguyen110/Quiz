from django.core.mail import send_mail
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

from . import question
from . import question_solution
from . import quiz
from . import quiz_participant
from . import user_answer


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    send_mail(
        "Reset Password",
        reset_password_token.key,
        "administrator@quiz.com",
        [reset_password_token.user.email]
    )
