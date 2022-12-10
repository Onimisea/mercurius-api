from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserListCreateAPIView.as_view()),
    path("register/", views.CreateUserAPIView.as_view(), name="register"),
    path("login/", views.LoginUserAPIView.as_view(), name="login"),
    path("delete/<str:id>/", views.DeleteUserAPIView.as_view()),
    path("verify/", views.VerifyUserAPIView.as_view()),
    path("<str:id>/", views.UserDetailAPIView.as_view()),
]
