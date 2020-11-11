from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, RatingViewset

router = routers.DefaultRouter()
router.register('posts',PostViewSet)
router.register('ratings',RatingViewset)

urlpatterns = [
    path('',include(router.urls))
]
