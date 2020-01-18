from rest_framework import serializers
from butter.models import User, UserTermsAgreement
from django.contrib.auth import authenticate
from rest_framework.response import Response
from butter.constants import agreement


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,
                                     min_length=8,
                                     write_only=True)
    token = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            "id",
            "email", "street", "post_code", "first_name", "last_name", "password",
            "token"
        )

    def create(self, validated_data):
        created_user = User.objects.create_user(**validated_data)
        if created_user:
            new_agreement = agreement.format(
            created_user.first_name, created_user.last_name, created_user.street, created_user.post_code, created_user.date_joined)
            signed_agreement = UserTermsAgreement(
                signed_user=created_user, signed_agreement=new_agreement)
            signed_agreement.save()
        return created_user


class UserTermsAgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTermsAgreement
        fields = [
            "signed_aggreement"
        ]
