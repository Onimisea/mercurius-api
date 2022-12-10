from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Webhook
from .serializers import WebhookSerializer


class WebhookListAPIView(generics.ListAPIView):
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer


class WebhookAPIView(generics.GenericAPIView):
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer
    lookup_field = 'slug'

    def post(self, request, *args, **kwargs):
        print(request.data)
        response = {
            "title": "Sent webhook",
            "data": request.data,
        }

        return Response(data=response, status=status.HTTP_201_CREATED)
