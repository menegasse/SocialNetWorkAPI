import graphene

#Types
from .type import MessagePageType, Pageinfo

#Models
from api.models import Post

from ..follow.query import get_following_users_id

class Query(graphene.ObjectType):
    feed = graphene.Field(MessagePageType, limit=graphene.Int(), offset=graphene.Int())

    def resolve_feed(self, info, limit, offset) -> MessagePageType:
        user_authenticated = info.context.user

        following_users_id = get_following_users_id(user_authenticated.id)

        messages = Post.objects.filter(user_id__in=following_users_id).order_by('-created_at')

        totalRecords = messages.count()

        pageInfo = Pageinfo(limit=limit, offset=offset, totalRecords=totalRecords)

        return MessagePageType(pageInfo=pageInfo, messages=messages[offset:offset+limit])