from django.urls import path

from . import views

urlpatterns = [
    path("", views.WebhookListAPIView.as_view()),
    path("<str:slug>/", views.WebhookAPIView.as_view()),
]
