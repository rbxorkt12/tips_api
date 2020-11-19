from django.db import models
from post.models import Post
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pk = models.IntegerField(blank=True)
    email = models.EmailField(max_length=500, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    credit = models.IntegerField(default=800000)
    phone = models.CharField(max_length=200, blank=True)
    KIND_LIST = (
        ('U','Undergraduate'),
        ('G','Graduated')
    )
    user_kind1 = models.CharField(max_length=1, choices=KIND_LIST)
    #학과
    user_kind2 = models.CharField(max_length=20, blank=True)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()