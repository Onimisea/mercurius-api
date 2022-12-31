from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from users.serializers import UpdateUserSerializer

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
    
    # user = serializers.StringRelatedField()
    user = UpdateUserSerializer()
    
    def update(self, instance, validated_data):
        instance.house_no = validated_data.get('house_no', instance.house_no)
        instance.street_name = validated_data.get('street_name', instance.street_name)
        instance.bus_stop = validated_data.get('bus_stop', instance.bus_stop)
        instance.lga = validated_data.get('lga', instance.lga)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)

        instance.save()

        return instance


# class UpdateUserSerializer(serializers.ModelSerializer):
#     fullname = serializers.CharField(max_length=100)
#     email = serializers.CharField(max_length=60)
#     phone = serializers.CharField(max_length=14)
#     gender = serializers.CharField(max_length=6)
#     dob = serializers.DateField(format=f"%d/%m/%Y", input_formats=[f"%d/%m/%Y",])

#     class Meta:
#         model = User
#         fields = ["fullname", "email", "phone", "gender", "dob"]
    
    # def update(self, instance, validated_data):
    #     instance.fullname = validated_data.get('fullname', instance.fullname)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.dob = validated_data.get('dob', instance.dob)

    #     instance.save()

    #     return instance