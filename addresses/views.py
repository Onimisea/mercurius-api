from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView, api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Address
from .serializers import AddressSerializer


class AddressListAPIView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailAPIView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "id"


@api_view(http_method_names=["PUT"])
def UpdateAddressAPIView(request:Request, pk):
    address = get_object_or_404(Address, pk=pk)
    data = request.data
    serializer = AddressSerializer(instance=address, data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "success": "Address Updated Successfully",
            "data": serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)
    

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)