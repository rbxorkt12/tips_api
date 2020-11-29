from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=400)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    KIND_LIST = (
        ('U','Undergraduate'),
        ('G','Graduated')
    )
    post_kind1 = models.CharField(max_length=1, choices=KIND_LIST,default='U')
    post_kind2 = models.CharField(max_length=20, blank=True)
 
    def rating_average(self):
        sum=0
        ratings = Rating.objects.filter(post=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) != 0:
            return sum/len(ratings)
        return 0

    def comment_list(self):
        comment_list = []
        ratings = Rating.objects.filter(post=self)
        for rating in ratings:
            comment_list.append(rating.comments)
        return comment_list
    

class Buying(models.Model):
    objects = models.Manager()
    post = models.ForeignKey(Post, related_name="buying",on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="buying",on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'post'),)
        index_together = (('user', 'post'),) 

class Rating(models.Model):
    objects = models.Manager()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.CharField(max_length=50)

    class Meta:
        unique_together = (('user', 'post'),)
        index_together = (('user', 'post'),)
