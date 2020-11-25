from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, RatingViewset,BuyingViewset

router = routers.DefaultRouter()
router.register('posts',PostViewSet)
router.register('ratings',RatingViewset)
router.register('buyings',BuyingViewset)

urlpatterns = [
    path('',include(router.urls))
]
