from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


# class UpdateUserSerializer(serializers.ModelSerializer):
#     fullname = serializers.CharField(max_length=100)
#     email = serializers.CharField(max_length=60)
#     phone = serializers.CharField(max_length=14)
#     gender = serializers.CharField(max_length=6)
#     dob = serializers.DateField(format=f"%d/%m/%Y", input_formats=[f"%d/%m/%Y",])

#     class Meta:
#         model = User
#         fields = ["fullname", "email", "phone", "gender", "dob"]
    
#     def update(self, instance, validated_data):
#         instance.fullname = validated_data.get('fullname', instance.fullname)
#         instance.email = validated_data.get('email', instance.email)
#         instance.phone = validated_data.get('phone', instance.phone)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.dob = validated_data.get('dob', instance.dob)

#         instance.save()

#         return instance