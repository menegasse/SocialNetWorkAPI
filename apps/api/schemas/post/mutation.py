import graphene 

#Types
from .type import MessageType

#Models
from django.contrib.auth.models import User 
from api.models import Post


class PostMessage(graphene.Mutation):
    class Arguments:
        text = graphene.String()

    success = graphene.Boolean()
    errorMessage = graphene.String()
    message = graphene.Field(MessageType)

    @staticmethod
    def mutate(root, info, text):
        user_authenticated = info.context.user

        try:
            post = Post(
                user_id = user_authenticated.id,
                text = text
            )

            post.save()
            success = True
        except:
            success = False
            error_message = "Failed to post the message"

        return PostMessage(message=post, success=success, errorMessage= None if success else error_message)

class Mutation(graphene.ObjectType):
    postMessage = PostMessage.Field()