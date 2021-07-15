import graphene 
from django.contrib.auth.models import User 
from graphql_jwt.shortcuts import  get_token
from django.contrib.auth.hashers import make_password, check_password



class Register(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()   

    success = graphene.Boolean()
    errorMessage = graphene.String()

    @staticmethod
    def data_validation(name, email, password) -> str:
        '''Return messages errors'''

        email_is_registered = User.objects.filter(email=email);

        if(email_is_registered):
            return "E-mail already registered"

        if(len(password) < 8):
            return "Password must be at least 8 characters long"

        return None


    @staticmethod
    def mutate(root, info, name, email, password):

        error_message = Register.data_validation(name, email, password)

        try:

            success = not error_message

            if(success):
                new_user = User( 
                    username= name,
                    email= email,
                    password= make_password(password),
                )
                new_user.save()

            return Register(success=success, errorMessage=error_message)
        except:
            return Register(success=False, errorMessage='Failed to register user')

class Login(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()   

    token = graphene.String()
    errorMessage = graphene.String()

    @staticmethod
    def mutate(root, info, email, password):

        try:
            searchUser = User.objects.filter(email=email).get();                
        except:
            searchUser = None
        finally:
            token = None
            error_message = "Incorrect email or password"

        if searchUser and check_password(password,searchUser.password):
                user = User(
                    username=searchUser.username,
                    email=searchUser.email,
                )

                token = get_token(user)
                error_message = None


        return Login(token=token, errorMessage=error_message)


class Mutation(graphene.ObjectType):
    login = Login.Field()
    register = Register.Field()