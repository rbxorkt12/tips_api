from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Post,Rating,Buying


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class BuyingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buying
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    buying = BuyingSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('comment_list','title','content','author','rating_average','post_kind1','post_kind2','cost','buying')