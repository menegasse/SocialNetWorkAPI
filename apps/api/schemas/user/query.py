import graphene
from django.contrib.auth.models import User
from .type import UserType

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    #Resolvers
    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, id):
        
        try:
            return User.objects.get(pk=id)
        except:
            return None


         

