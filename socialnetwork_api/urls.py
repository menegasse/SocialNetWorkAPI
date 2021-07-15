from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt

from apps.api.schemas import user, follow, post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', csrf_exempt(
                        jwt_cookie(
                            GraphQLView.as_view(graphiql=True, schema=user.schema)
                        )
                    )
        ),
    path('follow', csrf_exempt(
                        jwt_cookie(
                            GraphQLView.as_view(graphiql=True, schema=follow.schema)
                        )
                    )
        ),
    path('post', csrf_exempt(
                        jwt_cookie(
                            GraphQLView.as_view(graphiql=True, schema=post.schema)
                        )
                    )
        ),
]
