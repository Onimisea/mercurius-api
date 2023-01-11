from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Webhook
from .serializers import WebhookSerializer



@csrf_exempt
def webhook(request):
    if request.method == "POST":
        print("Data received from Webhook is: ", request.body)
        return HttpResponse("Webhook received!")

    return HttpResponse("Webhook waiting...")


@csrf_exempt
def WebhookAPIView(request):
    if request.method == "POST":
        print("Data received from Webhook is: ", request.body)
        response = {
            "message": "Webhook Received Successfully",
            "data": request.body,
        }

        return HttpResponse(request.body)
        
    return HttpResponse("Webhook waiting...")


# response = {
#             "title": "Sent webhook",
#             "data": request.data,
#         }

#         return Response(data=response, status=status.HTTP_201_CREATED)

# class WebhookListAPIView(generics.ListAPIView):
#     queryset = Webhook.objects.all()
#     serializer_class = WebhookSerializer


# class WebhookAPIView(generics.GenericAPIView):
#     queryset = Webhook.objects.all()
#     serializer_class = WebhookSerializer
#     lookup_field = 'slug'

#     def post(self, request, *args, **kwargs):
#         print(request.data)
#         response = {
#             "title": "Sent webhook",
#             "data": request.data,
#         }

#         return Response(data=response, status=status.HTTP_201_CREATED)
