from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow_me")
    user_followed = models.ForeignKey(User,  on_delete=models.CASCADE, related_name="followed")
    unfollow_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_post")
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    update_at = models.DateTimeField(null=True,blank=True)
    delete_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.text