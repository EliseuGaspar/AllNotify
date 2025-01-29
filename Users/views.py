from typing import Optional
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from Users.serializers import (
    UserListSerializer, UserRegisterSerializer,
    UserLoginSerializer, UserEmptySerializer
)

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer
        elif self.action == "login":
            return UserLoginSerializer
        elif self.action == 'logout':
            return UserEmptySerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create" or self.action == "login":
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        password: Optional[str] = request.data.get("password")
        if password:
            request.data["password"] = make_password(password)
        return super().create(request, *args, **kwargs)

    @action(methods=["POST"], detail=False)
    def login(self, request, *args, **kwargs) -> Response:
        """"""
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(data={"error": "missing username and password"}, status=status.HTTP_412_PRECONDITION_FAILED)

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'name': {
                    'first': user.first_name,
                    'last': user.last_name
                }
            }
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        method="post",
        operation_summary="User logout",
        operation_description="Removes the user's authentication token, ending the session.",
        request_body=None,
        responses={
            200: openapi.Response(description="Successful logout", examples={"application/json": {"detail": "Successfully logged out."}}),
            400: openapi.Response(description="Logout error", examples={"application/json": {"error": "Error when deleting token"}}),
        },
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                description="Authentication token in the format 'Token <your_token_here>'",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    @action(methods=["POST"], detail=False)
    def logout(self, request, *args, **kwargs) -> Response:
        """
        Log out the user by deleting the authentication token.
        """
        user = request.user

        if not user.is_authenticated:
            return Response({"error": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

        token = getattr(user, 'auth_token', None)

        if token:
            token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

        return Response({"error": "No active session found."}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        
        if "password" in request.data:
            user.set_password(request.data["password"])
            user.save()
            return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)

        return super().partial_update(request, *args, **kwargs)

