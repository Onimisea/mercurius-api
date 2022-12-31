from django.urls import path

from . import views

urlpatterns = [
    path("", views.AddressListAPIView.as_view()),
    path("<str:id>/", views.AddressDetailAPIView.as_view()),
    # path("delete/<str:id>/", views.DeleteUserAPIView.as_view()),
]
