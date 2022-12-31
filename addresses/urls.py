from django.urls import path

from . import views

urlpatterns = [
    path("", views.AddressListAPIView.as_view()),
    path("update/<str:id>/", views.UpdateAddressAPIView.as_view()),
    # path("delete/<str:id>/", views.DeleteAddressAPIView.as_view()),
    path("<str:id>/", views.AddressDetailAPIView.as_view()),
]
