from django.urls import path
from .views import login_views

urlpatterns = [
    path('login',login_views)
]