from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView, api_view
from rest_framework.request import Request
from rest_framework.response import Response

from users.models import User

from .models import Address
from .serializers import AddressSerializer, UpdateAddressSerializer


class AddressListAPIView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@api_view(http_method_names=["POST"])
def AddAddressAPIView(request: Request):

    if request.method == "POST":
        data = request.data
        serializer = AddressSerializer(data=data)

        user_id = request.data.get("user")
        user = User.objects.get(pk=user_id)

        
        Address.objects.all().filter(user=user).filter(is_default=True).update(is_default=False)
        

        if serializer.is_valid():
            serializer.save(user=user)

            response = {
                "success": "Address Added Successfully",
                "address": serializer.data,
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE
        )


class AddressDetailAPIView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "id"


@api_view(http_method_names=["PUT"])
def UpdateAddressAPIView(request: Request, pk):
    address = get_object_or_404(Address, pk=pk)
    user_id = request.data.get("user")
    user = get_object_or_404(User, pk=user_id)
    data = request.data
    serializer = UpdateAddressSerializer(instance=address, data=data)

    if serializer.is_valid():
        serializer.save(user=user)

        response = {
            "success": "Address Updated Successfully",
            "data": serializer.data,
        }

        return Response(data=response, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def DeleteAddressAPIView(request: Request, pk):
    address = get_object_or_404(Address, pk=pk)

    address.delete()

    response = {
        "success": "Address Deleted Successfully",
    }

    print(response)

    return Response(data=response, status=status.HTTP_204_NO_CONTENT)
