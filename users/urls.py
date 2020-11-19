from django.urls import path
from .views import ProfileUpdateAPI, RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path("auth/profile/update/", ProfileUpdateAPI.as_view()),
]