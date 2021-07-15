from django.core.checks import messages
import graphene
from graphene_django import DjangoObjectType
import math

#Types
from api.schemas.user.type import UserType

#models
from django.contrib.auth.models import User
from api.models import Post

#Define Types
class MessageType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ['id', 'text', 'created_at']

    postedAt = graphene.String()
    postedBy = graphene.Field(UserType)

    def resolve_postedAt(parent, info):
        return parent.created_at

    def resolve_postedBy(parent, info):
        return User.objects.get(pk=parent.user_id)

class Pageinfo(graphene.ObjectType):
    limit = graphene.Int()
    offset = graphene.Int()
    totalRecords= graphene.Int()
    totalPages = graphene.Int()
    page = graphene.Int()

    def resolve_totalPages(parent, info):
        limit = parent.limit if parent.limit else 1
        return math.ceil(int(parent.totalRecords)/limit)

    def resolve_page(parent, info):
        totalPages = parent.resolve_totalPages(info)
        totalPagesNotZero = totalPages if totalPages else 1
        currentPage = math.ceil(parent.offset/totalPagesNotZero) + 1
        return currentPage if currentPage < totalPages else totalPages

class MessagePageType(graphene.ObjectType):
    pageInfo = graphene.Field(Pageinfo)
    messages = graphene.List(MessageType)