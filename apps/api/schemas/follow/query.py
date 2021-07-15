import graphene
from api.schemas.user.type import UserType
from django.contrib.auth.models import User


def get_following_users_id(user_id: int):
    if user_id:
        following = User.objects.get(pk=user_id).follow_me.filter(unfollow_at__isnull=True)
        return [follow.user_followed_id for follow in following]
    return None

class Query(graphene.ObjectType):
    followsMe = graphene.List(UserType)
    following = graphene.List(UserType)

    #Resolvers
    def resolve_followsMe(self, info, **kwargs):
        user_authenticated = info.context.user

        try:
            followers = User.objects.get(pk=user_authenticated.id).followed.filter(unfollow_at__isnull=True)
            follwers_id = [follow.user_id for follow in followers]
            followers_user = User.objects.filter(pk__in=follwers_id)
        except:
            followers_user = None

        return followers_user


    def resolve_following(self, info, **kwargs):
        user_authenticated = info.context.user

        try:
            following_users_id = get_following_users_id(user_authenticated.id)
            following_users = User.objects.filter(pk__in=following_users_id)
        except:
            following_users = None

        return following_users

        

