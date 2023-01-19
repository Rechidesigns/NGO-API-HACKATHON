from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import permissions, status
from account.models import User
from .serializers import  LoginSerializer, LogoutSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.signals import user_logged_in
# Create your views here.


class LoginView(APIView):
    def post(self, request):
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(request, email = serializer.validated_data['email'], password = serializer.validated_data['password'])
            if user:
                if user.is_admin:
                    try:
                        refresh = RefreshToken.for_user(user)
                        user_details = {}
                        user_details['email'] = user.email
                        user_details['access_token'] = str(refresh.access_token)
                        user_details['refresh_token'] = str(refresh)
                        user_logged_in.send(sender=user.__class__,
                                            request=request, user=user)

                        data = {
                        'message' : "Admin Login successful",
                        'data' : user_details,
                        }
                        return Response(data, status=status.HTTP_200_OK)
                    except Exception as e:
                        raise e   
                else:
                    data = {
                        'message'  : "failed",
                        'errors': 'This Admin account is not active'
                        }
                    return Response(data, status=status.HTTP_403_FORBIDDEN)
            else:
                data = {
                    'message'  : "failed",
                    'errors': 'Please provide a valid email and password for the admin'
                    }
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)




class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Status": "Successfully logged out!"}, status=status.HTTP_204_NO_CONTENT)

