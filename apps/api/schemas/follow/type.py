import graphene 
from graphene_django import DjangoObjectType
from api.models import Follow

#Define Types
class FollowType(DjangoObjectType):
    class Meta:
        model = Follow
        fields = "__all__"

