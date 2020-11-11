from rest_framework import serializers
from .models import Post,Rating


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('comment_list','title','content','author','rating_average',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
