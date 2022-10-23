import os

import stripe
from rest_framework import serializers

stripe.api_key = os.environ['STRIPE_SECRET_KEY']


class BasePaymentSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    exp_month = serializers.IntegerField(allow_null=False)
    exp_year = serializers.IntegerField(allow_null=False)
    cvc = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)

    def save(self, **kwargs):
        token = stripe.Token.create(
            card={
                'number': self.validated_data['number'],
                'exp_month': self.validated_data['exp_month'],
                'exp_year': self.validated_data['exp_year'],
                'cvc': self.validated_data['cvc'],
            }
        )

        customer = stripe.Customer.create(
            name=self.context['name'],
            email=self.context['email'],
            source=token.id
        )

        stripe.Charge.create(
            amount=self.context['amount'],
            currency=self.context['currency'],
            description=self.context['description'],
            customer=customer
        )

        return None

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
