from rest_framework import viewsets, status
from .serializers import PostSerializer, RatingSerializer, BuyingSerializer
from .models import Post, Rating, Buying
from users.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from django.shortcuts import get_list_or_404
from .permission import IsOwnerOrReadOnly,NodeletePermission
from knox.auth import TokenAuthentication
from django.contrib.auth.models import User

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    #call by using http://127.0.0.1:8000/api/post/posts/own_post
    @action(methods=['GET'], detail=False)
    def own_post(self,request):
        if str(request.user) == 'AnonymousUser':
            return Response({'message: You have to login first'},status=status.HTTP_401_UNAUTHORIZED)
        queryset = Post.objects.filter(author=request.user)
        serilaizer = PostSerializer(queryset,many=True)
        return Response(serilaizer.data)


    @action(methods=['GET'], detail=True)
    def kind(self,request,pk=None):
        if pk is None :
            return Response({'meesage : Input proper kind option U or G'},status=status.HTTP_400_BAD_REQUEST)
        if str(request.user) == 'AnonymousUser':
            return Response({'message: You have to login first'},status=status.HTTP_401_UNAUTHORIZED)
        queryset = Post.objects.filter(post_kind1=pk)
        serilaizer = PostSerializer(queryset,many=True)
        return Response(serilaizer.data)

    #call by using http://127.0.0.1:8000/api/post/posts/1/rate_post/
    @action(methods=['POST'], detail=True)
    def rate_post(self, request, pk=None):
        if 'stars' in request.data:
            post = Post.objects.get(id=pk)
            stars = request.data['stars']
            comments = request.data['comment']
            user = request.user
            try:
                rating = Rating.objects.get(user=user.id, post=post.id)
                rating.stars = stars
                rating.comments = comments
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating has been updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, post=post, stars=stars, comments=comments)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating has been created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Plz enter stars field'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def buy_post(self, request, pk=None):
        if request.user.id is None :
            return Response({'message' : 'Plz login first'},status.HTTP_401_UNAUTHORIZED)
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=pk)
        profile = Profile.objects.get(user=user_id)
        if profile.credit < post.cost:
            return Response({'message': 'Dont have enought credit'},status.HTTP_402_PAYMENT_REQUIRED)
        buying = Buying.objects.create(post=post,user=user)
        serializer = BuyingSerializer(buying, many=False)
        profile.credit = profile.credit-post.cost
        profile.save()
        response = {'message': f'{request.user} bought {post.id}', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


class BuyingViewset(viewsets.ModelViewSet):
    serializer_class = BuyingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    queryset = Buying.objects.all()
    
    @action(methods=['GET'], detail=False)
    def own_bought(self,request):
        if str(request.user) == 'AnonymousUser':
            return Response({'message: You have to login first'},status=status.HTTP_401_UNAUTHORIZED)
        queryset = Buying.objects.filter(user=request.user)
        serilaizer = BuyingSerializer(queryset,many=True)
        return Response(serilaizer.data)

class RatingViewset(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,NodeletePermission)
    queryset = Rating.objects.all()

    def delete(self, request,*args, **kwargs):
        return Response({'message': 'Not acceptable'}, status.HTTP_406_NOT_ACCEPTABLE)
