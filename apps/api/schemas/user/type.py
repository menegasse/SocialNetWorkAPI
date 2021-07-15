import graphene
from graphene_django import DjangoObjectType 
from django.contrib.auth.models import User
from api.models import Follow

#Define Types
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['id', 'username']

    followsCount = graphene.Int()
    followersCount = graphene.Int() 
    name= graphene.String()

    def resolve_name(parent, info):
        return parent.username

    def resolve_followsCount(parent, info):
        return Follow.objects.filter(user_id=parent.id, unfollow_at__isnull=True).count()

    def resolve_followersCount(parent, info):
        return Follow.objects.filter(user_followed_id=parent.id, unfollow_at__isnull=True).count()
   