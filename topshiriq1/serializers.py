from django.forms import CharField
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from topshiriq1.models import Account, Vacancy


class AccountSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError("Passwords must be match")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        account: Account = super().create(validated_data)
        account.set_password(validated_data["password"])
        account.save()
        return account

    class Meta:
        model = Account
        fields = (
            "id",
            "username",
            "email",
            "password",
            "password2",
            "first_name",
            "last_name",
            "phone",
        )
        extra_kwargs = {
            "email": {"required": True, "allow_null": False},
            "first_name": {"required": True, "allow_null": False},
            "last_name": {"required": True, "allow_null": False},
            "phone": {"required": True, "allow_null": False},
        }


class LoginSerializer(serializers.Serializer):
    username = CharField()
    password = CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        if username and password:
            user = get_object_or_404(Account, username=username)
            if user.check_password(password):
                return attrs
            return user
        else:
            raise serializers.ValidationError("Username or password is invalid")


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ("name","salary")
