import graphene 
from datetime import datetime

#Models
from api import models 
from django.contrib.auth.models import User

class FollowMutationInterface(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errorMessage = graphene.String()


    @staticmethod
    def mutate(root, info, **args):
        pass

    @classmethod
    def data_validation(cls, user_authenticated: User, use_id_to_follow: int) -> str:
        '''Return message error'''

        if int(user_authenticated.id) == int(use_id_to_follow):
            return f'You can\'t {cls.__name__.lower()} yourself'

        user_to_follow_exist = User.objects.filter(pk=use_id_to_follow)

        if(not user_to_follow_exist):
            return f"User to {cls.__name__.lower()}ed don't exist"

        return None

class Follow(FollowMutationInterface):
    
    @staticmethod
    def mutate(root, info, id):
        user_authenticated = info.context.user  

        try:      
            error_message = Follow.data_validation(user_authenticated, id)

            success = not error_message

            if(success):

                is_already_follow_user = models.Follow.objects.filter(user_followed_id= id,
                                                        user_id= user_authenticated.id)
                
                if is_already_follow_user:
                    is_already_follow_user.update(unfollow_at=None)
                else:
                    follow_user = models.Follow(user_followed_id= id,
                                                user_id= user_authenticated.id)
                    follow_user.save()
            return Follow(success= success, errorMessage=error_message)
        except:
            return Follow(success=False, errorMessage='Failed to follow the user')
        
class Unfollow(FollowMutationInterface):
    
    @staticmethod
    def mutate(root, info, id):
        user_authenticated = info.context.user

        try:     
            error_message = Unfollow.data_validation(user_authenticated, id)

            success = not error_message

            if(success):   
                follow_user = models.Follow.objects.get(user_followed_id= id,
                                                        user_id= user_authenticated.id,
                                                        unfollow_at__isnull=True)

                follow_user.unfollow_at = datetime.now()

                follow_user.save()       
            
            return Unfollow(success=success, errorMessage=error_message)
        except:
            return Unfollow(success=False, errorMessage='Failed to unfollow the user')

class Mutation(graphene.ObjectType):
    follow = Follow.Field()
    unfollow = Unfollow.Field()