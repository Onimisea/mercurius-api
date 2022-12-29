from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=60)
    phone = serializers.CharField(max_length=11)
    gender = serializers.CharField(max_length=6)
    dob = serializers.DateField(format=["%d/%m/%Y"], input_formats=["%d/%m/%Y"])
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        phone_exists = User.objects.filter(phone=attrs['phone']).exists()
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Email has already been registered")
        if phone_exists:
            raise ValidationError("Phone Number has already been registered")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)

        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user


class VerifyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UpdateUserSerializer(serializers.ModelSerializer):
    
    fullname = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=60)
    phone = serializers.CharField(max_length=11)
    gender = serializers.CharField(max_length=6)
    dob = serializers.DateField(format=["%d/%m/%Y"], input_formats=["%d/%m/%Y"])

    class Meta:
        model = User
        fields = ["fullname", "email", "phone", "gender", "dob"]
