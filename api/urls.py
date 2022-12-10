from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

# router = routers.SimpleRouter()
# router.register(r"users", UserViews.UserViewSet)
urlpatterns = [
    path("auth/", obtain_auth_token),
    path("", views.api_home),
    path("users/", include("users.urls")),
    path("inventory/", include("inventory.urls")),
    path("webhooks/", include("webhooks.urls")),
]
# urlpatterns += router.urls
